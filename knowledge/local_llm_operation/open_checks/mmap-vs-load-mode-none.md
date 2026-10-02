---
id: mmap-vs-load-mode-none
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [moe-expert-offloading]
---

# Lademodus bei Expert-Offloading: mmap oder none?

## Aussage
`llama-server` warnt beim Start mit `-ncmoe`:

```
tensor overrides to CPU are used with mmap enabled
 - consider using --load-mode none for better performance
```

Die eigene Doku in `local_models/docs/02-tuning.md` empfiehlt dagegen `mmap`,
begruendet mit SSD-Schonung: Verschleiss entsteht durch Schreiben, nicht durch
Lesen. Unter `-lm none` liegt das Modell in anonymem Speicher und landet bei
RAM-Mangel im Pagefile - echte Schreibvorgaenge.

Beide Seiten haben ein Argument. **Keine der beiden ist gemessen.**

## Traegt
Nichts. Das ist der Punkt des Eintrags.

## Traegt nicht
Die aktuelle Empfehlung `mmap` ist eine Vermutung, kein Befund. Wer sie zitiert,
zitiert eine Vermutung.

## Bruchindikator
entfaellt

## Ablesung
blind

## Zu messen
Beide Modi auf derselben Maschine, gleicher `-ncmoe`, gleicher Prompt:
Prefill und Decode getrennt (siehe [separate-prefill-from-decode]), dazu freier
RAM und Pagefile-Schreibrate waehrend des Laufs. Entscheidend ist der Fall mit
**wenig freiem RAM** - bei viel freiem RAM duerften sich beide Modi kaum
unterscheiden.

Auf Victus waren waehrend des Betriebs 1,5 GB frei, das ist der interessante Fall.

## Verknuepft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
- [separate-prefill-from-decode](../rules/separate-prefill-from-decode.md)
