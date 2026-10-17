---
id: use-case-overview-gaps
typ: pruefpunkt
status: offen
thema: knowledge/ai_application_layer
stand: 2026-10-17
herkunft: Gespräch Projekt AI_news 2026-10-05; second pass against the live page and primary sources, Cle-session 2026-10-17
verweist_auf: [airport-biometric-checkin-use-case, sec-edgar-fulltext-search-is-the-reachable-primary-source, use-case-places-second-pass]
---

# Gaps in ai_use_cases_overview: candidates checked against the live card stock

## Aussage
The 2026-10-05 list was a keyword guess against a 98-card page. On 2026-10-17 the live page
(mendeltem.github.io/ai_use_cases_overview) was read directly: the array `const UC` holds 144 cards in 13 labelled
cluster blocks (Mobility, warehouse & energy, industry & humanoids, agriculture, medicine, hazardous, science, AI on
the local workstation, security & fraud, back office, city, enablers, compute & energy substrate) — the cluster
numbering has gaps, so the "18 clusters" of the SUMMARY come from more than this one array. Every candidate was then
matched against card titles plus card text, and the confirmed gaps were checked against primary sources.

**Confirmed gaps — no card. Five with a primary source, two without one (marked).**
- *Cashierless checkout (Just Walk Out).* No card. Amazon's FY2025 10-K names "Amazon's Just Walk Out technology"
  only inside a biometric-privacy class action; no deployment or store figure. So the technology is named in a filing
  but production scale is **unverified**.
- *ANPR and road tolling.* No card. Verra Mobility FY2025 10-K (CIK 1682745, filed 2026-02-24): Commercial Services
  $435.8M revenue 2025 (≈45 % of total), toll management ≈39 % and violation management ≈4 % of 2025 revenues,
  Parking Solutions $82.6M (≈8 %) with ≈1,775 parking customers, violation collection for foreign-registered vehicles
  in 20 European countries; "automated license plate recognition" is named. Shows: ANPR is the operating core of a
  listed photo-enforcement company with real revenue, not a pilot. This is the strongest new card candidate.
- *AI credit scoring / underwriting.* No card (only Fraud/AML banking, Insurance claims, Robo-advisory). Upstart
  FY2025 10-K (CIK 1647639): total revenue $1,043.9M in 2025 (2024: $636.5M), revenue from fees net $950.0M (+49 %),
  net income $53.6M, and the platform's approval decisions run on "our AI models"; in 2025 the top three lending
  partners originated 83 % of the loans facilitated through the marketplace. Shows: AI underwriting at a listed
  lender with real volume, and the concentration risk that comes with it.
- *Hearing aids with AI.* No card. Demant Annual Report 2025 states verbatim that "the most advanced hearing aids
  feature deep neural networks (DNNs) and use artificial intelligence (AI) to understand the sound scene"; the same
  report puts long-run market growth at ~6 % per year in units (upper end of a 4–6 % structural range) and estimates
  that ~13 million people were fitted with ~23 million hearing aids worldwide in 2025. Sonova FY2025/26: group sales
  CHF 3,605.9M (+5.9 % local), Hearing Instruments segment CHF 3,353.8M (+7.5 % local), normalized EBITA CHF
  811.2M; the release credits the "Infinio platform, including Infinio Ultra" with "AI-enabled hearing aid
  performance". Neither gives AI-attributable unit numbers. Shows: DNN-based hearing aids are a described, shipped
  product class in the two largest vendors' own reports.
- *Content moderation.* No card. TaskUs FY2025 10-K (CIK 1829864): Trust & Safety is a named reporting service line
  that "consists of two primary areas of service: Content Moderation and Financial Crime & Compliance"; the company
  supported ~200 clients as of 2025-12-31 and also sells AI Services (LLM support, data labelling) — but the filing
  names no AI system doing the moderation itself. Shows: content moderation is a real, reported business line, while
  the AI-in-the-loop claim is still unproven from this source.
- *Air traffic control.* No card; no source found this session. **Unverified.**
- *Mail sorting with handwriting recognition.* No card; USPS OIG search endpoints returned 406/403 from this network,
  no independent source found. **Unverified.**

