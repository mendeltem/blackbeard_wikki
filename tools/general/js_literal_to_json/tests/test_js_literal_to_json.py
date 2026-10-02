# -*- coding: utf-8 -*-
"""Synthetischer Test fuer js_literal_to_json. Keine privaten Daten."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import js_literal_to_json as t  # noqa: E402

PROBE = u'''<!doctype html>
<script>
/* Kommentar mit { geschweiften } Klammern und "Anfuehrungszeichen" */
const STAND = "2026-10-02";
const ZAHL = 4.0e12;
const MENGE = [
  {datum:"2025-05-20", anbieter:"Google", wert:480e12, art:'vom unternehmen genannt',
   notiz:"Text mit // Schraegstrichen, mit /* Klammern */ und mit , key: Muster", geprueft:false},
  // Zeilenkommentar, der ignoriert wird
  {datum:"2025-07-23", anbieter:'O\\'Reilly "Zitat"', wert:980e12, leer:null, ok:true, },
];
const TIEF = {a:{b:{c:[1, 2, {d:"ü ß 漢字"}]}}, grossBuchstaben_Ok:1, _unterstrich:2};
function nichtErfasst(){ return {x:1}; }
</script>
'''


def test_list():
    assert t.list_consts(PROBE) == ["STAND", "ZAHL", "MENGE", "TIEF"]


def test_string_and_number():
    assert t.to_json(t.extract_literal(PROBE, "STAND")) == "2026-10-02"
    assert t.to_json(t.extract_literal(PROBE, "ZAHL")) == 4.0e12


def test_array_with_comments_keys_and_trailing_comma():
    m = t.to_json(t.extract_literal(PROBE, "MENGE"))
    assert len(m) == 2
    assert m[0]["art"] == "vom unternehmen genannt"
    assert m[0]["geprueft"] is False
    # Schluesselmuster innerhalb der Zeichenkette bleibt unangetastet
    assert m[0]["notiz"] == "Text mit // Schraegstrichen, mit /* Klammern */ und mit , key: Muster"
    assert m[1]["anbieter"] == "O'Reilly \"Zitat\""
    assert m[1]["leer"] is None and m[1]["ok"] is True


def test_nested_and_unicode():
    d = t.to_json(t.extract_literal(PROBE, "TIEF"))
    assert d["a"]["b"]["c"][2]["d"] == u"ü ß 漢字"
    assert d["grossBuchstaben_Ok"] == 1 and d["_unterstrich"] == 2


def test_missing_const():
    try:
        t.extract_literal(PROBE, "GIBT_ES_NICHT")
    except KeyError:
        return
    raise AssertionError("KeyError erwartet")


def test_cli_roundtrip(tmp_path=None):
    import io
    import json
    import tempfile
    d = tmp_path or tempfile.mkdtemp()
    quelle = os.path.join(str(d), "probe.html")
    ziel = os.path.join(str(d), "aus.json")
    io.open(quelle, "w", encoding="utf-8").write(PROBE)
    rc = t.main([quelle, "--const", "MENGE", "--const", "TIEF", "--out", ziel])
    assert rc == 0
    aus = json.load(io.open(ziel, encoding="utf-8"))
    assert set(aus) == {"MENGE", "TIEF"}
    assert aus["MENGE"][1]["wert"] == 980e12


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok ", name)
    print("OK")
