---
id: research-cross-sectional-vs-longitudinal-consistency-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) via the compact literature tool, public literature only; quellen-pruefen 2026-10-18 (32 references, 32 with PMID, 32 correct, 0 wrong); all metadata and 'Shows' lines copied from the retrieved records
verweist_auf: [research-subcortical-segmentation-longitudinal-stroke-2026-10, research-longitudinal-volumetry-statistics-after-stroke-2026-10, longitudinal-volumetry-needs-error-statistics]
---

# Literature: is cross-sectional per-session segmentation (SynthSeg, recon-all) consistent enough for 5-year atrophy, or is a longitudinal pipeline required?

## Aussage
- **A longitudinal pipeline is required for within-person change, even when per-session cross-sectional quality is
  excellent.** The processing stream (longitudinal vs cross-sectional) is a larger determinant of measured change than
  scanner, sequence or head tilt; the FreeSurfer longitudinal stream is notably superior to the cross-sectional stream
  for reliability of individual change [5][8][10][11].
- **The reason is a built-in asymmetry, not accuracy.** Running each session independently treats the sessions
  differently and injects processing variance into the change signal; all images of a subject must be treated
  identically and an unbiased within-subject template is needed to remove this bias and avoid over-regularisation
  [3][4].
- **Cross-sectional is fine for one-time volume/QC, not for trajectories.** Cross-sectional segmenters remain valid and
  robust for a single session; the requirement to use the longitudinal stream is about the *difference*, not the level
  [1][2][6].
- **SynthSeg (and SynthSeg+ / SynthSeg-robust) is a cross-sectional segmenter by design.** Its strength is contrast- and
  resolution-invariance on heterogeneous clinical data with no retraining; there is no built-in temporal model, so
  running it per session does not by itself confer longitudinal consistency [1][2].
- **SAMSEG is the more repeatable cross-sectional alternative and is sequence-adaptive**, with significantly lower
  within- and between-scanner differences between repeated measures than FreeSurfer ASEG while keeping sensitivity to
  clinical change [6][7].
- **Deep-learning longitudinal methods with explicit temporal coupling exist and beat the longitudinal-FreeSurfer
  baseline on sensitivity to atrophy**: V2C-Long (longitudinal cortex reconstruction with spatiotemporal
  correspondence) [13], USLR (unbiased smooth longitudinal registration) [14], GeoLongSeg (geodesic shape regression for
  hippocampal atrophy) [18], and a FreeSurfer longitudinal whole-brain + WMH tool [12].
- **Implausible volume *increases* are common and expected, and the size of the effect is known.** Year-to-year brain
  volume fluctuates; the smallest detectable change (MDC) in an individual was 0.6-0.7 % whole-brain and reliable
  detection of pathological loss over one year required changes above about 1.1 % [9].
- **The flagging threshold is the smallest detectable change / repeatability coefficient, computed per structure and per
  scanner.** Six-package comparison yields within-scanner SDC from 1.02 % (SAMSEG whole brain) to 14.55 % (FreeSurfer
  CSF) and between-scanner SDC from 4.83 % (SynthSeg thalamus) to 29.25 % (CAT12 thalamus) [10]. Scanner change is the
  dominant false-atrophy source [10][11][26].
- **Test-retest reliability of the longitudinal stream is not unlimited either**: 2-year individual-change reliability is
  modest and reliability improves mainly with *longer follow-up*, not more observations — a 5-year design is on the good
  side [8].
- **QC must gate the numbers before the model.** Prescreen with global metrics (Euler number, image-quality metrics,
  SynthSeg+ faulty-segmentation detection), but do not exclude on global morphological outliers; image quality is the
  factor most often associated with variability [2][11][24][25].
- **Lesion growth or a new infarct between visits breaks per-session pipelines and lesion filling is not a cure.**
  Lesion filling changes regional cortical thickness and grey-matter volume estimates and improves accuracy, but does
  not remove the between-session inconsistency of a *changing* lesion; the mask must be consistent across sessions and
  lesion volume carried as a covariate [15][16][17].
