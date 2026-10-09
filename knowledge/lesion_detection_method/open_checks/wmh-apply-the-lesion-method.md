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

## Zu pruefen
- M1-M3 eingereiht 2026-10-09 (lokaler Agent); M4 braucht ~2 Tage GPU und pausiert das Sprachmodell.
