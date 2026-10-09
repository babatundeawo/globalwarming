# -*- coding: utf-8 -*-
"""
Downloads the Wikimedia Commons photos used by the site into images/photos/ so
pages serve them from the site itself (faster, and not dependent on Wikimedia
being reachable for every visitor). Runs in GitHub Actions before build.py.

If a download fails, the page keeps using the original Wikimedia link, so this
step can never break the site. Standard library only.
"""
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = os.path.join(ROOT, "images", "photos")
UA = "GlobalWarmingExplorer/1.0 (https://github.com/babatundeawo/globalwarming; build script)"
PATTERN = re.compile(r"https://commons\.wikimedia\.org/wiki/Special:FilePath/([^\"'?\s]+)\?width=(\d+)")


def local_name(commons_name, width):
    """Must match local_photo_name() in build.py."""
    base = urllib.parse.unquote(commons_name)
    stem, ext = os.path.splitext(base)
    stem = re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_")
    return "%s-%s%s" % (stem, width, ext.lower() or ".jpg")


def download(url, dest):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
            if len(data) < 2000:
                raise ValueError("response too small")
            with open(dest, "wb") as f:
                f.write(data)
            return True
        except Exception as exc:  # noqa: BLE001
            print("  attempt %d failed: %s" % (attempt + 1, exc))
            time.sleep(3 * (attempt + 1))
    return False


def main():
    os.makedirs(PHOTOS, exist_ok=True)
    source = open(os.path.join(ROOT, "build.py"), encoding="utf-8").read()
    found = sorted(set(PATTERN.findall(source)))
    ok = 0
    for name, width in found:
        dest = os.path.join(PHOTOS, local_name(name, width))
        url = "https://commons.wikimedia.org/wiki/Special:FilePath/%s?width=%s" % (name, width)
        if os.path.exists(dest):
            ok += 1
            continue
        print("Downloading", urllib.parse.unquote(name))
        if download(url, dest):
            ok += 1
        else:
            print("::warning::Could not download %s; the page will link to Wikimedia instead." % name)
    print("%d of %d photos available locally." % (ok, len(found)))
    sys.exit(0)


if __name__ == "__main__":
    main()
