---
id: arena-2-research-round-4-unlabelled-tabular-frozen-2026-10
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-25
herkunft: claude.ai chat with Mendel 2026-10-25 ("what can still be improved in Arena 2"); three literature agents on the three levers the wiki had no entry for; load-bearing IDs re-checked by hand
verweist_auf: [arena-2-research-round-3-2026-10, search-space-expansion-and-novel-hybrids-2026-10, voxel-token-transformers-unproven-at-300-subjects-2026-10, one-shared-candidate-classifier-for-all-cohorts, research-passes-invent-plausible-pmids]
---

# Arena 2, research round 4: unlabelled scans, a tabular stage 2, frozen foundation features (2026-10)

Scope: a keyword audit of cmb_detection and lesion_detection_method found zero entries on semi-supervised learning,
tabular / boosting candidate classifiers and frozen foundation-model features. Everything else asked for ("what can be
improved") is already covered by rounds 1-3 and the search-space expansion. All three levers below are stage-2 arms
(seed noise ~0.01, ~1 GPU hour or less), consistent with where the headroom is.

## Aussage

**1. Unlabelled scans: small gains at our label count, more likely a variance than a mean effect.**
No semi-supervised CMB paper on in-vivo SWI/T2* exists (PubMed query on microbleed AND semi-supervised / pseudo-label /
self-training / self-supervised / unlabeled / mean teacher: one hit, ex-vivo). The one CMB result: self-supervised
pretraining in an ex-vivo multi-echo GRE detector added about +0.007 AP (0.333 -> 0.340, 5 folds x 4 seeds) [1]; the
paper's headline 46 % AP gain comes mainly from its synthesis, not from the pretraining. Analogues:
- lung nodules, FocalMix: CPM +11.5 at 25 labelled scans, +4.4 at 100, +0.7 at 533 (no seeds) [2];
- brain metastases < 15 mm, noisy student with 217 labelled / 1,247 unlabelled: FP per scan at 90 % sensitivity
  9.23 -> 8.44, at 80 % no change; looser pseudo-label thresholds made the student WORSE than the teacher [3];
- perivascular spaces, pseudo-labels on 12,740 unlabelled T1w: Dice 85.7 -> 85.6, a null result (preprint) [4];
- in-domain self-supervised pretraining for nodule FP reduction: AUC 96.03 +- 1.82 -> 98.34 +- 0.44 over 10 runs,
  i.e. the run-to-run spread fell about 4-fold [5].
Pattern: large gains only below ~50 labelled scans. Expected here (extrapolation, not measured): stage 1 +0.00 to
+0.05 F1, below its seed noise; stage 2 +0.00 to +0.02.

**2. A tabular stage 2 is a mandatory cheap ablation, not a long shot.**
No paper compares a CNN and a boosting / random-forest stage 2 on the SAME CMB candidates; the "CNN beats handcrafted"
claims in CMB compare across datasets. Classical CMB pipelines: random-forest cascade on LoG candidates with Radon and
Hessian shape descriptors, 87 % sensitivity at 27.1 FP per subject [6]; two-stage RF (voxel then object) on SWI, object
RF improved every FROC point, remaining FPs were vessel segments that look spherical [7]; SVM on shape and intensity,
81.7 % (semi-automated) [8]. The only same-candidate head-to-head found (fundus red lesions, 28 and 78 training images,
407 positives) went to the tabular model, and the combination won [9]:

| features on the same candidates | DIARETDB1 CPM | e-ophtha CPM |
|---|---|---|
| CNN only | 0.376 | 0.306 |
| handcrafted + RF | 0.452 | 0.356 |
| CNN + handcrafted in RF | 0.487 | 0.368 |

Counter-case: with ~1,000 positives on LUNA16 all top FP-reduction entries were CNNs (CPM 0.758-0.908 vs classical
full systems 0.608-0.742) [10]. Our pool has about a hundred VALDO positives, i.e. the regime where [9] found the
tabular model ahead. Feature list per candidate (first pass): volume, equivalent diameter, slices spanned, max in-plane
area; PCA eigenvalue ratios (elongation), sphericity; multi-scale Hessian eigenvalues, Frangi vesselness and blobness
at sigma 0.5-2 mm (anisotropy-aware); contrast to a surrounding shell, min / mean intensity; stage-1 max and mean
probability; a tube score (how far the dark signal continues beyond the component along its main axis, a hand-made
proxy of TrackSet's slice-track module); plus the round-3 features (vote count, edge distance, vein atlas).

**3. Frozen foundation features: only with patch-local pooling at the candidate.**
Nothing exists on CMB. The decisive finding: in chest X-ray, linear probes on the CLS token of frozen RAD-DINO, DINOv2,
DINOv3, BiomedCLIP and MedSigLIP stayed at chance for 4-8 px perturbations, while pooling the patch tokens inside the
lesion box from the same forward pass reached AUC >= 0.899 on natural small lesions, +0.119 to +0.387 over CLS
(preprint; needs the lesion location, which our stage 1 provides) [11]. In a CT detector with 82 % of lesions < 6 mm a
frozen natural-image DINOv2 with registers beat the medical encoders (CPM 0.518 vs 0.423-0.433, preprint) [12]. Against:
3D CT foundation models stay near chance on small nodules [13]; on renal lesions no foundation model beat a ResNet-50
from scratch and radiomics did best (external AUC 0.88 vs 0.69-0.77) [14]; upsampling small native crops costs accuracy
(MedMNIST 28 px -> 224: AUC 91.75 vs 96.62 at native 224) [15]. Expected: parity with the stage-2 CNN, at best a
complement in a late-fusion average. Main risks: natural-image encoders may not separate bleeds from vessel
cross-sections on magnitude images, and features may encode site rather than lesion.

## Trägt
Three new stage-2 arms for Arena 2, all on the frozen out-of-fold candidate pool and the frozen folds, judged by the v2
decision rules:
- **T (tabular):** LightGBM, shallow trees, strong regularisation, nested scan-grouped CV, features above; plus T+E
  (same model with the CNN embedding appended). CPU, seconds per fit. Run this FIRST: it is the baseline every
  TrackSet module must beat, and it tells whether the slice-track idea is already captured by a hand-made tube score.
- **F (frozen):** DINOv2-B/14 with registers (second arm MedSigLIP-448), 16 mm in-plane crop, channels = slices -1/0/+1
  (mIP over +-2 slices for thin SWI), bicubic upsampling to 224, mean of the central 2x2-3x3 patch tokens from the last
  and one middle block, L2 logistic regression with nested C; never the CLS token alone.
- **U (unlabelled):** one noisy-student round on stage 2 only: stage 1 frozen on unlabelled scans of the same sequences,
  current stage 2 as teacher, keep only p > 0.95 positives and p < 0.05 negatives, student with stronger augmentation,
  5 paired seeds. Unlabelled in-house scans are class 3 data: local profile only.

## Trägt nicht
Any expectation of a large standalone gain from F or U; the effect-size ranges are the agents' extrapolations, not
measurements. No source measured any of the three levers on CMB candidates. Most sources were read at abstract level;
FocalMix and Orlando tables were read in full text; several 2026 sources are preprints.

## Bruchindikator
T falls clearly below the stage-2 CNN on all cohorts (then the few-positives argument does not hold here); F with
patch-local pooling stays near chance on our candidates; U produces more confident positives on veins than on bleeds.

## Ablesung
IDs fetched by the agents; re-checked by hand on 2026-10-25: [1], [3], [8] (PubMed metadata), [9], [11] (arXiv pages).
Others marked as agent-verified only. Tier 1b; preprints marked.
[1] Nikseresht G et al. 2026. Automated detection of cerebral microbleeds on ex-vivo MRI scans of community-based older adults. NeuroImage 335:121986. DOI 10.1016/j.neuroimage.2026.121986, PMID 42107619. Peer-reviewed. SSL ablation number from the full text as read by the agent.
[2] Wang D et al. 2020. FocalMix: semi-supervised learning for 3D medical image detection. CVPR. arXiv:2003.09108. Peer-reviewed (agent-verified).
[3] Dikici E et al. 2022. Advancing brain metastases detection in T1-weighted contrast-enhanced 3D MRI using noisy student-based training. Diagnostics 12(8):2023. DOI 10.3390/diagnostics12082023, PMID 36010373. Peer-reviewed.
[4] Pham et al. 2024. nnU-Net segmentation of perivascular spaces. arXiv:2411.19564. Preprint (agent-verified).
[5] Zhou Z et al. Models Genesis. Med Image Anal. arXiv:2004.07882. Peer-reviewed (DOI not verified).
[6] Fazlollahi A et al. 2015. Comput Med Imaging Graph. DOI 10.1016/j.compmedimag.2015.10.001 (agent-verified).
[7] van den Heuvel TLA et al. 2016. NeuroImage Clin. DOI 10.1016/j.nicl.2016.07.002 (agent-verified).
[8] Barnes SRS et al. 2011. Semiautomated detection of cerebral microbleeds in magnetic resonance images. Magn Reson Imaging 29(6):844-52. DOI 10.1016/j.mri.2011.02.028, PMID 21571479. Peer-reviewed.
[9] Orlando JI et al. 2018. An ensemble deep learning based approach for red lesion detection in fundus images. Comput Methods Programs Biomed. DOI 10.1016/j.cmpb.2017.10.017, arXiv:1706.03008. CPM values checked on the arXiv page.
[10] Setio AAA et al. 2017. LUNA16 challenge. Med Image Anal. arXiv:1612.08012 (DOI 10.1016/j.media.2017.06.015 not verified).
[11] Muthyala R et al. Frozen foundation-model embeddings discard small-lesion signal in chest radiography. arXiv:2606.11606. Preprint.
[12] Gokmen et al. 2026. SALT: lesion detection in CT with frozen self-distilled features. arXiv:2608.05100. Preprint (agent-verified).
[13] Chevli, Mueller et al. 2026. Big, bright, or invisible: frozen-feature benchmark of 3D CT foundation models. arXiv:2608.05960. Preprint (agent-verified).
[14] Haentze, Bressem et al. 2026. Benchmarking foundation models for renal lesion stratification in CT. arXiv:2605.07749. Preprint (agent-verified).
[15] Wu, Papiez. MedMNIST foundation-model benchmark. arXiv:2501.14685. MIDL 2025 submission (acceptance not verified).

## Verknüpft
- [arena-2-research-round-3-2026-10](arena-2-research-round-3-2026-10.md)
- [search-space-expansion-and-novel-hybrids-2026-10](search-space-expansion-and-novel-hybrids-2026-10.md)
- [voxel-token-transformers-unproven-at-300-subjects-2026-10](voxel-token-transformers-unproven-at-300-subjects-2026-10.md)
- [one-shared-candidate-classifier-for-all-cohorts](one-shared-candidate-classifier-for-all-cohorts.md)
- [research-passes-invent-plausible-pmids](../../agent_coordination/findings/research-passes-invent-plausible-pmids.md)
