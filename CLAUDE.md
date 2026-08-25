# DiaryFolio repository guidance

Read this file before changing the site. DiaryFolio is a compact, static technical blog with a long-lived archive. The generated site is hosted on GitHub Pages at `https://diaryfolio.com`; Astro is a build-time tool only.

## Non-negotiable product decisions

- Keep the interface compact and technical. Do not introduce oversized editorial or magazine-style headings.
- Describe the archive as **Since 2008**. Never add a fixed ending year to evergreen site copy.
- Preserve the original `public/favicon.ico` unless the owner explicitly supplies a replacement.
- Keep canonical URLs on the apex domain: `https://diaryfolio.com`.
- Preserve existing `.html` article routes and migrated content URLs.
- Keep the default build free of analytics and advertising requests. Those integrations are enabled only through documented build variables.
- When Analytics is enabled, do not load Google code or send analytics data before the visitor has explicitly accepted optional analytics.
- Keep production output static and compatible with GitHub Pages.

## Blog etiquette

Apply these rules whenever creating or materially editing an article:

- Use concise, direct technical prose. Prefer short sentences and focused
  paragraphs. Remove repeated conclusions, throat-clearing, and filler.
- Use plain ASCII punctuation wherever possible. Do not use em dashes, en
  dashes, or smart quotes. Use full stops, commas, colons, semicolons,
  parentheses, or the ASCII hyphen instead. Use non-ASCII characters only
  when a proper name, quotation, data value, or technical subject requires it.
- Avoid stock AI language and inflated phrasing, including "delve",
  "ever-evolving landscape", "game-changer", "it is important to note",
  "in today's world", and generic "in conclusion" summaries.
- Do not narrate the writing process or mention AI, prompts, internal research
  dossiers, or `research_id` in the public article body. `research_id` belongs
  only in frontmatter.
- Lead with the useful answer. For researched articles, place a compact
  **Quick read** near the start with the main answer, key takeaways, and the
  most important caveat.
- Use descriptive headings. Avoid clickbait, rhetorical questions used as
  padding, and headings that merely repeat the title.
- Write for the end reader, not for the author or search engine. Explain the
  practical meaning first, define unavoidable jargon, and use a concrete
  example when it makes the idea easier to apply.
- Keep the page easy to scan. Break a long wall of text with meaningful
  headings, short lists, a comparison table, or a diagram only when that
  structure improves understanding.
- Prefer a table for exact comparisons or repeated fields. Prefer a flow
  diagram for sequences, dependencies, architecture, or several interacting
  parts. A visual must replace or simplify prose, not decorate it.
- When a diagram is justified, first consider a purpose-built animated inline
  SVG if a progressive reveal materially improves comprehension. If custom
  animation is not useful or practical, use a clear static SVG. Use Mermaid
  when its supported syntax expresses the idea more clearly or maintainably
  than a custom SVG. Every option must keep a complete accessible static state.
- Mermaid diagrams use a fenced `mermaid` code block. Include Mermaid
  `accTitle` and `accDescr`, keep labels concise, and verify the rendered SVG
  in the production preview at desktop and mobile sizes. Use a repository-owned
  image instead when Mermaid cannot express the visual clearly.
- Use an animated diagram when its progressive reveal helps explain a flow,
  sequence, dependency, architecture, or timeline. Do not add a chart merely
  to create motion. Mermaid SVG diagrams animate automatically once when they
  enter the viewport. A purpose-built inline SVG may use the documented
  `article-svg-figure` and `data-animate-svg` pattern when Mermaid cannot express
  the visual clearly. The shared pattern may expose its accessible user-started
  Replay control. Article content must not include its own autoplay, looping,
  or decorative animation instructions.
- Keep tables and diagrams readable: concise labels, clear units, source and
  cutoff where relevant, useful alt text or caption, and no page-level
  horizontal overflow.
- Do not add a raster hero by default. When an explanatory visual can replace
  photography, prefer an accessible repository-owned SVG. Reference a static
  SVG through an `<img>` when it should also become the homepage card thumbnail;
  use inline SVG only when article-specific structure or animation requires it.
  Do not embed raster data inside an SVG merely to change the file extension.
- When a raster hero is justified, crop and resize it for the reading column
  before publication. For a typical new article, use WebP or AVIF, keep the
  longest edge at 960px unless the subject needs more detail, target 80 KB or
  less, and treat anything above 120 KB as requiring an explicit content reason.
  Record accurate intrinsic `width` and `height`, then verify image quality,
  file size, the homepage thumbnail, and desktop/mobile article rendering.
- Distinguish verified facts, vendor claims, independent evidence, inference,
  and uncertainty. Date volatile information and link important external
  sources directly.
- Do not declare a universal winner from mixed evidence. A scoped winner or
  recommendation must name its criteria and include a practical caveat.
- Prefer tables for genuinely comparable structured data. Do not force prose
  into a table or compare incompatible measurements as if they were equal.
- End when the analysis is complete. Do not restate the entire article in a
  second conclusion.

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
