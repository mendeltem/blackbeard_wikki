---
id: epvs-2024-winner-scores-0.28-on-valdo-below-every-single-method
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: PVS-Arena Alita, Versuch H (verfahren/epvs24_big_aehrc.sh, Kettenpruefung gegen den Container identisch), VALDO Task 1 12 Handfaelle referenz_v2, 2026-10-11 16:30
verweist_auf: [epvs-2024-submissions-are-public-docker-images-metric-equals-ours, candidate-threshold-0.02-lifts-valdo-f1-0.59-to-0.65-small-pvs-recall-doubles, mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs]
---

# Der EPVS-2024-Sieger BIG_AEHRC erreicht auf VALDO nur 0,28 -- unter jedem unserer Einzelverfahren

## Aussage
Der Siegercontainer (CSIRO, MedNeXt-S kernel5, 5 Falten, T1+T2+FLAIR, 3D-Zweig) liefert auf den 12 VALDO-Handfaellen mit seiner eigenen
Regel (Prob >= 0,3) Instanz-F1 0,268 [0,222; 0,313] (Recall 0,27, Praezision 0,32); die Schwellenkurve ist flach (0,25-0,30), out-of-fold
0,279 [0,226; 0,332] (Recall 0,36, Praezision 0,26). Zum Vergleich auf denselben Faellen: PINGU 0,449, MedNet-T1 0,440, MedNet-T2 0,388,
DRIPS-T2 0,354; unser Dreier-Pool mit Trenner 0,658. Lokale GPU-Kette (Code + Checkpoint aus dem Image, PYTHONPATH) reproduziert den
Container exakt (TP 70 / FP 203 auf sub-101) in 5 statt 42 Minuten.

## Traegt
Challenge-Rang ist kein Vorhersager fuer eine fremde Kohorte: der Report selbst zeigt den Einbruch auf dem ungesehenen Standort Shanghai,
VALDO (Ganzhirn-Annotation inkl. BG, 0,49-mm-RSS) ist ein weiterer. Fuer die Arena bleibt BIG_AEHRC hoechstens ein vierter Kandidatengeber
(Posteriors liegen); als Einzelverfahren ist es erledigt. Praktisch: Challenge-Container lassen sich ohne GPU-Docker lokal nachbauen
(Checkpoint + mitgelieferter Code), Kettenpruefung an einem Fall gegen den Container ist Pflicht.

## Traegt nicht
Wie BIG_AEHRC auf HCP-Aging (T2, 0,8 mm) abschneidet; ob die anderen fuenf Container besser uebertragen (hufsaim, ccnu als naechste).
Keine Aussage ueber die Challenge-Testdaten selbst.

## Bruchindikator
Ein anderer EPVS-Container liegt auf VALDO ueber 0,45, oder BIG_AEHRC im Pool hebt den Trenner um mehr als 0,02.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/epvs24-big_aehrc (Posteriors, Masken), epvs24-big_aehrc-oof.json, epvs24-big_aehrc-docker-mini vs -lokal-mini;
ARBEIT.md 11.10. 16:30.

## Verknuepft
- [epvs-2024-submissions-are-public-docker-images-metric-equals-ours](epvs-2024-submissions-are-public-docker-images-metric-equals-ours.md)
- [candidate-threshold-0.02-lifts-valdo-f1-0.59-to-0.65-small-pvs-recall-doubles](candidate-threshold-0.02-lifts-valdo-f1-0.59-to-0.65-small-pvs-recall-doubles.md)
- [mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs](mednet-t1-clinical-trainer-leads-valdo-but-misses-small-pvs.md)
