---
id: demdas-volumetry-primer-2026-10-13
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: primer v3 (15:45) for the presentation of the DEMDAS volumetry work (Alita, 13.10.2026); PDF next to this file
verweist_auf: [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort, synthseg-in-freesurfer-8-runs-on-cpu-only, cohort-copies-need-a-gzip-sweep, longitudinal-volumetry-needs-error-statistics]
---

# Primer: DEMDAS brain volumetry and cortical thickness: a primer for presenting the work (v3)

Version 3, built 2026-10-13 15:45 on workstation Alita (v1 11:10, v2 14:00) (Ubuntu 24.04, FreeSurfer 8.2.0). Author: Mendel Temuulen with Claude (Alita session). Internal document: the cohort contains patient data; this primer reports cohort-level numbers only, no identifiers.

**How to use it.** Sections 1 to 4 are what you must be able to explain without notes (data, pipeline, measures, why FreeSurfer). Sections 5 to 7 are the numbers from the pilot and how to read them. Sections 8 to 10 are the plan for the full cohort and the answers to the questions you will be asked. Every claim from the literature carries a reference number; the list at the end has DOI and PMID. Everything measured here names the script and date.

---

## 1. The cohort and the data

**DEMDAS** (DZNE Mechanisms of Dementia After Stroke) is a multi-centre longitudinal stroke cohort. The imaging set we hold:

| Item | Value (BIDS export of 2026-10-11) |
|---|---|
| Participants | 586 |
| Sessions | 1616 (M0 571, M6 436, M36 320, M60 289) |
| Sites (prefix in the ID) | ISD 218, BON 102, GOE 77, TUM 62, MAG 57, BER 37, BBF 33 |
| T1-weighted MPRAGE, 1 mm isotropic, Siemens 3T | 1652 files; all distortion-corrected (DIS3D in ImageType); 40 sessions have two T1 acquisitions (run-1, run-2) |
| Other series | FLAIR (most sessions), DWI with ADC and trace maps (scanner derivatives), T2w / T2*w in some sites |
| Participants with 1 / 2 / 3 / 4 sessions | 122 / 129 / 104 / 231 (121 have baseline only) |

**Rule since 2026-10-13:** participants with only one session (122, of which 121 baseline-only) are excluded from the first full-cohort runs and from the QC viewer; participants with the most sessions are processed first. They can be added later with one switch.

A **pilot subset** of 24 participants (65 sessions, 23 with usable SynthSeg output, 61 with finished recon-all as of 2026-10-13 10:00) carries all methods development. Its BIDS copy also holds the uncorrected ("ND") MPRAGE next to the distortion-corrected series for 62 sessions; this pair is used for the test-retest in section 5.

**Data integrity lesson.** One pilot T1 was a truncated copy (508 KB instead of 5.2 MB) for five weeks; SynthSeg failed silently and the session simply vanished from the QC page. Rule since 2026-10-12: after every copy run `gzip -t` over every NIfTI and compare file counts and byte sums with the source (886 files, under two minutes). Also, `du` on exFAT drives overstates sizes by 50 % (cluster size).

---

## 2. What we measure and why

1. **Tissue and structure volumes** per session: total grey matter (cortex + subcortical + cerebellum), cortex, subcortical GM, white matter, CSF and ventricles, plus nine focus structures (hippocampus, amygdala, entorhinal and parahippocampal cortex, thalamus, caudate, putamen, pallidum, accumbens, ventral diencephalon), left and right, in ml and in % of intracranial volume (ICV).
2. **Cortical thickness** per session: mean thickness per hemisphere and 34 Desikan-Killiany regions per hemisphere, in mm, from FreeSurfer surfaces.
3. **Lesions**: acute/chronic infarct masks (DeepISLES on DWI at M0; MAPPING on T1 for follow-ups) and white-matter hyperintensity (WMH) volume from an in-house 3D U-Net. Infarcts are **excluded** from the tissue classes after segmentation (variant C, user decision 2026-10-10/11); WMH is reported as its own quantity and no longer shown on the GM QC page (user decision 2026-10-13).
4. **Change over time**: slopes per participant and mixed-model slopes per structure, in % per year, and the question whether a change in one person is larger than the measurement error (detectability).

Why these: post-stroke cognitive decline is tied to atrophy of hippocampus, thalamus and cortex, to ventricular enlargement and to WMH growth; the imaging task is to measure those reliably in the presence of infarcts.

