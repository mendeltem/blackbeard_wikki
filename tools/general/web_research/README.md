---
id: web_research
bereich: tools/general
stand: 2026-10-17
herkunft: Cle-Session 2026-10-17, Recherche fuer den Luecken-Check ai_use_cases_overview
sprache: python
---

# web_research

## Zweck
Von der Cle-Workstation aus antworten die allgemeinen Suchdienste nicht (DuckDuckGo 202, Mojeek Captcha, GAO/USPS OIG/NHTSA 403-406, Bing RSS unbrauchbar). Die offenen Primärquellenregister antworten dagegen. Dieses Werkzeug spricht das erste davon an: die **SEC-EDGAR-Volltextsuche**, die zu jedem US-börsennotierten Emittenten die Einreichung (10-K, 10-Q, 8-K, EX-99) mit der exakten Archiv-URL liefert. Damit sind Umsatz-, Mengen- und Wortlautbelege aus dem Originaldokument erreichbar — ohne API-Schlüssel.

## Wann verwenden, wann nicht
Verwenden für Kennzahlen und Formulierungen **US-börsennotierter** Firmen (Umsatz, Segmente, Mengen, wie ein Haus seine eigene KI-Funktion nennt). Nicht verwenden für europäische, chinesische oder private Firmen — die liegen nicht in EDGAR und müssen über ihre eigenen Investor-Relations-Seiten geholt werden (siehe Eintrag `agent_tooling/findings/sec-edgar-fulltext-search-is-the-reachable-primary-source.md`). EDGAR belegt außerdem keine Produktion: eine Einreichung, die ein Merkmal nennt, ist keine Stückzahl.

## Aufruf
    python src/search_edgar.py '"automated license plate recognition"' --form 10-K -n 5
    python src/search_edgar.py '"content moderation"' --form 10-K --from 2025-06-01

Treffer werden als Firma, CIK, Formular, Einreichungsdatum und Archiv-URL ausgegeben. Dokumente mit `curl` und einem browserartigen `User-Agent` holen, nicht mit dem nackten Standard.

## Eingabe und Ausgabe
Eingabe: Suchbegriff (kurz halten, den Wortlaut des Emittenten treffen) plus optionale Filter `--form`, `--from`, `--to`, `-n`. Ausgabe: Klartextliste auf der Standardausgabe, Exit-Code 1 bei Netz- oder JSON-Fehler.

## Teststand
`python -m unittest discover -s tests` — 6 Tests, alle ohne Netz, am 2026-10-17 grün (Python 3.11.16, Cle). Live: `--form 10-K -n 3` zum Begriff der Erkennung von Kfz-Kennzeichen gab `total hits: 28` zurück, darunter Federal Signal (CIK 277509, 10-K 2009) — die Suche läuft, aber der Filter `--form 10-K` schließt EX-99-Pressemitteilungen nicht aus (das Feld trägt den Wurzeltyp).

## Grenzen
Nur US-Emittenten. Lange Anfragen mit mehreren zitierten ODER-Begriffen und einem angehängten Wort können 0 Treffer geben, obwohl die Kurzform greift — erst kurz suchen, dann mit `--form` eingrenzen. Nackter `curl`-Standard kann abgewiesen werden. Die Suche liefert Weblinks und Trefferlisten, kein Volltext-Ranking; das Dokument selbst muss gelesen werden.
