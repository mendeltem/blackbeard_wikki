---
id: official-label-2-rule-deletes-the-prediction
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: []
---

# Die offizielle Challenge-Metrik loescht Vorhersagen auf Label 2, sie zaehlt sie nicht als Fehlalarm

## Aussage
Am Quelltext der Challenge-Auswertung belegt (github.com/hjkuijf/wmhchallenge,
`evaluation.py`, Zeilen 47-50): die Referenz wird auf Label 1 reduziert UND die Vorhersage
wird auf allen Label-2-Voxeln (andere Pathologie) geloescht:

```python
maskedTestImage   = sitk.BinaryThreshold(testImage, 0.5, 1.5, 1, 0)   # Referenz: nur Label 1
nonWMHImage       = sitk.BinaryThreshold(testImage, 1.5, 2.5, 0, 1)   # 0 genau auf Label 2
maskedResultImage = sitk.Mask(resultImage, nonWMHImage)               # Vorhersage dort geloescht
```

`testImage` ist die Referenz (irrefuehrend benannt), `resultImage` die Vorhersage. Also:
`ref = (ref == 1)` und `pred = pred & (ref != 2)`. Eine Konvention, die die Vorhersage stehen
laesst und als Fehlalarm zaehlt, ist zu streng: an fuenf Modellen auf 110 Testfaellen
**+0,005 bis +0,007 Dice** (z. B. 0,7195 -> 0,7263), AVD etwa -3 Prozentpunkte,
Laesions-F1 +0,001, Laesions-Recall exakt unveraendert (er haengt nur an Referenzkomponenten --
das ist die Probe, dass richtig gerechnet wurde). 42 der 110 Faelle tragen Label 2; der Median
der fallweisen Differenz ist 0, das Maximum +0,49 in einem Fall.

Monatelang liefen im Projekt zwei Konventionen nebeneinander, und Zahlen aus beiden standen in
einer Tabelle. Vor jedem Vergleich pruefen, mit welcher Funktion gemessen wurde.

## Traegt
Jede Zahl, die mit der Challenge-Rangliste (sysu_media 0,80 usw.) verglichen werden soll.

## Traegt nicht
Eigene Kohorten ohne Label 2; dort ist die Frage gegenstandslos.

## Bruchindikator
Die Veranstalter aendern `evaluation.py`.

## Ablesung
Quelltext der Challenge-Auswertung, gelesen 2026-09-13; eigene Nachrechnung an fuenf Modellen. Tier 1a.

## Verknuepft
- [literature-dice-levers-for-wmh](literature-dice-levers-for-wmh.md)
