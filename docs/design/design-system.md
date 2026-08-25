# Compact technical-blog design system

## Direction

DiaryFolio is a working technical archive, not a magazine or lifestyle blog. The interface prioritises scanning, reading, code, diagrams, and long-lived URLs. Decoration is deliberately secondary to information density.

## Layout

- Content shell: maximum 1080px with compact responsive gutters.
- Reading column: maximum 760px for articles.
- Homepage/search: two-column card grid above 700px; one-column list below it.
- Header: sticky, 3.9rem high, with clear current-page state.
- Cards: 8px corners, quiet borders, restrained hover elevation, and small image thumbnails aligned to the upper-right.

## Type scale

The system uses native system fonts to avoid render-blocking font downloads.

| Element | Desktop | Mobile |
| --- | --- | --- |
| Homepage/search title | 1.9–2.85rem | 1.65–2.2rem |
| Article title | 1.8–2.65rem | 1.65–2.2rem |
| Card title | 1.1rem | 1.02rem |
| Article body | 1rem / 1.72 | .96rem / 1.72 |
| Metadata/tags | .62–.76rem | same |

Technical metadata, tags, dates, code labels, and the footer use the system monospace stack. Body copy remains sans-serif for consistent screen readability.

## Editorial voice

- Articles use concise, direct technical prose with short sentences and
  focused paragraphs.
- New or materially edited public copy uses plain ASCII punctuation wherever
  possible. Em dashes, en dashes, and smart quotes are replaced with sentence
  breaks or ordinary ASCII punctuation unless the subject itself requires the
  original character.
- Stock AI phrases, inflated transitions, process narration, repeated
  conclusions, clickbait, and filler are removed.
- Articles are written for the end reader: practical meaning comes first,
  unavoidable jargon is explained, and concrete examples are used when they
  improve understanding.
- Long prose is replaced with a clear table, short list, or diagram when the
  visual structure makes comparison, sequence, architecture, or dependency
  materially easier to understand. Visuals are informative rather than
  decorative.
- For a justified diagram, the preferred evaluation order is: a purpose-built
  animated inline SVG when progressive reveal improves understanding; a static
  inline SVG when motion adds no value or is impractical; then Mermaid when its
  maintained syntax is the clearer or more economical representation. This is
  a decision order, not a requirement to animate every visual. Accessibility,
  a complete static state, narrow-screen readability, and reduced-motion
  behaviour override the preference.
- Fenced `mermaid` blocks are enhanced into SVG on article pages. Mermaid is
  loaded lazily only when a diagram exists, uses strict security and a fixed
  high-contrast neutral canvas, and makes no third-party CDN request. Every
  diagram includes `accTitle` and `accDescr` and is checked at desktop and
  mobile sizes. A repository-owned image remains preferable when Mermaid
  cannot express the visual clearly.
- Mermaid SVG output receives one restrained viewport-triggered reveal. Motion
  is loaded from the local bundle only after Mermaid has rendered a diagram.
  Visible unfilled strokes draw progressively while the complete SVG fades in;
  charts without suitable stroke geometry receive only the short reveal. The
  effect does not loop and is not a reason to add an otherwise unnecessary
  visual.
- A purpose-built inline SVG may use `article-svg-figure` with
  `data-animate-svg` when its labelled structure is clearer than Mermaid. Child
  elements marked `data-svg-step` reveal in reading order and
  `data-svg-link` strokes draw between them. The complete accessible SVG is
  present in the article HTML, stays useful without JavaScript, reveals once,
  and skips motion when the reader requests reduced motion. A compact Replay
  control with a refresh icon is enabled only after Motion loads; it restarts
  that diagram on demand, disables while running, and remains hidden for
  reduced-motion readers or enhancement failures.
- Researched articles lead with a compact **Quick read** containing the main
  answer, useful takeaways, and a material caveat.
- Facts, vendor claims, independent evidence, inference, and uncertainty stay
  distinguishable. Scoped recommendations name their criteria and caveat.
- Internal research identifiers remain in frontmatter and are not presented
  as reader-facing sources.

## Colour

