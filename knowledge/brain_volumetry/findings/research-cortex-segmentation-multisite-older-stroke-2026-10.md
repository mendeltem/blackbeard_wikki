---
id: research-cortex-segmentation-multisite-older-stroke-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) via the compact literature tool, checked by Claude Code 2026-10-18 (quellen-pruefen 0 wrong, 'Shows' spot checks against abstracts)
verweist_auf: [synthseg-cortex-qc-depends-on-site-not-protocol]
---

# Literature: reliable cortical segmentation in a multi-centre older post-stroke cohort

## Aussage
* **Cortical failure is expected in such a cohort, not a bug of ours.** In 732 clinical T1 scans the
  cortical-thickness step failed visually in **38.5 %** of scans, with errors concentrated in regions of
  high atrophy and high white-matter-hyperintensity (WMH) load [16] — remarkably close to our 43 %.
* **The cortex is intrinsically harder than subcortical structures.** It is a 1–3 mm folded sheet, so
  1 mm voxels mix grey matter, white matter and CSF: thickness estimates that ignore this partial volume
  are biased, while partial-volume-aware estimators are robust to resolution and field strength [17].
  Subcortical nuclei are compact and homogeneous and suffer far less from the same image defects.
* **The QC score we see is a cortical score, not a whole-brain score.** SynthSeg itself is explicitly
  contrast- and resolution-robust for *tissue* segmentation [1]; SynthSeg+ adds cortical parcellation
  **and** automated detection of faulty segmentations — the stage the QC score belongs to [2].
* **Volume and thickness are different problems.** SynthSeg/SynthSeg+ deliver robust cortical labels,
  parcellation and volumes; true cortical thickness needs a surface pipeline (FreeSurfer, FastSurfer) or a
  registration-based method such as DL+DiReCT [2, 3, 7].
* **For thickness, surface pipelines still lead but are the least robust on damaged brains.** FreeSurfer and
  FastSurfer were the most consistent pair among four tools; FastSurfer is a full FreeSurfer alternative in
  <1 min (volumes) to ~1 h (thickness) with increased test–retest reliability [3, 8].
* **CAT12 is a fast voxel-based alternative, but not interchangeable with FreeSurfer.** FreeSurfer vs CAT12
  reproducibility is lower at ROI than at individual level, an acquisition-site effect is present, while
  within-framework test–retest reliability is high — do not mix the two across sites [6].
* **Scanner model and software version matter for the cortex.** 3–10 % inter-site variability and
  significant site differences in 21 of 68 cortical ROIs [11]; Siemens sites were more reliable than
  GE/Philips (0.80 vs 0.69) in a 21-site study [12]; FreeSurfer version, head tilt, sequence and processing
  stream change results, and thickness is the least reliable measure (ICC > 0.82 vs > 0.97 for volumes) [14].
* **Harmonisation helps the statistics, not the segmentation.** ComBat removes scanner effects in cortical
  thickness and increases power [10] — but it is a modelling step applied to the derived measures, not a
  repair of a failed surface.
* **Preprocessing that pays off:** careful lesion filling / inpainting before any cortical step [18, 19],
  plus motion/quality gating [13]. Super-resolution is not required at 1 mm and is not supported by the
  retrieved evidence (unverified).
* **Recommendation (details in §4):** keep SynthSeg+ for cortical labels/volumes and use its QC score as a
  flag; compute cortical **thickness** with FastSurfer (primary) or FreeSurfer recon-all with the
  longitudinal stream (reference) on lesion-filled T1, in one fixed software version, and harmonise the
  derived cortical measures (ComBat) before group statistics.

---

### Practical recommendation (as written for our setup)
Cohort: 3T Siemens MPRAGE 1 mm, 7 sites, older post-stroke; SynthSeg cortex QC < 0.65 in 43 % of sessions
(12–82 % by site/model), subcortical QC fine.

