---
id: icv-scaling-exponent-and-asymmetry-sdc-2026-10
typ: befund
status: vorschlag
thema: knowledge/brain_volumetry
stand: 2026-10-30
herkunft: own runs 2026-10-29/30 (DLBS public data; own stroke cohort as relative values), SynthSeg 2.0 --robust in FreeSurfer 8.2.0
verweist_auf: [research-icv-normalisation-and-lesioned-structures-2026-10, research-scanner-change-within-subject-longitudinal-2026-10, one-t1-per-visit-and-tab-columns-by-cut]
---

# Deep grey matter does not scale 1:1 with ICV; asymmetry is the scanner-robust endpoint

## Aussage
1. **ICV scaling exponent (DLBS, healthy, wave 1, MMSE >= 26, n = 464).** In log(volume) = a + b log(ICV) + age + age^2 + sex, cortex b = 0.99 [0.95; 1.02] and total GM b = 0.97 [0.93; 1.00], but deep GM is clearly below 1: thalamus 0.76 [0.68; 0.83], caudate 0.74, putamen 0.81, amygdala 0.84, pallidum 0.85, hippocampus 0.65 [0.56; 0.75]; cerebral WM 1.13. Dividing by ICV therefore over-corrects large heads: with men's ICV about 14 % larger, a man's thalamus fraction is about 3 % (hippocampus 4.5 %) lower from head size alone. Rule: ICV as a covariate (or volume / ICV^b) for deep GM; plain fractions only for cortex and total GM.
2. **Measurement error of a left-right asymmetry (own cohort, same-session repeat T1, QC-passed pairs).** SDC95 of the thalamus asymmetry index is about 5 percentage points, similar to the bilateral thalamus SDC95 (about 5 %); the left pallidum is unstable (SDC95 about 20 %).
3. **A scanner change shifts every volume (about +1 to +2 %, structure-specific, pallidum about twice) but cancels in the asymmetry** (thalamus asymmetry step -0.9 pp, CI includes 0), and adds no extra spread beyond the step.

## Trägt
- Bootstrap CIs over participants (2000 draws); QC-filtered sample (SynthSeg QC >= 0.65) gives the same exponents within 0.01.
- Scanner step confirmed within the sites that changed scanners, not only across sites.
- Fits the literature recommendation of ICV as a covariate over division (see verweist_auf).

## Trägt nicht
- Only 18 QC-passed same-session pairs: the SDC CIs are wide (thalamus asymmetry about 3-6.5 pp).
- Exponents from one scanner model (DLBS, Philips 3T MPRAGE); other scanners not tested.
- The SynthSeg QC score is not a lesion-misclassification detector, so QC-passed does not mean lesion-correct.

## Bruchindikator
- A structure/ICV fraction that still correlates with ICV within sex (r clearly away from 0) is being used for group comparisons.
- Without the QC filter a few failed segmentations dominate the SD (ICV SDC95 rose about 20-fold): use a robust (MAD) SD or the QC filter.

## Ablesung
- DLBS: Dallas Lifespan Brain Study, OpenNeuro ds004856 (CC0), https://openneuro.org/datasets/ds004856 (accessed 2026-10).
- SynthSeg: Billot B et al. 2023, PNAS, DOI 10.1073/pnas.2216399120, PMID 36802420; FreeSurfer 8.2.0, https://surfer.nmr.mgh.harvard.edu.
- SDC definition 1.96 x sqrt(2) x within-subject SD; own runs 2026-10-29 (scaling) and 2026-10-29/30 (SDC, scanner step).

## Verknüpft
- [research-icv-normalisation-and-lesioned-structures-2026-10](research-icv-normalisation-and-lesioned-structures-2026-10.md)
- [research-scanner-change-within-subject-longitudinal-2026-10](research-scanner-change-within-subject-longitudinal-2026-10.md)
- [one-t1-per-visit-and-tab-columns-by-cut](../rules/one-t1-per-visit-and-tab-columns-by-cut.md)
