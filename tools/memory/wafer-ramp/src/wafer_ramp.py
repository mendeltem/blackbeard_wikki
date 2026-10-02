# -*- coding: utf-8 -*-
"""Hochlauf einer Speicherfab zwischen zwei Eckpunkten, mit Erloesrechnung.

Rechnet Waferstarts je Monat zwischen einer gemeldeten Startmenge und einer
gemeldeten Zielmenge, wahlweise als logistische Kurve oder linear, und
uebersetzt sie ueber GB je Wafer und Preis je GB in einen Monatserloes.

Alle Mengen in Tausend 300-mm-Wafern je Monat, alle Erloese in Mrd. USD.
"""

import argparse
import json
import math

BASIS_GB = 2800.0   # GB je Wafer in DDR5-Aequivalent
VERSATZ = 4         # Monate zwischen Waferstart und Umsatz


def hochlauf(start, ziel, monate, form="s", k=0.9, mitte_anteil=0.55):
    """Waferstarts je Monat, einschliesslich Start- und Zielmonat.

    form "s" ist eine auf beide Eckpunkte normierte Logistik, form "linear"
    verteilt den Zuwachs gleichmaessig.
    """
    if monate < 2:
        raise ValueError("monate muss mindestens 2 sein")
    n = monate - 1
    if form == "linear":
        return [start + (ziel - start) * i / n for i in range(monate)]
    if form != "s":
        raise ValueError("form muss 's' oder 'linear' sein")
    mitte = n * mitte_anteil
    f = lambda i: 1.0 / (1.0 + math.exp(-k * (i - mitte)))
    f0, f1 = f(0), f(n)
    return [start + (ziel - start) * (f(i) - f0) / (f1 - f0) for i in range(monate)]


def gb_je_wafer(faktor, basis_gb=BASIS_GB):
    """GB Speicher je Wafer bei gegebenem Tauschverhaeltnis gegenueber DDR5."""
    if faktor <= 0:
        raise ValueError("faktor muss groesser als 0 sein")
    return basis_gb / faktor


def erloes_je_wafer(preis_je_gb, faktor, basis_gb=BASIS_GB):
    """Erloes je Wafer in USD."""
    return gb_je_wafer(faktor, basis_gb) * preis_je_gb


def monatserloes(wafer_tausend, preis_je_gb, faktor, basis_gb=BASIS_GB):
    """Erloes eines Monats in Mrd. USD aus Wafern je Monat (in Tausend)."""
    return wafer_tausend * 1000.0 * erloes_je_wafer(preis_je_gb, faktor, basis_gb) / 1e9


def verlauf(start, ziel, monate, form="s", preis_je_gb=15.0, faktor=3.0,
            basis_gb=BASIS_GB, versatz=VERSATZ, k=0.9, mitte_anteil=0.55):
    """Vollstaendige Tabelle als Liste von dicts, ein Eintrag je Monat."""
    mengen = hochlauf(start, ziel, monate, form, k, mitte_anteil)
    zeilen = []
    for i, w in enumerate(mengen):
        zeilen.append({
            "monat": i + 1,
            "wafer": w,
            "zuwachs": None if i == 0 else w - mengen[i - 1],
            "erloes_mrd": monatserloes(w, preis_je_gb, faktor, basis_gb),
            "umsatz_ab_monat": i + 1 + versatz,
        })
    return zeilen


def _text(zeilen, preis_je_gb, faktor, basis_gb):
    gb = gb_je_wafer(faktor, basis_gb)
    kopf = ("GB je Wafer %.0f, Erloes je Wafer %.0f USD bei %.2f USD/GB"
            % (gb, erloes_je_wafer(preis_je_gb, faktor, basis_gb), preis_je_gb))
    aus = [kopf, "", "Monat   Wafer   Zuwachs   Erloes   Umsatz ab"]
    for z in zeilen:
        zuw = "-" if z["zuwachs"] is None else "%.3f" % z["zuwachs"]
        aus.append("%-7d %-7.3f %-9s %-8.3f Monat %d"
                   % (z["monat"], z["wafer"], zuw, z["erloes_mrd"], z["umsatz_ab_monat"]))
    summe = sum(z["erloes_mrd"] for z in zeilen)
    aus.append("")
    aus.append("Summe aller Monatserloese: %.2f Mrd. USD" % summe)
    return "\n".join(aus)


def main(argv=None):
    p = argparse.ArgumentParser(description="Hochlauf einer Speicherfab, Wafer und Erloes je Monat.")
    p.add_argument("--start", type=float, required=True, help="Wafer je Monat in Tausend, Startmonat")
    p.add_argument("--ziel", type=float, required=True, help="Wafer je Monat in Tausend, Zielmonat")
    p.add_argument("--monate", type=int, required=True, help="Zahl der Monate einschliesslich Start und Ziel")
    p.add_argument("--form", choices=["s", "linear"], default="s")
    p.add_argument("--preis", type=float, default=15.0, help="USD je GB")
    p.add_argument("--faktor", type=float, default=3.0, help="Tauschverhaeltnis gegenueber DDR5")
    p.add_argument("--basis-gb", type=float, default=BASIS_GB, dest="basis_gb")
    p.add_argument("--versatz", type=int, default=VERSATZ, help="Monate bis zur Umsatzwirkung")
    p.add_argument("--k", type=float, default=0.9, help="Steilheit der S-Kurve")
    p.add_argument("--mitte", type=float, default=0.55, dest="mitte_anteil",
                   help="Lage des Wendepunkts als Anteil der Laufzeit")
    p.add_argument("--json", action="store_true", help="Ausgabe als JSON")
    a = p.parse_args(argv)

    zeilen = verlauf(a.start, a.ziel, a.monate, a.form, a.preis, a.faktor,
                     a.basis_gb, a.versatz, a.k, a.mitte_anteil)
    if a.json:
        print(json.dumps(zeilen, ensure_ascii=False, indent=1))
    else:
        print(_text(zeilen, a.preis, a.faktor, a.basis_gb))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
