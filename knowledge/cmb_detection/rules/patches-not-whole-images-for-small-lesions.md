---
id: patches-not-whole-images-for-small-lesions
typ: regel
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), Dosisreihe Patchgroesse (ARBEIT.md 5t) und Messungen 2026-10-07
verweist_auf: [anisotropic-first-level-beats-isotropic-3d-nets, csf-rule-removes-false-alarms-without-loss]
---

# Kleine Laesionen: Ausschnitte trainieren, Schiebefenster vorhersagen -- das ganze Bild auf einmal ist weder noetig noch bezahlbar

## Aussage
Beide Netze der CMB-Kette sehen nur Ausschnitte. U-Net: Patches 38 x 62 x 94 Voxel auf dem
0,5 x 0,5 x 1-mm-Gitter (38 x 31 x 47 mm), 800 je Epoche, 60 % um eine Laesion an zufaelliger
Stelle; Vorhersage mit Schiebefenster derselben Groesse, halber Versatz, Ueberlappung gemittelt
(~370 Fenster je Fall), nichts geht verloren. Klassifikator: 20-mm-Block je Kandidat, 16 mm davon
ins Netz. Vier Gruende, alle gemessen oder gerechnet:

1. **Speicher:** ein Volumen hat ~13 Mio. Voxel; die erste U-Net-Ebene allein braucht dafuer
   0,8 GB je Zwischenergebnis (32 Kanaele, bfloat16), der Rueckwaertsschritt mehrere je Ebene --
   Dutzende GB. Ein Patch: 221 000 Voxel; ein ganzes Training 1,6 GiB VRAM, Inferenz auf der CPU.
2. **Beispiele:** 800 Ausschnitte je Epoche zeigen jede Blutung in vielen Lagen; ganze Bilder
   waeren 57 Beispiele mit 99,99 % Hintergrund.
3. **Kontext:** eine Blutung ist 2-10 mm, "Gefaess oder Blutung" entscheidet sich in wenigen mm.
   Dosisreihe: 24 mm -0,216 [-0,277; -0,156], Rezept 0, 48 mm -0,016 [-0,074; +0,034]; 64 mm
   scheiterte am Arbeitsspeicher des Puffers (33 GB), nicht an der Idee. Das ganze Bild ist nur
   der Endpunkt dieser Reihe -- bewusst nicht gemessen (Nutzerentscheidung 2026-10-07).
4. **Was Patches nicht wissen** (Lage im Hirn), kommt danach: Liquor-Regel aus der Gewebekarte;
   als Eingangskanal war die Karte schlechter (-0,058).

## Traegt
Jede Detektion kleiner, seltener Objekte in 3D-Volumen mit begrenztem VRAM; Patches sind dort
zugleich die Datenvermehrung.

## Traegt nicht
Aufgaben, bei denen die Entscheidung globalen Kontext braucht (Hemisphaerenvergleich, grosse
Organe): dort ist das Ganze oder ein grober Massstab noetig.

## Bruchindikator
Ein Punkt der Dosisreihe deutlich ueber dem Rezept (z. B. 64 mm oder Ganzbild bei gleichem
Budget und zwei Startwerten besser als +0,08).

## Ablesung
Eigene Messungen VALDO 2021 Task 2, gepaarter Bootstrap; VRAM-Messung 2026-10-07. Tier 1a.

## Verknuepft
- [anisotropic-first-level-beats-isotropic-3d-nets](../findings/anisotropic-first-level-beats-isotropic-3d-nets.md)
- [csf-rule-removes-false-alarms-without-loss](../findings/csf-rule-removes-false-alarms-without-loss.md)
