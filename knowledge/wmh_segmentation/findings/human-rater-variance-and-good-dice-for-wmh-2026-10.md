---
id: human-rater-variance-and-good-dice-for-wmh-2026-10
typ: befund
status: vorschlag
thema: knowledge/wmh_segmentation
stand: 2026-10-25
herkunft: Claude Code (Alita) 2026-10-25, research round 4 (user question "experts make errors -- what is a good Dice?"), literature agents (WMH raters, methodology), IDs re-fetched by script; derived numbers marked as such
verweist_auf: [human-rater-variance-and-good-f1-for-cmb-2026-10]
---

# How much do WMH raters disagree, and what is a good Dice?

## Aussage
- **Human range on FLAIR (with or without T1):** inter-rater Dice 0.70-0.81, typically 0.77-0.80 -- WMH Challenge 2017 two extra
  observers 0.77 / 0.79 with lesion recall 0.65 / 0.66 and lesion F1 0.74 / 0.76 [1]; 0.80 +- 0.09 with a semi-automatic tool [2];
  human-human 0.805 on 50 doubly annotated scans [3]; 0.71 +- 0.11 on 20 blinded volumes [4]; 0.70 between raters and 0.72-0.86
  within raters across three cohorts [5]. Volume agreement is high (ICC 0.97-0.99).
- **Dice depends on load.** Rater-vs-rater Dice 0.51 at <= 5 ml [4]; the same outline error costs far more Dice on a small lesion
  (synthetic: 0.79 at 4-voxel vs 0.975 at 30-voxel diameter, methodology agent's calculation). Report Dice by load class and add
  lesion F1 and volume error; a Dice below ~0.6 on low-load cases is human-like, not a failure.
- **MS lesions as the closest analogue are harder:** inter-rater Dice about 0.60-0.67 [6,7].
- **Automatic methods:** the WMH 2017 winner reached Dice 0.80 and lesion F1 0.76-0.78 -- inside the human band, with the caveat that
  observers were scored on training images and methods on test images [1]; a CNN matched human-human Dice (0.792 vs 0.805) [3];
  off-the-shelf tools reach far less on clinical data (WMH-SynthSeg 0.62 FLAIR [8]; LST/BIANCA/SAMSEG 0.3-0.5 on clinician labels [9]).
- **For our models:** a Dice of ~0.75-0.80 on mixed-load data, or ~0.80-0.85 on high-load scans, is within rater variability;
  claim 'human-level' only with a second rater on the same scans (see the CMB entry for the paired design and sample sizes).

## Trägt
IDs re-fetched by script 2026-10-25; numbers from the cited abstracts or full texts as read by the agent (several via a page
summary -- re-check against the PDF before quoting in a manuscript).

## Trägt nicht
No rater-vs-rater Dice by region (periventricular vs deep) and no recent (2023-2026) independent two-rater WMH study were found;
load-stratified human Dice above 5 ml is inferred, not measured.

## Bruchindikator
A two-rater study on our scanners giving Dice far outside 0.70-0.81.

## Ablesung
[1] Kuijf HJ et al. 2019. Standardized Assessment of Automatic Segmentation of White Matter Hyperintensities and Results of the WMH Segmentation Challenge. IEEE TMI. DOI 10.1109/TMI.2019.2905770. PMID 30908194. Shows: two observers Dice 0.77/0.79, lesion F1 0.74/0.76; winner Dice 0.80.
[2] Heinen R et al. 2019. Scientific Reports. DOI 10.1038/s41598-019-52966-0. PMID 31727919. Shows: inter-rater Dice 0.80 +- 0.09, intra-rater 0.80 +- 0.08.
[3] Ghafoorian M et al. 2017. Scientific Reports. DOI 10.1038/s41598-017-05300-5. PMID 28698556. Shows: human-human Dice 0.805 vs best CNN 0.792.
[4] Khademi A et al. 2021. NeuroImage: Reports. DOI 10.1016/j.ynirp.2021.100044. Shows: two blinded raters Dice 0.71 +- 0.11, 0.51 at <= 5 ml.
[5] Dadar M et al. 2017. NeuroImage. DOI 10.1016/j.neuroimage.2017.06.009. PMID 28602597. Shows: intra-rater Dice 0.72-0.86, inter-rater 0.70, strong load dependence.
[6] Carass A et al. 2017. NeuroImage. DOI 10.1016/j.neuroimage.2016.12.064. PMID 28087490. Shows: ISBI-2015 MS raters Dice 0.634.
[7] Commowick O et al. 2018. Scientific Reports. DOI 10.1038/s41598-018-31911-7. PMID 30209345. Shows: MSSEG seven experts; lowest expert Dice 0.67 vs best method 0.59.
[8] Laso P et al. 2023. arXiv 2312.05119. Shows: WMH-SynthSeg average Dice 0.62 (FLAIR).
[9] Torres-Simon L et al. 2024. GeroScience. DOI 10.1007/s11357-024-01238-5. PMID 38869712. Shows: off-the-shelf tools Dice 0.3-0.5 on clinician labels.
