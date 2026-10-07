---
id: valdo-t1-carries-nan-in-33-of-72-cases
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), gemessen 2026-09-14
verweist_auf: [valdo-cohort-3-mask-is-a-head-mask]
---

# 33 von 72 VALDO-T1-Bildern tragen NaN, und der Segmentierer scheitert daran lautlos

## Aussage
`<sub>_space-T2S_desc-masked_T1.nii.gz` von VALDO 2021 Task 2 enthaelt bei **33 von 72** Faellen NaN:
sub-101 bis 106 rund 23 % der Voxel, sub-301 bis 327 (alle 27) 34-38 %. `_T2S` und `_CMB` sind bei
allen Faellen sauber; in Kohorte 3 traegt zusaetzlich `_T2` NaN. Es sind die GELIEFERTEN Dateien.

Teuer ist der lautlose Ausfall: NaN vergiftet die Perzentilnormierung von `mri_synthseg`, das Netz
gibt ueberall Hintergrund aus, **Rueckgabewert 0, Ausgabedatei vorhanden**. Erst die nachgelagerte
Rasterumrechnung faellt auf ("nur 1 Label"), und der Fall wird verworfen; die Rasterumrechnung stand
zwei Stunden zu Unrecht unter Verdacht. Kein Gegenbeispiel in beide Richtungen: jeder NaN-Fall
scheitert, jeder saubere liefert 33 Labels in 20-22 s.

Die Reparatur ist eine Zeile im Ladeschritt und geprueft sicher: `np.nan_to_num(..., nan=0.0)`.
Die NaN bilden eine Randschale vom Umrastern ausserhalb des Quellbilds (eine zusammenhaengende
Komponente am Volumenrand, nach dreifacher Erosion der Hirnmaske kein NaN im Inneren); Nullsetzen
erfindet keine Anatomie. An echten Daten bestaetigt: sub-304 von 1 Label / 0 Voxel auf 33 Labels /
1,65 M Voxel. Gelieferte Dateien nicht aendern.

Zwei Fallen beim Nachbauen: der Segmentierer leitet den AUSGABEnamen aus dem EINGABEnamen ab --
eine bereinigte Kopie erzeugt eine zweite Ausgabe neben der alten leeren, und ein Muster ohne
`sorted` erwischt die alte. Und er ueberspringt vorhandene Ausgaben nur bei GLEICHEM Namen.

## Traegt
Jede Kette, die VALDO-T1 nutzt (SynthSeg, Registrierung, Mehrkanal-Eingabe). Allgemein: bei jedem
neuen Bilddatensatz einmal `np.isnan(...).sum()` je Modalitaet zaehlen, bevor eine Kette laeuft.

## Traegt nicht
Ketten, die nur T2* und CMB-Referenz lesen; dort sind die Daten sauber.

## Bruchindikator
Eine korrigierte VALDO-Fassung ohne NaN.

## Ablesung
Eigene Zaehlung ueber alle 72 Faelle (Sudre et al. 2024, doi:10.1016/j.media.2023.103029). Tier 1a.

## Verknuepft
- [valdo-cohort-3-mask-is-a-head-mask](valdo-cohort-3-mask-is-a-head-mask.md)
- [empty-is-not-missing](../../agent_tooling/rules/empty-is-not-missing.md)
