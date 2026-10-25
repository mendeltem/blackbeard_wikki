---
id: voxel-token-transformers-unproven-at-300-subjects-2026-10
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-25
herkunft: chat with Mendel (claude.ai), 2026-10-25, literature scan on tokenising MRI volumes like an LLM
verweist_auf: [anisotropic-first-level-beats-isotropic-3d-nets, literature-2023-2026-shiva-cmb-is-the-public-comparable, fine-tune-from-public-valdo-weights, patches-not-whole-images-for-small-lesions]
---

# Voxel-as-token and small-patch transformers are unproven for CMB; at ~300 subjects only pretrained weights are an option

## Aussage
Question: can an MRI volume plus ROI be fed to a transformer as a flat 1D sequence (voxel = token, like an LLM), and
does that help CMB detection with about 300 subjects?

1. **Feasible in principle, cost is the limit.** Flattening loses no information if each token carries its (x,y,z)
   position embedding, or if the order follows a space-filling curve (Hilbert/Z-order) that keeps neighbours close.
   Global attention cost per head and layer (computed, n^2):
   - whole brain 1 mm (182x218x182 = 7.2e6 voxels) as voxel tokens: 5.2e13 pairs, infeasible;
   - crop 128^3 with patch 4^3: 32,768 tokens, 1.1e9 pairs, roughly the limit of dense attention;
   - crop 128^3 with patch 2^3: 262,144 tokens, 6.9e10 pairs global, but 9e7 with 7^3 window attention (Swin);
   - ROI-only tokens, e.g. 20,000 voxels at patch 1: 4e8 pairs, feasible.
   Halving the patch edge gives 8x tokens and 64x attention cost. A CMB of 2-10 mm spans 2-10 voxels at 1 mm, so a
   16^3 patch swallows it; 4^3 or 2^3 resolves it.
2. **Evidence for small patches is thin.** Only one preprint measures 3D patch size down to 1: ViT-Small fine-tuned on
   MedMNIST3D at 28^3, patch 1 vs 14 up to +23.78 % balanced accuracy, cost ~0.4 -> >800 GFLOPs per volume, no CNN
   baseline, one MRA set only (Dehghan et al. 2026, arXiv:2602.18614, preprint). Pixel-token transformers work on
   natural 2D images (Nguyen et al., ICLR 2025, peer-reviewed). No voxel-token or point-cloud model for brain lesions
   (WMH, CMB, stroke) with an nnU-Net baseline was found.
3. **Long-sequence alternatives exist but serialise features, not raw voxels:** Perceiver / Perceiver IO
   (Jaegle et al. 2021/2022, arXiv:2103.03206, arXiv:2107.14795); Hilbert-curve Mamba on MRI (GAMBAS,
   arXiv:2504.04523, preprint). Mamba results depend on the serialisation order. PerceiverIO on brain MRI segmentation
   with k-space input: arXiv:2407.01367 (status unclear).
4. **Data size.** Transformers lack the locality prior of CNNs and need more data (ViT below ResNet on ImageNet-1k,
   ahead only with 300 M images; Dosovitskiy et al., ICLR 2021, arXiv:2010.11929). With ~300 labelled subjects, training
   from scratch is not sensible. The large numbers in circulation are unlabelled pretraining sets, not a requirement for
   the fine-tuning set:
   - BrainSegFounder: SSL on 41,400 UK Biobank participants, Swin UNETR (Cox et al., Med Image Anal 2024,
     doi:10.1016/j.media.2024.103301, peer-reviewed); weights under the UK Biobank MTA (access needed).
   - AMAES / BRAINS-45K: 44,756 public brain MRI volumes, code, checkpoints and data open (Munk et al., arXiv:2408.00640,
     preprint).
   - FOMO60K: 60,529 scans from 11,187 subjects (scans are not subjects).
   - FOMO25 challenge: small pretrained models did well; larger models or longer training gave no reliable gain; MAE
     pretraining favours segmentation (arXiv:2604.11679, preprint).
5. **Counter-evidence in this wiki.** On VALDO, Swin UNETR and other isotropic 3D nets lost against a U-Net whose first
   level convolves only in-plane ([anisotropic-first-level-beats-isotropic-3d-nets](anisotropic-first-level-beats-isotropic-3d-nets.md)),
   and no CMB-specific transformer or foundation model was retrieved
   ([literature-2023-2026-shiva-cmb-is-the-public-comparable](literature-2023-2026-shiva-cmb-is-the-public-comparable.md)).
   Pretraining sets are mostly T1/FLAIR; whether they help SWI/T2* magnitude is open.

## Trägt
Decision on whether to try a transformer for CMB detection: only as fine-tuning of public pretrained weights, compared
in the same frozen folds against the current chain (anisotropic 3D U-Net plus stage-2 classifier), reported as lesion
F1 and FP per scan, with two seeds (effects below ~0.08 F1 are seed noise). A transformer over ROI or candidate tokens
fits stage 2 better than stage 1 (compare TrackSet-CMB in
[search-space-expansion-and-novel-hybrids-2026-10](search-space-expansion-and-novel-hybrids-2026-10.md)).

## Trägt nicht
Any claim that voxel-token transformers beat CNNs on CMB; any minimum subject count for fine-tuning (none found);
transfer of the MedMNIST 28^3 result to clinical resolution.

## Bruchindikator
A peer-reviewed voxel-token or small-patch transformer that beats nnU-Net or the anisotropic U-Net on CMB lesion F1;
a pretraining set with SWI/T2* where fine-tuned weights beat the chain in the same folds.

## Ablesung
Web search 2026-10-25. arXiv:2602.18614 full text read; BrainSegFounder count and DOI from the UK Biobank publication
page and the Hugging Face model card; BRAINS-45K, FOMO60K, FOMO25 from arXiv abstracts and a topic page. Not re-read:
Nguyen ICLR 2025, Dosovitskiy ICLR 2021, Jaegle 2021/2022 (cited from knowledge). Tier 1b (papers), preprints marked.
Attention costs computed, not measured.

## Verknüpft
- [anisotropic-first-level-beats-isotropic-3d-nets](anisotropic-first-level-beats-isotropic-3d-nets.md)
- [literature-2023-2026-shiva-cmb-is-the-public-comparable](literature-2023-2026-shiva-cmb-is-the-public-comparable.md)
- [fine-tune-from-public-valdo-weights](fine-tune-from-public-valdo-weights.md)
- [search-space-expansion-and-novel-hybrids-2026-10](search-space-expansion-and-novel-hybrids-2026-10.md)
- [patches-not-whole-images-for-small-lesions](../rules/patches-not-whole-images-for-small-lesions.md)
