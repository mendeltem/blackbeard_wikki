---
id: qc-build-order-for-a-new-lesion-type
typ: regel
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-08
herkunft: Projekte valdo-t2s (CMB), mb-arena (eigene CMB-Kohorten), pvs-arena (BELOVE-QC, Rating-Seite wp8), Liquor-Regel-Ebenen und Vorlesungsanimation 2026-10-08; Nutzer 08.10.: "Regeln aufstellen, damit wir nicht immer von 0 anfangen"
verweist_auf: [qc-slice-viewer-conventions, slice-viewer-as-shared-tool, show-what-a-rule-removes-before-trusting-it, reference-first-then-metric-then-model]
---

# Qualitaetskontrolle fuer eine neue Laesionsart: in dieser Reihenfolge bauen, nie von null

## Aussage
Die CMB-Qualitaetskontrolle ist die Vorlage. Fuer jede neue Laesionsart (PVS, WMH,
Infarkt, Lakunen) gilt dieselbe Reihenfolge; nur die Lader und die Wortwahl wechseln.

1. **Erst der Generator, nie eine neue Seite.** Die Seite (PAGE) bleibt, es kommt ein
   Lader je Datenlage dazu: Manifest mit `id` und Pfaden, Bild, Referenz oder
   Vergleichsmaske, je Lauf eine Wahrscheinlichkeits- oder Maskendatei mit Schwelle.
   Gemessen: der PVS-Betrachter fuer 73 Faelle war mit einem Lader von 150 Zeilen in
   einer Stunde fertig, weil PAGE, Umriss, Farben und Tasten aus dem CMB-Generator kamen.
2. **Ohne Handreferenz: die Vergleichsmaske heisst Vergleich.** Links blau steht dann
   die Pipeline- oder Fremdmaske, auf der Seite ausdruecklich "not a reference";
   alle Zaehler heissen Uebereinstimmung ("both / only method / only pipeline"), nie
   TP/FP/FN. Die gepoolten Zahlen der Seite muessen den Zahlen des Messskripts
   gleichen (BELOVE: behalten 9.591 / 2.120 / 33.237 = F6.2), sonst ist ein Lader falsch.
3. **Ein Modell: Urteilsfarben. Mehrere Modelle: Modellfarben.** Gruen erkannt, gelb
   Fehlalarm, rot verpasst (`--verdict`); beim Vergleich mehrerer Laeufe die
   Goldener-Schnitt-Farben ohne das blaue Band.
4. **Jede Regel bekommt eigene Ebenen, bevor sie in die Kette kommt.** Die Karte, auf
   der die Regel beruht (SynthSeg-Liquor als Fuellung), die Komponenten, die sie als
   Fehlalarm entfernt, und die, die sie entfernt, obwohl sie eine Referenz beruehren;
   Zaehler je Schicht, je Fall, gepoolt. Die Liquor-Regel loeschte so sichtbar 62 von
   426 Treffern auf SWI, was die Summenzahl verdeckt hatte.
5. **Jeder Fund braucht sein Warum.** Je Komponente: Groesse in Voxeln und mm3, Zahl
   der Schichten, Form, Lage nach Gewebekarte, p max, Zuordnung zur Referenz, und die
   Nachbarschichten als Stapel. Ein Gefaess laeuft durch die Schichten, eine
   Mikroblutung nicht; das sieht man nur im Stapel, nicht in der Schicht.
6. **Rating ist eine eigene Seite, nicht die QC-Seite.** Verblindet (p und
   Pipeline-Treffer erst nach dem Urteil), Reihenfolge zufaellig mit festem Seed je
   Fall, jedes Urteil sofort per POST in eine Datei je Fall, Definition der Laesion
   (STRIVE-2) in der LIESMICH, Zusatzfunde per Klick fuer den Recall der Decke,
   Auswerteskript liefert nur Summen je Verfahren und Groessenklasse.
7. **Patientendaten nur auf 127.0.0.1.** Live-Server im Projektordner, kein
   LAN, kein GitHub, keine Fallnummern auf der Tafel oder im Wiki. Oeffentlich nur
   oeffentliche Daten mit Lizenzzeile (VALDO: CC BY-NC-SA 4.0).
8. **Pruefung vor der Abgabe:** headless rendern bei 1400 und 1918 px, Zaehler gegen
   das Messskript, Rauchtest (Dateien laden, Konsole leer, bei Rating zwei Urteile
   schreiben und lesen), Rauchtest-Urteile danach beiseitelegen.
9. **Vorlesung ist ein eigenes Artefakt.** Animation oder Deck zeigen die Kette mit
   echten Schichten und echten Funden, aber sie ersetzen die QC-Seite nicht und
   kommen nicht in den QC-Ordner.
10. **Nach jeder Seite drei Zeilen hier:** was neu war, welche Setzung der Nutzer
    geaendert hat, welche Zahl die Seite bestaetigt oder widerlegt hat.

## Traegt
Detektion und Segmentierung kleiner Laesionen auf MRT, mit oder ohne Referenz, eigene
und oeffentliche Kohorten, NiiVue- wie Bildstapel-Seiten.

## Traegt nicht
Volumetrie ohne Komponenten; Seiten, die Patientendaten verlassen muessten (dann nur
Summen und synthetische Beispiele).

## Bruchindikator
Eine neue Laesionsart braucht mehr als einen Tag bis zur ersten QC-Seite, oder die
gepoolten Zahlen der Seite weichen vom Messskript ab.

## Ablesung
Setzungen aus den Projekten valdo-t2s, mb-arena und pvs-arena bis 2026-10-08; Zahlen
aus den jeweiligen ARBEIT.md. Der gemeinsame Generator als Tool ist der offene
Pruefpunkt [slice-viewer-as-shared-tool].

## Verknuepft
- [qc-slice-viewer-conventions](qc-slice-viewer-conventions.md)
- [slice-viewer-as-shared-tool](../open_checks/slice-viewer-as-shared-tool.md)
- [show-what-a-rule-removes-before-trusting-it](../../lesion_detection_method/rules/show-what-a-rule-removes-before-trusting-it.md)
- [reference-first-then-metric-then-model](../../lesion_detection_method/rules/reference-first-then-metric-then-model.md)
