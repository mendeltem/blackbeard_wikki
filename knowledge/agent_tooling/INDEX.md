# agent_tooling

Werkzeuge bauen, auf deren Ausgabe sich ein Agent oder ein Mensch verlaesst.
Nicht modellspezifisch: es geht um Pruefwerkzeuge, Messwerkzeuge und
Vorbedingungspruefungen.

Der rote Faden aller Einträge: **ein Pruefwerkzeug, dessen eigener Fehler wie
ein Befund am Geprueften aussieht, ist die gefaehrlichste Sorte.** Es wird
geglaubt, weil es wie eine Messung aussieht.

Stand 2026-10-07. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| regel | [release-test-means-fresh-machine-with-release-assets](rules/release-test-means-fresh-machine-with-release-assets.md) | Installierbar = frische Umgebung nur mit README + Gewichte vom Release, CI auf fremdem Runner, jede CLI-Option einmal; fand den stummen FSL-Haenger ohne FSLDIR | getragen |
| regel | [pip-freeze-is-not-an-install-file](rules/pip-freeze-is-not-an-install-file.md) | pip freeze ist Protokoll, keine Installationsdatei (+cu124, %2B); minimal gepinnt + Test aus frischem Clone bis zum Selbsttest, Log ins Repo | getragen |
| [Datenumzug: umbenennen, Symlink zurueck, Protokoll](rules/data-move-by-rename-symlink-and-protocol.md) | regel | vorschlag |
| [Ergebnis-Repo braucht eine Nachvollziehbarkeitskarte](rules/traceability-map-for-a-results-repo.md) | regel | vorschlag |
| [Kein Rueckfallwert ohne eine Zeile, die ihn benennt](rules/no-silent-fallback-values.md) | regel | getragen |
| [Leer ist nicht fehlend](rules/empty-is-not-missing.md) | regel | getragen |
| [Unbekannt ist kein Wert in einem Vergleich](rules/unknown-is-not-a-value-in-comparisons.md) | regel | getragen |
| [Erstmessung ist keine Veränderung](rules/first-measurement-is-not-a-change.md) | regel | getragen |
| [Gerechnetes und Gemeintes müssen auseinanderzuhalten sein](rules/computed-and-judged-must-stay-separable.md) | regel | getragen |
| [Agenten-Werkzeuge nach Aufgabenform schneiden](rules/agent-tools-by-task-shape.md) | regel | vorschlag |
| [Werkzeugwahl zeigt nur eine Spur am echten Host](rules/tool-choice-needs-host-trace.md) | regel | vorschlag |
| [Skill routet zuerst und schließt mit seiner Checkliste](rules/skill-routes-first-and-closes-its-checklist.md) | regel | vorschlag |
| [Tests belegen Aussagen, nicht Verkabelung](rules/tests-prove-claims-not-plumbing.md) | regel | vorschlag |
| [Eine Neustartschleife ist ein Alarm, keine Reparatur](rules/restart-loop-is-an-alarm-not-a-repair.md) | regel | vorschlag |
| [Jede Sperre und zustandsabhaengige Anweisung braucht ein Verfallsereignis](rules/conditions-need-an-expiry-event.md) | regel | vorschlag |
| [Die ersten N einer sortierten Liste sind ein Block](rules/first-n-of-a-sorted-list-is-a-block.md) | regel | vorschlag |
| [Vor dem Probelauf eines fremden Skripts nach Schreibzielen greppen](rules/grep-for-write-targets-before-a-dry-run.md) | regel | vorschlag |
| [Vor der ersten Aenderung an einer fremden Datei sichern](rules/back-up-before-first-edit-of-a-foreign-file.md) | regel | vorschlag |
| [Nachlauf als trap EXIT, dann im Log nachsehen](rules/exit-hook-via-trap-then-verify-in-log.md) | regel | vorschlag |
| [Eine billige Vorpruefung ordnet, sie entscheidet nicht](rules/cheap-precheck-ranks-but-does-not-decide.md) | regel | vorschlag |
| [Vor der Deutung einer gepoolten Zahl die tragenden Faelle zaehlen](rules/count-cases-behind-a-pooled-number.md) | regel | vorschlag |
| [Bausteine gegen ihren Code benennen](rules/name-a-component-against-its-code.md) | regel | vorschlag |
| [Erst die Definition suchen, dann die Differenz deuten](rules/find-the-definition-before-interpreting-a-difference.md) | regel | vorschlag |

## Herkunft

Die neun Regeln vom 2026-10-07 stammen aus der Aufsicht ueber einen lokalen Agenten in
der WMH- und CMB-Linie (Alita, 2026-09-14 bis 2026-09-23): jede aus einem eigenen,
am Code oder Log belegten Vorfall. Status vorschlag, weil nur je ein Vorfall dahintersteht.

Beide Einträge stammen aus dem Bau und der Pruefung von Werkzeugen im Projekt
[local_models](https://github.com/mendeltem/local_models) -- `tools/detect.py`
(Kapazitaetsrechnung) und `alita/werkzeuge/vorflug` (Vorbedingungspruefung eines
Agentenauftrags). Die Pfade und Messwerte stehen dort, hier steht nur, was
uebertragbar ist.

Die drei neueren Eintraege stammen aus der Lageseite
[AI_Lage](https://github.com/mendeltem/AI_Lage), die zehn Schwesterseiten liest
und daraus Thesen und Widersprueche rechnet.

Die vier Regeln vom 2026-10-06 sind aus dem Projekt [rea](https://github.com/morluto/rea)
(Reverse Engineering mit Agenten, MIT) übernommen: Werkzeugdesign, Skill-Aufbau,
Testprüfung. Bei uns nicht gemessen, daher vorschlag.
| regel | [never-edit-a-running-bash-script](rules/never-edit-a-running-bash-script.md) | bash liest Skripte waehrend der Ausfuehrung weiter; ein Edit mitten im Lauf erzeugt Syntaxfehler und verwaiste Ergebnisse; Aenderungen in neue Datei | getragen |
| regel | [gpu-job-needs-cuda-check-in-its-own-env](rules/gpu-job-needs-cuda-check-in-its-own-env.md) | Vor dem Einreihen: cuda.is_available, voller Inferenz-Import, Mini-Lauf mit GPU in GENAU der Umgebung; pkill-Muster nicht woertlich im Kommando | getragen |
| regel | [blackboard-short-protocol-long-html](rules/blackboard-short-protocol-long-html.md) | Tafel-Markdown nur Funktionskern (kurz, ueber das Werkzeug, Nummern stabil); Verstaendliches als gebaute, verlinkte HTML-Seiten mit Plots und Datenschutzfilter | getragen |
| regel | [kill-by-pid-fetched-in-a-separate-command](rules/kill-by-pid-fetched-in-a-separate-command.md) | pgrep/pkill -f trifft die eigene Shell, wenn der Zielname irgendwo im selben Kommando steht (3 Belege, Exit 144); PID in eigenem Kommando holen, dann nackt killen | getragen |
| regel | [case-ids-are-dataset-local-prefix-when-pooling](rules/case-ids-are-dataset-local-prefix-when-pooling.md) | sub-101 gibt es in HCP und VALDO: ohne Praefix ueberschrieben Testfaelle Trainingsfaelle (Leck, 'Test 6' statt 12); praefixieren, Zaehlung pruefen, Kurztest mit Kollision | getragen |
