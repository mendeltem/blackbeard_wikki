# lesion_detection_method: Kurzstand

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
