---
id: datacenter-gw-and-twh-to-2030
typ: pruefpunkt
status: offen
thema: knowledge/compute_bottlenecks
stand: 2026-10-14
herkunft: Projekt Artificial Intelligence (claude.ai), Gespräch 2026-10-14
verweist_auf: [bottleneck-migration, transformer-lead-times, announced-is-not-built]
---

# Rechenzentrumsleistung und Stromverbrauch bis 2030: Dossier-Zahlen gegen IEA

## Aussage
Das „Strategie-Dossier“ vom 2026-10-14 nennt ohne Quelle:
- installierte Rechenzentrumsleistung 50 bis 55 GW (2025) auf 120 bis 135 GW (2030), also +70 bis 80 GW;
- Zubau von 7 bis 10 GW pro Jahr (2025) auf 18 bis 25 GW pro Jahr (2030);
- Stromverbrauch von ~450 auf knapp 1.000 TWh.

Die Verbrauchszahl deckt sich in der Größenordnung mit dem Basisfall der IEA: 415 TWh im Jahr 2024 (rund 1,5 % des Weltstroms), etwa 945 TWh im Jahr 2030 (IEA, Energy and AI, 2025). Die GW-Zahlen sind nicht belegt.

Plausibilitätsrechnung (Annahme): 945 TWh entsprechen im Jahresmittel 945.000 GWh / 8.760 h ≈ 108 GW Durchschnittslast. Bei 80 % Auslastung der Anschlussleistung wären das ~135 GW installiert, bei 90 % ~120 GW. Die Dossier-Spanne für 2030 ist damit mit dem IEA-Verbrauch vereinbar, aber nicht unabhängig belegt. Sie lässt sich aus ihm zurückrechnen.

## Zu prüfen
1. Eine primäre GW-Quelle finden: IEA-Datentabellen zum Report, Behördendaten (EIA, ERCOT-Anschlussliste, EirGrid) oder Zählungen von Betreibern. Analystenhäuser nur als Hinweis.
2. Klären, ob „Kapazität“ IT-Last oder Netzanschluss meint. Der Faktor PUE (rund 1,1 bis 1,5) verschiebt die GW-Zahl.
3. Die Regel [announced-is-not-built](../rules/announced-is-not-built.md) anwenden: angekündigte Gigawatt-Campusse nicht als installiert zählen.
4. Bei Beleg: als Befund eintragen und den Mechanismus [bottleneck-migration](../mechanisms/bottleneck-migration.md) um die Jahreszubau-Zahl ergänzen.

## Ablesung
IEA, Energy and AI (2025), Executive Summary (zwischenstaatlicher Bericht, kein Filing, behandelt wie Tier 1b): https://www.iea.org/reports/energy-and-ai/executive-summary
GW-Zahlen des Dossiers: blind.

## Verknüpft
- [bottleneck-migration](../mechanisms/bottleneck-migration.md)
- [transformer-lead-times](../mechanisms/transformer-lead-times.md)
- [announced-is-not-built](../rules/announced-is-not-built.md)
