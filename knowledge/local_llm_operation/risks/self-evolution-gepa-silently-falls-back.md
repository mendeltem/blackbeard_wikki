---
id: self-evolution-gepa-silently-falls-back
typ: risiko
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-06
herkunft: Code-Lektuere NousResearch/hermes-agent-self-evolution, Commit 0a929e3, dspy 3.4.0, 2026-10-05
verweist_auf: []
---

# hermes-agent-self-evolution: GEPA laeuft gar nicht

## Aussage
Das Nous-Repo verspricht, Hermes-Skills per DSPy + GEPA zu verbessern. Im
aktuellen Stand (Commit 0a929e3) passiert etwas anderes:

1. `dspy.GEPA(metric=..., max_steps=iterations)` wirft unter dspy 3.4.0
   `TypeError: unexpected keyword argument 'max_steps'`. Das Skript faengt den
   Fehler ab und nimmt **stumm MIPROv2**. `--optimizer-model` wird nie benutzt,
   weil kein `reflection_lm` uebergeben wird.
2. Die Bewertung `skill_fitness_metric` ist **Wortueberschneidung** zwischen
   Antwort und erwarteter Antwort, kein LLM-Judge, und liefert GEPA kein
   Text-Feedback. Hermes selbst fuehrt dabei keine Werkzeuge aus.

Ein Lauf zeigt also nicht, was GEPA kann, und die Ausgabe sagt es nur in einer
gelben Zeile.

## Traegt
Jede Entscheidung, Geld oder Rechenzeit in einen Lauf zu stecken. Vorher den
Aufruf pruefen: `reflection_lm` und `max_metric_calls` oder `auto` setzen.

## Traegt nicht
Eine Aussage ueber GEPA selbst (ICLR 2026). Das Problem ist die Anbindung.

## Bruchindikator
Ein neuerer Commit im Repo ruft `dspy.GEPA` mit gueltigen Argumenten auf.

## Ablesung
Code gelesen, Aufruf in eigener venv nachgestellt (TypeError reproduziert).
Kein voller Lauf gemacht.

## Verknuepft
- Repo: <https://github.com/NousResearch/hermes-agent-self-evolution>
