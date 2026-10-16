---
id: public-code-knows-no-dataset
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-16
herkunft: user rule for a public research repository, 2026-10-16 ("das muss data agnostisch sein")
verweist_auf: [python-env-isolation-on-shared-clusters]
---

# Public code knows no dataset; the rules of a dataset live next to the data

## Aussage
A public repository gets no file names it looks for by itself (`excluded.tsv`), no folder layouts, modality spellings,
cohort or drive names, and no configs of in-house data. It takes path patterns (`{id}` + glob) and files passed
explicitly (`--ids`, `--exclude`); a standard layout (BIDS) may be offered as a preset. Everything specific to one
dataset (which list excludes whom, which mask wins) is a small private script stored with the data.
Before moving logic out, prove that old and new give the same result: here the generic case-list builder reproduced
the layout-specific one row by row (ids, paths, folds, lesion counts) on two cohorts.

## Trägt
The same move fixed a real error: the layout-specific builder found the exclusion list only in one folder, a copy of
the data had it one level up, and a case with a misfitting reference mask entered the case list unnoticed.
Generic code with explicit files plus a loud warning for quality-flagged cases makes that visible.

## Trägt nicht
Aggregate validation numbers may still be reported (no patient data); it is the code that must not encode a dataset.

## Bruchindikator
`grep` of the public diff finds cohort, drive or layout names; a function opens a file it was not given.

## Ablesung
BIDS specification 1.9 (derivatives, `desc-` entities): https://bids-specification.readthedocs.io/ ; Gorgolewski et al.,
Sci Data 2016, doi:10.1038/sdata.2016.44, PMID 27326542. Equality check: own run 2026-10-16 (75 and 61 cases identical).

## Verknüpft
[python-env-isolation-on-shared-clusters](python-env-isolation-on-shared-clusters.md)
