#!/usr/bin/env python3
"""Generate a clean, valid YojanaConnect technical pitch PPTX."""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt, Emu

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "YojnaConnect-TechPitch.pptx"

NAVY = RGBColor(0x0B, 0x16, 0x28)
CARD = RGBColor(0x16, 0x2A, 0x45)
ORANGE = RGBColor(0xFF, 0x8C, 0x42)
CYAN = RGBColor(0x2D, 0xD4, 0xBF)
WHITE = RGBColor(0xF8, 0xFA, 0xFC)
MUTED = RGBColor(0x94, 0xA3, 0xB8)
SOFT = RGBColor(0xCB, 0xD5, 0xE1)
GREEN = RGBColor(0x34, 0xD3, 0x99)
BLUE = RGBColor(0x38, 0xBD, 0xF8)
LINE = RGBColor(0x2A, 0x3F, 0x5F)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
TOTAL = 16


def style_run(run, size=16, bold=False, color=WHITE, name="Calibri"):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = name


def add_bg(slide, color=NAVY):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    # send to back
    sp = shape._element
    slide.shapes._spTree.remove(sp)
    slide.shapes._spTree.insert(2, sp)


def add_top_bar(slide):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ORANGE
    bar.line.fill.background()


def add_side_bar(slide):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.16), SLIDE_H)
    bar.fill.solid()
    bar.fill.fore_color.rgb = ORANGE
    bar.line.fill.background()


def add_footer(slide, page: int):
    left = slide.shapes.add_textbox(Inches(0.5), Inches(7.08), Inches(10.5), Inches(0.28))
    p = left.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "YojanaConnect  |  https://yojnaconnect.prakharkr.online/schemes  |  Technical Pitch"
    style_run(run, 10, False, MUTED)

    right = slide.shapes.add_textbox(Inches(11.7), Inches(7.08), Inches(1.3), Inches(0.28))
    p = right.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    run = p.add_run()
    run.text = f"{page:02d}/{TOTAL:02d}"
    style_run(run, 10, False, MUTED)


def add_text(
    slide,
    left,
    top,
    width,
    height,
    text,
    size=16,
    bold=False,
    color=WHITE,
    align=PP_ALIGN.LEFT,
):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    style_run(run, size, bold, color)
    return box


def add_lines(slide, left, top, width, height, lines, size=14, color=SOFT, bold=False):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(4)
        run = p.add_run()
        run.text = line
        style_run(run, size, bold, color)
    return box


def add_card(slide, left, top, width, height, fill=CARD):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = LINE
    try:
        shape.adjustments[0] = 0.08
    except Exception:
        pass
    return shape


def add_pill(slide, left, top, width, height, text, fill=ORANGE, text_color=NAVY):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background()
    try:
        shape.adjustments[0] = 0.5
    except Exception:
        pass
    tf = shape.text_frame
    tf.word_wrap = False
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    run = tf.paragraphs[0].add_run()
    run.text = text
    style_run(run, 11, True, text_color)
    return shape


def maybe_picture(slide, path: Path, left, top, width):
    if path.exists():
        slide.shapes.add_picture(str(path), left, top, width=width)
        return True
    return False


def new_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)
    add_top_bar(slide)
    return slide


