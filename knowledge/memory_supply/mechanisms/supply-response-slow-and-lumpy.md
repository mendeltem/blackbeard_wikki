---
id: supply-response-slow-and-lumpy
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-06
herkunft: Projekt SK Hynix, Projektnotizen und Recherche-Report vom 26.07.2026, eingetragen 2026-10-06
verweist_auf: [capex-discipline-after-2023, fab-lead-time-examples, no-standard-cycle-without-absorption-check, depreciation-outlasts-capex-cut, no-cycle-date]
---

# Angebotsantwort ist langsam und klumpig, der Zyklus entsteht auf der Angebotsseite

## Aussage
Zwei Aussagen, die zusammengehören:

1. Der Speicherzyklus entsteht auf der Angebotsseite, durch gleichzeitige Kapazitätsentscheidungen weniger Anbieter, nicht durch schwankende Nachfrage. Glattere KI-Nachfrage hebt den Zyklus deshalb nicht auf.
2. Die kurzfristige Angebotsantwort ist träge: bei SK Hynix kein neuer DRAM-Reinraum vor Yongin Fab 1 (Q1 2027, Installation danach), EUV-Lieferungen bis Dezember 2027 gebunden. Zusatzkapazität kommt in Blöcken.

Dazu ein behaupteter Strukturbruch: die Kosten je Bit fallen nicht mehr um rund 30 % im Jahr, weil die 1T1C-Zelle an die Skalierungsgrenze stößt. Angebot ließe sich dann nicht mehr über billige Shrinks fluten, nur über Greenfield.

## Trägt
Träge Antwort heute und Klumpenrisiko später sind dieselbe Eigenschaft: was jetzt die Knappheit verlängert, landet 2027 bis 2030 in Blöcken.

## Trägt nicht
- Die im Projekt notierte kurzfristige Angebotselastizität von 0,11 bis 0,18: Herkunft nicht dokumentiert, Annahme.
- Den Strukturbruch bei den Kosten je Bit: Quelle ist eine Fachanalyse (SemiAnalysis), also Warnsignal, unzulässige Quelle. Tier 1b wäre eine Dichte- oder Kostenreihe aus IEDM- oder VLSI-Papieren.
- Einen Zeitpunkt (Setzung no-cycle-date).

## Bruchindikator
Ein Hersteller meldet einen Node mit deutlichem Bit-je-Wafer-Sprung im Volumen früher als geplant, oder 3D-DRAM geht vor 2029 in Serie (siehe three-d-dram-binary-reordering).

## Ablesung
Reinraum- und EUV-Termine: SK hynix F-1, Tier 1a. Elastizität und Kostenkurve: blind.

## Verknüpft
- [capex-discipline-after-2023](capex-discipline-after-2023.md)
- [fab-lead-time-examples](../findings/fab-lead-time-examples.md)
- [no-standard-cycle-without-absorption-check](../rules/no-standard-cycle-without-absorption-check.md)
- [depreciation-outlasts-capex-cut](../../memory_earnings/mechanisms/depreciation-outlasts-capex-cut.md)
- [no-cycle-date](../axioms/no-cycle-date.md)
