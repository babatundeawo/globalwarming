# Global Warming Explorer

A from-scratch rebuild of your original classroom presentation site, now a
27-page, mobile-friendly, interactive learning site under your own name.
Built as a static HTML/CSS/JS project (no build tools, no framework, just
like your other GitHub Pages projects). Includes a free-roam site, an
8-lesson guided course with worksheets and a certificate, live weather, and
a free, GitHub-native classroom check-in system with an auto-updating
dashboard.

## Documentation pass fixes (this update)

Two real bugs were found and fixed while auditing this repo against its own
README:

- `js/checkin.js` had `GITHUB_REPO` hardcoded to `techbaseng/globalwarming`
  (a different org) instead of `babatundeawo/globalwarming`, so the
  "Submit Check-in" button was opening a new-issue link on the wrong repo.
  Fixed to point at the correct repo.
- `.github/workflows/update-dashboard.yml` — the GitHub Action this README
  documents throughout the "Classroom check-ins & the dashboard" section —
  was missing from the repo entirely, even though `scripts/build_roster.py`
  (the script it's supposed to run) was present. Re-added, matching exactly
  what `build_roster.py` and this README already expect: triggers on Issue
  `opened`/`edited`/`closed`/`reopened`, a 6-hour scheduled fallback, and
  manual `workflow_dispatch`, with `contents: write` permission to commit
  `roster-data.json` back to the repo.

## 2026 modernisation pass

This round of updates focused on making the site feel current on every
screen size, without touching the free, no-build-step architecture:

- **Dark mode** — a header toggle that respects system preference by
  default, persists across visits, and swaps instantly with no flash on
  load.
- **Command palette** — press `Ctrl/Cmd+K` (or tap the search icon on
  mobile) to fuzzy-search and jump straight to any of the 27 pages.
- **Scroll progress bar** and a **back-to-top button** on every page.
- Verified climate figures against NOAA, WMO and Berkeley Earth as of
  August 2026 (2025 as the third-warmest year on record, ~427 ppm CO2,
  +1.3°C vs. pre-industrial).
- Every em dash and en dash in the copy has been rewritten with clearer
  punctuation (colons, semicolons, or plain "to" for ranges).

## ✅ Already configured for this repo

`js/checkin.js` is pointed at:

```js
var GITHUB_REPO = "techbaseng/globalwarming";
```

Nothing to change, just make sure everything in this folder (including
the hidden `.github/` folder) actually gets uploaded to that repo. GitHub
hides dot-folders in some upload flows, so if you're drag-and-dropping
through the web UI rather than using `git push`, double-check
`.github/workflows/update-dashboard.yml` actually made it in, see
"Classroom check-ins & the dashboard" below for why that file matters.

## What's inside

```
index.html                     Home (free-roam entry point)
about.html                     About you + Techbase + your other projects
what-is-global-warming.html    Learn: the greenhouse effect
causes.html                    Learn: causes, ranked
effects.html                   Learn: global effects + Nigeria 2025 floods/heat
why-care.html                  Learn: why it matters, climate justice
carbon-footprint.html          Take Action: interactive footprint calculator
recycle.html                   Take Action: reduce/reuse/recycle
clean-energy.html              Take Action: solar, wind, Nigeria's opportunity
action-hub.html                Take Action: tickable checklist
data-explorer.html             Go further: live weather + CO2/warmest-years/renewables charts
quiz.html                      Go further: 10-question interactive quiz
glossary.html                  Go further: A to Z glossary + sources

course.html                    Guided course: syllabus + live progress bar
lesson-1.html … lesson-8.html  One page per lesson: objective + worksheet
for-teachers.html              Lesson plan, pacing guide, check-in setup
certificate.html               Certificate of Completion (drawn on canvas)
checkin.html                   Student → teacher progress check-in
class-dashboard.html           Auto-updating roster, built by a GitHub Action

css/styles.css                 Design system (one file, all pages)
js/main.js                     Shared nav/scroll/counter behaviour
js/calculator.js               Carbon footprint calculator logic
js/checklist.js                Action Hub checklist logic
js/quiz.js                     Quiz logic + questions
js/charts.js                   Data Explorer charts (uses Chart.js via CDN)
js/weather.js                  Live weather widget (Open-Meteo, no key)
js/progress.js                 Lesson-complete tracking (localStorage)
js/certificate.js              Certificate canvas drawing + PNG download
js/checkin.js                  Builds the pre-filled GitHub check-in link
js/dashboard.js                Renders roster-data.json on the dashboard

scripts/build_roster.py        Turns check-in Issues into roster-data.json
.github/workflows/update-dashboard.yml   The GitHub Action that runs it

images/profile/                Drop your photo here (see README.txt inside)
favicon.svg                    Browser-tab icon
build.py                       The generator script, edit this, not the .html files
```

## Adding your photo

Drop a photo at `images/profile/babatunde.jpg`, the About page will pick it
up automatically. Full details in `images/profile/README.txt`.

## How content gets edited

**Don't hand-edit the `.html` files directly**, they're all generated by
`build.py`. To change any text, find the relevant block inside `build.py`
(organised page-by-page, clearly commented), edit it there, then:

```
python3 build.py
```

This regenerates all 27 pages from the templates in one go, so nav, footer
and design stay consistent everywhere automatically. `roster-data.json` is
the one file `build.py` does *not* touch, that one's owned by the GitHub
Action.

## Deploying to GitHub Pages (free, no card required)

1. Upload everything in this folder, **including the hidden `.github/`
   folder**, to https://github.com/techbaseng/globalwarming, keeping the
   folder structure intact (`css/`, `js/`, `scripts/`, `.github/`,
   `images/`, all the `.html` files, `build.py`).
2. In the repo, go to **Settings → Pages**, set **Source** to your main
   branch (root folder), and save, if you haven't already.
3. In **Settings → Actions → General → Workflow permissions**, make sure
   "Read and write permissions" is selected, the dashboard Action needs
   this to commit `roster-data.json` back to the repo. (If this is greyed
   out or missing, it's already on by default for most personal repos.)
4. Your live site is at https://babatundeawo.github.io/globalwarming/.

## Classroom check-ins & the dashboard, how it actually works

`checkin.html` reads a student's local lesson progress (stored in their own
browser) and, on submit, opens a **pre-filled GitHub Issue** with their name
and completed lessons. They click "Submit new issue" themselves, nothing
is collected by the site, no backend, no secret keys anywhere.

From there, `.github/workflows/update-dashboard.yml` (a free GitHub Action)
watches the repo's Issues. Whenever one is opened, edited, closed or
reopened, or every 6 hours as a fallback, or on demand from the Actions
tab, it runs `scripts/build_roster.py`, which calls the GitHub API with the
automatically-provided `GITHUB_TOKEN`, parses every "Check-in: …" Issue, and
commits the result to `roster-data.json`. `class-dashboard.html` simply
fetches that file and renders it, no server, no database, nothing you
have to run yourself.

**Real constraints worth knowing:**
- Each student needs a free GitHub account to submit a check-in. There's no
  way around this without adding a backend.
- Issues on a public repo are visible to anyone, forever. The check-in page
  nudges students toward "first name + initial" rather than full names.
  If your students are minors and you want stronger privacy, switch the
  repo to private in Settings, everything above still works the same way.
- The dashboard updates within minutes of a check-in, or up to ~6 hours via
  the scheduled fallback. If it ever looks stuck, check the repo's
  **Actions** tab for the most recent "Update Class Dashboard" run.

## Live weather

The "Today's Weather" widget on `data-explorer.html` calls
[Open-Meteo](https://open-meteo.com/) directly from the visitor's browser, free, no API key, CORS-enabled, CC BY 4.0 licensed. It defaults to Ibadan,
but visitors can search any city or use their own location. It's
deliberately framed as *weather* (today, one place) next to the *climate*
charts (decades, the whole planet), the page explains the distinction
right there.

## Images used

All photos are real, freely-licensed images pulled from Wikimedia Commons
(NASA's public-domain Earth photo, and Wiki Loves Africa contest photos
from Nigeria), loaded directly from Commons, no copies needed, no
copyright concerns, full credit lines shown on each photo. Everything else
(the greenhouse-effect diagram, icons, charts, certificate) is built
directly in the site's own CSS/SVG/JS/Canvas.

## Notes on the data

Every statistic on the site (CO2 ppm, global temperature anomalies,
renewables share, Nigeria's 2025 flood and heat figures) is sourced from
NASA, NOAA, the IEA, and Nigerian agency reporting (NiMet/NEMA) as of mid-
2026. The Glossary & Sources page links to all of them. Worth a light
refresh once a year as new annual figures come out, search for "NOAA
global climate report [year]" and "IEA global energy review [year]" and
swap the numbers in `causes.html`, `effects.html`, `clean-energy.html`,
`data-explorer.html`, the relevant lesson summaries, and the readout strips
inside `build.py`.
