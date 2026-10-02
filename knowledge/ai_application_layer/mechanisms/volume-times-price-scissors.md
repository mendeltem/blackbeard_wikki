---
id: volume-times-price-scissors
typ: mechanismus
status: vorschlag
thema: knowledge/ai_application_layer
stand: 2026-10-02
herkunft: Projekt ki-anwendungsschicht, Gespräch 2026-09-05 bis 2026-10-02
verweist_auf: [open-search-space, demand-is-not-earnings, distillation-substitutes-compute, concentration-decides-margin]
---

# Schere aus Menge und Preis

## Aussage
Die Tokenmenge kann sich vervielfachen, während das Produkt aus Menge und Preis stillsteht. Google meldete 480 Billionen Token im Monat (Mai 2025, I/O), 980 (Juli 2025, Quartalsgespräch), 1.300 (Oktober 2025): Menge mal 2,71. Bewertet mit dem jeweils niedrigsten geltenden Listenpreis eines Spitzenmodells über alle Anbieter (DeepSeek-V3 1,10 Dollar je Million Ausgabetoken, ab 29.09.2025 V3.2-Exp 0,42 Dollar): Produkt 528 → 1.078 → 546 Millionen Dollar, Faktor 1,03. Mit dem Flaggschiff-Listenpreis (10 Dollar) gerechnet: Faktor 2,71. Zwei Preisreihen, dieselben Mengen, entgegengesetzte Aussage. Eine einzige Preissenkung eines einzigen Anbieters hat die gesamte Mengensteigerung aufgezehrt.

Preisregel: Preis zu einem Stichtag ist der niedrigste an diesem Tag geltende Listenpreis der Reihe über alle Anbieter, je Anbieter sein jüngster. Den zuletzt angekündigten Preis irgendeines Anbieters zu nehmen, ließe die Reihenfolge der Ankündigungen über das Ergebnis entscheiden.

## Trägt
Dass Mengenwachstum allein die Umsatzthese der Angebotsseite nicht trägt. Ergänzt den Jevons-Falsifikator in [Offener Suchraum](../../ai_demand_drivers/axioms/open-search-space.md): Dort Tokenwachstum gegen Effizienzrate, hier Tokenwachstum gegen Preisverfall. Mengen verschiedener Einheiten (je Tag, je Monat, je Quartal, je Minute) werden nie ineinander umgerechnet und nie in einer Linie gezeichnet.

## Trägt nicht
Erzielte Preise. Listenpreis ist nicht Erlös (Mengenrabatte, Zwischenspeicherung, Jahresverträge, nicht veröffentlicht). Das Produkt ist ein Rechenwert, keine Umsatzgröße; der weit überwiegende Teil der Google-Token wird kostenlos verbraucht. Agentenläufe sind die Gegenthese: Wächst die Menge je zahlendem Nutzer schneller, als der Preis fällt, steigt das Produkt trotzdem. Wird die Agentenlast aber überwiegend von kleinen Modellen auf gewöhnlicher Hardware bedient, verschärft sie die Schere statt sie zu schließen.

## Bruchindikator
Produkt aus Menge und erzieltem Preis steigt vier Halbjahre in Folge, während der günstigste Spitzenpreis weiter fällt: Nachfrage ist preiselastisch, jede Senkung ein Umsatztreiber.

## Ablesung
Mengen: Unternehmensangaben (Google I/O, Alphabet-Quartalsgespräch; Tier 1a nur das Gespräch). Preise: Preislisten der Anbieter, Tier 1b. Erzielter Preis: blind. Unabhängige Mengenquelle: Durchsatzstatistik von OpenRouter, misst eine Plattform, keine Wirtschaft.

## Verknüpft
- [open-search-space](../../ai_demand_drivers/axioms/open-search-space.md)
- [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)
- [distillation-substitutes-compute](distillation-substitutes-compute.md)
- [concentration-decides-margin](../../china_industrial_strategy/mechanisms/concentration-decides-margin.md)
