# Deployment guide (for the site owner)

You never type a command. You use github.com, GitHub Desktop and Windows File Explorer. A robot called **GitHub Actions** builds the site and publishes it to **GitHub Pages**.

## How it works

1. You change files on your PC and push them with GitHub Desktop.
2. GitHub Actions runs `build.py`, which writes all 27 pages, then downloads the fonts and Chart.js, checks the result, takes screenshots for the install prompt and publishes.
3. A run usually finishes in three to five minutes. It also runs by itself when a student checks in, and once a day.

## Update the site with a pull request (safest)

1. In GitHub Desktop choose **Current Branch > New Branch**, name it `update-site`, then **Create Branch**.
2. Change your files, or extract the ZIP over the repository folder (choose **Replace the files in the destination** when Windows asks).
3. In GitHub Desktop, write a summary in the box bottom left, then select **Commit to update-site**.
4. Select **Publish branch**, then **Create Pull Request**. GitHub opens in your browser.
5. On the page, wait for the **Build and check** line to show a green tick. Open that run and download the **built-site** file under Artifacts if you want to look at it first.
6. Select **Merge pull request**, then **Confirm merge**. The live site updates in a few minutes.

GitHub Pages has no built-in preview of a pull request. The downloadable built-site file is the closest option.

## Update the site directly (small text changes)

1. In GitHub Desktop make sure **Current Branch** says `main`, edit the file, commit, then select **Push origin**.
2. Open the repository on github.com, then the **Actions** tab, and wait for a green tick.

## First-time setup

1. github.com > **Settings > Pages > Build and deployment > Source** > choose **GitHub Actions**.
2. **Settings > Code security**: switch on **Dependabot alerts**, **Dependabot security updates**, **Secret scanning** and **Push protection**.
3. Open the **Actions** tab, select **Build and deploy**, then **Run workflow**.

The repository must be **Public** for Pages on the free GitHub plan.

## Check a deployment

Open the **Actions** tab. A green tick means live, a yellow circle means running, a red cross means it failed and the live site is unchanged. Select the run, then the red step, and read the line that starts with `Error`. Yellow warnings do not stop publishing.

## Roll back

1. On github.com open **Pull requests > Closed** and select the pull request you merged.
2. Select **Revert**, then **Create pull request**, then **Merge pull request**.
3. If you published straight to `main`, open **Code > Commits**, select the commit, then **...** > **Revert**.

## Hidden folders on Windows

The `.github` folder starts with a dot, so Windows may hide it. In File Explorer select **View > Show > Hidden items**. If `.github` is missing after extracting, extract again and make sure the ZIP was opened with **Extract All**, not dragged out in pieces.

## Class check-ins and the dashboard

Check-ins are GitHub Issues whose titles begin with `Check-in:`. Each deployment reads them. They are public, so ask students to use a first name or initials.

## Teacher's packet

After changing lesson content open **Actions > Rebuild teacher packet (manual) > Run workflow**. It regenerates the PDF.

## Custom domain (optional)

1. Buy a domain. In **Settings > Pages > Custom domain** type it and select **Save**.
2. At your registrar add the DNS records GitHub shows (four `A` records and a `CNAME` for `www`).
3. Tick **Enforce HTTPS** when it appears. No code change is needed: the build reads the address from GitHub.
4. Add the new address to `Allowed domains` only if you later add Firebase sign-in.

## What GitHub Pages cannot do

It cannot send HTTP security headers, so the Content Security Policy and referrer policy are set in each page's `<meta>` tags. Some headers (for example `X-Frame-Options` and HSTS preload settings) are not available on this host, so a header-scanner score will not be perfect.
