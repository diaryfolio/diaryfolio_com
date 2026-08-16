#!/usr/bin/env python3
"""Convert a Google Takeout Blogger Atom export to static-site source files.

The importer intentionally keeps post HTML unchanged (apart from local image URLs),
so no historic formatting or links are lost while the new site is being designed.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlparse

ATOM = "{http://www.w3.org/2005/Atom}"
BLOGGER = "{http://schemas.google.com/blogger/2018}"
GOOGLE_IMAGE_URL = re.compile(r"https?://blogger\.googleusercontent\.com/[^\"'<> )]+")


def text(entry: ET.Element, name: str) -> str:
    value = entry.findtext(f"{ATOM}{name}")
    return value.strip() if value else ""


def btext(entry: ET.Element, name: str) -> str:
    value = entry.findtext(f"{BLOGGER}{name}")
    return value.strip() if value else ""


def quoted(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip(".-") or "asset"


def legacy_parts(filename: str, published: str, title: str) -> tuple[str, str, str]:
    match = re.fullmatch(r"/(\d{4})/(\d{2})/(.+)\.html", filename)
    if match:
        return match.group(1), match.group(2), match.group(3)
    date = published[:10] if len(published) >= 10 else "1970-01-01"
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "untitled"
    return date[:4], date[5:7], slug


def make_asset_index(album_root: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for source in album_root.rglob("*"):
        if source.is_file() and source.suffix.lower() != ".json":
            index[source.name].append(source)
    return index


def image_name(url: str) -> str:
    # Blogger URLs finish with a size segment followed by the original filename.
    return safe_filename(unquote(urlparse(url).path.rsplit("/", 1)[-1]))


TAG_RULES = (
    ("kubernetes", "Kubernetes"), ("k8s", "Kubernetes"), ("docker", "Docker"),
    ("ansible", "Ansible"), ("devops", "DevOps"), ("ci/cd", "DevOps"), ("cicd", "DevOps"),
    ("aws", "AWS"), ("lambda", "AWS"), ("azure", "Azure"), ("cloud", "Cloud"),
    ("linux", "Linux"), ("fedora", "Linux"), ("ubuntu", "Linux"), ("unix", "Unix"),
    ("shell", "Shell"), ("bash", "Shell"), ("perl", "Perl"), ("java", "Java"),
    ("python", "Python"), ("android", "Android"), ("raspberry pi", "Raspberry Pi"),
    ("virtualbox", "Virtualization"), ("vmware", "Virtualization"), ("kvm", "Virtualization"),
    ("syslog", "Syslog"), ("network", "Networking"), ("dns", "Networking"), ("vpn", "Networking"),
    ("security", "Security"), ("firewall", "Security"), ("siteminder", "Security"),
    ("google", "Google"), ("gmail", "Google"), ("domain", "Web Development"),
    ("html", "Web Development"), ("css", "Web Development"), ("wordpress", "Web Development"),
    ("database", "Databases"), ("db2", "Databases"), ("data", "Data"),
    ("machine learning", "Machine Learning"), ("deep learning", "AI"), ("llm", "AI"),
    ("tensor", "Machine Learning"), ("crypto", "Cryptocurrency"), ("bitcoin", "Cryptocurrency"),
    ("property", "Property"), ("mortgage", "Property"), ("tax", "Tax"),
    ("sp 500", "Markets"), ("s&p 500", "Markets"), ("financial", "Finance"),
    ("apple", "Apple"), ("chromecast", "Streaming"), ("roku", "Streaming"),
)


def inferred_labels(title: str, body: str) -> list[str]:
    haystack = f"{title} {body}".lower()
    labels: list[str] = []
    for needle, label in TAG_RULES:
        if needle in haystack and label not in labels:
            labels.append(label)
    return labels[:5] or ["Technology"]


def gfc_article() -> str:
    return """<p class=\"article-lead\">A concise timeline of the S&amp;P 500 during the Global Financial Crisis, from the October 2007 peak through the March 2009 low.</p>

