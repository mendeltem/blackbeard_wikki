---
id: compute-allocation-by-sector
typ: pruefpunkt
status: offen
thema: knowledge/ai_application_layer
stand: 2026-10-14
herkunft: Projekt Artificial Intelligence (claude.ai), Gespräch 2026-10-14
verweist_auf: [pharma-share-of-ai-compute, absence-of-measurement-is-not-measurement-of-absence, accelerator-mass-balance]
---

# Compute-Aufteilung nach Anwendungsbereich: Dossier-Zahlen ohne Quelle

## Aussage
Ein „Strategie-Dossier“, das Mendel am 2026-10-14 vorlegte, verteilt den globalen Enterprise- und Inferenz-Compute so:

| Bereich | Anteil laut Dossier |
|---|---|
| Software-Engineering und Coding-Agenten | 25 bis 30 % |
| Wissensabfragen, Suche, Zusammenfassung | 20 bis 25 % |
| Echtzeit-Kommunikation, Voice, Telco | 15 bis 20 % |
| Generative Medien | 10 bis 15 % |
| Molekulardynamik und Pharma-Simulation | 5 bis 8 % |
| Fertigung, Robotik, Edge | 4 bis 6 % |
| Finanzanalytik, Betrugserkennung | 3 bis 5 % |

Keine Zeile hat eine Quelle, der Nenner ist nicht definiert (Rechenzeit, FLOPS, Token oder Ausgaben?), und die Mittelwerte summieren sich auf rund 96 %. Die Pharma-Zeile ist nach der Größenrechnung in [pharma-share-of-ai-compute](../findings/pharma-share-of-ai-compute.md) um etwa eine Größenordnung zu hoch. Molekulardynamik ist zudem klassisches HPC und kein KI-Inferenz-Workload. Die Tabelle ist deshalb kein Befund und darf nicht als Stütze zitiert werden.

## Zu prüfen
1. Nenner festlegen: Token, Inferenz-Ausgaben in Dollar oder installierte Beschleuniger-Leistung. Nur eine Größe je Tabelle.
2. Belegbare Ankerpunkte sammeln: Anthropic Economic Index (Aufgabenanteile nach Berufsgruppe), OpenRouter-Tokenstatistik nach Kategorie, Menlo-Ventures-Spend-Erhebungen. Für jede Quelle die Grenze nennen: Ein Plattformausschnitt ist nicht der Weltmarkt.
3. Coding-Anteil gegen Token-Statistiken halten (der Projekt-Report „AI Use Case Landscape Juli 2026“ nennt ~54 % des Coding-LLM-Spends bei Anthropic, Menlo Ventures, Sekundärquelle).
4. Ergebnis als Spannweite je Bereich mit Quelle eintragen, Lücken offen lassen (Regel [absence-of-measurement-is-not-measurement-of-absence](../rules/absence-of-measurement-is-not-measurement-of-absence.md)).

## Ablesung
blind. Die Dossier-Tabelle hat keine Quelle.

## Verknüpft
- [pharma-share-of-ai-compute](../findings/pharma-share-of-ai-compute.md)
- [absence-of-measurement-is-not-measurement-of-absence](../rules/absence-of-measurement-is-not-measurement-of-absence.md)
- [accelerator-mass-balance](accelerator-mass-balance.md)
