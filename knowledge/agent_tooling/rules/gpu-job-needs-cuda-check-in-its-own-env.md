---
id: gpu-job-needs-cuda-check-in-its-own-env
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-08
herkunft: PVS-Arena Alita, GPU-Warteschlange 2026-10-08 01:35-03:05 (drei Fehlversuche in Folge)
verweist_auf: [never-edit-a-running-bash-script, tests-prove-claims-not-plumbing, release-test-means-fresh-machine-with-release-assets]
---

# Vor dem Einreihen eines GPU-Auftrags: in GENAU dieser Umgebung CUDA, Importe und einen Mini-Lauf pruefen

## Aussage
Drei GPU-Auftraege scheiterten nacheinander an Dingen, die ein 30-Sekunden-Test vorher gezeigt haette: (1) das conda-torch
der frisch gebauten Umgebung war ein CPU-Build; der Auftrag lief 80 Minuten auf der CPU, hielt die GPU-Sperre und liess den
Modellserver des lokalen Agenten entladen -- der Agent stand. Der vorherige Rauchtest war absichtlich mit
CUDA_VISIBLE_DEVICES="" gelaufen und hat das verdeckt. (2) nnU-Net v1 importiert matplotlib im Trainer-Modul; das Paket fehlte,
Abbruch nach einer Sekunde. (3) torch 2.2 mit numpy 2.x gibt nur eine Warnung, scheitert aber beim ersten Tensor-Transfer.
Vorschrift vor `grossauftrag --einreihen`: in der Zielumgebung `python -c "import torch; assert torch.cuda.is_available()"`,
den vollstaendigen Import des Inferenz-Einstiegs (nicht nur des Pakets) und einen Mini-Lauf mit EINEM Fall MIT GPU.
Zusaetzlich: pkill-Muster duerfen nicht woertlich in demselben Kommando vorkommen, sonst trifft pkill die eigene Shell
(dreimal passiert; Bracket-Trick `pr[e]dict` hilft nur, wenn das Wort sonst nirgends im Kommando steht).

## Traegt
Jede Warteschlange, die eine knappe Ressource exklusiv vergibt (GPU-Sperre, die den Modellserver entlaedt): ein fehlerhafter
Auftrag kostet dort nicht nur seine Laufzeit, sondern blockiert alle anderen.

## Traegt nicht
Umgebungen, die bereits mit einem Mini-Lauf auf der GPU abgenommen sind.

## Bruchindikator
Keiner; die Regel ist eine Vorbedingung.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/mednet-t1-t050/predict_cpu_fehlversuch_0135.log ("CUDA is not available"),
pingu-t1-t050/predict_fehlversuch_matplotlib.log, ARBEIT.md 02:20-03:05.

## Verknuepft
- [never-edit-a-running-bash-script](never-edit-a-running-bash-script.md)
- [tests-prove-claims-not-plumbing](tests-prove-claims-not-plumbing.md)
- [release-test-means-fresh-machine-with-release-assets](release-test-means-fresh-machine-with-release-assets.md)
