---
id: allocation-beats-datasheet
typ: mechanismus
status: vorschlag
thema: knowledge/compute_bottlenecks
stand: 2026-10-03
herkunft: Gespräch Projekt AI_news, These Mendel, 2026-10-03
verweist_auf: [cowos-capacity-and-package-area, bottleneck-migration, bandwidth-bottleneck, induced-innovation, refresh-instead-of-new-build, financing-limit, gpu-memory-absorbs-fab-additions, custom-asics-use-hbm]
---

# Zuteilung schlägt Datenblatt

## Aussage
These (Mendel, 2026-10-03): Das größte Problem von AMD und Broadcom ist nicht die Technik, sondern die Zuteilung knapper Fertigungskapazität gegen Nvidia. Weil Strom knapp ist, wollen alle Käufer die leistungsstärkste Generation je Watt. Die ist durch Packaging und HBM begrenzt. Wer die Zuteilung hält, verkauft alles, was er bauen kann.

    Strom knapp → Leistung je Watt entscheidet → Nachfrage auf die neueste Generation
    → neueste Generation begrenzt durch CoWoS und HBM4
    → Absatz folgt der Zuteilung, nicht dem Datenblatt

Stand der Zuteilung 2026 (Analysten, kein Befund): TSMC-CoWoS gesamt rund 1,0 Mio. Wafer Nachfrage im Jahr, Kapazität Ende 2026 120.000 bis 140.000 Wafer je Monat, ausgebucht. Nvidia über 50 Prozent (800.000 bis 850.000 Wafer im Jahr, über 70 Prozent bei CoWoS-L), AMD rund 11 Prozent. Broadcom baut Kundenchips (Google TPU, Meta u. a.) auf denselben Linien und mit HBM. HBM4 für Rubin: SK Hynix 60 bis 70 Prozent, Samsung 20 bis 30 Prozent. Samsung soll Hauptlieferant für AMD MI455X werden, Qualifizierung offen.

Beispiel Datenblatt gegen Menge: AMD MI455X (H2 2026) liegt auf dem Papier bei FP4 40 PF, FP8 20 PF, 432 GB HBM4, 23,3 TB/s und damit gleichauf oder vor Rubin (35 PF FP4 dicht, 288 GB). Gemessen ist MI455X noch nicht. Mengen: AMD Data Center Q2 2026 6,7 Mrd. USD inklusive EPYC (10-Q), Ausblick Konzern Q3 rund 13 Mrd. USD; Nvidia Data Center Q2 GJ2027 89,0 Mrd. USD, Rubin allein im Q3 rund 20 Mrd. USD. Zusätzliches Risiko für AMD: MI455X auf TSMC N2, Rubin auf N3.

## Trägt
- Warum ein Wettbewerber mit besserem Datenblatt kurzfristig wenig Anteil gewinnt: Stromknappheit verstärkt den Vorteil dessen, der die Zuteilung hält, statt ihn auszugleichen. Das folgt aus den Axiomen [Bandbreiten-Engpass](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md) und [induzierte Innovation](../../ai_demand_drivers/mechanisms/induced-innovation.md).
- Wer nicht die neueste Nvidia-Generation bekommt, kauft, was verfügbar ist. AMD und ältere Generationen füllen die Lücke der Zuteilung.
- Für Speicher ist die Verteilung zwischen Nvidia, AMD und Broadcom nahezu gleichgültig: alle verbauen HBM, AMD je GPU sogar mehr (432 gegen 288 GB). Ein Anteilsgewinn von AMD erhöht eher den HBM-Bedarf, siehe [gpu-memory-absorbs-fab-additions](../../memory_supply/mechanisms/gpu-memory-absorbs-fab-additions.md).
- Stromknappheit verkürzt den Austauschtakt ([refresh-instead-of-new-build](../../ai_demand_drivers/mechanisms/refresh-instead-of-new-build.md)): alte Racks fliegen früher raus, weil jedes MW mit der neuesten Generation mehr leistet.

## Trägt nicht
- "Fortschrittlichste" ist nicht automatisch Nvidia. Hyperscaler optimieren auf Token je MW für die eigene Last; TPU und Trainium sind je Chip schwächer, können je Token aber günstiger sein. Daher die Broadcom-Aufträge.
- "Immer das Neueste" gilt, solange Strom der bindende Engpass ist. Wird Kapital bindend ([financing-limit](../../ai_demand_drivers/mechanisms/financing-limit.md)), kippt die Optimierung von Leistung je Watt zu Leistung je Dollar.
- Die Zuteilung ist nicht fest. Neue CoWoS-Linien (18 bis 24 Monate Vorlauf) und eine Samsung-HBM4-Freigabe können AMD 2027 mehr Menge geben.

## Bruchindikator
- AMD oder Broadcom melden für 2027 eine deutlich höhere CoWoS-Zuteilung, oder TSMC nennt eine Verschiebung der Anteile.
- AMD-Data-Center-GPU-Umsatz wächst über mehrere Quartale schneller als Nvidias, ohne dass Nvidia Lieferprobleme meldet.
- Käufer installieren in stromknappen Regionen bewusst ältere oder billigere Generationen in großem Umfang.

## Zu prüfen
1. CoWoS-Anteile Nvidia, AMD, Broadcom 2026 und 2027 aus TSMC-Calls oder Herstellerangaben statt Analysten.
2. AMD-Data-Center-Umsatz in GPU und CPU aufteilen (Segmentangaben, Calls).
3. Samsung-HBM4-Freigabe für MI455X und tatsächliche Auslieferung.
4. Erste unabhängige Messung von MI455X (MLPerf) gegen Rubin je GPU.

## Ablesung
Umsätze AMD und Nvidia: 10-Q und 8-K, Tier 1a, über Suchauszüge gelesen. CoWoS- und HBM-Anteile: Silicon Analysts, Cortex Advisory, KGI (Analysten), kein Befund. MI455X-Spezifikation: Herstellerangabe über Presse, Tier 1b. Konvention dicht/Sparsity bei AMDs 40 PF nicht sicher geklärt.

## Verknüpft
- [cowos-capacity-and-package-area](cowos-capacity-and-package-area.md)
- [bottleneck-migration](bottleneck-migration.md)
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
- [induced-innovation](../../ai_demand_drivers/mechanisms/induced-innovation.md)
- [refresh-instead-of-new-build](../../ai_demand_drivers/mechanisms/refresh-instead-of-new-build.md)
- [financing-limit](../../ai_demand_drivers/mechanisms/financing-limit.md)
- [gpu-memory-absorbs-fab-additions](../../memory_supply/mechanisms/gpu-memory-absorbs-fab-additions.md)
- [custom-asics-use-hbm](../../ai_demand_drivers/findings/custom-asics-use-hbm.md)
