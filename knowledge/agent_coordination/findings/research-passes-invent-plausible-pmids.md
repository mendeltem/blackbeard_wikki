---
id: research-passes-invent-plausible-pmids
typ: befund
status: getragen
thema: knowledge/agent_coordination
stand: 2026-10-21
herkunft: own runs 2026-10-21, three headless Claude research passes on the three-data-classes rule
verweist_auf: [three-data-classes-decide-what-may-leave-the-institution, remote-model-gets-only-data-free-skills-and-redacted-text]
---

# Research passes invent plausible PMIDs

## Aussage
An agent asked to research a topic returns citations that *look* right and are wrong. On 2026-10-21 three headless
research passes (Claude Code, `claude -p`, read-only tools, network on) were run against the three-data-classes rule.
One pass cited Schwarz et al. 2019 NEJM with PMID 31657887 and Rocher et al. 2019 Nature Communications with PMID
31427575, plus a PMC link. Checked against PubMed:

- PMID 31657887 is "Discrimination, Abuse, Harassment, and Burnout in Surgical Residency Training" (Hu YY, NEJM 2019).
- PMID 31427575 is "AAV-ie enables safe and efficient gene transfer to inner ear cells" (Tan F, Nat Commun 2019).
- The correct Schwarz PMID is 31644852, "Identification of Anonymous MRI Research Participants with Face-Recognition
  Software" (N Engl J Med 2019).
- The Rocher claim could not be verified at all; the citation was removed rather than repaired.

The numbers the pass reported (92 % embedding recovery, 70 of 84 rank-1 matches) were plausible and the *topics* were
right - only the identifiers were fabricated. A wrong PMID on a real-looking claim is harder to catch than a
nonsensical one.

**Same trap, one step further in (own error, same day).** After correcting the PMID, the figure "70 of 84 rank-1
matches" was copied into the rule as if verified. It is not: PMID 31644852 is a brief report with **no abstract**, so the
number was never read anywhere. An identifier can be perfectly real and the number beside it still invented. The rule now
says the figures were not read. A verified id is not a verified sentence.

## Trägt
It settles how to consume a research pass: treat every identifier as a claim to be checked, never as a lookup already
done. The check is cheap (one EUtils/Europe PMC call per id) and the failure is silent otherwise. It also justifies
using several independent passes: the passes agreed on the *shape* (Turing tiers, DUO vocabulary, output checking) and
disagreed on nothing structural, so the consensus carries even where a single citation does not.

## Trägt nicht
It does not mean the passes are useless. Two of three produced verified, load-bearing material: the Turing Data Safe
Haven tier mapping, the UK Biobank/SAIL/Five Safes output-checking comparison, and the DUO label list. The DUO labels
were re-read from `duo.csv` and matched exactly. The failure was narrow - identifiers - not the research.

It also does not mean a check makes a source *true*: a valid PMID proves the paper exists and has that title, not that
it supports the sentence it is attached to. That second step (read the abstract) stays manual.

## Bruchindikator
A wiki entry carries a PMID or DOI that the sources-check tool cannot tie to its title, or that resolves to an
unrelated paper. A citation is copied from a research pass without a check, or a "corrected" identifier is written
without reading the paper it now points to. The same applies to a DOI that resolves but to the wrong article.

## Ablesung
Check, own runs 2026-10-21: PubMed EUtils `esummary` for a PMID returns title, journal, first author - compare against
the claim. Europe PMC `search?query=DOI:"..."` resolves a DOI to its article. Corrected Schwarz reference:
https://pubmed.ncbi.nlm.nih.gov/31644852/ . Removed reference: Rocher et al. 2019, Nat Commun - PMID unverified, not
reinstated. Rule that consumes this: [three-data-classes-decide-what-may-leave-the-institution](../rules/three-data-classes-decide-what-may-leave-the-institution.md).
Tool for the standing check: `system/werkzeuge/quellen-pruefen`.
