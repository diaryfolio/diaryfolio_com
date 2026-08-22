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

## D-007 — Analytics requires explicit prior consent

**Status:** Accepted

**Decision:** Use basic consent mode for Google Analytics. When the Analytics build variable is configured, do not load Google code or send analytics data until the visitor accepts. Remember the choice for 180 days and provide permanent privacy and Cookie settings controls in the footer.

**Why:** Analytics cookies are optional, and DiaryFolio serves UK/EEA visitors. Basic mode provides a clear boundary: rejection sends no Analytics data, while acceptance remains reversible.

**Consequences:** Only `analytics_storage` is granted by the built-in panel. Advertising consent remains denied and AdSense must stay disabled until a separate Google-certified CMP flow is implemented.

**Details:** [GitHub Pages with Cloudflare DNS](github-pages-cloudflare.md)

## D-008 — Research provenance without a runtime dependency

**Status:** Accepted

**Decision:** Allow an optional `research_id` in article frontmatter, constrained to the `AR_1001`-style identifier format. Keep the research dossier in `df-blog-collect`; keep only final article content and real assets in this repository.

**Why:** A stable identifier makes the editorial evidence trail auditable without copying private workflow metadata into the public site or coupling the static build to another repository.

**Details:** [Website audit](website-audit.md)

## D-009 - Concise ASCII-first article style

**Status:** Accepted

**Decision:** New or materially edited articles follow the Blog etiquette in
`CLAUDE.md`: direct technical prose, minimal repetition, plain ASCII
punctuation wherever possible, evidence-aware claims, and no stock AI filler.
They use tables, lists, examples, or diagrams when those forms make the subject
clearer and easier to scan than long prose.

**Why:** The owner wants compact articles that read like deliberate technical
writing rather than verbose generated copy.

**Consequences:** Existing migrated archive content is not rewritten in bulk.
New articles and future material edits follow this convention. Non-ASCII text
remains acceptable when the subject, a proper name, quotation, or data value
requires it. Diagrams are used only when they simplify the subject.

## D-010 - Mermaid diagrams are rendered from local bundles

**Status:** Accepted

**Decision:** Support fenced `mermaid` blocks on article pages. Load the local
Mermaid bundle only when a diagram is present, render with strict security and
a fixed high-contrast theme, require `accTitle` and `accDescr`, and retain a
source-code fallback if rendering fails.

**Why:** Flow, architecture, dependency, and sequence explanations can be
clearer as diagrams than as long prose. A bundled renderer avoids a runtime
CDN dependency and keeps GitHub Pages deployment static.

**Consequences:** Mermaid becomes a direct dependency and creates a lazy
client-side bundle. Diagram pages execute that bundle; articles without a
diagram do not request it. Diagrams must be checked in the production preview
at desktop and mobile sizes.

## D-011 - Mermaid SVG animation is progressive and optional to the reader

**Status:** Accepted

**Decision:** Load Motion from the local bundle only after a Mermaid diagram
has rendered. Reveal each diagram once when it enters the viewport, drawing a
bounded set of visible unfilled strokes and fading in the complete SVG. Keep
the final diagram fully static, do not loop, and skip the animation when the
visitor requests reduced motion.

**Why:** A short progressive reveal can make flows, sequences, dependencies,
architectures, and timelines easier to follow without turning the technical
archive into a motion-heavy interface. Lazy loading keeps pages without
diagrams free of the animation dependency at runtime.

**Consequences:** Motion is a direct dependency and creates a second lazy
client-side bundle on diagram pages. Diagram animation must remain explanatory,
brief, and safe as progressive enhancement. Rendering and comprehension cannot
depend on motion, and any animation failure must leave the completed SVG
visible.

## D-012 - Purpose-built article SVGs share the progressive animation path

**Status:** Accepted

**Decision:** Allow accessible repository-authored inline SVG diagrams when a
specific visual is clearer than Mermaid. Use the reusable `article-svg-figure`
and `data-animate-svg` pattern, mark ordered content with `data-svg-step` and
connectors with `data-svg-link`, and animate each diagram once through the
existing local Motion dependency.

**Why:** Some editorial graphics need deliberate labels, emphasis, and layout
that are awkward to express in Mermaid. A shared enhancement pattern keeps the
SVG static by default while allowing a restrained reading-order reveal.

**Consequences:** Inline SVGs require an accessible title and description,
must remain complete without JavaScript, may not loop, and must be checked at
desktop and mobile widths. Reduced-motion visitors receive the finished static
graphic. A user may replay the finite sequence through the shared accessible
refresh control; the control is hidden when animation is unavailable or motion
is reduced. Articles without Mermaid do not load Mermaid merely to animate an
SVG.

## D-013 - Evaluate animated SVG first for justified article diagrams

**Status:** Accepted

**Decision:** When an article genuinely benefits from a diagram, first assess
whether a purpose-built animated inline SVG can explain the relationship in a
clear progressive sequence. If animation is not useful or practical, prefer a
static SVG. Use Mermaid when its supported syntax is clearer, more maintainable,
or less error-prone than custom SVG markup.

**Why:** The owner prefers compact, visual explanations and wants purposeful
SVG motion to be considered before a generic chart. A fallback order prevents
that preference from forcing decorative animation or brittle custom graphics.

**Consequences:** Writers document the visual purpose before choosing a format.
All formats require an accessible static state and responsive verification.
Reduced-motion, clarity, accuracy, maintainability, and page weight take
precedence over animation. A prose explanation or table remains better when no
diagram materially improves the article.
