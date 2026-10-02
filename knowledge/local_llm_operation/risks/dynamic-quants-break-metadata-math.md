---
id: dynamic-quants-break-metadata-math
typ: risiko
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [moe-expert-offloading]
---

# Groessen aus Metadaten und nomineller Bitbreite rechnen sich falsch

## Aussage
Der naheliegende Weg, die Groesse der Expert-Gewichte je Layer zu bestimmen -
`expert_count x 3 x embedding x ffn_length x Bits / 8` aus den GGUF-Metadaten -
geht bei modernen Quantisierungen daneben. Dynamische Quants (unsloth "UD",
i-Quants) geben verschiedenen Tensoren **verschiedene** Bitbreiten: Experten
weniger, Attention und Embeddings mehr. Auf Victus lag die Rechnung um Faktor zwei
daneben.

Richtig ist, die **Tensor-Tabelle** im GGUF-Header auszuwerten. Dort steht jeder
Tensor mit Name, Typ und Datei-Offset; die Differenz zweier aufeinanderfolgender
Offsets ist die exakte Groesse - unabhaengig vom Quant-Typ, auch fuer Typen, die
es beim Schreiben dieses Eintrags noch nicht gab.

Gegenprobe: Summe aller Tensoren 17,72 GB gegen 17,73 GB Dateigroesse.

## Traegt
Jede Kapazitaetsrechnung vor dem Laden: passt das Modell, wie viele Layer auf die
GPU, wie viel bleibt im RAM.

## Traegt nicht
Eine Aussage ueber Qualitaet. Dass Experten weniger Bits bekommen, heisst nicht,
dass das Modell schlechter ist - es ist die Absicht des Quantisierers.

## Bruchindikator
Die Summe aller Tensoren weicht deutlich von der Dateigroesse ab. Dann stimmt die
Leseroutine nicht, nicht das Modell.

Zweiter Indikator: eine ggml-Typtabelle im eigenen Code. Sie veraltet mit jedem
neuen Quant-Typ und rechnet dann **still** falsch - genau der erste Fehler, der
hier gemacht wurde.

## Ablesung
Eigene Messung. Erster Versuch mit Typtabelle: Experten 7,75 GiB bei 17,73 GB
Datei. Zweiter Versuch ueber Offsets: 14,12 GiB, Summe stimmt mit der Datei.

## Verknuepft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
