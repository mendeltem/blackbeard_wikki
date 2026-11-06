---
id: bianca-flair-slice-thickness-simulation-2026-11
typ: befund
status: vorschlag
thema: knowledge/wmh_segmentation
stand: 2026-11-06
herkunft: own BIANCA runs (FSL 6.0.7.23) on the public WMH Segmentation Challenge training scans, 432 settings runs + 3 seeds of the main setting, 2026-11-05/06
verweist_auf: [bianca-internals-and-official-challenge-split-2026-11]
---

# BIANCA and FLAIR slice thickness: test thickness decides, location matters most, patch can hurt

## Aussage
Simulation from the 3 mm challenge FLAIR: 5 mm by overlap-weighted slice averaging, 1 mm by linear interpolation; T1 resampled
from its own ~1 mm image. One model per thickness trained on 30 scans, tested at 1/3/5 mm on 30 other scans (cut-off tuned on 15,
Dice on 15 held out), scored on the native 3 mm grid against the official mask; no WM mask, no cluster removal.
- Mean Dice, main setting (FLAIR+T1, location, patch 3, noborder, 2000/10000 points), 3 seeds (noise <= 0.009), rows trained,
  columns tested 1/3/5 mm: 0.683 0.689 0.592 / 0.672 0.699 0.595 / 0.673 0.683 0.589.
- **Test thickness decides:** every model loses 0.094-0.107 on 5 mm test scans, 15/15 scans worse; small-lesion recall ~0.35 -> ~0.22.
  Training on 5 mm does not rescue 5 mm tests (-0.008 vs the 3 mm model). Matching helps a little at 3 mm only (+0.013 / +0.021).
- **Threshold:** best cut-off varies 0.60-0.99, but keeping the 3 mm cut-off was equal or slightly better on held-out scans
  (mean change -0.009 to 0.000 per cell): re-tuning on 15 scans buys nothing.
- **Settings (train = test, all else equal, 1/3/5 mm):** location +0.109/+0.143/+0.106 (largest, larger than the 5 mm loss);
  10000 vs 2000 non-lesion points +0.039/+0.041/+0.034; FLAIR+T1 vs FLAIR +0.039/+0.033/+0.024; surround vs any -0.028/-0.028/-0.011;
  noborder vs any ~0.
- **Patch hurts in strong settings:** FLAIR+T1, location, 10000 points: no patch 0.709/0.733/0.619 vs patch 0.683/0.703/0.588;
  the best setting on the tuning scans was "FLAIR+T1, location, no patch, 10000 points" in 9/9 cells, +0.012 to +0.038 over main
  (interval above 0 in 7/9). Untested guess: the kd-tree is unscaled and patch columns are ~2.6x wider.

## Trägt
Paired bootstrap over 15 held-out scans; 3 seeds for the main setting. Public data, numbers may be shown.

## Trägt nicht
A simulation (no real slice profile, gap, contrast or noise change); 1 mm FLAIR holds no new information; one split, 15 held-out
scans per cell; the settings grid used one seed; best-of-48 on 15 tuning scans stays somewhat optimistic.

## Bruchindikator
A claim that thin training scans fix thick test scans, or that thickness matters more than the location features.

## Ablesung
Griffanti L et al. 2016, NeuroImage 141:191-205, doi:10.1016/j.neuroimage.2016.07.018, PMID 27402600; Kuijf HJ et al. 2019,
IEEE TMI 38:2556-2568, doi:10.1109/TMI.2019.2905770, PMID 30908194. Data doi:10.34894/AECRSD (CC BY-NC 4.0). FSL 6.0.7.23.
Used in chapter 13 of the BIANCA tutorial film (2026-11-06).