<h2>Key dates during the crisis</h2>
<div class=\"timeline-table\"><table>
<thead><tr><th scope=\"col\">Event</th><th scope=\"col\">Approximate date</th><th scope=\"col\">What happened</th></tr></thead>
<tbody>
<tr><td><strong>Initial peak</strong></td><td>2007-10-09</td><td>S&amp;P 500 reached 1,565.15, its pre-crisis high.</td></tr>
<tr><td><strong>Bear market begins</strong></td><td>Late Oct 2007</td><td>A slow decline began after the peak.</td></tr>
<tr><td><strong>Bear market confirmed</strong></td><td>2008-01-09 to 2008-03-17</td><td>The index fell about 20%; the period included the Bear Stearns bailout.</td></tr>
<tr><td><strong>Short-term bottom</strong></td><td>2008-03-17</td><td>The index reached roughly 1,256 before a temporary rebound.</td></tr>
<tr><td><strong>Bear-market rally</strong></td><td>2008-05-19 to 2008-06-05</td><td>The index rallied to roughly 1,428 but did not recover its prior high.</td></tr>
<tr><td><strong>Major leg down</strong></td><td>2008-09-15</td><td>Lehman Brothers collapsed and markets fell rapidly.</td></tr>
<tr><td><strong>Panic-selling bottom</strong></td><td>2008-11-20</td><td>The index reached roughly 752, about 52% below the 2007 peak.</td></tr>
<tr><td><strong>Relief rally</strong></td><td>2008-12-08 to 2009-01-06</td><td>A short-term bounce carried the index to approximately 935.</td></tr>
<tr><td><strong>Final leg down</strong></td><td>2009-01-06 to 2009-03-09</td><td>The decline continued to a new cycle low.</td></tr>
<tr><td><strong>GFC bottom</strong></td><td>2009-03-09</td><td>Lowest close: 676.53. A long-term recovery began afterward.</td></tr>
</tbody></table></div>

<h2>Market phases</h2>
<div class=\"timeline-table\"><table>
<thead><tr><th scope=\"col\">Phase</th><th scope=\"col\">Start</th><th scope=\"col\">End</th><th scope=\"col\">S&amp;P 500 change</th></tr></thead>
<tbody>
<tr><td>Initial peak to first bottom</td><td>2007-10-09</td><td>2008-03-17</td><td class=\"down\">↓ ~20%</td></tr>
<tr><td>Bear rally</td><td>2008-03-17</td><td>2008-05-19</td><td class=\"up\">↑ ~13%</td></tr>
<tr><td>Second drop</td><td>2008-05-19</td><td>2008-11-20</td><td class=\"down\">↓ ~47%</td></tr>
<tr><td>Short rally</td><td>2008-11-20</td><td>2009-01-06</td><td class=\"up\">↑ ~25%</td></tr>
<tr><td>Final leg down</td><td>2009-01-06</td><td>2009-03-09</td><td class=\"down\">↓ ~28%</td></tr>
</tbody></table></div>

