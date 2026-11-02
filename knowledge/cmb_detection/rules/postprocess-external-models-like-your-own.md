---
id: postprocess-external-models-like-your-own
typ: regel
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-11-01
herkunft: Projekt mb-arena (Alita), external baselines job wk1 (SHIVA-CMB as downloaded on a clinical cohort), review 2026-11-01
verweist_auf: [freeze-folds-and-cap-candidate-sources]
---

# Score an external model with exactly your own post-processing -- never let a threshold search reach 0

## Aussage
An external CMB model (SHIVA-CMB, Tsuchida et al. 2024) was evaluated on a clinical cohort with a threshold chosen inside
the training folds. The search picked t = 0.00 (probability > 0) on both sequences and reported sensitivity 0.99 with lesion
F1 0.87, far above every detector so far; the agent called it "a real finding". It is a metric artefact: without the
min/max component size of the own chain, p > 0 forms few huge components, and the touch rule (a reference lesion counts
as found if any predicted voxel touches it) lets one blob "find" many CMB. As downloaded (t = 0.5) the same model gave a
plausible, low result.

## Traegt
Any comparison of an external probability map with an own detector: apply the same connected-component filter (minimum
volume, maximum component size; here 2 mm3 and 2100 voxels at 0.25 mm3) before matching; search thresholds on a grid that
excludes 0 and 1 (e.g. 0.05-0.95); report the component-size distribution at the chosen threshold; treat sensitivity
>= 0.98 with high F1, or a threshold at the grid edge, as a bug until shown otherwise.

## Traegt nicht
Models whose output is already a binary mask with their own post-processing -- there, score the mask as delivered and say so.

## Bruchindikator
With identical post-processing and a grid without 0, the nested threshold still lands at the lowest grid value AND the
component sizes stay CMB-like.

## Ablesung
Own review 2026-11-01 (own-cohort numbers withheld; artefact described qualitatively). Model: Tsuchida et al. 2024,
SHIVA-CMB, Scientific Reports, doi:10.1038/s41598-024-81870-5, PMID 39730628; code github.com/pboutinaud/SHIVA_CMB
(CC BY-NC-SA 4.0). Correction job queued (wk1b).

## Verknuepft
- [freeze-folds-and-cap-candidate-sources](freeze-folds-and-cap-candidate-sources.md)
