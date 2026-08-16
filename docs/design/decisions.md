# Design decision log

This log records material decisions. The linked design documents describe the full current state.

## D-001 — Static GitHub Pages hosting

**Status:** Accepted

**Decision:** Publish Astro's static `dist/` artifact with GitHub Actions and GitHub Pages. Keep Cloudflare as authoritative DNS for `diaryfolio.com`.

**Why:** The site needs no server runtime, and this keeps hosting simple and inexpensive while preserving the custom domain.

**Details:** [GitHub Pages with Cloudflare DNS](github-pages-cloudflare.md)

## D-002 — Astro retained as a build-only generator

**Status:** Accepted

**Decision:** Keep Astro as the sole direct production dependency. Do not migrate to Zensical at this time.

**Why:** The current implementation already provides chronological blog collections, stable legacy routes, cards, RSS, sitemap, structured metadata, and custom search. The deployed artifact is plain static HTML/CSS/JavaScript. Zensical currently focuses on documentation, is alpha software, and lists native blogging on its roadmap, so migration would add risk without reducing the deployed footprint.

**Details:** [Website audit](website-audit.md)

## D-003 — Compact technical visual language

**Status:** Accepted

**Decision:** Use restrained system typography, two-column desktop cards, a narrow article measure, strong code presentation, and one-column mobile layouts.

**Why:** DiaryFolio is a technical reference archive rather than an editorial or lifestyle publication.

**Details:** [Design system](design-system.md)

## D-004 — Evergreen archive wording

**Status:** Accepted

**Decision:** Use “Since 2008” without a fixed ending year in evergreen interface copy.

**Why:** The archive continues to grow and must not become visibly stale.

## D-005 — Preserve identity and URL history

**Status:** Accepted

**Decision:** Keep the original `public/favicon.ico`, use the apex canonical domain, and preserve the migrated `.html` routes.

**Why:** These choices retain the site's identity, backlinks, bookmarks, and search history.

## D-006 — Build artifacts are not versioned

**Status:** Accepted

**Decision:** Keep `node_modules/` and `dist/` untracked, ignored by `.gitignore`. The GitHub Pages workflow is the only producer of `dist/`.

**Why:** Committed dependencies and build output inflate the repository history and increase the risk of accidentally committing a real credential; the locked `npm ci` workflow already provides a reproducible build.

**Details:** [GitHub Pages with Cloudflare DNS](github-pages-cloudflare.md)