- **Multisite is a separate axis from the longitudinal axis.** Site/scanner effects persist even under a harmonised
  protocol and must be handled by longitudinal ComBat (more powerful for change than cross-sectional ComBat) in addition
  to the longitudinal stream [20][21][27][28]. WMH volume can be estimated from T1 alone in stroke when FLAIR is absent
  (WMH-SynthSeg) [32].

---

### Practical recommendation (as written for our setup)
Our setup: 7 sites, same MPRAGE 1 mm protocol, several Siemens models, visits 0/6/36/60 months, older ischaemic-stroke
adults with WMH and atrophy; SynthSeg 2 (FreeSurfer 8.2, cross-sectional per session, `--robust --qc`) on raw T1 and on
lesion-filled T1; per-structure QC gate (SynthSeg QC >= 0.65); cortical thickness with cross-sectional recon-all; Euler
gate; linear mixed models; longComBat planned.

1. **Do not treat per-session SynthSeg as a trajectory instrument.** Keep SynthSeg/per-session volumes as the
   *cross-sectional level* readout, but compute the *within-subject change* with a longitudinal stream. Add a
   longitudinal reference track: FreeSurfer longitudinal stream on the same subjects, and - where the extra cost is
   acceptable - one of the coupled DL methods (V2C-Long, USLR) as an independent check [3][4][13][14].
2. **Build the unbiased within-subject template** (all four visits, one template per patient) and process every session
   against it [3][4].
3. **Quantify the floor before modelling.** Run a local test-retest / travelling-subject repeat scan per scanner model
   to obtain within-scanner and between-scanner SDC per structure; publish within-subject SD/CV and SDC next to every
   atrophy rate [9][10].
4. **Flag implausible increases explicitly** with an SDC rule: for each structure and scanner combination, flag a
   visit-to-visit *increase* (or decrease) exceeding the 95 % repeatability coefficient (1.96 x sqrt(2) x within-subject
   SD). Expect increases up to ~0.7 % whole-brain even in stability; do not call a change pathological below ~1.1 % in
   one year [9].
5. **Gate on QC before harmonisation.** Keep the Euler gate and the per-structure SynthSeg QC gate; add SynthSeg+
   faulty-segmentation detection; treat these as *screening* flags, not exclusion criteria on global morphological
   outliers [2][11][24][25].
6. **Handle lesions across time explicitly.** Keep the contralateral-mirroring fill for the infarct and NAWM fill for
   WMH, but rebuild the lesion mask per visit, verify it is spatially consistent across visits, and carry lesion and WMH
   volume as covariates; never compare a filled session against an unfilled one. Filling does not remove *scanner*
   effects [15][16][17].
7. **Harmonise longitudinally, not cross-sectionally.** Apply longComBat with site/scanner as batch and age and
   scan-interval preserved, fit on a training split, and report the unharmonised model as a sensitivity analysis;
   verify harmonisation preserves the expected atrophy contrast [20][21][27].
8. **Model with subject random intercept + random slope for time** on the longitudinal-stream volumes, time in
   continuous years, lesion/WMH volumes as covariates; individual-level claims only above the SDC [8][9].

---

## Trägt
Every reference retrieved in this task; quellen-pruefen: 32 references, 32 with PMID, 32 correct, 0 wrong; DOIs
registered at doi.org (2026-10-18); one "Shows" sentence per reference copied from its retrieved abstract.

## Trägt nicht
Abstract-level evidence, a literature map rather than a systematic review. Open questions:

- **Quantitatively, how much worse is per-session SynthSeg change than the longitudinal FreeSurfer stream in *our*
  data?** The general longitudinal superiority is established [3][4][8], but the SynthSeg-specific longitudinal
  reliability is not directly reported.
- **What is the right SynthSeg-2 QC threshold per structure and per Siemens model?** The 0.65 gate is a project choice;
  the retrieved literature gives strategy comparisons [25] but no per-structure threshold calibrated on stroke scans.
