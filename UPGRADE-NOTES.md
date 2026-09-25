# Premium design upgrade — what changed

A senior-polish pass over the whole site (all 25 content pages + 404). The
diff is small and additive on purpose — nothing about the site's structure,
copy, data, or existing behaviour was touched. Two new files, one shared
stylesheet addition, one shared script include on every page, and a few
small, targeted hooks.

## New files
- **`css/styles.css`** — appended a `PREMIUM UPGRADE LAYER` section (doesn't
  touch a single existing rule; new rules with matching selectors simply
  layer on top, so it's easy to trim or tweak later). Adds: richer glow
  shadows, a gradient mesh + floating orbs behind every hero, gradient-fill
  numerals on stats/readouts, a magnetic-tilt + edge-glow treatment for
  cards, a button sheen sweep + ripple, a cursor-following glow on desktop,
  a livelier scroll-reveal with stagger, quiz correct/wrong micro-animations,
  a premium scrollbar, and a softer focus ring.
- **`js/premium.js`** — new, loaded right after `js/main.js` on every page.
  Auto-detects existing markup (no HTML edits needed elsewhere) and adds:
  scroll reveal for cards/facts/callouts/lists, magnetic tilt on pointer
  devices, button ripple, the cursor glow, and a reusable
  `window.GWConfetti()` burst.
- **`404.html`** — the site didn't have one; GitHub Pages was serving its
  generic default. Now on-brand, matches the design system.

## Small targeted edits
- **`js/quiz.js`** — a quick confetti burst on a correct answer, and a
  bigger one on a strong final score (70%+).
- **`js/certificate.js`** — the certificate itself got a visual upgrade
  (gradient border, soft glow, gold seal medallion), plus a confetti burst
  on download.
- **`js/calculator.js`** — the footprint result now pops in instead of
  just appearing.
- **`sw.js`** — bumped the cache version and added `js/premium.js` to the
  app-shell precache list, so installed/offline visitors actually get the
  update and premium.js works offline too.
- Every page (except `offline.html`, kept minimal on purpose) — one new
  `<script src="js/premium.js" defer></script>` line after the existing
  `main.js` include.

## Notes / things worth knowing
- Everything respects `prefers-reduced-motion` and disables on coarse
  (touch) pointers automatically — tilt and cursor-glow are desktop-only,
  intentionally, motion stays subtle on phones.
- Visual richness was prioritized per your steer, so a few effects (mesh
  gradients, glow shadows, cursor glow) do add a little paint/GPU cost.
  Nothing here adds new network requests or blocking assets — no new
  images, fonts, or libraries — so page-weight and load time are basically
  unchanged even though the feel is richer.
- Nothing in `.git` was touched; this zip is just the working tree so you
  can drop it over your existing clone and diff/commit as usual.
