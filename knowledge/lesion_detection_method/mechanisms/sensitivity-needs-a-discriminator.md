---
id: sensitivity-needs-a-discriminator
typ: mechanismus
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekt valdo-t2s (CMB), ARBEIT.md 5g bis 5r, 2026-09-20 bis 2026-09-22; uebertragen 2026-10-07
verweist_auf: [sensitivity-levers-do-not-raise-lesion-f1, one-shared-candidate-classifier-for-all-cohorts, data-chain-beats-training-levers]
---

# Empfindlichkeit lohnt nur, wenn etwas die zusaetzlichen Kandidaten trennen kann

## Aussage
Jeder Hebel, der einen Detektor fuer kleine Laesionen empfindlicher macht (Verlust je
Laesion, Zentrumskarten, Neugewichtung verpasster Laesionen, niedrigere Schwelle,
kuenstliche Laesionen), hebt die Sensitivitaet und bezahlt mit Fehlalarmen; das F1 faellt
oder bleibt. Auf CMB: kleine Blutungen 0,52 -> 0,64 / 0,66 gefunden, F1 -0,044 bis -0,054.
Der Engpass ist nicht das Finden, sondern das Trennen von Laesion und Verwechsler
(Gefaessquerschnitt, Verkalkung) mit der verfuegbaren Information.

Gegenprobe aus der Literatur: dieselben Hebel halfen bei CenSynCMB (+1,8 / +4,5 Punkte),
dort mit T1 + T2 + T2* als Eingabe. Empfindlichkeit zahlt sich also aus, sobald ein
Trenner da ist: mehr Sequenzen, oder eine zweite Stufe.

Form der zweiten Stufe, die sich reproduziert hat: EIN kleiner Kandidaten-Klassifikator
(3D-CNN, 216 k Parameter) auf dem Kandidaten-Pool ALLER Kohorten mit einer Schwelle,
out-of-fold je Fall. Mischen hilft auf Kandidaten-Ebene (+0,045 SWI, reproduziert), nicht
auf Voxel-Ebene (gemischt trainierte U-Nets -0,02 bis -0,045). Je Kohorte getrennte zweite
Stufen (logistisch, Wald, Boosting, CNN) brachten nichts.

Konsequenz: wer eine Schwelle durchprobiert (Vesselness, Wahrscheinlichkeit, Groesse),
bewegt sich nur auf der Sensitivitaet-Fehlalarm-Kurve. Ein Schwellensatz ist ein
Arbeitspunkt, kein Fortschritt. Fortschritt heisst: eine neue Information, die trennt.

## Traegt
Detektoren fuer kleine Laesionen, deren Verwechsler dieselbe Intensitaet haben
(Gefaesse gegen Blutungen, Gefaesse gegen PVS, PVS gegen Lakunen, PVS gegen WMH).

## Traegt nicht
Faelle, in denen die Sensitivitaet wirklich der Engpass ist (Recall deutlich unter der
Precision bei hoher Precision) -- dann zuerst die Datenkette pruefen (Uebermalung,
Interpolation, Maske).

## Bruchindikator
Ein Sensitivitaetshebel, der das Laesions-F1 gepaart und mit zweitem Startwert hebt,
ohne dass eine neue trennende Information dazukam.

## Ablesung
Eigene Messungen VALDO 2021 Task 2 und zwei eigene Kohorten (nur Summen). Tier 1a.
CenSynCMB 2026: Vergleichszahl aus dem Paper, nicht selbst nachgerechnet.

## Verknuepft
- [sensitivity-levers-do-not-raise-lesion-f1](../../cmb_detection/findings/sensitivity-levers-do-not-raise-lesion-f1.md)
- [one-shared-candidate-classifier-for-all-cohorts](../../cmb_detection/findings/one-shared-candidate-classifier-for-all-cohorts.md)
- [data-chain-beats-training-levers](data-chain-beats-training-levers.md)
