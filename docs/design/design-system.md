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

## Code and data

- Inline code uses a low-contrast panel and monospace type.
- Block code uses a dark, high-contrast panel with a small toolbar.
- Long snippets collapse by default and expose Expand/Collapse and Copy controls.
- Tables scroll horizontally by default; the curated timeline table becomes labelled cards on small screens.

## Accessibility and motion

- A keyboard-visible skip link targets the main content.
- All interactive controls receive a visible three-pixel focus ring.
- The active navigation item uses `aria-current="page"`.
- Search results report changes through a polite live region and expose loading state.
- Motion and smooth scrolling are disabled when the visitor requests reduced motion.
