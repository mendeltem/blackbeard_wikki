# brain_volumetry

Volumetrie des Gehirns ueber die Zeit (SynthSeg, FreeSurfer, eigene Netze): wie Verlaufszahlen gerechnet und
wie ihre Messfehler ausgewiesen werden. Keine Patientendaten; Zahlen bleiben bei den Projekten.

Stand 2026-10-12. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| regel | [longitudinal-volumetry-needs-error-statistics](rules/longitudinal-volumetry-needs-error-statistics.md) | Zu jeder Trendseite eine Fehlerseite: Test-Retest (SDw, CV, ICC, SDC95, Bland-Altman), Laengsschnitt-Residuen, Nachweisbarkeit (Jahre bis SDC), Ausfall/QC je Zeitpunkt; Laesionsausschluss nur mit Maske in allen Sitzungen |

## Herkunft
DEMDAS-GM-Beispiel auf Alita (demdas-gm/verlauf_statistik.py, fehler_statistik.py), Nutzerauftrag 12.10.2026.
