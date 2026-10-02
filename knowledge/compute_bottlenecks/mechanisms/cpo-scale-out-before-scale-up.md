---
id: cpo-scale-out-before-scale-up
typ: mechanismus
status: vorschlag
thema: knowledge/compute_bottlenecks
stand: 2026-10-02
herkunft: Projekt Artificial Intelligence (KI-Compute-Stack), Report Co-Packaged Optics through 2030 (Mai 2026), eingetragen 2026-10-02
verweist_auf: [bottleneck-migration, bandwidth-bottleneck]
---

# Optik im Package: erst zwischen Racks, dann im Rack

## Aussage
Co-Packaged Optics ersetzt steckbare Module zuerst in den Switches zwischen den Racks (Scale-out, ab 2025 und 2026). Die Verbindung zwischen Beschleunigern im Rack (Scale-up, NVLink) bleibt länger Kupfer, weil dort Latenz und Ausfallrate ein bis zwei Größenordnungen härter gefordert sind. Der Report nennt für NVIDIA 9 W je Port bei CPO gegen rund 30 W steckbar und optisches Scale-up frühestens mit der Generation Feynman (2028), nicht produktbestätigt.

## Trägt
Reihenfolge der Einführung und damit, wo Optik-Umsätze zuerst anfallen.

## Trägt nicht
Optische Anbindung von HBM. Der Report sieht sie vor 2030 nur als Demonstrator. Auch kein Ende steckbarer Module.

## Bruchindikator
Ein Hersteller liefert optisches Scale-up in Serie vor 2028, oder CPO-Switches fallen im Feld mit höheren Ausfallraten auf als steckbare Module.

## Ablesung
Produktankündigungen von NVIDIA, Broadcom, TSMC, Tier 1b. Zeitplan nach 2026 teils aus Trade Press. Zahlen aus dem Projekt-Report übernommen, gegen die Primärquelle nicht nachgeprüft.

## Verknüpft
- [bottleneck-migration](bottleneck-migration.md)
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
