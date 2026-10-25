---
id: search-space-expansion-and-novel-hybrids-2026-10
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-25
herkunft: Claude Code (Alita) 2026-10-25, four narrowly scoped literature agents (CMB audit, adjacent small-object detection, information levers, prior-art check of 12 hybrid designs) plus own checks; 125 arXiv IDs / DOIs re-fetched by script (titles match), key numbers re-read in abstracts or PDF tables; tried inventory from our own measurements 2026-09-18 to 2026-10-16
verweist_auf: [research-cmb-detection-2023-2026, sensitivity-levers-do-not-raise-lesion-f1, one-shared-candidate-classifier-for-all-cohorts, two-seeds-per-decision-below-0.08, anisotropic-first-level-beats-isotropic-3d-nets]
---

# CMB detection: where the headroom is, what is untried, and new hybrid models (2026-10)

## Aussage

**1. The headroom sits in stage 2, and stage 2 is where new models can be measured.** With a perfect candidate
classifier our chain would reach about F1 0.85 on VALDO instead of about 0.65 (candidates reached at stage-1 threshold
0.15). The seed spread of stage 2 on fixed candidates is about 10x smaller than that of a stage-1 training (VALDO sd
0.009 against about 0.08 between single stage-1 seeds; in-house cohorts smaller still), and one stage-2 arm costs about
one GPU hour. New models therefore go into stage 2 first; stage-1 changes need about 6 GPU hours per comparison and can
only resolve effects of about 0.08.

**2. Backbone swaps are exhausted, by our data and by the literature.** 15 stage-1 networks lost to the anisotropic
U-Net in our arena. CenSynCMB's own re-implementations on VALDO Task 2 give SwinUNETR F1 54.3 and VISTA3D 56.4 against
65.8 for an Attention U-Net backbone [1]; nnU-Net Revisited finds Mamba layers "have no effect" [14]; SAM-Med3D removed
all training masks below 1 cm3 [15], so CMB-sized objects lie outside it. No CMB-specific transformer, Mamba or
foundation detector was found.

**3. Most published levers are smaller than our stage-1 noise.** CenSynCMB's physics synthesis moves VALDO F1 71.7 ->
73.1 (+CMB) -> 74.3 (+mimics), FP/subject 1.4 -> 0.8, single seed, CI about +-9, no paired synthesis test p<0.05 [1].
Effects of +1 to +4 F1 cannot be seen with two stage-1 seeds; another reason to test in stage 2 or on the CPU.

**4. Untried options with the best evidence (audit of 31 CMB sources against our inventory):**
- Heterogeneous ensembles across architectures: VALDO EnsembleTop (mean of the top 4 teams) median F1 per subject 75.68
  [38.18; 100] against 68.42 for the best single team [2]. We only ensembled seeds of one architecture.
- Hard Sample Prototype Learning (feature of the hardest negative voxel per crop pushed away from a CMB prototype):
  FP/subject 14.73 -> 0.86 at 94.66 % sensitivity together with a feature-fusion module, on SWI+phase [3].
- Synthetic vessel mimics as an explicit label class: annotation-free SynthSeg-style training reaches CMB AUPRC 0.538
  against 0.004 for a Frangi baseline on 13 T2* cases [4]; synthetic-only training keeps about 87 % of real-trained
  sensitivity, but transfer depends on the framework [5].
- T1+T2 as extra channels (VALDO only): all leading VALDO teams used them; no ablation exists anywhere [1,2].
- Expert-audited labels: VALDO labels are "weak and noisy" [2], nnU-Net false positives on VALDO "could be an actual
  microbleed" [24]; SHIVA-CMB built its labels in an expert loop at p>=0.05 [19]; missing-annotation mining gave +2.3
  sensitivity / +2.7 precision on DeepLesion [25].
- An independent second candidate source (FRST peaks, per-scan GMM [21]) united with the U-Net candidates, to lift
  the ceiling of stage 2.

**5. Adjacent small-object fields: what transfers.** Our stage-1 logic (segmentation, connected components, max score)
is the "DetU-Net" baseline of Retina U-Net: 3D LIDC mAP10 36.6 against 49.8, lost mainly through high-confidence false
positives [6]; nnDetection made the Retina U-Net template safe for small objects [7]. A jointly trained, decoupled
false-positive branch raised nodule detection by 10.27 % [8]. Top-K centre-point matching beats a single-centroid
CenterNet by 21 points sensitivity at 1 FP/scan [9], a plausible reason why our centre-heatmap head failed. 3D group
convolutions reach the FROC of a CNN trained on ten times more data (0.550 -> 0.767 at 300 training samples) [10]; our
pooled classifier has about a hundred positive VALDO candidates. Counter-evidence: detection-head re-implementations
score 33.6-61.0 on VALDO against 65.8 [1], so a detector is a test, not a promise.

