---
id: separate-prefill-from-decode
typ: regel
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [moe-expert-offloading]
---

# Prefill und Decode getrennt messen, nie ueber die Wanduhr

## Aussage
Wer `completion_tokens / Gesamtdauer` rechnet, misst Prefill, Decode und
HTTP-Overhead in einer Zahl. Bei kurzen Antworten dominiert der Overhead.

Gemessen: dieselbe Anfrage meldete **0,4 t/s** nach Wanduhr, waehrend der Server
im selben Moment mit **27,4 t/s** dekodierte. Ein Faktor 68 zwischen Messfehler
und Wirklichkeit.

`llama-server` liefert beides getrennt im Feld `timings`:
`prompt_per_second` und `predicted_per_second`.

Zweite Haelfte der Regel: eine einzelne Prefill-Zahl ist ebenfalls irrefuehrend.
Innerhalb einer Sitzung gemessen: 6,1 / 25,7 / 90,2 / 243,3 t/s - abhaengig davon,
wie viele Modellseiten schon im RAM liegen und wie lang der Prompt ist. Kurze
Prompts sehen dabei **langsamer** aus als lange, weil der feste Aufwand je Anfrage
sich auf wenige Token verteilt.

## Traegt
Jede Durchsatzangabe zu einem lokalen Modell. Ohne Trennung ist sie nicht
vergleichbar - auch nicht mit sich selbst von gestern.

## Traegt nicht
Die Frage, wie lange ein Nutzer wartet. Dafuer ist die Wanduhr genau richtig -
sie darf nur nicht Durchsatz heissen.

## Bruchindikator
Eine Durchsatzzahl ohne Angabe von Promptlaenge und Waermezustand.

## Ablesung
Eigene Messung, llama.cpp b10603, Feld `timings` der
OpenAI-kompatiblen Antwort gegen eigene Wanduhrmessung.

## Verknuepft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
