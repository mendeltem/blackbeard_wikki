---
id: one-mapping-file-for-linked-pages
typ: regel
status: getragen
thema: knowledge/agent_coordination
stand: 2026-10-06
herkunft: Claude-Code-Sitzung, Verknüpfung ai_use_cases_overview / Supply_Atlas3D / AI_Companys, 2026-10-06
verweist_auf: [one-filename-two-contracts, parallel-sessions-same-working-tree]
---

# Verknüpfte Seiten: eine Zuordnungsdatei, feste Adressen, Rückweg im Generator

## Aussage
Drei Seiten sind seit 2026-10-06 gegenseitig verlinkt:
[ai_use_cases_overview](https://mendeltem.github.io/ai_use_cases_overview/) (Use-Case-Karten),
[Supply_Atlas3D](https://mendeltem.github.io/Supply_Atlas3D/) (Globus mit Standorten) und
[AI_Companys](https://mendeltem.github.io/AI_Companys/nvidia-oekosystem.html) (Firmenkennzahlen).
Damit das so bleibt, gelten drei Regeln.

1. **Eine Zuordnungsdatei.** Alle Verknüpfungen stehen in
   `ai_use_cases_overview/deployments.json`, nirgends sonst. Abschnitte:
   - `use_cases.<slug>.places`: Orte je Use Case; entweder `{"site": "<Name im Atlas>"}` oder eigene `la/lo` mit Satz und Quelle.
   - `companies.names`, `companies.operators` (Textstücke, gegen das Betreiberfeld `ow` im Atlas gesucht), `companies.use_cases` (Karten-Slug → Ticker), `companies.cards` (Kartennamen DE/EN).
   Alle drei Seiten lesen sie zur Laufzeit per `fetch`. Gleiche Domain, GitHub Pages liefert `Access-Control-Allow-Origin: *`.
2. **Feste Adressen, nicht ändern ohne alle drei Seiten:**
   - Karte: `ai_use_cases_overview/#uc=<slug>`, Slug = englischer Kartenname klein, Nicht-Alphanumerisches → `-`.
   - Globus je Use Case: `Supply_Atlas3D/?uc=<slug>`; je Firma: `?company=<TICKER>`; Test mit eigener Datei: `&dep=<datei>`.
   - Firma: `AI_Companys/nvidia-oekosystem.html#/<de|en|mn>/<TICKER>`.
3. **Rückweg auf generierten Seiten gehört in den Generator.** AI_Companys wird täglich von einer Pipeline neu geschrieben; `werkzeuge/seite.py` trägt Ergänzungen danach über Marker wieder auf. Der Verbundblock steht dort als eigener Schritt (`/* verbund-hilfe */`, Stil `verbund`, Texte `vb_*`). Direkt in die HTML geschrieben wäre er am nächsten Morgen weg.

## Trägt
- Einen neuen Ort oder eine neue Firmen-Zuordnung eintragen heißt: eine Zeile in `deployments.json`. Keine Seite muss neu gebaut werden.
- Fällt der Abruf aus, verschwinden die Verbundteile still; die Seiten bleiben benutzbar.

## Trägt nicht
- Einen Kartennamen ändern, ohne den Slug in `deployments.json` mitzuziehen: Links laufen dann ins Leere, ohne Fehlermeldung.
- Einen Atlas-Standort umbenennen: `{"site": ...}`-Verweise finden ihn nicht mehr und fallen weg.
- Den Rückweg auf AI_Companys von Hand in die HTML schreiben.

## Bruchindikator
Ein Link landet auf einer Karte, die nicht aufklappt, oder ein Use Case zeigt im Atlas weniger Orte als in `deployments.json` stehen. Prüfen: im Atlas `ucPlaces(UC_ALL[slug]).length` gegen `places.length`.

## Ablesung
Eigene Umsetzung, Commits 2026-10-06: ai_use_cases_overview 8910802, c2541be, 2700f45, 06d7a4b; Supply_Atlas3D bf3d831, 9973dfc, 7dbd125, 6600510; AI_Companys c6c3134. `seite.py`-Schritt im Probelauf zweimal angewandt, zweiter Lauf ohne Änderung; ein voller `seite.py`-Lauf ging nicht, weil der Datenordner `AI_companys_berichte` auf dem bauenden Rechner fehlte.

## Verknüpft
[one-filename-two-contracts](one-filename-two-contracts.md), [parallel-sessions-same-working-tree](parallel-sessions-same-working-tree.md)
