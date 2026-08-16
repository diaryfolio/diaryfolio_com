# DiaryFolio

DiaryFolio is a static Astro technical blog migrated from a Google Takeout Blogger export. It preserves the original `.html` article URLs and is designed to deploy to GitHub Pages at `https://diaryfolio.com`.

## Run locally

```bash
npm ci
npm run dev
```

Open the local URL printed by Astro, normally `http://localhost:4321`. To test the exact production output:

```bash
npm run build
npm run preview
```

## Content

- Article source: `content/posts/`
- Imported images: `public/assets/images/original/`
- Unmatched image report: `data/unmatched-images.csv`
- Legacy URL inventory: `redirects/legacy-urls.csv`

The historical Takeout import is complete. Edit the Markdown files directly for future revisions; do not rerun the importer over the migrated archive.

## GitHub Pages deployment

The workflow at `.github/workflows/deploy-pages.yml` builds and deploys `dist/` whenever `main` is updated. In the GitHub repository:

1. Open **Settings → Pages**.
2. Select **GitHub Actions** as the source.
3. Set the custom domain to `diaryfolio.com` and enable HTTPS after GitHub provisions the certificate.
4. Merge the tested changes into `main` or run the workflow manually.

`public/CNAME` records the intended custom domain in the deployed artifact, but the custom-domain value in **Settings → Pages** is authoritative for a GitHub Actions deployment. The `github.io` project URL becomes the hosting endpoint, while visitors and search engines use `diaryfolio.com`.

## Cloudflare DNS for GitHub Pages

Remove the existing Worker custom-domain record for the apex before changing DNS. Then create these records in Cloudflare:

| Type | Name | Value | Proxy while provisioning |
| --- | --- | --- | --- |
| A | `@` | `185.199.108.153` | DNS only |
| A | `@` | `185.199.109.153` | DNS only |
| A | `@` | `185.199.110.153` | DNS only |
| A | `@` | `185.199.111.153` | DNS only |
| CNAME | `www` | `diaryfolio.github.io` | DNS only |

Keep the records DNS-only until GitHub reports the custom domain and HTTPS certificate as healthy. GitHub will redirect `www.diaryfolio.com` to the configured apex domain.

## Analytics and advertising

The build supports Google Analytics and one restrained article-end AdSense placement. Add these as GitHub **Actions repository variables**:

```text
PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
PUBLIC_ADS_ENABLED=true
PUBLIC_ADSENSE_CLIENT=ca-pub-XXXXXXXXXXXXXXXX
PUBLIC_ADSENSE_ARTICLE_SLOT=1234567890
```

These values are intentionally public in the generated HTML. Leave them unset for a tracking-free local build. AdSense must approve `diaryfolio.com` before ads can appear, and privacy/consent requirements must be completed first. See `docs/advertising-and-analytics.md`.

## Design and migration notes

- [Design documentation index and update contract](docs/design/README.md)
- [Design decision log](docs/design/decisions.md)
- [Website audit](docs/design/website-audit.md)
- [Technical-blog design system](docs/design/design-system.md)
- [GitHub Pages and Cloudflare runbook](docs/design/github-pages-cloudflare.md)
- [Content migration](docs/content-migration.md)
- [Advertising and analytics](docs/advertising-and-analytics.md)
