---
id: cadence-and-yield-trough
typ: mechanismus
status: getragen
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Gespräch Projekt SK Hynix, 2026-10-02
verweist_auf: [bandwidth-bottleneck, sensing-and-experiment-loop]
---

# Kadenz und Yield-Tal

## Aussage
Schnellerer Chipentwurf (rekursive Verbesserung, interne Modelle) verkürzt den Generationsabstand der Beschleuniger. Die Nachfrage springt öfter auf eine neue HBM-Generation, die Lieferkette sitzt öfter im Yield-Tal mit weniger kumulierter Ausbringung je Generation. Das verlängert die Angebotslücke von der Angebotsseite.

## Trägt
Verlängerung der Angebotslücke ohne steigende Nachfrage.

## Trägt nicht
Sprünge in Sekunden. Die Schleife ist so schnell wie ihr langsamster physischer Schritt (Fertigung, Qualifikation von HBM, CoWoS und Rack, Netzanschluss). Wo kein Fertigungsschritt in der Schleife liegt (Software, Mathematik, Entwurf bis Tapeout), ist ein abrupter Sprung nicht ausgeschlossen.

## Bruchindikator
Generationsabstand deutlich unter einem Jahr: der Entwurf setzt den Takt. Bei etwa einem Jahr bindet die Physik.

## Ablesung
Herstellerangaben, Tier 1b.

## Verknüpft
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [sensing-and-experiment-loop](../mechanisms/sensing-and-experiment-loop.md)
