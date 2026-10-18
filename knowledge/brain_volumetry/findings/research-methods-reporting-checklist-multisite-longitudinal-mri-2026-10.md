---
id: research-methods-reporting-checklist-multisite-longitudinal-mri-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: research report by the remote-model agent (Clara on the hospital model hub) via the compact literature tool, public literature only; quellen-pruefen 2026-10-18 (22 references, 22 with PMID, 22 correct, 0 wrong); checked and committed by Claude Code
verweist_auf: [research-longitudinal-volumetry-statistics-after-stroke-2026-10, research-cross-sectional-vs-longitudinal-consistency-2026-10]
---

# Literature: methods and reporting checklist for a multisite longitudinal structural MRI cohort

## Aussage
- The binding skeleton for our paper is STROBE (cohort checklist, 22 items) for the epidemiological/design part plus
  COBIDAS/OHBM for the imaging/analysis part; STROBE governs participants, flow, missing data, descriptive data, outcome
  definitions and generalisability [5, 6], COBIDAS governs acquisition, preprocessing, model specification and
  code/data sharing [1, 2].
- Empirical checks show that reporting is the weak link, not the analysis: across published studies methods and results
  reporting "can differ greatly" and clarifies far less than the guidelines intend [3], and the checklist literature
  itself identifies transparency/reproducibility as a persisting obstacle that checklists have not yet solved [4].
- What is most often missing in practice is not the headline model but the audit trail: exact software versions and
  container/singularity images, the full preprocessing parameter set, QC metric + threshold + number of excluded scans,
  and an a-priori analysis plan deposited before unblinding [1, 3, 4, 7].
- Pre-registration / a dated analysis plan is the single cheapest protection against analytical flexibility: 70 teams
  analysing one dataset with the same 9 hypotheses chose no two identical workflows and reached materially different
  results [22]; pre-registration formalises the prediction/postdiction distinction [7].
- For multisite data, scanner variance must be quantified and reported, because it exceeded age- and sex-related
  variance for almost all structural features in a large multisite cohort [18]; ComBat removes it and increases power and
  reproducibility when applied correctly [14, 15].
- Harmonisation is not a solved problem for exactly our design: no method (there including ComBat and LongComBat)
  successfully harmonised a *longitudinal* dataset with scanner change within subject [17]; longComBat is validated for
  cross-sectional and longitudinal use on travelling subjects [16], so our longitudinal ComBat claims need an explicit
  within-subject scanner-change sensitivity analysis.
- QC must be reported as a quantitative, pre-specified gate and then handled in the model: the Euler number tracks manual
  quality ratings and detects "unusable" images with AUC 0.98-0.99 [11], automated QC generalises to unseen sites only at
  ~76% accuracy and remains susceptible to site effects [13], and thresholding by QC score attenuates but does not
  eliminate the bias quality induces on cortical estimates [12].
