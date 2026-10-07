---
id: training-geometry-must-cover-target-geometry
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), scripts/loco_t2.sh, Leave-one-cohort-out ueber vier T2*-Kohorten, 2026-10-07 abends
verweist_auf: [full-data-last-state-models-run-hotter, two-seeds-per-decision-below-0.08]
---

# Die Schichtgeometrie der Trainingsdaten muss die Zielgeometrie abdecken -- mehr Faelle anderer Geometrie ersetzen das nicht

## Aussage
Leave-one-cohort-out ueber vier T2*-Kohorten (VALDO 1: 4 mm, 11 Faelle; VALDO 2: 0,8 mm, 34;
VALDO 3: 3-4 mm, 27; klinische Kohorte: 5 mm, 75), Training auf drei, Test auf der vierten,
Laesions-F1 auf denselben Faellen gegen die Faltenmodelle, die die Kohorte im Training hatten:

- **4 mm weggelassen:** 0,577 gegen 0,576 -- kein Verlust; die 5-mm-Kohorte deckt die Geometrie ab.
- **0,8 mm weggelassen:** 0,295 gegen 0,641 roh, 0,503 gegen 0,707 mit Liquor-Regel -- halbe
  Sensitivitaet, viermal so viele Fehlalarme, obwohl 113 statt 46 Faelle im Training waren.
- **3-4 mm weggelassen:** 0,409 gegen 0,476 (22 Faelle, im Rauschen).
- **5 mm weggelassen** (nur VALDO im Training): 0,336 roh gegen 0,663 eigenes Training; kreuzgewaehlt
  0,583, mit zweiter Stufe 0,571.

Ein Netz, das nur dicke Schichten kennt, versagt auf duennen; eines, das nur duenne und mittlere
kennt, ueberdetektiert auf dicken (32 Fehlalarme je Fall). Die Fallzahl aus anderen Geometrien
hilft nicht, weil das Rezept ein festes Budget je Epoche hat und die Unterscheidung Blutung /
Gefaess an der Schichtdicke haengt.

## Traegt
Planung von Trainingsdaten fuer Laesionsdetektion: je Zielgeometrie (Schichtdicke, Aufloesung)
muessen Faelle im Training sein; "mehr Daten" aus anderen Scannern sind kein Ersatz. Vor dem
Einsatz auf neuen Daten: Schichtdicke pruefen und das Modell nehmen, dessen Training sie enthaelt.

## Traegt nicht
Aussagen ueber Sequenzen (T2* gegen SWI) -- dort ist der Verlust noch groesser und schon bekannt;
und ueber Startwert-Rauschen: ein Seed, zweiter Seed und Ensemble folgen (Freitags-Warteschlange).

## Bruchindikator
Ein zweiter Seed oder ein Ensemble, bei dem die 0,8-mm-Kohorte ohne sich selbst auf das Niveau der
Faltenmodelle kommt (Differenz unter 0,08).

## Ablesung
Eigene Messung 2026-10-07, VALDO 2021 Task 2 (oeffentlich) und eine klinische Kohorte (nur Summen),
gepoolte Laesions-F1 auf identischen Faellen. Tier 1a.

## Verknuepft
- [full-data-last-state-models-run-hotter](full-data-last-state-models-run-hotter.md)
- [two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md)
