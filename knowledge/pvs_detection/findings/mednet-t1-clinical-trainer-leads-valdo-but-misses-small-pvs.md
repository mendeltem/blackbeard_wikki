---
id: mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs
typ: befund
status: vorschlag
thema: knowledge/pvs_detection
stand: 2026-10-08
herkunft: PVS-Arena Alita, Versuche C2/C3/C5 auf VALDO Task 1 (12 Maskenfaelle, korrigierte Referenz), GPU, 2026-10-08 02:00-05:00
verweist_auf: [valdo-interrater-ceiling-and-drips-first-numbers, drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third, training-geometry-must-cover-target-geometry, sensitivity-needs-a-discriminator]
---

# Auf klinischem 1-mm-T1 fuehrt das auf klinischen T1 trainierte Netz (F1 0,44), findet aber die kleinsten PVS am schlechtesten; das synthetisch trainierte Netz findet sie am besten

## Aussage
VALDO Task 1, 12 Maskenfaelle (SABRE Ganzhirn, RSS mit Region), Instanz-F1 gegen Rater 1, Mittel ueber Faelle [KI95]:
MedNet-PVS-T1w (MedNeXt-L, trainiert auf 40 klinischen T1 mit WM+BG-Labels) 0,440 [0,366; 0,508], Precision 0,45, OOF-Schwelle
0,3 stabil, Kurve flach; MedNet-PVS-T2w (trainiert auf HCP-Aging-T2, nur WM) 0,388; DRIPS-T2 (synthetisch) 0,354; DRIPS-T1 0,351;
Inter-Rater 0,327. Groessenklasse 1-2 Voxel, Recall: DRIPS-T2 0,45, DRIPS-T1 0,32, MedNet-T2 0,19, MedNet-T1 0,12 (OOF 0,21);
Rater untereinander 0,34. Kohortenprofil: DRIPS gewinnt SABRE (Ganzhirn, 1 mm: 0,38 vs 0,37 MedNet-T1), MedNet-T1 gewinnt RSS
(0,5-mm-Gitter, Teilschichten: 0,52 vs 0,32). Gegen Rater 2: MedNet-T1 0,26, DRIPS-T2 0,24, MedNet-T2 0,07 (der HCP-T2-Trainer kennt
keine Basalganglien-PVS). Alle Schwellenkurven sind flach (0,1-0,5); Precision steigt, F1 nicht.

**Nachtrag 08.10. 16:25 (Gewebe am Schwerpunkt, SABRE 6 Faelle, Ganzhirn):** Rater 1 markiert 1103 WM- und 291 BG-Komponenten,
Rater 2 498 WM und 510 BG (BG-lastig). MedNet-T2w (HCP-Trainer, nur WM-Labels) sagt 1917 WM und **2** BG voraus -- das erklaert
sein 0,07 gegen Rater 2 vollstaendig; MedNet-T1w 1342/181, DRIPS-T2 2646/423. Ein auf WM-only-Labels trainiertes Netz ist fuer
Basalganglien-PVS (klinisch die wichtigere Region) unbrauchbar; Trainingslabels muessen die Zielregionen enthalten.

## Traegt
Wahl der Bausteine: fuer klinisches T1 (BELOVE) ist MedNet-T1 die praezise Basis; fuer das Ziel "auch kleine PVS" ist DRIPS der
Kandidatengeber (empfindlich, Klasse 1-2 ueber Rater-Niveau). Daraus folgt der naechste Schritt: Kandidaten-Pool beider plus
Trenner, nicht ein hoeherer Arbeitspunkt. Bestaetigt die Regel "Trainingsdomaene muss die Zieldomaene abdecken" (T1-Trainer
schlaegt T2-Trainer und Synthese auf T1) auf der dritten Laesionslinie.

## Traegt nicht
n = 12, Intervalle ueberlappen (Richtungsangabe, kein Befund); nur VALDO; EPVS-2024 und BELOVE-Rating stehen aus. Die
Inter-Rater-Grenze 0,33 ist fuer Modelle keine harte Decke (Modelle koennen "mittlere Annotation" lernen).

## Bruchindikator
Auf EPVS-2024 (200 Faelle, zwei Regionen) kehrt sich die Reihenfolge um, oder der Kandidaten-Pool hebt den F1 nicht.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/{mednet-t1-t050,mednet-t2-t050,drips-t2-t010,drips-t1-t010}-v2/zusammenfassung.json,
*-v2_schwellenkurve.json, ARBEIT.md 04:20-05:00. Oeffentliche Daten CC BY-NC 4.0.

## Verknuepft
- [valdo-interrater-ceiling-and-drips-first-numbers](valdo-interrater-ceiling-and-drips-first-numbers.md)
- [drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third](drips-on-hcp-aging-f1-0.55-threshold-flat-small-pvs-a-third.md)
- [training-geometry-must-cover-target-geometry](../../cmb_detection/findings/training-geometry-must-cover-target-geometry.md)
- [sensitivity-needs-a-discriminator](../../lesion_detection_method/mechanisms/sensitivity-needs-a-discriminator.md)
