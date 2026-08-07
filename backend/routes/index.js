import { Router } from "express";
import healthRoutes from "./healthRoutes.js";
import sectorsRoutes from "./sectorsRoutes.js";
import schemesRoutes, { debugParse } from "./schemesRoutes.js";

const router = Router();

router.use("/healthz", healthRoutes);
router.use("/sectors", sectorsRoutes);
router.get("/debug/parse/:id", debugParse);
router.use("/schemes", schemesRoutes);

export default router;
