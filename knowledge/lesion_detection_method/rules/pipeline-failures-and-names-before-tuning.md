---
id: pipeline-failures-and-names-before-tuning
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekte valdo-t2s (CMB) und wmhseg (WMH), 2026-09-14 bis 2026-09-21; uebertragen 2026-10-07
verweist_auf: [valdo-t1-carries-nan-in-33-of-72-cases, valdo-cohort-3-mask-is-a-head-mask, empty-target-looks-like-a-low-loss]
---

# Fehlschlaege, stille Leerausgaben und Benennungen pruefen, bevor man tunt

## Aussage
Drei Fehlerklassen, die in beiden Linien vor jedem Modell lagen und billig zu finden waren:
1. **Stille Leerausgaben.** 33 von 72 T1-Bildern trugen NaN in einer Randschale; der
   Segmentierer lieferte dafuer ein leeres Bild bei Rueckgabewert 0. Ein gedrehtes Bild
   ohne mitgedrehtes Ziel ergab 0 Zielvoxel im Training, und der geglaettete Dice meldete
   einen perfekten Verlust. Rueckgabewerte und niedrige Verluste sind keine Pruefung;
   pruefen heisst: Ausgabe oeffnen, Voxel zaehlen, Masken-Anteil Nicht-Hirn messen
   (Kohorte 3: 40 %).
2. **Technische Fehlschlaege zuerst.** Fehlertexte wie "Orientierung", "Dateityp",
   "unrecognized" sind Technik, nicht Anatomie; ein Drittel ausgefallener Faelle ist meist
   der billigste Gewinn der ganzen Linie und veraendert jede spaetere Zahl.
3. **Benennung gegen den Code.** "3D-ResNet" ohne Residuen, "60 feste Epochen" mit
   Zwischenstandswahl, "HD-BET-Masken", die mitgeliefert waren: Namen vor dem Berichten
   am Code messen. Bei uebernommenen Pipelines gilt das doppelt: welcher Filter laeuft
   wirklich, auf welcher Sequenz, mit welcher Maske?

Reihenfolge: (2) Fehlschlaege reparieren, (1) jede Zwischenausgabe einmal zaehlen,
(3) die Pipeline in eigenen Worten beschreiben und am Code pruefen; erst dann Schwellen
oder Modelle anfassen.

## Traegt
Jede uebernommene Pipeline, jeder neue Datensatz.

## Traegt nicht
Nichts bekannt; die Pruefung kostet Stunden, nicht Tage.

## Bruchindikator
Ein Datensatz, auf dem alle drei Pruefungen leer ausgehen -- dann war es nur billig,
nicht noetig.

## Ablesung
Eigene Befunde VALDO 2021 Task 2 und WMH-Linie. Tier 1a.

## Verknuepft
- [valdo-t1-carries-nan-in-33-of-72-cases](../../cmb_detection/findings/valdo-t1-carries-nan-in-33-of-72-cases.md)
- [valdo-cohort-3-mask-is-a-head-mask](../../cmb_detection/findings/valdo-cohort-3-mask-is-a-head-mask.md)
- [empty-target-looks-like-a-low-loss](../../wmh_segmentation/risks/empty-target-looks-like-a-low-loss.md)
