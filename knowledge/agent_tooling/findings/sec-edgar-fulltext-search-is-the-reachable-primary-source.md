---
id: sec-edgar-fulltext-search-is-the-reachable-primary-source
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-17
herkunft: Cle-session 2026-10-17, web research for the use-case gap check blocked by the network
verweist_auf: [disk-guard-verified-move-and-compact-literature-search, check-every-cited-source-and-summarise-it]
---

# From this network only a few search endpoints answer; SEC EDGAR full text is the one that gives primary sources

## Aussage
1. Measured on 2026-10-17 from the Cle workstation: the general web-search endpoints are unusable, but
   **SEC EDGAR full-text search works** and returns company filings (10-K, 10-Q, 8-K, EX-99 presses) with the exact
   Archive URL of the document. That is a primary source for every listed company — revenue, volumes and the
   wording a company uses for its own AI features — reachable without an API key.
   Endpoint used: `https://efts.sec.gov/LATEST/search-index?q=<query>&forms=<form>&startdt=<date>` (JSON, hit list
   with `_id`), documents under `https://www.sec.gov/Archives/edgar/data/<cik>/<accession>/<file>.htm`. A browser-ish
   `User-Agent` is enough; a bare curl default may be refused.
2. What does NOT answer from here (all checked the same day): DuckDuckGo html and lite both HTTP 202 with an anomaly
   page, Mojeek serves a JS captcha, Bing `format=rss` returns one unusable hit, GAO 403, USPS OIG 406, NHTSA 403,
   FAA technology paths 404, TED API 405 (needs POST), the DSA transparency API path not found. Wikipedia and
   gov.uk-style pages that were guessed directly still opened.
3. Consequence for research: when a general search is unreachable, do not give up and do not cite from memory — go to
   the primary-source registers that are open (SEC EDGAR for companies, PubMed/Europe PMC/OpenAlex/arXiv for papers)
   and for the rest try the exact URL, not a search. The lists of regulators and ministries in the gaps check
   ("Suchquellen") look right in principle but several of their search endpoints are closed from this network.
4. Full text search needs the right spelling and short queries: `"letter sorting"` returned 0 hits while
   `"automated license plate recognition"` returned stock in 10-Ks; the terms must be the filer's own. Long queries
   with several quoted OR-terms and a trailing word (e.g. `"photonic engine" OR "computational photography"`) can
   return 0 hits even though the short form works — start short, then narrow with `--form 10-K` before reading.

## Trägt
Own runs 2026-10-17: Upstart 10-K (CIK 1647639) total revenue $1,043.9M 2025 and $950.0M net fee revenue read from the
document; Verra Mobility 10-K (CIK 1682745) segment and toll/violation shares read; Amazon 10-K (CIK 1018724) searched
for "Just Walk Out"; Demant Annual Report 2025 PDF and Sonova FY2025/26 release PDF downloaded and read. Every figure
came out of the document, not out of a snippet.

## Trägt nicht
EDGAR covers only US-listed filers: European, Chinese and private companies stay invisible (Sonova and Demant are
Swiss/Danish, so they had to be fetched from their own investor-relations PDFs). It also says nothing about a
technology being in production — a filing naming a feature is not a deployment figure.

## Bruchindikator
An EDGAR hit whose quoted text is not in the document at the printed Archive URL (i.e. a stale accession path).

## Ablesung
- SEC EDGAR full-text search: https://efts.sec.gov/LATEST/search-index (searched 2026-10-17); SEC EDGAR browse and
  fair-access notes: https://www.sec.gov/os/accessing-edgar-data
- Windows of unreachability listed under Aussage point 2, measured with curl from the Cle workstation 2026-10-17
- the search helper written for this session sits in the wiki repo at
  `tools/general/web_research/src/search_edgar.py` (scratch copy was `/tmp/sec.py`); documents were fetched with
  curl + `pdftotext`, 2026-10-17
