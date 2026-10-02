---
id: token-billing-scales-with-tasks
typ: mechanismus
status: vorschlag
thema: knowledge/ai_buyers
stand: 2026-10-02
herkunft: Gespraech Projekt NVIDIA-Roadmap, 2026-09
verweist_auf: [open-search-space, bandwidth-bottleneck, demand-is-not-earnings, iso-capability-cost-halving, billed-inference-volume]
---

# Abrechnung je Token bindet Umsatz an Aufgaben

## Aussage
Modellanbieter rechnen ueberwiegend je verarbeitetem Token ab, nicht je Nutzer und Monat. Damit haengt ihr Umsatz an der Zahl erledigter Aufgaben und an der Laenge jeder Aufgabe, nicht an der Zahl der Sitzplaetze.

Agentische Arbeit verstaerkt beides: Eine Aufgabe besteht aus mehreren Modellaufrufen hintereinander (Groessenordnung zehn bis zwanzig, Annahme), und jeder Aufruf traegt den bis dahin gewachsenen Kontext mit. Rechenbedarf und vor allem Speicherbedarf je Aufgabe wachsen deshalb schneller als die Nutzerzahl.

Fuer die Hardwareseite folgt daraus: Der Bedarf an Bandbreite und an Platz fuer Zwischenzustaende (KV-Cache) waechst mit der Aufgabenzahl, nicht mit der Zahl verkaufter Lizenzen.

## Traegt
Eine Erklaerung, warum die Nachfrage nach Rechen- und Speicherkapazitaet schneller steigen kann als die Verbreitung der Werkzeuge, und warum Preissenkungen je Token den Gesamtverbrauch erhoehen koennen statt ihn zu senken.

## Traegt nicht
Keine Zahl. Die zehn bis zwanzig Aufrufe je Aufgabe sind eine Annahme aus der Beobachtung, kein gemessener Wert; ebenso wenig ist belegt, wie viel Speicher je Aufgabe tatsaechlich gebunden wird.

Kein Schluss auf Gewinn, weder beim Modellanbieter noch beim Speicherhersteller; dafuer gilt [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md).

Effizienzfortschritte wirken gegen den Mechanismus: kuerzere Kontexte, Quantisierung, Cache-Kompression, kleinere Modelle fuer einfache Schritte.

Der Preis je Token faellt gemessen schnell: fuer ein festes Faehigkeitsniveau halbiert er sich alle 1,6 bis 7,3 Monate ([iso-capability-cost-halving](../../model_capability_cost/findings/iso-capability-cost-halving.md)). Umsatz je Aufgabe entsteht also nur, wenn die Zahl der Aufrufe schneller steigt als der Preis faellt. Beide Groessen sind hier nicht gemessen, deshalb traegt dieser Eintrag keine Umsatzaussage, sondern nur die Richtung der Mengenseite. Was tatsaechlich abgerechnet wird, ist offen ([billed-inference-volume](../../model_capability_cost/open_checks/billed-inference-volume.md)).

## Bruchindikator
- Anbieter stellen auf Pauschalpreise je Nutzer um; dann entkoppelt sich ihr Umsatz vom Verbrauch.
- Messbar sinkende Zahl der Modellaufrufe je erledigter Aufgabe bei gleichem Ergebnis.

## Ablesung
Preismodelle der Anbieter, oeffentlich. Aufrufe je Aufgabe: eigene Beobachtung, blind. Eine belastbare Messung fehlt.

## Verknuepft
- [open-search-space](../../ai_demand_drivers/axioms/open-search-space.md)
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
- [anthropic-revenue-runrate](../findings/anthropic-revenue-runrate.md)
- [iso-capability-cost-halving](../../model_capability_cost/findings/iso-capability-cost-halving.md)
- [model-cost-falls-faster-than-hardware](../../model_capability_cost/mechanisms/model-cost-falls-faster-than-hardware.md)
- [billed-inference-volume](../../model_capability_cost/open_checks/billed-inference-volume.md)
