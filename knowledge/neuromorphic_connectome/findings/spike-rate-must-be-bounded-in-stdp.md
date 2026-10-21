---
id: spike-rate-must-be-bounded-in-stdp
typ: regel
status: getragen
thema: knowledge/neuromorphic_connectome
stand: 2026-10-21
herkunft: Cle-Arbeit, STDP-Lauf, Gespraech mit Nutzer, 21.10.2026
verweist_auf: [fly-connectome-topology-carries-no-advantage]
---

# In STDP muessen Rate und Gewichtsschritt begrenzt sein, sonst saettigt der Clamp

## Aussage
Ein erster STDP-Lauf auf dem Fliegen-Subgraph verschob die Gewichte in **einer**
Epoche um 235 % ihrer Skala (`w_drift = 2,35`): die reine Pair-Regel
`dW = A⁺·(sᵀx) − A⁻·(yᵀs)` ist ueber eine Batch von 16 Clips so gross, dass
alle Synapsen am `w_max`-Clamp kleben. Damit werden **alle Arme dieselbe
gesaettigte Matrix** — der Vergleich `fly` vs. Zufallsgraph ist dann still
wertlos, ohne dass eine Fehlermeldung erscheint.

Zweiter Fehler im selben Lauf: die Feuerrate war nicht durch die Batchgroesse
geteilt worden (3,83 statt 0,125). Auch das faellt nicht auf, solange man nur
die Genauigkeit ansieht.

Beides behoben durch: `--w-lr` begrenzt den RMS-Schritt pro Batch auf einen
Bruchteil des aktuellen RMS-Gewichts, und die Rate wird durch `T·B` geteilt.
Danach: Rate 0,124, Saettigung **0,000**, Genauigkeit in 96 s gemessen.

## Traegt
Jeden STDP- oder Hebb-Lauf mit Clamp. Zu jedem Lauf gehoeren drei Zahlen,
nicht eine: Genauigkeit, Rate, Saettigungsanteil (`sat` = Anteil der Gewichte
am Clamp). Ein `sat > 0` heisst, das Ergebnis ist ein Artefakt der Grenze.

Auch allgemeiner: eine Regel, die die Gewichte unbegrenzt verschiebt, zerstoert
genau die Struktur, die man mit einem Konnektom testen wollte.

## Traegt nicht
Kein Beleg, dass STDP generell nicht funktioniert. Der Nullbefund bleibt auch
mit gebremstem STDP bestehen (fly 0,5900 vs. dp 0,5917), aber er ist erst mit
`sat = 0` ein echter Befund.

## Bruchindikator
`sat` deutlich groesser als 0, oder `w_drift` in der Groessenordnung 1 oder
hoeher pro Epoche. Dann erst Lernrate senken, dann messen.

## Ablesung
Eigene Messung, 21.10.2026, `stdp_fly.py --w-lr 0.02`, n=3000, 5 Seeds,
5 Epochen. Der erste fehlerhafte Wert `w_drift = 2,35` steht so im
Entwicklungsverlauf und ist hier bewusst als Fehlwert dokumentiert.

## Verknuepft
- [fly-connectome-topology-carries-no-advantage](fly-connectome-topology-carries-no-advantage.md)
