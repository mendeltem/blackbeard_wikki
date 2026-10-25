# wmh_segmentation: Kurzstand

**New 2026-10-25 (what is a good Dice, given rater variance):** Inter-rater Dice on FLAIR 0.70-0.81, intra-rater 0.72-0.86, only 0.51 at <= 5 ml lesion load; the 2017 winner (0.80) sits inside the human band. Report Dice by load class plus lesion F1 ([human-rater-variance-and-good-dice-for-wmh-2026-10](findings/human-rater-variance-and-good-dice-for-wmh-2026-10.md)).

Stand 2026-10-07. Prefill fuer Chats und Agenten. Details in [INDEX.md](INDEX.md).

WMH auf FLAIR mit 2D-U-Nets, Messlatte WMH Segmentation Challenge 2017 (110 oeffentliche
Testfaelle, offizielle Label-2-Regel, gepaart mit Bootstrap). Eigene Zahlen darauf sind
Eigenmessungen, keine Platzierungen; Sieger 0,80, Beobachter 0,77/0,79, eigenes ausgeliefertes
Modell 0,725.

**Getragen (Befunde):** Die Hirnmaske ist Teil des Modells: 3 % Maskenunterschied verschieben
ueber die z-Normierung das ganze Eingangsbild und kosten 0,030 Dice -- so viel wie eine ganze
Architekturaenderung, die sich als genau dieses Artefakt erwies. Eine zweite Bias-Korrektur
(`fast -B`) auf schon korrigierten Challenge-Daten hilft trotzdem (Dice +0,011, Laesions-Recall
+0,037, Training stabiler): sie wirkt als Intensitaetsvereinheitlichung ueber Scanner. Der
Challenge-Code LOESCHT Vorhersagen auf Label 2 statt sie als Fehlalarm zu zaehlen (~0,006 Dice).
Ein 2D-Netz sieht Schnitte, nicht Faelle: Schichtdicke 0,49 bis 6 mm ist Faktor 12 im Gewicht je
Fall; mehr gemischte Daten kosteten 0,047 Dice auf der Zieldomaene. Ungesehene Scanner sind nicht
die Schwachstelle, alle Ausfaelle liegen auf bekannten Geraeten; nach Voxelvolumen stratifizieren,
nicht nach Standort. Literatur-Hebel: Ensemble +1,98 %, Augmentierung +1,38 % (Bereich!), TTA
+0,8-1,4, Ortsmerkmale bis +5; Instanzverluste, T1 und 3D bei 3 mm bringen nichts. Ein als Paket
geaendertes Netz brachte nichts und kostete Laesions-Recall.

**Regel:** Randverhalten (Ausfaelle, Untergruppen) gepaart messen, mit fester Perzentilmethode
und Bootstrap-Intervall; ein 5. Perzentil aus 30 Faellen traegt keinen Befund.

**Risiko:** Ziel und Maske nicht mit dem Bild gedreht: null Zielvoxel im Training, und der
geglaettete Dice meldet einen verdaechtig NIEDRIGEN Verlust. Zielvoxel-Summe und
Vorhersagevolumen zuerst pruefen.

**Lesen bei:** WMH, FLAIR, Hirnmaske, HD-BET, Bias-Korrektur, 2D-U-Net, gemischte Kohorten,
Challenge-Metrik, Scanner-Robustheit, Perzentile, Dice-Verlust.
- 11.10.: Pool 311 (5 identische Falten): mit gleichen Trainingsdaten sind 3D- und 2D-U-Net beim Dice gleich (+0,004 [-0,011; +0,020]), beide deutlich vor BIANCA (+0,111); der Dice haengt vor allem an der WMH-Last, deshalb geschichtet berichten (vorlaeufig, 2D 1/5 Falten).
