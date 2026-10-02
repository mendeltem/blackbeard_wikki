---
id: refresh-instead-of-new-build
typ: mechanismus
status: getragen
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Gespräch Projekt SK Hynix, 2026-10-02
verweist_auf: [hbm-gb-per-mw, induced-innovation, lead-times-datacenter-vs-fab]
---

# Refresh statt Neubau

## Aussage
Alte GPUs werden im Bestand ausgetauscht, dafür braucht es keinen neuen Netzanschluss.

    HBM-Nachfrage aus Refresh = installierte MW / Refresh-Takt × GB je MW der neuen Generation

Stromknappheit bremst den Neubau und verkürzt den Refresh-Takt. Sie verlagert die Nachfrage, statt sie zu löschen.

## Trägt
HBM-Nachfrage auch bei null Neubau, wenn GB je MW über die Generationen steigt.

## Trägt nicht
Drop-in bei älteren luftgekühlten Hallen. Bedingung ist die Leistungsreserve je Baujahrgang (Setzung Frontlastiger Capex).

## Bruchindikator
GB je MW fällt über die Generationen, oder die Rackleistung der Folgegeneration übersteigt die ausgelegte Reserve.

## Ablesung
Herstellerspezifikationen, Tier 1b. Auslegungsangaben der Betreiber, Tier 1a.

## Verknüpft
- [hbm-gb-per-mw](../open_checks/hbm-gb-per-mw.md)
- [induced-innovation](../mechanisms/induced-innovation.md)
- [lead-times-datacenter-vs-fab](../mechanisms/lead-times-datacenter-vs-fab.md)
