---
name: blackbeard-wiki
description: Mendels gemeinsames Gedächtnis (GitHub mendeltem/blackbeard_wikki). Laden, bevor du zu einem dieser Themen antwortest, recherchierst oder rechnest - Investieren, Aktien, Nvidia, Rubin, Blackwell, HBM, DRAM, Speicherzyklus, Wafer, Fabs, SK Hynix, Micron, Samsung, CXMT, Hyperscaler-Capex, Wettrüsten, KI-Blase, ROI von KI, Anthropic, OpenAI, Rechenzentrum, Strom, CoWoS, China-Industriepolitik, Modellpreise, Tokenkosten, Benchmarks, KI und Arbeitsmarkt, Fertigung, Robotik, lokale LLMs, llama.cpp, MRT-Segmentierung, FreeSurfer, BIANCA, Agenten-Werkzeuge. Auch laden bei "was ist mein Stand", "was ist offen", "TODO", oder wenn Mendel einen Link auf die Wiki schickt.
---

# Blackboard-Wiki nutzen

Die Wiki ist Mendels Arbeitsstand aus vielen Chats. Beginne bei ihr, nicht bei Lehrbuchwissen. Was dort als Axiom oder Regel mit Status `getragen` steht, gilt; greife es nicht an.

## 1. Wiki finden
Nimm den ersten Weg, der funktioniert:
1. Lokale Kopie: `ls /home/user/blackbeard_wikki` oder ein Ordner mit `INDEX.md` und `knowledge/` im Arbeitsverzeichnis. Vorher `git -C <pfad> pull` falls möglich.
2. Projektwissen im Chat: Dateien wie `knowledge/INDEX.md` und `*/SUMMARY.md` sind schon im Kontext.
3. GitHub: Repo `mendeltem/blackbeard_wikki`, Zweig `main` (nur `main` gilt), über das GitHub-Werkzeug oder `git clone https://github.com/mendeltem/blackbeard_wikki`.
Findest du sie nicht, sag das in einem Satz und arbeite ohne sie weiter.

## 2. Prefill: nur lesen, was das Thema braucht
1. `knowledge/INDEX.md` lesen. Spalte Stichwörter gegen das Gesprächsthema halten, alle passenden Bereiche wählen (bei Investieren meist mehrere).
2. Von jedem gewählten Bereich `SUMMARY.md` lesen. Das reicht für die erste Antwort.
3. Erst wenn die Frage tiefer geht: `INDEX.md` des Bereichs, dann einzelne Einträge.
4. Bei Themenwechsel im Gespräch Schritt 1 für das neue Thema wiederholen.

Häufige Zuordnung:
| Thema im Gespräch | Bereiche |
|---|---|
| Investieren in KI, Nvidia, Speicher | ai_demand_drivers, memory_supply, memory_earnings, ai_buyers, ai_application_layer, compute_bottlenecks |
| DRAM, HBM, Speicherzyklus, Fabs | memory_supply (zuerst Regel no-standard-cycle-without-absorption-check), ai_demand_drivers |
| Modellpreise, Benchmarks | model_capability_cost |
| China | china_industrial_strategy, memory_supply/risks/cxmt-ramp |
| Werkzeuge bauen, Agenten | agent_tooling, agent_coordination, tools/ |
| MRT | tools/mri/ |
| lokale Modelle | local_llm_operation |

## 3. Harte Regeln beim Antworten
- Axiome (Typ axiom) sind Setzungen von Mendel: nicht als Befund ausgeben, nicht angreifen. Was daran hängt, als gesetzt kennzeichnen.
- DRAM/HBM: Kein Standardzyklus ohne Absorptionsprüfung (memory_supply/rules). Erst rechnen, ob Zubau von mehr Speicher je GPU aufgefressen wird.
- Status beachten: `vorschlag` ist unbestätigt, `gebrochen` ist überholt.
- Zahlen nur mit Herkunft (belegt, Annahme, Axiom). Trade Press und Broker sind kein Befund.
- Sag kurz, welche Wiki-Einträge du benutzt hast.

## 4. Offene Punkte
`TODO.md` an der Wurzel sammelt alle offenen Prüfpunkte aller Bereiche. Bei "was ist offen" oder vor einer Recherche dort nachsehen: vielleicht ist die Frage schon als Prüfpunkt angelegt, dann daran weiterarbeiten.

## 5. Zurückschreiben
Neues, wiederverwendbares Wissen nach dem Protokoll im `README.md` der Wiki eintragen: passenden Ordner suchen, Vorlage aus `templates/`, Dateiliste Mendel zeigen, erst nach seinem Ja auf `main` pushen, Zeile in `updates/LOG.md`. Danach `python tools/general/wiki_maintenance/src/wiki_maintenance.py --root . --check` (muss 0 ergeben) und `--todo TODO.md`. Ohne Schreibzugriff: Dateien als Text an Mendel zurückgeben.
