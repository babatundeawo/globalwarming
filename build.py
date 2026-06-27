# -*- coding: utf-8 -*-
"""
Build script for the Global Warming Explorer site.
Generates all HTML pages from shared nav/footer/head templates so every
page stays consistent. Run with: python3 build.py
"""
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">"""

NAV_ITEMS = [
    ("index.html", "Home", "home"),
]
LEARN_ITEMS = [
    ("what-is-global-warming.html", "What Is Global Warming?", "learn-what"),
    ("causes.html", "Causes", "learn-causes"),
    ("effects.html", "Effects", "learn-effects"),
    ("why-care.html", "Why Should We Care?", "learn-why"),
]
ACT_ITEMS = [
    ("carbon-footprint.html", "Carbon Footprint Calculator", "act-cfp"),
    ("recycle.html", "Reduce, Reuse, Recycle", "act-recycle"),
    ("clean-energy.html", "Clean Energy", "act-energy"),
    ("action-hub.html", "Action Hub", "act-hub"),
]
TAIL_ITEMS = [
    ("data-explorer.html", "Data Explorer", "data"),
    ("quiz.html", "Quiz", "quiz"),
    ("glossary.html", "Glossary", "glossary"),
]

ALL_LINK_ITEMS = NAV_ITEMS + LEARN_ITEMS + ACT_ITEMS + TAIL_ITEMS + [("about.html", "About", "about")]

TOPIC_ORDER = [
    ("what-is-global-warming.html", "What Is Global Warming?"),
    ("causes.html", "Causes of Global Warming"),
    ("effects.html", "Effects, Worldwide and at Home"),
    ("why-care.html", "Why Should We Care?"),
    ("carbon-footprint.html", "Your Carbon Footprint"),
    ("recycle.html", "Reduce, Reuse, Recycle"),
    ("clean-energy.html", "Clean Energy"),
    ("action-hub.html", "Action Hub"),
]


def _cls(key, active):
    return " is-active" if key == active else ""


def nav_html(active):
    learn_active = any(k == active for _, _, k in LEARN_ITEMS)
    act_active = any(k == active for _, _, k in ACT_ITEMS)
    learn_pop = "\n".join(
        '<a href="%s">%s</a>' % (href, label) for href, label, _ in LEARN_ITEMS
    )
    act_pop = "\n".join(
        '<a href="%s">%s</a>' % (href, label) for href, label, _ in ACT_ITEMS
    )
    tail_links = "\n".join(
        '<a class="nav-link%s" href="%s">%s</a>' % (_cls(k, active), href, label)
        for href, label, k in TAIL_ITEMS
    )
    return """<header class="site-header">
    <nav class="nav">
      <a href="index.html" class="brand">
        <span class="mark">GW</span>
        <span>Global Warming Explorer<small>by Babatunde Awoyemi · Techbase</small></span>
      </a>
      <div class="nav-desktop">
        <a class="nav-link%s" href="index.html">Home</a>
        <a class="nav-link%s" href="course.html">Course</a>
        <div class="nav-group">
          <a class="nav-link%s" href="what-is-global-warming.html" aria-haspopup="true">Learn ▾</a>
          <div class="nav-pop">%s</div>
        </div>
        <div class="nav-group">
          <a class="nav-link%s" href="action-hub.html" aria-haspopup="true">Take Action ▾</a>
          <div class="nav-pop">%s</div>
        </div>
        %s
      </div>
      <div class="nav-cta">
        <a href="about.html" class="btn btn-ghost btn-sm">About</a>
        <button class="menu-btn" aria-label="Open menu" aria-expanded="false"><span></span></button>
      </div>
    </nav>
    <div class="mobile-menu">
      <a style="font-weight:800;font-size:1.1rem;" href="index.html">Home</a>
      <a style="font-weight:800;font-size:1.1rem;" href="course.html">Course</a>
      <div class="mm-section"><h4>Learn</h4>%s</div>
      <div class="mm-section"><h4>Take Action</h4>%s</div>
      <div class="mm-section"><h4>Go further</h4>
        <a href="data-explorer.html">Data Explorer</a>
        <a href="quiz.html">Quiz</a>
        <a href="glossary.html">Glossary</a>
        <a href="about.html">About</a>
      </div>
      <div class="mm-section"><h4>Guided course</h4>
        <a href="course.html">8-Lesson Course</a>
        <a href="checkin.html">Check In</a>
        <a href="class-dashboard.html">Class Dashboard</a>
        <a href="for-teachers.html">For Teachers</a>
        <a href="certificate.html">Certificate</a>
      </div>
    </div>
  </header>""" % (
        _cls("home", active),
        _cls("course", active),
        " is-active" if learn_active else "",
        learn_pop,
        " is-active" if act_active else "",
        act_pop,
        tail_links,
        "\n".join('<a href="%s">%s</a>' % (h, l) for h, l, _ in LEARN_ITEMS),
        "\n".join('<a href="%s">%s</a>' % (h, l) for h, l, _ in ACT_ITEMS),
    )


FOOTER_HTML = """<footer class="site-footer">
    <div class="footer-inner">
      <div>
        <div class="footer-brand"><span class="mark" style="width:26px;height:26px;font-size:.8rem;">GW</span> Global Warming Explorer</div>
        <p>An open, explorative guide to global warming — built from Ibadan, Nigeria, for curious minds everywhere, kids included. Originally created as a classroom presentation; rebuilt from the ground up as a free learning project.</p>
        <p class="muted">© <span class="js-year">2026</span> Babatunde Ayoola Awoyemi. Shared for learning — copy, remix and teach with it.</p>
      </div>
      <div>
        <h5>Learn</h5>
        <ul>
          <li><a href="what-is-global-warming.html">What Is Global Warming?</a></li>
          <li><a href="causes.html">Causes</a></li>
          <li><a href="effects.html">Effects</a></li>
          <li><a href="why-care.html">Why Should We Care?</a></li>
        </ul>
      </div>
      <div>
        <h5>Take Action</h5>
        <ul>
          <li><a href="carbon-footprint.html">Carbon Footprint Calculator</a></li>
          <li><a href="recycle.html">Reduce, Reuse, Recycle</a></li>
          <li><a href="clean-energy.html">Clean Energy</a></li>
          <li><a href="action-hub.html">Action Hub</a></li>
        </ul>
      </div>
      <div>
        <h5>Connect</h5>
        <ul>
          <li><a href="course.html">8-Lesson Course</a></li>
          <li><a href="checkin.html">Check In</a></li>
          <li><a href="class-dashboard.html">Class Dashboard</a></li>
          <li><a href="for-teachers.html">For Teachers</a></li>
          <li><a href="data-explorer.html">Data Explorer</a></li>
          <li><a href="quiz.html">Quiz</a></li>
          <li><a href="glossary.html">Glossary</a></li>
          <li><a href="about.html">About Babatunde</a></li>
          <li><a href="https://github.com/babatundeawo" target="_blank" rel="noopener">GitHub — babatundeawo</a></li>
          <li><a href="https://github.com/techbaseng" target="_blank" rel="noopener">GitHub — Techbase</a></li>
          <li><a href="https://babatundeawo.github.io/" target="_blank" rel="noopener">My Portfolio</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>Built with HTML, CSS &amp; vanilla JS — no tracking, no ads.</span>
      <span>A Techbase Consultant Services learning resource.</span>
    </div>
  </footer>"""

ISOLINES_SVG = """<svg class="isolines" viewBox="0 0 1200 500" preserveAspectRatio="none" aria-hidden="true">
      <defs>
        <linearGradient id="iso1" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#16847A"/><stop offset="100%" stop-color="#EE8C3C"/>
        </linearGradient>
      </defs>
      <g fill="none" stroke="url(#iso1)" stroke-width="1.1" opacity=".35">
        <path d="M-50,80 C200,40 400,120 650,70 C850,30 1050,90 1250,50"/>
        <path d="M-50,150 C220,110 420,190 660,140 C870,100 1040,160 1250,120"/>
        <path d="M-50,220 C240,260 440,180 670,230 C880,270 1040,210 1250,250"/>
        <path d="M-50,300 C260,340 460,270 690,320 C890,360 1050,300 1250,330"/>
        <path d="M-50,380 C280,420 480,360 710,400 C900,430 1060,390 1250,410"/>
      </g>
    </svg>"""


def readout(cells):
    """cells: list of dict(label, value, decimals=0, prefix='', suffix='', tone='')"""
    parts = []
    for c in cells:
        tone_cls = " tone-" + c["tone"] if c.get("tone") else ""
        value = c["value"]
        try:
            float(value)
            numeric = True
        except (TypeError, ValueError):
            numeric = False
        if numeric:
            parts.append(
                '<div class="readout-cell"><span class="ro-label">%s</span>'
                '<span class="ro-value js-counter%s" data-target="%s" data-decimals="%s" data-prefix="%s" data-suffix="%s">0</span></div>'
                % (
                    c["label"],
                    tone_cls,
                    value,
                    c.get("decimals", 0),
                    c.get("prefix", ""),
                    c.get("suffix", ""),
                )
            )
        else:
            parts.append(
                '<div class="readout-cell"><span class="ro-label">%s</span>'
                '<span class="ro-value%s">%s%s%s</span></div>'
                % (c["label"], tone_cls, c.get("prefix", ""), value, c.get("suffix", ""))
            )
    return '<div class="readout"><div class="readout-inner">%s</div></div>' % "".join(parts)


def topic_pager(current_href):
    hrefs = [h for h, _ in TOPIC_ORDER]
    if current_href not in hrefs:
        return ""
    i = hrefs.index(current_href)
    prev_html = ""
    next_html = ""
    if i > 0:
        h, t = TOPIC_ORDER[i - 1]
        prev_html = '<a class="pager-link prev" href="%s"><span class="pl-dir">← Previous</span><div class="pl-title">%s</div></a>' % (h, t)
    else:
        prev_html = '<span></span>'
    if i < len(TOPIC_ORDER) - 1:
        h, t = TOPIC_ORDER[i + 1]
        next_html = '<a class="pager-link next" href="%s"><span class="pl-dir">Next →</span><div class="pl-title">%s</div></a>' % (h, t)
    else:
        next_html = '<a class="pager-link next" href="data-explorer.html"><span class="pl-dir">Next →</span><div class="pl-title">Explore the Data</div></a>'
    return '<div class="topic-pager">%s%s</div>' % (prev_html, next_html)


