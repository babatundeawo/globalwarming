# Customizing the site

All page text lives in `build.py`, between quote marks. Change only the words, not the quote marks.

| To change | Where |
| --- | --- |
| Colors, spacing, radius, type scale | `css/brand.css` (top of the file) and the `:root` block in `css/styles.css` |
| Text on a page | `build.py` (use Find, `Ctrl + F`, to locate the sentence) |
| Site address | Nothing to do on GitHub Pages: the build reads it. For testing only, set `SITE_URL` |
| Fonts | `scripts/fetch_assets.py` lists them; they are downloaded at build time (Fraunces, Inter, JetBrains Mono, all SIL OFL) |
| The colored ribbon on the home hero | `stripes_html()` in `build.py` and `.stripes` in `css/brand.css` |
| Favicon and app icons | `favicon.svg` and `images/icons/` (192, 512, maskable 512, apple-touch 180, favicon 32) |
| Social preview image | `images/og-image.png` (1200 x 630) |
| Photos | Credited beside each photo in `build.py`; use only images you own or that are freely licensed |
| App name and shortcuts | `write_manifest()` in `build.py` |

To replace the app icons, keep the same file names and sizes. The maskable icon needs its artwork inside the centre 80 percent.
