export function parseField(value) {
  if (value === null || typeof value === "undefined") return [];

  if (Array.isArray(value)) return value;

  if (typeof value === "string") {
    const v = value.trim();
    if (!v) return [];

    try {
      const parsed = JSON.parse(v);

      if (Array.isArray(parsed)) return parsed;
      if (parsed && typeof parsed === "object") return [parsed];

      return [parsed];
    } catch {
      return [value];
    }
  }

  return [value];
}

export function parseSchemeJsonFields(scheme) {
  if (!scheme) return scheme;
  scheme.age_groups = parseField(scheme.age_groups);
  scheme.sectors = parseField(scheme.sectors);
  scheme.categories = parseField(scheme.categories);
  scheme.eligibility = parseField(scheme.eligibility);
  scheme.documents = parseField(scheme.documents);
  scheme.tags = parseField(scheme.tags);
  scheme.terms_and_conditions = parseField(scheme.terms_and_conditions);
  return scheme;
}
