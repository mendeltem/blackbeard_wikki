---
id: hbm-market-share-and-nvidia-allocation
typ: pruefpunkt
status: offen
thema: knowledge/memory_supply
stand: 2026-10-02
herkunft: Gespräch Projekt AI-Lage-Verbund, 2026-10-02
verweist_auf: [hbm-eats-wafer-area, dram-wafer-capacity-by-fab, peer-beat-transfers-weakly]
---

# HBM-Marktanteil und Nvidias HBM4-Allokation

## Aussage
Offener Erhebungsschritt: SK Hynix' HBM-Marktanteil und die Aufteilung von
Nvidias HBM4-Volumen sind marktbestimmend, aber bisher nur über Analysten
belegt, nicht Tier 1a. Zusammengetragener Stand, jede Zeile mit Herkunft und
Tier:

**Marktanteil am HBM-Umsatz** (Analysten, kein Befund):
- 2025 gesamt: SK Hynix rund 63 Prozent. (TrendForce)
- Q2 2025: SK Hynix 62, Micron 21, Samsung 17 Prozent. (Counterpoint via Chosun Biz)
- Q1 2026: SK Hynix rund 56 Prozent, fallend. Micron überholt Samsung auf Platz zwei. (TrendForce)
- Ausblick 2026: Samsung zielt auf rund 38 Prozent zum Jahresende; SK Hynix' Anteil
  schrumpft laut Prognose durch Qualifizierungsverzögerungen und Kapazitätsverschiebungen. (TrendForce)

**Nvidia-HBM4-Qualifizierung** (Firmenaussage über Presse):
- 05.06.2026: Nvidia-CEO Jensen Huang nennt alle drei (SK Hynix, Samsung, Micron)
  für HBM4 der Vera-Rubin-Plattform zertifiziert. Damit ist SK Hynix nicht mehr
  alleiniger qualifizierter HBM4-Lieferant — der Kern des bisherigen Vorsprungs.
- SK Hynix 12-Hi HBM4 in Serie, 16-Hi in Kundenqualifizierung; 48-GB-HBM4E-Muster
  seit 18.06.2026, 16 Gbit/s je Pin, über 20 Prozent effizienter.

**Vorläufige HBM4-Allokation bei Nvidia** (Analysten/Lieferkette, kein Befund):
- SK Hynix mittlere 50 bis rund zwei Drittel, Samsung mittlere 20, Micron rund 20 Prozent.

Kernbefund in einem Satz: SK Hynix führt bei HBM klar, aber der Anteil sinkt von
rund 63 (2025) auf Mitte 50 (Q1 2026), und mit der HBM4-Zertifizierung aller drei
im Juni 2026 wird der Vorsprung bestreitbar.

## Zu prüfen
1. Für jede Anteilszeile eine primärnahe Quelle statt Analystenschätzung finden,
   oder sie als unbelegt markieren. HBM-Marktanteile sind strukturell schwer
   Tier 1a zu belegen, weil kein Hersteller HBM-Umsatz getrennt ausweist.
2. Die Nvidia-Allokationsanteile gegen gemeldete HBM-Umsätze der drei Hersteller
   plausibilisieren, sobald diese vorliegen.
3. Prüfen, ob Samsungs HBM4-Zertifizierung in reale Auslieferung mündet; eine
   Zertifizierung ist kein Liefervertrag und kein Anteil.
4. Anteil gegen die Flächenrechnung aus
   [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md) und die Kapazität
   je Werk aus [dram-wafer-capacity-by-fab](dram-wafer-capacity-by-fab.md) stellen.

## Trägt nicht
Keinen Befund. Alle Anteilszahlen sind TrendForce oder Counterpoint, also
Warnsignal, kein Beleg. Keine Aussage über HBM-Preise oder -Margen je Hersteller.
Die Jensen-Huang-Zertifizierungsaussage ist eine Firmenaussage auf einer
Veranstaltung, über Presse gelesen — näher an primär, aber nicht nachgeprüft.

## Bruchindikator
Ein Hersteller weist HBM-Umsatz getrennt aus, oder Nvidia nennt die Allokation
selbst. Dann ersetzt ein Befund diese Sammlung. Oder SK Hynix' Anteil fällt in
zwei Folgequartalen unter 50 Prozent — dann ist der Vorsprung keine Führung mehr,
sondern ein knapper Vorrang.

## Ablesung
Überwiegend Branchendienste (TrendForce, Counterpoint via Chosun Biz) und
Presseberichte (Astute Group, Yahoo Finance, KED Global), also Warnsignal, kein
Befund. Nvidia-Zertifizierung: Aussage Jensen Huang vom 05.06.2026, über Presse.

## Verknüpft
- [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md)
- [dram-wafer-capacity-by-fab](dram-wafer-capacity-by-fab.md)
- [peer-beat-transfers-weakly](../../memory_earnings/mechanisms/peer-beat-transfers-weakly.md)
