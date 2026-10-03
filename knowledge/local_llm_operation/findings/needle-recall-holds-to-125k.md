---
id: needle-recall-holds-to-125k
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-03
herkunft: Claude-Code-Sitzung auf Victus, 2026-10-03
verweist_auf: [ollama-silently-truncates-context, moe-expert-offloading]
---

# Qwen3.6-35B-A3B findet eine Einzelangabe bis 125k Token, und der Prefill bleibt fast flach

## Aussage
Needle-in-a-Haystack auf Victus (Ubuntu, Ollama, `qwen3.6:35b`): ein Code in
deutschem Fuelltext, bei 10 % und 50 % Tiefe, dazu ein Koeder-Code bei 90 %.
Alle 20 Laeufe innerhalb des Kontextfensters richtig (64k- und 128k-Fenster zusammen), keiner fiel auf den Koeder herein.

| echte Token | Treffer | Prefill | Dauer |
|---|---|---|---|
| 2,6k | 2/2 | 330-365 t/s | 8 s |
| 20k | 2/2 | 397 t/s | 52 s |
| 40k | 2/2 | 388-395 t/s | 105 s |
| 63k | 4/4 | 360-387 t/s | 165-203 s |
| 100k | 2/2 | 348-353 t/s | 285 s |
| 125k | 2/2 | 329-334 t/s | 380 s |

Mit `num_ctx 131072` lag der RAM-Bedarf des Gesamtsystems bei hoechstens 10 GB
belegt (20,8 GB verfuegbar), VRAM 7,0 GB. Decode faellt mit dem Kontext von
~30 auf ~15 t/s.

## Traegt
`num_ctx 131072` ist auf Victus tragbar. Langer Kontext ist eine Frage der
Wartezeit (rund 6 Minuten fuer 125k beim ersten Lesen), nicht der Trefferquote.
Das widerspricht dem Satz in [moe-expert-offloading](../mechanisms/moe-expert-offloading.md),
grosser Kontext lohne nicht: unter Ubuntu kostet ein 16k-Prompt rund 40 s statt einer Minute.

## Traegt nicht
Verstaendnis ueber lange Texte. Einen markierten Satz wiederzufinden ist die
leichteste Aufgabe mit langem Kontext; Zusammenhaenge ueber viele Stellen sind
nicht geprueft.

## Bruchindikator
Ein Fehltreffer innerhalb des Fensters, oder Prefill unter 200 t/s bei langen
Prompts (dann verdraengt RAM-Mangel die Modellseiten).

## Ablesung
Eigene Messung, Ollama, `/api/generate`, Temperatur 0, Thinking aus. Skript
`context_test.py` in `~/hermes-bench` auf Victus.

## Verknuepft
- [ollama-silently-truncates-context](../risks/ollama-silently-truncates-context.md)
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
