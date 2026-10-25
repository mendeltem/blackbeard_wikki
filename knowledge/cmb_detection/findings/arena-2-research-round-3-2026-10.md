---
id: arena-2-research-round-3-2026-10
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-25
herkunft: Claude Code (Alita) 2026-10-25, eleven narrowly scoped literature agents (R1-R11) on the open questions of Arena 2, IDs re-fetched by script (Semantic Scholar / arXiv abs pages, Crossref, DataCite, PubMed E-utilities); numbers marked as the agents' own simulation or calculation where they are not from a source
verweist_auf: [search-space-expansion-and-novel-hybrids-2026-10, two-seeds-per-decision-below-0.08, report-healthy-controls-separately]
---

# Arena 2, research round 3: decisions, labels, data, priors, fusion, operating points (2026-10)

Naming (user, 2026-10-25): **Arena 1** = the U-Net tournaments and the earlier stage-2 tests; **Arena 2** = the new hybrid
models (TrackSet-CMB stage 2, independent candidate source, physics renderer) and everything measured from now on.

## Aussage

**1. Decision rules (R2): the first rules would have let a null arm through about every fifth time -- fixed before any run.**
A simulation of 10 null arms against one shared control gave a family-wise false-KEEP rate of 17-23 % (agents' simulation): one
bootstrap per arm, seed variance missing from the interval, a 2-df threshold, no multiplicity. Rules v2 (in code): one bootstrap
per draw shared by all arms and stratified by cohort, max-T (Dunnett-type) simultaneous lower bound at a family-wise 10 %, seed
variance in the interval (pooled, floor 0.009), margin +0.01 on all cohorts, shrunk deltas against the winner's curse, and the
word 'carry to confirmation' instead of 'keep': the survivor is tested once on cases never used (the external public SWI set). On
40 simulated all-null runs v2 carried no arm; a true +0.02 arm is confirmed only rarely with ~190 scans -- this arena can select,
not confirm small gains.

**2. Hyperparameter search (R1).** Only one Bayesian search ever ran (Arena 1, one fold, short runs). Stage 1: not worth it --
with a seed sd of 0.08 the best of 30 trials looks about +0.16 better from noise alone (agents' calculation). Stage 2: worth it
after the arm decision: ~40 TPE trials, one seed each, pruning on folds not epochs, top 5 + default re-run with three new seeds
and new fold assignment, final estimate on an untouched outer fold; tuning and reporting on the same CV is optimistic [1].

**3. Labels are a lever of unknown size (R6).** Single readers find 39-88 % of a four-reader CMB consensus [2]; with a reference
that holds a share s of the true lesions a perfect detector scores at most F1 = 2s / (1 + s) (no false labels), i.e. 0.58-0.94 for
s = 0.41-0.88 -- our 'perfect stage 2' ceiling of 0.85 lies inside that band. How many audited 'false positives' are real ranged
from 2.6 % [2] to 54 % (LUNA16 pooled FPs) and must be measured: about 650 blinded reads in six strata, two readers plus an
adjudicator, symmetric re-scoring of all arms with inclusion-probability weights. Cheap stage-2 use: relabel-and-ignore, nnPU loss
with the audited prior.

**4. Synthetic insertion (R3).** Precedent: FDA nodule insertion into whole CT exams, readers told inserted from real nodules with
AUC 0.52-0.71 [3]. Insertion helps most with little data (CarveMix +4.5 Dice at 100 %, +12.9 at 12.5 % of the data [4]); no study
compares patch- with volume-level insertion, so run volume-level with stage 1 frozen plus a crop-only ablation. Realism gate:
classifier two-sample test on candidate crops WITH a known-bad positive control, not FID. Do not insert calcifications as negatives:
on magnitude they equal a microbleed of the same moment; vein mimics are the negative class.

**5. Data (R4).** No new labelled CMB data appeared 2025-2026. Most useful new resource: QTAB (OpenNeuro ds004146, CC0) with
magnitude, phase, SWI and minIP per session at 3 T [5,6] -- for a T2* -> pseudo-SWI model and insertion into real complex data.
UK Biobank swMRI (0.8 x 0.8 x 3 mm, magnitude + phase, tens of thousands of participants) needs an application [7].

**6. Vein priors (R5).** Venous atlases in MNI space exist (Bernier 2018 from 3 T SWI [8], Ward 2018 [9], Huck 2019 from 7 T QSM
[10]); no public vein segmenter for SWI/T2* magnitude was found. Cheapest test: 3-5 atlas and SynthSeg-geometry values at the
candidate as stage-2 features after a contrast-agnostic registration (SynthMorph [11]); first a 30-minute AUC check; learned
feature only, never a hard rule.

**7. Clinical targets (R7).** The only regulator-reviewed tool with public numbers: icobrain aria (510(k) K240712, 2D FLAIR + 2D
T2*-GRE), lesion TPR 66.1 % at 0.9 FP per case [12]. Decisions turn at 0/1, 1/2, 4/5 and 9/10 microhaemorrhages (anti-amyloid
eligibility and ARIA-H severity), Boston criteria 2.0 count lobar lesions [13]. Report FROC at 0.5/1/2 FP per scan, category
agreement per patient and count error by count bin, T2* and SWI separately.

**8. Fusion (R8).** LUNA16 is our chain one step further: the union of five candidate generators raised candidate sensitivity
92.9 -> 98.3 % and averaging five FP-reduction networks on the SHARED candidate list raised CPM 0.908 -> 0.952 [14]. Our union of
seeds raised the ceiling but not F1 because stage 2 was not trained on the union and only one scorer was used. Recipe: union list,
the vote count (how many stage-1 runs found the object) as a feature, several stage-2 arms averaged in logit space, one temperature
on out-of-fold scores; members must be independent pipelines, not seeds.

**9. Spatial priors (R9).** CMB prevalence 17.8 % (60-69 y) to 38.3 % (> 80 y); strictly lobar CMB go with APOE e4, deep and
infratentorial with vascular risk [15]; CAA bleeds favour temporal and occipital lobes [16]. A brain-edge rule removes most
edge false positives but costs true positives -- distance to the edge belongs into stage 2 as a learned feature.

**10. Operating points (R10).** For a calibrated score the F1-optimal threshold is half the best attainable F1 [17], so an optimum
near 0.3 is expected and the 'hotter' full-data model is a calibration shift. Recipe for a new site: 0 scans -- frozen point plus
an alarm when detections per scan leave the development range; 5 scans -- one logit offset shrunk to the development value; 20 scans
-- two-parameter calibration, optional conformal control of the miss fraction [18]. Report frozen, site-calibrated and oracle rows.

**11. Challenge winners 2022-2026 (R11).** No exotic component won: nnU-Net-type networks, Dice + CE, five-fold ensembles,
domain-specific preprocessing; ISLES'22 top-3 recipes combined by a 2-of-3 vote beat each single winner [19]; ISLES'24 won on
per-modality intensity windowing [20]. Untried here: cross-family vote, the open nnU-Net v2 evaluation, out-of-fold audited
post-processing rules, an auxiliary anatomy head, a T2*-specific intensity window.

## Nachtrag 2026-10-25: Arena-2 tools built (tested on synthetic data and a template probe; nothing measured on patients yet)

- **Confirmation path:** the one arm that 'carries' is trained on the whole pool, its threshold chosen by 5-fold CV over the pool,
  and applied unchanged to the external public SWI set (never in the pools); one paired test, one-sided 2.5 %, fixed in advance.
- **New stage-2 inputs:** the vote count (how many stage-1 runs found the object [14]) and the distance to the brain edge as
  learned features; venous-atlas values (vein frequency at the candidate, maximum within 3 mm, distance to the nearest frequent vein)
  from the 3 T SWI atlas of 41 adults [8], carried onto each scan by a contrast-agnostic registration [11].
- **Registration finding (probe without patient data):** carrying an atlas with SynthMorph's apply step onto a scan works only if
  the atlas is first resampled onto the grid of the image that was registered. On a template-derived probe on our 0.5 x 0.5 x 1 mm
  grid the direct way gave a correlation of -0.02 with the true atlas position (Dice 0.02), the resampled way 0.917 (Dice 0.78);
  the registration itself was fine (template correlation 0.961). FreeSurfer 8.2.0, mri_synthmorph register -m joint.
- **Synthetic insertion into whole volumes:** physics-rendered microbleeds (labelled with their apparent extent) and vein segments
  at random angles to B0 (no label, signal loss fading over the last 4 mm), placed outside CSF, >= 8 mm from lesions and each other,
  70 / 12 / 18 % lobar / deep / infratentorial [15]; no calcifications (same magnitude image as a bleed); a bleed too faint to outline
  is not written at all; FRST recomputed on the modified volume; the stage-1 map of each copy only from the U-Net of its own fold
  (four of five fold models had seen the host); only candidates at inserted objects become training-only extras.
- **Realism gate (classifier two-sample test, fixed in advance):** pass if real-vs-inserted AUC <= 0.70 for bleeds and for veins and
  a known-bad fake (smoothed image channel) is caught with AUC >= 0.85; on synthetic data the same generator gave AUC 0.50 and the
  fake 1.0. Inserted candidates train stage 2 only after a pass.

## Trägt
IDs re-fetched by script 2026-10-25 with matching titles. Numbers come from the cited abstracts or full texts as read by the agents;
simulation results (points 1-2) are the agents' own, from scripts on synthetic data. The v2 rules are implemented and tested on
synthetic arms (two real arms carry, eight null arms do not).

## Trägt nicht
Most sources were read at abstract level; regulator numbers come from a third-party mirror of the FDA summaries. The label-audit
sizes, realism thresholds and threshold recipe are proposals derived from the sources, not validated on our data. No source
measures any of this on CMB except points 3, 7 and 9.

## Bruchindikator
A first Arena-2 screening run whose case-bootstrap SE differs strongly from the assumed 0.01-0.02; an audit yield near 0 or above
0.5; a realism test that cannot tell even the known-bad fake from real crops.

## Ablesung
[1] Cawley GC, Talbot NLC. 2010. On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation. J Mach Learn Res 11:2079-2107 (no DOI). Shows: non-nested tuning and reporting is optimistic by 0.02-1.19 percentage points.
[2] Kuijf HJ et al. 2013. Semi-automated detection of cerebral microbleeds on 3.0 T MR images. PLoS One 8:e66610. DOI 10.1371/journal.pone.0066610. PMID 23805246. Shows: single readers find 39-88 % of a four-reader consensus; few candidate-derived CMBs added after review.
[3] Pezeshk A et al. 2015. Seamless Insertion of Pulmonary Nodules in Chest CT Images. IEEE Trans Biomed Eng 62:2812-2827. DOI 10.1109/TBME.2015.2445054. PMID 26080378. Shows: nodules blended into whole CT exams; reader AUC 0.52-0.71 for telling inserted from real.
[4] Zhang X et al. 2021. CarveMix: a simple data augmentation method for brain lesion segmentation. MICCAI. arXiv 2108.06883. Shows: +4.5 Dice at full data, +12.9 at 12.5 %.
[5] Strike LT et al. 2023. The Queensland Twin Adolescent Brain Project, a longitudinal study of adolescent brain development. Scientific Data. DOI 10.1038/s41597-023-02038-w. Shows: 3 T SWI with magnitude, phase and minIP outputs.
[6] OpenNeuro ds004146 (QTAB). DOI 10.18112/openneuro.ds004146.v1.0.0. Shows: CC0 release; per session minIP, magnitude, phase and SWI.
[7] Wang C et al. 2022. Phenotypic and genetic associations of quantitative magnetic susceptibility in UK Biobank brain imaging. Nature Neuroscience. DOI 10.1038/s41593-022-01074-w. PMID 35606419. Shows: UK Biobank swMRI 0.8 x 0.8 x 3 mm, two echoes, magnitude and phase.
[8] Bernier M et al. 2018. The morphology of the human cerebrovascular system. Human Brain Mapping. DOI 10.1002/hbm.24337. Shows: venous and arterial atlases from 3 T SWI/TOF in MNI space.
[9] Ward PGD et al. 2018. Combining images and anatomical knowledge to improve automated vein segmentation in MRI. NeuroImage. DOI 10.1016/j.neuroimage.2017.10.049. Shows: a vein atlas improves vein segmentation.
[10] Huck J et al. 2019. High resolution atlas of the venous brain vasculature from 7 T quantitative susceptibility maps. Brain Structure and Function. DOI 10.1007/s00429-019-01919-4. Shows: MNI venous atlas at 0.5 mm.
[11] Hoffmann M et al. 2020. SynthMorph: learning contrast-invariant registration without acquired images. arXiv 2004.10282. Shows: registration that works across contrasts without T1.
[12] icometrix NV / FDA. 2024. 510(k) K240712, icobrain aria (decision summary via a third-party mirror). Shows: 66.1 % lesion TPR at 0.9 FP per case on 2D T2*-GRE + FLAIR; reader study endpoint.
[13] Charidimou A et al. 2022. The Boston criteria version 2.0 for cerebral amyloid angiopathy: a multicentre, retrospective, MRI-neuropathology diagnostic accuracy study. Lancet Neurology. DOI 10.1016/S1474-4422(22)00208-3. Shows: lobar haemorrhagic lesion counts in the CAA criteria.
[14] Setio AAA et al. 2017. Validation, comparison, and combination of algorithms for automatic detection of pulmonary nodules in computed tomography images: the LUNA16 challenge. Medical Image Analysis. arXiv 1612.08012. Shows: union of candidate generators and averaging of FP-reduction systems.
[15] Vernooij MW et al. 2008. Prevalence and risk factors of cerebral microbleeds: the Rotterdam Scan Study. Neurology. DOI 10.1212/01.wnl.0000307750.41970.d9. PMID 18378884. Shows: prevalence by age; lobar vs deep risk profiles.
[16] Rosand J et al. 2005. Spatial clustering of hemorrhages in probable cerebral amyloid angiopathy. Annals of Neurology. DOI 10.1002/ana.20596. PMID 16130107. Shows: temporal and occipital predominance, clustering within persons.
[17] Lipton ZC et al. 2014. Thresholding classifiers to maximize F1 score. ECML PKDD. arXiv 1402.1892. Shows: F1-optimal threshold of a calibrated classifier is half the best F1.
[18] Angelopoulos AN et al. 2022. Conformal risk control. arXiv 2208.02814. Shows: finite-sample control of any monotone risk on exchangeable calibration data.
[19] de la Rosa E et al. 2024. A Robust Ensemble Algorithm for Ischemic Stroke Lesion Segmentation: Generalizability and Clinical Utility Beyond the ISLES Challenge. arXiv 2403.19425. Shows: a vote of the ISLES'22 top-3 recipes beats each single one.
[20] Ren T et al. 2025. How We Won the ISLES'24 Challenge by Preprocessing. arXiv 2505.18424. Shows: per-modality intensity windowing raised CV Dice 0.218 -> 0.310.
Agent notes with all sources (R1-R11, about 200 entries) stay outside the wiki.
