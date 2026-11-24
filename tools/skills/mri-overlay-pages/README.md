---
id: mri-overlay-pages
bereich: tools/skills
stand: 2026-11-24
herkunft: own build 2026-11-24 on user request (fixed colours and best picture quality for MRI pictures with ground truth, second rater, TP, FP, FN, so that they are not said again); picture quality from the trainer rework of 2026-11-23/24
sprache: markdown, python, javascript
---

# mri-overlay-pages: Agent Skill for MRI slices with masks drawn on top

## Purpose
Fixes two things for every picture of a scan with masks, on an HTML page, a QC page, a trainer, a figure or a film
frame: the colours of the five roles and how the picture is made.

| Role | Colour | RGB | Hex |
|---|---|---|---|
| ground truth (reference, rater 1) | blue | 46, 134, 171 | #2E86AB |
| second rater | orange | 232, 135, 30 | #E8871E |
| true positive (found) | green | 59, 178, 115 | #3BB273 |
| false positive (false alarm) | pink | 232, 23, 138 | #E8178A |
| false negative (missed) | red | 235, 60, 60 | #EB3C3C |

Picture quality: window first, then cubic upsampling (order 3) in the generator; at least 3 points per voxel; masks
enlarged by repeating voxels and drawn as outlines on a separate transparent PNG; lossless PNG, no JPEG; shown at its
own size. Rule entry: [overlay-house-colours-and-picture-quality](../../../knowledge/mri_qc_viewers/rules/overlay-house-colours-and-picture-quality.md).

A picture of the demo page (synthetic phantom, no scan) is in the rule entry. Make it yourself with
`python scripts/overlay.py --demo <folder>`.

## When to use, when not
Use whenever a scan is shown with lesion, detection or rater outlines. Not for charts without a scan, and not for the
layout of the page around the picture.

## Install
    cp -r tools/skills/mri-overlay-pages ~/.agents/skills/mri-overlay-pages
    ln -s ~/.agents/skills/mri-overlay-pages ~/.claude/skills/mri-overlay-pages     # Claude Code

`scripts/overlay.py` needs Python with numpy, scipy and Pillow. `assets/cubic_up.js` runs in any browser.

## Call
    from overlay import COL, verdict, save_pair, legend_html
    layers = dict(gt=truth_slice, rater2=rater2_slice, **verdict(found_slice, truth_slice))
    save_pair("out/case_z", scan_slice, layers, scale=(6, 6), lo=window_low, hi=window_high)

writes `case_z.png` (scan, 8-bit grey) and `case_z_o.png` (transparent outlines of the same size).

## Test state
2026-11-24, numpy 2.4.6, scipy 1.17.1, Pillow 13.0.0, Chromium headless: the demo page was built from the installed
copy, looked at as a screenshot and as enlarged crops (all five roles in the legend with words, scan smooth, outlines
crisp, the switch hides all outlines). `verdict` on a 3-D test volume gave the expected 4 found, 1 false alarm,
1 missed. Non-square scale (6, 3), the grey placeholder (`hide=True`) and the refusal of an unknown role work.
`cubic_up.js` passed its node test (taken from the WMH trainer, MIT, commit 06e8190 of github.com/mendeltem/wmh_trainer).

## Limits
Not yet tested on a real scan, and no run with and without the skill was made. The values of red and blue, and how
the outlines are placed (rater marks inside the mask, verdicts around it, the second rater one step further in on a
shared lesion) were chosen by the author of the skill; the user fixed the colour names and the roles. The shared
viewer generator in this wiki still draws false alarms yellow and its reference in another blue (66, 150, 255); see
the rule entry.
