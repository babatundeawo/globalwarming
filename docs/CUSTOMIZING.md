# Customizing the site

All changes are made on github.com by opening a file, selecting the pencil icon, and committing. The site rebuilds automatically (see [DEPLOYMENT.md](DEPLOYMENT.md)).

## Text

Page content lives in `build.py`. Each page is a block with a title, description and body. Use search to find the words you want to change. Lesson content is in the `LESSONS` list; the glossary is in `GLOSSARY_TERMS`.

## Colors

Open `css/styles.css` and change the values at the top (the `:root` block for light mode and `[data-theme="dark"]` for dark mode). The main colors are:

| Name | Used for |
| --- | --- |
| `--teal-700` | Primary buttons, links, headings accents |
| `--amber-500` / `--amber-600` | The "heat" accent |
| `--paper` | Page background |
| `--ink` | Body text |

Spacing, type sizes and motion timings are in `css/brand.css`. After changing the main color, also update `theme_color` in `manifest.json` and the two `theme-color` lines in `build.py`.

## Fonts

Fonts come from Google Fonts. To change them, edit the `FONTS` line in `build.py` and the `font-family` names in `css/styles.css`. Only choose fonts with licenses that allow free commercial use.

## Images

- Replace `images/profile/babatunde.jpg` with a new photo of the same name.
- Replace `images/og-image.png` (1200 x 630) to change the picture shown when the site is shared.
- App icons are in `images/icons/`. Keep the file names and sizes.
- Photos on the home and topic pages are linked from Wikimedia Commons inside `build.py`; their credits sit next to them. Keep the credit if you swap in another photo.

## Address and analytics

Near the top of `build.py`:

- `SITE_URL` is the public address of the site.
- `GOATCOUNTER_CODE` is empty, which keeps analytics off. To measure visits without cookies, create a free account at goatcounter.com and paste your site code between the quotes.
