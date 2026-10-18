---
id: research-first-vs-second-run-volumetry-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-18
herkunft: 16 literature topics on longitudinal post-stroke volumetry, each researched twice and independently by the remote-model agent (Clara on the hospital model hub; first run model "clea", second run model "frontier", second run forbidden to open the first); quellen-pruefen 2026-10-18 on the second runs (512 references, 502 with PMID, 502 correct, 0 wrong, 10 without PMID); recommendation-by-recommendation comparison by a Claude Code subagent, checked and committed by Claude Code
verweist_auf: [research-icv-normalisation-and-lesioned-structures-2026-10, research-scanner-change-within-subject-longitudinal-2026-10, research-cross-sectional-vs-longitudinal-consistency-2026-10, research-attrition-and-missing-data-longitudinal-stroke-2026-10]
---

# Literature, run twice: where two independent research runs on longitudinal post-stroke volumetry agree and disagree

## Aussage
Running every literature question twice, with a different model and no access to the first answer, is cheap and
changes the conclusions in a few decisive places. Agreement across runs marks robust advice; disagreement marks
places where the literature does not decide and own data or an own experiment must.

**Robust (both runs):** a scanner change inside a participant is a directed bias, not noise, and must be modelled with a
time-varying scanner term [1]; ICV enters as a covariate or residual, the ratio only as a sensitivity analysis [2,3];
the longitudinal stream is more precise than per-session segmentation for change; QC is a cascade of cheap gates plus a
human pass on the flagged tail, and outlier exclusion on global volumes increases unexplained variance [4]; mixed
models with random intercept and slope, real time in years, no deletion of incomplete participants.

**Contradictions between runs (the literature does not settle these):**
1. *Mirror (enantiomorphic) filling of infarcts.* Run 1 calls it the best-validated classical family; run 2 finds no
   published volumetric validation at all and recommends against it as a default. Classical WM-intensity filling is
   strongly mask- and method-dependent: with gold-standard masks FSL `lesion_filling` left 24.5 % of the lesion area
   classified as GM versus 0.4 % for LEAP [5]; filling fixes misclassification that masking alone does not [6].
2. *Primary stream raw or filled T1.* Split across topics and runs; the two ICV/lesion runs and the inpainting run 2
   make the raw stream primary and the filled stream a sensitivity analysis.
3. *ICV once per participant or per session.* Run 1: baseline, time-invariant. Run 2: session-specific; the ICV
   estimator itself differs between scanners, segmentation-based TIV is more consistent across scanners [2].
4. *Harmonisation.* One run favours longitudinal ComBat over a scanner covariate [7], another the time-varying scanner
   term in the mixed model [1] and doubts that ComBat removes an effect confounded with time.
5. *Early interval (0-6 months).* Non-linear fast early atrophy (spline terms) versus "mostly measurement error, fit
   slopes on later visits".
6. *WMH tool.* LST-AI is validated on MS lesions only [8]; segcsvdWMH reports the best Dice on heterogeneous ageing/SVD
   cohorts [9].

## Trägt
Second-run references (checked: PMID matches title):

[1] Lee H, Nakamura K, Narayanan S, et al. (2019). Estimating and accounting for the effect of MRI scanner changes on
longitudinal whole-brain volume change measurements. NeuroImage 184:555-565. PMID: 30253207.
Shows: scanner/sequence changes shift whole-brain change measures with a sign; a fixed corrective term per transition
in a mixed model improves fit.

[2] Koike S, Maikusa N, Cai L, et al. (2025). Estimation of the intracranial volume is crucial ... Human Brain Mapping.
doi:10.1002/hbm.70405. PMID: 41190774.
Shows: eTIV and segmentation-based TIV agree only moderately (ICC 0.78) and sbTIV is more consistent across scanners
in longitudinal data.

[3] Brzezinski-Rittner A, Moqadam R, Zeighami Y, Dadar M. (2026). Intracranial volume: To adjust or not to adjust? It
is not a matter of if, but how. Imaging Neuroscience 4. doi:10.1162/imag.a.1235. PMID: 42206219.
Shows: proportional (ratio) correction can invert associations; covariate and residual adjustment agree with a
TIV-matched reference.

[4] Monereo-Sanchez J, de Jong JJA, Drenthen GS, et al. (2021). Quality control strategies for brain MRI segmentation
and parcellation. NeuroImage. doi:10.1016/j.neuroimage.2021.118174. PMID: 34000406.
Shows: Euler number and MRIQC-based exclusion perform best among automated options; excluding outliers on global
morphological measures increased relative unexplained variance.

[5] Popescu V, Ran NC, Barkhof F, et al. (2014). Accurate GM atrophy quantification in MS using lesion-filling with
co-registered 2D lesion masks. NeuroImage: Clinical. doi:10.1016/j.nicl.2014.01.004. PMID: 24567908.
Shows: with gold-standard masks LEAP left 0.4 % of the lesion area as GM, FSL lesion_filling 24.5 %.

[6] Battaglini M, Jenkinson M, De Stefano N. (2012). Evaluating and reducing the impact of white matter lesions on brain
volume measurements. Human Brain Mapping. doi:10.1002/hbm.21344. PMID: 21882300.
Shows: inserted WM lesions caused GM/WM misclassification that persisted when lesions were masked and was removed by
filling with normal-appearing WM intensity.

[7] Beer JC, Tustison NJ, Cook PA, et al. (2020). Longitudinal ComBat: a method for harmonizing longitudinal
multi-scanner imaging data. NeuroImage. doi:10.1016/j.neuroimage.2020.117129. PMID: 32640273.
Shows: longitudinal ComBat was more powerful for longitudinal change and controlled type I error better than
cross-sectional ComBat.

[8] Wiltgen T, McGinnis J, Schlaeger S, et al. (2024). LST-AI: a deep learning ensemble for accurate MS lesion
segmentation. NeuroImage: Clinical 42. doi:10.1016/j.nicl.2024.103611. PMID: 38703470.
Shows: three-U-Net ensemble beat LST, SAMSEG and nnU-Net on MS data (Dice 0.65 on MSSEG-1).

[9] Gibson E, Ramirez J, Woods LA, et al. (2024). segcsvdWMH: a CNN-based tool for quantifying white matter
hyperintensities in heterogeneous patient cohorts. Human Brain Mapping 45. doi:10.1002/hbm.70104. PMID: 39723488.
Shows: mean Dice 0.86 across four heterogeneous datasets, +7.8 % over HyperMapp3r and +21.8 % over SAMSEG.

Own data (2026-10-18, cohort-level, relative values only): within the same site, participants who changed scanner
show a global scale step of about +1.5 % in every volume including the ICV proxy, which vanishes when each volume is
divided by the same-session ICV; this argues for a per-session ICV in this cohort (contradiction 3).

## Trägt nicht
- No run found a volumetric validation of mirror filling; absence in two searches is not proof of absence.
- The comparison read the short-answer and recommendation sections, not every paragraph.
- 10 second-run references carry only a DOI and were not checked by PMID.

## Bruchindikator
- A published validation of enantiomorphic filling for structure volumes, or an own simulation (synthetic lesions in a
  healthy hemisphere, filled vs original volume per structure) that shows a bias below the smallest detectable change.
- Own data in which raw and filled streams give the same slopes per structure.

## Ablesung
For any methods decision: do it where both runs agree; where they disagree, decide by own data (measured step, test-
retest SDC) or by a small own experiment, and record the decision with both positions in the analysis plan.
