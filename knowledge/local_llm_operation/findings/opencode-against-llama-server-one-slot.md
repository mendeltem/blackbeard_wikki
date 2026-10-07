---
id: opencode-against-llama-server-one-slot
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-07
herkunft: Alita (RTX A5000 24 GB), Installation und Rauchtest 2026-10-07 20:10
verweist_auf: [hermes-delegates-to-opencode-locally]
---

# OpenCode laeuft gegen llama-server ueber eine Konfigdatei; mit einem Slot wartet es hinter dem Agenten

## Aussage
OpenCode 1.18.35 (npm `opencode-ai`, Node 22, ohne sudo) spricht einen lokalen llama-server
ueber den Anbieter `@ai-sdk/openai-compatible` an. Noetig ist nur `~/.config/opencode/opencode.json`
mit `provider.<name>.options.baseURL = http://127.0.0.1:8000/v1`, der Modell-ID genau wie in
`/v1/models` des Servers, und `limit.context` passend zur `--ctx-size`. Kein API-Schluessel.
Rauchtest `opencode run --model llamacpp/<id> "Antworte nur mit BEREIT"`: 25 s, richtig.

Fallstrick: llama-server mit `--parallel 1` hat EINEN Slot. Laeuft dort ein Agent (Hermes-Auftrag),
steht OpenCode in der Warteschlange und sieht aus wie haengend -- der erste Rauchtest lief in
einen 300-s-Timeout, ohne Fehler im OpenCode-Log, weil der Slot belegt war. Erst `curl /slots`
(`is_processing`) zeigt den Grund. Zweiter Versuch bei freiem Slot: 25 s.

Beim Start versucht OpenCode den Modellkatalog models.dev zu laden; ohne oder mit langsamem
Internet steht ein `Failed to fetch models.dev` im Log. Lokaler Betrieb ist davon unberuehrt.

## Traegt
Jeder OpenAI-kompatible lokale Server (llama-server, Ollama) mit OpenCode als Arbeiter, auch
als zweiter Anbieter fuer einen Testserver auf anderem Port.

## Traegt nicht
Parallelbetrieb mit einem Agenten auf demselben Ein-Slot-Server: beide verdraengen sich den
Prefix-Cache, und die Wartezeit addiert sich; dafuer `--parallel 2` mit halbem Kontext je Slot
oder ein zweiter Server.

## Bruchindikator
Eine OpenCode-Version, die den Anbieter ohne `npm`-Feld oder mit anderem Schema erwartet
(Schema: https://opencode.ai/config.json).

## Ablesung
Eigene Installation und Messung auf Alita, 2026-10-07. Tier 1a.

## Verknuepft
- [hermes-delegates-to-opencode-locally](hermes-delegates-to-opencode-locally.md)