**Not gaps — the 2026-10-05 keyword pass was wrong here.**
- Accessibility: cards "Be My Eyes" and "Be My AI" exist.
- Rail track inspection: "Rail predictive maintenance" (DB DIANA, Weichen-EKG) exists; the page's own note is right.
- Port automation: "AI container terminals" exists. The suspected "port = support" false positive does not apply.
- Delivery dispatch: "Logistics orchestration" (Walmart, DHL, Locus), "Sidewalk delivery robots" (Starship, Serve),
  "Autonomous trucks" and "Delivery & medical drones" already cover road and last-mile dispatch; a separate card is
  not obviously warranted.
- Insurance underwriting, steel/cement process control, pest control, factory predictive maintenance, payment fraud,
  telecom, mining, seismic, legal, HR, customer service, drug discovery, weather, translation, games, vision QC all
  have cards. Of the 11 Wednesday candidates only the seven listed above survived; the rest were already covered.

**New candidates found by holding industries without a card against known production cases.**
Automotive OEM manufacturing (the word "automotive" appears only in the Catena-X data-space card), consumer ADAS
(Super Cruise / BlueCruise, distinct from the robotaxi card), personalised advertising (probably the single largest AI
revenue line and absent), voice assistants, writing/coding assistants, e-commerce search and recommendation, fast-food
drive-thru AI, grocery demand forecasting, hotel revenue management. None of these was verified against a primary
source this session — they are candidates, not findings.

## Zu prüfen
1. Draft cards for the five sourced gaps (ANPR/tolling first) and send them to Mendel; page write access needed.
2. Verify the six candidates that have no source yet (ATC, mail sorting, checkout-free scale, computational
   photography, tutoring/adaptive learning, and the nine new industry candidates) the same way: production yes/no,
   figure with origin, authority vs company statement, maturity/evidence/growth.
3. Fresh read of the page before each pass — it changed twice in October alone; the keyword list from 05.10. is stale.
4. Decide language: this area is German, the standing rule says English for agent-written entries. Settled here by
   writing the entry in English and the INDEX row in the area's German style.

## Trägt nicht
That "no card" means no deployment — it means the page has no card. Some candidates (ATC, mail sorting) may still
turn out to be documented elsewhere. The card stock also moves: 98 → 143 → 144 cards within twelve days, so every
count here is a snapshot of 2026-10-17.

## Bruchindikator
A candidate confirmed as a real production case and still without a card after the next pass.

## Ablesung
- Live page JSON in `const UC`, fetched 2026-10-17 (144 cards, 13 labelled blocks); page URL
  https://mendeltem.github.io/ai_use_cases_overview/
- SEC EDGAR full-text search + filings read 2026-10-17: Upstart 10-K (CIK 1647639, FY2025, filed 2026-02),
  Verra Mobility 10-K (CIK 1682745, FY2025, filed 2026-02-24, confirmed via data.sec.gov submissions JSON), Amazon
  10-K (CIK 1018724, FY2025), TaskUs 10-K (CIK 1829864, FY2025). URLs are the Archives/edgar/data/<cik>/... .htm
  paths printed by the search tool. **Two search hits did not survive the quote:** Conduent has no FY2025 10-K
  (the term only appears in its 2018 8-K and older annual reports) and Rank One Computing (CIK 2077709) has filed no
  10-K at all — it appears via S-8/EX-3.1 registration statements only. Both were struck from the ANPR bullet.
- Demant Annual Report 2025 (PDF, demant.com investor relations, p. on hearing-aid technology and market growth);
  Sonova FY2025/26 results media release (PDF, sonova.com, 2026). Both opened 2026-10-17.
- Search reachability 2026-10-17: DuckDuckGo (html and lite) answered HTTP 202 anomaly, Mojeek a JS captcha, Bing
  RSS one unusable hit; GAO, USPS OIG, NHTSA and FAA endpoints 403/404/406; TED API requires POST; the DSA
  transparency API path was not found. See [sec-edgar-fulltext-search-is-the-reachable-primary-source].

## Verknüpft
- [airport-biometric-checkin-use-case](airport-biometric-checkin-use-case.md)
- [use-case-places-second-pass](use-case-places-second-pass.md)
- [sec-edgar-fulltext-search-is-the-reachable-primary-source](../../agent_tooling/findings/sec-edgar-fulltext-search-is-the-reachable-primary-source.md)
