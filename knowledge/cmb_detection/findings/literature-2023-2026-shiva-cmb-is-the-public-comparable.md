---
id: literature-2023-2026-shiva-cmb-is-the-public-comparable
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-17
herkunft: Literature review d_cmb_detection (PubMed E-utilities + Europe PMC, 37 retrieved records), report /home/uchralt/cle-arbeit/recherche/d_cmb_detection/REPORT.md, 2026-10-17
verweist_auf: [fine-tune-from-public-valdo-weights, second-stage-classifier-ported-reproduced, sensitivity-levers-do-not-raise-lesion-f1, csf-rule-removes-false-alarms-without-loss]
---

# CMB detection 2023-2026: SHIVA-CMB is the public comparable, mimics drive precision, foundation models are not CMB-ready

## Aussage
A literature review of automatic CMB detection on SWI/T2* (PubMed + Europe PMC, 37 retrieved records; arXiv not
reachable, HTTP 429 through the proxy) gives three actionable results for this project:

1. **The closest published analogue of our chain is SHIVA-CMB.** One 3D U-Net trained once on 450 scans from 7
   acquisitions and 6 cohorts, T2* and SWI mixed (Tsuchida 2024, PMID 39730628): held-out test sensitivity 0.67,
   precision 0.82, F1 (Dice) 0.74, 0.6 false positives per scan; on an evaluation-only set with acquisitions never
   seen in training 0.67 / 0.91 / 0.77 / 0.5 FP; correlation with expert visual counts in 1,992 T2*-weighted scans
   Pearson R 0.89. **Both the pipeline (SHiVAi) and the pretrained weights (SHIVA-CMB) are public** -- a free
   external baseline we should run on our data.
2. **Precision, not sensitivity, separates the methods.** The best lesion-level numbers reported 2023-2026 come from
   pipelines whose candidate stage is deliberately constrained: morphology filter bank + CNN, 95.0 % sensitivity at
   4.37 FP/patient versus 97.5 % at 25.87 FP without the filter bank (Nishioka 2025, PMID 38494702); a
   geometric-to-neural cascade (GMM candidate generation + two 3D ResNets on QA labels) removing 76.8 % of stage-A
   false positives, F1 0.693, AUC 0.9587 (Bogdanov 2026 preprint, DOI 10.64898/2026.07.24.740624); U-Net with CBAM
   attention, large kernels and anatomy localisation, F1 0.887 at 0.83 FP/scan on 506 multi-site scans (Cho 2026,
   PMID 41859233). This matches our own negative finding that sensitivity levers do not raise lesion F1.
3. **Mimic handling is a contrast problem, not an architecture problem.** QSM separates CMB from calcification
   better than SWI/phase on accuracy, confidence and inter-rater agreement (Kang 2025, PMID 39690177); adding a
   high-pass filtered phase channel to SWI gave 95.8 % sensitivity, 70.9 % precision, 1.6 FP/case (Liu 2019, PMID
   31121296); multi-modal T2w/SWI/QSM input improved CMB-versus-iron separation, QSM being the most informative
   channel (Rashid 2021, PMID 34238951). Anatomical masking (ventricles/CSF/choroid plexus/cerebellum/edges) is a
   free false-positive filter present in the top pipelines -- consistent with our CSF rule.

Secondary results: synthetic CMBs are now a first-class training strategy (analytic model, 37,000 lesions released,
~9 FP/scan when trained on synthetic only, Momeni 2021, PMID 34051412; 3D lesion GAN transferring to unseen MRI
parameters, PMID 34975381; self-supervised pseudo-labels giving +46 % average precision on ex-vivo T2*, Nikseresht
2026, PMID 42107619). The SWI/T2* domain gap is measurable: synthesising SWI from T2* magnitude recovers 19/28 CMBs
seen on real SWI versus 10/28 on magnitude images (Genc 2023, PMID 36733222). Meta-analytic pooled DL accuracy is
high (lesion-level sensitivity 0.96 / specificity 0.98, patient-level 0.89 / 0.86, Feng 2026, PMID 42767630), but the
authors themselves warn the study count is small. SWI detects about 1.6x more CMBs than T2*-GRE (13-study
meta-analysis, Yang 2026, PMID 41775374), so sequence mix dominates any single F1 number.

## Trägt
SHIVA-CMB publishes pipeline and weights, so it is a reproducible external baseline (claim 1). Claims 2 and 3 rest
on peer-reviewed abstracts retrieved in this task and are consistent with our own measured results (vessel
inpainting, CSF rule, sensitivity levers).

## Trägt nicht
- **No CMB-specific transformer or foundation model was retrieved.** The only retrieved foundation-model work is a
  universal brain-MRI lesion segmentation model with Mixture-of-Modality-Experts (9 datasets, 8 lesion types, CMB
  not among them, Zhang 2025, PMID 40031588); the foundation-model and diffusion reviews report no CMB numbers.
- **No post-2021 successor benchmark to VALDO was retrieved**, so the VALDO weak-label and case-level-inconsistency
  findings stand unresolved.
- arXiv was not retrievable in this task (HTTP 429 / "Rate exceeded." through the proxy across many retries), so
  computer-science preprints are entirely missing from this picture; treat the transformer/foundation-model blank as
  "not retrieved", not as "does not exist".

## Bruchindikator
A peer-reviewed work reporting CMB detection with a transformer or foundation model, or a new multi-centre CMB
benchmark superseding VALDO, or a paper showing a per-dataset-trained 3D U-Net beating a single multi-cohort model
(SHIVA-CMB) on unseen acquisitions.

## Ablesung
SHIVA-CMB: Tsuchida et al., Sci Rep 2024, doi:10.1038/s41598-024-81870-5, PMID 39730628. VALDO: Sudre et al., Med
Image Anal 2024, doi:10.1016/j.media.2023.103029, PMID 37988921. MicrobleedNet: Sundaresan et al., Front Neuroinform
2023, doi:10.3389/fninf.2023.1204186, PMID 37492242. Full reference list (37 records) and evidence tables:
/home/uchralt/cle-arbeit/recherche/d_cmb_detection/REPORT.md; PMIDs and DOIs checked with
local_agentic_system/system/werkzeuge/quellen-pruefen (36/36 PMIDs correct, 0 wrong). Own literature retrieval
2026-10-17.
