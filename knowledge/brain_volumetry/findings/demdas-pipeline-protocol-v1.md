---
id: demdas-pipeline-protocol-v1
typ: regel
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: frozen pipeline protocol for the DEMDAS pilot and first full-cohort run, 13.10.2026 (Alita); PDF in the QC mirror
verweist_auf: [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort, chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg]
---

# DEMDAS structural pipeline, protocol v1 (frozen 2026-10-13)

Status: FROZEN for the pilot and the first full-cohort run. Every later change is protocol v2 and is compared against v1 on the pilot before it is used. Author: Mendel Temuulen with Claude (Alita). Internal; cohort-level numbers only.

## 1. Scope
586 participants of the DEMDAS BIDS export of 2026-10-11 (1616 sessions, visits M0/M6/M36/M60; 1652 T1w). First runs: participants with at least two sessions (464 participants, 1494 sessions), most sessions first; the 40 sessions with two T1 acquisitions first of all (same-session test-retest). Baseline-only participants (121 + 1 with a single non-baseline visit) are added later with the same protocol.

## 2. Inputs per session
- T1w MPRAGE 1 mm, distortion-corrected series (ImageType DIS3D; `run-2` where two runs exist, else the plain T1w). The same series type for ALL sessions of a participant; never mix with the ND series.
- FLAIR (`run-2` if present, else plain), DWI trace and ADC (scanner derivatives) for lesion masks and QC display.
- Integrity: `gzip -t` on every NIfTI after every copy; file count and byte sum against the source.

## 3. Processing steps and exact settings
| Step | Tool, version | Command / settings |
|---|---|---|
| S1 Tissue and structure volumes | FreeSurfer 8.2.0 `mri_synthseg` (SynthSeg 2) | `--parc --robust --vol --qc --cpu --threads 8`; no bias correction, no skull strip, no lesion filling before SynthSeg |
| S2 Acute infarct mask | DeepISLES isles22_ensemble | DWI + ADC + FLAIR of the session, mask in DWI space, FLIRT 6 dof normmi to T1, trilinear to the SynthSeg grid, threshold 0.5 |
| S3 Chronic infarct mask (v1.1, pending wd7) | union of earlier DeepISLES masks moved forward (dilated 1 voxel) + MAPPING (ATLAS R2.0 nnU-Net) on T1 | per session; "new infarct" flag when an own mask > 1 ml appears at a follow-up |
| S4 Volumes | gm_beispiel.py | RAW = SynthSeg labels; INFARCT EXCLUDED = RAW minus infarct voxels (acute now, chronic from v1.1); counting groups: cortex 1000-1035/2000-2035/3/42; subcortical 10-13,17,18,26,28,49-54,58,60; cerebellum GM 8,47; WM 2,41,7,46,16; CSF 4,5,14,15,24,43,44; ICV = SynthSeg total intracranial |
| S5 Cortical thickness | FreeSurfer 8.2.0 `recon-all -all -openmp 8` (cross-sectional) | T1 only in v1; mean thickness = vertex-weighted MeanThickness of lh/rh.aparc.stats; Desikan-Killiany regions ThickAvg |
| S6 QC gate | qc_gate.py | Euler number of lh/rh.orig.nofix via mris_euler_number (LD_LIBRARY_PATH systemlibs); cutoff = cohort Q1 - 1.5 IQR of the mean (pilot: -109.5); SynthSeg QC minimum, working threshold 0.65 until calibrated by ratings (wd8) |
| S7 Error statistics | fehler_statistik.py | within-SD, CV, ICC(2,1), SDC95 per structure from test-retest pairs; detectability = annual slope / SDC |
| S8 Display | gm_qc_axial.py v3 | follow-ups aligned to the first complete session (FLIRT 6 dof normmi, cached); series FLAIR/DWI/ADC/T1ND registered to the T1 grid with `-nosearch`; display only, volumes always native |
| S9 Tables | cohort_statistics.py | analysis_table.csv one row per session + codebook |

## 4. Rules
1. One FreeSurfer version for all sessions of the cohort (8.2.0; the HPC module is 8.1.0, so 8.2.0 is installed in the project before the full run).
2. Never interpret a single between-session difference; slopes from mixed models; a within-person change counts only beyond SDC95.
3. Exclude single bad time points, not participants; document every exclusion with reason (QC gate, rating).
4. Lesions: never masked-and-left-empty for FreeSurfer surfaces; filling of WM lesions before recon-all is a v2 candidate (pilot variants: baseline, filled, filled + FLAIRpial, SAMSEG) and enters v2 only if Euler number and SDC95 improve on the pilot.
5. Every QC page lists software with versions, atlases, build time, and links its methods page locally.
6. Output files, sheet and column names in English.

## 5. Open items that define v2
- Chronic infarct masks (wd7), rating-calibrated QC thresholds (wd8), lesion filling / FLAIRpial / SAMSEG decision from the HPC pilot, FreeSurfer longitudinal stream (wd5), longComBat across sites (wd9), segmentation benchmark (wd6).

## 6. References
Billot 2023 PNAS (SynthSeg) PMID 36802420; Fischl 2012 NeuroImage (FreeSurfer) PMID 22248573; Reuter 2012 (longitudinal) PMID 22430496; Vidal-Pineiro 2025 Imaging Neurosci DOI 10.1162/imag_a_00547; Rosen 2018 (Euler) PMID 29278774; Monereo-Sanchez 2021 PMID 34000406; Chard 2010 PMID 20575080; Battaglini 2012 PMID 21882300; Magon 2014 PMID 25200127; Ozzoude 2020 PMID 33381009; Beer 2020 (longComBat) PMID 32640273.

## Verknuepft
- [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort](freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort.md)
- [chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg](chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg.md)
