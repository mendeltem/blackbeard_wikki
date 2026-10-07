---
id: empty-target-looks-like-a-low-loss
typ: risiko
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: []
---

# Ein nicht mitgedrehtes Ziel liefert einen VERDAECHTIG NIEDRIGEN Verlust, keinen Fehler

## Aussage
Drei Tage Rechenzeit gingen an eine Zeile: das Bild wurde fuer das 2D-Training mit
`np.moveaxis` nach (z, x, y) gedreht, Ziel und Gueltigkeitsmaske aber nicht. `ziel[z]` griff
damit sagittale Randebenen ab: **0 von 8 219 WMH-Voxeln** erreichten je das Training.

Drei Dinge machten den Fehler unsichtbar:
- `crop_pad` fuellt jede Form stumm auf 256x256 auf; keine Form- und keine Wertpruefung schlug an.
- Der geglaettete Dice-Verlust (`+1.0` in Zaehler und Nenner) ist bei leerem Ziel und leerer
  Vorhersage perfekt: Verlust 0,007 gegen 0,086 beim gesunden Lauf. **Der niedrige Verlust war
  das Symptom, nicht die Guete.**
- Ausserhalb der Gueltigkeitsmaske gab es keinen Gradienten; das Netz blieb bei p ~ 0,5, und bei
  Schwelle 0,3 lag der Median der Vorhersage bei 74 % der Hirnmaske. Recall 0,74-0,84 und
  Herd-F1 bis 0,89 sahen gut aus, weil EIN Klecks jede Referenzlaesion trifft: die Herdmetrik
  belohnt den Totalausfall.

Gegenmittel: Bild, Ziel und Masken in EINER Laderoutine gemeinsam drehen. Bei Dice nahe null
mit hohem Recall und Herdzahl 1 zuerst zwei Zahlen messen, bevor irgendetwas anderes gelesen
wird: (1) Summe der Zielvoxel ueber die Trainings-Patches gegen die Referenzsumme, (2)
Vorhersagevolumen gegen Hirnmaske. Gewinnt die Schwellensuche immer den untersten Gitterpunkt,
ist die Karte gesaettigt und das Netz untrainiert. Einen Verlust UNTER dem des gesunden
Vergleichslaufs nie als Fortschritt lesen.

## Traegt
Jedes Segmentierungstraining mit geglaettetem Dice und getrennten Lade- oder Augmentierungswegen fuer Bild und Ziel.

## Traegt nicht
---

## Bruchindikator
---

## Ablesung
Eigener Vorfall 2026-09-15, am Code belegt. Tier 1a.

## Verknuepft
- [brain-mask-is-part-of-the-model](../findings/brain-mask-is-part-of-the-model.md)
