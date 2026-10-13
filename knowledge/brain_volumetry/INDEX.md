# brain_volumetry

Volumetrie des Gehirns ueber die Zeit (SynthSeg, FreeSurfer, eigene Netze): wie Verlaufszahlen gerechnet und
wie ihre Messfehler ausgewiesen werden. Keine Patientendaten; Zahlen bleiben bei den Projekten.

Stand 2026-10-13. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| regel | [longitudinal-volumetry-needs-error-statistics](rules/longitudinal-volumetry-needs-error-statistics.md) | Zu jeder Trendseite eine Fehlerseite: Test-Retest (SDw, CV, ICC, SDC95, Bland-Altman), Laengsschnitt-Residuen, Nachweisbarkeit (Jahre bis SDC), Ausfall/QC je Zeitpunkt; Laesionsausschluss nur mit Maske in allen Sitzungen |

## Herkunft
DEMDAS-GM-Beispiel auf Alita (demdas-gm/verlauf_statistik.py, fehler_statistik.py), Nutzerauftrag 12.10.2026.
| befund | [synthseg-in-freesurfer-8-runs-on-cpu-only](findings/synthseg-in-freesurfer-8-runs-on-cpu-only.md) | fspython TF 2.13 ohne GPU; 85 s je Sitzung mit --robust, Ordner-Batches laden das Modell einmal; recon-all 8.2 40-48 min |
| befund | [demdas-segmentation-method-benchmark-wd6](findings/demdas-segmentation-method-benchmark-wd6.md) | 5 Methoden, Ränge 1..N + Mittelrank; Dice vs FreeSurfer 8.2 aseg (GM 0.80, WM 0.89, Hippo 0.88); Test-Retest ICC/SDC95 waechst mit Set B overnight |
| regel | [cohort-copies-need-a-gzip-sweep](rules/cohort-copies-need-a-gzip-sweep.md) | nach jeder Kohortenkopie gzip -t ueber alle NIfTI, Dateizahl und Bytes gegen die Quelle; du auf exFAT luegt |
| befund | [recon-all-8-memory-peak-is-a-15-minute-phase](findings/recon-all-8-memory-peak-is-a-15-minute-phase.md) | recon-all 8.2: 26 GB nur in den ersten ~15 min (SynthSeg/SynthMorph), danach 2-4 GB; 89 Laeufe gemessen: MAX_P 5/3/2 = 29/48/36 min, 174 OOM bei 5; Vollkohorte 1616 Sitzungen ~20 Tage lokal, Slurm 36 GB/4 CPU/6 h je Task |
| regel | [schedule-recon-all-8-by-phase-not-by-run](rules/schedule-recon-all-8-by-phase-not-by-run.md) | Vorschlag: Schleuse nur um autorecon1 (Synth-Phase), autorecon2/3 frei -> ~7,5 statt 3,4 Sitzungen je Stunde; getragen erst nach dem ersten gemessenen Batch |
| befund | [freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort](findings/freesurfer-improvement-plan-for-a-longitudinal-stroke-cohort.md) | FreeSurfer als Hauptwerkzeug: Long-Stream (+0,25 ICC), Laesionen fuellen (ONDRI 62 % -> 8 % Fehler), FLAIRpial testen, Euler-QC, lokaler Test-Retest, longComBat; Fehler in M0/M10/M60 erkennen und behandeln; 24 Quellen mit PMID |
| befund | [demdas-volumetry-primer-2026-10-13](findings/demdas-volumetry-primer-2026-10-13.md) | Lehrtext zum Vortragen (12 Seiten, PDF daneben): Kohorte, Pipeline mit Versionen, Messfehler, Verlaeufe, QC, Fehler ueber Zeitpunkte, FreeSurfer-Plan, Rechenbudget, Fragen und Antworten, 24 Quellen |
| befund | [chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg](findings/chronic-infarcts-are-invisible-to-dwi-masks-and-unlabelled-by-synthseg.md) | DWI-Maske nur akut; SynthSeg gibt Hoehlen Label 0; Folgesitzungen brauchen vorwaerts getragene Maske; Ausrichtung Dice 0,98-0,99 |
| regel | [euler-number-needs-the-binary-not-the-log](rules/euler-number-needs-the-binary-not-the-log.md) | mris_euler_number auf orig.nofix mit LD_LIBRARY_PATH; Log-Fallback liefert Nach-Fix-Wert 2 |
| regel | [demdas-pipeline-protocol-v1](findings/demdas-pipeline-protocol-v1.md) | eingefrorenes Protokoll v1: Eingaenge, exakte Einstellungen, Regeln, offene Punkte fuer v2 |
| regel | [one-t1-per-visit-and-tab-columns-by-cut](rules/one-t1-per-visit-and-tab-columns-by-cut.md) | HPC-Pilot: `read` verschluckt leere TSV-Spalten, zwei T1 je Besuch unter einer id; 5 von 14 "FAILED" waren Listenfehler, FLAIRpial-Abbruch 3/65 ist Befund |
| befund | [demdas-full-cohort-sample-gm-page-2026-10-13](findings/demdas-full-cohort-sample-gm-page-2026-10-13.md) | erste Seite aus der Vollkohorte: 12 Probanden x 4 Sitzungen, nur SynthSeg, QC-Werte 15/48, PASS/FLAGGED-Zeile auf beiden GM-Seiten entfernt |
