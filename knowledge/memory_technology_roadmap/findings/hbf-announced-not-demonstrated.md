---
id: hbf-announced-not-demonstrated
typ: befund
status: vorschlag
thema: knowledge/memory_technology_roadmap
stand: 2026-10-06
herkunft: Projekt SK Hynix, Recherche-Report Speicher-Roadmap nach HBM4E (Stichtag 26.07.2026), eingetragen 2026-10-06
verweist_auf: [roofline-decides-memory-class, sk-hynix-nand-solidigm-turnaround, benchmarks-from-one-hand, announced-is-not-built]
---

# High Bandwidth Flash: angekündigt und simuliert, nicht als Silizium gemessen

## Aussage
HBF stapelt 3D-NAND mit TSV in HBM-ähnlicher Bauform.

| Was | Status |
|---|---|
| SanDisk und SK Hynix (Absichtserklärung 06.08.2025, OCP-Arbeitsgruppe seit 25.02.2026) | Zielwerte Gen1: 512 GB je 16-Die-Stack, 1,6 TB/s Lesen; Samples 2. Hj. 2026, erste Geräte Anfang 2027. Datenblatt und Simulation. |
| SK Hynix "H3" (HBM plus HBF neben einer GPU) | bis 2,69-facher Durchsatz je Watt, Simulation (IEEE Computer Architecture Letters, Februar 2026) |
| Kioxia 5 TB, 64 GB/s (August 2025) | gebaut und gemessen, aber SSD-Bauform mit PCIe, rund ein Fünfundzwanzigstel der Zielbandbreite. Ein anderes Produkt. |

Physik laut SK-Hynix-Papier: langsamerer Zugriff (µs statt ns), geringere Schreibfestigkeit (rund 100.000 Zyklen), bis zum Vierfachen der Leistungsaufnahme von HBM. Geeignet für Daten, die einmal geladen und oft gelesen werden (Gewichte, geteilter Prefix-Cache, kalte MoE-Experten); ungeeignet für den aktiven KV-Cache beim Decode und für Training.

## Trägt
HBF ist, wenn es kommt, eine zusätzliche Stufe zwischen HBM und SSD und ergänzt HBM. Volumen läge im NAND, nicht im DRAM.

## Trägt nicht
Jede Leistungszahl. SanDisks Vergleich "innerhalb von 2,2 % von HBM" unterstellt in der eigenen Fußnote unbegrenzte HBM-Kapazität und misst damit den Kapazitätsvorteil gerade nicht. Standardisierung läuft bei OCP, nicht bei JEDEC.

## Bruchindikator
Unabhängig gemessene Samples (Bandbreite, Latenz, Schreibfestigkeit) oder ein Beschleuniger mit HBF-Platz von Nvidia, AMD oder Google. Bis dahin Option, kein Basisszenario.

## Ablesung
Herstellerdatenblatt und Pressemitteilungen (Tier 1a in der Herkunft, Marketing im Inhalt); IEEE CAL 2026 (peer-reviewed, Simulation; DOI nicht erhoben). Aus dem Projekt-Report übernommen, nicht nachgeprüft.

## Verknüpft
- [roofline-decides-memory-class](../../ai_demand_drivers/mechanisms/roofline-decides-memory-class.md)
- [sk-hynix-nand-solidigm-turnaround](../../memory_earnings/findings/sk-hynix-nand-solidigm-turnaround.md)
- [benchmarks-from-one-hand](../../model_capability_cost/rules/benchmarks-from-one-hand.md)
- [announced-is-not-built](../../compute_bottlenecks/rules/announced-is-not-built.md)
