---
id: calibrate-before-you-fine-tune
typ: regel
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-31
herkunft: phase-2 design of the CMB adaptation study (valdo-t2s), reviewer check 2026-10-31
verweist_auf: [full-data-last-state-models-run-hotter, fine-tune-from-public-valdo-weights]
---

# When a public detector over-detects at a new site, test "re-choose the threshold on the n local scans" before claiming a fine-tuning gain

## Aussage
A public CMB U-Net applied unchanged to a new scanner typically keeps its sensitivity and floods the scan with false
positives (own data: about 20x the false positives per scan of its own cross-validation; external example: CMB-HUNT,
0.54 -> 1.9 false positives per patient at similar sensitivity). Much of that is an operating-point shift, not missing
knowledge: the same weights reach a far better F1 at a higher threshold. A fine-tuning curve F1(n) must therefore be
compared with the cheapest adaptation that uses the same n annotated scans: keep the weights, re-choose threshold and
minimum lesion size on the n scans, apply to the test fold. Report the test-optimal cell as the upper bound of any
calibration. Only the part of the fine-tuning gain above this control is attributable to updating the weights.

## Trägt
Reasoning plus the measured calibration shift of full-data models (linked finding); calibration as the one-parameter
analogue of temperature scaling. AdaBN-type label-free normalisation adaptation is no alternative for instance-norm
U-Nets (instance norm already uses per-scan statistics).

## Trägt nicht
Not yet measured as a curve (queued 2026-10-31). A threshold chosen on 3 scans can be very noisy; report the draw spread.

## Bruchindikator
The calibration-only curve stays at the zero-shot level for every n (then the gap is in the weights, not the threshold).

## Ablesung
Guo et al., ICML 2017, "On Calibration of Modern Neural Networks", arXiv:1706.04599. Suwalska et al., Comput Biol Med
2022, doi:10.1016/j.compbiomed.2022.106233, PMID 36370581 (CMB-HUNT, external FP rise). Yu et al., Radiol Artif Intell
2022, doi:10.1148/ryai.210064, PMID 35652114 (most externally validated imaging algorithms lose performance). Kelly et
al., BMC Med 2019, doi:10.1186/s12916-019-1426-2, PMID 31665002 (local validation before use).

## Verknüpft
[full-data-last-state-models-run-hotter](../findings/full-data-last-state-models-run-hotter.md),
[fine-tune-from-public-valdo-weights](../findings/fine-tune-from-public-valdo-weights.md)