def page(filename, title, description, active, hero_html, body_html, extra_head="", extra_scripts=""):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s · Global Warming Explorer</title>
<meta name="description" content="%s">
%s
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="stylesheet" href="css/styles.css">
%s
</head>
<body>
<a href="#main" class="skip-link">Skip to content</a>
%s
<main id="main">
%s
%s
</main>
%s
<script src="js/main.js"></script>
%s
</body>
</html>""" % (
        title,
        description,
        FONTS,
        extra_head,
        nav_html(active),
        hero_html,
        body_html,
        FOOTER_HTML,
        extra_scripts,
    )
    with open(os.path.join(OUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

# =========================================================
# Reusable bits
# =========================================================
def img_credit(text):
    return '<span class="credit">%s</span>' % text

def hero_block(eyebrow, h1, lede, ctas_html, media_html, readout_cells, narrow=False):
    inner_cls = "hero-inner hero-inner--narrow" if narrow else "hero-inner"
    media = "" if narrow else '<div class="hero-media reveal">%s</div>' % media_html
    return """<section class="hero">
    %s
    <div class="%s">
      <div>
        <p class="eyebrow">%s</p>
        <h1>%s</h1>
        <p class="lede">%s</p>
        <div class="hero-ctas">%s</div>
      </div>
      %s
    </div>
    %s
  </section>""" % (ISOLINES_SVG, inner_cls, eyebrow, h1, lede, ctas_html, media, readout(readout_cells))


# =========================================================
# HOME
# =========================================================
home_hero = hero_block(
    eyebrow="A field guide to a warming world",
    h1="One atmosphere. One planet. Every degree counts &mdash; including at home.",
    lede="A free, explorative guide to global warming: the physics of why it happens, what it's already doing to rivers, farms and cities across Nigeria and the world, and what you can actually do about it. Built for curious minds of every age.",
    ctas_html='<a href="what-is-global-warming.html" class="btn btn-primary">Start exploring →</a>'
              '<a href="data-explorer.html" class="btn btn-ghost">See the live data</a>',
    media_html='<img src="https://commons.wikimedia.org/wiki/Special:FilePath/The_Blue_Marble.jpg?width=900" alt="The Blue Marble — Earth photographed from Apollo 17, showing Africa, Antarctica and the Arabian Peninsula">' + img_credit("Earth, 1972 · NASA / Apollo 17 (public domain)"),
    readout_cells=[
        {"label": "CO2 today (avg, 2025)", "value": "427.4", "decimals": 1, "suffix": " ppm", "tone": "warm"},
        {"label": "vs. pre-industrial (~280ppm)", "value": "53", "decimals": 0, "suffix": "% higher", "tone": "warm"},
        {"label": "2025 global temp.", "value": "1.3", "decimals": 1, "prefix": "+", "suffix": "°C vs 1850-1900", "tone": "alert"},
        {"label": "Renewables, world electricity", "value": "34", "decimals": 0, "suffix": "%", "tone": "cool"},
    ],
)

home_body = """
<section class="section section--tight">
  <div class="wrap">
    <div class="grid grid-2 reveal">
      <div class="card" style="border-color:var(--teal-500);">
        <span class="tag">Option 1 · Browse freely</span>
        <div class="ico">🧭</div>
        <h3>Explore in any order</h3>
        <p>Jump straight into whatever pulls you in &mdash; the cards below, organised by theme, no set sequence.</p>
        <a href="what-is-global-warming.html" class="card-link">Start exploring</a>
      </div>
      <div class="card" style="border-color:var(--amber-500);">
        <span class="tag">Option 2 · Follow a path</span>
        <div class="ico">🎓</div>
        <h3>Take the 8-Lesson Course</h3>
        <p>The same material, sequenced with objectives, printable worksheets, and a completion certificate at the end. Built for classrooms &mdash; great solo too.</p>
        <a href="course.html" class="card-link">View the course</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Where to start</p>
      <h2>Explore the guide</h2>
      <p class="lede">Three ways in: understand what's actually happening, see what it means close to home, then do something about it. Jump to whatever pulls you in &mdash; there's no wrong door.</p>
    </div>

    <div class="explore-group reveal">
      <h4>Understand it</h4>
      <div class="grid grid-4">
        <a class="card" href="what-is-global-warming.html"><div class="ico">☀️</div><span class="tag">Start here</span><h3>What Is Global Warming?</h3><p>The greenhouse effect, explained with a jar, a blanket, and the actual numbers.</p><span class="card-link">Read</span></a>
        <a class="card" href="causes.html"><div class="ico">🏭</div><span class="tag">Source</span><h3>Causes</h3><p>What's actually filling the atmosphere &mdash; ranked by how much each one matters.</p><span class="card-link">Read</span></a>
        <a class="card" href="effects.html"><div class="ico">🌊</div><span class="tag">Impact</span><h3>Effects</h3><p>Melting ice, fiercer storms &mdash; and the floods that hit Nigeria hard in 2025.</p><span class="card-link">Read</span></a>
        <a class="card" href="why-care.html"><div class="ico">❤️</div><span class="tag">Stakes</span><h3>Why Should We Care?</h3><p>Food, water, health, and why this hits some communities far harder than others.</p><span class="card-link">Read</span></a>
      </div>
    </div>

    <div class="explore-group reveal">
      <h4>Do something about it</h4>
      <div class="grid grid-4">
        <a class="card" href="carbon-footprint.html"><div class="ico">🧮</div><span class="tag">Tool</span><h3>Carbon Footprint Calculator</h3><p>Get a rough, honest estimate of your own footprint in two minutes.</p><span class="card-link">Calculate</span></a>
        <a class="card" href="recycle.html"><div class="ico">♻️</div><span class="tag">Habit</span><h3>Reduce, Reuse, Recycle</h3><p>Why the three Rs work, in the order they're meant to be used.</p><span class="card-link">Read</span></a>
        <a class="card" href="clean-energy.html"><div class="ico">🌬️</div><span class="tag">Future</span><h3>Clean Energy</h3><p>Solar, wind and the quiet energy revolution already under way.</p><span class="card-link">Read</span></a>
        <a class="card" href="action-hub.html"><div class="ico">✅</div><span class="tag">Checklist</span><h3>Action Hub</h3><p>Real actions for school, home and your community &mdash; tick them off as you go.</p><span class="card-link">Open hub</span></a>
      </div>
    </div>

    <div class="explore-group reveal">
      <h4>Go further</h4>
      <div class="grid grid-3">
        <a class="card" href="data-explorer.html"><div class="ico">📊</div><span class="tag">Live-ish data</span><h3>Data Explorer</h3><p>The CO2 curve, the warmest years on record, and Nigeria's 2025 flood numbers.</p><span class="card-link">Explore</span></a>
        <a class="card" href="quiz.html"><div class="ico">🎯</div><span class="tag">10 questions</span><h3>Quiz</h3><p>Test what you've picked up &mdash; built for explorers of every age.</p><span class="card-link">Play</span></a>
        <a class="card" href="glossary.html"><div class="ico">📖</div><span class="tag">A&ndash;Z</span><h3>Glossary &amp; Sources</h3><p>Every tricky term explained simply, plus where all the numbers come from.</p><span class="card-link">Look up</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="layout-2col reveal">
      <div>
        <p class="eyebrow">Who built this</p>
        <h2>A classroom project, rebuilt as an open resource</h2>
        <p>This guide started life years ago as a presentation built for a student. It's now been rebuilt from scratch by <strong>Babatunde Ayoola Awoyemi</strong> &mdash; a physicist, STEM educator, and Lead Consultant at <strong>Techbase Consultant Services</strong> in Ibadan, Nigeria &mdash; as a free, open learning tool for anyone curious about the warming world we live in.</p>
        <p>Babatunde's own research background is in atmospheric physics and solar radiation modelling, which is part of why this site leans on real instrument-style data wherever it can, instead of vague claims.</p>
        <a href="about.html" class="btn btn-primary">Meet your guide →</a>
      </div>
      <div class="side-card" style="position:static;">
        <h4>Built &amp; maintained by</h4>
        <p style="font-weight:700;font-size:1.05rem;color:var(--ink);margin-bottom:.2em;">Techbase Consultant Services</p>
        <p style="font-size:.88rem;">STEM education · IT consultancy · web development · robotics, based in Ibadan, Nigeria.</p>
        <ul style="margin-top:14px;">
          <li><a href="https://github.com/babatundeawo" target="_blank" rel="noopener">→ github.com/babatundeawo</a></li>
          <li><a href="https://github.com/techbaseng" target="_blank" rel="noopener">→ github.com/techbaseng</a></li>
          <li><a href="https://babatundeawo.github.io/" target="_blank" rel="noopener">→ My Portfolio</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

page(
    filename="index.html",
    title="Home",
    description="An explorative, mobile-friendly guide to global warming — the science, the effects in Nigeria and worldwide, and what you can do, for explorers of every age.",
    active="home",
    hero_html=home_hero,
    body_html=home_body,
)

# =========================================================
# WHAT IS GLOBAL WARMING
# =========================================================
GREENHOUSE_SVG = """<svg viewBox="0 0 700 430" style="width:100%;height:auto;" role="img" aria-label="Diagram of the greenhouse effect: sunlight enters the atmosphere, heat radiates from Earth's surface, and greenhouse gases trap part of that heat while some escapes to space.">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E7F2EF"/><stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <marker id="arrowAmber" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#D9691A"/></marker>
    <marker id="arrowCoral" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#C8432F"/></marker>
    <marker id="arrowTeal" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#0E5C56"/></marker>
  </defs>
  <rect x="0" y="0" width="700" height="430" fill="url(#sky)"/>
  <!-- space label zone -->
  <text x="20" y="28" font-family="JetBrains Mono, monospace" font-size="11" fill="#6E7D75" letter-spacing="1">SPACE</text>
  <line x1="0" y1="60" x2="700" y2="60" stroke="#CBD8CD" stroke-dasharray="4 5"/>
  <!-- greenhouse gas band -->
  <rect x="0" y="230" width="700" height="60" fill="#CFE6E1" opacity=".55"/>
  <text x="500" y="222" font-family="JetBrains Mono, monospace" font-size="11" fill="#0A4641" letter-spacing="1">GREENHOUSE GAS LAYER</text>
  <g fill="#16847A" opacity=".7">
    <circle cx="80" cy="255" r="4"/><circle cx="140" cy="270" r="4"/><circle cx="210" cy="250" r="4"/>
    <circle cx="280" cy="268" r="4"/><circle cx="350" cy="252" r="4"/><circle cx="420" cy="272" r="4"/>
    <circle cx="490" cy="254" r="4"/><circle cx="560" cy="268" r="4"/><circle cx="620" cy="250" r="4"/>
  </g>
  <!-- sun -->
  <circle cx="610" cy="70" r="30" fill="#EE8C3C"/>
  <g stroke="#EE8C3C" stroke-width="3" stroke-linecap="round">
    <line x1="610" y1="25" x2="610" y2="12"/><line x1="650" y1="40" x2="660" y2="30"/>
    <line x1="665" y1="70" x2="680" y2="70"/><line x1="650" y1="100" x2="660" y2="110"/>
  </g>
  <!-- ground -->
  <rect x="0" y="370" width="700" height="60" fill="#0A4641"/>
  <text x="20" y="410" font-family="JetBrains Mono, monospace" font-size="11" fill="#CFE6E1" letter-spacing="1">EARTH'S SURFACE</text>
  <!-- incoming sunlight -->
  <line x1="560" y1="95" x2="380" y2="365" stroke="#D9691A" stroke-width="2.5" marker-end="url(#arrowAmber)"/>
  <line x1="600" y1="100" x2="470" y2="365" stroke="#D9691A" stroke-width="2.5" marker-end="url(#arrowAmber)"/>
  <line x1="500" y1="90" x2="280" y2="365" stroke="#D9691A" stroke-width="2.5" marker-end="url(#arrowAmber)"/>
  <!-- outgoing heat from ground, trapped -->
  <path d="M300,368 C290,330 300,290 290,260" fill="none" stroke="#C8432F" stroke-width="2.5" marker-end="url(#arrowCoral)"/>
  <path d="M400,368 C410,330 398,290 408,260" fill="none" stroke="#C8432F" stroke-width="2.5" marker-end="url(#arrowCoral)"/>
  <!-- heat bounced back down -->
  <path d="M290,250 C270,280 275,330 260,368" fill="none" stroke="#C8432F" stroke-width="2" stroke-dasharray="2 5" marker-end="url(#arrowCoral)"/>
  <path d="M408,248 C425,280 418,330 430,368" fill="none" stroke="#C8432F" stroke-width="2" stroke-dasharray="2 5" marker-end="url(#arrowCoral)"/>
  <!-- heat that escapes to space -->
  <path d="M500,368 C515,300 505,150 520,55" fill="none" stroke="#0E5C56" stroke-width="2.5" marker-end="url(#arrowTeal)"/>
  <!-- labels -->
  <text x="170" y="150" font-family="Plus Jakarta Sans, sans-serif" font-size="13" font-weight="700" fill="#11201C">Sunlight passes</text>
  <text x="170" y="167" font-family="Plus Jakarta Sans, sans-serif" font-size="13" font-weight="700" fill="#11201C">through easily</text>
  <text x="20" y="340" font-family="Plus Jakarta Sans, sans-serif" font-size="13" font-weight="700" fill="#C8432F">Some heat is</text>
  <text x="20" y="357" font-family="Plus Jakarta Sans, sans-serif" font-size="13" font-weight="700" fill="#C8432F">trapped &amp; bounced back</text>
  <text x="530" y="120" font-family="Plus Jakarta Sans, sans-serif" font-size="13" font-weight="700" fill="#0E5C56">A little heat</text>
  <text x="530" y="137" font-family="Plus Jakarta Sans, sans-serif" font-size="13" font-weight="700" fill="#0E5C56">escapes to space</text>
</svg>"""

what_hero = hero_block(
    eyebrow="Start here · Learn",
    h1="What is global warming, really?",
    lede="Strip away the politics and the panic for a second: global warming is a physics problem. It's about what happens to heat once sunlight reaches Earth &mdash; and why a thin layer of gas, measured in parts per million, makes such an outsized difference.",
    ctas_html='<a href="causes.html" class="btn btn-primary">Next: what causes it →</a>',
    media_html="", readout_cells=[
        {"label": "CO2, pre-industrial (~1750)", "value": "280", "decimals": 0, "suffix": " ppm", "tone": "cool"},
        {"label": "CO2, 2025 average", "value": "427.4", "decimals": 1, "suffix": " ppm", "tone": "warm"},
        {"label": "Time CO2 lingers in the air", "value": "100", "decimals": 0, "suffix": "+ yrs", "tone": ""},
    ],
    narrow=True,
)

