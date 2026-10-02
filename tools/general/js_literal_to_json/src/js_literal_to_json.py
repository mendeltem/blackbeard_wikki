# -*- coding: utf-8 -*-
"""Zieht `const NAME = <Literal>;` aus einer HTML- oder JS-Datei und gibt JSON aus.

    python js_literal_to_json.py index.html --const MENGE --const UMSATZ --out daten.json
    python js_literal_to_json.py index.html --list

Nur Literale (Objekte, Arrays, Zeichenketten, Zahlen, true, false, null),
keine Ausdruecke. Kommentare, blanke Schluessel, einfache Anfuehrungszeichen
und nachlaufende Kommata werden ausserhalb von Zeichenketten umgesetzt;
Zeichenketten bleiben unangetastet.
"""
import argparse
import io
import json
import re
import sys

_CONST = re.compile(r"^const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*", re.M)


def list_consts(text):
    """Namen aller `const NAME =` am Zeilenanfang, in Reihenfolge."""
    return [m.group(1) for m in _CONST.finditer(text)]


def _string_end(text, i):
    """Index des schliessenden Anfuehrungszeichens der Zeichenkette, die bei i beginnt."""
    q = text[i]
    j = i + 1
    while j < len(text) and text[j] != q:
        j += 2 if text[j] == "\\" else 1
    if j >= len(text):
        raise ValueError("Zeichenkette nicht geschlossen ab Position %d" % i)
    return j


def extract_literal(text, name):
    """Das Literal hinter `const NAME =`, klammernzaehlend, mit Ruecksicht auf
    Zeichenketten und Kommentare. Mehrfachdefinition: die erste gewinnt."""
    m = re.search(r"^const\s+%s\s*=\s*" % re.escape(name), text, re.M)
    if not m:
        raise KeyError("Konstante nicht gefunden: " + name)
    i = m.end()
    if i >= len(text):
        raise ValueError("Literal fehlt hinter " + name)
    if text[i] in "\"'":
        return text[i:_string_end(text, i) + 1]
    if text[i] not in "[{":
        # Zahl, true, false, null: bis zum Semikolon oder Zeilenende
        k = i
        while k < len(text) and text[k] not in ";\n":
            k += 1
        return text[i:k].strip()
    tiefe, j = 0, i
    while j < len(text):
        c = text[j]
        if c in "\"'":
            j = _string_end(text, j) + 1
            continue
        if text.startswith("/*", j):
            k = text.find("*/", j + 2)
            j = len(text) if k < 0 else k + 2
            continue
        if text.startswith("//", j):
            k = text.find("\n", j)
            j = len(text) if k < 0 else k
            continue
        if c in "[{":
            tiefe += 1
        elif c in "]}":
            tiefe -= 1
            if tiefe == 0:
                return text[i:j + 1]
        j += 1
    raise ValueError("Literal nicht geschlossen: " + name)


def to_json_text(lit):
    """JS-Literal -> JSON-Text. Ein Durchlauf; alles ausserhalb von Zeichenketten."""
    out = []
    i, n = 0, len(lit)

    def prev_sig():
        for ch in reversed(out):
            if not ch.isspace():
                return ch
        return ""

    while i < n:
        c = lit[i]
        if c in "\"'":
            j = _string_end(lit, i)
            s = lit[i + 1:j]
            if c == "'":
                s = s.replace("\\'", "'").replace('"', '\\"')
            out.append('"' + s + '"')
            i = j + 1
            continue
        if lit.startswith("/*", i):
            k = lit.find("*/", i + 2)
            i = n if k < 0 else k + 2
            continue
        if lit.startswith("//", i):
            k = lit.find("\n", i)
            i = n if k < 0 else k
            continue
        if c in "}]":
            k = len(out) - 1
            while k >= 0 and out[k].isspace():
                k -= 1
            if k >= 0 and out[k] == ",":
                del out[k:]
            out.append(c)
            i += 1
            continue
        if (c.isalpha() or c == "_") and prev_sig() in ("{", ","):
            j = i
            while j < n and (lit[j].isalnum() or lit[j] == "_"):
                j += 1
            k = j
            while k < n and lit[k].isspace():
                k += 1
            if k < n and lit[k] == ":":
                out.append('"' + lit[i:j] + '"')
                i = j
                continue
        out.append(c)
        i += 1
    return "".join(out)


def to_json(lit):
    """JS-Literal -> Python-Wert (ueber JSON)."""
    return json.loads(to_json_text(lit))


def extract(text, names):
    """{name: Wert} fuer alle gewuenschten Konstanten."""
    return {name: to_json(extract_literal(text, name)) for name in names}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("datei", help="HTML- oder JS-Datei, UTF-8")
    p.add_argument("--const", action="append", default=[], metavar="NAME",
                   help="zu extrahierende Konstante; mehrfach erlaubt")
    p.add_argument("--list", action="store_true", help="nur die gefundenen Konstantennamen ausgeben")
    p.add_argument("--out", metavar="DATEI", help="Zieldatei; sonst Standardausgabe")
    a = p.parse_args(argv)

    text = io.open(a.datei, encoding="utf-8").read()
    if a.list:
        for name in list_consts(text):
            print(name)
        return 0
    if not a.const:
        p.error("mindestens ein --const NAME, oder --list")
    try:
        ergebnis = extract(text, a.const)
    except (KeyError, ValueError, json.JSONDecodeError) as e:
        sys.stderr.write("Fehler: %s\n" % e)
        return 1
    js = json.dumps(ergebnis, ensure_ascii=False, indent=1) + "\n"
    if a.out:
        io.open(a.out, "w", encoding="utf-8").write(js)
        sys.stderr.write("%s geschrieben: %d Konstanten\n" % (a.out, len(ergebnis)))
    else:
        sys.stdout.write(js)
    return 0


if __name__ == "__main__":
    sys.exit(main())
