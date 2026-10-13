---
id: demdas-full-cohort-sample-gm-page-2026-10-13
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: DEMDAS full cohort (586 participants), stratified sample, 2026-10-13
verweist_auf: [demdas-volumetry-primer-2026-10-13, one-t1-per-visit-and-tab-columns-by-cut]
---

# Full-cohort sample GM page: 12 participants x 4 sessions, SynthSeg only

## Aussage
First QC page from the **full** DEMDAS cohort (586 participants, 1616 sessions): 12 participants of the stratified sample, each with the maximum of 4 sessions (the full cohort has 231 participants with 4 sessions, 104 with 3, 129 with 2, 122 with 1; no participant has 5). Built with the same generator as the example page (`gm_qc_axial.py`), series T1 / T1 ND / FLAIR / DWI / ADC co-registered per session (FLIRT, 6 dof, `-nosearch`), counting groups, structures, hover definitions, "? Methods".

Deliberately absent: cortical thickness (no recon-all for these participants yet, planned on the HPC), infarct masks (not available for the full cohort), WMH volumes (user rule), and the PASS/FLAGGED gate row. The gate verdict was removed from **both** GM pages on 13.10.2026 at the user's request; the SynthSeg QC minimum and the Euler numbers stay as plain numbers. SynthSeg QC values are present for 15 of 48 sessions only, because `mri_synthseg` writes its `--qc` table per batch and the full-cohort batches of the remaining 33 sessions were not finished when the page was built; their volumes were derived from the label images instead (ICV = all non-zero labels).

Build cost: table step 37 min (48 sessions, per-label counting), 3 image workers 41 min, page 228 MB on the stick; registrations and resampled series (800 MB) stay local.

## Trägt
- Mirror check `qc_mirror_check.py` OK for build, mirror and stick (48 sessions).
- Page header "12 participants with >= 2 complete sessions (48 sessions), built 2026-10-13 18:35".

## Trägt nicht
- No thickness, no test-retest statistics for the sample yet (needs recon-all).

## Bruchindikator
- A rebuilt page after the SynthSeg batches finish must show 48 QC values; if it still shows 15, the batch tables were not merged.

## Ablesung
- `~/QUALITY_CONTROLL/DEMDAS/gm_sample_qc/index.html`, stick QWEN/QUALITY_CONTROLL/DEMDAS/gm_sample_qc (own data).
- SynthSeg QC predictor: Billot B. et al., "Robust machine learning segmentation for large-scale analytical lifespan studies", PNAS 2023, doi:10.1073/pnas.2216399120 (QC scores = predicted Dice per structure).

## Verknüpft
- [demdas-volumetry-primer-2026-10-13](demdas-volumetry-primer-2026-10-13.md)
