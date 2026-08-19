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

GitHub Pages serves normal static HTML and JavaScript, so Google Analytics works normally. The Astro build includes the analytics consent UI only when `PUBLIC_GA_MEASUREMENT_ID` is present at build time. It does not emit a Google script tag in the generated HTML.

DiaryFolio uses basic consent mode for Analytics:

1. A first visit displays an analytics-only consent panel.
2. Until the visitor accepts, no Google tag is loaded and no analytics request is sent.
3. Acceptance grants only `analytics_storage`; advertising storage, user data, and personalisation remain denied.
4. The choice is stored locally for 180 days.
5. The footer Cookie settings control lets the visitor change the choice. Withdrawal sends a denied update when possible, removes accessible `_ga` cookies, and reloads without Analytics.

The static privacy page at `/privacy.html` describes this behaviour and is included in the sitemap. If the build variable is absent, the site has no Analytics banner, Cookie settings button, Google code, or analytics requests; the privacy link remains available.

AdSense code also works technically, but approval is domain- and policy-based. Submit `diaryfolio.com` to AdSense; do not rely on the project URL under `github.io` for approval. After approval:

1. Add the publisher and slot IDs as GitHub Actions repository variables.
2. Set `PUBLIC_ADS_ENABLED=true`.
3. Publish an `ads.txt` file using the exact line supplied by AdSense.
4. Implement a separate Google-certified CMP flow for the intended audience and jurisdictions.

The built-in analytics consent panel does not grant or communicate advertising consent. Keep `PUBLIC_ADS_ENABLED` unset or false until the separate advertising consent flow is complete.

The current site deliberately emits no analytics or ad requests when those variables are absent. Adding or changing a repository variable requires a fresh GitHub Actions build because Astro resolves it at build time.

## Rollback

GitHub Pages deployments are immutable workflow artifacts. To roll back, redeploy a known-good commit from Actions or revert the problematic commit on `main`. DNS does not need to change for an application rollback.
