# GitHub Pages with Cloudflare DNS

## Architecture

```text
Visitor → diaryfolio.com → Cloudflare authoritative DNS → GitHub Pages CDN → Astro static files
```

Cloudflare remains the registrar/DNS and security control plane. GitHub Pages becomes the static origin. This is a custom-domain mapping, not a browser redirect to a visible `github.io` URL.

## Deployment

1. Push or merge the tested site to `main`.
2. GitHub Actions uses Node.js 24, installs the locked dependencies with `npm ci`, and runs `npm run build`.
3. The workflow uploads `dist/` as the Pages artifact.
4. GitHub deploys the artifact to the `github-pages` environment.
5. `public/CNAME` is copied into the artifact as a record of the intended domain; the `diaryfolio.com` value configured in **Settings → Pages** is authoritative.

`node_modules/` and `dist/` are build artifacts and are ignored by `.gitignore`; they are never versioned. The locked `npm ci` plus `npm run build` steps in the workflow are the only producer of `dist/`, so every deployment reflects an installed, reproducible build.

## Repository settings

In **Settings → Pages**:

1. Choose **GitHub Actions** as the publishing source.
2. Set custom domain to `diaryfolio.com`.
3. Wait for the DNS check and certificate provisioning.
4. Enable **Enforce HTTPS**.

GitHub recommends verifying the domain through the account or organisation Pages settings before publishing to reduce takeover risk.

## Cloudflare DNS cutover

Before the cutover, remove the Worker custom domain for `diaryfolio.com`; it currently owns the apex DNS record. Add the four GitHub Pages apex A records shown in the repository README and point the `www` CNAME directly to the owning organisation's default Pages domain, `diaryfolio.github.io`. Do not include the repository name in the CNAME target, and do not leave the old Google/Blogger A records or the Worker record alongside the GitHub records.

Use **DNS only** during GitHub's domain and certificate checks. GitHub Pages already uses a CDN, so enabling the Cloudflare proxy is optional rather than required. If the proxy is enabled later, retest HTTPS, redirects, caching, and the GitHub Pages domain check.

## Google Analytics and AdSense

GitHub Pages serves normal static HTML and JavaScript, so Google Analytics works normally. The Astro layout adds the Google tag only when `PUBLIC_GA_MEASUREMENT_ID` is present at build time.

AdSense code also works technically, but approval is domain- and policy-based. Submit `diaryfolio.com` to AdSense; do not rely on the project URL under `github.io` for approval. After approval:

1. Add the publisher and slot IDs as GitHub Actions repository variables.
2. Set `PUBLIC_ADS_ENABLED=true`.
3. Publish an `ads.txt` file using the exact line supplied by AdSense.
4. Implement the required privacy notice and consent flow for the intended audience and jurisdictions.

The current site deliberately emits no analytics or ad requests when those variables are absent.

## Rollback

GitHub Pages deployments are immutable workflow artifacts. To roll back, redeploy a known-good commit from Actions or revert the problematic commit on `main`. DNS does not need to change for an application rollback.
