---
id: front-loaded-capex
typ: axiom
status: getragen
thema: knowledge/ai_demand_drivers
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [refresh-instead-of-new-build, bandwidth-bottleneck, lead-times-datacenter-vs-fab]
---

# Frontlastiger Capex

## Aussage
Der Capex der Rechenzentren ist frontlastig, nicht dauerhaft. Gebäude, Stromzuführung, Netzanschluss und Kühlung sind Einmalaufwand mit langer Nutzungsdauer. Steht ein Standort, kostet der Austausch der Rechner deutlich weniger als ein Neubau. Der heutige Capex-Stand überzeichnet daher den Dauerbedarf. Das knappe und dauerhafte Gut ist der Netzanschluss, nicht der Beton.

Bedingung, ohne die die Setzung nicht gilt: der Standort wurde mit Leistungsreserve für mindestens eine Folgegeneration ausgelegt. Zu prüfen je Baujahrgang, nicht global.

Spannung zu bandwidth-bottleneck: der schnellste Beschleuniger ist auch der mit der höchsten Leistungsdichte. Jenes Axiom treibt genau die Größe, die dieses bricht. Beide dürfen nie gemeinsam in ihrer starken Form verwendet werden.

## Trägt
Speichernachfrage aus Refresh auch bei sinkendem Kunden-Capex. Deshalb wird Nachfrage über installierte MW und Refresh-Takt modelliert.

## Trägt nicht
Drop-in bei Hallen ohne Reserve. Auch keine Aussage über die Höhe des Dauer-Capex.

## Bruchindikator
Leistungsaufnahme je Rack der Folgegeneration übersteigt die ausgelegte Reserve des Baujahrgangs. Dann müssen Stromverteilung und Kühlung mit erneuert werden, und die Refresh-Kosten nähern sich den Neubaukosten.

## Ablesung
Herstellerspezifikationen der Rack- und Beschleunigergenerationen, Tier 1b, gegen Auslegungsangaben der Betreiber, Tier 1a. Je Baujahrgang und Standort getrennt. Wörtlich aus dem Projektprompt verdichtet; Setzung von Mendel.

## Verknüpft
- [refresh-instead-of-new-build](../mechanisms/refresh-instead-of-new-build.md)
- [bandwidth-bottleneck](bandwidth-bottleneck.md)
- [lead-times-datacenter-vs-fab](../mechanisms/lead-times-datacenter-vs-fab.md)