what_body = """
<section class="section">
  <div class="wrap">
    <div class="layout-2col">
      <div class="prose reveal">
        <h2>The greenhouse effect, in one diagram</h2>
        <p>Sunlight passes through the atmosphere fairly easily and warms the ground. The warmed Earth then radiates that energy back outward as heat (infrared radiation). Some of that heat escapes straight to space &mdash; but greenhouse gases like carbon dioxide (CO2), methane and water vapour absorb part of it and radiate it back down again, the way a blanket holds your body heat in rather than creating any heat of its own.</p>
        <div class="callout callout--note" style="background:#fff;padding:18px;">%s</div>
        <p>That's a genuinely good thing in the right amount &mdash; without any greenhouse effect at all, Earth's average surface temperature would sit somewhere around &minus;18°C, far too cold for the world as we know it. The trouble starts when we keep adding far more of these gases than natural processes can absorb, thickening the "blanket" year after year.</p>

        <h2 style="margin-top:1.6em;">Weather vs. climate vs. global warming</h2>
        <p>These three get mixed up constantly, so here's the difference in one line each:</p>
        <ul>
          <li><strong>Weather</strong> is what's happening outside right now &mdash; today's rain, today's heat.</li>
          <li><strong>Climate</strong> is the long-term pattern of weather in a place, usually averaged over 30 years.</li>
          <li><strong>Global warming</strong> is the measured rise in Earth's average surface temperature over decades, caused mainly by human-added greenhouse gases &mdash; one driver reshaping climates everywhere, at different speeds and in different ways.</li>
        </ul>
        <p>A cold week somewhere doesn't disprove global warming any more than one hot afternoon proves it. It's the decades-long average that matters &mdash; and that average keeps climbing.</p>

        <h2 style="margin-top:1.6em;">Why a few hundred parts per million matters so much</h2>
        <p>"Parts per million" (ppm) sounds tiny, and in one sense it is &mdash; CO2 is still a small slice of the atmosphere, which is mostly nitrogen and oxygen. But greenhouse gases are disproportionately powerful at trapping heat for their size. Atmospheric CO2 has risen from about 280 ppm before the Industrial Revolution to roughly 427 ppm in 2025 &mdash; about a 50%% increase &mdash; and each extra molecule adds a little more trapped heat across the entire planet, all the time.</p>
        <div class="callout callout--try">
          <span class="callout-label">Try this · A 10-minute experiment</span>
          <p>Place two thermometers in the sun: one inside a clear sealed jar, one left in the open air. Check both after 20&ndash;30 minutes. The jar traps heat the way greenhouse gases do &mdash; it almost always reads warmer. Scale that idea up to an entire planet, and you've got the core of this whole topic.</p>
        </div>
      </div>
      <aside class="side-card">
        <h4>On this page</h4>
        <ul>
          <li><a href="#main">The greenhouse effect</a></li>
        </ul>
        <h4 style="margin-top:22px;">Quick facts</h4>
        <div class="fact-strip" style="flex-direction:column;">
          <div class="fact"><div class="fv">~1859</div><div class="fl">First lab experiments on CO2 and heat (Eunice Foote, John Tyndall)</div></div>
          <div class="fact"><div class="fv">−18°C</div><div class="fl">Earth's rough average temperature with no greenhouse effect at all</div></div>
        </div>
      </aside>
    </div>
    %s
  </div>
</section>
""" % (GREENHOUSE_SVG, topic_pager("what-is-global-warming.html"))

page(
    filename="what-is-global-warming.html",
    title="What Is Global Warming?",
    description="The greenhouse effect explained simply: how sunlight, heat and greenhouse gases work together, and why a 50% rise in CO2 matters so much.",
    active="learn-what",
    hero_html=what_hero,
    body_html=what_body,
)

# =========================================================
# CAUSES
# =========================================================
causes_hero = hero_block(
    eyebrow="Learn · Source",
    h1="What's actually causing global warming?",
    lede="Almost all of the extra greenhouse gas behind today's warming comes from human activity since the 1800s &mdash; mainly the everyday business of making electricity, growing food, manufacturing things, and getting around.",
    ctas_html='<a href="effects.html" class="btn btn-primary">Next: the effects →</a>',
    media_html='<img src="https://commons.wikimedia.org/wiki/Special:FilePath/Factory_Emitting_Smoke.jpg?width=900" alt="Industrial smokestacks emitting smoke into the sky">' + img_credit("Industrial emissions · via Wikimedia Commons"),
    readout_cells=[
        {"label": "Share of emissions: energy & transport", "value": "73", "decimals": 0, "suffix": "%+", "tone": "warm"},
        {"label": "Share from agriculture & land use", "value": "18", "decimals": 0, "suffix": "%", "tone": ""},
        {"label": "Years of rapid acceleration", "value": "60", "decimals": 0, "suffix": "+", "tone": ""},
    ],
)

causes_body = """
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Ranked by scale</p>
      <h2>The big sources, in order of how much they matter</h2>
      <p class="lede">This list is genuinely a ranking &mdash; it follows roughly how much each sector contributes to global human-caused greenhouse gas emissions, based on international energy and climate accounting.</p>
    </div>
    <ol class="numbered-list reveal">
      <li>
        <h3>Burning fossil fuels for electricity &amp; heat</h3>
        <p>Coal, oil and natural gas power plants are the single largest source. Every kilowatt-hour generated this way releases CO2 that took millions of years to lock underground.</p>
      </li>
      <li>
        <h3>Transport</h3>
        <p>Petrol and diesel cars, motorcycles, trucks, ships and planes all burn fossil fuel directly. Road transport alone is a major and fast-growing slice of this.</p>
      </li>
      <li>
        <h3>Industry &amp; manufacturing</h3>
        <p>Making cement, steel, plastics and chemicals both burns fuel for heat and, in some processes (like cement), releases CO2 as a direct by-product of the chemistry itself.</p>
      </li>
      <li>
        <h3>Agriculture &amp; land use</h3>
        <p>Clearing forests removes carbon-storing trees and often releases the carbon stored in soil. Livestock farming adds methane; fertiliser use adds nitrous oxide &mdash; both far more potent than CO2 molecule-for-molecule.</p>
      </li>
      <li>
        <h3>Waste</h3>
        <p>Organic waste rotting in landfills without oxygen produces methane. It's a smaller slice of the total, but one of the easiest to shrink quickly through better waste management and recycling.</p>
      </li>
    </ol>

    <div class="callout callout--note reveal">
      <span class="callout-label">A note on speed, not just scale</span>
      <p>It isn't only how much we emit &mdash; it's how fast. Natural processes (plants, oceans, rock weathering) absorb CO2 over centuries to millennia. Humans have added a comparable amount in a little over a century, which is why concentrations have climbed roughly 100 times faster than at the end of the last ice age.</p>
    </div>

    <div class="fact-strip reveal">
      <div class="fact"><div class="fv">424.6</div><div class="fl">Mauna Loa annual CO2 average, 2024 (ppm)</div></div>
      <div class="fact"><div class="fv">430.5</div><div class="fl">Record monthly peak, May 2025 (ppm)</div></div>
      <div class="fact"><div class="fv">2.6</div><div class="fl">Average annual ppm increase, 2015&ndash;2024</div></div>
    </div>
    %s
  </div>
</section>
""" % topic_pager("causes.html")

page(
    filename="causes.html",
    title="Causes of Global Warming",
    description="The ranked list of what really causes global warming — energy, transport, industry, agriculture and waste — explained simply.",
    active="learn-causes",
    hero_html=causes_hero,
    body_html=causes_body,
)

# =========================================================
# EFFECTS
# =========================================================
effects_hero = hero_block(
    eyebrow="Learn · Impact",
    h1="Effects: worldwide, and a lot closer to home",
    lede="A warmer atmosphere doesn't just mean warmer days. It loads the dice toward heavier floods, longer droughts, melting ice and rising seas &mdash; and in 2025, Nigeria felt several of these firsthand.",
    ctas_html='<a href="why-care.html" class="btn btn-primary">Next: why care →</a>',
    media_html='<img src="https://commons.wikimedia.org/wiki/Special:FilePath/Auyo_village_flood_06.jpg?width=900" alt="Floodwaters surrounding a village in Auyo, Jigawa State, Nigeria">' + img_credit("Auyo village flood · Sani Maikatanga, Wikimedia Commons (CC BY-SA 4.0)"),
    readout_cells=[
        {"label": "2025: warmest years on record", "value": "3", "decimals": 0, "suffix": "rd", "tone": "alert"},
        {"label": "Arctic sea ice, 2025", "value": "2", "decimals": 0, "suffix": "nd-lowest ever", "tone": "cool"},
        {"label": "Nigerians at flood risk, 2025", "value": "15", "decimals": 0, "suffix": "M+", "tone": "warm"},
    ],
)

effects_body = """
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Around the world</p>
      <h2>What a warmer planet is already doing</h2>
    </div>
    <div class="grid grid-3 reveal">
      <div class="card"><div class="ico">🌡️</div><h3>Rising temperatures</h3><p>2025 was Earth's third-warmest year on record, about 1.3°C above the 1850&ndash;1900 average. The ten warmest years on record have all occurred since 2015.</p></div>
      <div class="card"><div class="ico">🧊</div><h3>Melting ice, rising seas</h3><p>Arctic sea ice in 2025 was the second-lowest on record. Melting ice sheets and warming, expanding seawater are pushing sea levels upward year after year.</p></div>
      <div class="card"><div class="ico">🌪️</div><h3>Fiercer weather</h3><p>Warmer air holds more moisture and warmer oceans fuel stronger storms &mdash; 2025 saw 101 named storms worldwide, above the recent average of 88.</p></div>
      <div class="card"><div class="ico">🌊</div><h3>Warming, more acidic oceans</h3><p>Oceans absorb most of the planet's extra heat. 2025 was the fifth straight year of record-high upper-ocean heat content &mdash; bad news for coral reefs and fisheries.</p></div>
      <div class="card"><div class="ico">🌾</div><h3>Disrupted growing seasons</h3><p>Shifting rainfall and longer dry spells throw off planting and harvest timing for farmers who depend on predictable seasons.</p></div>
      <div class="card"><div class="ico">🦋</div><h3>Pressure on ecosystems</h3><p>Species are shifting ranges, breeding times and migration patterns &mdash; some faster than ecosystems around them can adjust.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Closer to home</p>
      <h2>Nigeria in 2025: a hard year, on both ends of the water cycle</h2>
      <p class="lede">Climate change doesn't just bring more rain or less rain &mdash; in Nigeria's case, 2025 brought devastating amounts of both, in different regions, sometimes in the same season.</p>
    </div>
    <div class="layout-2col reveal">
      <div class="prose">
        <p><strong>Floods.</strong> Nigeria's federal flood outlook flagged more than 1,200 communities across 30 of its 36 states as high-risk in 2025, and roughly 15 million Nigerians were estimated to be at risk. The worst single event struck Mokwa, in Niger State, in late May &mdash; among the deadliest flash floods the area has seen in decades, destroying homes, farmland, schools and a bridge that cut communities off from help. Nationwide flood data later in the year showed children made up the largest single group affected.</p>
        <p><strong>Heat and drought.</strong> At the same time, northern and central states faced severe heat stress &mdash; NiMet issued warnings as temperatures climbed past 40°C across 18 states, reaching as high as 42°C in cities like Yola and Kebbi. Delayed rains disrupted planting across several states, deepening food insecurity that the World Food Programme projected could affect tens of millions of people into 2026.</p>
        <p><strong>Coastlines.</strong> Along Lagos and other coastal communities, rising seas and storm surges are accelerating erosion, threatening homes and infrastructure built right up to the waterline.</p>
      </div>
      <aside class="side-card">
        <h4>2025 Nigeria, by the numbers</h4>
        <div class="fact-strip" style="flex-direction:column;">
          <div class="fact"><div class="fv">30/36</div><div class="fl">States flagged at high flood risk</div></div>
          <div class="fact"><div class="fv">42°C</div><div class="fl">Peak heat recorded in northern cities</div></div>
          <div class="fact"><div class="fv">35M</div><div class="fl">People projected at risk of severe food insecurity into 2026</div></div>
        </div>
      </aside>
    </div>
    <div class="callout callout--alert reveal">
      <span class="callout-label">Why this matters beyond the headlines</span>
      <p>None of this means Nigeria caused the problem &mdash; the country's historic contribution to global emissions is small. But geography and economics mean the impacts land hard anyway. That tension is exactly what the next page digs into.</p>
    </div>
    %s
  </div>
</section>
""" % topic_pager("effects.html")

page(
    filename="effects.html",
    title="Effects of Global Warming",
    description="The real-world effects of global warming, from melting Arctic ice to Nigeria's devastating 2025 floods and northern heatwaves.",
    active="learn-effects",
    hero_html=effects_hero,
    body_html=effects_body,
)

# =========================================================
# WHY SHOULD WE CARE
# =========================================================
why_hero = hero_block(
    eyebrow="Learn · Stakes",
    h1="Why should you actually care?",
    lede="Because every system that feeds, waters, houses and employs people leans on a climate that's now shifting under it &mdash; and because the people who've contributed least to the problem are often the ones absorbing the most risk.",
    ctas_html='<a href="carbon-footprint.html" class="btn btn-primary">Next: your footprint →</a>',
    media_html="", readout_cells=[
        {"label": "WHO: heat-stress deaths/yr, est.", "value": "489", "decimals": 0, "suffix": "K", "tone": "alert"},
        {"label": "Of Nigeria's GDP from agriculture", "value": "31", "decimals": 0, "suffix": "%", "tone": ""},
        {"label": "Of world pop. in climate-vulnerable regions", "value": "3.3", "decimals": 1, "suffix": "B+", "tone": "warm"},
    ],
    narrow=True,
)

