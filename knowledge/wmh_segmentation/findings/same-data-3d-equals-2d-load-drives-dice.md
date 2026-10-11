---
id: same-data-3d-equals-2d-load-drives-dice
typ: befund
status: vorlaeufig
thema: knowledge/wmh_segmentation
stand: 2026-10-11
herkunft: Alita, WMH-Pool 311 (170 Challenge + 141 eigene Faelle), 5 identische Falten, offizielle Label-2-Auswertung, Schwelle 0,5
verweist_auf: [literature-dice-levers-for-wmh, unseen-scanners-are-not-the-weak-spot]
---

# Gleiche Daten: 3D- und 2D-U-Net gleich gut; der Dice haengt vor allem an der WMH-Last

## Aussage
Auf einem gemischten Pool (5 Falten geschichtet nach Kohorte x Aufnahmegeometrie x WMH-Volumen)
erreichen ein anisotropes 3D-U-Net (Patch 16x96x96, Zentrumskopf) und ein 2D-U-Net mit Attention
denselben Dice, wenn beide auf denselben Faellen trainiert werden. Der frueher gemessene 3D-Vorsprung
auf der Challenge (+0,06) war ein Effekt der Trainingsdaten. 3D behaelt einen Vorteil beim
Laesions-F1 auf 1-mm-isotropen Daten. Beide schlagen BIANCA deutlich.

## Zahlen (Zwischenstand 11.10., 2D erst 1 von 5 Falten auf identischen Faellen)
- 3D vs 2D, 63 gemeinsame Faelle: Dice +0,004 [-0,011; +0,020], Laesions-F1 +0,016 [-0,005; +0,038];
  1-mm-Kohorte Laesions-F1 +0,077 [+0,034; +0,123].
- 3D vs BIANCA, alle 311: Dice 0,711 vs 0,600, +0,111 [+0,100; +0,123]; Laesions-F1 +0,328.
- Dice nach WMH-Last (3D, 311): < 5 ml 0,573 (n=116), 5-15 ml 0,745 (n=77), > 15 ml 0,824 (n=118).
  Bei gleicher Last liegen eigene Kohorten unter der Challenge, vor allem bei wenig WMH (0,39-0,47 vs 0,70).

## Folgerung
Dice je Kohorte nur zusammen mit der WMH-Last berichten (geschichtet), sonst sehen Kohorten mit
wenig WMH schlechter aus, als das Modell ist. Architekturvergleiche nur auf identischen Trainingsdaten.
Offen: Aequivalenztest nach allen 5 Falten, 2x2 Architektur x Daten, Resampling-Test der 1-mm-Kohorten.
