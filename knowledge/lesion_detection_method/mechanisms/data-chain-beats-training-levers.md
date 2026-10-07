---
id: data-chain-beats-training-levers
typ: mechanismus
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekte valdo-t2s (CMB) und wmhseg (WMH), Alita, 2026-09 bis 2026-10; uebertragen 2026-10-07
verweist_auf: [vessel-inpainting-removes-microbleeds-on-thick-slices, brain-mask-is-part-of-the-model, sensitivity-levers-do-not-raise-lesion-f1, architecture-package-brought-no-gain]
---

# Die Datenkette traegt die grossen Gewinne, das Trainingsrezept keinen

## Aussage
In zwei Linien mit kleinen Laesionen (Mikroblutungen auf T2*/SWI, WMH auf FLAIR) lagen
alle gesicherten Gewinne in der Kette VOR und NACH dem Netz, keiner im Training selbst:
- CMB: Uebermalung des Referenzverfahrens entfernt +0,136 F1; anisotropes Netz, das dem
  Gitter folgt, +0,159; parameterfreie Liquor-Regel nach dem Netz +0,061. Rund vierzig
  Eingriffe am Trainingsrezept (Verluste, Gewichtung, Synthese, Epochen, Mischen,
  Feintuning) brachten nichts oder kosteten.
- WMH: 3 % Maskenunterschied = 0,030 Dice, so viel wie der ganze Architekturgewinn; eine
  zweite Bias-Korrektur +0,011 Dice und +0,037 Laesions-Recall; ein neues Netz als Paket
  Dice unentschieden, Laesions-Recall -0,038.

Mechanismus: bei Laesionen von wenigen Voxeln entscheidet, ob das Signal nach der
Vorverarbeitung ueberhaupt noch da ist (Uebermalung, Interpolation, Maske, Normierung in
der Maske) und ob Verwechsler anatomisch ausgeschlossen werden koennen. Das Netz lernt
den Rest, und dort sind die Rezepte austauschbar.

Reihenfolge fuer eine neue Linie: (1) jeden Vorverarbeitungsschritt einzeln gegen
"weglassen" messen, mit der Referenz pruefen, wie viele Laesionen er beruehrt;
(2) Gitter und Maske festlegen; (3) Nachbearbeitung aus der Fehlalarm-Anatomie;
(4) erst dann Architektur und Rezept, und nur mit zweitem Startwert.

## Traegt
Detektion kleiner, zaehlbarer Laesionen in der MRT mit einer oder zwei Sequenzen und
wenigen Dutzend bis wenigen hundert Faellen: CMB, WMH, PVS, Lakunen.

## Traegt nicht
Grosse zusammenhaengende Strukturen (Organe, Tumoren), bei denen das Signal die
Vorverarbeitung sicher ueberlebt; dort kann das Rezept die Rangfolge bestimmen.

## Bruchindikator
Eine Linie, in der ein Trainingshebel gepaart und mit zweitem Startwert mehr bringt als
der beste Schritt der Datenkette.

## Ablesung
Eigene Messungen VALDO 2021 Task 2 und WMH Segmentation Challenge 2017, gepaart mit
Bootstrap ueber Faelle. Tier 1a. Einzelbelege in den verknuepften Eintraegen.

## Verknuepft
- [vessel-inpainting-removes-microbleeds-on-thick-slices](../../cmb_detection/findings/vessel-inpainting-removes-microbleeds-on-thick-slices.md)
- [sensitivity-levers-do-not-raise-lesion-f1](../../cmb_detection/findings/sensitivity-levers-do-not-raise-lesion-f1.md)
- [brain-mask-is-part-of-the-model](../../wmh_segmentation/findings/brain-mask-is-part-of-the-model.md)
- [architecture-package-brought-no-gain](../../wmh_segmentation/findings/architecture-package-brought-no-gain.md)