- Where rating or visual reading is involved, blinding/calibration and agreement statistics belong in the methods:
  multisite expert readers reached only substantial (not perfect) agreement (Fleiss' kappa 0.70-0.87), with calibration
  necessary for comparability [10].
- Lesion handling must be reported as a method, not a footnote: lesion filling improved the power to detect atrophy and
  ventricular growth and reduced the required sample size by ~25% [19]; SynthSeg's value is precisely that it generalises
  without retraining, which must be stated together with the version used [20].
- Multiple comparisons across many regions need a pre-specified correction: permutation inference for the GLM gives exact
  false-positive control under exchangeability [21]; the correction family and the number of tested regions must be
  reported [1, 3].

### Practical recommendation (as written for a multisite longitudinal stroke cohort)
Two-column checklist: what to report, and what our cohort must document concretely.

| # | Item | Source | What our cohort must document |
|---|------|--------|-------------------------------|
| 1 | Study design / cohort checklist | STROBE [5, 6] | Prospective cohort, eligibility, recruitment, visit windows for 0/6/36/60 months, flow diagram with attrition per visit and per site |
| 2 | Imaging acquisition reporting (COBIDAS) | [1, 2, 3] | MPRAGE 1 mm parameters, the exact sequence per site, all Siemens models by site, field strength, coil, protocol deviations, scan dates |
| 3 | Preprocessing reporting | [1, 2, 3] | SynthSeg 2 / FreeSurfer 8.2, exact flags (`--robust --qc`), cross-sectional per-session processing (state explicitly that no longitudinal stream was used), recon-all for thickness, container/image digest |
| 4 | Software version freezing | [1, 2, 4, 20] | Frozen versions and container hashes for segmentation, recon-all, QC gate, lesion filling, harmonisation and model code; repository DOI |
| 5 | Lesion filling as a method | [19, 20] | Infarct filling by contralateral mirroring and WMH filling with NAWM intensity described operationally; which analysis is primary (raw vs filled); agreement/validation of the filled images |
| 6 | SVD terminology | STRIVE-2 [8] | WMH and atrophy defined in STRIVE-2 terms; acknowledge that WMH delineation conventionally uses FLAIR and that a T1-only cohort limits WMH quantification |
| 7 | QC metric and gate | [11, 12, 13] | SynthSeg per-structure QC >= 0.65 and Euler-number gate defined a priori, per-site and per-structure counts excluded, and the gate applied before any model fit |
| 8 | QC beyond the gate | [12, 13] | Sensitivity analysis with QC score as covariate; per-site QC distributions; statement that automated QC generalises imperfectly to new sites |
| 9 | Blinding / rating independence | [10] | QC and any manual lesion editing blind to group, visit and site; if any manual step remains: rater training, number of raters, inter-rater agreement |
| 10 | Statistical model | [15, 22] | Linear mixed models fully specified (fixed effects, random intercepts/slopes, time metric, covariance structure), and explicit separation of between- and within-subject effects |
| 11 | Multiple comparisons | [1, 3, 21] | Pre-specified region family, correction method (e.g. permutation with `randomise`), one-/two-sided, and the number of tested structures |
| 12 | Pre-registration / analysis plan | [7, 22] | Dated analysis plan before analysis (OSF/registered report): hypotheses, region set, primary outcome, covariates, correction, sensitivity/multiverse analyses |
| 13 | Multisite harmonisation | [14, 15, 16, 17, 18] | longComBat specification (batch = site/scanner, covariates, time); pre-harmonisation scanner-variance quantification; a within-subject scanner-change sensitivity analysis because longitudinal harmonisation failed in direct comparison |
| 14 | Missing data / attrition | [5, 6] | Missingness pattern at 36/60 months (death, dropout, scanner change), assumed mechanism, and the model's handling of it |
| 15 | Robustness of the segmentation tool | [20] | Statement that SynthSeg generalises across contrast/resolution without retraining, plus the version actually used and its QC behaviour in our data |
| 16 | Data and code sharing | [1, 2, 4] | Sharing statement: derived data, analysis code, container, and what cannot be shared (patient-level imaging) and why |

Priorities if reviewers force cuts: items 3, 4, 7, 12 and 13 are the ones most often missing in comparable papers and
the ones a methods-aware reviewer will check first [3, 4, 12, 17].

## Trägt
22 references, each retrieved in the task with the literature tool and checked (PMID matches title, DOI registered at doi.org). Each reference carries one "Shows:" sentence from its abstract.

[1] Nichols TE, Das S, Eickhoff SB, et al. (2017). Best practices in data analysis and sharing in neuroimaging using MRI. Nature Neuroscience. DOI 10.1038/nn.4500. PMID 28230846.
Shows: the OHBM best-practice (COBIDAS) recommendations for MRI data analysis, results reporting and algorithm/data sharing, and the discipline-level barriers to them — cited as the primary structural-MRI reporting standard for our analysis and sharing section.

[2] Pernet C, Garrido MI, Gramfort A, et al. (2020). Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. Nature Neuroscience. DOI 10.1038/s41593-020-00709-0. PMID 32958924.
Shows: the OHBM COBIDAS committee's "living" recommendations covering acquisition, analysis, reporting and sharing of data and analysis code — cited because it defines the current OHBM expectation that code and analysis choices are reported, not only results.

[3] Acar F, Maumet C, Heuten T, et al. (2023). Review Paper: Reporting Practices for Task fMRI Studies. Neuroinformatics. DOI 10.1007/s12021-022-09606-2. PMID 36199009.
Shows: a review of 160 papers finding that reporting styles for methods and results differ greatly and that results reporting needed a dedicated audit beyond the earlier methods-only reviews based on the 2008 guidelines — cited as the empirical evidence that guideline adherence, not analysis quality, is the common failure point.

[4] Ekhtiari H, Zare-Bidoky M, Sangchooli A, et al. (2024). Reporting checklists in neuroimaging: promoting transparency, replicability, and reproducibility. Neuropsychopharmacology. DOI 10.1038/s41386-024-01973-5. PMID 39242922.
Shows: lack of transparency, reproducibility and reliability remains a significant obstacle in neuroimaging; the review defines what a neuroimaging reporting checklist is, the core values that should inform its design (transparency, repeatability, data sharing), and a development cycle — cited for the checklist rationale and for what current checklists still fail to achieve.

[5] Vandenbroucke JP, von Elm E, Altman DG, et al. (2014). Strengthening the Reporting of Observational Studies in Epidemiology (STROBE): explanation and elaboration. International Journal of Surgery. DOI 10.1016/j.ijsu.2014.07.014. PMID 25046751.
Shows: the rationale and published examples for each of the 22 STROBE items (18 common to cohort/case-control/cross-sectional, 4 design-specific) plus flow-diagram templates, aimed at improving reporting of observational studies — cited as our design-level reporting backbone.

[6] Cuschieri S (2019). The STROBE guidelines. Saudi Journal of Anaesthesia. DOI 10.4103/sja.SJA_543_18. PMID 30930717.
Shows: STROBE consists of 22 checklist items to be fulfilled before submission and is a reporting aid for authors, explicitly not a validation tool for study conduct or a design framework — cited to justify pairing STROBE with an imaging guideline rather than treating it as sufficient.

[7] Nosek BA, Ebersole CR, DeHaven AC, et al. (2018). The preregistration revolution. Proceedings of the National Academy of Sciences of the USA. DOI 10.1073/pnas.1708274114. PMID 29531091.
Shows: the distinction between generating hypotheses with existing observations (postdiction) and testing them with new observations (prediction) is conceptually accepted but not respected in practice, motivating preregistration — cited as the basis for requiring a dated analysis plan.

[8] Duering M, Biessels GJ, Brodtmann A, et al. (2023). Neuroimaging standards for research into small vessel disease-advances since 2013. Lancet Neurology. DOI 10.1016/S1474-4422(23)00131-X. PMID 37236211.
Shows: STRIVE-2 updates the 2013 standards for established SVD markers and new sequences/features, and highlights a key role for quantitative imaging biomarkers of sub-visible tissue damage as intermediary outcomes — cited as the standardised terminology and the licence/obligation for our quantitative WMH and atrophy markers.

[9] Liew SL, Zavaliangos-Petropulu A, Jahanshad N, et al. (2022). The ENIGMA Stroke Recovery Working Group: Big data neuroimaging to study brain-behavior relationships after stroke. Human Brain Mapping. DOI 10.1002/hbm.25015. PMID 32310331.
Shows: the working group's neuroinformatics protocols for managing multisite stroke brain MRI, behavioural and demographic data (data intake, preprocessing, data handling) across over 2,100 patients from 39 research studies in 10 countries — cited as the stroke-specific template for how a multisite stroke cohort documents its intake and preprocessing.

[10] Soleimani-Meigooni DN, Pezzoli S, Blazhenets G, et al. (2025). Calibration of multisite raters for prospective visual reads of amyloid PET scans. Alzheimer's & Dementia. DOI 10.1002/alz.70732. PMID 41030129.
Shows: ten experts from eight centres reading 180 scans reached substantial inter-rater agreement (Fleiss' kappa 0.78 overall, 0.70-0.87 across tracers, full consensus on 69%), with lower agreement for intermediate-signal scans, and the calibration set becomes a training standard — cited as evidence that multisite rating requires documented calibration, reliability and reader blinding.

[11] Rosen AFG, Roalf DR, Ruparel K, et al. (2018). Quantitative assessment of structural image quality. Neuroimage. DOI 10.1016/j.neuroimage.2017.12.059. PMID 29278774.
Shows: the FreeSurfer Euler number correlated with manual quality ratings across samples and identified images rated unusable with high accuracy (AUC 0.98-0.99), and quality was related to cortical thickness and biased age associations — cited as the justification for a quantitative Euler-number gate and for controlling quality in the model.

[12] Bedford SA, Ortiz-Rosa A, Schabdach JM, et al. (2023). The impact of quality control on cortical morphometry comparisons in autism. Imaging Neuroscience. DOI 10.1162/imag_a_00022. PMID 38495338.
Shows: thresholding by QC score attenuated but did not eliminate the impact of image quality on cortical estimates, and inadequate control for quality altered case-control comparison results — cited to show that a QC gate alone is insufficient and quality must also enter the analysis.

[13] Esteban O, Birman D, Schaer M, et al. (2017). MRIQC: Advancing the automatic prediction of image quality in MRI from unseen sites. PLoS One. DOI 10.1371/journal.pone.0184661. PMID 28945803.
Shows: MRIQC's accept/exclude classifier reached about 76% accuracy on new sites and on a held-out dataset, while remaining susceptible to site effects and unable to account for artifacts specific to new sites — cited to require per-site QC reporting rather than a single pooled QC statistic.

[14] Fortin JP, Cullen N, Sheline YI, et al. (2018). Harmonization of cortical thickness measurements across scanners and sites. Neuroimage. DOI 10.1016/j.neuroimage.2017.11.024. PMID 29155184.
Shows: in two multi-site studies across 11 scanners, scanner effects biased cortical thickness analyses, and ComBat removed the unwanted scan variability while increasing the power and reproducibility of subsequent analyses — cited as the primary reference for ComBat harmonisation of structural measures.

[15] Sun D, Rakesh G, Haswell CC, et al. (2022). A comparison of methods to harmonize cortical thickness measurements across scanners and sites. Neuroimage. DOI 10.1016/j.neuroimage.2022.119509. PMID 35917919.
Shows: comparing site-random-intercept LME, LME with random slopes, ComBat and ComBat-GAM on cortical thickness from 29 sites, ComBat-GAM was most sensitive for case-control differences and age-related thinning, and ComBat/ComBat-GAM outperformed LME methods for sex effects — cited to justify ComBat-GAM for non-linear site effects and to require stating which harmonisation was used and why.

[16] Richter S, Winzeck S, Correia MM, et al. (2022). Validation of cross-sectional and longitudinal ComBat harmonization methods for magnetic resonance imaging data on a travelling subject cohort. Neuroimage: Reports. DOI 10.1016/j.ynirp.2022.100136. PMID 36507071.
Shows: ComBat harmonisation methods were validated for cross-sectional and longitudinal use on a travelling-subject cohort, addressing the need created by multicentre studies with hardware and protocol differences — cited as the validation basis for the planned longComBat step.

[17] Gebre RK, Senjem ML, Raghavan S, et al. (2023). Cross-scanner harmonization methods for structural MRI may need further work: A comparison study. Neuroimage. DOI 10.1016/j.neuroimage.2023.119912. PMID 36731814.
Shows: comparing deep-learning, histogram-matching and statistical (ComBat, LongComBat) harmonisation on participants scanned on GE and Siemens scanners, over-/under-estimation of cortical thickness followed scanner change and none of the methods succeeded on the longitudinal dataset, with region-dependent performance — cited as the decisive caveat forcing a within-subject scanner-change sensitivity analysis.

[18] Dudley JA, Maloney TC, Simon JO, et al. (2023). ABCD_Harmonizer: An Open-source Tool for Mapping and Controlling for Scanner Induced Variance in the Adolescent Brain Cognitive Development Study. Neuroinformatics. DOI 10.1007/s12021-023-09624-8. PMID 36940062.
Shows: scanner-induced variance was present in every image feature and for almost all features exceeded variance attributable to age and sex, ComBat removed it while preserving biological variability, and ComBat-harmonised data gave more accurate effect-size estimates than ordinary least-squares control for scanner in subsamples — cited to require quantifying and reporting scanner variance in our 7-site cohort.

[19] Guizard N, Nakamura K, Coupé P, et al. (2015). Non-Local Means Inpainting of MS Lesions in Longitudinal Image Processing. Frontiers in Neuroscience. DOI 10.3389/fnins.2015.00456. PMID 26696815.
Shows: a patch-based non-local-means lesion-filling method outperformed FSL lesion fill, Lesion-LEAP and simple masking or NAWM-intensity filling in reproducing healthy images, and improved the power to detect brain atrophy or ventricular growth, reducing the required sample size by 25% — cited as the quantitative justification for our lesion-filled T1 analysis and for reporting the filling method in detail.

[20] Billot B, Greve DN, Puonti O, et al. (2023). SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining. Medical Image Analysis. DOI 10.1016/j.media.2023.102789. PMID 36857946.
Shows: SynthSeg segments scans of widely varying contrast and resolution without retraining or fine-tuning by training on randomised synthetic data, and generalised to 5,000 scans of six modalities and ten resolutions — cited as the basis for using SynthSeg across our scanner models and as the robustness statement to include with the frozen version.

[21] Winkler AM, Ridgway GR, Webster MA, et al. (2014). Permutation inference for the general linear model. Neuroimage. DOI 10.1016/j.neuroimage.2014.01.060. PMID 24530839.
Shows: a generic permutation framework for complex GLMs with exchangeable and/or symmetric errors gives excellent false-positive control in common imaging scenarios even with nuisance variables, and provides the complete `randomise` algorithm — cited as the pre-specifiable multiple-comparison strategy for our region family.

[22] Botvinik-Nezer R, Holzmeister F, Camerer CF, et al. (2020). Variability in the analysis of a single neuroimaging dataset by many teams. Nature. DOI 10.1038/s41586-020-2314-9. PMID 32483374.
Shows: 70 independent teams analysing the same dataset against the same 9 ex-ante hypotheses chose no two identical workflows and produced sizeable variation in hypothesis-test results, leading the authors to recommend validating and sharing workflows and reporting multiple analyses — cited as the empirical argument for a pre-specified analysis plan plus sensitivity/multiverse analyses.

## Trägt nicht
Open questions from the report:

- Longitudinal harmonisation is unresolved: no tested method (incl. LongComBat) harmonised a dataset with scanner change
  within subject [17], while longComBat is validated on travelling subjects [16]; how large is our within-subject scanner
  change and does it survive as a sensitivity analysis?
- STRIVE-2 endorses quantitative imaging biomarkers [8], but its WMH guidance assumes FLAIR; what is the defensible
  T1-only WMH statement for a stroke cohort?
- Does a SynthSeg QC >= 0.65 gate need site-specific recalibration, given that automated QC classifiers reach only ~76%
  accuracy on unseen sites [13]?
- The prevalence of pre-registration in structural-MRI cohorts is itself unmeasured here (no retrieved abstract reports
  it) — "commonly missing" for pre-registration rests on the multiverse evidence [22] and the preregistration paper [7],
  not on an imaging-specific audit; marked as unverified for our field.
- Whether lesion filling should be primary or a sensitivity analysis in a cohort where infarcts are the exposure, not
  noise, is not answered by the retrieved lesion-filling evidence [19].
- Optimal handling of quality as covariate vs gate: thresholding attenuates but does not remove bias [12]; the best
  specification for a longitudinal mixed model is not settled by the retrieved literature.

Claims rest on abstracts, not full texts, unless the report says otherwise.

## Bruchindikator
A full-text reading or a later consensus paper contradicts a cited effect size or recommendation; or our own cohort data show the opposite (for example no scanner effect at a scanner change).

## Ablesung
Report written 2026-10-18 by Clara (hospital model hub), question set by Claude Code after a pipeline audit; sources verified with quellen-pruefen the same day.
