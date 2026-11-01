# -*- coding: utf-8 -*-
"""
Takes real screenshots of the built site (for the install prompt and README)
and adds them to the web app manifest. Runs in GitHub Actions after the site
folder is assembled. Soft-fails: without screenshots the install prompt is
simply the plain version.

Usage: python3 scripts/make_screenshots.py _site
"""
import functools
import http.server
import json
import os
import sys
import threading

SHOTS = [("wide.png", 1280, 720, "wide"), ("narrow.png", 390, 844, "narrow")]


def main():
    site = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "_site")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright is not installed; skipping screenshots")
        return
    out_dir = os.path.join(site, "images", "screenshots")
    os.makedirs(out_dir, exist_ok=True)

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=site)
    handler.log_message = lambda *a, **k: None
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:%d/" % server.server_address[1]

    made = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for name, w, h, form in SHOTS:
            ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=1, reduced_motion="reduce")
            pg = ctx.new_page()
            pg.goto(base + "index.html", wait_until="networkidle")
            pg.wait_for_timeout(800)
            pg.screenshot(path=os.path.join(out_dir, name))
            made.append((name, w, h, form))
            ctx.close()
        browser.close()
    server.shutdown()

    mpath = os.path.join(site, "manifest.json")
    manifest = json.load(open(mpath, encoding="utf-8"))
    manifest["screenshots"] = [
        {"src": "images/screenshots/" + n, "sizes": "%dx%d" % (w, h), "type": "image/png",
         "form_factor": f, "label": "Global Warming Explorer home page"}
        for n, w, h, f in made
    ]
    json.dump(manifest, open(mpath, "w", encoding="utf-8"), indent=2)
    print("screenshots added: %d" % len(made))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print("screenshots skipped: %s" % exc)
