---
id: foreign-gpu-process-before-measuring
typ: regel
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-04
herkunft: Victus, Einrichtung Hermes + OpenCode, 2026-10-04
verweist_auf: [separate-prefill-from-decode, moe-expert-offloading]
---

# Vor jeder Messung pruefen, wer sonst auf der GPU und im RAM sitzt

## Aussage
Ein vergessener `llama-server` aus einem frueheren Vergleichslauf hielt seit
3,5 Stunden **5 GB von 8 GB VRAM** und eine zweite Kopie des Modells im RAM.
Der Swap war voll (7/7 GB). Ollama bekam 2,4 GB VRAM.

| | Prefill |
|---|---|
| mit fremdem Prozess, OpenCode-Prompt ~11k Token | ~30 t/s, erste Anfrage nach 5 min abgebrochen |
| nach Beenden, 6k-Token-Prompt | 397 t/s |

Faktor 13. Fuer Ollama sah alles normal aus: das Modell lud, es kam keine
Fehlermeldung.

Nicht verwechseln: `ollama ps` zeigt bei Qwen3.6-35B-A3B immer ~98 % CPU. Das
ist das gewollte Expert-Offloading, kein Fehler.

## Traegt
Jede Durchsatzmessung und jede Fehlersuche "warum ist es heute langsam".
Zwei Befehle vorher:

```
nvidia-smi --query-compute-apps=pid,process_name,used_memory --format=csv
free -g
```

Mehr als ein Inferenzprozess auf der GPU oder voller Swap: erst aufraeumen,
dann messen.

## Nachtrag 2026-10-21: nicht jeder grosse VRAM-Halter ist ein Rest
Ein `llama-server`, der 20,4 von 24,6 GiB hielt, war **kein vergessener
Vergleichslauf**, sondern der `enabled`-Dienst des eigenen lokalen Profils
(`llama-server.service`, `Linger=yes`, `--n-gpu-layers 99`,
`--ctx-size 81920`). Er laeuft absichtlich dauerhaft, weil das lokale Profil
ihn als Gehirn fuer Patientendaten braucht. Vor dem "Aufraeumen" also erst
die Herkunft klaeren:

```
systemctl --user is-enabled llama-server.service
ps -o pid,lstart,cmd -p <pid>
```

Ein Prozess aus der eigenen Unit ist kein Fremdkoerper — ihn zu beenden nimmt
dem lokalen Profil die Inferenz weg. Gewuenschte Loesung dort ist nicht
killen, sondern `--sleep-idle-seconds`, siehe
[local-model-server-runs-only-when-needed](local-model-server-runs-only-when-needed.md).


## Traegt nicht
Andere Ursachen fuer langsames Prefill, etwa der Kaltstart nach dem Laden
(erste Decode-Messung 17 t/s, warm 30-35 t/s).

## Bruchindikator
Prefill weit unter dem bekannten Wert, ohne dass sich Modell oder Prompt
geaendert hat.

## Ablesung
Eigene Messung, Ollama 0.35.1. Prefill aus `print_timing` im Ollama-Log und
`prompt_eval_duration` der `/api/generate`-Antwort. Die beiden Zeilen der
Tabelle haben verschiedene Promptlaengen, siehe
[separate-prefill-from-decode](separate-prefill-from-decode.md). Der Faktor ist
deshalb eine Groessenordnung, keine genaue Zahl.

## Verknuepft
- [separate-prefill-from-decode](separate-prefill-from-decode.md)
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
