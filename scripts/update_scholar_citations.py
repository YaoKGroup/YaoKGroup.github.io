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

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


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
    entries: dict[str, dict] = {}
    with requests.Session() as session:
        session.headers["User-Agent"] = "Mozilla/5.0"
        for start in range(0, 1000, 100):
            response = session.get(
                "https://scholar.google.com/citations",
                params={"user": scholar_id, "hl": "en", "pagesize": 100, "cstart": start},
                timeout=(10, 30),
            )
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            rows = soup.select("tr.gsc_a_tr")
            if not rows:
                raise RuntimeError("Google Scholar returned no publication rows; existing data preserved.")
            previous_count = len(entries)
            for row in rows:
                link = row.select_one("a.gsc_a_at")
                count = row.select_one("a.gsc_a_ac")
                year = row.select_one(".gsc_a_y")
                if link is None or count is None:
                    raise RuntimeError("Unexpected Google Scholar publication markup.")
                title = link.get_text(strip=True)
                citation_text = count.get_text(strip=True)
                record = {
                    "title": title,
                    "citations": int(citation_text.replace(",", "")) if citation_text else 0,
                    "year": year.get_text(strip=True) if year else None,
                    "scholar_url": urljoin(response.url, link["href"]),
                }
                key = normalize_title(title)
                previous = entries.get(key)
                if previous is None or record["citations"] > previous["citations"]:
                    entries[key] = record
            print(f"Fetched {len(entries)} Google Scholar publications.", flush=True)
            more = soup.select_one("#gsc_bpf_more")
            if more is None or more.has_attr("disabled"):
                break
            if len(entries) == previous_count:
                raise RuntimeError("Google Scholar pagination did not advance.")
        else:
            raise RuntimeError("Google Scholar publication pagination exceeded the limit.")

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
        return 1

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

    if matched == 0:
        print("No site publications matched Google Scholar data.", file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = OUTPUT_PATH.with_suffix(".tmp")
    temporary_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    temporary_path.replace(OUTPUT_PATH)
    print(f"Updated {OUTPUT_PATH}: matched {matched}/{len(site_entries)} site publications.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
