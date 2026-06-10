#!/usr/bin/env python3
"""Update Google Scholar citation counts for the publications page."""

from __future__ import annotations

import difflib
import html
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from scholarly import scholarly


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_PATH = ROOT / "publications.md"
OUTPUT_PATH = ROOT / "assets" / "data" / "scholar_citations.json"
CONFIG_PATH = ROOT / "_config.yml"


def normalize_title(title: str) -> str:
    text = html.unescape(title or "")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[\u2010-\u2015\u2212]", "-", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower().replace("&", "and")
    text = re.sub(r"\(\s*news\s+and\s+views\s*\)", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def scholar_id_from_config() -> str | None:
    if not CONFIG_PATH.exists():
        return None
    match = re.search(r"scholar\.google\.com/citations\?[^\"'\n]*user=([A-Za-z0-9_-]+)", CONFIG_PATH.read_text())
    return match.group(1) if match else None


def get_scholar_id() -> str:
    scholar_id = os.getenv("GOOGLE_SCHOLAR_ID") or scholar_id_from_config()
    if not scholar_id:
        raise RuntimeError("Set GOOGLE_SCHOLAR_ID or add a Google Scholar profile URL to _config.yml.")
    return scholar_id


def site_publication_titles() -> list[str]:
    if not PUBLICATIONS_PATH.exists():
        raise RuntimeError(f"Cannot find {PUBLICATIONS_PATH}.")
    text = PUBLICATIONS_PATH.read_text()
    return [html.unescape(re.sub(r"<[^>]+>", "", item)).strip()
            for item in re.findall(r'<span class="pub-title">(.*?)</span>', text, flags=re.S)]


def scholar_publications(scholar_id: str) -> dict[str, dict]:
    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(author, sections=["publications"])

    entries: dict[str, dict] = {}
    for publication in author.get("publications", []):
        bib = publication.get("bib", {})
        title = bib.get("title")
        if not title:
            continue

        key = normalize_title(title)
        author_pub_id = publication.get("author_pub_id")
        scholar_url = None
        if author_pub_id:
            scholar_url = (
                "https://scholar.google.com/citations?view_op=view_citation"
                f"&hl=en&user={scholar_id}&citation_for_view={author_pub_id}"
            )

        record = {
            "title": title,
            "citations": int(publication.get("num_citations") or 0),
            "year": bib.get("pub_year"),
            "scholar_url": scholar_url,
        }

        previous = entries.get(key)
        if previous is None or record["citations"] > previous["citations"]:
            entries[key] = record

    return entries


def best_match(site_title: str, scholar_entries: dict[str, dict]) -> tuple[dict | None, float]:
    site_key = normalize_title(site_title)
    if site_key in scholar_entries:
        return scholar_entries[site_key], 1.0

    best_key = None
    best_score = 0.0
    for scholar_key in scholar_entries:
        score = difflib.SequenceMatcher(None, site_key, scholar_key).ratio()
        if score > best_score:
            best_key = scholar_key
            best_score = score

    if best_key is None:
        return None, 0.0

    contains_match = site_key in best_key or best_key in site_key
    if best_score >= 0.88 or (contains_match and best_score >= 0.80):
        return scholar_entries[best_key], best_score

    return None, best_score


def main() -> int:
    scholar_id = get_scholar_id()
    try:
        scholar_entries = scholar_publications(scholar_id)
    except Exception as exc:
        print(
            "::warning title=Google Scholar fetch failed::"
            f"Could not fetch Google Scholar data ({type(exc).__name__}: {exc}). "
            "Keeping the existing citation data."
        )
        if OUTPUT_PATH.exists():
            return 0
        raise

    site_entries: dict[str, dict] = {}

    matched = 0
    for title in site_publication_titles():
        key = normalize_title(title)
        record, score = best_match(title, scholar_entries)
        if record:
            matched += 1
            site_entries[key] = {
                "title": title,
                "citations": record["citations"],
                "scholar_title": record["title"],
                "scholar_url": record["scholar_url"],
                "match_score": round(score, 3),
            }
        else:
            site_entries[key] = {
                "title": title,
                "citations": None,
                "scholar_title": None,
                "scholar_url": None,
                "match_score": round(score, 3),
            }

    output = {
        "source": "Google Scholar",
        "scholar_id": scholar_id,
        "profile_url": f"https://scholar.google.com/citations?user={scholar_id}",
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "total_scholar_publications": len(scholar_entries),
        "total_site_publications": len(site_entries),
        "matched_site_publications": matched,
        "site_citations_by_title": site_entries,
        "scholar_citations_by_title": scholar_entries,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"Updated {OUTPUT_PATH}: matched {matched}/{len(site_entries)} site publications.")
    if matched == 0:
        print("No site publications matched Google Scholar data.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
