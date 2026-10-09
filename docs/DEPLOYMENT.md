# Deployment guide

This guide is for the site owner. You never need a terminal: everything is done in your web browser on github.com.

## How it works

The site's pages are written in one file, `build.py`. Every time you save a change on GitHub, a robot called **GitHub Actions** reads that file, builds all the pages, checks them, and publishes them. It also runs by itself when a student checks in and every six hours, so the class dashboard stays current. A change usually goes live within two to three minutes.

## One-time setup for the new repository

1. Sign in to github.com, select **+** (top right) > **New repository**.
2. Name it exactly `globalwarming`, set it to **Public**, and select **Create repository**.
3. On the empty repository page, select **uploading an existing file**. Drag in **everything** from the unzipped project folder, including the `.github` folder.
   - If you cannot see `.github`: on Windows open File Explorer > View > Show > Hidden items; on a Mac press `Cmd + Shift + .` in Finder.
   - If the upload still skips it, create each file by hand: **Add file > Create new file**, type the full path (for example `.github/workflows/deploy.yml`) as the file name, paste the contents, and commit.
4. Select **Commit changes**.
5. Open **Settings > Pages**. Under **Build and deployment > Source**, choose **GitHub Actions**.
6. Open the **Actions** tab. Select **Build and deploy** and, if it has not started, **Run workflow**. Wait for a green tick.
7. Visit `https://babatundeawo.github.io/globalwarming/`. You should see the new home page.

**Replacing the old repository:** the new repository can only take the name `globalwarming` after the old one is renamed or deleted. In the old repository, open **Settings > General**. Either change the repository name (for example to `globalwarming-old`) or scroll to **Danger Zone > Delete this repository**. Renaming keeps a backup, so it is the safer choice. Do this before step 1 above.

## Turn on the free security protections

1. Open **Settings > Code security** in the repository.
2. Switch on **Dependabot alerts** and **Dependabot security updates**.
3. Switch on **Secret scanning** and **Push protection**. This blocks you from accidentally publishing a password or key.
4. CodeQL (automatic code scanning) is already set up by the files in `.github/workflows`. Results appear under **Security > Code scanning**.

## Update the content

1. Open `build.py` in your repository and select the pencil icon.
2. Use your browser's search (`Ctrl/Cmd + F`) to find the sentence you want to change, edit it, and select **Commit changes**.
3. Open the **Actions** tab and watch the run. A green tick means the change is live.

Page text sits between quote marks inside `build.py`. Change only the words, not the quote marks or the symbols around them.

## Check whether a deployment worked

Open the **Actions** tab. The newest run is at the top.

- Green tick: live.
- Yellow circle: still running.
- Red cross: the build failed and the live site is unchanged. Select the run, then the red step, and read the line starting with `Error`. A message like `broken internal reference -> lesson-9.html` means a link points to a page that does not exist.

Warnings (shown with a yellow triangle) do not stop the site from publishing.

## Go back to an earlier version

1. Open **Code** and select the clock icon labelled **Commits**.
2. Find the change you want to undo and select it.
3. Select the **...** menu (top right of the change) > **Revert**, then **Create pull request**, then **Merge pull request**.
4. The site rebuilds without that change.

## Class check-ins and the dashboard

Student check-ins are GitHub issues whose titles begin with `Check-in:`. Each deployment reads them and builds the class dashboard. Check-ins are public, so ask students to use a first name or initials.

## Update the teacher's packet

After changing lesson content, open **Actions > Rebuild teacher packet (manual) > Run workflow**. It regenerates the PDF in about two minutes.

## Connect a custom domain (optional)

1. Buy a domain from a registrar.
2. In **Settings > Pages > Custom domain**, enter it and select **Save**.
3. At your registrar, add the DNS records GitHub lists on that page (four `A` records and one `CNAME` for `www`).
4. Tick **Enforce HTTPS** when it becomes available.
5. In `build.py`, change the `SITE_URL` line near the top to your new address and commit.