---

## 3. The pipeline as built (pilot, 2026-10-13)

| Step | Tool, version | Settings | Script |
|---|---|---|---|
| Conversion | dcm2niix v1.0.20260724 | BIDS, ImageType kept in JSON | HPC project SEGMENTATION_PROJECT |
| Tissue segmentation | FreeSurfer 8.2.0 `mri_synthseg` (SynthSeg 2, build 20260314) | `--parc --robust --cpu --threads 6`, on the distortion-corrected T1, no bias correction, no filling | demdas-gm/gm_beispiel.py |
| Infarct mask on the SynthSeg grid | DeepISLES (DWI, M0), MAPPING (ATLAS R2.0 nnU-Net v1, T1, all sessions) | nearest-neighbour resampling, infarct voxels removed from GM/WM/CSF totals ("INFARCT EXCLUDED") | gm_beispiel.py, demdas-infarkt/ |
| WMH | in-house 3D U-Net (architecture a12, 5-fold ensemble of the 311-case model) | reported in ml, not filled | derivatives/demdas/wmh-final |
| Cortical thickness | FreeSurfer 8.2.0 `recon-all -all` (cross-sectional) | `-openmp 4`, 3 runs in parallel, 40-48 min per session, peak RAM 17-28 GB per run | recon_alle.sh, recon_alle_v2.sh |
| Display alignment (QC only) | FSL FLIRT 6 dof, normmi | follow-ups shown on the M0 grid, Dice of brain masks 0.98-0.99; volumes come from native space | gm_qc_axial.py |
| Tables and pages | Python 3.12 (numpy, nibabel, scipy, pandas, PIL) | English keys, software block on every page | verlauf_statistik.py, fehler_statistik.py, thickness_table.py, qc_gate.py |

Two choices to defend: (a) **the distortion-corrected series** is the pipeline input for all time points, never mixed with the uncorrected one, because a change of series would look like atrophy; (b) **no WMH filling before SynthSeg**: measured on 22 M0 sessions, filling changed GM by at most 0.5 %, whereas excluding infarct voxels changed regional GM by up to 8 % (2026-10-11). This holds for SynthSeg; for FreeSurfer surfaces the literature says filling matters (section 8).

---

## 4. Method background you must be able to explain

**SynthSeg** [5] is a 3D U-Net trained only on synthetic images generated from label maps with random contrast, resolution and artefacts, so it segments any MRI contrast without retraining. `--robust` uses a two-step network for clinical-quality scans; `--parc` adds the Desikan-Killiany cortical parcellation; the QC score per structure is the network's own agreement estimate (0 to 1). It runs on the CPU inside FreeSurfer 8.2 (the bundled TensorFlow has no GPU build): 85-99 s per 1 mm image, peak RSS 19.2 GB per process (measured 2026-10-13).

**FreeSurfer recon-all** [1,2] builds surfaces: intensity normalisation, skull strip, white-matter segmentation, tessellation of the WM surface, topology correction, deformation to the white and pial surfaces, inflation, spherical registration to an atlas, parcellation. **Cortical thickness** is the distance between the white and pial surfaces at each vertex, averaged per region. The **Euler number** of the initial surface (`?h.orig.nofix`) counts topological defects: 2 - 2 × holes; more negative means more defects and is the best automated predictor of a bad segmentation [15,16]. FreeSurfer 8 replaced several classical steps by deep-learning modules (SynthSeg, SynthMorph, SynthStrip), which is why a run takes 45 minutes instead of 4-7 hours but needs 17-28 GB of RAM.

**Longitudinal stream** [3]: for each participant a within-subject template ("base") is built from all time points and each time point ("long") is then initialised from that template, so that processing is unbiased with respect to time point and random variation across time points shrinks. In 11 datasets the cross-sectional stream was about 0.25 ICC lower for change than the long stream [7].

**Lesion filling** [10-12] replaces lesion voxels in the T1 with white-matter-like intensities before segmentation so that WM lesions are not labelled grey matter or CSF; masking alone does not remove the bias [11]. For cortical or cavitary infarcts filling with WM intensity is wrong; inpainting (FastSurfer-LIT [14]) or masking is used there.

**Measurement error** (section 5): within-subject SD from paired measurements, ICC(2,1) for absolute agreement, and the smallest detectable change SDC95 = 1.96 × √2 × SD_within, the change that exceeds measurement noise in a single person with 95 % confidence.

