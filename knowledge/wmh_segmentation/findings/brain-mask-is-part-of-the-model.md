---
id: brain-mask-is-part-of-the-model
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: [measure-tails-paired-not-by-percentile, architecture-package-brought-no-gain]
---

# Die Hirnmaske ist Teil des Modells, nicht Vorverarbeitung

## Aussage
Zwei Messungen desselben WMH-Modells (gleiche Gewichte, Schwelle 0,4, gleiche Metrik,
praktisch gleiche FLAIR-Bilder) ergaben Dice **0,688 gegen 0,719** auf den 110 Testfaellen der
WMH Segmentation Challenge 2017. Einziger Unterschied: die HD-BET-Hirnmaske aus zwei Laeufen.
Keine der 110 Masken war identisch (im Mittel 24 685 abweichende Voxel, die neueren rund 3 %
groesser). Der Uebertragungsweg: die z-Normierung des Eingangsbilds rechnet Mittelwert und
Streuung INNERHALB der Maske; eine andere Maske verschiebt das Eingangsbild im ganzen
Volumen (hier -0,10 Sigma, Streuungsverhaeltnis 1,12), nicht nur am Rand. Folge: keine der
110 Vorhersagen identisch, im Mittel 832 abweichende Voxel.

Groessenordnung: 0,030 Dice durch die Maske gegen 0,032 Dice, die eine ganze
Architekturaenderung zu bringen schien -- und die sich als dieses Maskenartefakt erwies.

Regel daraus: bei jedem Modellvergleich die Maskenherkunft mitprotokollieren; zwei Zahlen ohne
gleiche Maske sind nicht vergleichbar. Ein ausgeliefertes Werkzeug, das zur Laufzeit eine
andere Maske ableitet als die Trainingskette (z. B. `flair > 0` statt HD-BET), hat damit ein
drittes Modell. Gegenmittel in Pruefung: maskenunabhaengige Normierung (Median/IQR,
Perzentile ohne Maske), Kriterium ist die kleinste Spanne ueber Maskenvarianten.

## Traegt
Jedes Netz, das Intensitaeten innerhalb einer Maske normiert (z-Score, Perzentile in der Maske). Gilt fuer WMH ebenso wie fuer andere Laesionsaufgaben.

## Traegt nicht
Modelle mit maskenfreier Normierung oder mit Normierung, die im Training zufaellig variiert wurde; dort ist der Effekt kleiner, aber nicht gemessen.

## Bruchindikator
Eine Messreihe mit zwei verschiedenen Masken desselben Verfahrens, deren gepaarte Dice-Differenz unter 0,005 liegt.

## Ablesung
Eigene Messung, 110 oeffentliche Challenge-Testfaelle (Kuijf et al. 2019, doi:10.1109/TMI.2019.2905770; Testsatz seit 2022 oeffentlich, doi:10.34894/AECRSD). Tier 1a.

## Verknuepft
- [architecture-package-brought-no-gain](architecture-package-brought-no-gain.md)
- [measure-tails-paired-not-by-percentile](../rules/measure-tails-paired-not-by-percentile.md)
