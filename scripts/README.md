# scripts

Helpers used by the build.

- `build_roster.py` reads check-in issues and writes `roster-data.json` for the class dashboard. Runs automatically on deploy.
- `check_site.py` checks the generated pages for broken internal links and missing metadata. Runs automatically on deploy.
- `build_teacher_packet.py` generates `downloads/teacher-packet.pdf` from the lesson content. Run it from the **Rebuild teacher packet** workflow.
- `fetch_images.py` downloads the Wikimedia photos into `images/photos/` during deployment so pages serve them from the site itself. If a download fails, the page links to Wikimedia instead.
