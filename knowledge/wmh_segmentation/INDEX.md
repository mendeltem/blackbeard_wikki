# wmh_segmentation

Automatische Segmentierung von White Matter Hyperintensities (WMH) auf FLAIR mit 2D-U-Nets.
Messlatte ist die oeffentliche WMH Segmentation Challenge 2017 (Kuijf et al. 2019,
doi:10.1109/TMI.2019.2905770; 60 Trainings- und 110 Testfaelle, Testsatz seit 2022
oeffentlich, doi:10.34894/AECRSD). Alle Zahlen hier stammen von diesen 110 Testfaellen,
gemessen mit der offiziellen Label-2-Regel, gepaart ueber Faelle mit Bootstrap-Intervall.
Eigene Kohorten kommen nur als Summen ohne Namen vor. Das Werkzeug dazu:
`tools/mri/mri_segmentation/wmh/` und das Repo wmhseg (Seite mit NiiVue-Betrachter).

Stand 2026-10-07. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt | Status |
|---|---|---|---|
| befund | [brain-mask-is-part-of-the-model](findings/brain-mask-is-part-of-the-model.md) | 3 % Maskenunterschied = 0,030 Dice ueber die z-Normierung in der Maske; so gross wie der ganze Architekturgewinn | getragen |
| befund | [second-bias-correction-helps-on-mixed-scanners](findings/second-bias-correction-helps-on-mixed-scanners.md) | `fast -B` auf schon korrigierten Daten: ohne ihn Dice -0,011 und Laesions-Recall -0,037, Startwert-Streuung dreifach | getragen |
| befund | [official-label-2-rule-deletes-the-prediction](findings/official-label-2-rule-deletes-the-prediction.md) | Challenge-Code loescht die Vorhersage auf Label 2; strengere Konvention ist ~0,006 Dice zu tief | getragen |
| befund | [slices-not-cases-weigh-in-2d-training](findings/slices-not-cases-weigh-in-2d-training.md) | Schichtdicke 0,49 bis 6 mm = Faktor 12 im Gewicht je Fall; 60 Challenge-Faelle nur 13,5 % der Schnitte; 0,772 gegen 0,725 | getragen |
| befund | [unseen-scanners-are-not-the-weak-spot](findings/unseen-scanners-are-not-the-weak-spot.md) | Testsatz hat fuenf Geraete, nicht drei Standorte; alle Ausfaelle auf bekannten Scannern | getragen |
| befund | [literature-dice-levers-for-wmh](findings/literature-dice-levers-for-wmh.md) | Ensemble +1,98 %, Augmentierung +1,38 %, TTA +0,8-1,4; Instanzverluste und T1 bringen nichts; Testsatz-Zahlen sind Eigenmessungen | getragen |
| befund | [architecture-package-brought-no-gain](findings/architecture-package-brought-no-gain.md) | Neues Netz als Paket: Dice unentschieden, Laesions-Recall -0,038; Bausteine einzeln aendern | getragen |
| befund | [same-data-3d-equals-2d-load-drives-dice](findings/same-data-3d-equals-2d-load-drives-dice.md) | Pool 311, gleiche Falten: 3D = 2D beim Dice (+0,004), beide >> BIANCA (+0,111); Dice haengt an der WMH-Last (<5 ml 0,57, >15 ml 0,82) | vorlaeufig |
| regel | [measure-tails-paired-not-by-percentile](rules/measure-tails-paired-not-by-percentile.md) | 5. Perzentil bei n = 30 ist Rauschen, Vorzeichen haengt an der Interpolation; gepaart und mit Intervall messen | getragen |
| risiko | [empty-target-looks-like-a-low-loss](risks/empty-target-looks-like-a-low-loss.md) | Ziel nicht mitgedreht: 0 Zielvoxel im Training, geglaetteter Dice meldet perfekten Verlust | getragen |

## Herkunft
Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18, Arbeitsprotokolle und
Pruefberichte; uebertragen aus den Sitzungsnotizen am 2026-10-07.
