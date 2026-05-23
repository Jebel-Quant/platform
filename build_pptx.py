from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

NAVY       = RGBColor(0x0D, 0x1B, 0x2A)
BLUE       = RGBColor(0x1E, 0x40, 0xAF)
ACCENT     = RGBColor(0x60, 0xA5, 0xFA)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xE5, 0xE7, 0xEB)
MID_GRAY   = RGBColor(0x6B, 0x72, 0x80)

W = Inches(13.33)
H = Inches(7.5)


def new_prs():
    prs = Presentation()
    prs.slide_width  = W
    prs.slide_height = H
    return prs


def blank_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def fill_solid(shape, colour):
    shape.fill.solid()
    shape.fill.fore_color.rgb = colour


def add_rect(slide, l, t, w, h, colour):
    shape = slide.shapes.add_shape(1, l, t, w, h)
    fill_solid(shape, colour)
    shape.line.fill.background()
    return shape


def text_box(slide, text, l, t, w, h,
             size=18, bold=False, colour=WHITE,
             align=PP_ALIGN.LEFT, wrap=True):
    txBox = slide.shapes.add_textbox(l, t, w, h)
    txBox.word_wrap = wrap
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = colour
    return txBox


def add_bullets(slide, items, l, t, w, h, size=20, colour=LIGHT_GRAY):
    txBox = slide.shapes.add_textbox(l, t, w, h)
    txBox.word_wrap = True
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_before = Pt(10)
        p.space_after  = Pt(10)
        run = p.runs[0] if p.runs else p.add_run()
        run.text = item
        run.font.size = Pt(size)
        run.font.color.rgb = colour
        p.bullet = True


def accent_bar(slide):
    add_rect(slide, 0, Inches(7.2), W, Inches(0.3), ACCENT)


def chrome(slide):
    add_rect(slide, 0, 0, W, H, NAVY)
    add_rect(slide, 0, 0, W, Inches(1.15), BLUE)
    add_rect(slide, 0, 0, Inches(0.08), H, ACCENT)
    accent_bar(slide)


def content_slide(prs, title, bullets, note=None):
    sl = blank_slide(prs)
    chrome(sl)
    text_box(sl, title,
             Inches(0.3), Inches(0.15), Inches(12.7), Inches(0.9),
             size=30, bold=True, colour=WHITE)
    add_bullets(sl, bullets,
                Inches(0.5), Inches(1.25), Inches(12.3), Inches(5.7),
                size=22, colour=LIGHT_GRAY)
    if note:
        text_box(sl, note, Inches(0.4), Inches(6.85), Inches(12.5), Inches(0.35),
                 size=11, colour=ACCENT)
    return sl


