#!/usr/bin/env python3
"""SEC EDGAR full-text search - primary-source company filings, no API key.

Written 2026-10-17 on the Cle workstation after measuring that the general web-search
endpoints do not answer from this network while EDGAR full text does (see the wiki
finding sec-edgar-fulltext-search-is-the-reachable-primary-source).

Usage:
  search_edgar.py "automated license plate recognition" [--form 10-K] [--from 2025-01-01] [--to 2026-10-17] [-n 10]

Notes:
  - Keep queries short and use the filer's own wording; several quoted OR-terms with a
    trailing word can return 0 hits even when the short form works.
  - Hits print the company, CIK, form, filing date and the exact Archive URL of the
    document. Fetch that URL with curl and a browser-ish User-Agent, not a bare default.
  - EDGAR only covers US-listed filers.

Requires only the standard library.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request

SEARCH = "https://efts.sec.gov/LATEST/search-index"
UA = "wiki-research (contact: see repo)"


def build_url(query: str, form: str | None, start: str | None, end: str | None) -> str:
    """Return the full-text-search URL for the given filters."""
    params = {"q": query}
    if form:
        params["forms"] = form
    if start:
        params["startdt"] = start
    if end:
        params["enddt"] = end
    return SEARCH + "?" + urllib.parse.urlencode(params)


def format_hits(data: dict, n: int) -> str:
    """Render an EDGAR search response as plain text. Pure - used by the tests."""
    hits = data.get("hits", {})
    total = hits.get("total", {}).get("value", 0)
    rows = hits.get("hits", [])[:n]
    out = [f"### total hits: {total}   (showing {len(rows)})"]
    for h in rows:
        src = h.get("_source", {})
        cik = (src.get("ciks") or [""])[0].lstrip("0")
        acc = h.get("_id", "").split(":")[0].replace("-", "")
        name = (src.get("display_names") or ["?"])[0]
        form_name = src.get("root_form") or src.get("file_type") or "?"
        filed = src.get("file_date", "?")
        file_name = h.get("_id", "").split(":")[-1]
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{file_name}"
        out.append(f"* {name}  (CIK {cik}) | {form_name} | filed {filed}")
        out.append(f"  {url}")
    return "\n".join(out)


def search(query: str, form: str | None, start: str | None, end: str | None, n: int) -> int:
    url = build_url(query, form, start, end)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as fh:
            data = json.loads(fh.read().decode("utf-8", "replace"))
    except Exception as exc:  # network, HTTP error, bad JSON
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"### SEC full-text: {query!r}  form={form}  range={start}..{end}")
    print(format_hits(data, n))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="SEC EDGAR full-text search")
    ap.add_argument("query")
    ap.add_argument("--form", default=None, help="e.g. 10-K, 10-Q, 8-K")
    ap.add_argument("--from", dest="start", default=None, help="start date YYYY-MM-DD")
    ap.add_argument("--to", dest="end", default=None, help="end date YYYY-MM-DD")
    ap.add_argument("-n", type=int, default=10)
    args = ap.parse_args()
    return search(args.query, args.form, args.start, args.end, args.n)


if __name__ == "__main__":
    raise SystemExit(main())
