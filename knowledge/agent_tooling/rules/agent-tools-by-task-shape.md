---
id: agent-tools-by-task-shape
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-06
herkunft: Projekt rea (morluto/rea, MIT), docs/tool-design.md und AGENTS.md, Stand b6c21b1 vom 2026-10-05
verweist_auf: [empty-is-not-missing, no-silent-fallback-values, computed-and-judged-must-stay-separable, tool-choice-needs-host-trace]
---

# Agenten-Werkzeuge nach Aufgabenform schneiden, nicht nach der API dahinter

## Aussage
rea (Reverse Engineering mit Agenten, 116 MCP-Werkzeuge) schneidet jedes Werkzeug
nach der Frage, die ein Agent stellt, nicht nach der Schnittstelle der Engine
darunter (Hopper, Ghidra). Sechs Formen:

| Form | wofür | gibt zurück |
|---|---|---|
| inspect | Fakten zu einem ausdrücklich benannten Objekt | Felder, Fundstelle, welche Teile verfügbar sind |
| search / list | Kandidaten finden | stabile Reihenfolge, Kontext je Treffer |
| trace | Beziehungen zwischen Dingen | typisierte Kanten, Beleg je Kante, offene Pfade |
| compare | zwei ausdrücklich gepaarte Dinge | gleiche Abdeckung, Unterschiede mit Beleg |
| workflow | wiederkehrendes Ergebnis aus mehreren Quellen | Ergebnis inline, beitragende Belege, Lücken |
| observe / capture | Fragen, die Laufzeit brauchen | nötige Befugnis, Lebenszyklus, Aufräumstatus |

Dazu sieben Vertragsregeln:
1. **Primitive zuerst.** Ein Workflow kommt erst, wenn beobachtete Nutzung dieselbe
   Folge von Aufrufen wiederholt zeigt, und er muss für verschiedene Anwendungen
   gleich sinnvoll sein. Geschäftslogik einer einzelnen Anwendung gehört nicht ins
   allgemeine Werkzeug.
2. **Vollständig per Voreinstellung.** Grenzen nur aus echten Format-, Protokoll-,
   Befugnis- oder Ressourcengründen, nie um ein vermutetes Kontextbudget zu schonen.
   Kürzung, Teilausfall und "nicht verfügbar" stehen ausdrücklich im Ergebnis.
3. **Fehlende Evidenz ist unbekannt, nicht leer und nicht falsch.**
4. **Beobachtet, abgeleitet und gefolgert getrennt**, jede wichtige Beziehung mit Beleg.
5. **Belege inline.** Der Agent soll nicht erst eine Ressource oder eine undurchsichtige
   ID nachladen müssen, um das Ergebnis zu verstehen.
6. **Wirkungen ehrlich deklarieren** (nur lesen, schreibt, startet Prozess, Netz, UI)
   und auf das im Aufruf genannte Ziel begrenzen.
7. **Keine Bestätigungs-Schalter** wie `approve: true`. Der gewählte Aufruf drückt die
   Absicht schon aus. Optionen, die nichts bewirken, entfernen.

Keine Mega-Werkzeuge, die Suchen, Ausführen und Ändern mischen, keine undurchsichtigen
Modus-Flags.

## Trägt
Entwurf eigener Agenten-Werkzeuge und MCP-Server: Laya-Router, `frag`, `schicht`-Abnahmen,
Prüfskripte unter local_models. Prüffrage vor jedem neuen Werkzeug: Welche Aufgabenform,
was ist das kleinste Ergebnis, das die Frage beantwortet, und welches bestehende
Werkzeug ist das nächstliegende?

## Trägt nicht
Dass rea damit gut auffindbar ist. Das belegt rea nach eigener Regel nur über echte
Host-Spuren, siehe [tool-choice-needs-host-trace](tool-choice-needs-host-trace.md).
Bei uns ist keine der sieben Regeln gemessen; sie sind übernommen.

## Bruchindikator
Ein Agent ruft ein Werkzeug regelmäßig zwei- oder dreimal hintereinander mit
ähnlichen Argumenten, um eine Frage zu beantworten. Dann fehlt ein Primitiv oder
ein Workflow ist fällig.

## Ablesung
Projekt-Doku (Selbstbeschreibung des Projekts, keine Fremdmessung):
- https://github.com/morluto/rea/blob/main/docs/tool-design.md
- https://github.com/morluto/rea/blob/main/AGENTS.md (Abschnitte "Designing MCP Tools", "Boundary Contracts")

## Verknüpft
- [empty-is-not-missing](empty-is-not-missing.md)
- [no-silent-fallback-values](no-silent-fallback-values.md)
- [computed-and-judged-must-stay-separable](computed-and-judged-must-stay-separable.md)
- [tool-choice-needs-host-trace](tool-choice-needs-host-trace.md)
