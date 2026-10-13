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

## Verknüpft
- [demdas-qc-gate-euler-synthseg](demdas-qc-gate-euler-synthseg.md)
