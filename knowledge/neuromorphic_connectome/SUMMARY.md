# neuromorphic_connectome: Kurzstand

Ob ein echtes Konnektom als rekurrentes Substrat mehr traegt als ein
Zufallsgraph gleicher Dichte. Nur oeffentliche Daten: FlyWire-abgeleitete
`fly783.csr` (138.639 Neuronen, 15.091.983 Kanten) und FSDD.

**Befund, neu 2026-10-21 (eigene Messung, vier Achsen, je mit Nullarmen):** Die
biologische Verdrahtung traegt **keinen** Vorteil. Eingefrorenes Reservoir
fly 0,5800 gegen dp 0,5820 / er 0,5900; BPTT nur `W_in` fly 0,6542 gegen
dp 0,6533 ± 0,0096; BPTT ganzes `W` fly 0,6417 gegen dp 0,6514 ± 0,0039;
STDP (bio-lokal) fly 0,5900 ± 0,0155 gegen dp 0,5917 ± 0,0137. Kontrolle ohne
Netz 0,5500. Trainieren hilft deutlich (0,58 → 0,65), die Topologie nicht —
und zwar unter dem globalen Gradienten *und* unter der lokalen
Spike-Timing-Regel ([fly-connectome-topology-carries-no-advantage](findings/fly-connectome-topology-carries-no-advantage.md)).

**Regel, neu 2026-10-21 (eigener Fehllauf):** In STDP muessen Rate und
Gewichtsschritt begrenzt sein. Ein erster Lauf verschob die Gewichte um 235 %
ihrer Skala in einer Epoche; alle Synapsen sassen am Clamp und **alle Arme
wurden still dieselbe gesaettigte Matrix**, ohne Fehlermeldung. Zu jedem Lauf
gehoeren drei Zahlen: Genauigkeit, Rate, Saettigungsanteil
([spike-rate-must-be-bounded-in-stdp](findings/spike-rate-must-be-bounded-in-stdp.md)).

**Befund, neu 2026-10-21 (Datenherkunft):** `fly783.csr` hat **keine
anatomischen 3D-Koordinaten**. Raeumliche Aussagen brauchen den Atlas oder die
Rohdaten. Nutzbar ist die Datei als Testumgebung fuer Sparsity und lokale
Lernregeln, nicht als Leistungsargument
([fly-subgraph-is-usable-but-not-special](findings/fly-subgraph-is-usable-but-not-special.md)).

**Offen:** BPTT `--trainable full` auf n=20000 (der Lauf auf n=5000 kam wegen
GPU-Belegung zustande, siehe `local_llm_operation`). Ereignisgetriebener
Kernel statt fester Zeitschritte — das ist der Test, bei dem die Biologie
auszahlen koennte, und der einzige Punkt auf der Liste mit neuer Aussage.
`sum(exp)`-Spike-Dump und Video. STDP-Hyperparameter-Sweep aendert
voraussichtlich nichts am Topologie-Befund, weil beide Nullen gleich
behandelt werden.

Details in [INDEX.md](INDEX.md), Stand 2026-10-21.