def build():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # 1 Title
    s = new_slide(prs)
    add_side_bar(s)
    add_pill(s, Inches(0.7), Inches(1.55), Inches(2.5), Inches(0.36), "LIVE PRODUCT")
    add_text(s, Inches(0.7), Inches(2.15), Inches(12), Inches(0.9), "YojanaConnect", 48, True, WHITE)
    add_text(
        s,
        Inches(0.7),
        Inches(3.15),
        Inches(12),
        Inches(0.5),
        "Enterprise-grade Welfare Scheme Discovery Platform",
        24,
        False,
        CYAN,
    )
    add_text(
        s,
        Inches(0.7),
        Inches(3.85),
        Inches(12),
        Inches(0.4),
        "Age-aware  ·  Bilingual EN/HI  ·  React + Express + MySQL  ·  Production live",
        16,
        False,
        MUTED,
    )
    add_text(
        s,
        Inches(0.7),
        Inches(4.7),
        Inches(12),
        Inches(0.4),
        "https://yojnaconnect.prakharkr.online/schemes",
        20,
        True,
        ORANGE,
    )
    add_text(
        s,
        Inches(0.7),
        Inches(5.4),
        Inches(12),
        Inches(0.35),
        "Technical Pitch for Tamil Nadu / Enterprise Review",
        14,
        False,
        SOFT,
    )
    add_footer(s, 1)

    # 2 Agenda
    s = new_slide(prs)
    add_text(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.5), "Agenda", 32, True)
    add_text(s, Inches(0.6), Inches(0.95), Inches(12), Inches(0.3), "Technical walkthrough for first-impact pitching", 14, False, MUTED)
    agenda = [
        ("01", "Problem to Solution", "Why scheme discovery fails and how we fix it"),
        ("02", "Live Product", "159 schemes, bilingual UX, real production URL"),
        ("03", "Architecture", "React SPA, Express REST API, MySQL knowledge base"),
        ("04", "Engineering Depth", "Filters, APIs, schema, Node/Express request path"),
        ("05", "Trust and Pilot Ask", "Security, scale path, Tamil Nadu next steps"),
    ]
    for i, (n, t, d) in enumerate(agenda):
        top = Inches(1.45) + Inches(i * 0.95)
        add_card(s, Inches(0.6), top, Inches(12.1), Inches(0.85))
        add_text(s, Inches(0.9), top + Inches(0.2), Inches(1.0), Inches(0.45), n, 22, True, ORANGE)
        add_text(s, Inches(2.1), top + Inches(0.12), Inches(10), Inches(0.35), t, 18, True, WHITE)
        add_text(s, Inches(2.1), top + Inches(0.45), Inches(10), Inches(0.3), d, 13, False, MUTED)
    add_footer(s, 2)

    # 3 Problem
    s = new_slide(prs)
    add_text(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "The Problem: Discovery Gap", 30, True)
    add_text(
        s,
        Inches(0.6),
        Inches(0.95),
        Inches(12),
        Inches(0.3),
        "India runs 400+ welfare schemes, but eligible citizens still miss benefits",
        14,
        False,
        MUTED,
    )
    problems = [
        ("Fragmented Sources", "Ministry sites, PDFs, and state portals with no single citizen entry point"),
        ("Complex Eligibility", "Hard bureaucratic language blocks first-time and rural digital users"),
        ("Language Barrier", "English-first experiences exclude large Hindi and regional audiences"),
        ("No Personalization", "Users browse catalogs instead of starting from life stage"),
    ]
    for i, (t, d) in enumerate(problems):
        col, row = i % 2, i // 2
        left = Inches(0.6) + Inches(col * 6.3)
        top = Inches(1.55) + Inches(row * 2.35)
        add_card(s, left, top, Inches(6.0), Inches(2.15))
        add_text(s, left + Inches(0.35), top + Inches(0.35), Inches(5.3), Inches(0.4), t, 20, True, ORANGE)
        add_text(s, left + Inches(0.35), top + Inches(1.0), Inches(5.3), Inches(0.85), d, 15, False, SOFT)
    add_footer(s, 3)

    # 4 Solution
    s = new_slide(prs)
    add_text(s, Inches(0.6), Inches(0.35), Inches(12), Inches(0.45), "Solution: Life-Stage First Discovery", 28, True)
    add_text(
        s,
        Inches(0.6),
        Inches(0.95),
        Inches(12),
        Inches(0.35),
        "From “Which yojana am I eligible for?” to a shortlist and official apply path in under 60 seconds",
        14,
        False,
        MUTED,
    )
    steps = [
        ("1", "AGE SIGNAL", "Citizen sets age. Mapped to Teen, Young Adult, Middle Age, or Senior."),
        ("2", "FILTER ENGINE", "Sector, income, keyword, and central/state filters refine results."),
        ("3", "SCHEME INTEL", "Eligibility, documents, steps, and terms shown on one page."),
        ("4", "OFFICIAL HANDOFF", "Apply Now opens the government portal. No Aadhaar stored by us."),
    ]
    for i, (n, t, d) in enumerate(steps):
        left = Inches(0.45) + Inches(i * 3.2)
        add_card(s, left, Inches(1.7), Inches(3.05), Inches(4.0))
        add_text(s, left + Inches(0.25), Inches(2.0), Inches(2.5), Inches(0.5), n, 34, True, ORANGE)
        add_text(s, left + Inches(0.25), Inches(2.8), Inches(2.5), Inches(0.4), t, 14, True, CYAN)
        add_text(s, left + Inches(0.25), Inches(3.5), Inches(2.5), Inches(1.8), d, 14, False, SOFT)
    add_footer(s, 4)

    # 5 Live metrics
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(8), Inches(0.4), "Live Product Snapshot", 28, True)
    add_text(
        s,
        Inches(0.5),
        Inches(0.8),
        Inches(8),
        Inches(0.3),
        "Production: yojnaconnect.prakharkr.online/schemes",
        13,
        False,
        ORANGE,
    )
    metrics = [
        ("159", "Total Schemes", ORANGE),
        ("39", "Central", BLUE),
        ("120", "State", GREEN),
        ("2", "Languages", CYAN),
    ]
    for i, (v, label, color) in enumerate(metrics):
        left = Inches(0.5) + Inches(i * 2.05)
        add_card(s, left, Inches(1.25), Inches(1.9), Inches(1.35))
        add_text(s, left + Inches(0.1), Inches(1.4), Inches(1.7), Inches(0.55), v, 28, True, color, PP_ALIGN.CENTER)
        add_text(s, left + Inches(0.1), Inches(2.05), Inches(1.7), Inches(0.35), label, 11, False, MUTED, PP_ALIGN.CENTER)

    maybe_picture(s, ASSETS / "yojna-schemes.png", Inches(8.7), Inches(1.2), Inches(4.2))
    add_lines(
        s,
        Inches(0.5),
        Inches(2.95),
        Inches(8),
        Inches(3.5),
        [
            "Age-personalized scheme grid with popularity ranking",
            "Sector, income, and keyword filters with live counts",
            "Detail pages: eligibility, documents, how-to-apply",
            "WhatsApp share and official Apply Now handoff",
            "YojanaBot guided assistant and English / Hindi UI",
            "Responsive SPA built for mobile-first civic use",
        ],
        15,
        SOFT,
    )
    add_footer(s, 5)

    # 6 Product surfaces
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.25), Inches(12), Inches(0.4), "Product Surfaces", 28, True)
    shots = [
        ("yojna-home.png", "Age Entry"),
        ("yojna-detail.png", "Scheme Detail"),
        ("yojna-extra.png", "YojanaBot"),
        ("yojna-language-hindi.png", "Hindi UI"),
    ]
    for i, (name, label) in enumerate(shots):
        left = Inches(0.35) + Inches(i * 3.25)
        ok = maybe_picture(s, ASSETS / name, left, Inches(1.0), Inches(3.05))
        if not ok:
            add_card(s, left, Inches(1.0), Inches(3.05), Inches(5.2))
        add_text(s, left, Inches(6.55), Inches(3.05), Inches(0.3), label, 13, True, CYAN, PP_ALIGN.CENTER)
    add_footer(s, 6)

    # 7 Architecture
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "System Architecture", 28, True)
    add_text(
        s,
        Inches(0.5),
        Inches(0.85),
        Inches(12),
        Inches(0.3),
        "Classic 3-tier design: clear, maintainable, familiar to government IT teams",
        14,
        False,
        MUTED,
    )
    layers = [
        ("PRESENTATION", "React 19, TypeScript, Vite\nTanStack Query, Wouter, i18next\nTailwind CSS v4, Radix / shadcn UI", ORANGE),
        ("APPLICATION", "Node.js and Express 5 REST API\nControllers with parameterized SQL\nJSON field parsers and CORS", CYAN),
        ("DATA", "MySQL 8+ scheme knowledge base\nJSON columns for age groups and sectors\nPopularity score ranking and pooling", GREEN),
    ]
    for i, (title, body, color) in enumerate(layers):
        top = Inches(1.4) + Inches(i * 1.7)
        add_card(s, Inches(1.4), top, Inches(10.5), Inches(1.5))
        add_text(s, Inches(1.7), top + Inches(0.25), Inches(3.2), Inches(0.4), title, 16, True, color)
        add_lines(s, Inches(5.1), top + Inches(0.25), Inches(6.4), Inches(1.15), body.split("\n"), 14, SOFT)
    add_footer(s, 7)

    # 8 Node Express explanation
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "How Node.js and Express Work Here", 26, True)
    add_text(
        s,
        Inches(0.5),
        Inches(0.85),
        Inches(12),
        Inches(0.3),
        "Express is the bridge between the citizen UI and the scheme database",
        14,
        False,
        MUTED,
    )
    flow = [
        "Citizen selects age in React UI",
        "Frontend calls GET /api/schemes?ageGroup=youngAdult",
        "Express route sends request to schemes controller",
        "Controller builds safe SQL filters and queries MySQL",
        "API returns JSON scheme list to the browser",
        "React renders cards; Apply Now opens official portal",
    ]
    for i, line in enumerate(flow):
        top = Inches(1.35) + Inches(i * 0.8)
        add_card(s, Inches(1.2), top, Inches(10.9), Inches(0.68))
        add_text(s, Inches(1.45), top + Inches(0.16), Inches(0.7), Inches(0.4), f"{i+1:02d}", 16, True, ORANGE)
        add_text(s, Inches(2.3), top + Inches(0.16), Inches(9.4), Inches(0.4), line, 15, False, WHITE)
    add_footer(s, 8)

    # 9 Filter engine
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "Request Path and Filtering Engine", 26, True)
    points = [
        "Browser stores ageGroup in localStorage after age selection",
        "GET /api/schemes with ageGroup, sector, incomeLimit, search",
        "Express builds parameterized WHERE clause (no string-concat SQL)",
        "MySQL uses JSON_CONTAINS, income brackets, and LIKE search",
        "Results sorted by popularity_score, then JSON fields are parsed",
        "Detail page uses GET /api/schemes/:id; Apply uses official_link",
    ]
    for i, line in enumerate(points):
        top = Inches(1.2) + Inches(i * 0.85)
        add_card(s, Inches(1.1), top, Inches(11.1), Inches(0.72))
        add_text(s, Inches(1.35), top + Inches(0.18), Inches(0.6), Inches(0.4), f"{i+1:02d}", 16, True, ORANGE)
        add_text(s, Inches(2.15), top + Inches(0.18), Inches(9.7), Inches(0.4), line, 15, False, WHITE)
    add_footer(s, 9)

    # 10 Tech stack
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "Technology Stack", 28, True)
    stacks = [
        ("Frontend", ["React 19", "TypeScript", "Vite", "TanStack Query", "Wouter", "i18next", "Framer Motion", "Tailwind CSS v4"]),
        ("Backend", ["Node.js", "Express 5", "mysql2 pool", "dotenv", "CORS", "REST JSON API", "pnpm monorepo", "Typed API client"]),
        ("Data and Ops", ["MySQL 8 JSON", "Seed SQL catalog", "Nginx reverse proxy", "Static SPA build", "Healthz endpoint", "Env-based config", "HTTPS live deploy", "Mobile-first UX"]),
    ]
    for i, (title, items) in enumerate(stacks):
        left = Inches(0.45) + Inches(i * 4.25)
        add_card(s, left, Inches(1.15), Inches(4.05), Inches(5.35))
        add_text(s, left + Inches(0.25), Inches(1.35), Inches(3.5), Inches(0.4), title, 18, True, ORANGE)
        for j, item in enumerate(items):
            add_text(
                s,
                left + Inches(0.35),
                Inches(1.95) + Inches(j * 0.5),
                Inches(3.4),
                Inches(0.4),
                f">  {item}",
                14,
                False,
                SOFT,
            )
    add_footer(s, 10)

    # 11 API
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "API Surface", 28, True)
    add_text(
        s,
        Inches(0.5),
        Inches(0.85),
        Inches(12),
        Inches(0.3),
        "Read-optimized REST endpoints ready for web, CSC apps, or future WhatsApp bots",
        14,
        False,
        MUTED,
    )
    apis = [
        ("GET", "/api/healthz", "Health / liveness probe"),
        ("GET", "/api/schemes", "Filtered list by age, sector, income, search, state"),
        ("GET", "/api/schemes/:id", "Full scheme document"),
        ("GET", "/api/schemes/:id/related", "Related scheme suggestions"),
        ("GET", "/api/schemes/popular", "Top schemes by popularity score"),
        ("GET", "/api/schemes/stats", "Total, central, and state counts"),
        ("GET", "/api/sectors", "Sector taxonomy with optional age filter"),
    ]
    for i, (method, path, desc) in enumerate(apis):
        top = Inches(1.3) + Inches(i * 0.7)
        add_pill(s, Inches(0.6), top + Inches(0.08), Inches(0.9), Inches(0.4), method, GREEN, NAVY)
        add_text(s, Inches(1.7), top + Inches(0.1), Inches(5.5), Inches(0.4), path, 15, True, CYAN)
        add_text(s, Inches(7.3), top + Inches(0.1), Inches(5.3), Inches(0.4), desc, 14, False, SOFT)
    add_footer(s, 11)

    # 12 Data model
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "Data Model", 28, True)
    add_card(s, Inches(0.5), Inches(1.1), Inches(6.1), Inches(5.3))
    add_text(s, Inches(0.8), Inches(1.3), Inches(5.5), Inches(0.4), "schemes", 18, True, ORANGE)
    add_lines(
        s,
        Inches(0.8),
        Inches(1.85),
        Inches(5.5),
        Inches(4.2),
        [
            "id, name, name_hindi, ministry",
            "age_groups (JSON), sectors (JSON)",
            "income_limit, categories, benefit",
            "eligibility and documents (JSON)",
            "how_to_apply, official_link, deadline",
            "terms_and_conditions, tags",
            "is_state, state, popularity_score",
        ],
        14,
        SOFT,
    )
    add_card(s, Inches(6.9), Inches(1.1), Inches(5.9), Inches(2.3))
    add_text(s, Inches(7.2), Inches(1.3), Inches(5.3), Inches(0.4), "sectors", 18, True, CYAN)
    add_lines(
        s,
        Inches(7.2),
        Inches(1.85),
        Inches(5.3),
        Inches(1.3),
        ["sector_id, name, name_hindi", "age_groups (JSON), icon"],
        14,
        SOFT,
    )
    add_card(s, Inches(6.9), Inches(3.65), Inches(5.9), Inches(2.75))
    add_text(s, Inches(7.2), Inches(3.85), Inches(5.3), Inches(0.4), "Why JSON columns?", 16, True, GREEN)
    add_lines(
        s,
        Inches(7.2),
        Inches(4.4),
        Inches(5.3),
        Inches(1.7),
        [
            "Multi-value age and sector tags without heavy joins",
            "Fast iteration when scheme metadata changes",
            "Queryable with MySQL JSON_CONTAINS",
        ],
        13,
        SOFT,
    )
    add_footer(s, 12)

    # 13 Security
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "Security, Privacy, Trust", 28, True)
    add_card(s, Inches(0.5), Inches(1.15), Inches(6.0), Inches(5.2))
    add_text(s, Inches(0.8), Inches(1.35), Inches(5.4), Inches(0.4), "Current Posture", 18, True, GREEN)
    add_lines(
        s,
        Inches(0.8),
        Inches(1.95),
        Inches(5.4),
        Inches(4.0),
        [
            "Discovery platform, not a benefit processor",
            "No Aadhaar, bank, or KYC data collected",
            "Applications happen on official portals",
            "Parameterized SQL against injection risk",
            "Secrets loaded from environment variables",
            "HTTPS production deployment behind Nginx",
        ],
        14,
        SOFT,
    )
    add_card(s, Inches(6.8), Inches(1.15), Inches(6.0), Inches(5.2))
    add_text(s, Inches(7.1), Inches(1.35), Inches(5.4), Inches(0.4), "Hardening Path", 18, True, ORANGE)
    add_lines(
        s,
        Inches(7.1),
        Inches(1.95),
        Inches(5.4),
        Inches(4.0),
        [
            "Remove public debug endpoints",
            "Hide stack traces from client errors",
            "Tighten CORS to known origins",
            "Rate-limit public GET APIs",
            "Add WAF/CDN and audit logging",
            "Add auth when bookmarks or admin ship",
        ],
        14,
        SOFT,
    )
    add_footer(s, 13)

    # 14 Scale
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "Scale and Reliability Path", 28, True)
    phases = [
        ("NOW", "SPA + Node API + MySQL", "Single region, read-heavy catalog, connection pooling"),
        ("NEXT", "Cache + CDN", "Redis for popular lists, edge cache for static assets"),
        ("SCALE", "Horizontal API", "Stateless replicas behind load balancer, DB read replicas"),
        ("GOV", "Managed hosting", "NIC or state data center, Kubernetes, SLOs and monitoring"),
    ]
    for i, (phase, title, desc) in enumerate(phases):
        left = Inches(0.4) + Inches(i * 3.2)
        add_card(s, left, Inches(1.45), Inches(3.05), Inches(4.5))
        add_text(s, left + Inches(0.25), Inches(1.75), Inches(2.5), Inches(0.35), phase, 16, True, ORANGE)
        add_text(s, left + Inches(0.25), Inches(2.4), Inches(2.5), Inches(1.0), title, 16, True, WHITE)
        add_text(s, left + Inches(0.25), Inches(3.7), Inches(2.5), Inches(1.8), desc, 13, False, MUTED)
    add_footer(s, 14)

    # 15 TN roadmap
    s = new_slide(prs)
    add_text(s, Inches(0.5), Inches(0.3), Inches(12), Inches(0.4), "Tamil Nadu Pilot Roadmap", 28, True)
    phases = [
        ("Phase 1", "Localize", "Tamil UI strings\nTop TN schemes content\nDepartment source QA"),
        ("Phase 2", "Pilot", "1 to 2 districts or CSC\nDiscovery KPIs\nCitizen feedback loop"),
        ("Phase 3", "Operate", "Admin CMS\nAnalytics dashboard\nGov hosting and SLA"),
    ]
    for i, (phase, title, body) in enumerate(phases):
        left = Inches(0.6) + Inches(i * 4.2)
        add_card(s, left, Inches(1.35), Inches(3.95), Inches(4.6))
        add_text(s, left + Inches(0.3), Inches(1.65), Inches(3.3), Inches(0.35), phase, 14, True, ORANGE)
        add_text(s, left + Inches(0.3), Inches(2.2), Inches(3.3), Inches(0.5), title, 24, True, WHITE)
        add_lines(s, left + Inches(0.3), Inches(3.1), Inches(3.3), Inches(2.3), body.split("\n"), 15, SOFT)
    add_footer(s, 15)

    # 16 Close
    s = new_slide(prs)
    add_side_bar(s)
    add_pill(s, Inches(0.7), Inches(1.55), Inches(2.0), Inches(0.36), "THE ASK")
    add_text(s, Inches(0.7), Inches(2.15), Inches(12), Inches(0.8), "Pilot YojanaConnect for Tamil Nadu", 32, True, WHITE)
    add_lines(
        s,
        Inches(0.7),
        Inches(3.2),
        Inches(11.5),
        Inches(2.0),
        [
            "1. Verified Tamil Nadu scheme content and Tamil language pack",
            "2. Preferred hosting guidance (state data center or cloud)",
            "3. CSC or district discovery pilot with clear KPIs",
        ],
        18,
        SOFT,
    )
    add_text(
        s,
        Inches(0.7),
        Inches(5.4),
        Inches(12),
        Inches(0.4),
        "https://yojnaconnect.prakharkr.online/schemes",
        20,
        True,
        ORANGE,
    )
    add_text(
        s,
        Inches(0.7),
        Inches(6.0),
        Inches(12),
        Inches(0.35),
        "Thank you. Ready for architecture deep-dive and live walkthrough.",
        14,
        False,
        MUTED,
    )
    add_footer(s, 16)

    if OUT.exists():
        OUT.unlink()
    prs.save(str(OUT))
    return OUT


def validate(path: Path):
    prs = Presentation(str(path))
    assert prs.slide_width == SLIDE_W
    assert prs.slide_height == SLIDE_H
    assert len(prs.slides) == TOTAL
    # ensure every slide has at least one shape and readable text
    for i, slide in enumerate(prs.slides, start=1):
        assert len(slide.shapes) > 0, f"slide {i} empty"
    # zip integrity
    import zipfile

    with zipfile.ZipFile(path, "r") as zf:
        bad = zf.testzip()
        assert bad is None, f"corrupt zip member: {bad}"
        names = zf.namelist()
        assert "[Content_Types].xml" in names
        assert "ppt/presentation.xml" in names
    size = path.stat().st_size
    assert size > 100_000, f"file unexpectedly small: {size}"
    print(f"VALID: {path} ({size} bytes, {TOTAL} slides)")


if __name__ == "__main__":
    out = build()
    validate(out)