- **Does lesion filling of a *growing* WMH/infarct between visits bias the trajectory?** Filling improves single-visit
  accuracy [15][16][17], but the retrieved abstracts do not separate the effect of a changing lesion volume from the
  filling itself on the change estimate.
- **Is longitudinal-then-harmonise preferable to harmonise-then-model?** longComBat is more powerful than cross-sectional
  ComBat [20], and validation on structural metrics warns that harmonising when there is no scanner effect can obscure
  biology [21], but the best ordering for a 7-site stroke design is not settled.
- **Do the coupled DL longitudinal methods have published failure modes on lesions?** Their papers report gains on
  non-stroke cohorts [13][14][18]; behaviour with large infarcts and WMH is unverified.
- **What is the practical sample-size penalty of per-session cross-sectional segmentation vs the longitudinal stream?**
  Reliability gain of longitudinal processing is 15-50 % [11] and 2-year designs need ~2.7x the subjects of 4-year
  designs [8], but the exact inflation factor for a 4-visit 5-year stroke design is unverified.

## Bruchindikator
A cited abstract that does not contain the claim, or a study showing per-session cross-sectional segmentation of the
type we use gives change estimates equal to the longitudinal stream within the SDC.

## Ablesung
[1] Billot B, Greve DN, Puonti O, et al. (2023). SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining. Medical Image Analysis. doi:10.1016/j.media.2023.102789. PMID: 36857946.
Shows: a CNN trained only on synthetic data with fully randomised contrast and resolution segments real scans of any contrast/resolution without retraining, enabling analysis of heterogeneous clinical data.

[2] Billot B, Magdamo C, Cheng Y, et al. (2023). Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. Proc Natl Acad Sci U S A. doi:10.1073/pnas.2216399120. PMID: 36802420.
Shows: SynthSeg+ adds cortical parcellation, ICV estimation and automatic detection of faulty segmentations, and in an aging study on 14 000 clinical scans replicates atrophy patterns seen on higher-quality data.

[3] Reuter M, Schmansky NJ, Rosas HD, et al. (2012). Within-subject template estimation for unbiased longitudinal image analysis. NeuroImage. doi:10.1016/j.neuroimage.2012.02.084. PMID: 22430496.
Shows: an unbiased robust within-subject template plus identical treatment of all time points reduces variability and avoids over-regularisation; removing only interpolation asymmetry is insufficient to remove processing bias.

[4] Reuter M, Fischl B (2011). Avoiding asymmetry-induced bias in longitudinal image processing. NeuroImage. doi:10.1016/j.neuroimage.2011.02.076. PMID: 21376812.
Shows: longitudinal processing of images against a single earlier reference introduces asymmetry-induced bias, which is avoided by using an unbiased within-subject template.

[5] Hedges EP, Dimitrov M, Zahid U, et al. (2022). Reliability of structural MRI measurements: The effects of scan session, head tilt, inter-scan interval, acquisition sequence, FreeSurfer version and processing stream. NeuroImage. doi:10.1016/j.neuroimage.2021.118751. PMID: 34848299.
Shows: scan session, repositioning, head tilt, sequence, FreeSurfer version and processing stream all affect test-retest reliability of structural measures, quantifying how much these factors matter for longitudinal designs.

[6] Sederevičius D, Vidal-Piñeiro D, Sørensen Ø, et al. (2021). Reliability and sensitivity of two whole-brain segmentation approaches included in FreeSurfer - ASEG and SAMSEG. NeuroImage. doi:10.1016/j.neuroimage.2021.118113. PMID: 33940143.
Shows: in 1 629 subjects and 24 subjects scanned on three Siemens models, SAMSEG gave significantly lower differences between repeated measures intra- and inter-scanner without losing sensitivity to longitudinal or clinical change.

