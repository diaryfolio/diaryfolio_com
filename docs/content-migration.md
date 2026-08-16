# DiaryFolio content migration

## Canonical input

Place the Blogger export XML in `migration-input/` while importing. That directory is intentionally ignored: it may contain private drafts, comments, author data, and duplicated media URLs. Keep a separately backed-up original export.

The importer will convert published posts to `content/posts/` and static Blogger pages to `content/pages/`. Preserve each post's original publication date, title, labels, and legacy URL.

## Asset conventions

Assets used by a post live under the following path, where the date and slug match the published post:

```text
public/assets/images/original/YYYY/MM/post-slug/source-filename.ext
public/assets/images/derived/YYYY/MM/post-slug/source-filename-1200w.webp
```

Use `original/` for the untouched downloaded file. Use `derived/` only for optimised responsive variants. The generated content should link to paths beginning `/assets/images/...`, never to local disk paths or Blogger's image host.

Shared brand assets belong in `public/assets/images/site/` (create it when an asset is first added). Non-image attachments belong in `public/assets/downloads/YYYY/MM/post-slug/`.

## URL preservation

Blogger posts use paths such as `/2025/08/post-title.html`. Keep those exact output paths for migrated posts whenever possible. Record every unavoidable change in `redirects/legacy-urls.csv`, then generate Cloudflare redirect rules from it before the domain is switched.

Do not take Blogger offline until the deployed site has been crawled and its old URLs, canonical tags, feeds, sitemap, and image links have been checked.
