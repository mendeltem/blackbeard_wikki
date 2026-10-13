---
id: demdas-cortical-thickness-qc-page
typ: befund
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-12
herkunft: wd3 DEMDAS cortical thickness (Alita, demdas-gm/thickness_table.py, thickness_qc.py, recon-all 8.2 cross-sectional), user request 12.10.2026 "cortical thickness as a QC page and table, DEMDAS priority one"
verweist_auf: [qc-pages-explain-every-number-on-hover, qc-pages-english-sessions-in-one-window]
---

# DEMDAS cortical thickness QC page: how every number is computed (long form of the "? Methods" overlay)

## Aussage
Long form of the texts shown on hover and in the Methods overlay of
`QUALITY_CONTROLL/DEMDAS/cortical_thickness/index.html`. English on purpose: the page
may go to third parties. No patient data here, only methods. Software versions as
installed on Alita on 2026-10-12.

**Pipeline.** FreeSurfer 8.2.0 `recon-all -all`, run **independently on every session**
(cross-sectional, one recon-all per session; `SUBJECTS_DIR=
/home/uchralt/data/derivatives/demdas/freesurfer`, log `alle.log`). There is **no
longitudinal stream, no group-average template, no `-ctk`** — surfaces and thicknesses
of different sessions of one participant are therefore NOT registered to each other.
The slope is a simple linear trend of per-session cross-sectional thickness, not a
longitudinal measurement (stated explicitly on the page).

**Numbers.**
- Mean thickness lh / rh (mm): `ThickAvg` of each of the 34 Desikan-Killiany regions in
  `stats/lh.aparc.stats` / `rh.aparc.stats` (distance between the white and pial surface
  at every vertex, averaged over the vertices of the region), then the unweighted mean
  over all 34 regions. `ThickAvg` is what `mris_anatomical_stats` writes.
- Mean thickness (both hemispheres): `(lh + rh) / 2`, unweighted (region surface areas
  differ slightly, so this is not the surface-area-weighted cortex-wide mean).
- eTIV (ml): `EstimatedTotalIntraCranialVol` from `stats/aseg.stats`.
- Slope (mm/year): least-squares slope of the line through (months, mean thickness) of
  all finished sessions of that participant, x 12; shown only with >= 2 sessions.
- Plot: one line per hemisphere plus the mean over session months; dotted = least-squares
  fit of the mean; green band = cohort median of the mean thickness at the M0 sessions
  (25th-75th percentile band).

**Image.** ONE axial image per session: `T1.mgz` in grayscale with `aparc+aseg.mgz`
labels coloured by the FreeSurfer colour LUT (60/40 blend), all axial slices tiled in a
square grid (same mosaic style as the GM page). Left/right keys = slice, up/down =
session of the same participant, PgUp/PgDn = participant.

**Missing sessions.** Listed with the reason "recon-all not finished as of <date>"; the
page is rebuilt (thickness_table.py + thickness_qc.py) when `status_check.sh` reports
`fehlend=0`.

**Finished definition.** A session is finished when recon-all has written both
`surf/lh.thickness` and `surf/rh.thickness` (same definition as `status_check.sh` and the
acceptance test). If aparc.stats lags the thickness surface by a few minutes, the summary
row falls back to the mean of the decoded `.thickness` surface so the finished set always
matches the disk.

## Software (versions)
FreeSurfer 8.2.0; Python 3.12 (conda env `dl`); nibabel; numpy; Pillow; openpyxl (xlsx
sheet "Cortical thickness"); Chromium (headless) for the acceptance screenshot. CPU only,
GPU untouched.
