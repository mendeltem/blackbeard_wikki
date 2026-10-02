# Installation

## Geprüfte Umgebung
Windows 10, Python 3.13, keine GPU. Erwartet lauffähig ab Python 3.8 auf jedem Betriebssystem.

## Abhängigkeiten
Keine außerhalb der Standardbibliothek (`argparse`, `json`, `re`, `io`, `sys`).

## Schritte
1. Ordner `src/` kopieren oder das Repo klonen.
2. `python src/js_literal_to_json.py --help`
3. Test: `python tests/test_js_literal_to_json.py` (gibt `OK` aus und endet mit Code 0).