**6. Prior-art check of 12 hybrid designs (searched 2026-10-25, absence is not proof):**

| design | verdict | closest work |
|---|---|---|
| one network, U-Net + candidate head, joint loss | known for CMB | Kim 2025 RPN + FFM + HSPL [3] |
| scan-level candidate set transformer | port (nodules) | NoduleSAT [11] |
| learned slice-track sequence model ("does the dark structure continue?") | novel | coronary centreline tracking only [12] |
| rotation-equivariant classifier | port (nodules) | 3D G-CNN [10] |
| spacing-conditioned detector | port | HyperSpace [26] |
| dipole-rendered CMB + vessel mimics | known for stage 1 | CenSynCMB [1]; B0-orientation-aware vessels and use in stage 2 not found |
| joint through-plane super-resolution + detection | novel (joint); SR-then-detect known [18] | SR erases small lesions [17] |
| point / count supervision | novel for CMB | P2PNet [33] |
| pseudo-healthy inpainting residual per candidate | novel for CMB | normative diffusion restoration [29] |
| GNN on an extracted vessel graph | novel | liver vessel-graph pruning [30] |
| mIP slab channels as input | port (nodules), partial for CMB | MIP slabs for nodules vs vessels [13] |
| mixture of experts by geometry / sequence | port | MoME [35] |

**7. Proposed new mixed model, stage 2: "TrackSet-CMB".** Built on the fixed out-of-fold candidates of the anisotropic
U-Net; every module is one arena switch, so each can be ablated:
- (a) local crop encoder (image, FRST, probability, 16 mm) with in-plane D4 equivariance plus z-flip (full 3D groups
  are invalid on 5 mm slices) [10,32];
- (b) slice-track encoder: per slice above and below the candidate, a 2D crop re-centred on the local intensity minimum
  (so a curved vessel stays centred), shared 2D encoder, small transformer over the slice tokens with their offsets and
  contrast (novel by the search; a learned form of the track-length rule that helped on one external SWI set only);
- (c) soft context: SynthSeg region, distance to brain edge and ventricles, replacing the hard CSF rule (which deletes
  real deep CMB on SWI);
- (d) one attention layer across all candidates of the scan with a geometric bias (distance, collinearity) [11];
- losses: BCE with positive weight plus the prototype margin loss of [3]; optional third class "vessel mimic" trained
  with counterfactual renderings (same host, same renderer, sphere vs B0-oriented cylinder).
As a whole this combination was not found; (b) and the orientation-aware counterfactual mimics are the novel parts.

**8. Proposed stage-1 hybrid (port, not novel):** anisotropic U-Net trunk with three heads: segmentation (as now),
top-K centre-point matching [9] and a decoupled early-feature false-positive head [8], trained jointly with the
prototype loss [3]; objects are scored by the heads instead of connected components plus threshold [6].

**9. Measurement order with rules fixed in advance.**
- Phase 0, CPU only: heterogeneous ensemble from existing out-of-fold maps; ceiling of the candidate union
  (FRST/GMM + U-Net, about 4 CPU minutes); neighbour-candidate features (k nearest candidates) into the existing pooled
  classifier as a cheap proxy for (d); the blinded expert review (waiting since 2026-09-22).
- Phase 1, stage 2 only, 3 seeds per arm, about 1 GPU hour each: (a), (a)+prototype loss, (b), (d), rendered mimics,
  inpainting residual. An arm stays if its paired gain exceeds twice the stage-2 seed spread, the case bootstrap
  interval excludes 0 on the pooled F1, and no cohort gets significantly worse; then confirm the combination with an
  independent stage-1 seed. Renderer first passes a realism probe (a classifier must not tell rendered from real
  crops) before any training, as our augmentation lesson requires.
- Phase 2, stage 1, 2 seeds, ceiling check before each run: T1+T2 on VALDO, real nnU-Net v2 (calibration),
  nnDetection, the stage-1 hybrid.
