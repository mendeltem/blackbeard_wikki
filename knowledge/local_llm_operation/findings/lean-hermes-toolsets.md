---
id: lean-hermes-toolsets
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-06
herkunft: Victus, Hermes Agent v0.21.5 + Qwen3.6-35B-A3B ueber Ollama, 2026-10-06
verweist_auf: [minimal-harness-prompt-size, prefix-cache-single-slot, laya-router-before-agent]
---

# Schlanker Hermes: halber Prompt mit zwei Werkzeugen

## Aussage
`hermes -z "<frage>" -t terminal,file --ignore-rules` laedt nur die Werkzeuge
Terminal und Dateien und laesst AGENTS.md, SOUL.md, Memory und vorgeladene
Skills weg.

| | Prompt erste Anfrage | Wanduhr |
|---|---|---|
| Hermes voll | rund 13 000 Token | 3:17 min (Laya-Toolaufruf, 3 Modellrunden) |
| Hermes schlank | **5 648 Token** | **37 s** (Dateien zaehlen, 2 Modellrunden) |

Die Antwort des schlanken Laufs war richtig (4 Dateien, Rest Ordner).

## Traegt
Kurze Aufgaben am Rechner: zaehlen, nachsehen, eine Einstellung aendern. Bei
einem Slot (siehe [prefix-cache-single-slot]) zaehlt jeder Token Prompt bei
jedem Cache-Verlust neu.

## Traegt nicht
- Aufgaben, die Regeln, Memory oder Skills brauchen: die fehlen hier bewusst.
- Einen sauberen Zeitvergleich. Die beiden Laeufe hatten verschiedene Aufgaben
  und Rundenzahlen; nur die Prompt-Groesse ist direkt vergleichbar.

## Bruchindikator
Der schlanke Hermes loest Aufgaben falsch, die der volle loest, weil eine
Regel aus AGENTS.md oder SOUL.md fehlt.

## Ablesung
Eigene Messung, `--usage-file` von Hermes (`input_tokens`, `api_calls`).
Teilantwort auf [minimal-harness-prompt-size]: halb so viel Prompt ohne
Harness-Wechsel, aber noch weit ueber den unter 1000 Token von Pi.

## Verknuepft
- [minimal-harness-prompt-size](../open_checks/minimal-harness-prompt-size.md)
- [prefix-cache-single-slot](../mechanisms/prefix-cache-single-slot.md)
- [laya-router-before-agent](laya-router-before-agent.md)