def divider_slide(prs, label):
    sl = blank_slide(prs)
    add_rect(sl, 0, 0, W, H, NAVY)
    add_rect(sl, 0, Inches(3.4), W, Inches(0.08), ACCENT)
    add_rect(sl, 0, 0, Inches(0.08), H, ACCENT)
    text_box(sl, label,
             Inches(1), Inches(2.7), Inches(11), Inches(1.2),
             size=40, bold=True, colour=WHITE, align=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════════════
prs = new_prs()

# ── TITLE ─────────────────────────────────────────────────────────────────────
sl = blank_slide(prs)
add_rect(sl, 0, 0, W, H, NAVY)
add_rect(sl, 0, 0, Inches(0.12), H, ACCENT)
add_rect(sl, 0, Inches(3.1), W, Inches(0.06), BLUE)
text_box(sl, "A Technology Vision for\nQuantitative Trading",
         Inches(0.5), Inches(0.9), Inches(12), Inches(1.9),
         size=42, bold=True, colour=WHITE)
text_box(sl, "Thomas Schmelzer",
         Inches(0.5), Inches(3.4), Inches(8), Inches(0.5),
         size=24, bold=True, colour=ACCENT)
text_box(sl, "May 2026",
         Inches(0.5), Inches(3.95), Inches(8), Inches(0.4),
         size=18, colour=LIGHT_GRAY)
text_box(sl, "Two decades across systematic hedge funds, HFT, family offices and sovereign wealth funds.",
         Inches(0.5), Inches(4.7), Inches(10), Inches(0.7),
         size=16, colour=MID_GRAY)

# ── EXECUTIVE SUMMARY ─────────────────────────────────────────────────────────
content_slide(prs, "The Problem in Brief", [
    "▸  Researchers in MATLAB/Python, engineers reimplementing in C++",
    "▸  Knowledge fragmented; new hires rebuilt the same tools from scratch",
    "▸  Modern ML (PyTorch) made the C++ mandate impossible to sustain",
    "▸  The kitchen was never built — essential tools reinvented everywhere",
])

content_slide(prs, "The Answer in Brief", [
    "▸  Research and production share the same environment and the same container",
    "▸  Team structured like a professional kitchen — collaborative, quality shared",
    "▸  Common tools built once and shared; Rhiza keeps repositories aligned",
    "▸  Focus preserved for the one thing that cannot be bought: the edge",
])

# ── THE PROBLEM ───────────────────────────────────────────────────────────────
divider_slide(prs, "The Problem")

content_slide(prs, "The Script Era", [
    "▸  Researchers: mathematicians, physicists and statisticians",
    "▸  Strategies developed in MATLAB or Python — fast to iterate",
    "▸  Outputs were dense, clever and deeply personal scripts",
    "▸  Logic accumulated in layers over months and years",
])

content_slide(prs, "Reinventing the Wheel", [
    "▸  No shared library — same components rebuilt by every researcher",
    "▸  Moving averages, portfolio construction, signal filters: all duplicated",
    "▸  Diverging results with no clear explanation",
    "▸  Onboarding meant starting from scratch; knowledge walked out with people",
])

content_slide(prs, "The Ambition Ceiling", [
    "▸  Researchers in isolation gravitate to strategies they can personally implement",
    "▸  The limit is often programming skill, not research ideas",
    "▸  Strong mathematical intuition, modest software engineering experience",
    "▸  A shared platform raises that ceiling — ambition is no longer self-limiting",
])

content_slide(prs, "The Handover Model", [
    "▸  Strategies passed to C++ engineers for production reimplementation",
    "▸  C++ offered performance, determinism and operational robustness",
    "▸  Handover rarely clean: translation errors, implicit edge cases, precision issues",
    "▸  Research cycles bottlenecked — months between idea and live strategy",
])

content_slide(prs, "The Handover Model — Why It Broke", [
    "▸  Every change to a live strategy risked restarting the reimplementation process",
    "▸  PyTorch and modern ML simply cannot be reimplemented in C++",
    "▸  When things go wrong, accountability diffuses — nobody owns it",
    "▸  Discussed by Marcos Lopez de Prado; tested at ADIA's Team Q",
])

content_slide(prs, "History's Verdict", [
    "▸  Across the industry, the pattern repeated: the kitchen was never built",
    "▸  Essential tools created independently by every team in slightly different ways",
    "▸  Data APIs, portfolio tools, analytics: all reinvented dozens of times",
    "▸  Result: a sprawling collection of overlapping partial solutions",
])

# ── A NEW DIRECTION ───────────────────────────────────────────────────────────
divider_slide(prs, "A New Direction")

content_slide(prs, "One Environment", [
    "▸  Research and production share the same environment",
    "▸  Researchers express ideas in high-level terms",
    "▸  The platform carries them through to execution without a translation step",
    "▸  No reimplementation, no port, no step where something silently goes wrong",
])

content_slide(prs, "The Kitchen Analogy", [
    "▸  Assembly line fails for knowledge work — interfaces are never fixed in advance",
    "▸  Lopez de Prado's car factory: appealing but misleading",
    "▸  Better image: the professional kitchen — familiar and collaborative",
    "▸  Quality is everyone's responsibility throughout, not inspected at the end",
])

content_slide(prs, "The Chef Does Not Build the Oven", [
    "▸  A professional kitchen assumes a working environment",
    "▸  Researchers and developers should not build basic infrastructure from scratch",
    "▸  Data pipelines, execution connectors, backtesting engines: that is the oven",
    "▸  The platform provides it — the team's energy belongs on the edge",
])

content_slide(prs, "The Checkerboard Structure", [
    "▸  Researchers and developers sit together, alternate and collaborate continuously",
    "▸  Knowledge moves in both directions — no wall between them",
    "▸  The boundary between researcher and developer is blurry by design",
    "▸  When the team builds something together, it owns it together",
])

content_slide(prs, "Containerization", [
    "▸  Container packages code and the entire runtime environment",
    "▸  Identical on researcher's laptop, backtesting cluster and production",
    "▸  Silent numerical differences between environments create false confidence",
    "▸  Researcher opens the container and starts — no setup day",
])

# ── BUILDING THE PLATFORM ─────────────────────────────────────────────────────
divider_slide(prs, "Building the Platform")

content_slide(prs, "The Data API", [
    "▸  The most critical piece of infrastructure — everything depends on it",
    "▸  Abstracts sourcing, normalising and versioning across providers",
    "▸  Strict point-in-time semantics — no look-ahead by construction",
    "▸  Researchers ask for what they need; the API handles the rest",
])

content_slide(prs, "Common Strategy Tooling", [
    "▸  Portfolio construction, signal combination, position sizing are not proprietary",
    "▸  Shared across the industry and across the team",
    "▸  Implemented once, tested thoroughly, available to everyone",
    "▸  No researcher should reimplement a portfolio optimiser from scratch",
])

content_slide(prs, "Performance Analytics & Live Monitoring", [
    "▸  Returns decomposition, drawdown analysis, factor attribution, cost accounting",
    "▸  Consistent metrics — results comparable across strategies and time",
    "▸  Live: position/exposure tracking, P&L attribution, execution quality",
    "▸  Alerts when something moves outside expected bounds",
])

content_slide(prs, "Build With Researchers, Not Just For Them", [
    "▸  A platform built only by engineers risks solving the wrong problems",
    "▸  Researchers know what data they need and what slows their work down",
    "▸  Kitchen and strategies are often built in parallel — that is healthy",
    "▸  But a minimal foundation comes first: data API, portfolio tools, Rhiza",
])

content_slide(prs, "Rhiza — The Repo Zoo Problem", [
    "▸  Each strategy in its own repository — left unmanaged, they diverge",
    "▸  CI workflows split, Python versions drift, security fixes get missed",
    "▸  The same fragmentation as personal scripts, now at the infrastructure level",
    "▸  Rhiza is a living template system that keeps every repo aligned",
], note="github.com/Jebel-Quant/rhiza")

content_slide(prs, "Rhiza — How It Works", [
    "▸  Central template holds canonical CI, linting, container config",
    "▸  Template changes → pull request in each downstream repo",
    "▸  Owners review, adapt if needed, merge — nothing forced, nothing missed",
    "▸  Already in use at Stanford CVXGRP and Janus Henderson",
], note="github.com/Jebel-Quant/rhiza")

# ── LIVE TRADING ──────────────────────────────────────────────────────────────
divider_slide(prs, "Live Trading")

content_slide(prs, "Proximity — Same Container", [
    "▸  The same container runs in research, paper trading and production",
    "▸  No translation step — nothing can silently go wrong",
    "▸  The gap between backtest and live is where losses hide",
    "▸  Closing it is a core design requirement, not a convenience",
])

content_slide(prs, "Configuration, Not Code", [
    "▸  What changes between environments is configuration, not code",
    "▸  Data source, parameters, risk limits and execution venue: all config",
    "▸  Moving to live means changing config, not rebuilding the system",
    "▸  Every deployment: a known container image plus a known config state",
])

content_slide(prs, "Prime Broker Connectivity", [
    "▸  Strategy expresses intent — the execution layer handles translation",
    "▸  FIX or proprietary API: irrelevant to the strategy",
    "▸  Switching brokers or adding a venue is a configuration change",
    "▸  Same execution interface in backtest and live — backed by simulator or real connection",
])

content_slide(prs, "Auditability & Rollback", [
    "▸  Every configuration file is versioned",
    "▸  Full audit trail: reconstruct exactly what ran, when and with what parameters",
    "▸  Rolling back is a configuration change, not an emergency deployment",
    "▸  Problems in production have a clear, fast path to a known-good state",
])

# ── QUALITY & RISK ────────────────────────────────────────────────────────────
divider_slide(prs, "Quality & Risk")

content_slide(prs, "Backtesting — Honesty First", [
    "▸  The gap between backtest and live is rarely bad ideas",
    "▸  It is almost always an optimistic backtest",
    "▸  Look-ahead bias: platform enforces strict point-in-time data semantics",
    "▸  Structurally difficult to request data that would not have been available",
])

content_slide(prs, "Backtesting — Costs and Overfitting", [
    "▸  Transaction costs: market impact, bid-ask, borrow — modelled explicitly",
    "▸  Conservative, realistic and optimistic cost scenarios before anything is taken seriously",
    "▸  Overfitting: walk-forward and out-of-sample evaluation as standard",
    "▸  Culture matters — no tool prevents repeated tweaking until results look good",
])

content_slide(prs, "Risk Management — By Design", [
    "▸  Risk is a layer through the entire platform, not bolted on at the end",
    "▸  Research: factor exposure analysis and stress testing before any live capital",
    "▸  Deployment: pre-trade checks — position, notional and concentration limits",
    "▸  All limits are configuration: versioned, auditable, no code changes needed",
])

content_slide(prs, "Risk Management — In Production", [
    "▸  Continuous monitoring: drawdown limits, automatic position reduction or halt",
    "▸  Gross and net exposure tracked in real time against defined thresholds",
    "▸  Kill switch is a first-class platform concept — not an emergency procedure",
    "▸  Tested regularly, the same way a kitchen tests its fire procedures",
])

# ── AI & JEBEL QUANT ──────────────────────────────────────────────────────────
divider_slide(prs, "AI & Jebel Quant Research")

content_slide(prs, "The Impact of AI — Building & Research", [
    "▸  AI is used at every stage of this work",
    "▸  Platform construction: boilerplate, documentation and code review in hours",
    "▸  Research: signal generation, literature review, rapid prototyping",
    "▸  More ideas tested; more reach the stage of serious evaluation",
])

content_slide(prs, "The Impact of AI — Production & Limits", [
    "▸  Production: anomaly detection — problems surface in minutes, not hours",
    "▸  AI does not know which signals are real and which are spurious",
    "▸  It cannot distinguish a broken model from a changed market",
    "▸  AI removes friction; judgement remains with the team",
])

content_slide(prs, "Jebel Quant Research — Infrastructure", [
    "▸  Rhiza: living template system — in use at Stanford CVXGRP and Janus Henderson",
    "▸  Data access: normalised, versioned API across asset classes",
    "▸  Live trading infrastructure: container model, config management, broker connectivity",
    "▸  All tools designed to be reusable across strategies and organisations",
], note="github.com/Jebel-Quant")

content_slide(prs, "Jebel Quant Research — Research Tools", [
    "▸  Portfolio construction: convex optimisation (linalg, basanos)",
    "▸  Collaboration with Stephen Boyd's group at Stanford",
    "▸  Co-authored research with Ron Kahn",
    "▸  Signal combination and analytics: jquantstats",
], note="github.com/Jebel-Quant")

prs.save("/Users/thomasschmelzer/projects/jqr/repos/platform/vision.pptx")
print(f"Saved vision.pptx — {len(prs.slides)} slides")
