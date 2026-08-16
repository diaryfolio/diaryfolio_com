# DiaryFolio repository guidance

Read this file before changing the site. DiaryFolio is a compact, static technical blog with a long-lived archive. The generated site is hosted on GitHub Pages at `https://diaryfolio.com`; Astro is a build-time tool only.

## Non-negotiable product decisions

- Keep the interface compact and technical. Do not introduce oversized editorial or magazine-style headings.
- Describe the archive as **Since 2008**. Never add a fixed ending year to evergreen site copy.
- Preserve the original `public/favicon.ico` unless the owner explicitly supplies a replacement.
- Keep canonical URLs on the apex domain: `https://diaryfolio.com`.
- Preserve existing `.html` article routes and migrated content URLs.
- Keep the default build free of analytics and advertising requests. Those integrations are enabled only through documented build variables.
- Keep production output static and compatible with GitHub Pages.

## Design documentation is part of the code

Any change that affects architecture, visual language, layout, typography, hosting, DNS, metadata, URL policy, content conventions, dependencies, analytics, or advertising must update the relevant file under `docs/design/` in the same change.

Use [docs/design/README.md](docs/design/README.md) to find the source-of-truth document. Add a concise entry to [docs/design/decisions.md](docs/design/decisions.md) when a decision is introduced, reversed, or materially refined. Do not add decision entries for routine bug fixes that leave the documented design unchanged.

Before finishing, verify that code, configuration, README instructions, and design documentation agree. A change is incomplete when the implementation and its design record disagree.

## Repository map

- `content/posts/`: article Markdown and frontmatter
- `src/layouts/`: document shell, metadata, navigation, analytics, and ad hooks
- `src/components/`: reusable presentation components
- `src/pages/`: static routes, feeds, sitemap, and search index
- `src/styles/site.css`: visual design system implementation
- `public/`: assets copied unchanged into the build, including the original favicon and custom-domain files
- `docs/design/`: current design, architecture, audit, and decision records
- `.github/workflows/deploy-pages.yml`: GitHub Pages deployment

## Required verification

Run these checks after relevant changes:

```bash
npm ci
npm run build
npm audit --omit=dev --audit-level=high
git diff --check
```

For interface changes, also inspect the local production preview at desktop and narrow widths. Check the homepage, search (including a real query), and at least one article with code or media. Confirm there is no horizontal overflow or browser-console error.

Do not push or deploy unless the owner explicitly asks. Leave a production preview available when the owner asks to test locally.