why_body = """
<section class="section">
  <div class="wrap">
    <div class="grid grid-2 reveal" style="margin-bottom:30px;">
      <div class="card">
        <div class="ico">🌽</div>
        <h3>Food &amp; farming</h3>
        <p>Agriculture employs a huge share of people across Africa and contributes over 31%% of Nigeria's GDP. Shifting rainfall, drought and flooding directly hit crop yields, prices, and household income.</p>
      </div>
      <div class="card">
        <div class="ico">💧</div>
        <h3>Water</h3>
        <p>Some regions get hit with floods that contaminate drinking water and spark disease outbreaks; others face drought that dries up wells and rivers in the same year, sometimes the same country.</p>
      </div>
      <div class="card">
        <div class="ico">🏥</div>
        <h3>Health</h3>
        <p>Extreme heat is dangerous on its own, and floods increase waterborne diseases like cholera. Climate-related disasters strain already stretched health systems.</p>
      </div>
      <div class="card">
        <div class="ico">💼</div>
        <h3>Economy &amp; jobs</h3>
        <p>Damaged farmland, disrupted supply chains and rebuilding costs after disasters all weigh on growth &mdash; money that could otherwise go toward schools, hospitals and infrastructure.</p>
      </div>
      <div class="card">
        <div class="ico">🦓</div>
        <h3>Biodiversity</h3>
        <p>Ecosystems that took millennia to balance are being asked to adjust in decades. Some species and habitats simply can't keep pace.</p>
      </div>
      <div class="card">
        <div class="ico">🧒</div>
        <h3>The next generation</h3>
        <p>Today's children will live through more decades of accumulating change than anyone reading this &mdash; which is exactly why this site is built to make sense to them too.</p>
      </div>
    </div>

    <div class="layout-2col">
      <div class="prose reveal">
        <h2>The uncomfortable fairness problem</h2>
        <p>Here's the part that doesn't get said often enough: Africa as a whole has contributed a small share of the greenhouse gases that built up in the atmosphere since the Industrial Revolution. Nigeria's own historic emissions are modest by global standards. Yet the impacts &mdash; floods like Mokwa, heat stress across the north, coastal erosion in Lagos &mdash; land hard, because so much of the economy and so many livelihoods depend directly on stable rainfall, farmland and coastlines.</p>
        <p>This is the heart of what's often called <em>climate justice</em>: the places least responsible for causing the problem are frequently among the most exposed to its consequences, and the least equipped, financially, to absorb the shocks.</p>
        <p>It's also exactly why local knowledge, local adaptation, and a new generation of African scientists, engineers and educators matter so much &mdash; this isn't a problem anyone elsewhere is going to solve <em>for</em> Nigeria. It has to be understood, and acted on, from here too.</p>
      </div>
      <aside class="side-card">
        <h4>One honest caveat</h4>
        <p style="font-size:.88rem;">These figures (WHO heat-related mortality estimate, global vulnerability count) are widely cited international estimates, not exact counts &mdash; real-world impacts are hard to measure precisely. Treat them as "this is roughly the scale we're talking about," not a perfectly exact tally.</p>
      </aside>
    </div>
    %s
  </div>
</section>
""" % topic_pager("why-care.html")

page(
    filename="why-care.html",
    title="Why Should We Care?",
    description="Why global warming matters — food, water, health, economy and the climate justice problem facing Nigeria and the wider African continent.",
    active="learn-why",
    hero_html=why_hero,
    body_html=why_body,
)

# =========================================================
# CARBON FOOTPRINT CALCULATOR
# =========================================================
cfp_hero = hero_block(
    eyebrow="Take Action · Tool",
    h1="What's your carbon footprint?",
    lede="A carbon footprint adds up the greenhouse gases linked to your everyday choices &mdash; mainly travel, electricity and food &mdash; into one rough number. This calculator gives you an honest estimate in about two minutes. It's a learning tool, not a scientific audit.",
    ctas_html='<a href="recycle.html" class="btn btn-primary">Next: reduce, reuse, recycle →</a>',
    media_html="", readout_cells=[
        {"label": "Rough world average", "value": "4.7", "decimals": 1, "suffix": " t CO2e/yr", "tone": ""},
        {"label": "Biggest single lever, most people", "value": "1", "decimals": 0, "suffix": " = transport", "tone": "warm"},
    ],
    narrow=True,
)

cfp_body = """
<section class="section">
  <div class="wrap">
    <div class="layout-2col">
      <div class="reveal">
        <form id="footprint-form" class="tool-panel">
          <div class="field">
            <label>Weekly distance by car or motorcycle <span class="field-val"><span id="cf-distance-val">50</span> km/week</span></label>
            <input type="range" id="cf-distance" min="0" max="400" value="50" step="5">
          </div>
          <div class="field">
            <label>Main way you get around</label>
            <select name="transport_mode">
              <option value="walk_cycle">Mostly walk or cycle</option>
              <option value="bus">Mostly public transport / bus</option>
              <option value="motorcycle" selected>Motorcycle / okada</option>
              <option value="car_petrol">Car (petrol)</option>
              <option value="car_diesel">Car (diesel)</option>
            </select>
          </div>
          <div class="field">
            <label>Flights in a typical year</label>
            <div class="radio-row">
              <label><input type="radio" name="flights" value="none" checked> None</label>
              <label><input type="radio" name="flights" value="short"> 1&ndash;2 short flights</label>
              <label><input type="radio" name="flights" value="long"> 3+ / long-haul</label>
            </div>
          </div>
          <div class="field">
            <label>Household electricity use</label>
            <select name="electricity">
              <option value="low">Low &mdash; lights &amp; small appliances mainly</option>
              <option value="medium" selected>Medium &mdash; fridge, fans, regular appliances</option>
              <option value="high">High &mdash; AC, many appliances, large household</option>
            </select>
          </div>
          <div class="field">
            <label>Backup generator use</label>
            <div class="radio-row">
              <label><input type="radio" name="generator" value="none" checked> Rarely / never</label>
              <label><input type="radio" name="generator" value="occasional"> Occasionally</label>
              <label><input type="radio" name="generator" value="frequent"> Frequently</label>
            </div>
          </div>
          <div class="field">
            <label>Typical diet</label>
            <div class="radio-row">
              <label><input type="radio" name="diet" value="plant"> Mostly plant-based</label>
              <label><input type="radio" name="diet" value="balanced" checked> Balanced / mixed</label>
              <label><input type="radio" name="diet" value="meat"> Meat with most meals</label>
            </div>
          </div>
        </form>
      </div>
      <div>
        <div class="result-box reveal" id="cf-result">
          <div class="rb-value"><span id="cf-result-value">0</span></div>
          <div class="rb-label">estimated tonnes CO2e / year</div>
          <div class="result-bar"><span id="cf-result-bar" style="width:0%%"></span></div>
          <p id="cf-result-note" style="color:#D7E4DD;font-size:.85rem;margin-top:14px;text-align:left;"></p>
        </div>
        <div class="callout callout--note" style="margin-top:20px;">
          <span class="callout-label">Reading this honestly</span>
          <p>This is a simplified estimate using broad, illustrative factors &mdash; it's built to teach you which choices move the number most, not to be an exact personal audit. Transport distance, flights and generator use tend to shift it the most.</p>
        </div>
      </div>
    </div>
    %s
  </div>
</section>
""" % topic_pager("carbon-footprint.html")

page(
    filename="carbon-footprint.html",
    title="Carbon Footprint Calculator",
    description="An interactive carbon footprint calculator: estimate your rough annual CO2 footprint from transport, electricity, flights and diet.",
    active="act-cfp",
    hero_html=cfp_hero,
    body_html=cfp_body,
    extra_scripts='<script src="js/calculator.js"></script>',
)

# =========================================================
# RECYCLE
# =========================================================
recycle_hero = hero_block(
    eyebrow="Take Action · Habit",
    h1="Reduce, reuse, recycle &mdash; in that order",
    lede="The three Rs aren't interchangeable; they're a priority list. Reducing what you use in the first place beats reusing, which beats recycling, which still beats throwing away &mdash; and the order matters more than people realise.",
    ctas_html='<a href="clean-energy.html" class="btn btn-primary">Next: clean energy →</a>',
    media_html="", readout_cells=[
        {"label": "Order of priority", "value": "3", "decimals": 0, "suffix": " Rs", "tone": ""},
        {"label": "Energy saved recycling aluminium vs. new", "value": "90", "decimals": 0, "suffix": "%+", "tone": "cool"},
    ],
    narrow=True,
)

recycle_body_main = """
<section class="section">
  <div class="wrap">
    <div class="grid grid-3 reveal">
      <div class="card">
        <span class="tag">1 · Best</span>
        <div class="ico">🛍️</div>
        <h3>Reduce</h3>
        <p>The waste and emissions that never happen are the cheapest kind to deal with. Buy less, choose durable things over disposable ones, and question whether you need a new item at all.</p>
      </div>
      <div class="card">
        <span class="tag">2 · Good</span>
        <div class="ico">🔁</div>
        <h3>Reuse</h3>
        <p>Refill bottles, repair instead of replace, hand things down. Reuse keeps an item's embedded energy and materials working for longer before anything needs reprocessing.</p>
      </div>
      <div class="card">
        <span class="tag">3 · Better than landfill</span>
        <div class="ico">♻️</div>
        <h3>Recycle</h3>
        <p>When something truly can't be reduced or reused further, recycling turns it back into raw material &mdash; using far less energy than mining or manufacturing from scratch.</p>
      </div>
    </div>

    <div class="layout-2col" style="margin-top:40px;">
      <div class="prose reveal">
        <h2>Why recycling actually cuts emissions</h2>
        <p>Making things from raw materials &mdash; mining ore, refining oil into plastic, cutting down trees for paper &mdash; takes a lot of energy, almost always from fossil fuels. Recycling skips most of those early, energy-hungry steps. Recycled aluminium, for example, typically needs a small fraction of the energy that producing new aluminium from ore does. Multiply that across millions of cans, bottles and boxes, and the emissions saved add up fast.</p>
        <h2 style="margin-top:1.4em;">A quick, kid-friendly sorting guide</h2>
        <ul>
          <li><strong>Paper &amp; cardboard</strong> &mdash; flatten boxes, keep them dry.</li>
          <li><strong>Plastic bottles &amp; containers</strong> &mdash; rinse out food residue first.</li>
          <li><strong>Glass &amp; metal cans</strong> &mdash; almost endlessly recyclable without losing quality.</li>
          <li><strong>Organic waste</strong> (peels, leftovers) &mdash; compost where possible instead of binning it; it cuts landfill methane.</li>
          <li><strong>E-waste</strong> (batteries, old phones) &mdash; never bin these; they need specialist handling.</li>
        </ul>
        <div class="callout callout--note">
          <span class="callout-label">The Nigeria angle</span>
          <p>Formal recycling infrastructure is still patchy in much of Nigeria, but a large informal economy of waste pickers and scrap dealers already recovers huge volumes of metal, plastic and paper for resale &mdash; an unglamorous but genuinely important climate contribution worth recognising.</p>
        </div>
      </div>
      <aside class="side-card">
        <h4>Try this at home or school</h4>
        <p style="font-size:.88rem;">Set up three labelled boxes for a week &mdash; Reduce candidates (things you almost didn't need), Reuse, and Recycle. At the end of the week, see which box filled up fastest. It usually says a lot.</p>
      </aside>
    </div>
"""
recycle_body = recycle_body_main + topic_pager("recycle.html") + "</div></section>"

page(
    filename="recycle.html",
    title="Reduce, Reuse, Recycle",
    description="Why the three Rs work in priority order, how recycling cuts emissions, and a simple sorting guide for home or school.",
    active="act-recycle",
    hero_html=recycle_hero,
    body_html=recycle_body,
)

# =========================================================
# CLEAN ENERGY
# =========================================================
energy_hero = hero_block(
    eyebrow="Take Action · Future",
    h1="Clean energy: the quiet revolution already under way",
    lede="Solar panels and wind turbines aren't a future idea anymore &mdash; they're the fastest-growing source of new electricity on Earth, and Nigeria has some of the best untapped sunlight on the planet to work with.",
    ctas_html='<a href="action-hub.html" class="btn btn-primary">Next: the Action Hub →</a>',
    media_html='<img src="https://commons.wikimedia.org/wiki/Special:FilePath/Solar_panel_installer.jpg?width=900" alt="A solar panel installer at work in Nigeria">' + img_credit("Solar installation, Nigeria · Wiki Loves Africa, Wikimedia Commons (CC BY-SA 4.0)"),
    readout_cells=[
        {"label": "Renewables, world electricity, 2025", "value": "34", "decimals": 0, "suffix": "%", "tone": "cool"},
        {"label": "...a decade earlier", "value": "23", "decimals": 0, "suffix": "%", "tone": ""},
        {"label": "Solar + wind, 2025 share", "value": "17", "decimals": 0, "suffix": "%", "tone": "cool"},
    ],
)

