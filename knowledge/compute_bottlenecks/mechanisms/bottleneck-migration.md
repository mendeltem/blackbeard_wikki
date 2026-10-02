---
id: bottleneck-migration
typ: mechanismus
status: vorschlag
thema: knowledge/compute_bottlenecks
stand: 2026-10-02
herkunft: Projekt Artificial Intelligence (KI-Compute-Stack), Report Behind-the-Meter and Bridge Power (Juli 2026), eingetragen 2026-10-02
verweist_auf: [hbm-gb-per-mw-three-generations, lead-times-datacenter-vs-fab, gas-turbine-order-backlog, cowos-capacity-and-package-area, announced-is-not-built]
---

# Der bindende Engpass wandert

## Aussage
Der Ausbau von KI-Rechenleistung hängt am jeweils knappsten Glied. Laut Projekt-Reports wanderte es von der GPU-Zuteilung (2023 bis 2024) über Packaging (CoWoS) und Netzanschluss (2024 bis 2025) zur Lieferkette für Turbinen, Generatoren und Transformatoren (ab 2025). Wird ein Glied entlastet, bindet das nächste.

## Trägt
Schließt an den Befund hbm-gb-per-mw-three-generations an: Wenn zusätzliche HBM-Bits zusätzliche Megawatt brauchen, entscheiden die Glieder der Stromkette über die verbaubare Menge. Die Reihenfolge der Prüfung: Für die Menge an Speicher, die in einem Jahr verbaut werden kann, zählt das engste Glied, nicht die Speicherkapazität allein.

## Trägt nicht
Dass Speicher nie bindet. Auch keine Datierung der Übergänge, die Jahreszahlen sind Lesart des Reports.

## Bruchindikator
Ausgelieferte Beschleuniger liegen über zwei Quartale unbenutzt auf Lager, weil Strom fehlt (Strom bindet), oder Rechenzentren stehen mit Strom und ohne Beschleuniger (Chips oder Speicher binden).

## Ablesung
Betreiber- und Herstellerkommentar in Calls, Tier 1a, uneinheitlich. Zahlen aus dem Projekt-Report übernommen, gegen die Primärquelle nicht nachgeprüft.

## Verknüpft
- [hbm-gb-per-mw-three-generations](../../ai_demand_drivers/findings/hbm-gb-per-mw-three-generations.md)
- [lead-times-datacenter-vs-fab](../../ai_demand_drivers/mechanisms/lead-times-datacenter-vs-fab.md)
- [gas-turbine-order-backlog](../findings/gas-turbine-order-backlog.md)
- [cowos-capacity-and-package-area](cowos-capacity-and-package-area.md)
- [announced-is-not-built](../rules/announced-is-not-built.md)
