---
id: freeze-folds-and-cap-candidate-sources
typ: regel
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-25
herkunft: Claude Code (Alita) 2026-10-25, Arena 2: fold check on VALDO, three out-of-memory kills of the local agent's runner
verweist_auf: [two-seeds-per-decision-below-0.08, arena-2-research-round-3-2026-10]
---

# Freeze the folds with a checksum, and cap every new candidate source

## Aussage
1. **Folds are data, not code.** The 5-fold assignment of every cohort is written once (VALDO: stratified by cohort x burden, seed 0)
   and then frozen as a file with a SHA-256; every run input (candidate sets, prediction folders, manifests, synthetic copies) is
   checked against it before a run, and a different assignment is refused, never written over. On VALDO all inputs of Arena 1 and
   Arena 2 agreed (57 cases, 0 mismatches in two candidate sets, three runs and the manifest). Stage-2 GPU code runs with
   deterministic cuDNN kernels so that a rerun repeats.
2. **A new candidate source needs a cap before it meets patch extraction.** Uncapped radial-symmetry and per-scan Gaussian-mixture
   sources produced 33,661-125,920 candidates on VALDO instead of 278 from the U-Net; storing a crop for each one took ~41 GB and the
   runner was killed by the out-of-memory killer three times. The ceiling gain was real (perfect-stage-2 F1 0.851 -> 0.92-0.95, all
   sources together 0.978), so the source is kept, but only the K strongest new components per scan (by radial-symmetry peak) are
   passed on, and its ceiling is measured on the maps alone (no crops) first.

## Trägt
Own runs 2026-10-25 (VALDO check output; kernel OOM log; candidate counts from the ceiling tool).

## Trägt nicht
The cap value K is not measured yet; the in-house fold check runs on the local agent.

## Bruchindikator
A fold check that reports mismatches; a capped source whose candidate count still exceeds about twice the U-Net's.

## Ablesung
Tools in the project: fold freeze/check (sha256), candidate-source cap (--max-new, --min-voxels). VALDO 2021 Task 2 data: Sudre CH et al. 2024, Medical Image Analysis, DOI 10.1016/j.media.2023.103029, PMID 37988921.