energy_body = """
<section class="section">
  <div class="wrap">
    <div class="grid grid-3 reveal">
      <div class="card"><div class="ico">☀️</div><h3>Solar</h3><p>Photovoltaic panels turn sunlight directly into electricity. Costs have fallen so far, so fast, that solar is now the cheapest new electricity source in much of the world &mdash; including across Africa.</p></div>
      <div class="card"><div class="ico">🌬️</div><h3>Wind</h3><p>Turbines convert moving air into electricity with no fuel and no emissions during operation. Onshore and offshore wind together now supply a meaningful slice of global power.</p></div>
      <div class="card"><div class="ico">💧</div><h3>Hydro, geothermal &amp; biomass</h3><p>Flowing water, underground heat, and organic material round out the renewable mix &mdash; each suited to different geographies and grids.</p></div>
    </div>

    <div class="reveal" style="margin:36px 0;">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Wind_turbines_(Adair_Wind_Farm,_Iowa,_USA)_3_(48916255452).jpg?width=1200" alt="Rows of wind turbines at a wind farm" style="border-radius:var(--radius);border:1px solid var(--line-soft);">
      <p class="muted" style="font-size:.8rem;margin-top:8px;">Wind turbines at a wind farm · via Wikimedia Commons</p>
    </div>

    <div class="layout-2col">
      <div class="prose reveal">
        <h2>Why this matters for the climate fight</h2>
        <p>Electricity generation is the single largest source of human greenhouse gas emissions (see Causes). Swapping fossil-fuelled generation for solar, wind and other renewables is the most direct lever available for cutting that number &mdash; and it's already happening faster than most people realise: renewables supplied about 34%% of the world's electricity in 2025, up from roughly 23%% just a decade earlier. Coal-fired generation, long the largest single source, is now being overtaken.</p>
        <h2 style="margin-top:1.4em;">Nigeria's particular opportunity</h2>
        <p>Nigeria sits in one of the sunniest belts on Earth, and millions of homes and businesses already rely on diesel generators for power that's expensive, noisy and polluting. Off-grid and mini-grid solar &mdash; sometimes paired with battery storage &mdash; is increasingly filling that gap directly, skipping the need for a country-spanning grid to reach communities that need power now.</p>
        <div class="callout callout--try">
          <span class="callout-label">Try this</span>
          <p>Next time the power goes out, time how long it takes for a solar lantern or solar phone charger to top back up the next sunny day. It's a small, very concrete demonstration of energy that costs nothing to "refuel."</p>
        </div>
      </div>
      <aside class="side-card">
        <h4>Worth knowing</h4>
        <div class="fact-strip" style="flex-direction:column;">
          <div class="fact"><div class="fv">700GW+</div><div class="fl">Renewable capacity added worldwide in 2024 alone</div></div>
          <div class="fact"><div class="fv">22</div><div class="fl">Consecutive years of record renewable capacity growth</div></div>
        </div>
      </aside>
    </div>
    %s
  </div>
</section>
""" % topic_pager("clean-energy.html")

page(
    filename="clean-energy.html",
    title="Clean Energy",
    description="How solar, wind and other renewables work, why they cut emissions, and Nigeria's growing off-grid solar opportunity.",
    active="act-energy",
    hero_html=energy_hero,
    body_html=energy_body,
)

# =========================================================
# ACTION HUB
# =========================================================
hub_hero = hero_block(
    eyebrow="Take Action · Checklist",
    h1="The Action Hub",
    lede="Reading about climate change is step one. This page is step two: a real, tickable list of things you can actually do at school, at home, and in your community &mdash; starting today.",
    ctas_html='<a href="data-explorer.html" class="btn btn-primary">Next: explore the data →</a>',
    media_html="", readout_cells=[
        {"label": "Actions on this page", "value": "16", "decimals": 0, "suffix": "", "tone": ""},
        {"label": "Cost to start most of them", "value": "0", "decimals": 0, "prefix": "₦", "suffix": "", "tone": "cool"},
    ],
    narrow=True,
)

hub_body = """
<section class="section">
  <div class="wrap">
    <div class="impact-meter reveal">
      <span class="im-count"><span id="impact-count">0</span> / <span id="impact-total">16</span></span>
      <span class="muted">actions checked off &mdash; come back any time and keep going.</span>
    </div>

    <div class="explore-group reveal">
      <h4>🏫 At school</h4>
      <ul class="checklist">
        <li><input type="checkbox"><div><div class="ct-title">Start or join a climate / eco club</div><div class="ct-desc">Even three or four students meeting monthly can run real projects.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Run a school recycling or composting point</div><div class="ct-desc">Start with one bin and one habit — paper, plastic or food waste.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Teach this topic to a younger class</div><div class="ct-desc">Explaining something is one of the fastest ways to really learn it.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Ask for a school garden or tree-planting day</div><div class="ct-desc">Trees absorb CO2 as they grow, and shade cuts cooling costs too.</div></div></li>
      </ul>
    </div>

    <div class="explore-group reveal">
      <h4>🏠 At home</h4>
      <ul class="checklist">
        <li><input type="checkbox"><div><div class="ct-title">Turn off lights, fans and chargers when not in use</div><div class="ct-desc">Small, but it's the easiest habit to start today.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Try one no-generator evening a week</div><div class="ct-desc">See how far solar lanterns or daylight hours stretch it.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Start a kitchen compost or food-waste habit</div><div class="ct-desc">Cuts methane from landfill and can feed a garden.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Walk, cycle or share transport for short trips</div><div class="ct-desc">The single biggest lever in most personal footprints.</div></div></li>
      </ul>
    </div>

    <div class="explore-group reveal">
      <h4>🤝 In your community</h4>
      <ul class="checklist">
        <li><input type="checkbox"><div><div class="ct-title">Join or organise a community clean-up</div><div class="ct-desc">Cleared drains flood less — directly relevant after 2025's floods.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Support local recycling or scrap collectors</div><div class="ct-desc">They're already doing real climate work — value it.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Share what you learn here with family or friends</div><div class="ct-desc">Understanding spreads faster than almost anything else.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Back local tree-planting or green spaces</div><div class="ct-desc">Green cover helps with flooding, heat and air quality together.</div></div></li>
      </ul>
    </div>

    <div class="explore-group reveal">
      <h4>🗳️ As a future leader / voter</h4>
      <ul class="checklist">
        <li><input type="checkbox"><div><div class="ct-title">Follow what NiMet and NEMA say about local risk</div><div class="ct-desc">Early warnings only help if people actually read them.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Ask questions about local flood and waste planning</div><div class="ct-desc">Good infrastructure decisions reduce disaster damage hugely.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Consider a STEM, climate or environmental path</div><div class="ct-desc">Africa needs more of its own scientists and engineers on this.</div></div></li>
        <li><input type="checkbox"><div><div class="ct-title">Keep learning — re-take the quiz in a few weeks</div><div class="ct-desc">See how much more sticks the second time around.</div></div></li>
      </ul>
    </div>

    <div class="callout callout--try reveal" style="text-align:center;">
      <span class="callout-label">Want a printable copy?</span>
      <p>Use your browser's print option to save this checklist as a PDF or paper copy for school or home.</p>
      <button class="btn btn-ghost print-btn" onclick="window.print()" style="margin-top:8px;">🖨️ Print this page</button>
    </div>
    %s
  </div>
</section>
""" % topic_pager("action-hub.html")

page(
    filename="action-hub.html",
    title="Action Hub",
    description="A real, tickable checklist of climate actions for school, home, community and future leadership.",
    active="act-hub",
    hero_html=hub_hero,
    body_html=hub_body,
    extra_scripts='<script src="js/checklist.js"></script>',
)

# =========================================================
# DATA EXPLORER
# =========================================================
data_hero = hero_block(
    eyebrow="Go further · Data",
    h1="The Data Explorer",
    lede="Three real, sourced datasets, visualised: the long climb of atmospheric CO2, the warmest years on record, and how fast renewables are growing &mdash; plus Nigeria's own 2025 flood numbers.",
    ctas_html='<a href="quiz.html" class="btn btn-primary">Next: take the quiz →</a>',
    media_html="", readout_cells=[
        {"label": "CO2, Mauna Loa, 2025", "value": "427.4", "decimals": 1, "suffix": " ppm", "tone": "warm"},
        {"label": "3 warmest years on record", "value": "2023", "decimals": 0, "suffix": "&ndash;25", "tone": "alert"},
    ],
    narrow=True,
)

data_body = """
<section class="section">
  <div class="wrap">
    <div class="chart-card reveal">
      <h3>🌤️ Today's weather</h3>
      <p class="chart-meta">Live, right now &mdash; defaults to Ibadan, or search any city</p>
      <div id="weather-mount"></div>
      <p class="source-note">Weather data: <a href="https://open-meteo.com/" target="_blank" rel="noopener">Open-Meteo</a> (free, no key, CC BY 4.0). One important distinction: this is <strong>weather</strong> &mdash; today, one place. The charts below are <strong>climate</strong> &mdash; decades, the whole planet. A hot or rainy day here says nothing about global warming on its own; see <a href="what-is-global-warming.html">Weather vs. Climate</a>.</p>
    </div>

    <div class="chart-card reveal">
      <h3>Atmospheric CO2 is still climbing</h3>
      <p class="chart-meta">Annual mean CO2 concentration, Mauna Loa Observatory, Hawaii (parts per million)</p>
      <div class="chart-wrap"><canvas id="chart-co2"></canvas></div>
      <p class="source-note">Source: NOAA Global Monitoring Laboratory, Mauna Loa Observatory annual mean CO2 records.</p>
    </div>

    <div class="chart-card reveal">
      <h3>2023, 2024 and 2025: the three warmest years on record</h3>
      <p class="chart-meta">Global surface temperature anomaly vs. the 20th-century (1901&ndash;2000) average</p>
      <div class="chart-wrap"><canvas id="chart-warm"></canvas></div>
      <p class="source-note">Source: NOAA National Centers for Environmental Information (NCEI), annual global climate reports. The ten warmest years on record have all occurred since 2015.</p>
    </div>

    <div class="chart-card reveal">
      <h3>Renewables are closing in on coal</h3>
      <p class="chart-meta">Share of global electricity generation from renewable sources</p>
      <div style="display:grid;gap:14px;margin-top:10px;">
        <div><div style="display:flex;justify-content:space-between;font-size:.85rem;font-weight:700;margin-bottom:4px;"><span>~2015</span><span>23%</span></div><div class="result-bar" style="background:var(--line-soft);"><span style="width:23%;background:var(--teal-200);"></span></div></div>
        <div><div style="display:flex;justify-content:space-between;font-size:.85rem;font-weight:700;margin-bottom:4px;"><span>2024</span><span>32%</span></div><div class="result-bar" style="background:var(--line-soft);"><span style="width:32%;"></span></div></div>
        <div><div style="display:flex;justify-content:space-between;font-size:.85rem;font-weight:700;margin-bottom:4px;"><span>2025</span><span>34%</span></div><div class="result-bar" style="background:var(--line-soft);"><span style="width:34%;"></span></div></div>
      </div>
      <p class="source-note">Source: International Energy Agency, Global Energy Review 2026 — electricity supply.</p>
    </div>

    <div class="chart-card reveal">
      <h3>Nigeria, 2025: a year of climate extremes</h3>
      <div class="fact-strip" style="margin-top:6px;">
        <div class="fact"><div class="fv">30 / 36</div><div class="fl">states flagged at high flood risk</div></div>
        <div class="fact"><div class="fv">~15M</div><div class="fl">Nigerians estimated at flood risk</div></div>
        <div class="fact"><div class="fv">42°C</div><div class="fl">peak heat recorded in the north</div></div>
        <div class="fact"><div class="fv">35M</div><div class="fl">people projected at food-insecurity risk into 2026</div></div>
      </div>
      <p class="source-note">Sources: Nigeria's 2025 Annual Flood Outlook (NIHSA/NEMA), NiMet heat advisories, WFP food security projections.</p>
    </div>
  </div>
</section>
"""

page(
    filename="data-explorer.html",
    title="Data Explorer",
    description="Live weather plus real, sourced climate data: the CO2 curve, the warmest years on record, renewables growth, and Nigeria's 2025 flood numbers.",
    active="data",
    hero_html=data_hero,
    body_html=data_body,
    extra_scripts='<script src="js/weather.js"></script>\n<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>\n<script src="js/charts.js"></script>',
)