[7] Puonti O, Iglesias JE, Van Leemput K (2016). Fast and sequence-adaptive whole-brain segmentation using parametric Bayesian modeling. NeuroImage. doi:10.1016/j.neuroimage.2016.09.011. PMID: 27612647.
Shows: the parametric Bayesian whole-brain segmentation underlying SAMSEG achieves state-of-the-art accuracy on T1 across scanners/field strengths/sequences while being one to two orders of magnitude faster.

[8] Vidal-Piñeiro D, Sørensen Ø, Strømstad M, et al. (2025). Reliability of structural brain change in cognitively healthy adult samples. Imaging Neuroscience (Camb). doi:10.1162/imag_a_00547. PMID: 40800869.
Shows: longitudinal reliability of brain change was modest at 2-year follow-up and rose strongly with longer follow-up; 2-year designs need ~2.7x/4.0x more subjects than 4/6-year designs, and the FreeSurfer longitudinal stream was notably superior to the cross-sectional stream.

[9] Narayanan S, Nakamura K, Fonov VS, et al. (2020). Brain volume loss in individuals over time: Source of variance and limits of detectability. NeuroImage. doi:10.1016/j.neuroimage.2020.116737. PMID: 32171923.
Shows: repeated MPRAGE showed technical variability dominates measured brain volume change until loss exceeds ~0.6-0.7 % (one scanner) and ~1.1 % for a reliable 1-year pathological change, defining minimum detectable change.

[10] van Nederpelt DR, Amiri H, Brouwer I, et al. (2023). Reliability of brain atrophy measurements in multiple sclerosis using MRI: an assessment of six freely available software packages for cross-sectional analyses. Neuroradiology. doi:10.1007/s00234-023-03189-8. PMID: 37526657.
Shows: across FreeSurfer, FSL, SAMSEG, FastSurfer, CAT-12 and SynthSeg on three 3 T scanners, within-scanner SDC ranged from 1.02 % to 14.55 % and between-scanner SDC from 4.83 % to 29.25 %, with no clear effect of lesion filling.

[11] Rusinek H, Bokacheva L, Chen H, et al. (2026). Test-retest reliability of FreeSurfer measures of neurodegeneration. NeuroImage. doi:10.1016/j.neuroimage.2026.121920. PMID: 41966233.
Shows: in 100 older adults scanned twice within ~5.5 weeks, the FreeSurfer longitudinal stream improved precision by 15-50 % over cross-sectional processing for most measures, largest for entorhinal thickness.

[12] Cerri S, Greve DN, Hoopes A, et al. (2023). An open-source tool for longitudinal whole-brain and white matter lesion segmentation. NeuroImage: Clinical. doi:10.1016/j.nicl.2023.103354. PMID: 36907041.
Shows: SAMSEG extended with subject-specific latent variables that enforce temporal consistency attained higher test-retest reliability than its cross-sectional formulation and two benchmark longitudinal methods.

[13] Bongratz F, Fecht J, Rickmann AM, et al. (2025). V2C-Long: Longitudinal cortex reconstruction with spatiotemporal correspondence. Imaging Neuroscience (Camb). doi:10.1162/imag_a_00500. PMID: 40800931.
Shows: a dedicated longitudinal deep-learning cortex reconstruction establishes strong inherent spatiotemporal correspondence across visits, removing the need for surface-based post-processing.

[14] Casamitjana A, Sala-Llonch R, Lekadir K, et al. (2025). USLR: An open-source tool for unbiased and smooth longitudinal registration of brain MRI. Medical Image Analysis. doi:10.1016/j.media.2025.103662. PMID: 40592111.
Shows: USLR estimates non-linear image trajectories that are smooth across time, unbiased to any timepoint and robust to artefacts, and improves time-consistency in an Alzheimer's disease study.

[15] Magon S, Gaetano L, Chakravarty MM, et al. (2014). White matter lesion filling improves the accuracy of cortical thickness measurements in multiple sclerosis patients: a longitudinal study. BMC Neuroscience. doi:10.1186/1471-2202-15-106. PMID: 25200127.
Shows: filling WM lesions with the intensity of neighbouring normal-appearing WM improved the accuracy of cross-sectional and longitudinal cortical thickness measures in 50 MS patients over 3 and 6 years.

