---
id: no-silent-fallback-values
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-02
herkunft: Projekt local_models, Codepruefung 2026-08-29
verweist_auf: [empty-is-not-missing]
---

# Kein Rueckfallwert ohne eine Zeile, die ihn als solchen benennt

## Aussage
Wo eine Messung fehlt, schreibt Code einen plausiblen Ersatzwert hin, statt zu
sagen, dass er es nicht weiss. Die Ausgabe sieht danach wie eine Messung aus,
und deshalb merkt niemand, wann sie nicht mehr gilt.

Eine Pruefung von 32 bestaetigten Befunden in einem Messwerkzeug fand sieben
Faelle mit derselben Ursache:

    head_dim = (n_emb // n_head) if n_head else 128      geraten, obwohl die
                                                         Datei den Wert mitbringt
    fits = int(usable // layer_mib) if layer_mib > 0 else 0
                                                         Division-durch-null-
                                                         Rueckfall, der sich als
                                                         Messergebnis liest
    "ram_gb": round(host["ram_gb"] or 0, 1)              eine erfundene Null im
                                                         Messprotokoll
    "ngl": 99  neben  "gpu": "keine"                     Konstante neben der
                                                         Feststellung, dass es
                                                         keine GPU gibt

Keiner dieser Faelle ist Absicht. Sie entstehen, weil `or 0`, `else 0` und
`else 128` billiger zu tippen sind als eine Fallunterscheidung.

Die Regel raeumt alle sieben mit einem Satz ab: **jeder Rueckfallwert bekommt
eine Zeile auf stderr, die ihn benennt.** Dann bleibt die Ausgabe benutzbar, und
der Leser weiss, welcher Teil gemessen ist.

## Traegt
Jedes Werkzeug, dessen Ausgabe als Grundlage fuer eine Entscheidung dient --
Kapazitaetsrechner, Vorbedingungspruefer, Statusberichte, Messprotokolle.
Besonders dort, wo die Ausgabe spaeter zitiert wird: eine Zahl in einer
Dokumentation, die aus einem Rueckfallwert stammt, ist nicht mehr von einer
Messung zu unterscheiden.

## Traegt nicht
Verzicht auf Rueckfallwerte. Ein Werkzeug, das bei jeder fehlenden Angabe
abbricht, ist unbenutzbar. Es geht um die Kennzeichnung, nicht um den Verzicht.

Auch nicht: Rueckfallwerte in reinen Rechenhilfen ohne Aussenwirkung.

## Bruchindikator
Eine Zahl in einer Dokumentation, zu der niemand mehr sagen kann, ob sie
gemessen oder gerechnet ist. Im geprueften Fall stand eine KV-Cache-Groesse
unter der Ueberschrift "Gemessen auf dem Referenzsystem" -- sie war die Ausgabe
einer Formel mit einem geratenen Eingabewert.

Zweiter Indikator: ein `or 0`, `else 0` oder ein Zahlenliteral im Code, das
neben einer Feststellung steht, dass etwas fehlt.

## Ablesung
Eigene Codepruefung, 32 bestaetigte Befunde ueber sechs Dimensionen, davon
sieben mit dieser gemeinsamen Ursache. Keine fremde Quelle.

Unabhängig bestätigt im Projekt rea (morluto/rea, docs/provider-evaluation.md, 2026-10-05): ein Analyse-Provider bleibt für die Lebensdauer eines Ziels gebunden, "never fail over silently between Hopper and Ghidra". Siehe [agent-tools-by-task-shape](agent-tools-by-task-shape.md).

## Verknuepft
- [empty-is-not-missing](empty-is-not-missing.md)
- [agent-tools-by-task-shape](agent-tools-by-task-shape.md)
