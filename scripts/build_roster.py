"""
Reads every "Check-in: ..." Issue in this repo via the GitHub REST API and
writes roster-data.json — the file class-dashboard.html fetches and renders.

Runs inside GitHub Actions (see .github/workflows/update-dashboard.yml),
using the automatically-provided GITHUB_TOKEN — no secrets to set up, no
third-party service involved. Standard library only, no pip installs.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

REPO = os.environ.get("GITHUB_REPOSITORY", "")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "roster-data.json")

NAME_RE = re.compile(r"\*\*Name:\*\*\s*(.+)")
PROGRESS_RE = re.compile(r"\*\*Progress:\*\*\s*(\d+)\s*of\s*8")
LESSON_RE = re.compile(r"-\s*Lesson\s*(\d+):")


def api_get(path):
    url = "https://api.github.com" + path
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + TOKEN,
        "Accept": "application/vnd.github+json",
        "User-Agent": "global-warming-explorer-dashboard-bot",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_all_issues():
    issues = []
    page = 1
    while page <= 20:  # safety cap: 2000 issues max
        try:
            data = api_get("/repos/%s/issues?state=all&per_page=100&page=%d" % (REPO, page))
        except urllib.error.HTTPError as e:
            print("GitHub API error on page %d: %s" % (page, e), file=sys.stderr)
            break
        if not data:
            break
        issues.extend(data)
        if len(data) < 100:
            break
        page += 1
    return issues


def parse_checkin(issue):
    if issue.get("pull_request"):
        return None
    title = issue.get("title") or ""
    if not title.lower().startswith("check-in"):
        return None
    body = issue.get("body") or ""
    name_m = NAME_RE.search(body)
    if not name_m:
        return None
    progress_m = PROGRESS_RE.search(body)
    lessons = sorted(set(int(n) for n in LESSON_RE.findall(body)))
    return {
        "name": name_m.group(1).strip()[:80],
        "progress": int(progress_m.group(1)) if progress_m else len(lessons),
        "lessons": lessons,
        "issue_number": issue.get("number"),
        "issue_url": issue.get("html_url"),
        "created_at": issue.get("created_at"),
        "updated_at": issue.get("updated_at") or issue.get("created_at"),
        "state": issue.get("state"),
    }


def main():
    if not REPO:
        print("GITHUB_REPOSITORY not set — nothing to do.", file=sys.stderr)
        sys.exit(0)

    issues = fetch_all_issues()
    checkins = []
    for issue in issues:
        parsed = parse_checkin(issue)
        if parsed:
            checkins.append(parsed)

    checkins.sort(key=lambda c: c["created_at"] or "", reverse=True)

    # de-duplicate into a "current standing" per student name, keeping their
    # best (highest-progress) check-in
    students = {}
    for c in checkins:
        key = c["name"].strip().lower()
        if key not in students or c["progress"] > students[key]["progress"]:
            students[key] = c
    student_list = sorted(students.values(), key=lambda c: (-c["progress"], c["name"].lower()))

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repo": REPO,
        "total_checkins": len(checkins),
        "total_students": len(student_list),
        "students": student_list,
        "checkins": checkins[:300],
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("Wrote %s — %d students, %d check-ins" % (OUT_PATH, len(student_list), len(checkins)))


if __name__ == "__main__":
    main()
