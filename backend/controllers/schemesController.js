import { pool } from "../config/database.js";
import { parseField, parseSchemeJsonFields } from "../utils/parseFields.js";

async function resolveSectorSlug(sector) {
  const value = String(sector);

  if (/^\d+$/.test(value)) {
    const [rows] = await pool.query(
      "SELECT sector_id FROM sectors WHERE id = ? LIMIT 1",
      [value]
    );
    return rows.length ? rows[0].sector_id : value;
  }

  return value;
}

function buildIncomeFilter(incomeLimit) {
  const n = Number(incomeLimit);
  if (Number.isNaN(n)) return null;

  // User-selected income brackets; show schemes where eligibility cap covers that bracket.
  // NULL income_limit means no income restriction.
  if (n <= 100000) {
    return {
      clause: "(income_limit IS NULL OR income_limit >= ?)",
      params: [100000],
    };
  }

  if (n <= 300000) {
    return {
      clause: "(income_limit IS NULL OR income_limit >= ?)",
      params: [300000],
    };
  }

  return {
    clause: "(income_limit IS NULL OR income_limit >= ?)",
    params: [800000],
  };
}

export async function getSchemeById(req, res) {
  try {
    const [rows] = await pool.query(
      "SELECT * FROM schemes WHERE id = ? LIMIT 1",
      [req.params.id]
    );

    if (!rows.length) {
      return res.status(404).json({ message: "Scheme not found" });
    }

    const scheme = rows[0];

    console.log("RAW ELIGIBILITY =", scheme.eligibility);
    console.log("RAW DOCUMENTS =", scheme.documents);
    console.log("RAW TERMS =", scheme.terms_and_conditions);

    return res.json(parseSchemeJsonFields({ ...scheme }));
  } catch (err) {
    console.error("SchemeDetail Error:", err);
    return res.status(500).json({
      message: err?.message ?? "Internal Server Error",
      stack: err?.stack,
    });
  }
}

export async function debugParse(req, res) {
  try {
    const [rows] = await pool.query(
      "SELECT eligibility, documents, terms_and_conditions FROM schemes WHERE id = ? LIMIT 1",
      [req.params.id]
    );
    if (!rows.length) return res.status(404).json({ message: "not found" });

    const r = rows[0];
    return res.json({
      raw: r,
      parsed: {
        eligibility: parseField(r.eligibility),
        documents: parseField(r.documents),
        terms_and_conditions: parseField(r.terms_and_conditions),
      },
    });
  } catch (err) {
    return res.status(500).json({ message: err?.message ?? "error" });
  }
}

export async function listSchemes(req, res) {
  try {
    const { ageGroup, sector, incomeLimit, isState, search } = req.query;

    const whereParts = [];
    const params = [];

    if (typeof isState !== "undefined") {
      const v = String(isState);
      whereParts.push("is_state = ?");
      params.push(v === "true" || v === "1" ? 1 : 0);
    }

    if (ageGroup) {
      whereParts.push("JSON_CONTAINS(age_groups, JSON_QUOTE(?))");
      params.push(String(ageGroup));
    }

    if (sector) {
      const sectorSlug = await resolveSectorSlug(sector);
      whereParts.push("JSON_CONTAINS(sectors, JSON_QUOTE(?))");
      params.push(sectorSlug);
    }

    if (incomeLimit) {
      const incomeFilter = buildIncomeFilter(incomeLimit);
      if (incomeFilter) {
        whereParts.push(incomeFilter.clause);
        params.push(...incomeFilter.params);
      }
    }

    if (search) {
      whereParts.push(
        "(name LIKE ? OR name_hindi LIKE ? OR ministry LIKE ? OR tags LIKE ?)"
      );
      const s = `%${String(search)}%`;
      params.push(s, s, s, s);
    }

    const whereSql = whereParts.length ? `WHERE ${whereParts.join(" AND ")}` : "";

    const [rows] = await pool.query(
      `SELECT * FROM schemes ${whereSql} ORDER BY popularity_score DESC`,
      params
    );

    return res.json(rows.map((r) => parseSchemeJsonFields({ ...r })));
  } catch (err) {
    console.error("Schemes Error:", err);
    return res.status(500).json({
      message: err?.message ?? "Internal Server Error",
      stack: err?.stack,
    });
  }
}

export async function getPopularSchemes(req, res) {
  try {
    const { limit, ageGroup } = req.query;
    const lim = Math.max(1, Math.min(Number(limit) || 6, 50));

    const whereParts = [];
    const params = [];

    if (ageGroup) {
      whereParts.push("JSON_CONTAINS(age_groups, JSON_QUOTE(?))");
      params.push(String(ageGroup));
    }

    const whereSql = whereParts.length ? `WHERE ${whereParts.join(" AND ")}` : "";

    const [rows] = await pool.query(
      `SELECT * FROM schemes ${whereSql} ORDER BY popularity_score DESC LIMIT ?`,
      [...params, lim]
    );

    return res.json(rows.map((r) => parseSchemeJsonFields({ ...r })));
  } catch (err) {
    console.error("Popular Error:", err);
    return res.status(500).json({
      message: err?.message ?? "Internal Server Error",
      stack: err?.stack,
    });
  }
}

export async function getSchemesStats(req, res) {
  try {
    const [[tot]] = await pool.query("SELECT COUNT(*) AS total FROM schemes");

    const [[central]] = await pool.query(
      "SELECT COUNT(*) AS centralSchemes FROM schemes WHERE is_state = 0"
    );

    const [[state]] = await pool.query(
      "SELECT COUNT(*) AS stateSchemes FROM schemes WHERE is_state = 1"
    );

    return res.json({
      total: tot.total,
      centralSchemes: central.centralSchemes,
      stateSchemes: state.stateSchemes,
    });
  } catch (err) {
    console.error("Stats Error:", err);
    return res.status(500).json({
      message: err?.message ?? "Internal Server Error",
      stack: err?.stack,
    });
  }
}

export async function getRelatedSchemes(req, res) {
  try {
    const [rows] = await pool.query(
      `SELECT *
       FROM schemes
       WHERE id != ?
       ORDER BY popularity_score DESC
       LIMIT 6`,
      [req.params.id]
    );

    return res.json(rows.map((r) => parseSchemeJsonFields({ ...r })));
  } catch (err) {
    console.error("Related Schemes Error:", err);
    return res.status(500).json({
      message: err?.message ?? "Internal Server Error",
    });
  }
}
