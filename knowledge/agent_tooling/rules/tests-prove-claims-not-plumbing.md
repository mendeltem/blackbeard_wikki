---
id: tests-prove-claims-not-plumbing
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-06
herkunft: Projekt rea (morluto/rea, MIT), docs/test-suite-audit.md vom 2026-10-04 und AGENTS.md, Stand b6c21b1
verweist_auf: [empty-is-not-missing, no-silent-fallback-values]
---

# Tests belegen Aussagen, nicht Verkabelung

## Aussage
rea hat am 2026-10-04 alle 355 Testdateien in drei Durchgängen geprüft und
Tests gestrichen oder ersetzt, die nichts belegten. Rangfolge der Belegkraft:

1. echter End-to-End-Lauf mit dem echten Werkzeug (Hopper, Ghidra, Browser)
2. Integration über die echten Schemata und Transportwege (CLI und MCP)
3. Goldens aus echten Daten

Niedrigere Tests werden gestrichen, sobald ein höherer dieselbe Aussage belegt.
Fehlerfälle, die ein erfolgreicher E2E-Lauf nicht auslösen kann, bleiben.

Gestrichen oder umgebaut wurden unter anderem:
- Tests, die **willkürliche Grenzen oder Aufrufreihenfolgen festschreiben**
  (Seitengröße 10 001, Position eines Werkzeugs in einem Prompt-Vorschlag,
  CI-Matrix-Werte).
- Positivtests mit **selbstgebauten Eingaben**, die mit derselben Bibliothek
  erzeugt wurden, die sie lesen. Ersetzt durch echte erfasste Dateien.
- Prüfungen, die nur **bedingt auf Erfolg** liefen. Unerwartete Fehler konnten
  so bestehen; jetzt wird Erfolg zuerst verlangt.
- Ein Prüflauf, der **verweigerte Berechtigung als bestanden** wertete. Jetzt zwei
  getrennte Ergebnisse; der Lauf ohne Berechtigung meldet ausdrücklich "kein Beleg".

Aussagen über echte externe Werkzeuge lassen sich nicht durch Mocks ersetzen.

## Trägt
Tests in local_models (`alltag`, `schicht`, `laya`, `finetune`). Das dort benutzte
Muster, jede Prüfung gegen eine bekannt gute **und** eine bekannt schlechte Antwort
laufen zu lassen, ist die kleine Form derselben Idee. Der OpenCode-Lauf, der
`json.load` ein MagicMock reichte, ist ein Beispiel für einen Test, der Verkabelung
statt Verhalten prüft.

## Trägt nicht
Eine Aussage zur nötigen Abdeckung. rea senkt Abdeckungsschwellen ausdrücklich
nicht, um Tests streichen zu können.

## Bruchindikator
Ein Test, der grün bleibt, wenn man die geprüfte Funktion durch eine falsche
ersetzt. Oder ein Prüflauf, der "bestanden" meldet, obwohl das Werkzeug gar nicht
lief.

## Ablesung
Projekt-Doku: https://github.com/morluto/rea/blob/main/docs/test-suite-audit.md
und https://github.com/morluto/rea/blob/main/AGENTS.md (Abschnitt "Testing Guidelines").

## Verknüpft
- [empty-is-not-missing](empty-is-not-missing.md)
- [no-silent-fallback-values](no-silent-fallback-values.md)
