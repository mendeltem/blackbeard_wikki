---
id: dataset-handover-one-folder-per-case-no-copies
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-16
herkunft: user requests on Alita 2026-10-16 while preparing an in-house microbleed data set for a master student who works with MicrobleedNet
verweist_auf: [readme-for-a-research-package, public-code-knows-no-dataset, release-test-means-fresh-machine-with-release-assets]
---

# Handing over a data set: one folder per case, the other tool's layout as siblings, no copies, a file table, a QC page

## Aussage
1. Raw scans stay in BIDS (`sub-X/anat/`); everything derived goes under `derivatives/`, with ONE folder per case
   (`derivatives/preprocessed/sub-X/`) and file names that say what they are (`_t2star` / `_swi`, `_brainmask`,
   `_cmb`, `_synthseg`, `_csf`, `_flair`), not `_image` / `_label`.
2. Every derived map lies on the matrix of the scan (SynthSeg, CSF mask, FLAIR), so any viewer overlays it directly.
3. If the recipient's tool expects its own layout, add it as sibling folders with that tool's names
   (`images/`, `frsts/`, variants as `images_inpainted/`), made with the tool's own code.
4. No duplicates: a folder that would only repeat another file (e.g. `labels/` = the manual masks) is not stored;
   a small script builds it where the recipient works.
5. `files.xlsx` with one row per case, one column per file, a second sheet that explains every column, and the
   source of each derived map (e.g. SynthSeg from FLAIR or from the scan).
6. A QC page over several axial slices per case with an overlay switch, built before the handover, and every
   transfer verified by checksums.

## Trägt
Each point came from a user correction on the same day ("ich will keine Redundanzen", "image should be t2_star",
"flair ist nicht preprocessed", "in derivatives drei Ordner"); the result was accepted.

## Trägt nicht
Data sets for public release follow the BIDS derivatives specification in full (dataset_description per pipeline).

## Bruchindikator
A recipient who needs a file that is only reachable through a second copy.

## Ablesung
BIDS: Gorgolewski KJ et al. Sci Data 2016;3:160044, doi:10.1038/sdata.2016.44, PMID 27326542; BIDS derivatives:
https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html. MicrobleedNet layout:
https://github.com/v-sundaresan/microbleed-detection (commit 958f1cb, `commands.py`).