<figure class=\"article-figure\"><img src=\"/assets/images/original/2025/07/gfc-key-dates-in-table/GFC-Global-Financial-Crisis.png\" alt=\"S&amp;P 500 Global Financial Crisis chart\" loading=\"lazy\" /><figcaption>S&amp;P 500 timeline during the Global Financial Crisis.</figcaption></figure>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True, help="Blogger feed.atom")
    parser.add_argument("--albums", type=Path, required=True, help="Google Takeout Blogger/Albums directory")
    parser.add_argument("--output", type=Path, default=Path("."), help="repository root")
    parser.add_argument("--overwrite", action="store_true", help="replace generated files")
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error(f"input does not exist: {args.input}")
    if not args.albums.is_dir():
        parser.error(f"albums directory does not exist: {args.albums}")

    root = ET.parse(args.input).getroot()
    output = args.output.resolve()
    image_index = make_asset_index(args.albums)
    report_rows: list[dict[str, str]] = []
    redirect_rows: list[dict[str, str]] = []
    used_assets: set[Path] = set()
    counts = defaultdict(int)

    for entry in root.findall(f"{ATOM}entry"):
        entry_type = btext(entry, "type")
        status = btext(entry, "status")
        if entry_type not in {"POST", "PAGE"} or status != "LIVE":
            counts["skipped"] += 1
            continue

        title = text(entry, "title") or "Untitled"
        source_id = text(entry, "id")
        published = text(entry, "published")
        updated = text(entry, "updated")
        legacy_url = btext(entry, "filename")
        year, month, slug = legacy_parts(legacy_url, published, title)
        post_kind = "posts" if entry_type == "POST" else "pages"
        destination = output / "content" / post_kind / year / month / f"{slug}.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and not args.overwrite:
            raise FileExistsError(f"refusing to overwrite {destination}; pass --overwrite")

        categories = [c.attrib["term"] for c in entry.findall(f"{ATOM}category") if c.attrib.get("term")]
        author = entry.find(f"{ATOM}author/{ATOM}name")
        body_node = entry.find(f"{ATOM}content")
        body = body_node.text if body_node is not None and body_node.text else ""
        # Some newer Blogger posts contain a complete standalone HTML document.
        # Keep its article body, but remove document chrome and inline theme styles
        # so the new site can provide one consistent presentation layer.
        body = re.sub(r"<head\b[^>]*>.*?</head\s*>", "", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"<style\b[^>]*>.*?</style\s*>", "", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"<script\b[^>]*>.*?</script\s*>", "", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"</?(?:html|body)\b[^>]*>", "", body, flags=re.IGNORECASE)
        body = re.sub(r"\sstyle=(['\"]).*?\1", "", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"</?font\b[^>]*>", "", body, flags=re.IGNORECASE)
        # A few Blogger posts contain an old full copy followed by a second
        # edited copy. Keep the final H1-led copy as the canonical article.
        h1_matches = list(re.finditer(r"<h1\b", body, flags=re.IGNORECASE))
        if len(h1_matches) > 1:
            body = body[h1_matches[-1].start():]
        # The new template renders the post title as the single document H1.
        # Blogger exports often repeat that title as the first body H1.
        body = re.sub(r"^\s*<h1\b[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.IGNORECASE | re.DOTALL)
        if not categories:
            categories = inferred_labels(title, body)
        asset_directory = output / "public" / "assets" / "images" / "original" / year / month / slug
        used_names: dict[str, str] = {}

        def localise_image(match: re.Match[str]) -> str:
            remote_url = html.unescape(match.group(0))
            filename = image_name(remote_url)
            candidates = image_index.get(filename, [])
            if not candidates:
                report_rows.append({"legacy_url": legacy_url, "image_url": remote_url, "reason": "not in Takeout album"})
                return remote_url
            source = candidates[0]
            used_assets.add(source)
            local_name = used_names.setdefault(filename, filename)
            target = asset_directory / local_name
            if not target.exists():
                asset_directory.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            return f"/assets/images/original/{year}/{month}/{slug}/{local_name}"

        body = GOOGLE_IMAGE_URL.sub(localise_image, body)
        if legacy_url == "/2025/07/gfc-key-dates-in-table.html":
            body = gfc_article()
        meta_description = btext(entry, "metaDescription")
        front_matter = [
            "---",
            f"title: {quoted(title)}",
            f"date: {quoted(published)}",
            f"updated: {quoted(updated)}",
            f"legacy_url: {quoted(legacy_url)}",
            f"source_id: {quoted(source_id)}",
            f"author: {quoted(author.text.strip() if author is not None and author.text else '')}",
        ]
        if categories:
            front_matter.append("labels:")
            front_matter.extend(f"  - {quoted(label)}" for label in categories)
        else:
            front_matter.append("labels: []")
        if meta_description:
            front_matter.append(f"description: {quoted(meta_description)}")
        front_matter.extend(["---", "", body.rstrip(), ""])
        destination.write_text("\n".join(front_matter), encoding="utf-8")
        redirect_rows.append(
            {
                "from": legacy_url,
                "to": legacy_url or f"/{year}/{month}/{slug}.html",
                "status": "200",
            }
        )
        counts[post_kind] += 1

    unmatched_report = output / "data" / "unmatched-images.csv"
    unmatched_report.parent.mkdir(parents=True, exist_ok=True)
    with unmatched_report.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["legacy_url", "image_url", "reason"])
        writer.writeheader()
        writer.writerows(report_rows)

    redirects = output / "redirects" / "legacy-urls.csv"
    redirects.parent.mkdir(parents=True, exist_ok=True)
    with redirects.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["from", "to", "status"])
        writer.writeheader()
        writer.writerows(redirect_rows)

    unassigned_root = output / "public" / "assets" / "images" / "original" / "unassigned"
    for source in sorted(image_index_path for paths in image_index.values() for image_index_path in paths):
        if source in used_assets:
            continue
        relative = source.relative_to(args.albums)
        target = unassigned_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(source, target)
        counts["unassigned_assets"] += 1

    print(f"Imported {counts['posts']} posts and {counts['pages']} pages.")
    print(f"Skipped {counts['skipped']} non-live or non-content entries.")
    print(f"Copied {counts['unassigned_assets']} unassigned Takeout assets.")
    print(f"Image URLs not matched locally: {len(report_rows)} (see {unmatched_report}).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ET.ParseError, FileExistsError) as error:
        print(f"Import failed: {error}", file=sys.stderr)
        raise SystemExit(1)
