---
id: datacenter-beats-workstation-per-token
typ: mechanismus
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-14
herkunft: Projekt Artificial Intelligence (claude.ai), Gespräch 2026-10-14, Einwand Mendel
verweist_auf: [bandwidth-bottleneck, hbm-bypass-architectures, distillation-substitutes-compute, every-sector-grows-sum-counts]
---

# Rechenzentrum schlägt Workstation pro Token um eine Größenordnung

## Aussage
Beim Erzeugen von Tokens wird je Schritt das ganze Modell aus dem Speicher gelesen. Eine Workstation tut das für eine Anfrage, ein Rechenzentrum bündelt viele Anfragen in einem Schritt. Überschlag (Speicherbandbreite geteilt durch Modellgröße, Herstellerangaben gerundet):

- Workstation, RTX 5090 (~1,8 TB/s, ~575 W), 8B-Modell FP8 (8 GB), eine Anfrage: ~225 Token/s, **~2,5 J je Token**.
- Rechenzentrum, B200 (~8 TB/s, ~1.000 W), 70B-Modell FP8 (70 GB), 64 Anfragen gebündelt: ~114 Schritte/s × 64 = ~7.300 Token/s, **~0,14 J je Token**.

Lokal kostet also grob das 20-Fache an Strom je Token, und das mit einem fast zehnmal kleineren Modell. Neue Use Cases landen deshalb im Rechenzentrum, nicht auf lokalen Geräten.

## Trägt
Dass Effizienzdruck die Last ins Rechenzentrum zieht, nicht hinaus. Die Bündelung braucht ihrerseits Speicher: Der Zwischenspeicher (KV-Cache) wächst mit Anzahl gleichzeitiger Anfragen mal Kontextlänge; lange Agentenkontexte verlangen Kapazität und Bandbreite, also HBM. Damit stützt der Mechanismus das Axiom bandwidth-bottleneck.

## Trägt nicht
Die Aufteilung innerhalb des Rechenzentrums. Dort kann ein Teil auf andere Speicher wandern (Prefill auf GDDR7 bei Rubin CPX, SRAM-Chips für kleine Modelle), siehe hbm-bypass-architectures. Auch keine Aussage zu Leerlauf, Kühlung und Netz (PUE) im Rechenzentrum; die ändern den Faktor, nicht die Größenordnung. Lokale Geräte bleiben eigene Speichernachfrage (LPDDR), nur nicht für die großen Lasten.

## Bruchindikator
Ein lokales Gerät erreicht bei gleichem Modell weniger als das Doppelte der Joule je Token eines gebündelten Rechenzentrumsbetriebs.

## Ablesung
Eigene Rechnung aus Herstellerangaben (Tier 1b, gerundet, nicht gegen Datenblätter nachgelesen). Messwerte: MLPerf Inference Power, nicht ausgewertet.

## Verknüpft
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [hbm-bypass-architectures](../risks/hbm-bypass-architectures.md)
- [distillation-substitutes-compute](../../ai_application_layer/mechanisms/distillation-substitutes-compute.md)
- [every-sector-grows-sum-counts](every-sector-grows-sum-counts.md)
