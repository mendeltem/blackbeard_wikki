---
id: false-alarms-cluster-by-anatomy
typ: mechanismus
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekt valdo-t2s (CMB), ARBEIT.md 4.3, gemessen 2026-09-20; uebertragen 2026-10-07
verweist_auf: [csf-rule-removes-false-alarms-without-loss, sensitivity-needs-a-discriminator]
---

# Fehlalarme haben einen Ort: erst zaehlen, dann eine parameterfreie Regel nach dem Netz

## Aussage
Bevor man einen Detektor verbessert, die Fehlalarme nach anatomischem Ort auszaehlen
(Gewebekarte desselben Falls, z. B. SynthSeg, laeuft kontrastunabhaengig). Auf CMB lagen
98 von 176 Fehlalarmen im freien Liquor, wo die Laesion nicht liegen kann. Eine Regel
ohne Parameter ("Komponente mehrheitlich im Liquor -> weg") brachte 0,585 -> 0,646 bei
0 von 139 verlorenen Blutungen.

Zwei Mechanismen dahinter:
1. Die Regel NACH dem Netz ist besser als die Karte VOR dem Netz: mit der Gewebekarte
   als Eingangskanal lernt das Netz die Regel selbst, macht aber anderswo mehr Fehlalarme
   (-0,058). Das Netz soll Laesionen finden; Anatomie ist eine Nebenbedingung, keine
   Eingabe.
2. Eine harte Regel wird dort falsch, wo die Karte an der Grenze ungenau ist (SWI mit
   duennen Schichten: echte Blutungen an der Ventrikelwand geloescht). Dann ersetzt ein
   kleiner Kandidaten-Klassifikator mit der Gewebeklasse als MERKMAL die Regel
   (SWI +0,044 gegen die Regel, auf T2* gleichauf).

Die Zaehlung ist billig (CPU, eine Stunde) und ordnet jede spaetere Idee ein: sagt sie
"meist Gefaesse", ist eine zweite Stufe das Werkzeug; sagt sie "meist echte, nicht
annotierte Laesionen", liegt der Engpass in der Referenz.

## Traegt
Jede Laesionsart mit anatomischem Ausschlussgebiet: CMB nicht im Liquor, PVS nicht im
Kortex oder in den Sulci, Lakunen nicht in den Ventrikeln.

## Traegt nicht
Laesionen, die selbst Liquorsignal tragen und an Liquorraeume grenzen (PVS, Lakunen):
dort darf die Regel nicht ueber die Intensitaetsklasse, sondern nur ueber die Lage
(Ventrikel, aeussere Liquorraeume, Sulci) gehen, und die Grenzgenauigkeit der Karte ist
vorher zu messen.

## Bruchindikator
Ein Datensatz, auf dem die Ortsregel echte Laesionen loescht (Sensitivitaet faellt,
Verluste in der Referenz nachgezaehlt).

## Ablesung
Eigene Messung VALDO 2021 Task 2. SynthSeg: Billot et al., Med Image Anal 2023,
doi:10.1016/j.media.2023.102789. Tier 1a.

## Verknuepft
- [csf-rule-removes-false-alarms-without-loss](../../cmb_detection/findings/csf-rule-removes-false-alarms-without-loss.md)
- [sensitivity-needs-a-discriminator](sensitivity-needs-a-discriminator.md)
