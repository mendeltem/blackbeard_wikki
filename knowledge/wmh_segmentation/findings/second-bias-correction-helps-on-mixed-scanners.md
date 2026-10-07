---
id: second-bias-correction-helps-on-mixed-scanners
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: [brain-mask-is-part-of-the-model]
---

# Eine zweite Bias-Korrektur hilft auf gemischten Scannern, obwohl sie nichts korrigieren sollte

## Aussage
Die Challenge-Daten sind bereits mit SPM12 bias-korrigiert (Li et al. 2018). Ein zweiter
Durchgang mit FSL `fast -B` war deshalb a priori ueberfluessig und wurde gestrichen.
Gemessen ist das Gegenteil: 3 gegen 3 Startwerte, 2D-U-Net, 40 Epochen, dieselben 12
Validierungs- und 110 Testfaelle, offizielle Metrik.

| Kette | Dice je Startwert | Mittel | Streuung |
|---|---|---|---|
| mit `fast -B` | 0,7689 / 0,7701 / 0,7719 | 0,7703 | 0,0030 |
| ohne `fast -B` | 0,7636 / 0,7588 / 0,7551 | 0,7591 | 0,0085 |

Gepaart ueber 110 Faelle: Dice **-0,011** [-0,016; -0,006], Laesions-Recall **-0,037**
[-0,045; -0,028], Laesions-F1 unentschieden. Welch ueber Startwerte p = 0,034.
Deutung: `fast -B` wirkt hier nicht als Bias-Korrektur, sondern als Intensitaets-
Vereinheitlichung ueber Scanner hinweg; dazu passt, dass der Laesions-Recall (FINDEN schwacher
Herde) viel staerker leidet als der Dice. Nebenbefund: ohne den Schritt streut das Training
ueber Startwerte fast dreimal so stark -- der Schritt stabilisiert auch das Training.

Die Schaetzung der Groesse ist dreimal gewandert (0,013 -> 0,009 -> 0,011), jedes Mal durch
einen weiteren Lauf. Belastbar: Richtung sicher, Groesse etwa 0,01, keine dritte Nachkommastelle.

## Traegt
Training auf FLAIR aus mehreren Scannern, wenn die Vorverarbeitungskette ohnehin ein FSL-`fast` enthaelt. Die Heuristik "nichts zweimal anwenden" bleibt gut, ersetzt aber die Messung nicht.

## Traegt nicht
Einzelscanner-Daten; dort ist der Effekt nicht gemessen. Und: 3 gegen 3 Startwerte sind duenn, das Intervall ist ueber Faelle gerechnet, nicht ueber Laeufe.

## Bruchindikator
Fuenf oder mehr Startwerte je Kette ohne Unterschied im Laesions-Recall.

## Ablesung
Eigene Messung auf den 110 oeffentlichen Challenge-Testfaellen; Vorverarbeitung der Veranstalter: Li et al. 2018, arXiv:1802.05203. Tier 1a (eigene Messung), 1b (Paper).

## Verknuepft
- [brain-mask-is-part-of-the-model](brain-mask-is-part-of-the-model.md)
- [literature-dice-levers-for-wmh](literature-dice-levers-for-wmh.md)
