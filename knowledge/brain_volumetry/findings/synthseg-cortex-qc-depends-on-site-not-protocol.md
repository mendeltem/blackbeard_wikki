---
id: synthseg-cortex-qc-depends-on-site-not-protocol
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-17
herkunft: full-cohort automatic QC of a multi-centre longitudinal stroke cohort (raw-T1 SynthSeg), Alita session 2026-10-17
verweist_auf: [research-subcortical-segmentation-longitudinal-stroke-2026-10, longitudinal-volumetry-needs-error-statistics]
---

# SynthSeg's cortex QC score splits by site, not by protocol; subcortical scores are almost all fine

## Aussage
1. Per-structure gate (QC score >= 0.65 per structure, as in Billot et al. 2023): subcortical nuclei, white matter, CSF,
   cerebellum and brainstem were usable in 99.8-100 % of 1253 scored sessions; the cerebral cortex only in 57 %.
2. The cortex share differs by site from 18 % to 88 %, while the T1 protocol is identical everywhere (Siemens 3T MPRAGE,
   TR 2.5 s, TI 1.1 s, flip 7 deg, 1 mm isotropic). Scanner model explains part (one model/software version 41 %, another 72 %),
   but the SAME model at two sites gave 20 % vs 97 % and 30 % vs 57 %. Time point (baseline vs 6-60 months) did not matter (39-47 %).
3. The QC score is a predicted Dice; on the 24-case example, measured SynthSeg-vs-FreeSurfer grey-matter Dice was 0.80 while
   predicted scores were lower. A low cortex score means "inspect", not "wrong", until checked against visual verdicts.
4. Two silent pipeline gaps found by the full-cohort pass: the cohort volume table was empty (rebuild wrote -1 rows) and
   237 of 1490 sessions had no QC score.
5. Growth that atrophy cannot explain (> 5 % between consecutive sessions) appeared in ~4 % of follow-ups, mostly amygdala and
   caudate: a cheap longitudinal plausibility flag.

## Trägt
qc_all.csv and segmentations of the full cohort, T1w JSON sidecars (cohort-level counts only), 2026-10-17.

## Trägt nicht
No visual verdicts yet (blind rating page with 53 stratified cases prepared); site effects can also come from patient mix.

## Bruchindikator
Visual verdicts that pass most low-score cortex segmentations (then the 0.65 gate is too strict for this cohort).

## Ablesung
- Billot B et al. Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets.
  PNAS 2023;120(9):e2216399120. DOI 10.1073/pnas.2216399120, PMID 36802420. Shows: SynthSeg+ segments clinical scans of any
  quality, detects faulty segmentations itself and keeps per-region volumes only where the QC score is above 0.65 (full text, checked).
- Iglesias JE, FreeSurfer mailing list, 28.06.2025: "This QC scores represent the expected Dice of the segmentations"; example
  reject threshold 0.7. https://mail.nmr.mgh.harvard.edu/archives/list/freesurfer@nmr.mgh.harvard.edu/message/BVYB65YZKG44PK3FQZE23ZJ5GTJ3M5KQ/
- own scripts qc_full_cohort.py, site_protocols.py, site_model_qc.py (2026-10-17)
