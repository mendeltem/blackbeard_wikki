---
id: stacked-yield-is-decomposed
typ: regel
status: getragen
thema: knowledge/memory_supply
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [yield-trough, hbm-eats-wafer-area, wafer-growth-is-not-bit-growth]
---

# Yield gestapelter Produkte wird zerlegt, nie gemittelt

## Aussage
Rechenkette für jede Mengenaussage:

    Bits = Wafer/Monat x 12 x Dies/Wafer x Kapazität/Die x Yield

Yield ist eine Funktion von (Generation, kumulierte Ausbringung), nie eine Konstante und nie eine Funktion der Kalenderzeit allein. Bei gestapelten Produkten wird er zerlegt in Die-Yield, Rate bekannter guter Dies und Stapelausbeute. Die Stapelausbeute wirkt über die Stapelhöhe multiplikativ: bei Ausbeute p je Bondschritt und n Lagen grob p^(n-1). Deshalb 12-Hi und 16-Hi getrennt rechnen.

Kapazität ist nicht fungibel: Waferkapazität, Node-Mix und Bitausbringung sind drei Größen. Node-Konversion verbraucht während der Umstellung Kapazität. Wafer-Allokation getrennt ausweisen nach DRAM konventionell, HBM Vorgängergeneration, HBM aktuelle Generation, NAND.

## Trägt
Die Form der Rechnung. Beispiel für die Wirkung: p = 0,99 ergibt 0,895 bei 12-Hi und 0,860 bei 16-Hi; p = 0,97 ergibt 0,715 und 0,633.

## Trägt nicht
Werte für p. Das Beispiel ist Arithmetik, keine Messung. Eine einzige gemittelte HBM-Yieldzahl ist unzulässig, weil sie den Generationseffekt verdeckt.

## Bruchindikator
Keiner. Rechenvorschrift.

## Ablesung
Keine Quelle nötig; Eingangsgrößen je Generation aus Konferenzpapieren und Herstellerangaben, Tier 1b.

## Verknüpft
- [yield-trough](../axioms/yield-trough.md)
- [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md)
- [wafer-growth-is-not-bit-growth](../mechanisms/wafer-growth-is-not-bit-growth.md)
