---
id: human-rater-variance-and-good-f1-for-cmb-2026-10
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-25
herkunft: Claude Code (Alita) 2026-10-25, research round 4 (user question "experts make errors -- what is a good F1?"), two literature agents (CMB raters, methodology), 42 IDs re-fetched by script; derived numbers marked as such
verweist_auf: [arena-2-research-round-3-2026-10, human-rater-variance-and-good-dice-for-wmh-2026-10]
---

# How much do CMB raters disagree, and what is a good lesion-level F1?

## Aussage
- **No absolute "good" F1 exists; the human range is the yardstick.** Blind, pairwise, from-scratch lesion F1 between two CMB
  raters has not been published. The best proxy: six raters on 15 subjects (3 T, 2D T2*-GRE) scored against an adjudicated
  reference reach lesion Dice (= F1) 0.52-0.76, median 0.69; definite CMB only 0.58-0.84, median 0.77; per-lesion sensitivity
  38-78 %, precision 49-90 % (recomputed from the paper's table) [1]. The two reference experts of that study overlap on 75 of 134
  definite lesions, pairwise Dice about 0.72 (derived). The same expert re-segmenting T2* scans reaches 0.82 +- 0.14 [2].
- **Experience and sequence move the human numbers most.** Per-lesion sensitivity on 3 T SWI: neuroradiologist 0.905, resident
  0.621, neurosurgeon 0.871 [3]; at 7 T four raters found 31-83 % of the definite CMB and count ICC fell to 0.38-0.46 (1.5 T
  0.91-0.95), mainly through MISSED small lesions [4]. Six-rater count ICC: SWI 0.951 vs GRE 0.764 [5].
- **Subject level is much better than lesion level.** Weighted kappa on 0 / 1 / 2-4 / 5-9 / >= 10 CMB: 0.71, after a joint protocol
  review 0.82 (747 patients, two readers) [6]. Count ICC and category kappa hide which lesions are marked.
- **Derived human range (3 T T2*/SWI, experienced raters):** lesion F1 about 0.65-0.80 (central 0.70-0.75), precision 0.75-0.90;
  non-expert about 0.52-0.60; same rater twice about 0.82. Treat as +-0.1 (studies of 8-30 subjects, different matching rules).
- **What it means for a detector:** F1 >= 0.65-0.70 against one independent rater, or >= 0.75 against a consensus, WITH precision
  >= 0.75 lies within rater variability. An F1 above ~0.85 against one rater is above what a rater reproduces on himself and points
  to a lenient or algorithm-assisted reference, not to a superhuman detector. Our chain (~0.65 against single-rater labels) is in the
  lower-middle of the human band.
- **Method (round 4, H3):** compare the algorithm and the original rater with the SAME new independent rater, per scan:
  d = metric(algorithm, rater B) - metric(rater A, rater B), with a margin fixed in advance and a scan-clustered bootstrap; with two
  raters score each separately, not against a merged truth (majority or STAPLE references inflate performance and need many raters [8,9]);
  10-20 re-annotated scans support a non-inferiority margin of only about 0.08-0.12, a margin of 0.05 needs about 50 scans
  (agents' power calculation). Report definite-only and all-lesion F1 separately, and the matching rule.

## Trägt
IDs re-fetched by script 2026-10-25 (titles match). Kaaouana numbers recomputed from the published TP/FN/FP table; pairwise
expert Dice and the human range are derived (marked).

## Trägt nicht
No blind pairwise lesion-level CMB study exists; VALDO released no CMB double reading [7]. Several rows are abstract-level.

## Bruchindikator
A blind two-rater CMB study with lesion F1 far outside 0.65-0.80; our own second-rater check (10-20 scans) giving a different band.

## Ablesung
[1] Kaaouana T et al. 2017. NeuroImage: Clinical. DOI 10.1016/j.nicl.2016.08.005. PMID 28560152. Shows: six raters vs an adjudicated reference on 15 subjects, lesion Dice 0.52-0.76; reference experts overlap on 75 of 134 definite lesions.
[2] Dadar M et al. 2022. Frontiers in Neuroimaging. DOI 10.3389/fnimg.2022.940849. PMID 37555147. Shows: intra-rater per-lesion similarity 0.82 +- 0.14 on T2*.
[3] Won SY et al. 2024. Acta Neurochirurgica. DOI 10.1007/s00701-024-06267-9. PMID 39325068. Shows: per-lesion sensitivity by reader experience on 3 T SWI, unaided and AI-aided.
[4] de Bresser J et al. 2012. Visual cerebral microbleed detection on 7T MR imaging: reliability and effects of image processing. AJNR. DOI 10.3174/ajnr.A2960. PMID 22345502. Shows: at 7 T raters miss small CMB; count ICC 0.38-0.46 vs 0.91-0.95 at 1.5 T.
[5] Ford JN et al. 2026. Alzheimer's & Dementia: DADM. DOI 10.1002/dad2.70477. PMID 42745918. Shows: six-rater count ICC 0.951 on SWI vs 0.764 on GRE.
[6] Privsek E et al. 2026. Alzheimer's & Dementia: DADM. DOI 10.1002/dad2.70472. PMID 42824080. Shows: category kappa 0.71 -> 0.82 after protocol refinement, intra-rater 0.77-0.85.
[7] Sudre CH et al. 2024. Medical Image Analysis. DOI 10.1016/j.media.2023.103029. PMID 37988921. Shows: no CMB inter-rater analysis in VALDO; lacune rater-vs-rater lesion F1 48.5-55.8.
[8] Maier-Hein L et al. 2024. Metrics reloaded: recommendations for image analysis validation. Nature Methods 21:195-212. DOI 10.1038/s41592-023-02151-z. PMID 38347141. Shows: small lesions as detection tasks with lesion-wise metrics; report the reference quality (inter-/intra-rater).
[9] Reinke A et al. 2024. Understanding metric-related pitfalls in image analysis validation. Nature Methods 21:182-194. DOI 10.1038/s41592-023-02150-0. PMID 38347140. Shows: Dice is unstable for small structures.
