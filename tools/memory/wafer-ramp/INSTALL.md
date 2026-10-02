# Installation

## Abhaengigkeiten
Keine. Nur die Standardbibliothek.

## Geprueft mit
- Python 3.13.14, Windows 10, 2026-10-02.
- Erwartet laufffaehig ab Python 3.8 (nur `math`, `argparse`, `json`, `unittest`).

## Schritte

    git clone https://github.com/mendeltem/blackbeard_wikki.git
    cd blackbeard_wikki/tools/memory/wafer-ramp
    python src/wafer_ramp.py --start 10 --ziel 57.5 --monate 11

## Tests

    cd blackbeard_wikki/tools/memory/wafer-ramp
    python -m unittest discover -s tests -v

Die Tests brauchen keine privaten Daten; alle Werte sind im Test selbst gesetzt.
