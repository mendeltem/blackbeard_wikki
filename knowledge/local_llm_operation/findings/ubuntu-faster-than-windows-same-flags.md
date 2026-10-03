---
id: ubuntu-faster-than-windows-same-flags
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-03
herkunft: Claude-Code-Sitzung auf Victus, 2026-10-03
verweist_auf: [moe-expert-offloading, separate-prefill-from-decode]
---

# Unter Ubuntu laeuft dasselbe Modell mit denselben Flags gut 50 Prozent schneller als unter Windows 10

## Aussage
Victus wurde von Windows 10 auf Ubuntu 26.04 umgestellt. Gleiches Modell
(Qwen3.6-35B-A3B UD-IQ4_XS, 17,73 GB), gleiche Flags wie im Windows-Startskript
(`-ngl 99 -ncmoe 34 -c 16384 -t 8 -fa on -np 1 -lm mmap`), gleiche Messart
(`timings` aus `/v1/chat/completions`, Thinking aus):

| | Windows 10, b10603 | Ubuntu 26.04, b11379 |
|---|---|---|
| Decode, kurzer Prompt | 19,4 t/s | 29,5 t/s |
| Decode nach 15k Prompt | - | 28,1 t/s |
| Prefill, langer Prompt | 180-306 t/s | 500 t/s (15k Token) |

`llama-bench` bestaetigt das: tg128 30,9 t/s, pp4096 510 t/s.

Auf Ubuntu haengt das Display an der AMD-iGPU; die RTX 4070 belegt im Leerlauf
62 MiB. `-ncmoe 30` passt damit ebenfalls (6,6 GB VRAM bei Bench-Kontext), bringt
aber nur Prefill +8 %, Decode unveraendert. `-ncmoe 26` scheitert an cudaMalloc.

## Traegt
Fuer Expert-Offloading auf Victus Linux bevorzugen. Der Gewinn ist gross genug,
dass er die Wahl zwischen den Systemen entscheidet, wenn das Modell lokal laufen soll.

## Traegt nicht
Die Zuordnung allein zum Betriebssystem. Zwischen den Messungen liegen auch
sechs Wochen llama.cpp-Entwicklung (b10603 -> b11379). Fuer b10603 gibt es keinen
Linux-CUDA-Build, ein Gegentest mit gleicher Version ist so nicht moeglich.
Ebenso wenig traegt die Vermutung, IQ4_XS sei auf der CPU der Bremser: dieselbe
Datei ist unter Ubuntu nicht langsamer als Ollamas eigenes Quant.

## Bruchindikator
Ein Windows-Lauf mit b11379 (oder neuer) und denselben Flags, der in die Naehe von
29 t/s kommt. Dann war es die Version, nicht das System.

## Ablesung
Eigene Messung, llama.cpp b11379 (`llama-b11379-bin-ubuntu-cuda-13.4-x64`),
Treiber 595.91. Windows-Werte aus [moe-expert-offloading](../mechanisms/moe-expert-offloading.md).
Rohdaten: `~/hermes-bench` auf Victus.

## Verknuepft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
- [separate-prefill-from-decode](../rules/separate-prefill-from-decode.md)
