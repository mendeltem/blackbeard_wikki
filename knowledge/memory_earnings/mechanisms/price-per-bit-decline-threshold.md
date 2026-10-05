---
id: price-per-bit-decline-threshold
typ: mechanismus
status: vorschlag
thema: knowledge/memory_earnings
stand: 2026-10-06
herkunft: Projekt SK Hynix, Projektnotiz, Herleitung rekonstruiert 2026-10-06
verweist_auf: [wafer-growth-is-not-bit-growth, depreciation-outlasts-capex-cut, low-pe-is-about-the-denominator, demand-is-not-earnings]
---

# Umsatz hält nur, wenn der Preis je Bit langsamer fällt, als die Bits wachsen

## Aussage
    Umsatz = Bits x Preis je Bit
    Umsatz konstant, wenn Preisrückgang d = g / (1 + g) bei Bitwachstum g

| Bitwachstum g | zulässiger Preisrückgang d |
|---|---|
| 7,9 % | 7,3 % |
| 9,9 % | 9,0 % |
| 12,6 % | 11,2 % |
| 20 % | 16,7 % |

Der Preis je Bit ist die dominante Größe: in früheren Jahrzehnten fiel er um 25 bis 30 % im Jahr und fraß das Bitwachstum auf. Mit dem Bitwachstum, das aus dem Verdopplungsziel folgt (7 bis 13 %), hält der Umsatz nur, wenn der Preis je Bit um weniger als rund 7 bis 11 % im Jahr fällt. Bitwachstum allein trägt keinen Gewinn.

## Trägt
Die Schwelle als Identität. Sie verbindet die Mengenrechnung (memory_supply) mit der Ergebnisrechnung.

## Trägt nicht
Die Projektnotiz nennt "rund 11 %" ohne Herleitung; die Tabelle ist eine Rekonstruktion (11,2 % entspricht f = 0,3 und r = 2). Die historischen 25 bis 30 % sind Allgemeinwissen ohne Quelle hier. Gewinn statt Umsatz verlangt zusätzlich die Kostenkurve je Bit.

## Bruchindikator
Realisierter ASP je Bit fällt über vier Quartale schneller als d bei gemeldetem Bit-Growth.

## Ablesung
ASP- und Bit-Veränderung Q/Q im IR-Deck von SK Hynix, Tier 1a.

## Verknüpft
- [wafer-growth-is-not-bit-growth](../../memory_supply/mechanisms/wafer-growth-is-not-bit-growth.md)
- [depreciation-outlasts-capex-cut](depreciation-outlasts-capex-cut.md)
- [low-pe-is-about-the-denominator](../rules/low-pe-is-about-the-denominator.md)
- [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)
