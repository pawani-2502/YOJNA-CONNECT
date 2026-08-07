import { Router } from "express";
import {
  getSchemeById,
  debugParse,
  listSchemes,
  getPopularSchemes,
  getSchemesStats,
  getRelatedSchemes,
} from "../controllers/schemesController.js";

const router = Router();

router.get("/popular", getPopularSchemes);
router.get("/stats", getSchemesStats);
router.get("/:id/related", getRelatedSchemes);
router.get("/:id", getSchemeById);
router.get("/", listSchemes);

export { debugParse };
export default router;
