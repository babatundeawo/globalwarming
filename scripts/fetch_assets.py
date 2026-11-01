# -*- coding: utf-8 -*-
"""
Downloads the site's fonts and Chart.js once, during the GitHub Actions build,
so visitors never contact Google or a CDN. Files land in css/fonts/ and
js/vendor/ and are served from the site itself (and cached for offline use).

Soft-fails: if a download fails, build.py detects the missing file and falls
back to system fonts / the pinned CDN copy, so the site is never broken.
Standard library only.
"""
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, "css", "fonts")
VENDOR_DIR = os.path.join(ROOT, "js", "vendor")
UA = "GlobalWarmingExplorer/2.0 (build script)"

# Fontsource serves the open-licence (SIL OFL) Google fonts as WOFF2, latin subset.
FONTSOURCE = "https://cdn.jsdelivr.net/fontsource/fonts/%s@latest/latin-%s-normal.woff2"
FONTS = [
    ("fraunces", "600"), ("fraunces", "700"),
    ("inter", "400"), ("inter", "500"), ("inter", "600"), ("inter", "700"),
    ("jetbrains-mono", "500"), ("jetbrains-mono", "600"),
]
CHARTJS = ("https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js", "chart.umd.min.js")


def fetch(url, dest, magic=None, min_bytes=1000):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
            if len(data) < min_bytes:
                raise ValueError("response too small (%d bytes)" % len(data))
            if magic and not data.startswith(magic):
                raise ValueError("unexpected file type")
            with open(dest, "wb") as f:
                f.write(data)
            return True
        except Exception as exc:  # noqa: BLE001 - any failure means "use the fallback"
            print("  attempt %d failed: %s" % (attempt + 1, exc))
            time.sleep(2)
    return False


def main():
    os.makedirs(FONT_DIR, exist_ok=True)
    os.makedirs(VENDOR_DIR, exist_ok=True)
    got = 0
    for family, weight in FONTS:
        name = "%s-%s.woff2" % (family, weight)
        dest = os.path.join(FONT_DIR, name)
        if os.path.exists(dest):
            got += 1
            continue
        print("font", name)
        if fetch(FONTSOURCE % (family, weight), dest, magic=b"wOF2"):
            got += 1
    url, name = CHARTJS
    dest = os.path.join(VENDOR_DIR, name)
    if not os.path.exists(dest):
        print("chart.js")
        fetch(url, dest, min_bytes=50000)
    print("fonts ready: %d of %d" % (got, len(FONTS)))
    # Never fail the build: pages fall back gracefully when a file is missing.
    sys.exit(0)


if __name__ == "__main__":
    main()
