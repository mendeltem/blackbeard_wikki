---
id: skill-routes-first-and-closes-its-checklist
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-06
herkunft: Projekt rea (morluto/rea, MIT), skills/reverse-engineer-anything/SKILL.md Version 25, Stand b6c21b1 vom 2026-10-05
verweist_auf: [agent-tools-by-task-shape, rule-lists-make-small-models-refuse]
---

# Ein Agenten-Skill routet zuerst und schließt mit seiner Checkliste

## Aussage
Der Skill von rea ist kurz und folgt einem Aufbau, der sich auf andere Skills
übertragen lässt:

1. **Wann nicht.** Die Beschreibung sagt, wofür der Skill nicht gedacht ist
   ("für ein vollständiges Quell-Repo normale Werkzeuge nehmen").
2. **Zuerst routen.** Das erste Werkzeug ergibt sich aus der Art des Ziels
   (ASAR, Paket, Assembly, Browserseite, Binary). Fehlt das Ziel, nachfragen;
   nie selbst ein Beispiel wählen.
3. **Erst die Zusammenfassung.** Mit dem Standardergebnis anfangen, keinen
   identischen Aufruf wiederholen, nur gezielt nachfassen, wenn eine konkrete
   Frage offen bleibt.
4. **Beobachtung, Folgerung, Unbekanntes** in jeder Schlussfolgerung getrennt,
   mit Beleg-IDs.
5. **Große Untersuchungen gestuft:** Anfrage in eine Fragen-Checkliste mit nötigem
   Beleg je Frage zerlegen, vorhandenen Stand wiederverwenden, unabhängige Fragen
   parallel vergeben, ein knappes Befund-Register führen.
6. **Vor dem Abschluss die Checkliste erneut durchgehen** und jede Frage als
   beantwortet, teilweise beantwortet oder offen markieren. Eine breite
   Untersuchung nie "fertig" nennen, solange Pflichtfragen offen sind.
7. **Bereitschaft nur bei Bedarf prüfen.** `doctor` läuft nicht vor jeder Aufgabe,
   sondern nur, wenn ein Werkzeug fehlt oder die Registrierung veraltet ist.
   Setup zeigt den Plan und braucht Zustimmung, bevor es etwas schreibt.
8. **Nur die passende Referenz lesen.** Details liegen in getrennten Dateien unter
   `references/`, der Skill verweist je Zielart auf genau eine.

## Trägt
Eigene Skills, etwa unsloth-finetune im Wiki, Hermes-Skills und Aufträge für
`schicht`. Punkt 6 ist die Gegenmaßnahme zu Agenten, die "fertig" melden, während
Teilaufgaben offen sind; Punkt 7 spart Prompt und Zeit bei jedem Aufruf.

## Trägt nicht
Dass kleine lokale Modelle einen Skill dieser Länge befolgen. Lange Regellisten
im System-Prompt können kleine Modelle zum Ablehnen bringen, siehe
[rule-lists-make-small-models-refuse](../../local_llm_operation/findings/rule-lists-make-small-models-refuse.md).
Der rea-Skill zielt auf große Hosts.

## Bruchindikator
Ein Agent mit diesem Aufbau meldet eine breite Untersuchung als abgeschlossen,
obwohl Fragen der eigenen Checkliste offen sind.

## Ablesung
Projekt-Doku: https://github.com/morluto/rea/blob/main/skills/reverse-engineer-anything/SKILL.md

## Verknüpft
- [agent-tools-by-task-shape](agent-tools-by-task-shape.md)
- [rule-lists-make-small-models-refuse](../../local_llm_operation/findings/rule-lists-make-small-models-refuse.md)