[16] Valverde S, Oliver A, Roura E, et al. (2015). Quantifying brain tissue volume in multiple sclerosis with automated lesion segmentation and filling. NeuroImage: Clinical. doi:10.1016/j.nicl.2015.10.012. PMID: 26740917.
Shows: fully automated lesion segmentation plus filling pipelines introduced acceptable error in GM/WM tissue segmentation compared with expert lesion annotation filling, replacing manual lesion masking.

[17] Pareto D, Sastre-Garriga J, Aymerich FX, et al. (2016). Lesion filling effect in regional brain volume estimations: a study in multiple sclerosis patients with low lesion load. Neuroradiology. doi:10.1007/s00234-016-1654-5. PMID: 26847633.
Shows: white matter lesions are erroneously segmented as grey matter, and lesion filling reduced the resulting error in grey matter fraction and regional volumes.

[18] Gao N, Chen H, Guo X, et al. (2024). Geodesic shape regression based deep learning segmentation for assessing longitudinal hippocampal atrophy in dementia progression. NeuroImage: Clinical. doi:10.1016/j.nicl.2024.103623. PMID: 38821013.
Shows: GeoLongSeg integrates geodesic shape regression into a two-stage network to reduce longitudinal segmentation variability unrelated to disease by enforcing intra-individual morphological consistency.

[19] Tustison NJ, Holbrook AJ, Avants BB, et al. (2019). Longitudinal Mapping of Cortical Thickness Measurements: An Alzheimer's Disease Neuroimaging Initiative-Based Evaluation Study. Journal of Alzheimer's Disease. doi:10.3233/JAD-190283. PMID: 31356207.
Shows: an ANTs longitudinal framework that minimises residual variability while maximising between-subject variability gave competitive-to-superior power for detecting longitudinal cortical change versus cross-sectional and longitudinal FreeSurfer.

[20] Beer JC, Tustison NJ, Cook PA, et al. (2020). Longitudinal ComBat: A method for harmonizing longitudinal multi-scanner imaging data. NeuroImage. doi:10.1016/j.neuroimage.2020.117129. PMID: 32640273.
Shows: longitudinal ComBat models additive and multiplicative scanner effects in repeated measures and is more powerful for detecting longitudinal change than cross-sectional ComBat, with better type I error control than covariate adjustment.

[21] Richter S, Winzeck S, Correia MM, et al. (2022). Validation of cross-sectional and longitudinal ComBat harmonization methods for magnetic resonance imaging data on a travelling subject cohort. NeuroImage: Reports. doi:10.1016/j.ynirp.2022.100136. PMID: 36507071.
Shows: on a travelling-subject cohort, structural metrics showed no significant scanner effect and harmonisation gave no benefit and could obscure true effects, whereas diffusion metrics had marked scanner effects that were successfully harmonised.

[22] Li Q, Pardoe H, Lichter R, et al. (2015). Cortical thickness estimation in longitudinal stroke studies: A comparison of 3 measurement methods. NeuroImage: Clinical. doi:10.1016/j.nicl.2014.08.017. PMID: 26110108.
Shows: comparing a surface-based (FreeSurfer) and two voxel-based cortical thickness methods in stroke, accuracy of segmentation was worst in peri-lesional cortex, making this the critical region for longitudinal thickness estimates.

[23] Khlif MS, Werden E, Egorova N, et al. (2019). Assessment of longitudinal hippocampal atrophy in the first year after ischemic stroke using automatic segmentation techniques. NeuroImage: Clinical. doi:10.1016/j.nicl.2019.102008. PMID: 31711030.
Shows: automated hippocampal volumes agreed variably with manual tracing in stroke and lesion presence affected volume estimation; hippocampal volume fell ~3.9 % in first-ever and ~9.2 % in recurrent stroke at three months.

