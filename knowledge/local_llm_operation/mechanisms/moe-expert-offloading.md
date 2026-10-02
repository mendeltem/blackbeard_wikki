---
id: moe-expert-offloading
typ: mechanismus
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [dynamic-quants-break-metadata-math, prefix-cache-single-slot]
---

# Ein MoE-Modell laeuft auf einer GPU, auf die es nicht passt

## Aussage
Ein dichtes Modell muss fuer jedes Token alle Gewichte lesen, ein Mixture-of-Experts
nur die aktiven. Damit laesst sich ein 35-B-Modell mit 3 B aktiven Parametern auf
einer 8-GB-Karte interaktiv betreiben: `-ngl 99` legt Attention, Embeddings und
KV-Cache ins VRAM, `-ncmoe N` laesst die Expert-Gewichte der ersten N Layer im RAM
und rechnet sie auf der CPU. Beides arbeitet gleichzeitig.

Gemessen auf Victus (RTX 4070 Laptop, 8 GB; Qwen3.6-35B-A3B UD-IQ4_XS, 40 Layer):

| | `-ncmoe 99` (alles CPU) | `-ncmoe 34` (6 Layer GPU) |
|---|---|---|
| VRAM | 5132 MiB | 6733 MiB |
| Decode | 15,9 t/s | 19,4 t/s |
| Prefill, warm | 160 t/s | 180-306 t/s |

## Traegt
Dass sich die Modellgroesse von der Kartengroesse entkoppeln laesst, solange das
Modell MoE ist. Die Richtung der Abwaegung: jeder Expert-Layer, der auf die GPU
wandert, bringt ein paar Prozent.

## Traegt nicht
Ein dichtes Modell. Dort gilt nichts davon - ein dichtes 27 B blieb auf derselben
Karte bei etwa 4 t/s.
Auch kein Argument fuer grossen Kontext: der Prefill laeuft CPU-seitig und ist
compute-bound, ein 16k-Prompt kostet rund eine Minute.

## Bruchindikator
Decode-Rate faellt unter die Rate bei `-ncmoe 99`. Dann ist nicht die Aufteilung
schuld, sondern RAM-Mangel - Modellseiten werden verdraengt und von SSD neu
gelesen. Erster gemessener Prefill auf Victus: 6 t/s statt 243.

## Ablesung
Eigene Messung, Tier 1b-aequivalent: llama.cpp b10603, CUDA 13.3, `/v1/chat/completions`
mit `timings`. Nicht uebertragbar auf andere Karten ohne Nachmessen.

## Verknuepft
- [dynamic-quants-break-metadata-math](../risks/dynamic-quants-break-metadata-math.md)
- [prefix-cache-single-slot](../mechanisms/prefix-cache-single-slot.md)
