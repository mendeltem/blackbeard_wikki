# lesion_detection_method

Uebertragbare Methode fuer die Detektion kleiner, zaehlbarer Laesionen in der MRT.
Destilliert aus zwei vermessenen Linien, Mikroblutungen (cmb_detection, VALDO 2021) und
WMH (wmh_segmentation, Challenge 2017), als Mechanismen und Regeln ohne Fachbezug, mit
einem offenen Pruefpunkt, der sie auf eine dritte Linie anwendet (PVS, perivaskulaere
Raeume). Die Belege liegen in den Fachbereichen; hier steht, was davon auf die naechste
Linie uebergeht und wo es nicht traegt.

Stand 2026-10-07. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt | Status |
|---|---|---|---|
| mechanismus | [data-chain-beats-training-levers](mechanisms/data-chain-beats-training-levers.md) | Alle gesicherten Gewinne lagen vor und nach dem Netz (Uebermalung, Gitter, Maske, Ortsregel); rund vierzig Rezept-Hebel brachten nichts | getragen |
| mechanismus | [sensitivity-needs-a-discriminator](mechanisms/sensitivity-needs-a-discriminator.md) | Empfindlichkeit kauft Fehlalarme; Fortschritt braucht einen Trenner (mehr Sequenzen oder EINE zweite Stufe ueber alle Kohorten); Schwellensaetze sind Arbeitspunkte | getragen |
| mechanismus | [false-alarms-cluster-by-anatomy](mechanisms/false-alarms-cluster-by-anatomy.md) | Fehlalarme nach Ort zaehlen; parameterfreie Regel NACH dem Netz schlaegt Karte VOR dem Netz; bei Liquor-tragenden Laesionen nur ueber Lage | getragen |
| mechanismus | [geometry-follows-the-acquisition](mechanisms/geometry-follows-the-acquisition.md) | Erste Ebene nur in der Schicht bei dicken Schichten; Patches statt Bilder; 2D-Netze wiegen Schnitte, nicht Faelle | getragen |
| regel | [reference-first-then-metric-then-model](rules/reference-first-then-metric-then-model.md) | Pipeline-Ausgaben sind keine Wahrheit; Instanzmass gepaart mit Bootstrap; Auswerteregel der Referenz wortgetreu | getragen |
| regel | [noise-floor-before-effects](rules/noise-floor-before-effects.md) | Drei Startwerte zuerst (~0,08 F1); Verlust ordnet nichts; Vorpruefungen ordnen, entscheiden nicht; Regel vor dem Lauf | getragen |
| regel | [count-cases-behind-pooled-numbers](rules/count-cases-behind-pooled-numbers.md) | 3 Faelle = 28 % der Blutungen; Verteilung je Fall mitberichten, gepaart ueber Faelle, keine "ersten N" | getragen |
| regel | [operating-points-do-not-transfer](rules/operating-points-do-not-transfer.md) | Schwelle gehoert zu Modell und Scanner (0,415 statt 0,622 bei uebernommener Schwelle); zweite Stufe faengt es ab | getragen |
| regel | [pipeline-failures-and-names-before-tuning](rules/pipeline-failures-and-names-before-tuning.md) | Stille Leerausgaben bei rc 0, technische Fehlschlaege zuerst, Namen am Code messen | getragen |
| pruefpunkt | [pvs-apply-the-lesion-method](open_checks/pvs-apply-the-lesion-method.md) | PVS-Kohorte (103 Faelle, T1 1 mm, FLAIR 5 mm, RORPO-Pipeline, 11 Schwellensaetze, 31 Fehlschlaege, keine Referenz): sieben Schritte in Reihenfolge | offen |

## Herkunft
cmb_detection (valdo-t2s, 2026-09-10 bis 2026-10-07) und wmh_segmentation (wmhseg,
2026-09-12 bis 2026-09-18), zusammengefasst am 2026-10-07 auf Wunsch von Mendel als
Meta-Wissen fuer kommende Linien; PVS-Datenlage aus der Bestandsaufnahme des Clusters.