[24] Rosen AFG, Roalf DR, Ruparel K, et al. (2018). Quantitative assessment of structural image quality. NeuroImage. doi:10.1016/j.neuroimage.2017.12.059. PMID: 29278774.
Shows: quantitative T1 quality measures relate systematically to cortical thickness and, if ignored, bias inference about age-related structural associations, across 1 840 manually rated scans.

[25] Monereo-Sánchez J, de Jong JJA, Drenthen GS, et al. (2021). Quality control strategies for brain MRI segmentation and parcellation: Practical approaches and recommendations - insights from the Maastricht study. NeuroImage. doi:10.1016/j.neuroimage.2021.118174. PMID: 34000406.
Shows: side-by-side comparison of 12 automated QC strategies against manual editing in 259 subjects gives practical recommendations for reducing measurement error in segmentation-based morphometry.

[26] Puzio T, Matera K, Karwowski J, et al. (2025). Deep learning-based automatic segmentation of brain structures on MRI: A test-retest reproducibility analysis. Computational and Structural Biotechnology Journal. doi:10.1016/j.csbj.2025.04.007. PMID: 40271109.
Shows: deep-learning segmentation was highly consistent within the same scanner type but degraded when scanner type/field strength differed, which matters for a mixed-scanner multisite fleet.

[27] Yang Q, Shomal-Zadeh F, Gholipour A (2026). Harmonization in magnetic resonance imaging: A survey of acquisition, image-level, and feature-level methods. Medical Image Analysis. doi:10.1016/j.media.2026.104066. PMID: 41936201.
Shows: a survey showing that site/batch effects reduce reproducibility and power and that harmonisation must remove site bias while preserving biological signal, categorising acquisition-, image- and feature-level methods.

[28] Jakimovski D, Zivadinov R, Bergsland N, et al. (2022). Multisite MRI reproducibility of lateral ventricular volume using the NAIMS cooperative pilot dataset. Journal of Neuroimaging. doi:10.1111/jon.12998. PMID: 35384119.
Shows: scanner-induced T1-based whole-brain volume error was large relative to clinically meaningful change, and T2-FLAIR-based lateral ventricular volume was proposed as a more reproducible proxy.

[29] Elliott ML, Du J, Nielsen JA, et al. (2026). Precision estimates of longitudinal brain aging capture unexpected individual differences in one year. Nature Communications. doi:10.1038/s41467-026-68886-3. PMID: 41644538.
Shows: densely repeated cluster scanning over one year was required to reveal individual differences in brain change that ordinary single scans could not resolve, quantifying measurement error in short intervals.

[30] Schmitz-Koep B, Schultz V, Bongratz F, et al. (2026). Longitudinal assessment of cortical thickness in healthy older individuals: a comparison between CAT12 and freesurfer. Neuroradiology. doi:10.1007/s00234-025-03866-w. PMID: 41384963.
Shows: cross-sectional cortical thickness values differed systematically between CAT12 and FreeSurfer, and longitudinal annualised percent change also differed significantly between the two pipelines.

[31] Aamodt EB, Lydersen S, Alnæs D, et al. (2022). Longitudinal Brain Changes After Stroke and the Association With Cognitive Decline. Frontiers in Neurology. doi:10.3389/fneur.2022.856919. PMID: 35720079.
Shows: in a multisite stroke cohort followed up to 36 months, cortical thickness and subcortical volumes declined more in the ipsilesional hemisphere and were associated with cognitive decline, demonstrating feasible longitudinal atrophy detection in stroke.

[32] Khan MH, Chakraborty S, Ferris JK, et al. (2026). Estimating white matter hyperintensities volume in individuals with stroke using T1-weighted images. NeuroImage: Reports. doi:10.1016/j.ynirp.2026.100344. PMID: 42011418.
Shows: WMH-SynthSeg and SAMSEG can estimate WMH volume from T1 alone in 227 stroke patients, relevant where FLAIR is unavailable, but accuracy varies with the lesion mask used.
