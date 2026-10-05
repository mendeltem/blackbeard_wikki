---
id: laya-router-before-agent
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-06
herkunft: Victus, Laya 0.3.28 als Weiche vor Hermes/OpenCode/Claude, 2026-10-05/06
verweist_auf: [lean-hermes-toolsets, minimal-harness-prompt-size, hermes-delegates-to-opencode-locally]
---

# Laya als Weiche vor dem Agenten: 24 von 30 richtig, 0,1 s

## Aussage
Laya (Convai Innovations, Apache 2.0) ist eine offene Alternative zu TypeSafes
Jev: ein Entscheidungsmodell, das keinen Text schreibt, sondern eine Wahl mit
Wahrscheinlichkeit liefert. Getestet als Weiche: Soll eine Anfrage an einen
schlanken Hermes (`trivial`), an OpenCode (`coding`) oder an Claude (`schwer`)?

30 echte Anfragen (18 aus Hermes-Sessions, 12 aus Claude-Code-Sitzungen),
Soll-Labels von Hand:

| Checkpoint | Ziele | richtig | Zeit je Anfrage, CPU |
|---|---|---|---|
| multilingual (322 Mio.) | 3 | **24/30** | 61 ms |
| english (421 Mio.) | 3 | 17/30 | 193 ms |
| multilingual | 4 (trivial geteilt in chat/shell) | 15-16/30 | - |

Fehlerrichtung beim besten Lauf: 3 von 7 schweren Anfragen gingen zu niedrig
(2 an `coding`, 1 an `trivial`). Das ist die teure Richtung: die schwere Frage
landet beim lokalen Modell und bekommt eine plausible, schwache Antwort.

Als **Tool in Hermes** (MCP) bringt Laya keine Zeit: Hermes brauchte 3:17 min,
fast alles Prefill des Hermes-Prompts, bevor Qwen das Tool ueberhaupt aufruft.
Der Gewinn entsteht nur **vor** dem Agenten.

## Traegt
- Weiche vor dem Agenten mit Schwelle: ab p 0,8 entscheidet Laya, darunter wird
  nachgefragt, `schwer` geht immer an das starke Modell.
- Betrieb als Dienst (`laya-serve`, 127.0.0.1): 0,1 s je Entscheidung, rund
  1,6 GB RAM. Ohne Dienst kostet jeder Aufruf rund 6-7 s Modellladen.

## Traegt nicht
- Mehr als drei grobe Ziele. Mit vier fiel die Trefferquote auf die Haelfte.
- Die Konfidenz als Garantie: im Bereich ab 0,8 lagen 10 von 12 richtig, zwei
  Fehler mit 0,96 und 0,97. Bei 30 Faellen ist das eine Tendenz.
- Die englische Variante fuer deutsche Anfragen.

## Bruchindikator
Im Log `frag.log` weicht die Trefferquote bei p >= 0,8 deutlich unter 80 % ab,
oder schwere Anfragen landen dort regelmaessig bei OpenCode.

## Ablesung
Eigene Messung, Laya 0.3.28, PyTorch CPU, `Router.predict` mit einer
`choice`-Frage, Checkpoint explizit gewaehlt. Labels sind eine Einschaetzung,
keine objektive Wahrheit. Beliebtheit des Projekts auffaellig: 5224 Likes bei
11 733 Downloads auf Hugging Face, Repo zwei Wochen alt.

## Verknuepft
- [lean-hermes-toolsets](lean-hermes-toolsets.md)
- [minimal-harness-prompt-size](../open_checks/minimal-harness-prompt-size.md)
- [hermes-delegates-to-opencode-locally](hermes-delegates-to-opencode-locally.md)
