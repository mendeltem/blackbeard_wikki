---
id: only-hbm4-is-jedec-standard
typ: befund
status: vorschlag
thema: knowledge/memory_technology_roadmap
stand: 2026-10-06
herkunft: Projekt SK Hynix, Recherche-Report Speicher-Roadmap nach HBM4E (Stichtag 26.07.2026), eingetragen 2026-10-06
verweist_auf: [yield-trough, benchmarks-from-one-hand, hybrid-bonding-forced-by-stack-height]
---

# Nur HBM4 ist standardisiert, alles ab HBM5 ist Projektion

## Aussage
| Generation | Status | Eckwerte |
|---|---|---|
| HBM4 | JEDEC JESD270-4 (April 2025, aktualisiert Dez. 2025); Package SPHBM4 JESD330-4 (Juni 2026) | 2048 Bit, 8 GT/s, bis 2 TB/s je Stack, 32 Kanäle |
| HBM4E | kein einheitlicher JEDEC-Standard, Herstellerangaben | bis 12,8 GT/s, rund 3 TB/s, bis 64 GB, bis 80 W, rund 2027 |
| HBM5 | JEDEC "active project" (JC-42), keine Zielwerte | Projektion: 4096 I/O, 4 TB/s, 80 GB, 100 bis 120 W, 2029 |
| HBM6 | nur Projektion | 8 TB/s, 96 bis 120 GB, Cu-Cu-Bonding, rund 2032 |
| HBM7, HBM8 | nur Projektion | 24 und 64 TB/s, rund 2035 und 2038 |

Die Werte ab HBM5 stammen aus einer akademischen Roadmap (KAIST TERALAB, HBM Roadmap Ver 1.7, Juni 2025) und aus Konferenzfolien der Hersteller. Thermik wird in diesen Projektionen ab HBM5 zur bindenden Größe (75 W bei HBM4 auf 160 W bei HBM7).

## Trägt
Die Regel, HBM5 und später nie als Spezifikation zu zitieren.

## Trägt nicht
Jahreszahlen und Zielwerte ab HBM5. Statuswechsel erst mit einem JEDEC-Dokument für HBM5.

## Bruchindikator
JEDEC veröffentlicht einen HBM5-Standard.

## Ablesung
JEDEC-Dokumentnummern, Tier 1b; aus dem Projekt-Report übernommen, bei JEDEC nicht nachgeprüft. KAIST-Roadmap: akademische Projektion, kein Herstellercommitment.

## Verknüpft
- [yield-trough](../../memory_supply/axioms/yield-trough.md)
- [benchmarks-from-one-hand](../../model_capability_cost/rules/benchmarks-from-one-hand.md)
- [hybrid-bonding-forced-by-stack-height](../mechanisms/hybrid-bonding-forced-by-stack-height.md)
