---
id: literature-dice-levers-for-wmh
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: [architecture-package-brought-no-gain, second-bias-correction-helps-on-mixed-scanners]
---

# Belegte Dice-Hebel fuer WMH auf FLAIR, und was nachweislich nichts bringt

## Aussage
Kernquelle ist die Ablation des Challenge-Siegers auf genau dieser Aufgabe
(Li et al. 2018, arXiv:1802.05203, Tab. 7, Split 48/12, Wilcoxon FDR-korrigiert).

**Wirkt:** Ensemble +1,98 % DSC (p = 0,012; 5 Modelle besser als 3, danach Saettigung).
Augmentierung +1,38 % (p = 0,003); entscheidend ist der Bereich -- ein reales
Voxelgroessenverhaeltnis von 1,21 lag ausserhalb von 0,9-1,1, dort war die Leistung am
schlechtesten. TTA +0,8 bis +1,4 Dice-Punkte (Wang et al. 2019, arXiv:1807.07356).
Ortsmerkmale +1,6 bis +5,3 Punkte (Ghafoorian et al. 2017, Sci Rep, doi:10.1038/s41598-017-05300-5);
typischer Fehler des ortsblinden Netzes: Septum pellucidum. Als blosser Eingabekanal nur +0,03,
als eigener Pfad mit Attention +1,44 (BAGAU-Net, arXiv:2010.09586, kleine Testmenge).

**Bringt nichts oder schadet:** Instanzverluste (blob loss, CC-DiceCE): Dice 0,771 -> 0,771,
Laesions-F1 -0,011 (arXiv:2511.17146; bei Mikroblutungen dagegen +0,052). T1 dazunehmen:
+0,62 % nicht signifikant, AVD schlechter (Li 2018). 3D statt 2D bei ~3 mm Schichtdicke: 2D
axial und triplanar signifikant besser (TrUE-Net, Sundaresan et al. 2021). Kleinkomponenten
loeschen: der Challenge-Auswertungscode filtert kein Mindestvolumen und nutzt 26er-Nachbarschaft,
Loeschen senkt Recall und F1 direkt.

**Eigene Gegenprobe:** ein Ensemble aus drei Startwerten brachte beim Dice nichts (-0,002,
unentschieden); die +1,98 % bestaetigen sich bei uns nicht, vermutlich weil die Startwerte
fast deckungsgleich laufen.

**Einordnung:** Challenge-Sieger 0,80; Beobachter 0,77/0,79; gepoolte Meta-Analyse 0,78
[0,74; 0,82]. Der Testsatz ist seit 2022 oeffentlich -- jede eigene Zahl darauf ist eine
Eigenmessung, keine Platzierung, und nie mit Zahlen vergleichen, die Autoren auf eigenen Kohorten
berichten. Kleine Laesionen sind die eigentliche Schwaeche (Laesions-Recall < 10 mm3 deutlich
unter dem Gesamtwert, auch bei menschlichen Beobachtern); deshalb immer nach Groessenklassen berichten.

## Traegt
Planung von Verbesserungsschritten an einem FLAIR-WMH-Netz: Reihenfolge Ensemble/TTA, Augmentierungsbereich, Ortsmerkmale.

## Traegt nicht
Uebertragung der Prozentzahlen auf andere Daten; sie sind auf 12 Validierungsfaellen gemessen.

## Bruchindikator
Eine Replikation mit anderem Vorzeichen bei einem der Hebel auf dem oeffentlichen Testsatz.

## Ablesung
Peer-reviewed bzw. Preprint wie angegeben (arXiv-Nummern nicht alle nachgeprueft); eigene Gegenprobe Tier 1a.

## Verknuepft
- [architecture-package-brought-no-gain](architecture-package-brought-no-gain.md)
- [second-bias-correction-helps-on-mixed-scanners](second-bias-correction-helps-on-mixed-scanners.md)