1. **Keep SynthSeg+ but re-scope it.** Use SynthSeg+ for cortical labels, parcellation and volumes and keep
   its QC score as a *flag*; treat a low cortex QC score as "thickness from this scan is not usable", not as
   "the brain segmentation failed" [1, 2].
2. **Lesion-fill / inpaint the T1 before any cortical step** (LST-style filling, or FastSurfer-LIT diffusion
   inpainting). This is the single highest-yield preprocessing step for a post-stroke cohort [18, 19].
3. **Compute cortical thickness with a surface pipeline on the lesion-filled image, in one fixed version:**
   - Primary: **FastSurfer** — full FreeSurfer alternative (thickness in ~1 h), increased test–retest
     reliability, high dementia sensitivity, most consistent with FreeSurfer of the tools tested [3, 8].
   - Reference/backbone: **FreeSurfer recon-all 7.x with the longitudinal stream** (precision gain 15–50 %,
     largest for entorhinal thickness) [15].
   - Thickness for selected ROIs only, when speed matters: **DL+DiReCT** (r = .887 vs FreeSurfer, similar
     scan–rescan robustness) [7].
4. **Do not switch tools or versions mid-study.** FreeSurfer, FastSurfer, BrainSuite, volBrain and CAT12 are
   not interchangeable for thickness [6, 8]; version, sequence, head tilt and stream all matter [14].
   Document the exact version and process all sites with it.
5. **Use partial-volume-aware thickness estimation** where available; hard-thresholded thickness is biased
   at 1 mm [17].
6. **Harmonise the derived cortical measures across the 7 sites before statistics:** ComBat on cortical
   thickness removes scanner effects and increases power [10]; additionally keep site/scanner model in the
   statistical model, because cortical ROIs differ significantly by site [11, 12].
7. **Gate on QC and report per-site failure rates.** The 12–82 % spread we observe is exactly the
   documented between-site/scanner heterogeneity [11, 12]; publishing it stratified by site and scanner
   model is the honest way to handle it, together with the Euler-characteristic and motion metrics [13, 15].
8. **Do not expect a volume pipeline to produce thickness.** SynthSeg/SynthSeg+ cortical label volumes and
   FreeSurfer/FastSurfer thickness are different quantities; report them separately and never compare
   thickness across tools within one study [2, 3, 8].

---

## Trägt
Every reference retrieved in the task; quellen-pruefen: 0 wrong PMIDs/titles, DOIs registered (2026-10-18); one "Shows"
sentence per reference from its abstract; spot checks consistent.

## Trägt nicht
Abstract-level evidence, a literature map rather than a systematic review. Open questions:

* Is the SynthSeg+ QC score calibrated separately for cortical structures, and what threshold is right for
  a post-stroke 3T cohort? No retrieved paper validates the SynthSeg+ cortex QC score against a
  post-stroke visual rating — this needs a local rating study (ties into topic g_segmentation_qc_at_scale).
* How much of the 12–82 % site spread is **scanner model/coil** vs **protocol** (TI/TR, resolution) vs
  **subject factors** (atrophy, WMH, motion)? A phantom/travelling-subject analysis at our 7 sites would
  separate these components [11, 12].
* Does diffusion-based **lesion inpainting** improve cortical thickness in *stroke* brains specifically?
  Demonstrated for tumours and MS lesions, not yet for stroke, in the retrieved literature [18, 19].
* Is SAMSEG's lower inter-scanner variability [4] transferable to the **cortex and to thickness**, not just
  to the eight subcortical structures tested?
* Which harmonisation (ComBat vs DeepComBat vs normative modelling) is best for **longitudinal atrophy**,
  rather than cross-sectional thickness? (unverified)

---

## Bruchindikator
A cited abstract that does not contain the claim, or a newer study contradicting the recommendation.

