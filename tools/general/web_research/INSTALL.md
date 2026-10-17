# INSTALL

## Abhängigkeiten
Keine. Nur die Standardbibliothek von Python 3.8 oder neuer (`argparse`, `json`, `urllib.request`, `unittest`).

## Schritte
1. Ordner kopieren.
2. Ausführen: `python src/search_edgar.py --help`

## Geprüfte Umgebung
Agent-Workstation Cle, Linux, Python 3.11.16, 2026-10-17. Netzzugang zu `efts.sec.gov` und `www.sec.gov` nötig.

## Tests
```
cd tools/general/web_research
python -m unittest discover -s tests          # ohne Netz
```
