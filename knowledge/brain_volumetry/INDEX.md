# brain_volumetry

Volumetrie des Gehirns ueber die Zeit (SynthSeg, FreeSurfer, eigene Netze): wie Verlaufszahlen gerechnet und
wie ihre Messfehler ausgewiesen werden. Keine Patientendaten; Zahlen bleiben bei den Projekten.

Stand 2026-10-12. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| regel | [longitudinal-volumetry-needs-error-statistics](rules/longitudinal-volumetry-needs-error-statistics.md) | Zu jeder Trendseite eine Fehlerseite: Test-Retest (SDw, CV, ICC, SDC95, Bland-Altman), Laengsschnitt-Residuen, Nachweisbarkeit (Jahre bis SDC), Ausfall/QC je Zeitpunkt; Laesionsausschluss nur mit Maske in allen Sitzungen |

## Herkunft
DEMDAS-GM-Beispiel auf Alita (demdas-gm/verlauf_statistik.py, fehler_statistik.py), Nutzerauftrag 12.10.2026.
| befund | [synthseg-in-freesurfer-8-runs-on-cpu-only](findings/synthseg-in-freesurfer-8-runs-on-cpu-only.md) | fspython TF 2.13 ohne GPU; 85 s je Sitzung mit --robust, Ordner-Batches laden das Modell einmal; recon-all 8.2 40-48 min |
| regel | [cohort-copies-need-a-gzip-sweep](rules/cohort-copies-need-a-gzip-sweep.md) | nach jeder Kohortenkopie gzip -t ueber alle NIfTI, Dateizahl und Bytes gegen die Quelle; du auf exFAT luegt |
