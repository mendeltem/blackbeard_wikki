---
id: backend-and-base-die-are-separate-capacity
typ: regel
status: getragen
thema: knowledge/memory_supply
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [sk-hynix-fab-footprint-f1, sk-hynix-expansion-approved-vs-announced, cowos-capacity-and-package-area, base-die-shifts-value-to-foundry]
---

# Backend und Logik-Basisdie sind eigene Kapazität; den bindenden Engpass nennen

## Aussage
TSV-Bearbeitung, Stacking, Test und Burn-in sind nicht in der Fab-Waferzahl enthalten und werden getrennt geführt. Ab HBM4 ist der Logik-Basisdie ein zugekaufter Foundry-Chip: Materialaufwand zu Foundry-Marge, eigene Kostenposition und eigener möglicher Engpass.

Bei jeder Kapazitätsrechnung wird der bindende Engpass benannt: Wafer, Backend, CoWoS, Logik-Basisdie oder Netzanschluss. Entlastung eines nicht bindenden Engpasses erhöht den Durchsatz nicht.

## Trägt
Die Pflicht zur getrennten Führung. Gestützt durch das Filing: zwei von drei freigegebenen Projekten von SK Hynix sind Backend, und deren Ausgaben liegen später als die der Wafer-Fab.

## Trägt nicht
Welcher Engpass gerade bindet. Backend-Kapazität in Stacks und Basisdie-Versorgung stehen in keiner zulässigen Quelle.

## Bruchindikator
Keiner. Rechenvorschrift.

## Ablesung
Für die Projektliste SK hynix F-1, Tier 1a. Für den bindenden Engpass derzeit blind.

## Verknüpft
- [sk-hynix-fab-footprint-f1](../findings/sk-hynix-fab-footprint-f1.md)
- [sk-hynix-expansion-approved-vs-announced](../findings/sk-hynix-expansion-approved-vs-announced.md)
- [cowos-capacity-and-package-area](../../compute_bottlenecks/mechanisms/cowos-capacity-and-package-area.md)
- [base-die-shifts-value-to-foundry](../../memory_technology_roadmap/mechanisms/base-die-shifts-value-to-foundry.md)
