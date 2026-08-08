#!/usr/bin/env python3
"""Generate a tech-forward Yojna Connect pitch deck (PPTX) for TCS / government review."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt, Emu

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "YojnaConnect-TechPitch.pptx"

# Brand / tech palette (matches live product orange + enterprise slate)
NAVY = RGBColor(0x0B, 0x16, 0x28)
SLATE = RGBColor(0x11, 0x22, 0x3A)
CARD = RGBColor(0x16, 0x2A, 0x45)
ORANGE = RGBColor(0xFF, 0x8C, 0x42)
CYAN = RGBColor(0x2D, 0xD4, 0xBF)
WHITE = RGBColor(0xF8, 0xFA, 0xFC)
MUTED = RGBColor(0x94, 0xA3, 0xB8)
SOFT = RGBColor(0xCB, 0xD5, 0xE1)
GREEN = RGBColor(0x34, 0xD3, 0x99)
BLUE = RGBColor(0x38, 0xBD, 0xF8)
RED = RGBColor(0xF8, 0x71, 0x71)

W, H = Inches(13.333), Inches(7.5)


def set_run(run, size=18, bold=False, color=WHITE, font="Calibri"):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font
    rPr = run._r.get_or_add_rPr()
    latin = rPr.find(qn("a:latin"))
    if latin is None:
        latin = rPr.makeelement(qn("a:latin"), {})
        rPr.insert(0, latin)
    latin.set("typeface", font)


def add_bg(slide, color=NAVY):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    spTree = slide.shapes._spTree
    sp = shape._element
    spTree.remove(sp)
    spTree.insert(2, sp)
    return shape


def add_accent_bar(slide, top=0):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, top, W, Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ORANGE
    bar.line.fill.background()


def add_footer(slide, page, total=16):
    box = slide.shapes.add_textbox(Inches(0.5), Inches(7.05), Inches(10), Inches(0.3))
    p = box.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "YojanaConnect  ·  Live: yojnaconnect.prakharkr.online  ·  Confidential pitch"
    set_run(run, 10, False, MUTED)
    num = slide.shapes.add_textbox(Inches(11.8), Inches(7.05), Inches(1.2), Inches(0.3))
    p = num.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    run = p.add_run()
    run.text = f"{page:02d} / {total:02d}"
    set_run(run, 10, False, MUTED)


def textbox(slide, left, top, width, height, text, size=18, bold=False, color=WHITE, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    set_run(run, size, bold, color)
    return box


def multi_text(slide, left, top, width, height, lines, size=16, color=SOFT, bold=False, spacing=1.15):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(6)
        run = p.add_run()
        run.text = line
        set_run(run, size, bold, color)
    return box


def card(slide, left, top, width, height, fill=CARD):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = RGBColor(0x2A, 0x3F, 0x5F)
    shape.adjustments[0] = 0.08
    return shape


def pill(slide, left, top, width, height, text, fill=ORANGE, text_color=NAVY):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background()
    shape.adjustments[0] = 0.5
    tf = shape.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    set_run(run, 11, True, text_color)
    return shape


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    blank = prs.slide_layouts[6]
    total = 16

    # 1 Title
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    # side glow strip
    strip = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.18), H)
    strip.fill.solid()
    strip.fill.fore_color.rgb = ORANGE
    strip.line.fill.background()
    pill(s, Inches(0.7), Inches(1.5), Inches(2.6), Inches(0.38), "LIVE PRODUCT DEMO", ORANGE, NAVY)
    textbox(s, Inches(0.7), Inches(2.1), Inches(11), Inches(1.2), "YojanaConnect", 54, True, WHITE)
    textbox(
        s,
        Inches(0.7),
        Inches(3.2),
        Inches(11),
        Inches(0.8),
        "Enterprise-grade Welfare Scheme Discovery Platform",
        26,
        False,
        CYAN,
    )
    textbox(
        s,
        Inches(0.7),
        Inches(4.1),
        Inches(11),
        Inches(0.6),
        "Age-aware · Bilingual · REST + MySQL · Production URL live",
        18,
        False,
        MUTED,
    )
    textbox(s, Inches(0.7), Inches(5.2), Inches(11), Inches(0.4), "https://yojnaconnect.prakharkr.online/schemes", 20, True, ORANGE)
    textbox(s, Inches(0.7), Inches(5.8), Inches(11), Inches(0.35), "Technical Deep-Dive Pitch  ·  Tamil Nadu / Enterprise Review", 14, False, SOFT)
    add_footer(s, 1, total)

    # 2 Agenda
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.6), Inches(0.35), Inches(10), Inches(0.5), "Agenda", 32, True, WHITE)
    textbox(s, Inches(0.6), Inches(0.9), Inches(10), Inches(0.35), "What we will cover in this technical walkthrough", 14, False, MUTED)
    items = [
        ("01", "Problem → Solution", "Why scheme discovery fails citizens today"),
        ("02", "Live Architecture", "3-tier design, data flow, API contracts"),
        ("03", "Engineering Depth", "Stack, schema, filtering engine, i18n, bot"),
        ("04", "Enterprise Readiness", "Security, scale path, ops, TN pilot"),
        ("05", "Roadmap & Ask", "What ships next and how to partner"),
    ]
    for i, (n, t, d) in enumerate(items):
        top = Inches(1.5) + Inches(i * 0.95)
        card(s, Inches(0.6), top, Inches(12.1), Inches(0.85))
        textbox(s, Inches(0.85), top + Inches(0.18), Inches(1), Inches(0.5), n, 22, True, ORANGE)
        textbox(s, Inches(2.0), top + Inches(0.12), Inches(9), Inches(0.35), t, 18, True, WHITE)
        textbox(s, Inches(2.0), top + Inches(0.45), Inches(9.5), Inches(0.3), d, 13, False, MUTED)
    add_footer(s, 2, total)

    # 3 Problem
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.5), "The Problem: Discovery Gap", 30, True, WHITE)
    textbox(s, Inches(0.6), Inches(0.95), Inches(12), Inches(0.35), "India runs 400+ welfare schemes — eligibility still fails at the first click", 15, False, MUTED)
    problems = [
        ("Fragmented Sources", "Ministry sites, PDFs, state portals — no unified citizen entry"),
        ("Complex Eligibility", "Bureaucratic language blocks rural / first-time digital users"),
        ("Language Barrier", "English-first UX excludes large Hindi / regional audiences"),
        ("Zero Personalization", "Users browse catalogs; systems rarely start from life-stage"),
    ]
    for i, (t, d) in enumerate(problems):
        col = i % 2
        row = i // 2
        left = Inches(0.6) + Inches(col * 6.3)
        top = Inches(1.6) + Inches(row * 2.3)
        card(s, left, top, Inches(6.0), Inches(2.05))
        textbox(s, left + Inches(0.35), top + Inches(0.35), Inches(5.3), Inches(0.45), t, 20, True, ORANGE)
        textbox(s, left + Inches(0.35), top + Inches(0.95), Inches(5.3), Inches(0.8), d, 15, False, SOFT)
    add_footer(s, 3, total)

    # 4 Solution
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.5), "Solution: Life-Stage First Discovery", 28, True, WHITE)
    textbox(
        s,
        Inches(0.6),
        Inches(0.95),
        Inches(12),
        Inches(0.4),
        "From “which yojana am I eligible for?” → shortlist + official apply path in under 60 seconds",
        15,
        False,
        MUTED,
    )
    steps = [
        ("1", "AGE SIGNAL", "Citizen sets age → Teen / YA / Middle / Senior"),
        ("2", "FILTER ENGINE", "Sector · Income · Keyword · Central/State"),
        ("3", "SCHEME INTEL", "Eligibility · Docs · Steps · Terms"),
        ("4", "OFFICIAL HANDOFF", "Apply Now → government portal (no PII)"),
    ]
    for i, (n, t, d) in enumerate(steps):
        left = Inches(0.45) + Inches(i * 3.2)
        card(s, left, Inches(1.8), Inches(3.0), Inches(3.8))
        textbox(s, left + Inches(0.25), Inches(2.1), Inches(2.5), Inches(0.5), n, 36, True, ORANGE)
        textbox(s, left + Inches(0.25), Inches(2.9), Inches(2.5), Inches(0.5), t, 14, True, CYAN)
        textbox(s, left + Inches(0.25), Inches(3.6), Inches(2.5), Inches(1.5), d, 14, False, SOFT)
    add_footer(s, 4, total)

    # 5 Live product metrics + screenshot
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(8), Inches(0.45), "Live Product Snapshot", 28, True, WHITE)
    textbox(s, Inches(0.5), Inches(0.8), Inches(8), Inches(0.3), "Production: yojnaconnect.prakharkr.online/schemes", 13, False, ORANGE)
    metrics = [("159", "Total Schemes", ORANGE), ("39", "Central", BLUE), ("120", "State", GREEN), ("2", "Languages", CYAN)]
    for i, (v, l, c) in enumerate(metrics):
        left = Inches(0.5) + Inches(i * 2.05)
        card(s, left, Inches(1.25), Inches(1.9), Inches(1.35))
        textbox(s, left + Inches(0.1), Inches(1.4), Inches(1.7), Inches(0.55), v, 28, True, c, PP_ALIGN.CENTER)
        textbox(s, left + Inches(0.1), Inches(2.05), Inches(1.7), Inches(0.35), l, 11, False, MUTED, PP_ALIGN.CENTER)
    img = ASSETS / "yojna-schemes.png"
    if img.exists():
        s.shapes.add_picture(str(img), Inches(8.7), Inches(1.2), width=Inches(4.2))
    multi_text(
        s,
        Inches(0.5),
        Inches(2.9),
        Inches(8),
        Inches(3.5),
        [
            "✓ Age-personalized scheme grid with popularity ranking",
            "✓ Sector + income + keyword filters with live counts",
            "✓ Detail pages: eligibility, documents, how-to-apply",
            "✓ WhatsApp share + official Apply Now handoff",
            "✓ YojanaBot guided assistant + EN / हिन्दी i18n",
            "✓ Responsive SPA — mobile-first civic UX",
        ],
        15,
        SOFT,
    )
    add_footer(s, 5, total)

    # 6 Product gallery
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.25), Inches(12), Inches(0.4), "Product Surfaces", 28, True, WHITE)
    shots = [
        ("yojna-home.png", "Age Entry"),
        ("yojna-detail.png", "Scheme Detail"),
        ("yojna-extra.png", "YojanaBot"),
        ("yojna-language-hindi.png", "Hindi UI"),
    ]
    for i, (name, label) in enumerate(shots):
        left = Inches(0.35) + Inches(i * 3.25)
        path = ASSETS / name
        if path.exists():
            s.shapes.add_picture(str(path), left, Inches(1.0), width=Inches(3.05))
        textbox(s, left, Inches(6.55), Inches(3.05), Inches(0.3), label, 13, True, CYAN, PP_ALIGN.CENTER)
    add_footer(s, 6, total)

    # 7 Architecture
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "System Architecture", 28, True, WHITE)
    textbox(s, Inches(0.5), Inches(0.8), Inches(12), Inches(0.3), "Classic 3-tier — optimized for clarity, auditability, and gov IT familiarity", 14, False, MUTED)
    layers = [
        ("PRESENTATION", "React 19 · TypeScript · Vite\nTanStack Query · Wouter · i18next\nTailwind v4 · Radix / shadcn", ORANGE),
        ("APPLICATION", "Node.js · Express 5 REST\nControllers · parameterized SQL\nJSON field parsers · CORS", CYAN),
        ("DATA", "MySQL 8+\nJSON columns for age/sectors\nPopularity score ranking\nConnection pooling", GREEN),
    ]
    for i, (t, d, c) in enumerate(layers):
        top = Inches(1.35) + Inches(i * 1.7)
        shape = card(s, Inches(1.5), top, Inches(10.3), Inches(1.5))
        textbox(s, Inches(1.8), top + Inches(0.2), Inches(3), Inches(0.4), t, 16, True, c)
        multi_text(s, Inches(5.0), top + Inches(0.2), Inches(6.4), Inches(1.2), d.split("\n"), 14, SOFT)
    add_footer(s, 7, total)

    # 8 Data flow
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "Request Path & Filtering Engine", 28, True, WHITE)
    flow = [
        "Browser → React SPA (ageGroup in localStorage)",
        "GET /api/schemes?ageGroup&sector&incomeLimit&search",
        "Express controller builds parameterized WHERE clause",
        "MySQL: JSON_CONTAINS(age_groups) + income brackets + LIKE",
        "ORDER BY popularity_score → JSON parse → SchemeCards",
        "Detail: /api/schemes/:id → Apply Now = official_link",
    ]
    for i, line in enumerate(flow):
        top = Inches(1.2) + Inches(i * 0.85)
        card(s, Inches(1.2), top, Inches(10.8), Inches(0.7))
        textbox(s, Inches(1.45), top + Inches(0.18), Inches(0.6), Inches(0.4), f"{i+1:02d}", 16, True, ORANGE)
        textbox(s, Inches(2.2), top + Inches(0.18), Inches(9.4), Inches(0.4), line, 15, False, WHITE)
    add_footer(s, 8, total)

    # 9 Tech stack matrix
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "Technology Stack — Production Choices", 26, True, WHITE)
    stacks = [
        ("Frontend", ["React 19", "TypeScript", "Vite", "TanStack Query", "Wouter", "i18next", "Framer Motion", "Tailwind CSS v4"]),
        ("Backend", ["Node.js", "Express 5", "mysql2 pool", "dotenv", "CORS", "REST JSON API", "pnpm monorepo", "Orval client"]),
        ("Data & Ops", ["MySQL 8 JSON", "Seed SQL", "Nginx reverse proxy", "Static SPA build", "Healthz endpoint", "Env-based config", "Mobile-first UX", "Live HTTPS"]),
    ]
    for i, (title, items) in enumerate(stacks):
        left = Inches(0.45) + Inches(i * 4.25)
        card(s, left, Inches(1.15), Inches(4.05), Inches(5.4))
        textbox(s, left + Inches(0.25), Inches(1.35), Inches(3.5), Inches(0.4), title, 18, True, ORANGE)
        for j, item in enumerate(items):
            textbox(s, left + Inches(0.35), Inches(1.95) + Inches(j * 0.5), Inches(3.4), Inches(0.4), f"▸  {item}", 14, False, SOFT)
    add_footer(s, 9, total)

    # 10 API contracts
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "API Surface — Contract Design", 28, True, WHITE)
    textbox(s, Inches(0.5), Inches(0.85), Inches(12), Inches(0.3), "Read-optimized REST — clean for CSC apps, WhatsApp bots, or state portals later", 14, False, MUTED)
    apis = [
        ("GET", "/api/healthz", "Liveness probe"),
        ("GET", "/api/schemes", "Filtered list (age, sector, income, search, state)"),
        ("GET", "/api/schemes/:id", "Full scheme document"),
        ("GET", "/api/schemes/:id/related", "Related / popular adjacency"),
        ("GET", "/api/schemes/popular", "Top-N by popularity_score"),
        ("GET", "/api/schemes/stats", "Aggregate KPIs for dashboard"),
        ("GET", "/api/sectors", "Sector taxonomy (+ age filter)"),
    ]
    for i, (m, path, desc) in enumerate(apis):
        top = Inches(1.3) + Inches(i * 0.7)
        pill(s, Inches(0.6), top + Inches(0.08), Inches(0.9), Inches(0.4), m, GREEN, NAVY)
        textbox(s, Inches(1.7), top + Inches(0.1), Inches(5.5), Inches(0.4), path, 15, True, CYAN)
        textbox(s, Inches(7.3), top + Inches(0.1), Inches(5.3), Inches(0.4), desc, 14, False, SOFT)
    add_footer(s, 10, total)

    # 11 Data model
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "Data Model — Flexible Scheme Knowledge Base", 26, True, WHITE)
    card(s, Inches(0.5), Inches(1.15), Inches(6.1), Inches(5.3))
    textbox(s, Inches(0.8), Inches(1.35), Inches(5.5), Inches(0.4), "schemes", 18, True, ORANGE)
    multi_text(
        s,
        Inches(0.8),
        Inches(1.9),
        Inches(5.5),
        Inches(4.3),
        [
            "id · name · name_hindi · ministry",
            "age_groups (JSON) · sectors (JSON)",
            "income_limit · categories · benefit",
            "eligibility / documents (JSON arrays)",
            "how_to_apply · official_link · deadline",
            "terms_and_conditions · tags",
            "is_state · state · popularity_score",
        ],
        14,
        SOFT,
    )
    card(s, Inches(6.9), Inches(1.15), Inches(5.9), Inches(2.4))
    textbox(s, Inches(7.2), Inches(1.35), Inches(5.3), Inches(0.4), "sectors", 18, True, CYAN)
    multi_text(
        s,
        Inches(7.2),
        Inches(1.9),
        Inches(5.3),
        Inches(1.4),
        ["sector_id · name · name_hindi", "age_groups (JSON) · icon"],
        14,
        SOFT,
    )
    card(s, Inches(6.9), Inches(3.8), Inches(5.9), Inches(2.65))
    textbox(s, Inches(7.2), Inches(4.0), Inches(5.3), Inches(0.4), "Why JSON columns?", 16, True, GREEN)
    multi_text(
        s,
        Inches(7.2),
        Inches(4.55),
        Inches(5.3),
        Inches(1.6),
        [
            "Multi-value age/sector tags without join explosion",
            "Fast iteration for scheme metadata",
            "Queryable via MySQL JSON_CONTAINS",
        ],
        13,
        SOFT,
    )
    add_footer(s, 11, total)

    # 12 Security
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "Security · Privacy · Trust Model", 28, True, WHITE)
    left_items = [
        "Discovery platform — not a benefit processor",
        "No Aadhaar / bank / KYC collected today",
        "Apply happens on official government portals",
        "Parameterized SQL — injection-resistant queries",
        "Secrets via environment variables",
        "HTTPS live deployment behind Nginx",
    ]
    right_items = [
        "Production hardening backlog:",
        "• Remove debug endpoints from public edge",
        "• Suppress stack traces in client errors",
        "• Tighten CORS to known origins",
        "• Rate-limit public GET APIs",
        "• Add WAF / CDN + audit logging",
        "• Auth only when bookmarks/admin ship",
    ]
    card(s, Inches(0.5), Inches(1.2), Inches(6.0), Inches(5.2))
    textbox(s, Inches(0.8), Inches(1.4), Inches(5.4), Inches(0.4), "Current Posture", 18, True, GREEN)
    multi_text(s, Inches(0.8), Inches(2.0), Inches(5.4), Inches(4.0), [f"✓  {x}" for x in left_items], 14, SOFT)
    card(s, Inches(6.8), Inches(1.2), Inches(6.0), Inches(5.2))
    textbox(s, Inches(7.1), Inches(1.4), Inches(5.4), Inches(0.4), "Enterprise Hardening Path", 18, True, ORANGE)
    multi_text(s, Inches(7.1), Inches(2.0), Inches(5.4), Inches(4.0), right_items, 14, SOFT)
    add_footer(s, 12, total)

    # 13 Scalability
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "Scale & Reliability Path", 28, True, WHITE)
    phases = [
        ("NOW", "SPA + Node API + MySQL", "Single region, read-heavy catalog, connection pool"),
        ("NEXT", "Cache + CDN", "Redis for popular lists, Cloudflare/Nginx static cache"),
        ("SCALE", "Horizontal API", "Stateless replicas behind LB; MySQL replica reads"),
        ("GOV", "Managed hosting", "NIC / state DC / Kubernetes; observability + SLOs"),
    ]
    for i, (p, t, d) in enumerate(phases):
        left = Inches(0.4) + Inches(i * 3.2)
        card(s, left, Inches(1.5), Inches(3.05), Inches(4.4))
        textbox(s, left + Inches(0.25), Inches(1.8), Inches(2.5), Inches(0.4), p, 16, True, ORANGE)
        textbox(s, left + Inches(0.25), Inches(2.5), Inches(2.5), Inches(1.0), t, 16, True, WHITE)
        textbox(s, left + Inches(0.25), Inches(3.7), Inches(2.5), Inches(1.8), d, 13, False, MUTED)
    add_footer(s, 13, total)

    # 14 Differentiation
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "Differentiation vs Generic Portals", 26, True, WHITE)
    rows = [
        ("Life-stage entry", "Age → personalized shortlist (not ministry-first browsing)"),
        ("Unified UX", "Eligibility + docs + steps + official link in one flow"),
        ("Bilingual native", "EN / HI UI + Hindi scheme names in data model"),
        ("In-product guide", "YojanaBot for high-frequency scheme FAQs"),
        ("Extensible API", "Same REST can power CSC kiosks / WhatsApp later"),
        ("TN-ready story", "State layer + Tamil localization as pilot upgrade"),
    ]
    for i, (t, d) in enumerate(rows):
        top = Inches(1.15) + Inches(i * 0.85)
        card(s, Inches(0.6), top, Inches(12.1), Inches(0.75))
        textbox(s, Inches(0.9), top + Inches(0.2), Inches(3.3), Inches(0.4), t, 15, True, CYAN)
        textbox(s, Inches(4.4), top + Inches(0.2), Inches(8), Inches(0.4), d, 14, False, SOFT)
    add_footer(s, 14, total)

    # 15 TN Roadmap
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    textbox(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.45), "Tamil Nadu Pilot Roadmap", 28, True, WHITE)
    phases = [
        ("Phase 1", "Localize", "Tamil UI strings\nTop TN schemes seed\nContent QA with dept sources"),
        ("Phase 2", "Pilot", "1–2 districts / CSC\nDiscovery KPIs\nFeedback loop"),
        ("Phase 3", "Operate", "Admin CMS\nAnalytics dashboard\nSLA + hosting on gov infra"),
    ]
    for i, (ph, t, d) in enumerate(phases):
        left = Inches(0.6) + Inches(i * 4.2)
        card(s, left, Inches(1.4), Inches(3.95), Inches(4.5))
        textbox(s, left + Inches(0.3), Inches(1.7), Inches(3.3), Inches(0.4), ph, 14, True, ORANGE)
        textbox(s, left + Inches(0.3), Inches(2.3), Inches(3.3), Inches(0.5), t, 24, True, WHITE)
        multi_text(s, left + Inches(0.3), Inches(3.2), Inches(3.3), Inches(2.2), d.split("\n"), 15, SOFT)
    add_footer(s, 15, total)

    # 16 Close
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    strip = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.18), H)
    strip.fill.solid()
    strip.fill.fore_color.rgb = ORANGE
    strip.line.fill.background()
    pill(s, Inches(0.7), Inches(1.6), Inches(2.4), Inches(0.38), "THE ASK", ORANGE, NAVY)
    textbox(s, Inches(0.7), Inches(2.2), Inches(11.5), Inches(0.9), "Pilot YojanaConnect for Tamil Nadu", 34, True, WHITE)
    multi_text(
        s,
        Inches(0.7),
        Inches(3.3),
        Inches(11.5),
        Inches(2.2),
        [
            "1. Verified TN scheme content + Tamil language pack",
            "2. Preferred hosting guidance (state DC / cloud)",
            "3. CSC / district discovery pilot with measurable KPIs",
        ],
        18,
        SOFT,
    )
    textbox(s, Inches(0.7), Inches(5.5), Inches(11.5), Inches(0.4), "https://yojnaconnect.prakharkr.online/schemes", 20, True, ORANGE)
    textbox(s, Inches(0.7), Inches(6.1), Inches(11.5), Inches(0.35), "Thank you — open for architecture deep-dive & live walkthrough", 14, False, MUTED)
    add_footer(s, 16, total)

    prs.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
