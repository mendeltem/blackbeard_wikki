# wafer-ramp

Rechnet den Hochlauf einer Fab zwischen zwei genannten Eckpunkten (Startmenge, Zielmenge, Zahl der Monate) und uebersetzt die Waferstarts in Erloes je Monat.

## Wann verwenden
- Eine Firma nennt nur Anfangs- und Endmenge eines Werks, der Monatsverlauf fehlt. Beispiel: SK Hynix M15X, 10k Wafer im Februar 2026, 55k bis 60k zum Jahresende.
- Es soll gezeigt werden, in welchem Monat der Zuwachs am groessten ist und wann er als Umsatz ankommt.

## Wann nicht verwenden
- Als Prognose. Die Kurvenform ist eine Annahme, keine Meldung. Das Werkzeug gibt nur zwei Formen her: S-Kurve und linear.
- Fuer Bits. Gerechnet wird in Waferstarts; die Umrechnung auf GB benutzt ein pauschales Tauschverhaeltnis gegenueber DDR5 und keine Ausbeutekurve.
- Fuer Gewinn. Herauskommt Erloes, nicht Marge.

## Beispielaufruf

    python src/wafer_ramp.py --start 10 --ziel 57.5 --monate 11 --form s --preis 15 --faktor 3

Ausgabe (gekuerzt), Mengen in Tausend Wafern je Monat, Erloes in Mrd. USD je Monat:

    Monat   Wafer   Zuwachs   Erloes   Umsatz ab
    1       10.000  -         0.140    Monat 5
    6       28.610  8.932     0.401    Monat 10
    7       39.381  10.771    0.551    Monat 11
    11      57.500  1.167     0.805    Monat 15

## Eingabe
- `--start`, `--ziel`: Wafer je Monat in Tausend, Eckpunkte wie gemeldet.
- `--monate`: Zahl der Monate einschliesslich Start- und Zielmonat.
- `--form`: `s` (logistisch) oder `linear`.
- `--preis`: USD je GB fuer das gefertigte Produkt.
- `--faktor`: Tauschverhaeltnis gegenueber DDR5 (HBM3E rund 3, HBM4 rund 4).
- `--basis-gb`: GB je Wafer in DDR5-Aequivalent, Standard 2800.
- `--versatz`: Monate zwischen Waferstart und Umsatz, Standard 4.

## Ausgabe
Je Monat: Wafer je Monat, Zuwachs gegenueber Vormonat, Erloes je Monat in Mrd. USD, Monat der Umsatzwirkung. Als Text oder mit `--json` als JSON.

## Annahmen, die im Ergebnis stecken
- GB je Wafer = `basis_gb / faktor`. Bei 2800 und Faktor 3 sind das 933 GB, rund 26 Stapel zu 36 GB.
- Die S-Kurve ist eine Logistik mit Steilheit k = 0,9 und Mitte bei 55 Prozent der Laufzeit, beides ueber Parameter aenderbar. Sie ist auf die Eckpunkte normiert, trifft Start und Ziel also exakt.
- Der Umsatzversatz von vier Monaten ist eine Faustzahl fuer Fertigung, Stapeln, Test und Auslieferung.

## Test
`python -m unittest discover -s tests -v`, ausgefuehrt am 2026-10-02 unter Python 3.13.14 (Windows 10), 7 Tests, bestanden.
