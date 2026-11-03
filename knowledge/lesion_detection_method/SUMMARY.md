# lesion_detection_method: Kurzstand

**New 2026-11-03:** The Lead-DBS release of the GSP1000 connectome has x mirrored in its header against the NIfTI release of the same time courses; the NIfTI orientation is supported by anatomy and language lateralisation. Whether Lead Mapper is affected is unverified. [[gsp1000-leaddbs-header-left-right-mirror]]

Stand 2026-10-07. Prefill fuer jede neue Linie mit kleinen Laesionen (PVS, Lakunen,
neue CMB- oder WMH-Kohorten). Details in [INDEX.md](INDEX.md), Belege in
cmb_detection und wmh_segmentation.

**Reihenfolge, die sich in zwei Linien bewaehrt hat:** (1) Referenz klaeren, sonst gibt es
keine Zahl; Pipeline-Ausgaben sind keine Wahrheit. (2) Technische Fehlschlaege reparieren,
jede Zwischenausgabe einmal oeffnen und zaehlen (stille Leerausgaben bei Rueckgabewert 0,
Masken mit 40 % Nicht-Hirn, NaN-Randschalen), Pipeline-Namen am Code pruefen.
(3) Instanzmass je Fall gepaart mit Bootstrap; Verteilung je Fall mitberichten, weil
drei Faelle ein Viertel der Laesionen tragen koennen. (4) Rauschboden mit drei
Startwerten (~0,08 F1 bei U-Nets), Entscheidungsregel vor dem Lauf. (5) Erst dann
Modelle.

**Wo die Gewinne liegen:** in der Datenkette vor und nach dem Netz (Uebermalung weg
+0,136, Gitter, das der Aufnahme folgt, +0,159, Ortsregel aus der Gewebekarte +0,061;
WMH: 3 % Maske = 0,030 Dice), nicht im Trainingsrezept (rund vierzig Hebel ohne Gewinn).

**Was nicht funktioniert:** Empfindlichkeit erhoehen ohne Trenner (jeder Hebel kauft
Fehlalarme); Schwellen durchprobieren (Arbeitspunkte, kein Fortschritt); Schwellen von
einem Lauf auf einen anderen uebernehmen (0,415 statt 0,622); Netze auf Voxel-Ebene ueber
Kohorten mischen. Was funktioniert: EIN kleiner Kandidaten-Klassifikator ueber alle
Kohorten als zweite Stufe, parameterfreie Ortsregeln nach dem Netz, Patches und
Schiebefenster.

**Offen:** die Uebertragung auf PVS ist ein Plan mit sieben Schritten
([pvs-apply-the-lesion-method](open_checks/pvs-apply-the-lesion-method.md)), keine
Messung; bei PVS sind die Verwechsler andere (Gefaesse, Lakunen) und die Laesion traegt
selbst Liquorsignal, Ortsregeln also nur ueber Lage.

**Lesen bei:** neue Laesionslinie, uebernommene Pipeline, Parameterdateien ohne Herkunft,
PVS, Lakunen, Kandidaten-Klassifikator, Fehlalarme, Referenzmasken, Startwert-Rauschen.
- 08.10.: Regel: Anteil der Referenz AUSSERHALB jeder Zusatzmaske vor der ersten Zahl messen (VALDO-Slab-Maske kostete 75 % der SABRE-Referenz).

**Regel, neu 2026-10-08:** Eine anatomische Nachbearbeitungsregel wird erst im Betrachter sichtbar gemacht (Karte, entfernte Fehlalarme, entfernte Treffer als getrennte Ebenen mit Zaehlern), dann geglaubt. Die Liquor-Regel entfernt auf VALDO 27 Fehlalarme und 1 von 90 Treffern, auf der eigenen SWI-Kohorte 88 Fehlalarme und 62 von 426 Blutungen: die Summenzahl haette das verdeckt.
- 11.10.: Neue Regel aus der PVS-Linie: Instanz-Metriken mit Beruehrungsregel brauchen Dice/Volumen/Mehrfachtreffer als Nebenbedingung, sonst belohnen sie Blob-Verschmelzung (PVS: F1 0,591 -> 0,658 bei Dice 0,365 -> 0,241).
