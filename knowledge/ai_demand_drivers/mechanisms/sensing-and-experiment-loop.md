---
id: sensing-and-experiment-loop
typ: mechanismus
status: getragen
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Gespräch Projekt SK Hynix, 2026-10-02
verweist_auf: [open-search-space, simulation-needs-compute, cadence-and-yield-trough]
---

# Mess- und Experimentierkreislauf (Sensoren und Aktoren)

## Aussage
Hardware wird billiger und lässt sich kleiner wie größer bauen. Billigere Hardware → mehr Sensoren und Aktoren → mehr Messdaten und Experimente → bessere Simulation und Forschung → bessere Hardware. Der Kreislauf ist der Mechanismus, über den Offener Suchraum wirkt.

## Trägt
Sensoren liefern die Bodenwahrheit für Simulation. Aktoren (automatisierte Labore, Roboter) verkürzen den Experimentierschritt. Speicherseitig zuerst LPDDR und NAND am Rand und eSSD für die Daten, also die Segmente DRAM konventionell und NAND mit Solidigm.

## Trägt nicht
Fertigung im großen Maßstab und Zulassungen werden nicht schneller. Den HBM-Aufpreis stützt der Kreislauf nur mittelbar, über Training und Simulation auf den Daten.

## Bruchindikator
keiner

## Ablesung
Stückzahlen und Preise der Sensoren: Herstellerberichte, Tier 1a. Speicher je Roboter oder Edge-Gerät: Spezifikationen, Tier 1b. Anteil der Daten, der ins Training fließt: blind.

## Verknüpft
- [open-search-space](../axioms/open-search-space.md)
- [simulation-needs-compute](../mechanisms/simulation-needs-compute.md)
- [cadence-and-yield-trough](../mechanisms/cadence-and-yield-trough.md)
