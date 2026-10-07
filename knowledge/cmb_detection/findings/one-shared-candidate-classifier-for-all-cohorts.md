---
id: one-shared-candidate-classifier-for-all-cohorts
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), cmb/stage2/final_classifier.py, gemessen 2026-10-07
verweist_auf: [csf-rule-removes-false-alarms-without-loss, two-seeds-per-decision-below-0.08]
---

# Ein einziger Kandidaten-Klassifikator ueber alle Kohorten ersetzt die Liquor-Regel und braucht keine Gewebekarte

## Aussage
Zweite Stufe eines CMB-Detektors: jede Komponente ueber einer niedrigen Schwelle (p > 0,15,
>= 1 mm3) wird zum Kandidaten; ein kleines 3D-CNN (drei Doppelfaltungsbloecke 16/32/64,
0,22 M Parameter) sieht Bild, FRST-Karte und Wahrscheinlichkeit der ersten Stufe in einem
16-mm-Wuerfel und sagt ja/nein. Je Kohorte trainiert lernt es nichts (zu wenige Kandidaten);
auf dem **Pool aller Kohorten** (oeffentlich VALDO 278 + zwei klinische Kohorten, 2230
Kandidaten, 1164 positiv) wird daraus EIN auslieferbares Modell mit EINER Schwelle (0,30,
per 5-fach-Kreuzvalidierung je Fall ueber den Pool gewaehlt, out-of-fold):

- gepoolt F1 0,675 (P 0,72, S 0,63);
- VALDO 0,624 = Liquor-Regel 0,631 (-0,008 [-0,048; +0,043]), gegen Schwelle allein +0,060 [+0,009; +0,129];
- T2*-Kohorte 0,676 = Regel (+0,001);
- SWI-Kohorte 0,684, **+0,061 [+0,014; +0,104] gegen die Regel** (die dort echte Blutungen loescht).

Der Klassifikator bekommt KEINE Gewebeklasse als Eingang und lernt die Liquor-Regel
trotzdem; damit faellt FreeSurfer/SynthSeg als Abhaengigkeit eines Produkts weg.

## Traegt
Jeder Zwei-Stufen-Detektor fuer kleine, seltene Laesionen, bei dem die Kandidatenmenge je
Datensatz zu klein ist: Kandidaten ueber Datensaetze poolen, eine Schwelle, ein Modell.
Ein auf VALDO-Kandidaten allein trainierter Klassifikator uebertraegt ohne Anpassung
(SWI 0,671 gegen 0,672 gepoolt) -- die zweite Stufe ist kohortenunabhaengiger als die erste.

## Traegt nicht
Die erste Stufe: U-Nets uebertragen NICHT zwischen Sequenzen (VALDO-T2*-Netz auf SWI 0,305
gegen 0,626 eigenes Training); je Sequenz ein eigenes Netz bleibt noetig.

## Bruchindikator
Eine Kohorte, auf der der gemeinsame Klassifikator messbar unter die Liquor-Regel faellt
(Intervall unter Null), oder ein Datensatz ohne Liquor-Fehlalarme, auf dem er nichts zu
lernen hat.

## Ablesung
Eigene Messung, out-of-fold ueber den Pool, gepaarter Bootstrap ueber Faelle (5000 Zuege).
Klassifikator-Muster nach Setio et al. 2016 (doi:10.1109/TMI.2016.2536809). Tier 1a.

## Verknuepft
- [csf-rule-removes-false-alarms-without-loss](csf-rule-removes-false-alarms-without-loss.md)
- [two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md)
