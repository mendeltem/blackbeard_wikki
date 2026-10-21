---
id: fly-connectome-topology-carries-no-advantage
typ: befund
status: getragen
thema: knowledge/neuromorphic_connectome
stand: 2026-10-21
herkunft: Cle-Arbeit, Reservoir/SNN-Linie, Gespraech mit Nutzer, 21.10.2026
verweist_auf: [fly-subgraph-is-usable-but-not-special, spike-rate-must-be-bounded-in-stdp]
---

# Das Fliegen-Konnektom traegt keinen Topologie-Vorteil, unter keiner Lernregel

## Aussage
Die biologische Verdrahtung von *Drosophila* ist ein brauchbares rekurrentes
Substrat. Sie ist aber **nicht besser** als ein Zufallsgraph gleicher Dichte.
Gemessen auf vier unabhaengigen Trainingsachsen, jeweils mit den Nullarmen
`dp` (grad-erhaltend) und `er` (Erdoes-Renyi gleicher Dichte), Klassifikation
gesprochener Ziffern (FSDD), LOSO-Ridge auf den Spikes:

| Achse | fly | dp | er | fly vs. Null |
|---|---|---|---|---|
| eingefroren (Reservoir, n=3000) | 0,5800 | 0,5820 | 0,5900 | kein Effekt |
| BPTT, nur `W_in` (n=20000, 5 Seeds) | 0,6542 | 0,6533 ± 0,0096 | 0,6517 ± 0,0033 | +0,0008 |
| BPTT, ganzes `W` (n=5000, 3 Seeds) | 0,6417 | 0,6514 ± 0,0039 | 0,6514 ± 0,0232 | −0,0097 |
| STDP, bio-lokale Regel (n=3000, 5 Seeds) | 0,5900 ± 0,0155 | 0,5917 ± 0,0137 | 0,5892 ± 0,0141 | −0,0017 / +0,0008 |

Kontrollarm ohne Netz: 0,5500.

Der Kern: **Trainieren hilft dem Netz deutlich** (0,58 → 0,65), **die
Topologie traegt aber nichts**. Und das gilt fuer den unbiologischen
Stark-Optimierer BPTT *und* fuer die rein lokale biologische Regel STDP.

## Traegt
Die Aussage, dass "das Fliegengehirn als Substrat" per se kein
Leistungsargument ist. Wer mit einem Konnektom eine Methode begruenden will,
braucht den `dp`/`er`-Nullarm, sonst misst er die Dichte, nicht die Struktur.

Auch als Fundstelle dafuer, dass zwei sehr verschiedene Trainingsverfahren
(globaler Gradient vs. lokale Spike-Timing-Regel) dasselbe Nullergebnis
liefern — der Befund ist nicht ein Artefakt eines bestimmten Lerners.

## Traegt nicht
Keine Aussage darueber, ob das Konnektom fuer *andere* Aufgaben traegt:
zeitliche Mustererkennung statt Ziffernklassifikation, Navigation, Motorik.
Keine Aussage ueber groessere Subgraphen (der BPTT-`full`-Lauf auf n=20000
kam wegen GPU-Belegung nicht zustande, siehe Bruchindikator).

Kein Beleg gegen "Neuromorphic Computing" insgesamt: gemessen ist die
Topologie als Substrat, nicht der Nutzen von Spikes, Sparsity oder
ereignisgetriebener Rechnung.

## Bruchindikator
Ein `fly`-Vorteil ausserhalb der Seed-Streuung auf einer dieser Achsen. Oder
derselbe Test auf n=20000 mit `--trainable full` — der fehlende, groessere
Lauf. Solange der nicht da ist, ist die BPTT-`full`-Zeile nur bei n=5000
belegt.

## Ablesung
Eigene Messung, 21.10.2026, GPU-LIF mit Surrogate-Gradient, `snn_fly.py` und
`stdp_fly.py`, Details in `RESULTS_neuromorphic_training.md` und
`RESULTS_reservoir.md` (Cle-Arbeit, `reservoir_fly/`). Betriebspunkt
`in_scale=10,0`, Feuerrate ~0,12, keine stillen und keine Dauerfeuer-Neuronen.

## Verknuepft
- [fly-subgraph-is-usable-but-not-special](../findings/fly-subgraph-is-usable-but-not-special.md)
- [spike-rate-must-be-bounded-in-stdp](../findings/spike-rate-must-be-bounded-in-stdp.md)
