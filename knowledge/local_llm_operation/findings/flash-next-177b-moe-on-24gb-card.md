---
id: flash-next-177b-moe-on-24gb-card
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-07
herkunft: Alita (RTX A5000 24 GB, 62 GB RAM, 24 Kerne, NVMe), acht Messlaeufe 2026-10-07 19:49 bis 21:15, llama.cpp 448147d
verweist_auf: [opencode-against-llama-server-one-slot]
---

# Ein 177B-MoE (Qwen3.8-Flash-Next GSQ-RCO) laeuft auf einer 24-GB-Karte: Experten im RAM, n-Gramm-Tabelle auf der Platte

## Aussage
ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (512 Experten je Schicht, 10 aktiv, 48 Schichten,
Architektur qwen4exp, zwei Shards: Gewichte 37,6 bis 54,8 GB plus 28,8 GB n-Gramm-Tabelle,
die bei allen vier Varianten dieselbe Datei ist) laeuft mit einem aktuellen llama.cpp
(Build vom 2026-10-07; der Build vom 24.08. kennt die Architektur nicht) auf einer 24-GB-Karte
mit 62 GB RAM, wenn man `--n-cpu-moe N --load-mode mmap --lazy-mode on` setzt: die Experten der
ersten N Schichten bleiben im RAM, die Tabelle wird je Token von der NVMe nachgeschlagen.
Alle acht Laeufe beantworteten sechs Pruefragen (Rechnen, Zaehlen, Regex, Uhrzeit, Sortieren,
JSON) 6/6 richtig; Unterschiede in der Qualitaet sind damit nicht aufgeloest, dafuer gelten die
Benchmarks der Modellkarte (Task-Mittel Q2_0 89,1 / IQ2_XS 89,2 / IQ3_XXS 92,6 / IQ3_S 93,3).
Kontext 16k, ein Slot, 20 Threads, Prompt von 5 677 Token.

| Variante | Experten | VRAM | RSS / Seitencache | Laden | Prompt tok/s | Erzeugung tok/s |
|---|---|---|---|---|---|---|
| IQ2_XS | alle 48 Schichten CPU | 5,6 GB | 31 / 30 GB | 20 s | 228 | 15,1 |
| Q2_0 | alle CPU | 5,5 GB | 31 / 31 GB | 21 s | 251 | 10,7 |
| IQ3_XXS | alle CPU | 6,4 GB | 30 / 31 GB | 15 s | 127 | 12,5 |
| IQ3_S | alle CPU | 6,7 GB | 30 / 32 GB | 30 s | 135 | 11,7 |
| IQ2_XS | 16 Schichten GPU | 17,2 GB | 25 / 29 GB | 21 s | 349 | 20,5 |
| Q2_0 | 16 Schichten GPU | 16,3 GB | 23 / 31 GB | 15 s | 345 | 13,9 |
| IQ3_XXS | 16 Schichten GPU | 22,1 GB | 29 / 30 GB | 25 s | 349 | 20,1 |
| IQ3_S | 16 Schichten GPU | 23,6 GB | 30 / 32 GB | 30 s | 251 | 23,3 |

Drei Befunde darin:
1. **Kurze Prompts taeuschen.** Bei 50 bis 70 Token lagen die Prompt-Raten bei 3 bis 38 tok/s,
   beim 5 677-Token-Prompt bei 127 bis 349 tok/s. Die Tabelle muss je Token nachgeschlagen
   werden; das dominiert bei kleinen Stapeln. Tempo nur mit langem Prompt messen.
2. **Q2_0 ist auf der Karte NICHT schneller.** Die Modellkarte verspricht 3,4-fachen
   Prompt-Durchsatz gegen IQ2_XS; das gilt fuer den CPU-Pfad (251 gegen 228) und nicht fuer die
   CUDA-Kerne (13,9 gegen 20,5 tok/s Erzeugung). Mit Experten auf der Karte ist IQ2_XS die
   schnellere 2-Bit-Variante.
3. **RAM ist der Engpass, nicht VRAM.** RSS plus Seitencache liegen bei allen Laeufen bei
   rund 60 GB, also am Rand der 62 GB. Neben einem Training (18 GB RAM) bleibt nur die
   39-GB-Variante IQ2_XS rechnerisch resident; IQ3_XXS (47 GB) und IQ3_S (55 GB) wuerden
   seitenweise von der Platte nachladen. Zwei Flash-Next parallel passen nicht.

Zum Vergleich der 27B-Dense-Server derselben Maschine: ~30 tok/s Erzeugung, 80k Kontext, 21 GB VRAM.

## Traegt
Karten mit 16 bis 24 GB und 64 GB RAM; MoE-GGUFs mit per_layer_token_embd; die Flaggen
sind llama.cpp-Standard ab Oktober 2026.

## Traegt nicht
Rechner mit 32 GB RAM (kein Experten-Shard passt); Erzeugungslast, bei der 15 bis 23 tok/s
zu langsam sind; Kontexte ueber 16k sind ungemessen (bei Experten auf der CPU bleiben
18 GB VRAM fuer den KV-Cache, bei 16 Schichten auf der Karte fast nichts).

## Bruchindikator
Ein llama.cpp-Build, der Q2_0-CUDA-Kerne beschleunigt (dann Punkt 2 neu messen), oder
ein Lauf, bei dem RSS plus Seitencache deutlich unter 60 GB bleibt (dann ist die
RAM-Rechnung in Punkt 3 zu pessimistisch).

## Ablesung
Eigene Messung, Skripte `system/werkzeuge/flashnext-test.sh` und `flashnext-quality.py`
(Alita), Ergebnisse `ergebnisse/flashnext-<Variante>-cmoe<N>.json`. Tier 1a.
Modellkarte: https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF (Herstellerangabe, Tier 1b).

## Verknuepft
- [opencode-against-llama-server-one-slot](opencode-against-llama-server-one-slot.md)