**ComBat / longComBat** [21-23]: empirical-Bayes location-scale harmonisation of ROI tables across scanners, protecting covariates of interest; the longitudinal variant models subject-specific intercepts.

---

## 5. Pilot results: measurement error (fehler_statistik.py, built 2026-10-13 10:13)

Test-retest proxy: SynthSeg on the uncorrected versus the distortion-corrected MPRAGE of the same session (61 pairs; this is an upper bound of the segmentation error because the two series also differ by the distortion correction). An exact rerun with the pipeline settings on the ND series is queued (task wd2).

| Structure | mean ml | CV % | ICC(2,1) | SDC95 ml | SDC95 % |
|---|---|---|---|---|---|
| Hippocampus L / R | 3.80 / 3.87 | 0.94 / 0.88 | 0.998 / 0.997 | 0.10 / 0.09 | 2.6 / 2.4 |
| Amygdala L / R | 1.71 / 1.76 | 0.57 / 0.56 | 0.999 / 0.999 | 0.03 / 0.03 | 1.6 / 1.6 |
| Thalamus L / R | 6.27 / 6.05 | 1.37 / 1.89 | 0.992 / 0.984 | 0.24 / 0.32 | 3.8 / 5.2 |
| Caudate L+R | 7.75 | 1.42 | 0.990 | 0.31 | 3.9 |
| Putamen L+R | 9.81 | 0.72 | 0.998 | 0.20 | 2.0 |
| Grey matter total | | | | | 1.9 |
| Cerebral cortex | | | | | 2.4 |
| White matter | | | | | 2.5 |
| Lateral ventricles | | | | | 2.9 |

Reading: a hippocampal change in one person is only interpretable if it exceeds about 2.5 %; the thalamus needs 4-5 %. With the QC-passed subset (35 pairs) the thalamus SDC drops to 2-3 %, i.e. part of its noise is segmentation failure, not biology.

**Detectability** (annual change from the mixed model divided into the SDC): lateral ventricles grow 5.5 % per year (CI 4.0-7.0) and exceed their SDC within about 6 months; subcortical GM loses 0.7 % per year (CI 0.5-1.0), about 3 years to exceed the SDC; total GM and cortex change by less than 0.1 % per year in this pilot, so a single person's cortical change is not detectable with SynthSeg volumes over the study span. This is the quantitative reason for measuring cortical thickness with surfaces and for the longitudinal stream.

**Longitudinal noise**: residual SD around each participant's line is 1-3 % for hippocampus, amygdala and thalamus (12 participants with 3 or more sessions); 2 of 15 M0-to-M6 hippocampus-left changes fall outside ±30 %, which flags segmentation or mask errors, not atrophy (section 9).

---

## 6. Pilot results: trajectories (verlauf_statistik.py) and cortical thickness

Mixed model (volume in % ICV ~ years + random intercept per participant, 23 participants, 63 sessions, RAW version):

| Structure | slope % per year | 95 % CI | p |
|---|---|---|---|
| Hippocampus L / R | -1.22 / -0.65 | | 0.010 / <0.001 |
| Amygdala L / R | -1.14 / -0.91 | | <0.001 / <0.001 |
| Thalamus L / R | -1.61 / -0.79 | | <0.001 / <0.001 |
| Putamen | -0.84 | | <0.001 |
| Ventral diencephalon | -0.85 | | <0.001 |
| Caudate | -0.39 | | 0.075 |
| Lateral ventricles | +5.5 | 4.0 to 7.0 | <0.001 |

Side comparison (14 participants with a lateralised M0 infarct): thalamus ipsilateral to the infarct loses 2.2 % per year versus 0.6 % contralateral (Wilcoxon p = 0.009), robust to infarct exclusion (p = 0.011); hippocampus and amygdala show no significant side difference. Caveats to state: cross-sectional segmentation per session, small n per time point, no multiple-testing correction, follow-up infarct masks pending.

