---
id: longitudinal-volumetry-needs-error-statistics
typ: regel
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-12
herkunft: Nutzer 12.10.2026 zum DEMDAS-GM-Beispiel: "bei DEMDAS muss man auch die Fehlerstatistiken rechnen"; umgesetzt in demdas-gm/fehler_statistik.py
verweist_auf: [qc-pages-explain-every-number-on-hover]
---

# Jede Verlaufs-Volumetrie bekommt eine Fehlerstatistik neben der Trendstatistik

## Aussage
Eine Seite mit jaehrlichen Aenderungen (gemischtes Modell, Steigungen je Proband) ist ohne Messfehler nicht lesbar:
niemand kann sehen, ob -0,8 %/Jahr Amygdala mehr ist als das Rauschen. Deshalb gehoert zu jeder Verlaufs-Volumetrie
eine zweite Seite `error_statistics.html` mit vier Bausteinen, alle ohne neue Bildrechnung, wenn die Daten da sind:

1. **Test-Retest je Struktur** aus zwei Segmentierungen derselben Sitzung (hier: MPRAGE ohne und mit Verzeichnungskorrektur,
   beide SynthSeg). Kennzahlen: Mittel, Bias, SD der Differenz, Within-Subject-SD = SD/sqrt 2, CV %, ICC(2,1),
   **SDC95 = 1,96 * sqrt 2 * SDw** (kleinste Aenderung, die bei EINER Person als echt gelten darf), Bland-Altman-Plots.
   Ehrlich kennzeichnen, wenn das Paar kein echtes Scan-Rescan ist: dann ist es eine obere Schranke.
2. **Laengsschnitt-Rauschen aus der Pipeline selbst**: Residuen-SD um die Gerade je Proband (>= 3 Sitzungen, % der Baseline)
   und die Aenderung ueber das kuerzeste Intervall (M0 -> M6) als Verteilung. Enthaelt Biologie + Fehler, sagt das auch.
3. **Nachweisbarkeit**: jaehrliche Aenderung (gemischtes Modell, mit KI in denselben Einheiten!) gegen SDC95 ->
   Jahre, bis eine Einzelperson die SDC ueberschreitet. Ein Balkenbild mit beiden Groessen je Struktur.
4. **Ausfall- und QC-Zaehlung je Zeitpunkt**: Sitzungen, Segmentierungs-QC unter Schwelle, fehlende Laesionsmasken,
   Ausrichtungs-Dice, recon-all fertig/abgebrochen, Zusatzgroessen (WMH) vorhanden.

Nebenregel aus dem ersten Lauf: **relative Aenderungen mit Laesionsausschluss nur, wenn die Maske in allen Sitzungen
existiert**. Fehlt sie in Folgesitzungen, werden aus einem fast weggemaskten M0-Wert Aenderungen von +1400 % --
ein Maskeneffekt, der in jeder Verlaufszahl steckt, bis die chronische Maske da ist.

## Traegt
Jede Verlaufs-Volumetrie (SynthSeg, FreeSurfer, eigene Netze) auf dem Stick oder fuer Dritte; die Deutung jeder
Steigung; die Entscheidung, ob ein Laengsschnitt-Strom (FreeSurfer longitudinal) noetig ist (ja, wenn Jahre bis SDC > Studiendauer).

## Traegt nicht
Querschnittsvergleiche zwischen Gruppen (dort zaehlt die Gruppen-SD, nicht die SDC); Datensaetze ohne zweite Segmentierung
je Sitzung -- dann bleibt nur Baustein 2 bis 4 und die Literatur-SDC.

## Bruchindikator
Eine Trendseite ohne Verweis auf die Fehlerseite; eine Nachweisbarkeitstabelle, deren KI in anderen Einheiten steht als
die Punktschaetzung (im ersten Lauf passiert: %ICV/Jahr neben relativ %/Jahr).

## Ablesung
Umgesetzt 12.10.2026 (demdas-gm/fehler_statistik.py, 61 Sitzungspaare, Seite in gm_beispiel/verlauf/). Zahlen bleiben
unter ~/data (eigene Kohorte). Offen: ND-Serie mit den Pipeline-Einstellungen (--parc --robust) nachrechnen, damit
Baustein 1 exakt der Pipeline entspricht und die Rindenregionen dazukommen.

## Verknuepft
- [qc-pages-explain-every-number-on-hover](../../mri_qc_viewers/rules/qc-pages-explain-every-number-on-hover.md)
