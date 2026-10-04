---
id: dense-27b-vs-moe-on-8gb
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-10-04
herkunft: Video Sam Witteveen "Which is The Best Qwen3.8-27B?", 2026-10-04
verweist_auf: [moe-expert-offloading, reasoning-effort-for-routine-agent-tasks]
---

# Weniger Denken bei einem dichten 27B: schneller als das MoE auf 8 GB?

## Aussage
Drei Fine-Tunes von Qwen3.8-27B sollen bei fast gleicher Genauigkeit weniger
Denk-Token erzeugen. Die Zahlen stammen von den Herstellern, berichtet im Video:

| Modell | Versprechen | Lizenz |
|---|---|---|
| ThinkingCap (BottleCapAI) | 37 % weniger Token ueber 12 Benchmarks, Genauigkeit 86,6 auf 85,8 | klein-gewerblich und privat |
| Swift 1.5 (UkisAI) | bis 58,5 % weniger; LiveCodeBench 77 auf 81,7 % bei 11 200 auf 8 400 Token | eigene, frei bis 1 Mio. $ Umsatz |
| QwenPi | fuer den Pi-Harness; medium so gut wie Basis-xhigh auf Terminal Bench, 41 % weniger Output | Apache 2 |

Fuer Victus zaehlt etwas anderes: **Qwen3.8-27B ist dicht.** Pro Token wirken
alle 27 Mrd. Parameter, beim jetzigen Qwen3.6-35B-A3B etwa 3 Mrd. Expert-Offloading
greift bei einem dichten Modell nicht.

Eigene Schaetzung, nicht gemessen: Q4 rund 16 GB, davon passen etwa 6,5 GB ins
VRAM. Die restlichen rund 10 GB muessen je Token aus dem RAM gelesen werden. Bei
rund 60 GB/s ergibt das **5-8 t/s Decode**, gegen gemessene 30-35 t/s beim MoE.
Auch 58 % weniger Denk-Token holen einen Faktor 4-6 nicht ein.

Dazu kommt der Speicher: 16 GB neben den 22 GB des MoE-Modells passen nicht in
30 GB RAM. Ein Wechsel heisst jedes Mal neu laden.

## Traegt
Nichts. Die Tabelle ist Herstellerangabe aus zweiter Hand, die Geschwindigkeit
ist eine Rechnung.

## Traegt nicht
Die Annahme "weniger Denken = schneller" laesst sich nicht von einer RTX Pro
6000 mit 96 GB (Testmaschine im Video) auf 8 GB uebertragen. Dort ist das
Modell decode-gebunden im VRAM, hier im RAM.

## Bruchindikator
Ein gemessener Decode ueber 15 t/s fuer ein dichtes 27B auf Victus. Dann ist
die Rechnung oben falsch und der Vergleich offen.

## Ablesung
Video von Sam Witteveen, 2026-10-04, Kapitel 6-8, Testmaschine Dell Pro Max mit
RTX Pro 6000, vLLM. Einzelbeobachtung aus den Kommentaren, nicht pruefbar: auf
einem MacBook M5 mit 32 GB loeste Qwen3.6-35B-A3B eine HTML/JS-Aufgabe in 2:44
min, Qwen3.8-27B in 4:30 min, ein erster Anlauf des 27B lief 10 min in einer
Schleife.

## Zu messen
Swift 1.5 als GGUF (Q4) auf Victus, gleicher Prompt wie beim MoE: Prefill und
Decode getrennt (siehe [separate-prefill-from-decode]), dazu Denk-Token und
Wanduhr bis zur fertigen Antwort. Swift, weil es als einziges GGUFs fuer kleine
GPUs anbietet. Vorher das MoE-Modell entladen.

## Verknuepft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
- [reasoning-effort-for-routine-agent-tasks](reasoning-effort-for-routine-agent-tasks.md)
- [separate-prefill-from-decode](../rules/separate-prefill-from-decode.md)