- Neutral slate ink and cool-grey surfaces provide the main hierarchy.
- Teal is reserved for links, focus, and technical accents.
- Rust marks dates and eyebrow labels without dominating the page.
- Dark mode maps the same roles to higher-contrast values rather than inverting arbitrary colours.

## Cards and images

- A card uses the first image found in the migrated article as a compact thumbnail.
- Thumbnails are decorative because the linked title already names the destination.
- Cards without an image retain the same textual hierarchy without an empty placeholder.
- Full article images are width-constrained, bordered, and allowed to preserve their natural aspect ratio.
- Article video embeds use the reusable `article-video` class so a 16:9 player fills the reading column without overflowing or becoming too tall on small screens. Prefer privacy-enhanced provider URLs when available.
- New articles do not require a raster hero. An accessible, repository-owned
  static SVG is preferred when a diagram communicates the subject as well as
  photography. Referencing that SVG through an `<img>` lets the existing card
  extractor reuse it on the homepage. Inline SVG remains appropriate for
  article-only or animated diagrams, but is not extracted as a card thumbnail.
- SVG assets contain real vector geometry and no embedded base64 or linked
  raster payload used merely to disguise image weight. They are responsive,
  have useful alternative text when referenced as images, and are checked in
  the homepage card as well as the article.
- A typical new raster hero is cropped to the intended composition, encoded as
  WebP or AVIF, and limited to a 960px longest edge unless fine detail requires
  more. The normal target is at most 80 KB. Files above 120 KB require an
  explicit content reason and a recorded visual check showing that a smaller
  version is not adequate. Intrinsic width and height in article markup match
  the final file.
- Image QA checks decoded appearance, byte size, desktop and mobile rendering,
  and the homepage thumbnail. A diagram or text-only card is preferable to a
  decorative duplicate asset.

## Code and data

- Inline code uses a low-contrast panel and monospace type.
- Block code uses a dark, high-contrast panel with a small toolbar.
- Long snippets collapse by default and expose Expand/Collapse and Copy controls.
- Standard article tables use the full reading-column width and wrap long cell content so their visual grid reaches the table border without creating an empty strip. Tables intentionally wider than the reading column use the reusable `wide-table-wrap` and `wide-table` horizontal-scroll pattern; the curated timeline table becomes labelled cards on small screens.
- Benchmark tables fill the reading column on wide screens and scroll inside a dedicated container on narrow screens. The benchmark-name column receives 30% of the table width; comparison columns divide the remainder evenly, and long model names wrap instead of distorting the grid. Leaders use a shaded cell, accent edge, bold value, and a visible text label so the distinction remains clear without relying on colour alone.
- Mermaid diagrams render inside a bordered, horizontally contained figure.
  SVG output scales to the reading column, while any exceptional intrinsic
  width scrolls within the figure rather than overflowing the page.

## Accessibility and motion

- A keyboard-visible skip link targets the main content.
- All interactive controls receive a visible three-pixel focus ring.
- The active navigation item uses `aria-current="page"`.
- Search results report changes through a polite live region and expose loading state.
- Motion and smooth scrolling are disabled when the visitor requests reduced motion.
- SVG diagram animation starts only when at least 20% of the diagram enters the
  viewport, runs once, and leaves the complete static SVG in place. It is
  skipped entirely when the visitor requests reduced motion. Drawable geometry
  is capped per diagram to keep complex charts responsive. Print styles always
  expose the completed SVG, even when it has not entered the screen viewport.

## Consent surfaces

- The analytics consent panel is a small fixed-bottom notice that uses the existing card, colour, type, and focus systems. Its copy stays to one compact sentence on normal desktop widths and wraps above the actions on narrow screens.
- Accept and reject are both explicit buttons; the banner has no preselected choice and does not seize focus on first display.
- At narrow widths the content and controls stack, with both actions retaining comfortable touch targets and no horizontal overflow.
- The footer always links to the privacy page. When Analytics is configured, it also exposes a persistent Cookie settings button so withdrawal is as accessible as acceptance.
- The banner is rendered only when the Analytics build variable exists and no current choice has been stored.
