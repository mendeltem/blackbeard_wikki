---
id: architecture-package-brought-no-gain
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: [brain-mask-is-part-of-the-model, literature-dice-levers-for-wmh]
---

# Ein als Paket geaendertes Netz brachte keinen Gewinn und kostete Laesions-Recall

## Aussage
Eine neue Architektur (3,1 M Parameter, 5x5-Eingang, starke Augmentierung, robuste Normierung,
TTA, 60 statt 40 Epochen) schien +0,032 Dice besser. Auf einheitlicher Maske, gepaart auf
110 Challenge-Testfaellen, Bootstrap-KI95:

| Vergleich | Dice | Laesions-Recall | Laesions-F1 |
|---|---|---|---|
| alt -> neu, Einzelmodell | -0,001 unentschieden | **-0,038 schlechter** | -0,013 unentschieden |
| alt -> Ensemble (3 Startwerte) | -0,002 unentschieden | **-0,037 schlechter** | -0,003 unentschieden |

Ausfaelle praktisch gleich. Das auszuliefernde Modell blieb das alte. Weil die Architektur als
PAKET geaendert wurde, ist unklar, welcher Teil schadet; Verdacht: die starke Augmentierung
glaettet (8,9 Herde weniger je Fall bei gleichem Gesamtvolumen).

Die Fehlerkette davor: zwei Modelle verglichen, ohne die Maskenherkunft zu pruefen, und den
Unterschied dreimal hintereinander falsch erklaert (Perzentil, Vorverarbeitungskette,
Augmentierung), bevor die Maske gefunden war. Regel: vor jedem Modellvergleich pruefen, ob
beide Messungen dieselben Eingaben UND dieselben Masken benutzen -- und Bausteine einzeln
aendern, sonst ist ein Negativbefund nicht zuordenbar.

## Traegt
Jede Architekturentscheidung mit erwartetem Gewinn unter 0,03 Dice.

## Traegt nicht
Datensaetze mit anderer Laesionslast; der Recall-Verlust kann dort anders ausfallen.

## Bruchindikator
Ein Baustein des Pakets, einzeln gemessen, hebt Dice oder Laesions-Recall gepaart mit Intervall ohne Null.

## Ablesung
Eigene Messung, 110 oeffentliche Challenge-Testfaelle, 2026-09-13. Tier 1a.

## Verknuepft
- [brain-mask-is-part-of-the-model](brain-mask-is-part-of-the-model.md)
- [literature-dice-levers-for-wmh](literature-dice-levers-for-wmh.md)
