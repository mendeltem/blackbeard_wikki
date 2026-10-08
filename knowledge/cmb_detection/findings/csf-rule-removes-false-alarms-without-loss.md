---
id: csf-rule-removes-false-alarms-without-loss
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-08
herkunft: Projekt valdo-t2s (Alita), ARBEIT.md 4.3, gemessen 2026-09-20
verweist_auf: [sensitivity-levers-do-not-raise-lesion-f1, show-what-a-rule-removes-before-trusting-it, one-shared-candidate-classifier-for-all-cohorts]
---

# Eine Liquor-Regel aus der Gewebekarte entfernt die Haelfte der Fehlalarme, ohne eine Blutung zu verlieren

## Aussage
Von 176 Fehlalarmen des Detektors auf VALDO lagen 98 im freien Liquor (Ventrikel,
aeussere Liquorraeume) -- dort, wo eine Mikroblutung als parenchymale Laesion nicht
liegen kann. Regel: jede vorhergesagte Komponente, deren Mehrheitslabel in einer
SynthSeg-Segmentierung desselben Falls Ventrikel oder Liquor ist, wird verworfen.
Kein Parameter, nichts zu tunen. Ergebnis am festen Arbeitspunkt (Schwelle 0,3,
mindestens 2 mm3): **0,585 -> 0,646, 0 von 139 Blutungen verloren.**

Zwei Nebenbefunde: (a) gibt man dem Netz die Gewebekarte als Eingangskanaele, lernt es
die Regel selbst (keine Vorhersage mehr im Liquor), macht aber anderswo mehr Fehlalarme
(-0,058); die Regel nach dem Netz ist besser als die Karte vor dem Netz. (b) Auf SWI mit
duennen Schichten ist die harte Regel zu grob -- dort loescht sie echte Blutungen; ein
kleiner Kandidaten-Klassifikator mit der Gewebeklasse als Merkmal ersetzt sie
(SWI +0,044 [+0,012; +0,085] gegen die Regel, auf T2*/VALDO gleichauf).

## Traegt
Nachbearbeitung jedes CMB-Detektors, fuer den eine Gewebekarte zu haben ist.
SynthSeg laeuft kontrastunabhaengig auch direkt auf T2* (mit `--robust`).

## Traegt nicht
Blutungen an der Ventrikelwand oder im Plexus, wenn die Gewebekarte dort ungenau ist;
auf VALDO trat das nicht auf (0 Verluste), auf anderen Daten ist es zu pruefen.

## Bruchindikator
Ein Datensatz, auf dem die Regel echte Blutungen loescht (Sensitivitaet faellt).

## Ablesung
Eigene Messung VALDO 2021 Task 2. SynthSeg: Billot et al., Med Image Anal 2023,
doi:10.1016/j.media.2023.102789. Tier 1a.

## Nachtrag 2026-10-08: der Bruchindikator ist auf den eigenen Kohorten eingetreten
Im Schichtbetrachter (`--csf-overlay`, Regel auf der rohen Vorhersage des
Siegernetzes nur gezeigt, nicht angewendet) entfernt die Regel: VALDO 27
Fehlalarme und 1 von 139 Blutungen (Ensemble, 57 CV-Faelle); eigene SWI-Kohorte
88 Fehlalarme und **62 von 426 Blutungen** in 18 Faellen; eigene T2*-Kohorte 56
Fehlalarme und 15 von 545 Blutungen in 8 Faellen. Die Aussage "ohne Verlust" gilt
damit nur fuer VALDO. Fuer die eigenen Kohorten bleibt der gemeinsame
Kandidaten-Klassifikator die Nachbearbeitung; ob SynthSeg auf SWI (duenne
Schichten, Resampling auf 1 mm und zurueck) die Ventrikelwand und den Kortex zu
grob zeichnet oder die Regel fuer diese Anatomie falsch ist, ist am Bild zu
pruefen (Ebenen `csf_drop_tp`, `csf_free`, `csf_vent`).

## Verknuepft
- [sensitivity-levers-do-not-raise-lesion-f1](sensitivity-levers-do-not-raise-lesion-f1.md)
- [show-what-a-rule-removes-before-trusting-it](../../lesion_detection_method/rules/show-what-a-rule-removes-before-trusting-it.md)
- [one-shared-candidate-classifier-for-all-cohorts](one-shared-candidate-classifier-for-all-cohorts.md)
