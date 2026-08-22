# DiaryFolio website audit

## Scope

The audit covers the Astro source, 113 migrated posts, generated production HTML, archive/search behaviour, responsive presentation, metadata, privacy controls, and static hosting. The baseline build completes successfully and generates 118 pages.

## Findings and resolutions

| Priority | Finding | Impact | Resolution |
| --- | --- | --- | --- |
| High | Article JSON-LD and enhancement scripts were emitted after `</html>`. | Invalid document structure and unreliable script execution. | Structured data now renders in `<head>` and article enhancement code remains inside the layout body. |
| High | Canonicals, RSS, sitemap, robots, and structured data used `www.diaryfolio.com`, while the active domain is the apex. | Split indexing signals and duplicate URLs. | All generated first-party URLs now use `https://diaryfolio.com`. |
| High | The homepage displayed `2008–2025`. | The ending year becomes stale and contradicted the evergreen positioning. | The site uses only “Since 2008” and “Technical notes since 2008”. |
| High | No reproducible deployment workflow existed for the chosen host. | Manual deployments could publish inconsistent output. | A locked `npm ci` GitHub Pages workflow deploys `dist/` from `main`. |
| Medium | Homepage/search headings scaled to 5–6rem and mobile headings to 4.2rem. | The site read like an editorial showcase rather than a technical reference. | Top-level headings now cap at 2.85rem on desktop and 2.2rem on mobile. |
| Medium | Duplicate mobile media queries overrode one another. | Fragile responsive behaviour. | Styles were consolidated into one deliberate mobile layout. |
| Medium | Search embedded roughly 384 KB of post data directly in the HTML. | Slower HTML parsing and no independent caching. | Search data moved to a cacheable generated `search-index.json`; the UI initially shows 24 recent results. |
| Medium | Cards could show every migrated label. | Dense, noisy cards with uneven heights. | Cards show three labels plus a compact remainder count; search results show four. |
| Medium | The topic selector exposed hundreds of one-off migrated labels. | The filter was difficult to scan and operate. | The selector shows the 30 most-used topics; all labels remain searchable as text. |
| Medium | Google-hosted display fonts were render-blocking. | Extra third-party request and an overly editorial visual tone. | The site now uses a fast system sans-serif and system monospace stack. |
| Medium | Keyboard focus and skip navigation were missing. | Keyboard navigation was harder to follow. | Added a skip link, visible focus states, and current-page navigation state. |
| Medium | Analytics loaded immediately whenever its build variable was present. | UK/EEA visitors had no prior choice and no persistent withdrawal control. | Analytics now uses a basic consent flow that blocks Google code until acceptance, remembers the choice for 180 days, and exposes Cookie settings in the footer. |
| Low | Four old posts contained HTTP iframe URLs. | Modern browsers could block the embeds as mixed content. | Upgraded the known embeds to HTTPS and added titles and lazy loading. |
| Low | The migrated Astro 5 dependency tree reported security advisories. | Build tooling should not retain known vulnerable packages even though the deployed output is static. | Upgraded to Astro 7.2.2 and compatible patched transitive packages; `npm audit` now reports zero vulnerabilities. |

## Generator decision

Astro remains a build-time dependency only: GitHub Pages serves the generated HTML, CSS, and JavaScript without an Astro server. It is retained because the existing implementation already provides the blog-specific features this archive needs: chronological collections, cards, RSS, sitemap, legacy routes, structured metadata, and a custom searchable index. Mermaid and Motion are the additional direct runtime dependencies. Both are bundled locally: Mermaid is loaded lazily only on article pages containing a Mermaid diagram, and Motion is loaded only after a Mermaid or purpose-built inline SVG diagram is ready and the visitor has not requested reduced motion.

Zensical was considered, but its current focus is technical documentation and its native blog functionality is still on its roadmap. Moving now would trade a completed static implementation for theme overrides and another content migration without reducing the deployed footprint.

## Content quality observations

- Several migrated posts have no description, so their cards contain only the title and metadata. New or high-traffic posts should receive concise frontmatter descriptions.
- New posts developed from the separate research workflow may include an optional `research_id` matching `AR_[0-9]{4,}`. This is frontmatter-only provenance: reader-facing source sections link directly to important external evidence and do not expose the internal dossier ID. The public build does not read or depend on the research repository.
- A subset of images remains hosted on `blogger.googleusercontent.com`; `data/unmatched-images.csv` is the migration backlog.
- Historic posts contain obsolete external links and embedded demos. Preserve the original text, but annotate or repair broken resources when a post is reviewed.
- The original `.html` routes are valuable backlinks and should remain stable.

## Acceptance criteria

- No site-level heading exceeds the compact type scale.
- Homepage and search cards work at desktop and mobile widths without horizontal overflow.
- Article images remain within the reading column and retain aspect ratio.
- Code blocks are readable, scrollable, copyable, and collapsible when long.
- Fenced Mermaid blocks render as accessible SVG without a CDN request, stay
  inside the reading column, and retain source-code fallback on render failure.
- Canonical, RSS, sitemap, robots, and structured data agree on the apex domain.
- The privacy page is included in the sitemap, and the footer exposes privacy and cookie controls.
- With Analytics configured, no Google Analytics script or request occurs before acceptance; rejection persists, and withdrawal prevents loading on the next page view.
- Production HTML contains no scripts after `</html>`.
- GitHub Pages publishes the exact Astro `dist/` artifact.
