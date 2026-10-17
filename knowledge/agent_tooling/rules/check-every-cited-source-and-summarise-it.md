---
id: check-every-cited-source-and-summarise-it
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-17
herkunft: user rule 2026-10-17 after a research report by a remote-model agent with wrong references; Alita session
verweist_auf: [disk-guard-verified-move-and-compact-literature-search]
---

# Every cited source is checked against the original and carries a one-sentence summary

## Aussage
Before a report, answer or wiki entry cites a source: (1) the source exists and its link works (PMID found in PubMed,
DOI registered at doi.org), (2) the PMID belongs to the cited title, (3) the claim it backs is in its abstract, and
(4) each reference carries one sentence "Shows: ..." with what the paper found. Anything that cannot be checked is
marked "unverified". Never cite from memory; copy titles and ids from the retrieved record.

## Trägt
2026-10-17: three research reports by the same agent and model (hospital model hub). Two were fully correct (22/22 and 39/39
references). The third had 20 of 28 references with REAL PMIDs attached to invented, generic titles ("Effect of infarcts
and enlarged ventricles on automated subcortical segmentation" pointing at a paper on cortical thickness harmonisation).
Real numbers made the wrong list look trustworthy; only the automatic comparison with PubMed found it.

## Trägt nicht
The title check does not prove that the claim is in the paper; that needs reading the abstract (the tool prints the last
abstract sentence with --kurz as an aid). References without PMID or DOI (software, web pages) are checked by hand.

## Bruchindikator
A report that passes the tool but whose claims are not in the cited abstracts.

## Ablesung
- tool `quellen-pruefen REPORT.md [--kurz]` (2026-10-17): PubMed efetch title match (first 40 letters/digits), DOI
  registration via https://doi.org/api/handles/<doi> (responseCode 1), exit 1 on any WRONG line
- NCBI E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/ ; DOI handle API: https://www.doi.org/the-identifier/resources/factsheets/doi-resolution-documentation
- own check runs 2026-10-17 on the three reports