**Cortical thickness** (FreeSurfer 8.2 cross-sectional, 61 sessions, 23 participants, thickness_table.py 2026-10-13, corrected 11:40: the hemisphere mean is FreeSurfer's vertex-weighted MeanThickness, the first build had used the unweighted mean of the 34 regions, 0.04 mm too high): median mean thickness 2.34 mm (range about 2.15-2.56), typical for age 60-80; per-participant slopes (17 participants with ≥ 2 sessions ≥ 6 months apart) median -0.17 % per year (IQR -0.51 to +0.32), i.e. within noise, as expected without the longitudinal stream [7].

---

## 7. Quality control: pages, gate and known artefacts

**Pages** (mirror ~/QUALITY_CONTROLL/DEMDAS, copied to the stick; every page English, every number with a hover explanation, a "? Methods" overlay and a software block):
- `gm_beispiel_qc/index.html` (v3, rebuilt 2026-10-13): only participants with at least two COMPLETE sessions (SynthSeg + recon-all thickness + infarct mask), most sessions first (16 participants, 53 sessions; excluded ones listed with reason). One axial image per session, sessions switched in the same window. Image series switch (keys 1-5): T1 corrected, T1 ND, FLAIR, DWI, ADC, all rigidly registered onto one display grid. Lesion handling: NOT REMOVED / REMOVED BEFORE (filled T1, pending) / REMOVED AFTER. Overlays: none, segmentation, COUNTED (each voxel coloured by the counting group it was summed into, legend with the FreeSurfer label IDs), infarct. Lesion panel (volume, side, components, slice range, 'go to lesion') and magenta marks under the slider at every infarct slice. Across-session table with ICV, coloured only where a change exceeds the structure's SDC95. Counting panel (key C) with ml per group. No WMH anywhere on the page. Methods overlay with atlases, software versions, local methods HTML + PDF, primer.
- `cohort_statistics/index.html` (new 2026-10-13): 586 participants, sessions per participant and visit, single-session participants per site, intervals between visits, series availability, scanners, processing status, infarct size classes (small < 5 ml, medium 5-30 ml, large > 30 ml, plus tertiles) and side, WMH distribution, volumes and thickness per visit, and `analysis_table.csv` (one row per session, 1616 rows) with a codebook.
- `volumenverlauf/verlauf.html` and `error_statistics.html`: trajectories, test-retest, detectability, failures, QC gate.
- `cortical_thickness/index.html`: thickness per region and session with the cohort band.

**QC gate** (qc_gate.py, 2026-10-13): Euler number per hemisphere from `mris_euler_number`, mean per session; cohort cutoff Q1 - 1.5 × IQR = -107.75; pilot median -51 (range -108 to -15); 1 of 55 finished sessions flagged. SynthSeg QC minimum over structures: median 0.674, 5th percentile 0.555; a 0.65 threshold flags 28 of 64 sessions, so 0.65 is too strict for this cohort and must be recalibrated (proposal: cohort 5th percentile, or visual grading of the 10 lowest).

**Visual review of all 17 multi-session participants (13.10., review sheets in `gm_beispiel_qc/review/`):** alignment between sessions Dice 0.982-0.990 in all 55 sessions; FLAIR, DWI and ADC registered correctly everywhere; ICV drift within participants at most 1.7 %; SynthSeg plausible across visits, also with confluent WMH and enlarged ventricles; acute infarcts at M0 sit exactly under the DWI mask (0.4 ml pons to 110 ml MCA territory). Systematic finding: the acute (DWI) mask is empty at follow-ups in 12 of 17 participants, SynthSeg gives the chronic cavity label 0 (dropped from all totals and from ICV) and counts gliosis as WM or cortex, so INFARCT EXCLUDED is complete only at M0 until the chronic mask (task wd7) exists. One participant has a new 7 ml infarct at an unscheduled 10-month visit. Minor: one 0.02 ml mask speck outside the brain; one noisy single-file DWI without mask.

**Euler-number error, fixed 13.10.:** six finished sessions had reported Euler 2 because `mris_euler_number` failed on a missing ITK library and the log fallback read the post-fix value; with the library path set, all 61 sessions have proper values (cohort cutoff -109.5, no Euler flag, 23 of 55 SynthSeg-QC flags at the uncalibrated 0.65).

**Known artefact, fixed 2026-10-12**: a page showed a coloured strip at the top of every image; it was not a segmentation error but a tile offset, because index.html had been copied after a rebuild while the JPEG mosaics were from an older build with a different tile height. Rule: copy whole page folders, and run qc_mirror_check.py (sprite size against tile layout, build vs mirror vs stick).

---

## 8. Why FreeSurfer as the main tool, and how to improve from here (literature, PMID-verified 2026-10-13)

Ordered by expected gain for this cohort:

1. **Longitudinal stream** for the 465 participants with follow-up; baseline-only participants as one-time-point bases so processing is identical. Evidence: +0.25 ICC for change versus cross-sectional [7]; the 0-6-month contrast is noise, rates come from 0/36/60 months [7].
2. **Lesion handling before recon-all**: fill WM lesions (WMH + WM infarcts) with FSL lesion_filling [10-12]; cortical / cavitary infarcts by inpainting (FastSurfer-LIT [14], not yet validated on infarcts) or masking; always exclude lesion-overlapping vertices and voxels from ROI statistics. In chronic stroke / SVD a lesion-aware FreeSurfer procedure cut tissue-segmentation failures from 62 % to 8 % [13].
3. **FLAIR-assisted pial surface** (`-FLAIRpial`): plausible, no quantitative study found; test on 30-40 sessions against Euler number, edit need and SDC95.
4. **QC gate per session**: Euler number per site [15,16], MRIQC [18], recalibrated Qoala-T [17]; motion proxy as covariate (motion lowers GM and thickness by about 0.7 % per mm/min [20]).
5. **Local test-retest** from the 40 same-session repeat T1 pairs: the cohort's own SDC95 per ROI, used as the threshold for implausible within-subject jumps.
6. **longComBat** on the ROI tables across the 7 sites, protecting age, sex, group and lesion load [21,23].
7. **SynthSeg only as comparator and fallback** for large tissue volumes: 3.1 % traveling-subject variation on average, up to 15-20 %, amygdala and ventral DC 7-8 %, systematic hippocampal offset [8]; no independent evidence that it is more site-robust than FreeSurfer on 1 mm MPRAGE.

A **benchmark** on the pilot plus the 40 repeat pairs (task wd6, running) compares SynthSeg robust, SynthSeg fast, FastSurfer CNN, FreeSurfer aseg and FSL FAST/FIRST on ICC, SDC95, Dice against FreeSurfer, infarct robustness, failure rate and runtime; the decision follows the table.

---

## 9. Segmentation errors across time points (M0, M10, M60): detect and handle

**Detect.** Per time point: Euler number (per-site threshold), MRIQC, recalibrated Qoala-T [15-18]; a time point whose Euler number drops far below the participant's other time points is suspect even if the cohort rule passes. Within participant: fit a robust line per ROI and flag residuals above the local SDC95; flag non-monotonic jumps in structures that only shrink; flag sudden left-right asymmetry changes; check that ICV is constant within participant (drift = skull strip or registration error). Visual QC of all flagged sessions, a random 10 % of the rest stratified by site and visit, and the lesion-heaviest decile.

**Handle, in this order.** (1) Rerun with lesion-filled T1 and, where the FLAIR is good, -FLAIRpial [13]. (2) The longitudinal stream reduces time-point-specific errors because each time point starts from the template [3,7], but it cannot repair an error that is in the template: fix or exclude a bad time point BEFORE building the base. (3) Manual edits (brainmask, wm.mgz, control points, pial) only for flagged cases, one editor, documented, applied to the cross-sectional run and then base and long rebuilt; edits had large effects on subcortical volumes in the Maastricht Study [16]. (4) Exclude single time points, not participants; mixed models tolerate missing visits. (5) Report with and without flagged data, with a per-time-point QC covariate, and a sensitivity analysis because failures concentrate in the sickest [13]. Expect more than 10 % first-pass failures in this population (ONDRI unmodified: 11 % ribbon and 62 % tissue fails [13]).

---

## 10. Plan for the full cohort and the compute budget

Measured on Alita (24 cores, 62 GB RAM, RTX 24 GB): recon-all 8.2 cross-sectional 40-48 min per session with 3 in parallel (RAM-limited, 17-28 GB each); SynthSeg robust 85-99 s per image and 19.2 GB per process (2 in parallel at most; 3 caused seven out-of-memory kills in the night of 12/13 October).

**HPC inventory (Charité sc-projects, measured 2026-10-13; scripts in `demdas-gm/hpc/` and on the stick `HPC_SCRIPTS/`):** compute partition 43 nodes with 64-192 EPYC cores and 0.5-1 TB RAM, 2-day walltime, user limit 900 CPUs, arrays up to 10000 jobs; gpu partition 27 A100 (40/80 GB) and L40S, pgpu with H100/H200; modules FreeSurfer 7.4.1 and 8.1.0, FSL 6.0.7.18, Apptainer; conda env GM_SEGMENTATION (Python 3.11, torch cu126) in the project; project storage 16 TB with 6.6 TB free. Measured on one DEMDAS session in a job: SynthSeg robust 50 s and 19.9 GB with 8 threads; SAMSEG T1+FLAIR with lesion model 7 min and 11.1 GB. Open point: the HPC has FreeSurfer 8.1.0, the pilot used 8.2.0; one version must be used for all sessions (install 8.2.0 in the project, README_HPC.md step 0). GPU nodes: A100 40 GB, driver CUDA 12.7, so torch must be a cu126 build (env GM_SEGMENTATION). Job preamble that works: source miniforge conda, activate GM_SEGMENTATION, module load freesurfer fsl. Ready: session-list builder (repeat pairs first, single-session participants excluded), SLURM arrays for SynthSeg (8 CPU, 24 GB, 15 min), recon-all in four variants (base, FLAIRpial, filled, filled + FLAIRpial; 8 CPU, 32 GB, 4 h), SAMSEG (8 CPU, 16 GB, 30 min), lesion filling, and a collector for the result tables. Pilot plan: 24 participants in the four recon-all variants plus SAMSEG, judged on Euler number, SDC95 from the repeat pairs and visual rating, then the full run.

| Step | Sessions | Alita alone | With the HPC (SLURM, GPU nodes; project path SEGMENTATION_PROJECT) |
|---|---|---|---|
| SynthSeg robust, multi-session participants (1528 T1) | 1528 | about 40 h with 1 process, running since 2026-10-13 10:36 | about 1 h as an array job (50 s per session measured) |
| recon-all cross-sectional | 1616 | about 23 days | 1-2 days with 50 parallel jobs |
| base + long | 465 participants, 1495 time points | not feasible locally | a few days |
| FastSurfer CNN (GPU) comparator | 1652 | about 1 day | hours |

Decision rules: (1) the full-cohort SynthSeg run gives all volumes and QC scores first; (2) recon-all and the longitudinal stream go to the HPC; Alita keeps pilot, benchmark and QC; (3) the pilot variants (baseline, lesion-filled, lesion-filled + FLAIRpial, LIT for cavities) are judged on Euler number, edit need, SDC95 on the repeat pairs and a visual grade before the full run; (4) nothing is mixed across tools within one model.

---

## 10b. Status on 2026-10-13 evening and the next steps (v3)

Frozen: pipeline protocol v1 (`primer/DEMDAS_pipeline_protocol_v1.pdf`). Running: SynthSeg over the multi-session participants of the full cohort (repeat-acquisition sessions first). Delivered today: GM viewer v3 (17 participants, 55 sessions, series switch, counted groups, lesion panel, no WMH), cohort statistics page with analysis table and codebook, corrected thickness page, review sheets, three-case page for the discussion (`pia_cases/`), HPC environment and scripts, derivatives backup on the SSD.

Queued for Clara, each with acceptance test: wd7 chronic infarct masks and the "new infarct" flag; wd8 rating widget and rating-calibrated QC thresholds; wd9 mixed-model analysis script (five variants, ipsi/contra, detectability, optional longComBat) that runs unchanged on the full cohort; wd6 segmentation benchmark (SynthSeg robust/fast, FastSurfer, FreeSurfer aseg, FSL) in progress; wd5 longitudinal stream after the cross-sectional runs.

Decisions still open, in this order: (1) FreeSurfer 8.2.0 in the HPC project; (2) lesion-handling variant from the HPC pilot; (3) QC thresholds from the ratings; (4) longitudinal stream yes/no from the pilot comparison; (5) longComBat across the seven sites.

## 11. Presenting it: storyline and expected questions

Suggested 10 slides: (1) question and cohort; (2) data: sites, visits, series, integrity check; (3) pipeline diagram with versions; (4) one QC page screenshot, explain RAW / INFARCT EXCLUDED and the counted groups; (5) measurement error table and what SDC95 means for one person; (6) trajectories: ventricles, thalamus, hippocampus, ipsilateral thalamus; (7) cortical thickness status; (8) QC gate and error handling across time points; (9) why FreeSurfer, the ordered improvement plan with references; (10) full-cohort plan and compute.

Questions you will get, with the answer in one or two sentences:
- *Why SynthSeg for volumes if FreeSurfer is the main tool?* It is contrast-robust and 1-2 minutes per image, so it gives the complete volume table and a QC score for all 1652 images first; FreeSurfer surfaces are the primary tool for thickness and for the longitudinal stream; small structures are never mixed across tools [5,8].
- *Why not fill WMH?* For SynthSeg volumes, filling changed GM by at most 0.5 % in our 22 M0 sessions; for FreeSurfer surfaces the literature says fill, so the FreeSurfer runs will use filled T1 after the pilot [10-13].
- *How do you know a change is real?* It must exceed the SDC95 of that structure (2.5 % hippocampus, 4-5 % thalamus here) and survive the QC gate; cohort slopes come from mixed models, not from single differences.
- *Is 0 to 6 months useful?* For atrophy no: at 2 years the ICC of change is 0.24 in healthy adults [7]; 6 months is a reliability estimate and a check on acute-phase effects.
- *What about seven scanners?* Same vendor and sequence family; longComBat on the tables after QC, with site as random effect in a sensitivity analysis [21,23].
- *How many will fail?* Expect over 10 % first-pass failures; the gate, lesion filling and reruns are planned for that [13,16].
- *Your follow-up volumes ignore the old infarct?* Yes, today: the DWI mask is acute-only; the chronic mask (carried forward + MAPPING on T1) is being built, and SynthSeg already drops cavities from the totals, so the remaining bias is the gliotic rim counted as tissue.
- *Why these reliability numbers if the segmentation is "deep learning"?* Deep learning changes the error pattern, not the need to measure it; our test-retest is an upper bound and the exact rerun is queued.

---

## 12. Glossary

ICV / eTIV: intracranial volume (SynthSeg "total intracranial"; FreeSurfer estimated total intracranial volume). SDC95: smallest detectable change at 95 % confidence for one person. ICC(2,1): intraclass correlation, two-way random, absolute agreement, single measure. CV: coefficient of variation = within-subject SD / mean. Euler number: 2 - 2 × (number of holes) of the initial cortical surface; -50 is typical, below the cohort cutoff is suspect. RAW / INFARCT EXCLUDED: volumes before / after removing infarct voxels. Base / long: FreeSurfer longitudinal template and time-point runs. Desikan-Killiany: 34-region cortical atlas per hemisphere (labels 1000-1035 left, 2000-2035 right).

---

## 13. References

Software: FreeSurfer 8.2.0 (build 20260314-d932c45); SynthSeg 2 as shipped in FreeSurfer 8.2; FSL (FLIRT, lesion_filling, FAST, FIRST); FastSurfer 2.x (GitHub Deep-MI/FastSurfer, checkpoints aparc_vinn v2.0.0, CerebNet v1.0.0, HypVINN v1.1.0); DeepISLES; MAPPING (ATLAS R2.0, nnU-Net v1); in-house WMH 3D U-Net a12; dcm2niix v1.0.20260724; Python 3.12 with numpy, nibabel, scipy, pandas, PIL.

1. Fischl B et al. 2002. Whole brain segmentation: automated labeling of neuroanatomical structures in the human brain. Neuron 33:341-355. DOI 10.1016/S0896-6273(02)00569-X. PMID 11832223.
2. Fischl B. 2012. FreeSurfer. NeuroImage 62:774-781. DOI 10.1016/j.neuroimage.2012.01.021. PMID 22248573.
3. Reuter M et al. 2012. Within-subject template estimation for unbiased longitudinal image analysis. NeuroImage 61:1402-1418. DOI 10.1016/j.neuroimage.2012.02.084. PMID 22430496.
4. Henschel L et al. 2020. FastSurfer: a fast and accurate deep learning based neuroimaging pipeline. NeuroImage 219:117012. DOI 10.1016/j.neuroimage.2020.117012. PMID 32526386.
5. Billot B et al. 2023. Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. PNAS 120:e2216399120. DOI 10.1073/pnas.2216399120. PMID 36802420.
6. Cerri S et al. 2021. A contrast-adaptive method for simultaneous whole-brain and lesion segmentation in multiple sclerosis. NeuroImage 225:117471. DOI 10.1016/j.neuroimage.2020.117471. PMID 33099007.
7. Vidal-Pineiro D et al. 2025. Reliability of structural brain change in cognitively healthy adult samples. Imaging Neuroscience 3:imag_a_00547. DOI 10.1162/imag_a_00547. PMCID PMC12319936.
8. Kondrateva E et al. 2025. Benchmarking the reproducibility of brain MRI segmentation across scanners and time. arXiv:2504.15931 (preprint, unverified).
9. DZNE software record, FastSurfer v2.4.2. https://pub.dzne.de/record/277720 (unverified).
10. Chard DT et al. 2010. Reducing the impact of white matter lesions on automated measures of brain gray and white matter volumes. J Magn Reson Imaging 32:223-228. DOI 10.1002/jmri.22214. PMID 20575080.
11. Battaglini M et al. 2012. Evaluating and reducing the impact of white matter lesions on brain volume measurements. Hum Brain Mapp 33:2062-2071. DOI 10.1002/hbm.21344. PMID 21882300.
12. Magon S et al. 2014. White matter lesion filling improves the accuracy of cortical thickness measurements in multiple sclerosis patients: a longitudinal study. BMC Neurosci 15:106. DOI 10.1186/1471-2202-15-106. PMID 25200127.
13. Ozzoude M et al. 2020. Cortical thickness estimation in individuals with cerebral small vessel disease, focal atrophy, and chronic stroke lesions. Front Neurosci 14:598868. DOI 10.3389/fnins.2020.598868. PMID 33381009.
14. Pollak C et al. 2025. FastSurfer-LIT: lesion inpainting tool for whole-brain MRI segmentation with tumors, cavities, and abnormalities. Imaging Neuroscience 3. DOI 10.1162/imag_a_00446. PMID 40109899.
15. Rosen AFG et al. 2018. Quantitative assessment of structural image quality. NeuroImage 169:407-418. DOI 10.1016/j.neuroimage.2017.12.059. PMID 29278774.
16. Monereo-Sanchez J et al. 2021. Quality control strategies for brain MRI segmentation and parcellation: insights from the Maastricht Study. NeuroImage 237:118174. DOI 10.1016/j.neuroimage.2021.118174. PMID 34000406.
17. Klapwijk ET et al. 2019. Qoala-T: a supervised-learning tool for quality control of FreeSurfer segmented MRI data. NeuroImage 189:116-129. DOI 10.1016/j.neuroimage.2019.01.014. PMID 30633965.
18. Esteban O et al. 2017. MRIQC: advancing the automatic prediction of image quality in MRI from unseen sites. PLoS One 12:e0184661. DOI 10.1371/journal.pone.0184661. PMID 28945803.
19. Backhausen LL et al. 2016. Quality control of structural MRI images applied using FreeSurfer: a hands-on workflow to rate motion artifacts. Front Neurosci 10:558. PMID 27570508 (title/DOI unverified).
20. Reuter M et al. 2015. Head motion during MRI acquisition reduces gray matter volume and thickness estimates. NeuroImage 107:107-115. DOI 10.1016/j.neuroimage.2014.12.006. PMID 25498430.
21. Fortin JP et al. 2018. Harmonization of cortical thickness measurements across scanners and sites. NeuroImage 167:104-120. DOI 10.1016/j.neuroimage.2017.11.024. PMID 29155184.
22. Fortin JP et al. 2017. Harmonization of multi-site diffusion tensor imaging data. NeuroImage 161:149-170. DOI 10.1016/j.neuroimage.2017.08.047. PMID 28826946.
23. Beer JC et al. 2020. Longitudinal ComBat: a method for harmonizing longitudinal multi-scanner imaging data. NeuroImage 220:117129. DOI 10.1016/j.neuroimage.2020.117129. PMID 32640273.
24. Uhr V et al. 2025. Deep-learning versus classical pipelines and white-matter hypointensities. arXiv:2503.20571 (preprint, unverified).

Internal sources: demdas-gm/doku/DEMDAS_pipeline_protocol_v1.md, demdas-gm/hpc/README_HPC.md, demdas-gm/literatur/quality_levers_2026-10-12.md, compute_plan_full_cohort_2026-10-12.md, segmentation_best_practice_2026-10-13.md; wiki blackbeard_wikki/knowledge/brain_volumetry (findings freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort, synthseg-in-freesurfer-8-runs-on-cpu-only; rules cohort-copies-need-a-gzip-sweep, longitudinal-volumetry-needs-error-statistics) and knowledge/mri_qc_viewers/rules.

## Verknuepft
- [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort](freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort.md)
- [chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg](chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg.md)
- [demdas-pipeline-protocol-v1](demdas-pipeline-protocol-v1.md)
- PDF: [demdas-volumetry-primer-2026-10-13.pdf](demdas-volumetry-primer-2026-10-13.pdf)
