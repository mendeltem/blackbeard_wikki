---
id: decider-4b-matches-knn-on-60-routing-cases
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-08
herkunft: Alita, decider-4b v2.1 Q4_K_M auf CPU (llama-cpp-python 0.3.36, 16 Threads) gegen bge-m3-kNN, 60 Routing-Faelle aus local_models tools/laya/faelle/route.jsonl, 2026-10-08
verweist_auf: [decision-model-as-profile-orchestrator, laya-router-before-agent, lean-hermes-toolsets]
---

# decider-4b trifft auf 60 Routing-Faellen so oft wie kNN auf dem vorhandenen Embedding-Server, aber mit brauchbarer Konfidenz

## Aussage
Weiche vor dem Agenten mit drei Zielen (trivial / coding / schwer), 60 echte
Anfragen mit Soll-Label von Hand, dieselben wie fuer Laya auf Victus:

| Verfahren | Treffer | schwer zu niedrig | Treffer bei p >= 0,8 | Zeit je Fall |
|---|---|---|---|---|
| kNN k=5, bge-m3 (Port 8001), leave-one-out | 49/60 (0,82) | 2 | – | 0,03 s |
| kNN k=1 | 44/60 | 3 | – | 0,03 s |
| decider-4b Q4, deutsche Formulierung | **50/60 (0,83)** | 2 | **21/21** | 0,75 s |
| decider-4b Q4, englische Formulierung | 46/60 | 4 | 21/21 | 0,69 s |
| Laya multilingual (Victus, 30 Faelle) | 24/30 (0,80) | 3 von 7 | 10/12 | 0,06 s |

decider laedt in 2,5 s (2,7 GB GGUF, CPU), antwortet ohne Feinjustierung und
ohne Beispiele. Alle zehn Fehler der deutschen Fassung liegen unter p 0,8; mit
der Regel "unter 0,8 an das Hauptmodell" ist keine Entscheidung falsch, aber nur
21 von 60 werden ueberhaupt entschieden. Sieben der zehn Fehler sind kleine
Shell-Aufgaben, die das Label "trivial" tragen und die decider als "coding"
liest; das ist eine Konvention der Labels, keine Schwaeche des Modells. Die
teure Richtung (schwere Anfrage nach unten) trifft decider und kNN gleich
selten, je zwei.

## Traegt
- Ein Entscheidungsmodell auf CPU neben dem 27B, 0,75 s je Entscheidung, 2,7 GB
  Platte, 16 Threads kurz voll.
- Die Formulierung der Ziele in der Sprache der Anfragen (deutsch) ist vier
  Treffer besser als englisch.
- Konfidenz als Schalter: ab 0,8 verlaesslich (21/21), darunter nachfragen oder
  Standardziel.

## Traegt nicht
- Ein Vorsprung vor kNN auf dem Embedding-Server, der ohnehin laeuft: ein Fall
  von 60 ist Rauschen. Wer die Konfidenz nicht braucht, braucht decider nicht.
- Die Labels selbst: "Shell-Befehl = trivial" ist eine Setzung; mit "Shell =
  coding" waere decider bei 57/60.
- Mehr als drei Ziele (ungemessen) und Anfragen ueber 1.536 Token (Kontextkappung
  des Prompt-Bauers).

## Bruchindikator
Auf 200 statt 60 Faellen faellt decider unter kNN, oder die Treffer bei p >= 0,8
sinken unter 90 %.

## Ablesung
Eigene Messung, `system/werkzeuge/decider-route-test.py`, Ergebnis
`ergebnisse/decider/route_ergebnis.json`. Download der Gewichte ueber WLAN: curl
mit `-C -` und `-r` zusammen liefert bei Wiederaufnahme falsche Bytes, die
SHA-256 gegen Hugging Face entlarvte es; Bereiche ohne Wiederaufnahme laden.

## Verknuepft
- [decision-model-as-profile-orchestrator](../open_checks/decision-model-as-profile-orchestrator.md)
- [laya-router-before-agent](laya-router-before-agent.md)
- [lean-hermes-toolsets](lean-hermes-toolsets.md)
