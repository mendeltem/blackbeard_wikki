---
id: training-loss-does-not-rank-networks-or-schedules
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), code/arena_loss_plot.py, Verlaeufe der Turnierlaeufe, 2026-10-07
verweist_auf: [anisotropic-first-level-beats-isotropic-3d-nets, two-seeds-per-decision-below-0.08]
---

# Der Trainingsverlust ordnet weder Netze noch Trainingslaengen -- nur das Laesions-F1 ausserhalb der Falte tut das

## Aussage
Verlaeufe von 16 Turnierlaeufen (BCE + Dice mit tiefer Ueberwachung, je 5 Falten gemittelt),
gezeichnet auf der oeffentlichen Seite (Abschnitt 3, drei aufklappbare Bloecke):

- **Netze:** das flache dilatierte U-Net erreicht denselben Trainingsverlust wie der Sieger
  (0,154) bei Test-F1 0,176 statt 0,404; das Residual-SE-U-Net 0,155 bei 0,105. Ein
  Voxelverlust ist mit vielen kleinen Fehlalarmen billig zu senken. MedNeXt und R2U-Net
  starten niedriger und enden hoeher (0,16 / 0,20 gegen 0,13) -- der Startwert des Verlusts
  sagt nichts. 16 Basiskanaele erreichen den Verlust der Basis (0,125), nicht ihr F1.
- **Trainingslaenge:** 60 / 90 / 120 feste Epochen: Verlust 0,128 / 0,117 / 0,109 faellt
  weiter, das beste innere F1 steigt (0,609 / 0,644 / 0,658), weil es ein Maximum ueber mehr
  Pruefpunkte ist; der Out-of-fold-Wert folgt nicht (-0,016 / -0,029, auf der klinischen
  T2*-Kohorte -0,022 gesichert).
- **Fruehstopp auf dem inneren F1** (alle 5 Epochen, Geduld 3) feuert auf Startwert-Rauschen
  (~0,08): beim zweiten Startwert hielt eine Falte Epoche 5 und stoppte bei 20, Lauf 0,321
  statt 0,404. Feste 60 Epochen mit Cosinus-Abfall: 0,470.

## Traegt
Jede Modellwahl fuer kleine, seltene Laesionen: Verlustkurven zeigen, DASS gelernt wird
(Rauchtest), nicht WIE GUT; entscheiden darf nur die Laesionsmetrik ausserhalb der Falte.
Ein fester Zeitplan statt Fruehstopp, wenn das Stoppkriterium so verrauscht ist wie der
Effekt, den es messen soll.

## Traegt nicht
Verluste verschiedener Verlustfunktionen oder Budgets je Epoche sind nicht auf einer Achse
vergleichbar (focal Tversky, 400/1600 Patches wurden darum nicht gezeichnet).

## Bruchindikator
Ein Datensatz, auf dem die Rangfolge nach Trainingsverlust mit der nach Out-of-fold-F1
uebereinstimmt, oder ein Fruehstopp-Kriterium mit Rauschen deutlich unter dem Effekt.

## Ablesung
Eigene Messung VALDO 2021 Task 2, 5-fach-CV; Kurven: Mittel ueber die Falten je Epoche,
`ergebnisse/turnier/<Lauf>/fold*/verlauf.json`. Tier 1a.

## Verknuepft
- [anisotropic-first-level-beats-isotropic-3d-nets](anisotropic-first-level-beats-isotropic-3d-nets.md)
- [two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md)