- Predictions written before measuring: (a) helps most where positives are fewest; (b) helps on thin slices and is
  neutral on 5 mm slices, where true CMB also span several slices; rendered mimics lower vessel false positives only if
  they pass the realism probe.

**Not recommended (evidence against):** Mamba backbones [14], SAM-Med3D / VISTA3D / BrainSegFounder for tiny lesions
[15,1], DETR-type detectors with a few hundred lesions, through-plane super-resolution as preprocessing [17], more seed
ensembles.

## Trägt
Every ID was re-fetched by script on 2026-10-25 (arXiv API, Crossref; PMIDs via PubMed E-utilities) and the title
matched. The numbers in points 2-5 were re-read in the abstracts or PDF tables (VALDO Table 8, CenSynCMB Tables I and
IV, G-CNN Table 2, NoduleNet and Cao abstracts). The tried inventory comes from our own measurements on VALDO and the
in-house cohorts (only relative statements here).

## Trägt nicht
Agents read many sources at abstract level; HSPL [3] was read in full by one agent but not re-checked here. All
adjacent-field gains are on CT nodules or aneurysms, not on CMB. The novelty verdicts rest on about 30 targeted
searches (PubMed, arXiv, web) and are no proof of absence. The CenSynCMB external AIBL set is very likely the same
public SWI collection as our external set, under a different (per-subject macro) metric, so its 65.0 is not comparable
with our pooled F1. TrackSet-CMB and the stage-1 hybrid are designs, not results.

## Bruchindikator
A published CMB paper with a learned slice-track or orientation-aware mimic renderer; a Phase-0 ceiling or ensemble
result that shows no headroom; stage-2 arms that cannot beat twice the seed spread.