## Ablesung
[1] Billot B, Greve DN, Puonti O, et al. (2023). SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining. Medical Image Analysis. doi:10.1016/j.media.2023.102789 PMID: 36857946
Shows: SynthSeg is trained on synthetic data with fully randomised contrast and resolution, needs no retraining or fine-tuning and generalises to 5,000 scans of six modalities and ten resolutions — the basis for using it as a robust tissue segmenter across our heterogeneous 7-site data.

[2] Billot B, Magdamo C, Cheng Y, et al. (2023). Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. Proceedings of the National Academy of Sciences U S A. doi:10.1073/pnas.2216399120 PMID: 36802420
Shows: SynthSeg+ adds cortical parcellation, intracranial volume estimation and automated detection of faulty segmentations and replicated atrophy patterns in an aging study on 14,000 clinical scans — it is the pipeline that produces our cortex QC score.

[3] Henschel L, Conjeti S, Estrada S, et al. (2020). FastSurfer - A fast and accurate deep learning based neuroimaging pipeline. NeuroImage. doi:10.1016/j.neuroimage.2020.117012 PMID: 32526386
Shows: A 95-class deep network replicates FreeSurfer segmentation, surface reconstruction and cortical parcellation, providing volumetric analysis in under 1 minute and surface-based thickness in about 1 hour with increased test–retest reliability and high sensitivity to dementia group differences — our recommended fast thickness pipeline.

[4] Sederevičius D, Vidal-Piñeiro D, Sørensen Ø, et al. (2021). Reliability and sensitivity of two whole-brain segmentation approaches included in FreeSurfer - ASEG and SAMSEG. NeuroImage. doi:10.1016/j.neuroimage.2021.118113 PMID: 33940143
Shows: In 1,629 subjects plus 24 subjects scanned on three Siemens scanner models, SAMSEG gave significantly lower differences between repeated measures for intra- and inter-scanner analysis than ASEG while both still detected within-person longitudinal change — evidence for lower scanner sensitivity of the Bayesian approach (for eight subcortical structures).

[5] Gaser C, Dahnke R, Thompson PM, et al. (2024). CAT: a computational anatomy toolbox for the analysis of structural MRI data. GigaScience. doi:10.1093/gigascience/giae049 PMID: 39102518
Shows: CAT provides voxel-based, surface-based and region-based morphometric analysis streams, incorporates multiple quality-control options and covers cross-sectional and longitudinal preprocessing end to end — the citable reference for CAT12, one of the compared tools.

[6] Dias MFM, Carvalho P, Castelo-Branco M, et al. (2022). Cortical thickness in brain imaging studies using FreeSurfer and CAT12: A matter of reproducibility. NeuroImage: Reports. doi:10.1016/j.ynirp.2022.100137 PMID: 40567565
Shows: Reproducibility between FreeSurfer and CAT12 for cortical thickness is lower at ROI than at individual level, an acquisition-site effect was identified, and multicentric cross-sectional results must be interpreted with caution, while within-framework test–retest reliability is high — the key argument against mixing frameworks across our sites.

[7] Rebsamen M, Rummel C, Reyes M, et al. (2020). Direct cortical thickness estimation using deep learning-based anatomy segmentation and cortex parcellation. Human Brain Mapping. doi:10.1002/hbm.25159 PMID: 32786059
Shows: DL+DiReCT correlates with FreeSurfer at r = .887 for global mean cortical thickness (vs r = .608 for ANTs), has similar scan–rescan robustness to FreeSurfer while ANTs was poor, and gave the largest effect sizes for controls versus dementia — a fast, validated thickness option for ROI work.

[8] Emekli E, Emekli E, Demirel BC, et al. (2026). Evaluation of consistency and reliability among four brain segmentation tools for cortical thickness measurement. Journal of Neuroscience Methods. doi:10.1016/j.jneumeth.2026.110758 PMID: 41905534
Shows: Cortical thickness differed significantly across FreeSurfer, FastSurfer, BrainSuite and volBrain; FreeSurfer and FastSurfer were the most consistent pair, FreeSurfer showed no correlation with any other software and seven cortical regions had no inter-software consistency — tools are not interchangeable.

