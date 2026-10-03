---
id: hermes-agent-local-qwen-benchmark
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-03
herkunft: Claude-Code-Sitzung auf Victus, 2026-10-03
verweist_auf: [ollama-silently-truncates-context, counting-needs-thinking, rule-lists-make-small-models-refuse]
---

# Hermes Agent mit lokalem Qwen3.6 loest Alltagsaufgaben, scheitert an Format und Rueckfragen

## Aussage
Hermes Agent (Nous Research) auf Victus, Modell `qwen3.6:35b` ueber Ollama mit
`num_ctx 65536`, Aufruf `hermes -z <aufgabe>`. 14 Aufgaben, jede mit Pruefskript,
das Hermes nicht sieht:

- 13/14 laut Pruefung bestanden, in 10 Minuten zusammen; 9 bis 110 s je Aufgabe,
  1 bis 11 Modellaufrufe.
- Inhaltlich alle richtig: Dateien zaehlen, Skript schreiben, JSON ohne Beiwerk,
  Bugfix, Absturz mit falschen Datentypen, Umbenennen ueber drei Dateien, CSV mit
  800 Zeilen, 16 Dateien anlegen, git mit Branch, LIS in O(n log n) (200k
  Elemente in 0,02 s), Todo-CLI gegen versteckte Tests.
- **Format:** CSV-Ergebnis mit deutschem Dezimalkomma (`101898,03`) statt dem
  verlangten Punkt.
- **Rueckfrage:** "Aendere den Port" bei zwei Ports in der Datei - Hermes nahm den
  ersten und sagte das hinterher, statt vorher zu fragen. Die Pruefung hat das
  als bestanden gewertet; streng genommen ist es keins.

Der Hermes-System-Prompt allein ist rund 13k Token gross und geht bei jeder
Aufgabe mit, auch bei Kopfrechnen.

## Traegt
Lokales Qwen3.6 als Agent fuer abgegrenzte Aufgaben mit klarer Pruefung. Ausgaben,
die Maschinen weiterlesen, brauchen eine Formatpruefung. Mehrdeutige Auftraege
nicht unbeaufsichtigt laufen lassen.

## Traegt nicht
Lange, offene Aufgaben (mehr als ~20 Schritte, fremde grosse Codebasen). Die
Aufgaben hier waren zu klein, um die Grenze zu finden. Einmaliger Lauf, eigene
Aufgaben - kein Vergleichswert zu anderen Modellen.

## Bruchindikator
Ein Lauf, in dem inhaltliche Fehler auftauchen, oder Aufgaben, die mitten im
Verlauf die 50k nutzbaren Token ueberschreiten (siehe Kuerzungsrisiko).

## Ablesung
Eigene Messung, Hermes Agent main @ 5d3c05977, Ollama, Victus Ubuntu 26.04.
Aufgaben und Pruefungen: `tasks.py` in `~/hermes-bench` auf Victus.

## Verknuepft
- [ollama-silently-truncates-context](../risks/ollama-silently-truncates-context.md)
- [counting-needs-thinking](../findings/counting-needs-thinking.md)
- [rule-lists-make-small-models-refuse](../findings/rule-lists-make-small-models-refuse.md)
