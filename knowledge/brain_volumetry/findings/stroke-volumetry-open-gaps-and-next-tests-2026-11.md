---
id: stroke-volumetry-open-gaps-and-next-tests-2026-11
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-11-06
herkunft: literature research 06.11.2026 (four focused searches, 108 sources checked by the agents, 13 PMIDs re-checked by hand, all correct), for a multi-site longitudinal stroke cohort with SynthSeg 2.0 on clinical T1
verweist_auf: [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort, icv-scaling-exponent-and-asymmetry-noise]
---

# Stroke volumetry: what the literature still lacks, and the next tests (Nov 2026)

## Aussage
Four questions that block a longitudinal stroke volumetry study have **no published answer**: (1) a lesion-size limit for mirror
(enantiomorphic) filling, or any stroke validation of filling/inpainting for regional volumes [1-4]; (2) the fail rate of the SynthSeg+
cortex QC on routine clinical T1 [5]; (3) the ipsilateral-minus-contralateral thalamus change in %/year [6-8]; (4) a longitudinal
validation of any segmentation pipeline in stroke; SynthSeg has no longitudinal stream [9-11]. Own runs must fill these gaps.

Facts that change the reading of own results:
- The SynthSeg+ QC regressor reads only the **label map**, not the image; it predicts Dice for 10 regions and was validated as whole-scan
  pass/fail, not near the 0.65 cut-off and not on pathology [5]. A low cortex score is a flag, not proof of a wrong cortex. In the own
  clinical cohort the cortex fail rate is about 24 times that of a healthy MPRAGE reference (DLBS 1.7 %).
- Lesion filling can hurt: virtual-brain-grafting fill lowered FastSurfer parcellation accuracy in brain trauma [2].
- Secondary thalamic atrophy is front-loaded (2-4x faster in months 0-3 than 3-12) and the contralesional thalamus shrinks too [7];
  disconnection predicts remote change better than lesion volume, only in disconnected thalamic nuclei groups [8, 12].
- Longitudinal processing roughly halves reproducibility error across sites and vendors [9]; Longitudinal ComBat keeps type I error
  better than a scanner covariate alone [10].

Next tests, ranked: blind visual rating of ~60 visits against the cortex QC (ROC, fails by sequence/site/contrast agent); mirror fill +
drop touched structures with a measured size cut-off; disconnection score + thalamic nuclei as secondary endpoints; FreeSurfer -long
on 40-60 patients next to SynthSeg, judged by within-person residual SD and slope ICC; change-level QC; SynthSR/FLAIR input only if
the rating shows real errors; piecewise time term in the mixed model.

## Traegt
Abstract-level evidence for every listed fact; own power calculation: asymmetry SEM 1.8 pp (from SDC95 5 pp), so the main effect needs
few complete patients, and subgroups, interactions and informative dropout are the real limits.

## Traegt nicht
Full texts were not read; effect sizes per study come from abstracts. The power numbers rest on an assumed between-patient spread.

## Bruchindikator
A blind rating that agrees with the cortex QC (high AUC) would make the QC-based exclusion correct and the alternative-input tests unnecessary.

## Ablesung
Full notes with all sources: research round folder of the cohort project (00_synthesis.md, 01-04). Own runs: synthetic-lesion test 2026-10-30/11-05, robust size x location test started 2026-11-06.

## Quellen
1. Nachev P et al. 2008, NeuroImage 39:1215-1226, doi 10.1016/j.neuroimage.2007.10.002, PMID 18023365 (enantiomorphic normalisation; not tested for volumetry).
2. Deutscher E et al. 2025, Front Neurol 16:1652385, doi 10.3389/fneur.2025.1652385, PMID 41451415 (VBG filling lowered parcellation accuracy in TBI).
3. Deutscher E et al. 2026, NeuroImage, doi 10.1016/j.neuroimage.2026.121869, PMID 41881175 (scoping review of T1 lesion inpainting in brain injury).
4. Pollak C et al. 2025, Imaging Neurosci, doi 10.1162/imag_a_00446, PMID 40109899 (FastSurfer-LIT; tumours, not stroke).
5. Billot B et al. 2023, PNAS 120:e2216399120, doi 10.1073/pnas.2216399120, PMID 36802420 (SynthSeg+, QC regressor on label maps).
6. Geng J et al. 2022, J Stroke Cerebrovasc Dis, doi 10.1016/j.jstrokecerebrovasdis.2022.106895, PMID 36495644 (ipsilateral thalamus smaller after non-thalamic infarcts, linked to cognition).
7. Brodtmann A et al. 2020, Stroke, doi 10.1161/STROKEAHA.120.030256, PMID 32772680 (atrophy front-loaded in the first year).
8. Koubiyr I et al. 2025, Brain 148:3551-3562, doi 10.1093/brain/awaf082, PMID 40070356 (R2* rise only in disconnected thalamic nuclei groups).
9. Jovicich J et al. 2013, NeuroImage, longitudinal FreeSurfer reproducibility across 8 sites (PMID in the full note).
10. Beer JC et al. 2020, NeuroImage 220:117129, doi 10.1016/j.neuroimage.2020.117129, PMID 32640273 (Longitudinal ComBat).
11. Aamodt EB et al. 2022, Front Neurol 13:856919, doi 10.3389/fneur.2022.856919, PMID 35720079 (Nor-COAST, 36 months, ipsi > contra atrophy, MoCA).
12. Williams B et al. 2022, NeuroImage, doi 10.1016/j.neuroimage.2022.119340, PMID 35649466 (thalamic nuclei atlas validation; weak posteriorly).
