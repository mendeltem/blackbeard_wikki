---
id: break-indicator-needs-a-reading
typ: regel
status: getragen
thema: knowledge/analysis_method
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [data-tuple-decides-admissibility, supply-gap, contract-stability]
---

# Ein Bruchindikator ohne Ablesung ist eine Absichtserklärung

## Aussage
Jede Setzung und jede These führt einen Bruchindikator mit Schwellenwert und die Angabe, aus welcher zulässigen Quelle er abgelesen wird. Gibt es keine solche Quelle, wird der Indikator ersetzt oder als "blind" gekennzeichnet.

Folgen:
- Ein Ersatzindikator, der unschärfer ist als der eigentliche (etwa gemischter DRAM-ASP statt HBM-Preis), liefert schwächere Entwarnung. Das wird bei jeder Ergebnisausgabe mitgeführt.
- "Nicht ausgelöst" und "blind" sind verschiedene Zustände. Ein blinder Indikator sagt nichts.
- Setzungen werden bei jeder Ausgabe als Setzungen gekennzeichnet. Der ungünstige Pfad (P10) ist der, auf dem mindestens eine Setzung bricht.
- Indikatoren mit zwei Quartalen in Folge als Schwelle bestätigen; sie warnen nicht früh. Wo möglich einen vorlaufenden und einen nachlaufenden Indikator trennen.

## Trägt
Die Mindestform eines prüfbaren Eintrags. Entspricht dem Abschnitt Ablesung der Wiki-Vorlage.

## Trägt nicht
Dass ablesbare Indikatoren die richtigen sind. Ablesbarkeit ist notwendig, nicht hinreichend.

## Bruchindikator
Keiner. Verfahrensregel.

## Ablesung
Keine.

## Verknüpft
- [data-tuple-decides-admissibility](data-tuple-decides-admissibility.md)
- [supply-gap](../../memory_supply/axioms/supply-gap.md)
- [contract-stability](../../memory_earnings/axioms/contract-stability.md)
