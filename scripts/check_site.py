# -*- coding: utf-8 -*-
"""
Quality gate for the built site (run by GitHub Actions after build.py).

Fails (exit 1) only for things that are really broken:
  - an internal link, script, stylesheet or image that points to a file that does not exist
Warns (exit 0) for softer issues:
  - missing/duplicate <title>, missing meta description, missing canonical,
    images without alt text, external links without rel="noopener"
Standard library only.
"""
import glob
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, warnings = [], []


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids = [], set()
        self.title = ""
        self._in_title = False
        self.has_desc = self.has_canonical = False
        self.warn = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "title":
            self._in_title = True
        if tag == "meta" and a.get("name") == "description" and a.get("content"):
            self.has_desc = True
        if tag == "link" and a.get("rel") == "canonical":
            self.has_canonical = True
        for key in ("href", "src"):
            if a.get(key):
                self.refs.append(a[key])
        if tag == "img" and "alt" not in a:
            self.warn.append("image without alt: %s" % a.get("src", "?"))
        if tag == "a" and (a.get("href", "").startswith("http")) and a.get("target") == "_blank":
            if "noopener" not in (a.get("rel") or ""):
                self.warn.append('external link missing rel="noopener": %s' % a["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "*.html")))
    titles = {}
    for path in files:
        name = os.path.basename(path)
        p = Page()
        p.feed(open(path, encoding="utf-8").read())
        if not p.title.strip():
            warnings.append("%s: missing <title>" % name)
        titles.setdefault(p.title.strip(), []).append(name)
        if name not in ("404.html", "offline.html"):
            if not p.has_desc:
                warnings.append("%s: missing meta description" % name)
            if not p.has_canonical:
                warnings.append("%s: missing canonical link" % name)
        warnings.extend("%s: %s" % (name, w) for w in p.warn)
        for ref in p.refs:
            if re.match(r"^(https?:|mailto:|tel:|data:|javascript:|//|#|\?)", ref) or not ref:
                continue
            target = ref.split("#")[0].split("?")[0]
            if not target:
                continue
            if not os.path.exists(os.path.join(ROOT, target)):
                errors.append("%s: broken internal reference -> %s" % (name, ref))
    for t, names in titles.items():
        if t and len(names) > 1:
            warnings.append("duplicate title %r on: %s" % (t, ", ".join(names)))
    print("Checked %d pages." % len(files))
    for w in warnings:
        print("::warning::" + w)
    for e in errors:
        print("::error::" + e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
