---
id: valdo-cohort-3-mask-is-a-head-mask
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), gemessen 2026-09-19
verweist_auf: [valdo-t1-carries-nan-in-33-of-72-cases, csf-rule-removes-false-alarms-without-loss]
---

# Die gelieferten VALDO-Masken sind nicht eng: Kohorte 3 ist eine Kopfmaske

## Aussage
Die `*_desc-masked_T2S`-Bilder von VALDO 2021 Task 2 sind ausserhalb einer Maske genullt, aber die
Maske ist je Kohorte etwas anderes. Volumen und Anteil ausserhalb des SynthSeg-Hirns:

| Kohorte | Maskenvolumen | Anteil Nicht-Hirn |
|---|---|---|
| 1 | 1 419 ml | 4 % |
| 2 | 1 770 ml | 16 % |
| 3 | 2 533 ml | 40 % |

Kohorte 3 enthaelt Schaedelknochen, Kopfhaut und an der Basis den ganzen Kopfquerschnitt.
Keine Referenz-CMB liegt ausserhalb irgendeiner Maske. Die Aussage "Bilder bereits hirnmaskiert,
Skull-Stripping entfaellt" hatte nur "Nullen ausserhalb" geprueft, nicht "eng"; die Zahlenpruefung
("0 von 236 CMB abgeschnitten") beantwortete die falsche Frage. Aufgefallen erst am Bild.

Abhilfe: Hirnmaske aus SynthSeg (> 0, aus dem T1 im T2*-Raum, 2 Voxel geweitet) fuer alle 72 Faelle;
alternativ HD-BET. Eine Maske immer zweifach pruefen: schneidet sie etwas ab UND wie viel Nicht-Hirn
laesst sie drin (Volumen in ml gegen 1 200-1 500 ml). Bilder ansehen, nicht nur Summen.

## Traegt
Jede Kette auf VALDO Task 2, und jede Annahme "ist schon maskiert" bei fremden Datensaetzen.

## Traegt nicht
Ob die weite Maske das F1 kostet, ist nicht getrennt gemessen (Maskenvariante lag in der
Startwert-Streuung, siehe [two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md)).

## Bruchindikator
Eine neue VALDO-Fassung mit engen Masken.

## Ablesung
Eigene Messung an den gelieferten Dateien (Sudre et al. 2024, doi:10.1016/j.media.2023.103029). Tier 1a.

## Verknuepft
- [valdo-t1-carries-nan-in-33-of-72-cases](valdo-t1-carries-nan-in-33-of-72-cases.md)
- [csf-rule-removes-false-alarms-without-loss](csf-rule-removes-false-alarms-without-loss.md)
- [brain-mask-is-part-of-the-model](../../wmh_segmentation/findings/brain-mask-is-part-of-the-model.md)
