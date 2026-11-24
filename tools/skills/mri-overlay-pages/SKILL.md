---
name: mri-overlay-pages
description: Fixed house colours and picture quality for MRI slices with masks drawn on top - ground truth, second rater, true positive, false positive, false negative. Use when building or changing an HTML page, QC page, trainer, figure or film frame that shows a scan with lesion, detection or rater outlines, also for "Overlay", "TP/FP/FN-Bilder", "Ground Truth einzeichnen", "Rater-Vergleich", blurry or blocky slice pictures. Load it before planning or writing such a picture, the colours are not to be recalled from memory. Not for charts without a scan and not for the page layout itself (that is qc-page-building).
license: CC-BY-4.0
compatibility: scripts/overlay.py needs Python with numpy, scipy and Pillow (on this workstation ~/miniconda3/envs/manim/bin/python has them). assets/cubic_up.js runs in any browser.
metadata:
  author: Uchralt Temuulen
  version: "1.0"
  since: "2026-11-24"
---

# MRI overlay pages

User rule 24.11.2026: these colours and this picture quality hold for every picture of a scan with masks, without being asked again.
This skill fixes the colours and how the picture is made. The page around it (overlay switch, Methods box, hover titles, "internal, do not share") is the skill `qc-page-building`.

## Colours: never change, never reuse for something else

| Role | Colour | RGB | Hex | Drawn as |
|---|---|---|---|---|
| ground truth (reference, rater 1) | blue | 46, 134, 171 | #2E86AB | ring inside the mask |
| second rater | orange | 232, 135, 30 | #E8871E | ring inside the mask, one step further in where it lies on a ground-truth lesion |
| true positive (found) | green | 59, 178, 115 | #3BB273 | ring around the found cluster |
| false positive (false alarm) | pink | 232, 23, 138 | #E8178A | ring around the found cluster |
| false negative (missed) | red | 235, 60, 60 | #EB3C3C | ring around the missed ground-truth lesion |

1. Take the colours from `scripts/overlay.py` (`COL`) or this table. Never retype them from memory, never pick "a nicer" shade.
2. A generator, tool or old page with other colours (for example yellow for false positives) gets these colours before the page is built. Say in the report what you changed. Do not change a shared tool or an already delivered page without asking; write your own page with the right colours and report the difference.
3. Every page and every figure has a legend with words: colour name = role. Never colour alone. `legend_html(roles)` writes it.
4. A layer that is none of the five (brain mask, another model, a region) gets a colour that is none of the five and its own legend line.
5. Outlines, not filled masks: the lesion itself must stay visible. Outlines are a separate transparent picture, so that the switch "Overlays: ON/OFF (O)" works.

## Picture quality

1. **Window first, then enlarge.** Clip to the display window, then upsample with a cubic spline (order 3). Never enlarge with nearest neighbour, never leave the enlarging to the browser.
2. **Enough points:** at least 3 points per voxel, main view at least 768 points wide (128 voxels x 6, 256 x 3).
3. **Masks are never smoothed.** Enlarge them by repeating voxels, then draw the ring. Counts, Dice and volumes are computed on the native voxels, never on the enlarged picture.
4. **PNG, lossless.** Scan as 8-bit grey PNG, outlines as RGBA PNG of the same size. No JPEG. No PDF for pictures.
5. Show the picture at its own size (`width` and `height` in CSS equal to the file), or in whole-number steps.
6. Write on the page: orientation, window, upsampling factor, and how a hit is counted.

## How

Python, pictures made before the page (QC pages, figures, film frames):

```python
import sys; sys.path.insert(0, "<this skill>/scripts")
from overlay import COL, verdict, save_pair, legend_html
layers = dict(gt=truth_slice, rater2=rater2_slice, **verdict(found_slice, truth_slice))   # leave out what the page does not have
save_pair("out/case_z", scan_slice, layers, scale=(6, 6), lo=window_low, hi=window_high)   # writes case_z.png and case_z_o.png
```

`verdict` counts by connected clusters that touch. If the project counts a hit differently (distance, overlap share, 3-D clusters), compute tp, fp, fn with the project's rule on the volume and pass the slices; state the rule on the page.
Voxels that are not square: give `scale` per axis so that the picture has the true proportions, for example `(6, 3)`.

In the browser, when the page carries the raw slices (trainers): `assets/cubic_up.js`, `cubicUp(grey, w, h, factor)`; draw masks on the canvas with `imageSmoothingEnabled = false`.

Working example with all five roles on a synthetic phantom: `python scripts/overlay.py --demo <folder>`.

## Check before you report

Take a screenshot of the page and look at it (commands in `qc-page-building`); for small lesions cut an enlarged crop. Passed when: every role on the page is in the legend with its word, the outlines are sharp, the scan shows no blocks, the switch hides all outlines, and a small lesion is still visible inside its ring.
Pages with patient scans: only the local model or a flat grey placeholder may be looked at by a remote model (`save_pair(..., hide=True)` gives the layout without the scan); the page says "internal, do not share".

## When it fails

- Outlines look washed out: the mask was smoothed or saved as JPEG; repeat voxels, save PNG.
- Thin white or black edge around bright structures: the window was applied after the upsampling; window first.
- Two raters agree and only one ring shows: both masks are identical; the second-rater ring is set one step inside, keep `width` at 2 or more and the scale at 4 or more.
- A one-voxel lesion disappears under its ring: raise the scale, do not thin the ring below 2.
- The page is too large: PNG is lossless and larger than JPEG; cut the picture to the brain or show fewer slices, do not go back to JPEG.