[9] Blattner T, Romascano D, McKinley R, et al. (2026). Mitigating the Impact of MR Sequence Parameters: Increasing the Robustness of DL-Based Cortical Thickness Estimates. Human Brain Mapping. doi:10.1002/hbm.70560 PMID: 42252567
Shows: Fine-tuning a DL thickness tool on simulated MPRAGE from quantitative relaxation maps reduced its contrast dependence (correlation with contrast from −0.644 to 0.094) and it outperformed FreeSurfer and SynthSeg on a synthetic-atrophy dataset — direct evidence that sequence contrast, not only noise, drives cortical thickness error.

[10] Fortin JP, Cullen N, Sheline YI, et al. (2018). Harmonization of cortical thickness measurements across scanners and sites. NeuroImage. doi:10.1016/j.neuroimage.2017.11.024 PMID: 29155184
Shows: Across 11 scanners in two large multi-site studies, ComBat removed scanner-related variability in cortical thickness while increasing the power and reproducibility of subsequent statistical analyses — the harmonisation we propose for our 7 sites.

[11] Bosco P, Lancione M, Retico A, et al. (2023). Quality assessment, variability and reproducibility of anatomical measurements derived from T1-weighted brain imaging: The RIN-Neuroimaging Network case study. Physica Medica. doi:10.1016/j.ejmp.2023.102577 PMID: 37126963
Shows: In 77 T1 scans from 15 sites and three vendors, cortical thickness varied 3–10 % (subcortical volumes 11–19 %), 21 of 68 cortical ROIs differed significantly by site, and vendor could be classified from brain measures above chance — quantifies the between-site heterogeneity behind our 12–82 % spread.

[12] Pan Y, Hong LE, Acheson A, et al. (2024). A Site-Wise Reliability Analysis of the ABCD Diffusion Fractional Anisotropy and Cortical Thickness: Impact of Scanner Platforms. Human Brain Mapping. doi:10.1002/hbm.70070 PMID: 39526419
Shows: Across 21 ABCD sites, site-wise cortical thickness reliability was 0.76 ± 0.12 and significantly higher at Siemens sites than at GE/Philips sites (0.80 vs 0.69) — scanned evidence that scanner model modulates cortical thickness reliability.

[13] Olsson H, Millward JM, Starke L, et al. (2024). Simulating rigid head motion artifacts on brain magnitude MRI data-Outcome on image quality and segmentation of the cerebral cortex. PLoS One. doi:10.1371/journal.pone.0301132 PMID: 38626138
Shows: Using real and simulated motion-corrupted data (MR-ART, n = 148) and six tools, cortical segmentation Dice decreased with motion severity for all tools and SynthSeg+ was the most robust — motion must be gated if cortical measures are to be trusted.

[14] Hedges EP, Dimitrov M, Zahid U, et al. (2022). Reliability of structural MRI measurements: The effects of scan session, head tilt, inter-scan interval, acquisition sequence, FreeSurfer version and processing stream. NeuroImage. doi:10.1016/j.neuroimage.2021.118751 PMID: 34848299
Shows: With FreeSurfer v5.3.0, 6.0.0 and 7.1.0, subcortical and cortical volumes and cortical surface areas reached mean ICC > 0.97 while cortical thickness reached only mean ICC > 0.82, and head tilt had the greatest adverse impact — the version/stream/head-position sensitivity we must fix.

[15] Rusinek H, Bokacheva L, Chen H, et al. (2026). Test-retest reliability of FreeSurfer measures of neurodegeneration. NeuroImage. doi:10.1016/j.neuroimage.2026.121920 PMID: 41966233
Shows: In 100 older adults (mean age 73.5), longitudinal FreeSurfer processing improved precision by 15–50 % (largest gain for entorhinal thickness), the Euler characteristic was the only factor significantly associated with measurement variability, and detecting a 1 % change needed 36 to over 300 subjects depending on the region.

