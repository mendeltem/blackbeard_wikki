---
id: supply-gap
typ: axiom
status: getragen
thema: knowledge/memory_supply
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [bandwidth-bottleneck, yield-trough, supply-response-slow-and-lumpy, micron-customer-deposits-jump]
---

# Angebotslücke

## Aussage
Das Angebot bleibt hinter der HBM-Nachfrage zurück. Bit-Angebot < Bit-Nachfrage ist Ausgangszustand des Modells, nicht Ergebnis, und gilt als Zustand bis zum Bruchindikator, nicht bis zu einem Datum. Die Trägheit der Angebotsantwort wird über den Optionswert des Wartens begründet, nicht über Kapazitätsmangel allein.

## Trägt
Preissetzungsmacht im Basisszenario, als gesetzt zu kennzeichnen.

## Trägt nicht
Einen Befund. Industrieweites HBM-Bit-Angebot gegen HBM-Bit-Nachfrage und industrieweite HBM-Contract-Preise sind bei zulässigen Quellen nicht ablesbar; diese Größen gibt es nur bei ausgeschlossenen Anbietern.

## Bruchindikator
- Primär: der von SK Hynix selbst berichtete realisierte DRAM-ASP (Veränderung Q/Q im IR-Deck) fällt zwei Quartale in Folge bei positivem Bit-Growth.
- Sekundär: Microns HBM-Umsatz je berichteter Bit-Einheit fällt zwei Quartale in Folge.

Beobachtbarkeitsverlust: der Ersatzindikator mischt HBM und konventionelles DRAM und reagiert träger. Ein nicht ausgelöster Indikator ist schwächere Entwarnung als ein HBM-eigener Preisindikator und ist bei jeder Ausgabe so zu kennzeichnen.

## Ablesung
SK Hynix IR-Deck und Micron-Berichte, Tier 1a. Wörtlich aus dem Projektprompt verdichtet; Setzung von Mendel. Der dort genannte Bruchmechanismus "Bruch von unten" steht im Thesenregister, das hier nicht vorliegt.

## Verknüpft
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
- [yield-trough](yield-trough.md)
- [supply-response-slow-and-lumpy](../mechanisms/supply-response-slow-and-lumpy.md)
- [micron-customer-deposits-jump](../../memory_earnings/findings/micron-customer-deposits-jump.md)
