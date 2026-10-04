---
id: hermes-delegates-to-opencode-locally
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-04
herkunft: Victus, Einrichtung Hermes + OpenCode, 2026-10-04
verweist_auf: [prefix-cache-single-slot, opencode-run-hangs-on-open-stdin, foreign-gpu-process-before-measuring]
---

# Hermes gibt Programmieraufgaben lokal an OpenCode ab: funktioniert, 160 s

## Aussage
Hermes Agent hat eine eingebaute Skill `opencode`, die den OpenCode-CLI per
`opencode run '...'` als Arbeiter aufruft. Beide Agenten laufen gegen dasselbe
Ollama-Modell (`qwen3.6-64k` = Qwen3.6-35B-A3B, `num_ctx 65536`).

Testauftrag an Hermes (`hermes -z`): in `calc.py` die Funktion `mul(a, b)`
ergaenzen und `test_calc.py` mit Tests fuer `add` und `mul` anlegen.

| | Ergebnis |
|---|---|
| Wanduhr gesamt | 160 s |
| Hermes-Aufrufe | 4, 17 848 Input-Token, 48 460 aus dem Cache |
| OpenCode-Sitzung angelegt | ja, eigene Session in `opencode session list` |
| Code korrekt | ja, beide Testfunktionen laufen fehlerfrei |
| Kosten | 0 |

Hermes meldete danach "pytest passed". **pytest war auf dem System nicht
installiert.** Der Code stimmt, die Erfolgsmeldung ist trotzdem nicht belegt.

Zweite Haelfte: zwei Slots, damit sich die beiden Agenten nicht gegenseitig den
Prefix-Cache verdraengen, gibt es nicht. Mit `OLLAMA_NUM_PARALLEL=2` startet
Ollama trotzdem `-np 1` und loggt
`model architecture does not currently support parallel requests architecture=qwen35moe`.

## Traegt
Kleine, abgegrenzte Programmieraufgaben in einem Repo: eine Funktion, Tests
dazu, eine Fehlererklaerung. Alles bleibt auf der Maschine.

## Traegt nicht
- Lange Sitzungen mit vielen Wechseln. Hermes-Prompt rund 13k Token, OpenCode
  rund 11k. Bei einem Slot heisst jeder Wechsel neues Prefill, bei ~400 t/s etwa
  30 s. Geschaetzt, nicht gemessen.
- Groessere Umbauten ueber viele Dateien. Nicht getestet.
- Eine einzelne Aufgabe ist kein Zuverlaessigkeitsmass. Deshalb Status
  `vorschlag`.

## Bruchindikator
- Hermes meldet Testerfolg, ohne dass ein Testlauf im Protokoll steht.
- Eine Ollama-Version, die `qwen35moe` parallel bedient. Dann zwei Slots neu
  messen.

## Ablesung
Eigene Messung. Ollama 0.35.1, Hermes Agent v0.21.5 (upstream 5d3c0597),
OpenCode 1.18.34. Ollama-Override: `OLLAMA_KEEP_ALIVE=24h`,
`OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`. Danach gemessen:
Prefill 397 t/s (6014-Token-Prompt), Decode 30-35 t/s warm.
Zeitstempel aus `hermes -z --usage-file`.

## Verknuepft
- [prefix-cache-single-slot](../mechanisms/prefix-cache-single-slot.md)
- [opencode-run-hangs-on-open-stdin](../risks/opencode-run-hangs-on-open-stdin.md)
- [foreign-gpu-process-before-measuring](../rules/foreign-gpu-process-before-measuring.md)
