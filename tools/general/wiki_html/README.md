---
id: wiki_html
bereich: tools/general
stand: 2026-10-11
herkunft: blackbeard_wikki, Nutzerregel 2026-10-11 (Lesen in HTML, Schreiben in Markdown)
sprache: python
---

# wiki_html

## Zweck

Erzeugt aus den Markdown-Quellen der Wiki eine verlinkte HTML-Seite für Menschen: `index.html` als Einstieg mit Suche, Kennzahlen, Aktivitätsplot, „Zuletzt geändert“ und einer Karte je Bereich; je Bereich eine Seite mit Kurzstand oben und allen Einträgen als aufklappbare Details; je Eintrag eine eigene Seite mit Metadaten, Verweisen und Rückverweisen; Werkzeuge, Protokoll, offene Punkte, Regeln. Dazu `search.js` (Suche im Browser, auch per `file://`) und `index.json` (Maschinenindex).

Markdown bleibt die Quelle. Agenten schreiben weiter Markdown mit Frontmatter; dieses Werkzeug baut die Lesefassung.

## Wann verwenden, wann nicht

Nach jedem Beitrag zur Wiki, vor dem Commit (der lokale pre-commit-Haken macht es automatisch, siehe INSTALL). Nicht verwenden, um Inhalte zu prüfen: es rendert, es bewertet nicht. Frontmatter-Fehler und tote Markdown-Links findet `wiki_maintenance --check`.

## Aufruf

```
python tools/general/wiki_html/src/wiki_html.py --root . --out docs
```

Lesen: `docs/index.html` im Browser öffnen (Doppelklick genügt) oder `python -m http.server -d docs 8769`.

## Eingabe und Ausgabe

Eingabe: die Wiki nach README-Aufbau (`knowledge/INDEX.md` mit Spalten Thema/Inhalt/Stichwörter, je Bereich `INDEX.md` und `SUMMARY.md`, Einträge `knowledge/<bereich>/<typ>/<id>.md` mit Frontmatter `id, typ, status, stand, herkunft, verweist_auf`; `tools/**/README.md`; `TODO.md`, `updates/LOG.md`, `README.md`). Git-Historie für „zuletzt geändert“ und den Aktivitätsplot (ohne Git läuft es trotzdem, dann ohne Daten).

Ausgabe unter `--out`: `index.html`, `<bereich>/index.html`, `<bereich>/<typ>/<id>.html`, `tools/**/index.html`, `rules.html`, `todo.html`, `log.html`, `search.js`, `index.json`. Relative Markdown-Links werden auf die HTML-Seiten umgeschrieben; Links auf Dateien ohne HTML-Fassung (Quelltext, Vorlagen) zeigen auf GitHub. Keine externen Abhängigkeiten im Browser, hell/dunkel nach Systemeinstellung, tauglich für das Handy.

## Teststand

2026-10-11, Ubuntu 24.04, Python 3.12, python-markdown 3.11: `python tools/general/wiki_html/tests/test_build.py` bestanden (synthetische Wiki, Seiten vorhanden, 0 tote Links). Auf der echten Wiki: 21 Bereiche, 219 Einträge, 14 Werkzeuge, 287 Seiten, 5463 interne Links, 0 tot.

## Grenzen

- Nur Einträge mit Frontmatter und Ordnerstruktur `<bereich>/<typ>/` werden als Einträge erkannt; andere Markdown-Dateien bekommen keine Seite.
- GitHub Pages ist für das private Repo im aktuellen Plan nicht verfügbar (geprüft 2026-10-11, HTTP 422). Die Seite liegt deshalb als `docs/` im Repo und wird lokal gelesen.
- Der Suchindex ist ein einfacher Teilstring-Abgleich über Titel, Inhalt, Bereich, Typ, Status.
