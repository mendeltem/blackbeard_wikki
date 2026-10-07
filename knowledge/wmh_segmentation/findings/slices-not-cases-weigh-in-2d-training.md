---
id: slices-not-cases-weigh-in-2d-training
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: [official-label-2-rule-deletes-the-prediction]
---

# Ein 2D-Netz sieht Schnitte, nicht Faelle: Schichtdicke bestimmt das Gewicht je Fall

## Aussage
Bei gemischten Kohorten zaehlt fuer ein 2D-Netz die Zahl der Schnitte mit Hirn je Fall, und
die haengt an der Schichtdicke. Gemessen an 201 Faellen aus vier Quellen (echte Hirnmasken,
Schnitte ohne Hirn uebersprungen): die 60 Challenge-Trainingsfaelle (3 mm) stellen 44 Schnitte
je Fall und nur **13,5 %** aller 19 650 Schnitte; eine duenngeschichtete Kohorte (0,49 mm) mit
20 Faellen stellt 293 je Fall und 29,8 %. Zwischen 0,49 und 6 mm liegt ein **Faktor 12** im
Gewicht je Fall. Jeder Challenge-Schnitt stand gegen 6,4 fremde, obwohl der Testsatz zu 100 %
aus der Challenge-Domaene stammt.

Dazu passt: dasselbe Netz erreicht, auf den 60 Challenge-Faellen allein trainiert, Dice 0,772
auf den 110 Testfaellen; auf allen 201 Faellen nur 0,725 (offizielle Regel). Mehr Daten
kosteten 0,047. Die Schnittbilanz ist dafuer eine plausible und vor allem behebbare Erklaerung
(Schnitte je Fall deckeln oder je Kohorte gewichten), anders als "Domaenenverschiebung".

Verworfene Vermutung, nicht erneut aufrollen: ein Orientierungsfehler beim Schneiden. Bei
allen 201 Faellen ist Achse 2 die S/I-Achse; die duennen Kohorten sind schlicht duenn
aufgenommen.

## Traegt
Jedes 2D- oder 2,5D-Netz auf gemischten Kohorten, auch ausserhalb von WMH. Vor dem Training `maske.any(axis=(0,1)).sum()` je Fall zaehlen.

## Traegt nicht
3D-Netze mit Patches gleicher physikalischer Groesse.

## Bruchindikator
Ein Lauf mit gedeckelten Schnitten je Fall, der den Abstand 0,772 gegen 0,725 nicht verkleinert.

## Ablesung
Eigene Zaehlung und Messung; Challenge-Zahlen oeffentlich, Zusammensetzung der uebrigen Kohorten hier bewusst nicht genannt. Tier 1a.

## Verknuepft
- [official-label-2-rule-deletes-the-prediction](official-label-2-rule-deletes-the-prediction.md)
- [unseen-scanners-are-not-the-weak-spot](unseen-scanners-are-not-the-weak-spot.md)
