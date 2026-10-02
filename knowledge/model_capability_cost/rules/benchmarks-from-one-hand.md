---
id: benchmarks-from-one-hand
typ: regel
status: getragen
thema: knowledge/model_capability_cost
stand: 2026-10-02
herkunft: Projekt ai_modellkurve, 2026-09-05
verweist_auf: [iso-capability-cost-halving]
---

# Benchmarkreihen nur aus einer Hand

## Aussage
Eine Zeitreihe über Benchmarkwerte mehrerer Modelle darf nur Werte eines einzigen Messers enthalten. Werte aus Modellkarten der Anbieter sind untereinander nicht vergleichbar, weil Gerüst, Zahl der Wiederholungen, Zeitbudget und Werkzeuge abweichen und nicht vollständig berichtet werden. Sie liegen systematisch höher als unabhängige Messungen desselben Modells.
Wer anbietergemeldete und unabhängige Werte in einer Reihe mischt, misst teilweise das Gerüst statt das Modell. Die Reihe sieht dann steiler aus, als sie ist.

## Trägt
Jede Kosten-, Fortschritts- oder Vergleichskurve über Modelle. In Projekt ai_modellkurve stammen alle SWE-bench-Verified- und GPQA-Diamond-Werte ausschließlich aus den eigenen Messläufen von Epoch AI; anbietergemeldete Werte sind bewusst nicht aufgenommen, obwohl sie die Abdeckung erhöht hätten.

## Trägt nicht
Ein Urteil darüber, welcher Wert der richtige ist. Ein höherer Wert mit besserem Gerüst ist nicht falsch — er beantwortet nur eine andere Frage ("was ist mit diesem Modell erreichbar" statt "wie gut ist dieses Modell unter festen Bedingungen").
Die Regel kostet Abdeckung. Bei 90 Modellen lagen Werte vor für SWE-bench Verified bei 29 und GPQA Diamond bei 78. Diese Lücke ist der Preis der Vergleichbarkeit und wird als Lücke ausgewiesen, nicht gefüllt.

## Bruchindikator
keiner, Enthaltsamkeitsregel

## Ablesung
entfällt

## Verknüpft
- [iso-capability-cost-halving](../findings/iso-capability-cost-halving.md)
