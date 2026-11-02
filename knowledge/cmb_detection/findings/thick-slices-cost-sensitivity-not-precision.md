---
id: thick-slices-cost-sensitivity-not-precision
typ: befund
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-11-01
herkunft: Projekt valdo-t2s (Alita), VALDO 2021 Task 2 cross-validation, full two-stage chain (stage 2 pooled tset-plain, fixed post-processing), two stage-2 seeds, 2026-11-01; script paper/figures_src/scripts/plot_slice_thickness_heatmap.py
verweist_auf: [training-geometry-must-cover-target-geometry, vessel-inpainting-removes-microbleeds-on-thick-slices]
---

# Thick slices cost sensitivity, not precision -- and hide the smallest microbleeds from image and reference alike

## Aussage
VALDO 2021 Task 2 (public), 57 scans in frozen 5-fold cross-validation, split by native slice spacing and by reference CMB
size (equivalent-sphere diameter of the 26-connected reference component):

| Slice | Site | Scans | CMB | found, < 2 mm | found, 2-5 mm | found, > 5 mm | wrong share of 2-5 mm detections |
|---|---|---|---|---|---|---|---|
| 0.8 mm | RSS | 27 | 80 | 38 % (5/13) | 66 % (44/67) | none annotated | 30 % |
| 3 mm | ALFA | 14 | 16 | none annotated | 62 % (8/13) | 67 % (2/3) | 48 % |
| 4 mm | ALFA | 8 | 11 | none annotated | 45 % (5/11) | none annotated | 41 % |
| 3 mm, 1 mm gaps (4 mm spacing) | SABRE | 8 | 32 | none annotated | 41 % (11/27) | 80 % (4/5) | 26 % |

- Within one size class (2-5 mm), sensitivity drops from about 0.64 (contiguous 0.8-3 mm) to about 0.43 at 4 mm slice spacing (ALFA 4 mm slices; SABRE 3 mm slices with 1 mm gaps -- correction 02.11.: SABRE was first listed as 4 mm, the header value is the spacing); within ALFA, same scanner
  and cohort, 0.62 at 3 mm against 0.45 at 4 mm.
- The share of wrong detections and false positives per scan (0.4-0.9) show no trend with thickness.
- On 3-4 mm slices no CMB smaller than 2 mm is annotated at all, and the annotated ones look LARGER (median 12-16 mm3 against
  7 mm3 at 0.8 mm), because one dot fills at least one thick slice. The smallest CMB vanish from image and reference, a loss
  no sensitivity value can show.

## Traegt
Reading results of a CMB detector on routine clinical scans (often 3 or 5 mm T2*): expect lower sensitivity at the same CMB
size, not more false alarms; report the protocol slice thickness with every result; do not compare CMB volumes across
thicknesses.

## Traegt nicht
A causal claim: thickness is confounded with site, scanner and rater in VALDO, and cells hold 11-80 CMB. VALDO has no 5 mm
scans and only 16 CMB at 3 mm, exactly the clinical range. A controlled test (thicker slices simulated from the same 0.8 mm
scans) is planned.

## Bruchindikator
The simulation from the same 0.8 mm scans shows no sensitivity drop at 4-5 mm for 2-5 mm CMB, or a rising false-positive share.

## Ablesung
Own measurement 2026-11-01 on public VALDO data (numbers may be reported). Data: Sudre et al. 2024, Where is VALDO?, Medical
Image Analysis, doi:10.1016/j.media.2023.103029, PMID 37988921. Tier 1b (one dataset, few CMB per cell).

## Verknuepft
- [training-geometry-must-cover-target-geometry](training-geometry-must-cover-target-geometry.md)
- [vessel-inpainting-removes-microbleeds-on-thick-slices](vessel-inpainting-removes-microbleeds-on-thick-slices.md)
