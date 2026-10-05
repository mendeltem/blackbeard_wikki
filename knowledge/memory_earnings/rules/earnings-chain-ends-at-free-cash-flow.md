---
id: earnings-chain-ends-at-free-cash-flow
typ: regel
status: getragen
thema: knowledge/memory_earnings
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [sk-hynix-free-cash-flow-2024-h1-2026, sk-hynix-q2-2026-oneoff-and-tax, stacked-yield-is-decomposed, contract-stability, sk-hynix-shareholder-return-policy]
---

# Die Rechenkette endet beim freien Cashflow, nicht beim operativen Ergebnis

## Aussage
    Umsatz = Bits x ASP                (je Produktklasse getrennt)
    OP     = Umsatz x Marge            (je Segment, nicht konsolidiert geraten)
    FCF    = OP - Barsteuern + Abschreibung - Capex - Delta Working Capital

Drei Punkte sind nicht optional:
1. In der Ausbauphase liegt der Capex über der Abschreibung. Der FCF ist strukturell kleiner als der OP, und die Lücke schließt sich erst, wenn das Capex-Wachstum endet.
2. Erhaltene Anzahlungen aus LTAs sind Working-Capital-Quelle. Dieselbe Zahl ist Bilanzdeckungstest und FCF-Treiber und wird an beiden Stellen aus derselben Quelle gespeist.
3. Die Barsteuerquote ist eine Annahme. Die effektive Steuerquote aus der GuV ist nicht die Barsteuerquote, besonders wenn latente Steuern auf unrealisierte Bewertungsgewinne sie verzerren.

Jede Eingangsgröße ist belegt, als Annahme markiert oder verweist auf eine Setzung. Kundennachfrage wird über installierte Leistung (MW) und Refresh-Takt modelliert, nicht über den Capex-Betrag der Kunden. Der Kostenanteil des Speichers am Systempreis wird gerechnet, weil er den ASP-Spielraum setzt.

## Trägt
Die Form jeder Ergebnisaussage. Die Ausschüttung von SK Hynix hängt am FCF, also an dieser Kette.

## Trägt nicht
Werte. Für Q2 2026 abgeleitet 23,5 % effektive Steuerquote; als Barsteuerquote nicht verwendbar.

## Bruchindikator
Keiner. Rechenvorschrift.

## Ablesung
Kapitalflussrechnung und Anhang, Tier 1a.

## Verknüpft
- [sk-hynix-free-cash-flow-2024-h1-2026](../findings/sk-hynix-free-cash-flow-2024-h1-2026.md)
- [sk-hynix-q2-2026-oneoff-and-tax](../findings/sk-hynix-q2-2026-oneoff-and-tax.md)
- [stacked-yield-is-decomposed](../../memory_supply/rules/stacked-yield-is-decomposed.md)
- [contract-stability](../axioms/contract-stability.md)
- [sk-hynix-shareholder-return-policy](../findings/sk-hynix-shareholder-return-policy.md)
