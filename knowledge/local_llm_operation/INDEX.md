# local_llm_operation

Betrieb eines lokalen Sprachmodells auf eigener Hardware: was auf eine zu kleine
Karte passt, wie man es misst, und woran kleine Modelle zuverlaessig scheitern.

Alle Zahlen stammen von **Victus** (RTX 4070 Laptop 8 GB, Ryzen 7 7840HS,
31,3 GB RAM, Qwen3.6-35B-A3B). Bis 2026-08-29 unter Windows 10 mit UD-IQ4_XS und
llama.cpp b10603; ab 2026-10-03 unter Ubuntu 26.04 mit llama.cpp b11379 und Ollama.
Nicht auf andere Maschinen uebertragbar ohne Nachmessen.

| Typ | Eintrag | Inhalt |
|---|---|---|
| mechanismus | [moe-expert-offloading](mechanisms/moe-expert-offloading.md) | `-ngl` plus `-ncmoe`: ein 35-B-Modell auf 8 GB VRAM, 19,4 t/s |
| mechanismus | [prefix-cache-single-slot](mechanisms/prefix-cache-single-slot.md) | `-np 1`, und warum Prompt-Kompaktierung den Cache zerstoert |
| befund | [rule-lists-make-small-models-refuse](findings/rule-lists-make-small-models-refuse.md) | Eskalationsliste im System-Prompt: 0 auf 100 Prozent nach dem Entfernen |
| befund | [ubuntu-faster-than-windows-same-flags](findings/ubuntu-faster-than-windows-same-flags.md) | Gleiche Flags, Ubuntu statt Windows 10: Decode 19,4 auf 29,5 t/s, Prefill 500 t/s |
| befund | [needle-recall-holds-to-125k](findings/needle-recall-holds-to-125k.md) | 20/20 Needle-Treffer bis 125k Token, Prefill flach bei 330-400 t/s |
| befund | [hermes-agent-local-qwen-benchmark](findings/hermes-agent-local-qwen-benchmark.md) | Hermes Agent + Qwen3.6 lokal: 14 Aufgaben inhaltlich geloest, Schwaechen Format und Rueckfrage |
| befund | [counting-needs-thinking](findings/counting-needs-thinking.md) | Laengen und Anzahlen brauchen Thinking, Kosten Faktor 20 |
| befund | [vendor-sampling-params-no-gain](findings/vendor-sampling-params-no-gain.md) | Sampling-Empfehlung der Modellkarte: 15/15 gegen 15/15 |
| risiko | [dynamic-quants-break-metadata-math](risks/dynamic-quants-break-metadata-math.md) | Groessenrechnung aus Metadaten liegt um Faktor zwei daneben |
| risiko | [ollama-silently-truncates-context](risks/ollama-silently-truncates-context.md) | Prompt ueber `num_ctx`: Ollama behaelt stumm 32k vom Ende, Modell nennt den Koeder |
| regel | [separate-prefill-from-decode](rules/separate-prefill-from-decode.md) | Durchsatz nie ueber die Wanduhr: 0,4 gegen 27,4 t/s |
| pruefpunkt | [mmap-vs-load-mode-none](open_checks/mmap-vs-load-mode-none.md) | Lademodus bei Expert-Offloading, ungemessen |

## Werkzeuge dazu

Die Werkzeuge liegen im Projekt-Repo, nicht hier - Pfade und Messwerte stehen
dort beieinander:
<https://github.com/mendeltem/local_models>

- `tools/detect.py` - rechnet `-ncmoe` aus GGUF-Tensor-Tabelle und freiem VRAM
- `tools/lok.py` - CLI fuer kleine Aufgaben, Batch-Modus, Eskalation per Exit-Code
- `docs/03-model-wiki.md` - welche Aufgabe mit welchen Einstellungen
