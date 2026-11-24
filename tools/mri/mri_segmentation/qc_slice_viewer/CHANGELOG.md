# CHANGELOG

## 2026-11-24
- House colours (user rule 2026-11-24, knowledge/mri_qc_viewers/rules/overlay-house-colours-and-picture-quality.md):
  reference blue (46, 134, 171) instead of (66, 150, 255); verdict mode found green (59, 178, 115) instead of
  (0, 200, 0), false alarm **pink** (232, 23, 138) instead of yellow (255, 205, 0), missed red unchanged (235, 60, 60).
  Help text and swatches follow.
- Picture quality: the grey sheet is a lossless PNG (was JPG quality 88); the slice is windowed first as float, then
  enlarged with a cubic spline (order 3), then turned into 8 bit (was: 8 bit first, bilinear). Tile width 768 (was 640).
- Each case in `data.json` carries `sheet: "png"`; the page reads `img/<id>.<sheet>` and falls back to `jpg`, so a
  folder built before this change still works with `--refresh-html`.
- Test `tests/test_synthetic.py` extended (layer PNGs hold exactly the house colour, sheet is 8-bit grey PNG at
  least 768 wide, no `.jpg`, help text says pink, old data without `sheet` renders): passed.
- Measured on one public WMH Challenge FLAIR case (240 x 240 x 48, 48 tiles, invented prediction): grey sheet 6.9 MB
  instead of 1.8 MB; layer PNGs about 1.4 times larger (wider tiles). Page opened in a headless browser, no errors.
- Not changed: the CSF layer `csf_drop_tp` (magenta) and the run palette of the mode without verdict; both come
  close to a house colour. Pages that were already delivered are not rebuilt.

## 2026-10-08
- Erste Fassung: Seite (PAGE) aus `valdo-t2s/cmb/review/build_slice_viewer.py` (Stand 08.10., mit
  Liquor-Ebenen `__EXTRA__`), Lader manifestgesteuert nach dem Muster von `pvs-arena/skripte/qc_belove_bauen.py`
  (Vergleichsmaske statt Referenz, Zaehler = Uebereinstimmung). Laeufe als Wahrscheinlichkeit oder Maske,
  Schwelle, Mindestvolumen in mm3, Hoechstgroesse in Voxeln, Liquor-Regel je Lauf; Urteilsmodus; Liquor-Ebenen.
- Test `tests/test_synthetic.py` bestanden (tp/fp/fn 2/1/1, Urteilsmodus, Vergleichs-Wortlaut, Maskenlauf,
  Fall ohne Referenz).
- Gegenprobe an drei VALDO-Faellen (sub-104, sub-107, sub-111; Ensemble, Schwelle 0,3, 2 mm3, 2100 Voxel,
  Liquor-Ebenen an): tp/fp/fn und Kachelzahl identisch mit dem CMB-Generator (0/0/0, 2/1/0, 1/0/2; 34 Kacheln).
- Offen: Klick-Werte je Komponente, Einzeldatei-Variante, Live-Server als Teil des Tools.