# =========================================================
# QUIZ
# =========================================================
quiz_hero = hero_block(
    eyebrow="Go further · 10 questions",
    h1="The Climate Explorer Quiz",
    lede="Ten questions pulled straight from this guide &mdash; some easy, some sneaky. Built for explorers of every age. No score is saved anywhere; just play, learn, and try again whenever you like.",
    ctas_html='<a href="glossary.html" class="btn btn-primary">Next: the glossary →</a>',
    media_html="", readout_cells=[
        {"label": "Questions", "value": "10", "decimals": 0, "suffix": "", "tone": ""},
        {"label": "Time to play", "value": "3", "decimals": 0, "suffix": " min", "tone": "cool"},
    ],
    narrow=True,
)

quiz_body = """
<section class="section">
  <div class="wrap" style="max-width:760px;">
    <div class="quiz-card reveal" id="quiz-mount"></div>
  </div>
</section>
"""

page(
    filename="quiz.html",
    title="Quiz",
    description="A 10-question interactive quiz testing what you've learned about global warming — built for explorers of every age.",
    active="quiz",
    hero_html=quiz_hero,
    body_html=quiz_body,
    extra_scripts='<script src="js/quiz.js"></script>',
)

# =========================================================
# GLOSSARY
# =========================================================
glossary_hero = hero_block(
    eyebrow="Go further · A&ndash;Z",
    h1="Glossary &amp; sources",
    lede="Every tricky term used across this site, explained simply &mdash; plus where the numbers and facts actually came from.",
    ctas_html='<a href="about.html" class="btn btn-primary">Meet your guide →</a>',
    media_html="", readout_cells=[
        {"label": "Terms explained", "value": "24", "decimals": 0, "suffix": "", "tone": ""},
    ],
    narrow=True,
)

GLOSSARY_TERMS = [
    ("A", "Adaptation", "Changing how we live or build to cope with a climate that's already shifting — like raising buildings above flood level."),
    ("A", "Albedo", "How much sunlight a surface reflects rather than absorbs. Fresh snow has high albedo (reflects a lot); dark ocean water has low albedo (absorbs a lot)."),
    ("B", "Biodegradable", "Material that natural processes can break down over time, like food waste or paper — unlike most plastics."),
    ("C", "Carbon footprint", "The total greenhouse gases a person, product or activity is responsible for, usually measured in tonnes of CO2-equivalent per year."),
    ("C", "Carbon sequestration", "Capturing and storing carbon so it doesn't stay in the atmosphere — trees and soil do this naturally; some technologies try to do it artificially."),
    ("C", "Climate", "The long-term, averaged pattern of weather in a place, typically measured over 30 years."),
    ("C", "Climate justice", "The idea that the people and countries who've contributed least to climate change often suffer its worst effects — and that responses should account for that imbalance."),
    ("D", "Deforestation", "Clearing forest land, which removes a major carbon-absorbing resource and often releases stored carbon back into the air."),
    ("E", "El Niño / La Niña", "Natural, multi-year ocean-temperature cycles in the Pacific that shift weather patterns worldwide — separate from, but layered on top of, long-term global warming."),
    ("E", "Emissions", "Greenhouse gases released into the atmosphere, usually from burning fuel, farming, or industrial processes."),
    ("F", "Fossil fuel", "Coal, oil and natural gas — formed from ancient organic matter over millions of years, and the largest source of human-caused emissions when burned."),
    ("G", "Greenhouse effect", "The natural process by which certain gases trap heat in Earth's atmosphere, keeping the planet warm enough to support life."),
    ("G", "Greenhouse gas", "Any gas that traps heat in the atmosphere — mainly carbon dioxide (CO2), methane, nitrous oxide and water vapour."),
    ("I", "IPCC", "The Intergovernmental Panel on Climate Change — the United Nations body that reviews and summarises the global scientific research on climate change."),
    ("M", "Methane", "A greenhouse gas released by livestock, rice farming, landfills and gas leaks — far more potent than CO2 per molecule, though it breaks down faster."),
    ("M", "Mitigation", "Action taken to reduce or prevent greenhouse gas emissions in the first place, as opposed to adapting to effects that are already happening."),
    ("N", "Net zero", "A state where any remaining greenhouse gas emissions are balanced out by removals — through forests, technology, or other means — so the net addition to the atmosphere is zero."),
    ("O", "Ocean acidification", "Oceans absorbing extra CO2 from the air, which makes seawater more acidic and stresses coral reefs and shellfish."),
    ("P", "Paris Agreement", "A 2015 international agreement where countries committed to limit global warming, broadly to well below 2°C above pre-industrial levels."),
    ("P", "ppm (parts per million)", "A way of measuring tiny concentrations — 427 ppm of CO2 means 427 out of every one million air molecules are CO2."),
    ("P", "Pre-industrial baseline", "Conditions before large-scale fossil fuel use began (roughly 1850&ndash;1900), used as the comparison point for how much warming has happened since."),
    ("R", "Renewable energy", "Energy from sources that naturally replenish, like sunlight, wind, and flowing water, instead of being extracted and burned."),
    ("S", "Sea level rise", "The long-term increase in ocean height caused by melting ice and seawater expanding as it warms."),
    ("W", "Weather", "What's happening in the atmosphere right now or over the next few days — distinct from the long-term pattern that defines climate."),
]

def glossary_dl():
    parts = []
    seen_letters = set()
    for letter, term, definition in GLOSSARY_TERMS:
        anchor = ('<span id="letter-%s"></span>' % letter) if letter not in seen_letters else ""
        seen_letters.add(letter)
        parts.append('<div class="gloss-item">%s<dt>%s</dt><dd>%s</dd></div>' % (anchor, term, definition))
    return "\n".join(parts)

def az_jump():
    letters = sorted(set(l for l, _, _ in GLOSSARY_TERMS))
    return "\n".join('<a href="#letter-%s">%s</a>' % (l, l) for l in letters)

glossary_body = """
<section class="section">
  <div class="wrap">
    <div class="layout-2col">
      <div class="reveal">
        <div class="az-jump">%s</div>
        <dl class="glossary-grid">
          %s
        </dl>
      </div>
      <aside class="side-card">
        <h4>Sources &amp; further reading</h4>
        <ul style="display:grid;gap:14px;">
          <li><a href="https://science.nasa.gov/earth/explore/earth-indicators/global-temperature/" target="_blank" rel="noopener">NASA GISS &mdash; Global Temperature</a><br><span class="muted" style="font-size:.8rem;">Long-running global surface temperature analysis.</span></li>
          <li><a href="https://www.ncei.noaa.gov/" target="_blank" rel="noopener">NOAA NCEI &mdash; Global Climate Reports</a><br><span class="muted" style="font-size:.8rem;">Monthly and annual global climate summaries.</span></li>
          <li><a href="https://gml.noaa.gov/ccgg/trends/" target="_blank" rel="noopener">NOAA Global Monitoring Laboratory</a><br><span class="muted" style="font-size:.8rem;">Mauna Loa Observatory's atmospheric CO2 record.</span></li>
          <li><a href="https://www.iea.org/" target="_blank" rel="noopener">International Energy Agency (IEA)</a><br><span class="muted" style="font-size:.8rem;">Annual data on global electricity and renewables.</span></li>
          <li><a href="https://www.ipcc.ch/" target="_blank" rel="noopener">IPCC</a><br><span class="muted" style="font-size:.8rem;">The UN's scientific climate assessment body.</span></li>
          <li><span style="font-weight:700;">NiMet &amp; NEMA, Nigeria</span><br><span class="muted" style="font-size:.8rem;">National weather warnings and disaster response data referenced on the Effects and Data Explorer pages.</span></li>
        </ul>
      </aside>
    </div>
  </div>
</section>
""" % (az_jump(), glossary_dl())

page(
    filename="glossary.html",
    title="Glossary & Sources",
    description="A simple A-to-Z glossary of climate terms, plus the sources behind every statistic used on this site.",
    active="glossary",
    hero_html=glossary_hero,
    body_html=glossary_body,
)

# =========================================================
# ABOUT
# =========================================================
about_hero = hero_block(
    eyebrow="Meet your guide",
    h1="Babatunde Ayoola Awoyemi",
    lede="Physicist, STEM educator, and Lead Consultant at Techbase Consultant Services in Ibadan, Nigeria &mdash; and the person who built this whole guide, twice.",
    ctas_html='<a href="https://babatundeawo.github.io/" class="btn btn-primary" target="_blank" rel="noopener">View my full portfolio →</a>'
              '<a href="https://github.com/babatundeawo" class="btn btn-ghost" target="_blank" rel="noopener">GitHub →</a>',
    media_html="", readout_cells=[
        {"label": "Base", "value": "Ibadan", "decimals": 0, "suffix": ", Nigeria", "tone": ""},
        {"label": "Field", "value": "Atmospheric", "decimals": 0, "suffix": " Physics", "tone": "cool"},
    ],
    narrow=True,
)

