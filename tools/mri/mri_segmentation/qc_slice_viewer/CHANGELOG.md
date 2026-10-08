# CHANGELOG

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
