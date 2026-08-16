# Design documentation

This directory is the source of truth for DiaryFolio's product and technical design. It must remain synchronized with the implementation.

## Documents

- [Website audit](website-audit.md): migration findings, resolutions, generator rationale, content debt, and acceptance criteria.
- [Design system](design-system.md): layout, typography, colour, cards, media, code, data, accessibility, and motion.
- [GitHub Pages with Cloudflare DNS](github-pages-cloudflare.md): hosting architecture, deployment, DNS cutover, analytics, advertising, and rollback.
- [Decision log](decisions.md): concise record of material decisions and their consequences.

## Update contract

| Change | Required documentation update |
| --- | --- |
| Layout, typography, colour, cards, code, images, responsive behaviour, accessibility | `design-system.md` |
| Generator, content model, routes, metadata, search, dependencies, migration quality | `website-audit.md` |
| GitHub Actions, GitHub Pages, custom domain, Cloudflare DNS, analytics, ads, rollback | `github-pages-cloudflare.md` |
| A material decision is introduced, reversed, or substantially refined | `decisions.md` plus the relevant document above |

Update the documentation in the same change as the code or configuration. Describe the current intended state, not a speculative future design. When a decision is superseded, retain its decision-log entry and point it to the replacement.
