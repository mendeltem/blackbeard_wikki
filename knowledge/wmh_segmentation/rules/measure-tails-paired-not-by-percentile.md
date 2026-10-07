---
id: measure-tails-paired-not-by-percentile
typ: regel
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: [unseen-scanners-are-not-the-weak-spot]
---

# Randverhalten gepaart messen, nicht ueber Perzentile aus kleinen Gruppen

## Aussage
Ein gemeldeter Befund "das 5. Perzentil faellt von 0,313 auf 0,286, waehrend der Mittelwert
steigt" hielt nicht: bei n = 30 haengt das VORZEICHEN an der Interpolationswahl.

| Konvention | alt | neu | Differenz |
|---|---|---|---|
| `statistics.quantiles(n=20)[0]` (exclusive, Vorgabe) | 0,313 | 0,286 | -0,028 |
| `numpy.percentile(a, 5)` (linear) | 0,384 | 0,398 | +0,014 |
| numpy `method='lower'` | 0,370 | 0,327 | -0,043 |
| numpy `method='higher'` | 0,401 | 0,485 | +0,084 |

Bootstrap (20 000 Ziehungen, dieselben 30 Faelle): das 5. Perzentil hat SD 0,106 gegen 0,029
fuer den Mittelwert; der gemeldete Abfall war ein Viertel einer Standardabweichung. Bei n = 30
wird P5 vom 2. und 3. kleinsten Fall getragen; ein zweiseitiges verteilungsfreies 95-%-Intervall
dafuer existiert nicht mit endlicher Untergrenze.

Regel:
1. Perzentilmethode immer dazuschreiben und fuer alle Vergleiche EINE festlegen
   (Empfehlung `numpy.percentile`, linear).
2. Randverhalten gepaart messen: fallweise Differenz, Zahl verschlechterter Faelle, Zahl der
   Ausfaelle unter fester Schwelle (Dice < 0,5 und < 0,6), McNemar. Das hat bei n = 30
   Trennschaerfe, das Perzentil nicht.
3. Zu jedem Randmass ein Bootstrap-Intervall; ohne Intervall kein Befund.
4. Global (n = 110) ist P5 brauchbar, je Untergruppe (n = 10-30) nicht.

## Traegt
Jede Zuverlaessigkeitsaussage ueber Untergruppen (Scanner, Kohorte, Lastklasse).

## Traegt nicht
Grosse Gruppen (n > 100), dort sind Perzentile stabil genug.

## Bruchindikator
---

## Ablesung
Eigene Nachrechnung 2026-09-13. Tier 1a.

## Verknuepft
- [unseen-scanners-are-not-the-weak-spot](../findings/unseen-scanners-are-not-the-weak-spot.md)
