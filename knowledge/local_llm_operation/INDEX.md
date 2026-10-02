# local_llm_operation

Betrieb eines lokalen Sprachmodells auf eigener Hardware: was auf eine zu kleine
Karte passt, wie man es misst, und woran kleine Modelle zuverlaessig scheitern.

Alle Zahlen stammen von **Victus** (RTX 4070 Laptop 8 GB, Ryzen 7 7840HS,
31,3 GB RAM, Qwen3.6-35B-A3B UD-IQ4_XS, llama.cpp b10603). Nicht auf andere
Maschinen uebertragbar ohne Nachmessen.

| Typ | Eintrag | Inhalt |
|---|---|---|
| mechanismus | [moe-expert-offloading](mechanisms/moe-expert-offloading.md) | `-ngl` plus `-ncmoe`: ein 35-B-Modell auf 8 GB VRAM, 19,4 t/s |
| mechanismus | [prefix-cache-single-slot](mechanisms/prefix-cache-single-slot.md) | `-np 1`, und warum Prompt-Kompaktierung den Cache zerstoert |
| befund | [rule-lists-make-small-models-refuse](findings/rule-lists-make-small-models-refuse.md) | Eskalationsliste im System-Prompt: 0 auf 100 Prozent nach dem Entfernen |
| befund | [counting-needs-thinking](findings/counting-needs-thinking.md) | Laengen und Anzahlen brauchen Thinking, Kosten Faktor 20 |
| befund | [vendor-sampling-params-no-gain](findings/vendor-sampling-params-no-gain.md) | Sampling-Empfehlung der Modellkarte: 15/15 gegen 15/15 |
| risiko | [dynamic-quants-break-metadata-math](risks/dynamic-quants-break-metadata-math.md) | Groessenrechnung aus Metadaten liegt um Faktor zwei daneben |
| regel | [separate-prefill-from-decode](rules/separate-prefill-from-decode.md) | Durchsatz nie ueber die Wanduhr: 0,4 gegen 27,4 t/s |
| pruefpunkt | [mmap-vs-load-mode-none](open_checks/mmap-vs-load-mode-none.md) | Lademodus bei Expert-Offloading, ungemessen |

## Werkzeuge dazu

Die Werkzeuge liegen im Projekt-Repo, nicht hier - Pfade und Messwerte stehen
dort beieinander:
<https://github.com/mendeltem/local_models>

- `tools/detect.py` - rechnet `-ncmoe` aus GGUF-Tensor-Tabelle und freiem VRAM
- `tools/lok.py` - CLI fuer kleine Aufgaben, Batch-Modus, Eskalation per Exit-Code
- `docs/03-model-wiki.md` - welche Aufgabe mit welchen Einstellungen
