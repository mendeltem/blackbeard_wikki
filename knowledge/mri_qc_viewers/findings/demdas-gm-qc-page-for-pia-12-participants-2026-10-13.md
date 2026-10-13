---
id: demdas-gm-qc-page-for-pia-12-participants-2026-10-13
typ: befund
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-13
herkunft: DEMDAS example set (24 participants), compact GM QC page built 2026-10-13 18:46
verweist_auf: [demdas-full-cohort-sample-gm-page-2026-10-13, demdas-qc-gate-euler-synthseg]
---

# Compact GM QC page for the clinical reviewer: 12 participants, 41 sessions, complete data only

## Aussage
User request 2026-10-13: a QC page for the clinical reviewer (Pia) with 12 participants, as complete as possible, many
sessions (4 where they exist, also participants with 2), and not too much information. Built from the example set, because
only there every session has SynthSeg + recon-all thickness (FreeSurfer 8.2.0) + infarct mask + all five series:
8 participants with 4 to 5 visits and 4 participants with 2 visits = 41 sessions (40 of 41 with all four extra series).

The generator `gm_qc_axial.py` got two options: `--kompakt` (no per-structure table of ~100 SynthSeg labels, no disabled
"REMOVED BEFORE" button, narrower right column with the five counted groups only) and `--titel`. The page keeps: one axial
image per session with series switch, overlays (segmentation / counted / infarct), session buttons M0..M60, totals, the
across-session table coloured by SDC95, cortical thickness, SynthSeg QC and Euler numbers as plain numbers (no verdict),
hover definitions and "? Methods". Sprites were hard-linked from the example-page cache (`--nur-seite`), so the build took
seconds instead of a 40-minute render; page 238 MB.

## Trägt
- `qc_mirror_check.py` OK for build, local mirror and stick (41 sessions); `node --check` of the page script OK.
- Index entry at the top of the DEMDAS section in `QUALITY_CONTROLL/index.html` (local and stick).

## Trägt nicht
- Not reviewed by the reader yet; what "too much information" means for her is still to be learned from feedback.

## Bruchindikator
- A rebuild without `--kompakt` silently brings the structure table back; the index text would then be wrong.

## Ablesung
- `~/QUALITY_CONTROLL/DEMDAS/gm_pia_qc/index.html`, stick QWEN/QUALITY_CONTROLL/DEMDAS/gm_pia_qc (own data).
- Build dir `~/data/derivatives/demdas/gm_beispiel/qc_pia`; generator `~/data/work/demdas-gm/gm_qc_axial.py` (backup `.vor-1013-pia`).

## Nachtrag 2026-10-13: "removed before" and the literature behind before/after
"Removed before" exists only as variant B of the A/B/C comparison (WMH filled with FSL lesion_filling before SynthSeg,
22 baseline sessions, `derivatives/demdas/abc`): GM changes by <= 0.5 % (max 3.1 ml at 63 ml WMH, sub-PDDISDLFN51T12).
Infarct filling before segmentation was never computed; the page button "REMOVED BEFORE" is hidden in the compact view.
Literature (PubMed, 13.10.2026): for MS white-matter lesions, filling BEFORE intensity-based segmentation is recommended
and masking afterwards does not remove the border misclassification (Chard 2010 doi:10.1002/jmri.22214; Battaglini 2012
doi:10.1002/hbm.21344; Gelineau-Morel 2012 doi:10.1002/hbm.21402; Popescu 2014 doi:10.1016/j.nicl.2014.01.004; Valverde
2014 doi:10.1016/j.nicl.2014.08.016; Magon 2014 doi:10.1186/1471-2202-15-106 for cortical thickness). For infarcts no
filling literature exists; stroke cortical-thickness work excludes infarcted vertices AFTER reconstruction with a lesion
mask (Khlif 2022 doi:10.1016/j.nicl.2022.103200; Li 2015 doi:10.1016/j.nicl.2014.08.017), registration work masks the
lesion out of the cost function (Brett 2001 doi:10.1006/nimg.2001.0845; Nachev 2008 doi:10.1016/j.neuroimage.2007.10.002).
Conclusion unchanged: SynthSeg on the unfilled T1, infarct removed after; the reviewer note carries the reference list.

## Verknüpft
- [demdas-qc-gate-euler-synthseg](demdas-qc-gate-euler-synthseg.md)