about_body = """
<section class="section">
  <div class="wrap">
    <div class="layout-2col">
      <div>
        <div class="avatar-frame reveal">
          <img src="images/profile/babatunde.jpg" alt="Babatunde Ayoola Awoyemi" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
          <div class="initials" style="display:none;width:100%;height:100%;align-items:center;justify-content:center;">BA</div>
        </div>
        <ul class="credential-list">
          <li><span class="dot"></span> B.Sc. Physics, University of Ibadan (2014)</li>
          <li><span class="dot"></span> M.Sc. Atmospheric Physics, University of Ibadan (2019)</li>
          <li><span class="dot"></span> Research: satellite (MODIS/CERES) &amp; ground-based solar radiation modelling</li>
          <li><span class="dot"></span> Published researcher — direct solar irradiance estimation under all-sky conditions (2020)</li>
          <li><span class="dot"></span> Lead Consultant, Techbase Consultant Services</li>
          <li><span class="dot"></span> Volunteer STEM educator, RCCG Kingdom Diplomats Youth Church</li>
        </ul>
      </div>
      <div class="prose reveal">
        <h2>From a classroom slide deck to an open learning project</h2>
        <p>Years ago, I put together a presentation on global warming for a student to use in class. He never came back for it, and the files sat untouched for a long time. Rebuilding it felt like the right way to put that work to use &mdash; not as a one-off assignment, but as something anyone curious about climate change could explore, learn from, and act on.</p>
        <p>My own background is in atmospheric physics &mdash; I studied how sunlight and heat move through the atmosphere, and how satellites like MODIS and CERES help us measure it from space. That's part of why this site leans on real instrument-style numbers wherever it can, rather than vague claims: it's how I was trained to think about the atmosphere in the first place.</p>
        <p>Outside of climate and physics, I run <strong>Techbase Consultant Services</strong>, where I work across IT consultancy, web development, robotics, and &mdash; closest to my heart &mdash; STEM education for young people across Nigeria. I also teach and help build curriculum at my church, and spend a fair amount of free time on photography, football, and long drives.</p>
        <h2 style="margin-top:1.2em;">A few other things I've built</h2>
        <div class="project-strip">
          <a href="https://babatundeawo.github.io/ai-prompt-library/" target="_blank" rel="noopener"><span>AI Prompt Library &mdash; 200+ curated, searchable prompts</span><span>↗</span></a>
          <a href="https://babatundeawo.github.io/ai-studio-android-guide/" target="_blank" rel="noopener"><span>AI Studio Android Guide</span><span>↗</span></a>
          <a href="https://babatundeawo.github.io/career-engine-guide/" target="_blank" rel="noopener"><span>Personal AI Career Engine &mdash; a guided career-building system</span><span>↗</span></a>
          <a href="https://techbaseng.github.io/" target="_blank" rel="noopener"><span>Techbase STEM Academy &mdash; courses, Scratch &amp; robotics lessons</span><span>↗</span></a>
        </div>
        <a href="https://babatundeawo.github.io/" target="_blank" rel="noopener" class="btn btn-amber" style="margin-top:20px;width:100%;justify-content:center;">🔗 See everything I've built &mdash; My Portfolio →</a>
        <div class="callout callout--note" style="margin-top:28px;">
          <span class="callout-label">A note for whoever's reading this</span>
          <p>If you're a teacher, student, or just someone who stumbled in here &mdash; this site is free to use, copy and remix for learning. If it helps you explain climate change to someone else, it's done its job.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

page(
    filename="about.html",
    title="About",
    description="Meet Babatunde Ayoola Awoyemi — physicist, STEM educator, and Lead Consultant at Techbase Consultant Services — the creator of this guide.",
    active="about",
    hero_html=about_hero,
    body_html=about_body,
)

print("ALL PAGES BUILT")

# =========================================================
# COURSE MODULE: 8 lessons, course index, for-teachers, certificate
# =========================================================

def lesson_pager(num):
    prev_html = '<span></span>'
    next_html = '<a class="pager-link next" href="course.html"><span class="pl-dir">Finished →</span><div class="pl-title">Back to course overview</div></a>'
    if num > 1:
        prev_html = '<a class="pager-link prev" href="lesson-%d.html"><span class="pl-dir">← Previous</span><div class="pl-title">Lesson %d</div></a>' % (num - 1, num - 1)
    if num < 8:
        next_html = '<a class="pager-link next" href="lesson-%d.html"><span class="pl-dir">Next →</span><div class="pl-title">Lesson %d</div></a>' % (num + 1, num + 1)
    return '<div class="lesson-pager">%s%s</div>' % (prev_html, next_html)


LESSONS = [
    {
        "num": 1, "title": "The Greenhouse Effect", "minutes": 15,
        "objective": "Explain, in your own words, why greenhouse gases cause warming.",
        "source_href": "what-is-global-warming.html", "source_title": "What Is Global Warming?",
        "summary": """<p>Sunlight passes through the atmosphere easily and warms the ground. The warmed Earth radiates that energy back out as heat. Some heat escapes to space, but greenhouse gases like CO2 absorb part of it and send it back down &mdash; like a blanket holding body heat in.</p>
        <p>CO2 has risen from about 280 ppm before the Industrial Revolution to roughly 427 ppm in 2025 &mdash; about a 50% increase. More greenhouse gas means more trapped heat, all the time, everywhere.</p>""" + GREENHOUSE_SVG,
        "worksheet": """
        <div class="ws-q">
          <label>1. Fill in the blanks</label>
          <p>Greenhouse gases let <span class="ws-blank"></span> pass through easily, but trap some of the <span class="ws-blank"></span> that radiates back up from the ground.</p>
        </div>
        <div class="ws-q">
          <label>2. Short answer</label>
          <p>Why is the rise from 280 ppm to 427 ppm of CO2 a big deal, even though it still sounds like a small number?</p>
          <div class="ws-line"></div><div class="ws-line"></div>
        </div>
        <div class="ws-q">
          <label>3. Try the experiment</label>
          <p>Do the jar-and-thermometer activity from the <em>What Is Global Warming?</em> page. Record both readings:</p>
          <p>Open air temperature: <span class="ws-blank"></span> &nbsp;&nbsp; Inside the jar: <span class="ws-blank"></span></p>
        </div>""",
    },
    {
        "num": 2, "title": "Causes of Global Warming", "minutes": 15,
        "objective": "List the top human causes of greenhouse gas emissions, in order of scale.",
        "source_href": "causes.html", "source_title": "Causes of Global Warming",
        "summary": """<p>Most human-caused emissions come from burning fossil fuels for electricity, heat and transport. Industry, agriculture &amp; land use, and waste add the rest &mdash; roughly in that order of scale.</p>
        <p>It isn't just how much we emit, but how fast: humans have added in a little over a century roughly what natural processes used to take millennia to balance.</p>""",
        "worksheet": """
        <div class="ws-q">
          <label>1. Rank these from biggest to smallest source of global emissions</label>
          <p>(Write 1&ndash;5 next to each: Waste, Transport, Electricity &amp; heat, Agriculture &amp; land use, Industry)</p>
          <p>Electricity &amp; heat <span class="ws-blank"></span> &nbsp; Transport <span class="ws-blank"></span> &nbsp; Industry <span class="ws-blank"></span> &nbsp; Agriculture &amp; land use <span class="ws-blank"></span> &nbsp; Waste <span class="ws-blank"></span></p>
        </div>
        <div class="ws-q">
          <label>2. Short answer</label>
          <p>Pick one cause above. Describe one realistic way someone in your own community could help reduce it.</p>
          <div class="ws-line"></div><div class="ws-line"></div>
        </div>""",
    },
    {
        "num": 3, "title": "Effects: Worldwide and at Home", "minutes": 18,
        "objective": "Describe at least three effects of global warming, including one local to Nigeria.",
        "source_href": "effects.html", "source_title": "Effects, Worldwide and at Home",
        "summary": """<p>Worldwide: rising temperatures (2025 was the third-warmest year on record), melting ice, rising seas, and fiercer storms.</p>
        <p>In Nigeria, 2025 brought both extremes: devastating floods (Mokwa, Niger State, among the worst in decades) affecting roughly 15 million people at risk across 30 of 36 states &mdash; and, at the same time, severe heat past 40&deg;C in the north that disrupted planting season.</p>""",
        "worksheet": """
        <div class="ws-q">
          <label>1. Match the effect to its description</label>
          <table>
            <tr><th>Effect</th><th>Write the matching letter</th></tr>
            <tr><td>Melting Arctic ice</td><td><span class="ws-blank"></span></td></tr>
            <tr><td>Mokwa flood (2025)</td><td><span class="ws-blank"></span></td></tr>
            <tr><td>Northern heat stress</td><td><span class="ws-blank"></span></td></tr>
          </table>
          <p style="font-size:.82rem;margin-top:8px;">A) Temperatures past 40&deg;C disrupted planting season &nbsp; B) Sea ice in 2025 was the second-lowest on record &nbsp; C) Among the worst flash floods the area has seen in decades</p>
        </div>
        <div class="ws-q">
          <label>2. Short answer</label>
          <p>Name one effect of global warming that you or your family have noticed personally, even a small one.</p>
          <div class="ws-line"></div>
        </div>""",
    },
    {
        "num": 4, "title": "Why Should We Care?", "minutes": 15,
        "objective": "Explain the climate justice problem in your own words.",
        "source_href": "why-care.html", "source_title": "Why Should We Care?",
        "summary": """<p>Climate change reaches food, water, health, jobs and ecosystems all at once. Africa has historically contributed a small share of global emissions, yet faces some of the heaviest impacts &mdash; because so many livelihoods depend directly on stable rainfall, farmland and coastlines. That mismatch is what's often called <em>climate justice</em>.</p>""",
        "worksheet": """
        <div class="ws-q">
          <label>1. Short answer</label>
          <p>In your own words, what does "climate justice" mean?</p>
          <div class="ws-line"></div><div class="ws-line"></div>
        </div>
        <div class="ws-q">
          <label>2. Discussion (pairs or small group)</label>
          <p>Is it fair that countries who emitted the least are often hit hardest? What, if anything, should change about that?</p>
          <div class="ws-line"></div><div class="ws-line"></div><div class="ws-line"></div>
        </div>""",
    },
    {
        "num": 5, "title": "Your Carbon Footprint", "minutes": 15,
        "objective": "Calculate and interpret your own rough carbon footprint.",
        "source_href": "carbon-footprint.html", "source_title": "Your Carbon Footprint",
        "summary": """<p>A carbon footprint adds up the greenhouse gases linked to your transport, electricity and food choices into one rough yearly number, usually in tonnes of CO2-equivalent. The rough global average is about 4.7 tonnes per person per year &mdash; transport, flights and generator use usually move the number the most.</p>""",
        "worksheet": """
        <div class="ws-q">
          <label>1. Use the Carbon Footprint Calculator</label>
          <p>My estimated footprint: <span class="ws-blank"></span> tonnes CO2e/year</p>
        </div>
        <div class="ws-q">
          <label>2. Identify</label>
          <p>Which single input (transport, flights, electricity, generator, or diet) moved your number the most when you changed it?</p>
          <div class="ws-line"></div>
        </div>
        <div class="ws-q">
          <label>3. Commit</label>
          <p>Write one realistic change you could make this month, and re-run the calculator with it.</p>
          <div class="ws-line"></div>
        </div>""",
    },
    {
        "num": 6, "title": "Reduce, Reuse, Recycle", "minutes": 15,
        "objective": "Apply the three Rs, in priority order, to real examples.",
        "source_href": "recycle.html", "source_title": "Reduce, Reuse, Recycle",
        "summary": """<p>The three Rs are a priority order, not interchangeable options: reducing what you use beats reusing it, which beats recycling it, which still beats throwing it away. Recycling works because reprocessing used material almost always takes far less energy than starting from raw ore, oil or trees.</p>""",
        "worksheet": """
        <div class="ws-q">
          <label>1. Sort these into the right column: plastic bottle, school exercise book, banana peel, old phone, glass jar, plastic bag</label>
          <table>
            <tr><th>Reduce</th><th>Reuse</th><th>Recycle</th></tr>
            <tr><td style="height:60px;"></td><td></td><td></td></tr>
          </table>
        </div>
        <div class="ws-q">
          <label>2. Short answer</label>
          <p>Why does recycling aluminium use so much less energy than making it from raw ore?</p>
          <div class="ws-line"></div>
        </div>""",
    },
    {
        "num": 7, "title": "Clean Energy", "minutes": 15,
        "objective": "Compare two renewable energy sources and explain why Nigeria suits solar.",
        "source_href": "clean-energy.html", "source_title": "Clean Energy",
        "summary": """<p>Solar and wind convert sunlight and moving air directly into electricity, with no fuel burned during operation. Renewables reached about 34% of the world's electricity in 2025, up from roughly 23% a decade earlier. Nigeria sits in a sunny belt and already relies heavily on diesel generators &mdash; making off-grid solar a particularly direct, practical opportunity.</p>""",
        "worksheet": """
        <div class="ws-q">
          <label>1. Compare</label>
          <p>Solar needs: <span class="ws-blank"></span> &nbsp;&nbsp; Wind needs: <span class="ws-blank"></span></p>
          <p>One advantage solar has for Nigeria specifically: <span class="ws-blank"></span></p>
        </div>
        <div class="ws-q">
          <label>2. Fill in the stat</label>
          <p>In 2025, renewables supplied about <span class="ws-blank"></span>% of the world's electricity.</p>
        </div>""",
    },
    {
        "num": 8, "title": "Taking Action", "minutes": 20,
        "objective": "Commit to and track real personal or community climate actions.",
        "source_href": "action-hub.html", "source_title": "Action Hub",
        "summary": """<p>Understanding the problem is step one; doing something is step two. The Action Hub lists real, tickable actions across school, home, community, and future leadership &mdash; most of them free to start today.</p>""",
        "worksheet": """
        <div class="ws-q">
          <label>1. Choose 3 actions from the Action Hub checklist</label>
          <table>
            <tr><th>Action</th><th>When I'll start</th><th>How I'll know it worked</th></tr>
            <tr><td style="height:40px;"></td><td></td><td></td></tr>
            <tr><td style="height:40px;"></td><td></td><td></td></tr>
            <tr><td style="height:40px;"></td><td></td><td></td></tr>
          </table>
        </div>
        <div class="ws-q">
          <label>2. Reflection</label>
          <p>After this course, what's the one idea you'll remember a year from now?</p>
          <div class="ws-line"></div><div class="ws-line"></div>
        </div>""",
    },
]


def lesson_hero(lesson):
    return hero_block(
        eyebrow="Guided Course · Lesson %d of 8" % lesson["num"],
        h1=lesson["title"],
        lede=lesson["objective"],
        ctas_html='<a href="%s" class="btn btn-ghost">Read the full page →</a>' % lesson["source_href"],
        media_html="", readout_cells=[
            {"label": "Estimated time", "value": lesson["minutes"], "decimals": 0, "suffix": " min", "tone": ""},
            {"label": "Lesson", "value": lesson["num"], "decimals": 0, "suffix": " of 8", "tone": "cool"},
        ],
        narrow=True,
    )


for lesson in LESSONS:
    body = """
<section class="section">
  <div class="wrap" style="max-width:780px;">
    <div class="objective-box reveal">
      <span class="ob-ico">🎯</span>
      <div><span class="ob-label">Learning objective</span><p>%s</p></div>
    </div>
    <div class="prose reveal">%s</div>

    <div class="complete-box reveal">
      <button class="btn btn-primary" id="mark-complete-btn" data-lesson="%d">Mark this lesson complete</button>
      <span id="complete-status"></span>
    </div>

    <div class="worksheet reveal">
      <h3>📝 Worksheet — Lesson %d</h3>
      %s
    </div>

    <div class="callout callout--note reveal print-btn" style="text-align:center;">
      <button class="btn btn-ghost" onclick="window.print()">🖨️ Print this lesson + worksheet</button>
    </div>
    %s
  </div>
</section>
""" % (
        lesson["objective"], lesson["summary"], lesson["num"], lesson["num"],
        lesson["worksheet"], lesson_pager(lesson["num"]),
    )
    page(
        filename="lesson-%d.html" % lesson["num"],
        title="Lesson %d: %s" % (lesson["num"], lesson["title"]),
        description="Lesson %d of the 8-lesson guided course: %s" % (lesson["num"], lesson["objective"]),
        active="course",
        hero_html=lesson_hero(lesson),
        body_html=body,
        extra_scripts='<script src="js/progress.js"></script>',
    )


# ---- COURSE INDEX ----
course_hero = hero_block(
    eyebrow="Guided course",
    h1="The 8-Lesson Course",
    lede="The same site, walked through in order &mdash; one objective and one worksheet per lesson. Built for classrooms, but just as good for exploring solo at your own pace.",
    ctas_html='<a href="lesson-1.html" class="btn btn-primary">Start Lesson 1 →</a>'
              '<a href="for-teachers.html" class="btn btn-ghost">For teachers</a>',
    media_html="", readout_cells=[
        {"label": "Lessons", "value": "8", "decimals": 0, "suffix": "", "tone": ""},
        {"label": "Total time, roughly", "value": "2", "decimals": 0, "suffix": " hrs", "tone": "cool"},
    ],
    narrow=True,
)

