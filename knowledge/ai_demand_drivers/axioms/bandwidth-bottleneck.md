---
id: bandwidth-bottleneck
typ: axiom
status: getragen
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Gespräch Projekt SK Hynix, 2026-10-02
verweist_auf: [induced-innovation, cadence-and-yield-trough, simulation-needs-compute]
---

# Bandbreiten-Engpass (Von-Neumann-Bottleneck)

## Aussage
Speicherbandbreite begrenzt den Durchsatz der Beschleuniger. Unter Strom- und Flächenknappheit kaufen Käufer das Teil mit dem höchsten Durchsatz, die Nachfrage konzentriert sich auf die neueste HBM-Generation.

## Trägt
Nachfrage nach Bandbreitenspeicher (HBM), hergeleitet über das Roofline-Modell.

## Trägt nicht
DRAM allgemein. Wandert Inferenz auf kapazitätsdominierten Speicher, bleibt die Bitnachfrage hoch, der Waferverbrauch je Bit sinkt aber.

## Bruchindikator
Inferenzlast wandert messbar auf SOCAMM, LPDDR oder DDR5-RDIMM.

## Ablesung
Produktkommentare SK Hynix und Micron, Tier 1a. Speicherkonfiguration in Herstellerspezifikationen, Tier 1b.

## Verknüpft
- [induced-innovation](../mechanisms/induced-innovation.md)
- [cadence-and-yield-trough](../mechanisms/cadence-and-yield-trough.md)
- [simulation-needs-compute](../mechanisms/simulation-needs-compute.md)
