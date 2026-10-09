# Contributing

Thank you for helping improve Global Warming Explorer.

## Report a problem or suggest an idea

Use the [issue form](https://github.com/babatundeawo/globalwarming/issues/new/choose). Include the page name and, for display problems, your device and browser.

## Propose a change

1. Open the file you want to change on GitHub and select the pencil icon. Page text lives in `build.py`; styles are in `css/`.
2. Choose **Commit changes** and select **Create a new branch and start a pull request**.
3. The pull request builds the site and runs the checks automatically. A green tick means the site still builds.

## Developing locally (optional)

Local setup is only for contributors who prefer it. You need Python 3.12 and no other dependencies:

```bash
python3 build.py              # generate the pages
python3 scripts/check_site.py # check links and metadata
python3 -m http.server        # preview at http://localhost:8000
```

Generated `.html` files are not committed; the deploy workflow builds them.
