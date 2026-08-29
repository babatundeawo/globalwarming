# -*- coding: utf-8 -*-
"""
Generates downloads/teacher-packet.pdf: a single printable PDF covering the
full 8-lesson course (objectives, summaries and worksheets) plus the pacing
guide from for-teachers.html.

Pulls its content straight from LESSONS in build.py, so it never drifts out
of sync with the site, edit a lesson there and re-run this script to refresh
the PDF.

Requires: pip install playwright --break-system-packages && playwright install chromium
Run with: python3 scripts/build_teacher_packet.py
"""
import os
import re
import sys
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import build as site  # noqa: E402  (re-runs build.py's page-writing side effects; harmless/idempotent)

OUT_PATH = os.path.join(ROOT, "downloads", "teacher-packet.pdf")


def strip_tags_keep_breaks(html):
    """Turn a lesson's summary/worksheet HTML into clean print HTML: drop the
    inline SVG diagrams (decorative, not needed on paper) but keep the rest."""
    html = re.sub(r"<svg.*?</svg>", "", html, flags=re.S)
    return html


def build_pacing_table():
    rows = []
    for l in site.LESSONS:
        rows.append(
            "<tr><td class='num'>%d</td><td><strong>%s</strong><div class='muted'>%s</div></td>"
            "<td>%d min</td><td>%s</td></tr>"
            % (l["num"], l["title"], l["source_title"], l["minutes"], l["objective"])
        )
    return "\n".join(rows)


def build_lesson_sections():
    parts = []
    for l in site.LESSONS:
        summary = strip_tags_keep_breaks(l["summary"])
        worksheet = strip_tags_keep_breaks(l["worksheet"])
        parts.append(
            """
<section class="lesson">
  <h2>Lesson %d &middot; %s <span class="mins">%d min</span></h2>
  <p class="objective"><strong>Objective:</strong> %s</p>
  <h3>Summary</h3>
  %s
  <h3>Worksheet</h3>
  <div class="worksheet">%s</div>
  <div class="answer-space">
    <p class="muted">Space for written answers:</p>
    <div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>
  </div>
</section>"""
            % (l["num"], l["title"], l["minutes"], l["objective"], summary, worksheet)
        )
    return "\n".join(parts)


HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page { size: A4; margin: 22mm 18mm 20mm 18mm; }
  * { box-sizing: border-box; }
  body {
    font-family: Georgia, 'Times New Roman', serif;
    color: #16211d;
    font-size: 11.5pt;
    line-height: 1.55;
  }
  h1, h2, h3 { font-family: Arial, Helvetica, sans-serif; color: #0E5C56; }
  .cover {
    height: 240mm;
    display: flex; flex-direction: column; justify-content: center;
    page-break-after: always;
  }
  .cover .mark {
    width: 64px; height: 64px; border-radius: 16px;
    background: linear-gradient(135deg, #0E5C56, #EE8C3C);
    color: #fff; font-family: Arial, sans-serif; font-weight: 800; font-size: 22px;
    display: flex; align-items: center; justify-content: center; margin-bottom: 28px;
  }
  .cover h1 { font-size: 34pt; margin: 0 0 6px; line-height: 1.15; }
  .cover .sub { font-size: 14pt; color: #3c4a44; margin-bottom: 40px; }
  .cover .meta { font-size: 10.5pt; color: #5b6b64; border-top: 1px solid #cfd8d3; padding-top: 16px; }
  .toc { page-break-after: always; }
  .toc table { width: 100%; border-collapse: collapse; margin-top: 18px; }
  .toc td { padding: 9px 8px; border-bottom: 1px solid #e2e8e4; vertical-align: top; font-size: 10.5pt; }
  .toc td.num { width: 26px; font-weight: 800; color: #0E5C56; font-family: Arial, sans-serif; }
  .toc .muted { color: #6b7a73; font-size: 9.5pt; }
  .lesson { page-break-before: always; }
  .lesson h2 { font-size: 16pt; border-bottom: 2px solid #0E5C56; padding-bottom: 6px; margin-bottom: 10px; }
  .lesson .mins { float: right; font-size: 10pt; font-weight: 600; color: #EE8C3C; }
  .objective { background: #eef4f0; border-left: 3px solid #0E5C56; padding: 8px 12px; font-size: 10.5pt; }
  .lesson h3 { font-size: 12.5pt; margin-top: 20px; margin-bottom: 6px; }
  .lesson p { margin: 0 0 8px; }
  .worksheet .ws-q { margin-bottom: 12px; }
  .worksheet label { display: block; font-weight: 700; font-family: Arial, sans-serif; font-size: 10pt; color: #0E5C56; margin-bottom: 3px; }
  .worksheet .ws-blank { display: inline-block; min-width: 90px; border-bottom: 1px solid #16211d; }
  .worksheet .ws-line { display: block; border-bottom: 1px solid #cfd8d3; height: 20px; margin-top: 4px; }
  .answer-space { margin-top: 18px; }
  .wline { border-bottom: 1px solid #cfd8d3; height: 24px; margin-bottom: 2px; }
  .muted { color: #6b7a73; }
  footer.pfoot { position: fixed; bottom: -14mm; left: 0; right: 0; font-size: 8.5pt; color: #8b9994; text-align: center; }
</style>
</head>
<body>

<div class="cover">
  <div class="mark">GW</div>
  <h1>Global Warming Explorer</h1>
  <div class="sub">Teacher's Packet &mdash; 8-Lesson Climate Course</div>
  <p style="max-width: 420px; font-size: 11pt; color: #3c4a44;">
    A ready-to-teach unit: one objective, one summary and one printable worksheet
    per lesson, built for roughly one lesson a week over eight weeks (or compress
    it into fewer, longer sessions).
  </p>
  <div class="meta">
    by Babatunde Ayoola Awoyemi &middot; Techbase Consultant Services<br>
    globalwarmingexplorer &middot; babatundeawo.github.io/globalwarming<br>
    Generated __GEN_DATE__
  </div>
</div>

<div class="toc">
  <h2>Pacing Guide</h2>
  <p class="muted">The same table as on the site's <em>For Teachers</em> page, one row per lesson.</p>
  <table>
    __PACING_TABLE__
  </table>
</div>

__LESSON_SECTIONS__

</body>
</html>"""

HTML = (
    HTML.replace("__GEN_DATE__", datetime.date.today().strftime("%B %Y"))
    .replace("__PACING_TABLE__", build_pacing_table())
    .replace("__LESSON_SECTIONS__", build_lesson_sections())
)


def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    html_path = os.path.join(ROOT, "_teacher_packet_tmp.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file://" + html_path)
        page.pdf(
            path=OUT_PATH,
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=(
                "<div style='font-size:8px;color:#999;width:100%;text-align:center;'>"
                "Global Warming Explorer &middot; Teacher's Packet &middot; "
                "<span class='pageNumber'></span> / <span class='totalPages'></span></div>"
            ),
            margin={"top": "22mm", "bottom": "16mm", "left": "18mm", "right": "18mm"},
        )
        browser.close()

    os.remove(html_path)
    size_kb = os.path.getsize(OUT_PATH) / 1024
    print("wrote %s (%.0f KB)" % (OUT_PATH, size_kb))


if __name__ == "__main__":
    main()
