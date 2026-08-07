import { Router } from "express";
import { listSectors } from "../controllers/sectorsController.js";

const router = Router();

router.get("/", listSectors);

export default router;
