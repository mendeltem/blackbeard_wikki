---
id: wmh-apply-the-lesion-method
typ: pruefpunkt
status: offen
thema: knowledge/lesion_detection_method
stand: 2026-10-09
herkunft: Alita, Plan wmh-modell201/PLAN-METHODE-1009.md; Lehren aus cmb_detection, pvs_detection, wmh_segmentation
verweist_auf: [pvs-apply-the-lesion-method]
---

# WMH: die Methode aus CMB und PVS noch einmal anwenden

## Warum
Die WMH-Linie lief mit 2D-U-Nets und Trainingsrezept-Hebeln (ausgeliefert 0,725 Dice auf dem 110er-Test). Die CMB-Linie
zeigte danach, dass die Gewinne in der Datenkette liegen: Gitter, das der Aufnahme folgt (+0,159 F1), Ortsregel nach dem Netz,
EIN Kandidaten-Klassifikator. Die Challenge-FLAIRs haben durchgehend 3-mm-Schichten bei ~1 mm in der Schicht: genau der
Fall des anisotropen Netzes.

## Schritte (Reihenfolge der Methode)
1. M1 Gitter auf nativem Raster, je Fall pruefen (Referenz ausserhalb der Hirnmaske, Label 2, Geometrie). Probe: 0 % ausserhalb.
2. M2 Auswertung mit offizieller Label-2-Regel; muss die alte 2D-Kreuzvalidierung auf 0,001 wiedergeben.
3. M3 Rauschboden: anisotropes 3D-U-Net, 3 Startwerte x 5 feste Falten, gepaart gegen die 2D-Grundlinie.
4. M4 Turnier aller Netze + nnU-Net v2 (gleiche Falten).
5. M5 Ortsregel (ausserhalb WM/periventrikulaer) erst im Betrachter, dann messen.
6. M6 Kandidaten-Klassifikator als zweite Stufe.
7. M7 eingefrorene Kette einmal auf dem 110er-Test; M8 eigene Kohorte (nur lokal), stratifiziert nach Voxelvolumen.

## Entscheidungsregel (vorab)
Gewinn = gepaartes 95-%-Bootstrap-Intervall (Dice oder Laesions-F1) ueber 0 UND groesser als die Startwert-Streuung aus M3.
Kein Verlust-/Augmentierungs-Suchen vor M5/M6.

## Stand 2026-10-09 abends
- M1 fertig (60/60, Referenz vollstaendig in der Hirnmaske). M2 fertig: Messcode gibt die alte Testzahl 0,7719 Dice,
  Laesions-F1 0,7517, Recall 0,7921, AVD 29,48 % bitgenau wieder (AVD der alten Kette ist relativ in %).
- Reihenfolge geaendert: erst Patch-Vorlauf mit dem anisotropen Netz (16x64x64, 16x96x96, 16x160x160, 32x96x96), Wahl nach
  vorab festgelegter Regel, dann Arena mit 16 Netzen, 60 Epochen, nnU-Net v2 als Referenz; zuletzt Sieger mit gegen ohne Patches
  (ganzes Volumen) samt gemessenem Speicherbedarf. Grund: die Patchgroesse gilt fuer alle Netze, bei CMB kostete ein zu kleiner
  Patch -0,216 F1; "passt nicht auf die Karte" gilt erst mit gemessener Zahl (CMB-Patches brauchten nur 0,6-2,7 GiB).

## Stand 2026-10-10 frueh
- Vorlauf gerechnet. Falle: die binaeren Masken des CMB-Turniers loeschen Komponenten ueber 2100 Voxel (Klumpenwaechter
  fuer Mikroblutungen) -- fuer WMH falsch, Dice scheinbar 0,46. Auf den Wahrscheinlichkeitskarten (Schwelle 0,5):
  anisotropes 3D-U-Net 0,798 gegen 2D 0,783 Dice, gepaart +0,015 [+0,009; +0,023], 43 von 60 Faellen besser, alle drei
  Scanner positiv. Patchgroessen 16x64x64 bis 32x96x96 gleichauf (Unterschiede +-0,002). Rauschboden ueber Startwerte offen.
- Regel fuer uebernommene Pipelines: Nachbearbeitung der Herkunftslinie (hier Groessenfilter fuer CMB) vor der ersten Zahl
  pruefen; Verdacht, wenn Laesions-F1 gleich bleibt, der Dice aber einbricht und die Streuung riesig ist.

## Stand 2026-10-10 morgens: Laesions-F1 und QC
- Offizielles Mass (Label-2-Regel, Hirnmaske), Schwelle 0,5, 60 Faelle out-of-fold: 3D Dice 0,798 / Laesions-F1 0,747 /
  Laesions-Recall 0,742; 2D 0,783 / 0,739 / 0,690. Gepaart: Dice +0,015 [+0,009; +0,023], F1 +0,009 [-0,006; +0,024].
  Der 3D-Gewinn liegt im Voxel-Dice und im Recall, beim Laesions-F1 ist er nicht gesichert.
- Zwei Messfallen im eigenen Auswerteskript: eine Wahrscheinlichkeitskarte als uint8 (0..255) wurde wie eine Maske gelesen
  (effektive Schwelle 1/255: Dice 0,72 statt 0,80), und ein Pfad nahm die Label-2-Datei als Hirnmaske (alles 0).
  Regel: den Datentyp der Vorhersage vor dem Schwellen pruefen; ein Mass, das bei der Grundlinie stimmt, kann beim neuen
  Dateiformat falsch sein -- jede neue Vorhersageart einmal gegen eine Direktrechnung halten.
- QC-Seite mit dem gemeinsamen Werkzeug qc_slice_viewer gebaut (60 Faelle, beide Modelle), nur lokal.

## Stand 2026-10-10 vormittags: extern auf eigener Kohorte (BELOVE, 56 Faelle mit Handmaske)
- Das nur auf den 60 Challenge-Faellen trainierte 3D-Netz faellt auf BELOVE auf Dice 0,42 (Sensitivitaet 0,33, Praezision 0,78);
  ein 2D-Modell mit BELOVE im Training erreicht auf denselben Faellen 0,665.
- Der Einbruch folgt der Geometrie: 5 mm / 0,86 mm Pixel 0,57; 5 mm / 0,69 mm 0,44; 6 mm / 0,96 mm 0,32; 6 mm / 0,43 mm 0,20 (das 2D-Modell
  mit Eigendaten bleibt ueber alle Geometrien bei 0,64-0,68). Pixel in der Schicht vor der Vorhersage auf ~1 mm umrechnen hebt die 0,43-mm-Faelle
  von 0,21 auf 0,37 Dice (Praezision 0,97), die Sensitivitaet bleibt niedrig.
- Regel: Ein Patch-Netz lernt Strukturen in Voxeln, nicht in mm. Vor der Anwendung auf fremde Daten die Pixelgroesse auf die des Trainings bringen;
  was danach fehlt, ist Domaene (Schichtdicke, Kontrast, Zeichenstil) und braucht eigene Trainingsdaten.

## Zu pruefen
- M1-M3 eingereiht 2026-10-09 (lokaler Agent); M4 braucht ~2 Tage GPU und pausiert das Sprachmodell.