## Ablesung
[1] He L. 2026. CenSynCMB: Centre Maps and Physics-Guided Synthesis for Microbleed Detection. arXiv 2607.05325. Shows: centre map + FN reweighting + dipole-kernel synthesis with vessel-/calcification-like negatives; re-implemented baselines on VALDO (SwinUNETR 54.3, VISTA3D 56.4, Attention U-Net 65.8).
[2] Sudre CH et al. 2024. Where is VALDO? Medical Image Analysis 91:103029. DOI 10.1016/j.media.2023.103029. PMID 37988921. Shows: EnsembleTop median per-subject F1 75.68 vs best team 68.42 on Task 2; weak and noisy labels.
[3] Kim JH et al. 2025. Toward automated detection of microbleeds with anatomical scale localization using deep learning. Medical Image Analysis. DOI 10.1016/j.media.2024.103415. PMID 39642804 (arXiv 2306.13020). Shows: one U-Net + RPN model with FFM and Hard Sample Prototype Learning, sensitivity 94.66 %, FP/subject 14.73 -> 0.86 (SWI+phase).
[4] Cao Y. 2026. Synthetic training for long-tail haemorrhagic lesion segmentation in data-scarce settings. arXiv 2610.01542. Shows: annotation-free synthetic training with vessels as mimics, CMB AUPRC 0.538 vs 0.004 (Frangi), 13 cases.
[5] Hsu TL. 2026. Synthetic-to-Real Transfer in Cerebral Microbleed Generation and Segmentation. arXiv 2610.00743. Shows: synthetic-only training reaches about 87 % of real-trained lesion sensitivity; transfer depends on the architecture.
[6] Jaeger PF. 2018. Retina U-Net. arXiv 1811.08661. Shows: auxiliary segmentation in a one-stage detector; segmentation + connected components baseline far behind (3D LIDC mAP10 36.6 vs 49.8).
[7] Baumgartner M. 2021. nnDetection: A Self-configuring Method for Medical Object Detection. MICCAI, LNCS 12905. DOI 10.1007/978-3-030-87240-3_51 (arXiv 2106.00817). Shows: self-configuring Retina U-Net detector with small-object fixes.
[8] Tang H. 2019. NoduleNet: Decoupled False Positive Reduction for Pulmonary Nodule Detection and Segmentation. arXiv 1907.11320. Shows: jointly trained, decoupled FP branch, +10.27 % detection accuracy.
[9] Luo X. 2022. SCPM-Net. Medical Image Analysis 75:102287. DOI 10.1016/j.media.2021.102287. PMID 34731775. Shows: top-K centre-point matching, 92.3 % vs 71.4 % (single-centroid CenterNet) sensitivity at 1 FP/scan.
[10] Winkels M. 2018. 3D G-CNNs for Pulmonary Nodule Detection. arXiv 1804.04656. Shows: group convolutions match a CNN trained on ten times more data (FROC 0.550 -> 0.767 at N=300).
[11] Yang J. 2020. Relational Learning between Multiple Pulmonary Nodules via Deep Set Attention Transformers. arXiv 2004.05640. Shows: set attention over all nodules of a patient improves FP reduction.
[12] Wolterink JM. 2018. Coronary artery centerline extraction in cardiac CT angiography using a CNN-based orientation classifier. arXiv 1810.03143. Shows: learned vessel tracking (not lesion FP reduction).
[13] Zheng S. 2019. Automatic Pulmonary Nodule Detection in CT Scans Using CNNs Based on Maximum Intensity Projection. arXiv 1904.05956. Shows: MIP slab inputs separate nodules from vessels.
[14] Isensee F. 2024. nnU-Net Revisited. arXiv 2404.09556. Shows: well-scaled CNN U-Nets match or beat transformer/Mamba variants; Mamba layers have no effect.
[15] Wang H. 2023. SAM-Med3D. arXiv 2310.15161. Shows: training data excluded masks below 1 cm3.
[16] Wald T. 2024. Revisiting MAE pre-training for 3D medical image segmentation. arXiv 2410.23132. Shows: MAE-pretrained ResEnc U-Net +2.5 to +3.7 Dice on MS/stroke, +0.5 on small aneurysms.
[17] Khodakarami Z. 2026. Does FLAIR super-resolution erase or hallucinate small white-matter lesions? arXiv 2608.06311. Shows: super-resolution mostly erases small lesions, more with slice thickness.
[18] Liu F et al. 2026. Zero-shot arbitrary-scale super resolution in susceptibility-weighted imaging for cerebral microbleed analysis. Computer Methods and Programs in Biomedicine. DOI 10.1016/j.cmpb.2026.109433. PMID 42155350. Shows: SR before CMB segmentation (separate step).
[19] Tsuchida A et al. 2024. SHIVA-CMB. Scientific Reports. DOI 10.1038/s41598-024-81870-5. PMID 39730628. Shows: labels grown in an expert-reviewed loop; public weights.
[21] Bogdanov S et al. 2026. A geometric-to-neural cascade for cerebral microbleed detection in susceptibility-weighted MRI. bioRxiv. DOI 10.64898/2026.07.24.740624. Shows: per-scan GMM candidates + two 3D ResNets, 76.8 % of stage-A FPs removed.
[22] Momeni S et al. 2021. Generative Model of Brain Microbleeds for MRI Detection of Vascular Marker of Neurodegenerative Diseases. Frontiers in Neuroscience. DOI 10.3389/fnins.2021.778767. PMID 34975381. Shows: learned synthetic CMB beat the analytic model.
[24] Kuijf HJ. 2021. MixMicrobleedNet: segmentation of cerebral microbleeds using nnU-Net. arXiv 2108.01389. Shows: many nnU-Net FPs may be missed CMBs.
[25] Bai X. 2023. An End-to-End Framework For Universal Lesion Detection With Missing Annotations. arXiv 2303.15024. Shows: teacher mining of unlabelled lesions, +2.3 sensitivity / +2.7 precision on DeepLesion.
[26] Joutard S. 2024. HyperSpace: Hypernetworks for spacing-adaptive image segmentation. arXiv 2407.03681. Shows: conditioning on voxel spacing instead of resampling.
[29] Lawry Aguila A. 2025. CADD: normative conditional diffusion restoration of brain images. arXiv 2508.03594. Shows: pseudo-healthy restoration for large lesions.
[30] Zhang D. 2020. Graph Attention Network based Pruning for Reconstructing 3D Liver Vessel Morphology. arXiv 2003.07999. Shows: GNN on a vessel graph (not lesions).
[32] Weiler M. 2018. 3D Steerable CNNs. arXiv 1807.02547. Shows: rotation-equivariant volumetric features.
[33] Song Q. 2021. Rethinking Counting and Localization in Crowds: A Purely Point-Based Framework. arXiv 2107.12746. Shows: point-based detection and counting.
[35] Zhang X. 2024. A Foundation Model for Brain Lesion Segmentation with Mixture of Modality Experts. arXiv 2405.10246. Shows: modality-expert routing; CMB not evaluated.
Agent notes with the full tables (31 + 24 + 31 + 38 sources) stay outside the wiki.
