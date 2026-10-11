---
id: kill-by-pid-fetched-in-a-separate-command
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-11
herkunft: drei Selbsttreffer der Agentenshell (07.10. drips_lauf, 11.10. 03:35 synapse get, 11.10. 07:05 G2-Neustart), PVS-Arena Alita
verweist_auf: [gpu-job-needs-cuda-check-in-its-own-env, never-edit-a-running-bash-script]
---

# Prozesse per PID beenden, die PID in einem EIGENEN Kommando holen -- pgrep/pkill -f trifft sonst die eigene Shell

## Regel
`pkill -f MUSTER` und `kill $(pgrep -f MUSTER)` pruefen jede Kommandozeile, auch die der Shell, die den Aufruf gerade ausfuehrt.
Steht das Muster -- oder ein Text, auf den das Muster passt -- irgendwo in demselben Kommando (ein spaeterer Aufruf desselben
Skripts, ein Log-Pfad mit dem Skriptnamen, ein sed auf den Dateinamen), stirbt die eigene Shell mit Exit 144, und alles, was
nach dem kill kommen sollte (Protokollzeile, Neustart), laeuft nicht. Der Klammertrick (`cn[n]`) schuetzt nur vor dem Muster
selbst, nicht vor dem echten Dateinamen weiter hinten im Kommando.
Deshalb: 1) In einem eigenen Kommando `pgrep -f MUSTER` ausfuehren und die PID lesen. 2) Im naechsten Kommando `kill PID`
(nackte Zahl). 3) Erst danach das Kommando mit Protokoll, Patch und Neustart. Wer es in einem Kommando braucht: PID vorher
in eine Variable holen und sicherstellen, dass der Zielname sonst nirgends im Kommando vorkommt -- was praktisch nie gelingt,
wenn man dasselbe Skript danach neu startet.

## Belege
- 07.10.: pkill auf das DRIPS-Skript, Exit 144, Korrekturzeilen fehlten im Protokoll.
- 11.10. 03:35: `synapse get` beenden + ARBEIT.md anhaengen + sed auf die Memory-Datei in einem Kommando -> Exit 144, zwei von drei Schritten fehlten.
- 11.10. 07:05: `kill $(pgrep -f "zweite_stufe_cn[n]")` gefolgt von py_compile und Neustart desselben Skripts im selben Kommando -> das Muster traf den
  spaeteren Dateinamen in der eigenen Kommandozeile; Patch und Test fielen aus, die Ursache war erst nach einem weiteren Kommando klar.

## Verknuepft
- [gpu-job-needs-cuda-check-in-its-own-env](gpu-job-needs-cuda-check-in-its-own-env.md) (Nachtrag dort war die erste Fassung)
- [never-edit-a-running-bash-script](never-edit-a-running-bash-script.md)
