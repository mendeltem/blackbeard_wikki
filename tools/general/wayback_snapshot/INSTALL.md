# INSTALL

## Abhängigkeiten
Keine. Nur die Standardbibliothek von Python 3.8 oder neuer (`argparse`, `json`, `re`, `urllib.request`, `unittest`).

## Schritte
1. Ordner kopieren.
2. Ausführen: `python src/wayback_snapshot.py --help`

## Geprüfte Umgebung
Windows 10, Python 3.13.3, 2026-10-02. Netzzugang zu `archive.org` und `web.archive.org` nötig.

## Tests
```
cd tools/general/wayback_snapshot
python -m unittest discover -s tests          # ohne Netz, 1 Test wird übersprungen
WAYBACK_NETZ=1 python -m unittest discover -s tests   # mit Netz
```
