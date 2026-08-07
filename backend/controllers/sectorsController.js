import { pool } from "../config/database.js";
import { parseField } from "../utils/parseFields.js";

function mapSectorRow(row) {
  return {
    id: row.sector_id,
    name: row.name,
    nameHindi: row.name_hindi,
    ageGroups: parseField(row.age_groups),
    icon: row.icon,
  };
}

export async function listSectors(req, res) {
  try {
    const { ageGroup } = req.query;

    let sql = "SELECT * FROM sectors";
    const params = [];

    if (ageGroup) {
      sql += " WHERE JSON_CONTAINS(age_groups, JSON_QUOTE(?))";
      params.push(String(ageGroup));
    }

    sql += " ORDER BY name";

    const [rows] = await pool.query(sql, params);
    return res.json(rows.map(mapSectorRow));
  } catch (err) {
    console.error("Sectors Error:", err);
    return res.status(500).json({
      message: err?.message ?? "Internal Server Error",
      stack: err?.stack,
    });
  }
}