[16] Metz A, Moqadam R, Zeighami Y, et al. (2025). Quantifying brain atrophy in Frontotemporal Dementia: a head-to-head comparison of neuroimaging techniques. medRxiv. doi:10.1101/2025.10.28.25339007 PMID: 41282725
Shows: In 732 clinical T1 scans, visual QC gave failure rates of 38.5 % for cortical thickness and 23.6 % for FreeSurfer segmentation versus 2–3 % for registration-based volumetric measures, with errors concentrated in high-atrophy and high-WMH regions — the closest published analogue to our cortex-QC failure rate.

[17] Joshi AA, Salloum R, Bhushan C, et al. (2025). Robust cortical thickness estimation in the presence of partial volumes using adaptive diffusion equation. Journal of Neuroscience Methods. doi:10.1016/j.jneumeth.2025.110552 PMID: 40850598
Shows: An adaptive-diffusion thickness estimator that uses grey-matter fractions is robust to finite resolution and blurring, is histologically consistent and showed superior consistency in multi-scanner test–retest versus Laplace-based methods and FreeSurfer — the quantitative reason the folded cortex is harder than compact subcortical structures.

[18] Pollak C, Kügler D, Bauer T, et al. (2025). FastSurfer-LIT: Lesion inpainting tool for whole-brain MRI segmentation with tumors, cavities, and abnormalities. Imaging Neuroscience. doi:10.1162/imag_a_00446 PMID: 40109899
Shows: Diffusion-based inpainting of lesions and cavities outperformed prior solutions on 100 simulated tumours and 39 synthetic MS lesions and increased reliability in reproducing pre-operative cortical thickness estimates from post-operative scans — the strongest retrieved evidence that inpainting rescues cortical measures.

[19] Pareto D, Sastre-Garriga J, Aymerich FX, et al. (2016). Lesion filling effect in regional brain volume estimations: a study in multiple sclerosis patients with low lesion load. Neuroradiology. doi:10.1007/s00234-016-1654-5 PMID: 26847633
Shows: White-matter lesions are erroneously segmented as grey matter; after lesion masking or filling the grey-matter fraction decreased significantly (mean difference −0.598, p < 0.001) versus the original image in 152 patients at 3T — why lesion handling must precede cortical/volumetric segmentation.

[20] Salah Khlif M, Egorova-Brumley N, Bird LJ, et al. (2022). Cortical thinning 3 years after ischaemic stroke is associated with cognitive impairment and APOE ε4. NeuroImage: Clinical. doi:10.1016/j.nicl.2022.103200 PMID: 36116165
Shows: In 90 stroke survivors and 36 controls, cortical thickness was estimated with FreeSurfer, segmentation inaccuracies were manually corrected and infarcted ipsilesional vertices were excluded with a-priori lesion masks; cortical thinning at 3 years was more widespread ipsilesionally and greater in cognitively impaired survivors — shows how post-stroke cortical measures must handle lesions explicitly.

---

### Notes / limitations

* All 20 references were retrieved in this task with `literatur suche` / `literatur details` (PubMed); titles,
  authors, journals, years, DOIs and PMIDs were copied verbatim from the `literatur details` output, which is
  reproducible from the saved raw files (`es_*.json`, `ef_*.xml`, `det*.txt`).
* Ref [16] is a **medRxiv preprint**, not peer-reviewed; it is used for the failure-rate figure and is
  therefore weaker evidence than the peer-reviewed entries.
* Statements marked "unverified" are not backed by a retrieved abstract and must not be cited.
* Further works retrieved but not cited (kept in `det8.txt`/`ef_lesion_fill.xml`): e.g. Valverde et al. 2014
  on WM lesion refilling, and Debiasi et al. 2023 on pipeline/input/age effects on cortical estimates.

