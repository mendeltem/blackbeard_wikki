---
id: operating-points-do-not-transfer
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekt valdo-t2s (CMB), full_data-Vollmodelle 2026-10-07, catalina-Transfer 2026-09; uebertragen 2026-10-07
verweist_auf: [full-data-last-state-models-run-hotter, sensitivity-needs-a-discriminator]
---

# Arbeitspunkte gehoeren zum Modell und zum Scanner, nie zu einem anderen Lauf

## Aussage
Eine Schwelle (Wahrscheinlichkeit, Vesselness, Mindestgroesse) ist ein Arbeitspunkt auf
der Sensitivitaet-Fehlalarm-Kurve EINES Modells auf EINER Datenverteilung. Beispiele:
- Ein auf allen Faellen trainiertes Vollmodell ohne inneren Checkpoint ist "heisser" als
  das Faltenensemble: feste Schwelle 0,3 auf fremdem Scanner 0,415 statt 0,622 F1;
  mit kreuzgewaehlter Schwelle gleichauf. Die zweite Stufe faengt die Verschiebung ab.
- Elf durchprobierte Schwellensaetze einer Pipeline sind elf Arbeitspunkte, von denen
  keiner "der richtige" ist, solange nicht gesagt ist, auf welcher Referenz und welchem
  Scanner er gewaehlt wurde.

Vorschriften:
- Arbeitspunkt immer out-of-fold oder auf einer Haltemenge DESSELBEN Modells waehlen und
  mit dem Modell abspeichern (Modell + Schwelle + Mindestgroesse = eine Einheit).
- Beim Wechsel auf einen anderen Scanner oder eine andere Kohorte zuerst die Kurve
  neu messen, nicht die Schwelle uebernehmen.
- Wo die Schwelle unvermeidlich wandert (Vollmodell, neuer Scanner), eine kleine zweite
  Stufe mit eigener, stabiler Schwelle dahinter setzen; sie streut nur 0,003 bis 0,009.

## Traegt
Jeden Detektor, der mit einer Schwelle ausgeliefert wird; jede uebernommene Pipeline mit
Parameterdateien.

## Traegt nicht
Modelle, deren Ausgabe kalibriert und ueber Scanner geprueft ist (bisher keines gesehen).

## Bruchindikator
Ein Modell, dessen feste Schwelle auf drei fremden Scannern innerhalb des Rauschbodens
dasselbe F1 liefert wie die kreuzgewaehlte.

## Ablesung
Eigene Messungen VALDO 2021 Task 2 und eigene Kohorten (nur Summen). Tier 1a.

## Verknuepft
- [full-data-last-state-models-run-hotter](../../cmb_detection/findings/full-data-last-state-models-run-hotter.md)
- [sensitivity-needs-a-discriminator](../mechanisms/sensitivity-needs-a-discriminator.md)