course_lesson_cards = "\n".join(
    '<a class="lesson-card reveal" href="lesson-%d.html" data-lesson="%d"><span class="ln">%d</span>'
    '<div><div class="lc-title">%s</div><div class="lc-obj">%s &middot; %d min</div></div>'
    '<span class="lesson-check">Start →</span></a>'
    % (l["num"], l["num"], l["num"], l["title"], l["objective"], l["minutes"])
    for l in LESSONS
)

course_body = """
<section class="section">
  <div class="wrap" style="max-width:820px;">
    <div class="course-progress-wrap reveal">
      <div class="course-progress-top">
        <span><span id="course-progress-count">0</span> of 8 lessons complete</span>
        <span style="display:flex;gap:8px;flex-wrap:wrap;">
          <a href="checkin.html" class="btn btn-amber btn-sm">Check in with teacher →</a>
          <a href="class-dashboard.html" class="btn btn-ghost btn-sm">View class dashboard →</a>
          <button class="btn btn-ghost btn-sm" id="reset-progress-btn" type="button">Reset progress</button>
        </span>
      </div>
      <div class="course-progress-track"><span id="course-progress-bar"></span></div>
    </div>
    <ol class="lesson-list reveal">
      %s
    </ol>
    <div class="callout callout--note reveal" style="margin-top:30px;">
      <span class="callout-label">How this differs from free exploration</span>
      <p>The <a href="what-is-global-warming.html">Learn</a> and <a href="action-hub.html">Take Action</a> pages are still there for browsing freely in any order. This course is the same material, just sequenced with objectives, worksheets and a finish line &mdash; useful for a classroom, a homeschool unit, or anyone who wants a clear start-to-end path.</p>
    </div>
  </div>
</section>
""" % course_lesson_cards

page(
    filename="course.html",
    title="The 8-Lesson Course",
    description="An 8-lesson guided course version of the Global Warming Explorer, with objectives, worksheets, and progress tracking.",
    active="course",
    hero_html=course_hero,
    body_html=course_body,
    extra_scripts='<script src="js/progress.js"></script>',
)

# ---- FOR TEACHERS ----
teachers_hero = hero_block(
    eyebrow="Guided course · For teachers",
    h1="For Teachers",
    lede="A ready-to-use lesson plan for running this as a classroom unit &mdash; eight sessions, each with an objective, a discussion question, and a printable worksheet already built in.",
    ctas_html='<a href="course.html" class="btn btn-primary">View the course →</a>'
              '<a href="certificate.html" class="btn btn-ghost">Certificate template →</a>',
    media_html="", readout_cells=[
        {"label": "Suggested pacing", "value": "1", "decimals": 0, "suffix": " lesson/week", "tone": ""},
    ],
    narrow=True,
)

teacher_rows = "\n".join(
    '<tr><td><strong>%d. %s</strong><br><span class="muted" style="font-size:.82rem;">%d min</span></td>'
    '<td>%s</td><td><a href="lesson-%d.html">Open lesson →</a></td></tr>'
    % (l["num"], l["title"], l["minutes"], l["objective"], l["num"])
    for l in LESSONS
)

teachers_body = """
<section class="section">
  <div class="wrap">
    <div class="prose reveal">
      <h2>Suggested pacing</h2>
      <p>Built for roughly one lesson per week over an 8-week unit, but every lesson also stands alone &mdash; compress it into a single intensive day, or stretch it across a full term. Each lesson runs 15&ndash;20 minutes of core content plus its worksheet; budget extra time for discussion and the hands-on activities in Lessons 1, 5 and 8.</p>
    </div>
    <table class="teacher-table reveal">
      <tr><th>Lesson &amp; time</th><th>Objective</th><th>Link</th></tr>
      %s
    </table>
    <div class="grid grid-2 reveal">
      <div class="card">
        <div class="ico">🖨️</div><h3>Worksheets</h3>
        <p>Every lesson page has a built-in printable worksheet with a print button &mdash; no separate handouts to manage.</p>
      </div>
      <div class="card">
        <div class="ico">✅</div><h3>Assessment idea</h3>
        <p>Use the site-wide <a href="quiz.html">10-question Quiz</a> as a light end-of-unit check, and the <a href="certificate.html">Certificate of Completion</a> as a nice close-out for each student.</p>
      </div>
      <div class="card">
        <div class="ico">💬</div><h3>Discussion starters</h3>
        <p>Lessons 3, 4 and 8 work especially well as small-group discussions rather than solo worksheet time &mdash; they're opinion- and reflection-heavy by design.</p>
      </div>
      <div class="card">
        <div class="ico">🔁</div><h3>Progress, honestly</h3>
        <p>"Mark complete" buttons save to each device's browser, not a shared gradebook &mdash; great for self-paced learning, but for a class roster you'll still want the check-in below.</p>
      </div>
    </div>

    <div class="prose reveal" style="margin-top:40px;">
      <h2>Setting up class check-ins (free, no card, GitHub-only)</h2>
      <p>Students can send their progress to you via the <a href="checkin.html">Check In</a> page &mdash; it opens a pre-filled GitHub Issue in your repo with their name and completed lessons. They click "Submit new issue" themselves; nothing is collected on the site, and you need no backend or paid service at all.</p>
      <ol>
        <li>Check-ins land in your repo's <strong>Issues</strong> tab, and automatically flow into the <a href="class-dashboard.html">Class Dashboard</a> &mdash; a free GitHub Action rebuilds it whenever an Issue changes (and every 6 hours as a fallback). Nothing to configure beyond the repo itself.</li>
        <li>Decide public vs. private for the repo. If your students are minors, either keep the repo private, or ask them to check in with a first name + initial instead of a full name &mdash; the check-in page already nudges them toward that.</li>
        <li>If the dashboard ever looks stuck, open the repo's <strong>Actions</strong> tab and check the "Update Class Dashboard" workflow run, or trigger it manually from there.</li>
      </ol>
    </div>
  </div>
</section>
""" % teacher_rows

page(
    filename="for-teachers.html",
    title="For Teachers",
    description="A classroom lesson plan and pacing guide for running the Global Warming Explorer as an 8-lesson unit.",
    active="course",
    hero_html=teachers_hero,
    body_html=teachers_body,
)

# ---- CERTIFICATE ----
cert_hero = hero_block(
    eyebrow="Guided course · Finish line",
    h1="Certificate of Completion",
    lede="Finished all 8 lessons? Type a name below and download a certificate &mdash; a small, real way to mark finishing the course.",
    ctas_html='<a href="course.html" class="btn btn-ghost">← Back to course</a>',
    media_html="", readout_cells=[
        {"label": "Lessons required", "value": "8", "decimals": 0, "suffix": " of 8", "tone": "cool"},
        {"label": "Format", "value": "PNG", "decimals": 0, "suffix": "", "tone": ""},
    ],
    narrow=True,
)

cert_body = """
<section class="section">
  <div class="wrap cert-panel" style="max-width:820px;">
    <div class="cert-form reveal">
      <div class="field">
        <label for="cert-name" style="display:block;">Name to print on the certificate</label>
        <input type="text" id="cert-name" placeholder="e.g. Ada Okafor" style="margin-top:8px;">
      </div>
    </div>
    <div class="cert-canvas-wrap reveal">
      <canvas id="cert-canvas"></canvas>
    </div>
    <button class="btn btn-amber" id="cert-download" style="margin-top:24px;">⬇️ Download as PNG</button>
    <p class="muted" style="font-size:.85rem;margin-top:16px;">Drawn right here in your browser &mdash; nothing is uploaded or saved anywhere.</p>
  </div>
</section>
"""

page(
    filename="certificate.html",
    title="Certificate of Completion",
    description="Generate and download a Certificate of Completion for the Global Warming Explorer 8-lesson course.",
    active="course",
    hero_html=cert_hero,
    body_html=cert_body,
    extra_scripts='<script src="js/certificate.js"></script>',
)

print("COURSE MODULE BUILT")

# =========================================================
# CHECK-IN (free, GitHub-native classroom check-in via prefilled Issue)
# =========================================================
checkin_hero = hero_block(
    eyebrow="Guided course · Check in",
    h1="Check in with your teacher",
    lede="This sends your name and lesson progress to your teacher as a GitHub Issue &mdash; free, and nothing leaves this page until you choose to submit it on GitHub yourself.",
    ctas_html='<a href="course.html" class="btn btn-ghost">← Back to course</a>',
    media_html="", readout_cells=[
        {"label": "Cost", "value": "0", "decimals": 0, "prefix": "₦", "suffix": "", "tone": "cool"},
        {"label": "Where it goes", "value": "GitHub", "decimals": 0, "suffix": " Issues", "tone": ""},
    ],
    narrow=True,
)

checkin_body = """
<section class="section">
  <div class="wrap" style="max-width:640px;">
    <div class="callout callout--alert reveal" id="checkin-setup-warning">
      <span class="callout-label">Setup needed (for the site owner)</span>
      <p>This check-in form isn't connected to a repo yet. Open <code>js/checkin.js</code> and change <code>GITHUB_REPO</code> to your real <code>owner/repo-name</code>, then this message disappears automatically.</p>
    </div>

    <div class="callout callout--note reveal">
      <span class="callout-label">Before you start</span>
      <p>You'll need a free GitHub account to actually submit this (most students who code already have one). Consider using just your first name and last initial &mdash; e.g. "Ada O." &mdash; rather than your full name, since this can be visible publicly.</p>
    </div>

    <form id="checkin-form" class="tool-panel reveal">
      <div class="field">
        <label for="checkin-name">Your name (or first name + initial)</label>
        <input type="text" id="checkin-name" placeholder="e.g. Ada O." required>
      </div>

      <div class="checkin-progress-box">
        <strong style="font-size:.9rem;"><span id="checkin-progress-count">0</span> of 8 lessons complete on this device</strong>
        <ul id="checkin-progress-list"></ul>
      </div>

      <div class="field">
        <label for="checkin-note">Anything you want to tell your teacher? (optional)</label>
        <textarea id="checkin-note" placeholder="e.g. I found Lesson 3 really interesting!"></textarea>
      </div>

      <button type="submit" id="checkin-submit" class="btn btn-primary" style="width:100%;justify-content:center;">Open my check-in on GitHub →</button>
    </form>

    <p id="checkin-result" class="callout callout--try" style="margin-top:18px;"></p>
  </div>
</section>
"""

page(
    filename="checkin.html",
    title="Check In With Your Teacher",
    description="Send your lesson progress to your teacher via a free, pre-filled GitHub check-in — no account needed on this site, no data collected here.",
    active="course",
    hero_html=checkin_hero,
    body_html=checkin_body,
    extra_scripts='<script src="js/progress.js"></script>\n<script src="js/checkin.js"></script>',
)
print("CHECK-IN PAGE BUILT")

# =========================================================
# CLASS DASHBOARD (auto-updated by a free GitHub Action)
# =========================================================
dashboard_hero = hero_block(
    eyebrow="Guided course · Class dashboard",
    h1="Class Dashboard",
    lede="A live view of every student check-in &mdash; built automatically by a free GitHub Action that watches the repo's Issues, so you never have to read a raw Issues list by hand.",
    ctas_html='<a href="checkin.html" class="btn btn-ghost">Check In page →</a>'
              '<a href="for-teachers.html" class="btn btn-ghost">For teachers →</a>',
    media_html="", readout_cells=[
        {"label": "Updates", "value": "Auto", "decimals": 0, "suffix": "", "tone": "cool"},
        {"label": "Cost", "value": "0", "decimals": 0, "prefix": "₦", "suffix": "", "tone": ""},
    ],
    narrow=True,
)

dashboard_body = """
<section class="section">
  <div class="wrap">
    <div id="dashboard-mount" class="reveal"><div class="weather-loading">Loading dashboard&hellip;</div></div>
    <div class="callout callout--note reveal" style="margin-top:30px;">
      <span class="callout-label">How this stays up to date</span>
      <p>Every time a check-in Issue is opened (or every six hours as a fallback), a free GitHub Action reads the repo's Issues, rebuilds <code>roster-data.json</code>, and commits it back &mdash; no server, no database, no cost. See <code>.github/workflows/update-dashboard.yml</code> and <code>scripts/build_roster.py</code> in the repo.</p>
    </div>
  </div>
</section>
"""

page(
    filename="class-dashboard.html",
    title="Class Dashboard",
    description="An auto-updating class dashboard showing every student's lesson check-ins, built with a free GitHub Action — no backend required.",
    active="course",
    hero_html=dashboard_hero,
    body_html=dashboard_body,
    extra_scripts='<script src="js/dashboard.js"></script>',
)
print("DASHBOARD PAGE BUILT")
