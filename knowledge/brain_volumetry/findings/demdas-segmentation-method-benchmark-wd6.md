---
id: demdas-segmentation-method-benchmark-wd6
typ: befund
status: getragen
thema: knowledge/brain_volumetry
stand: 2026-10-13
herkunft: wd6 DEMDAS segmentation benchmark, 13.10.2026 (Alita)
verweist_auf: [synthseg-in-freesurfer-8-runs-on-cpu-only]
---

# DEMDAS segmentation-method benchmark (wd6): measured-evidence table, 5 methods

## Aussage
Fünf Segmentationsmethoden werden auf dem DEMDAS-Benchmark-Set mit gemessenen
Werten verglichen (keine Empfehlung in der Tabelle; die Methodenauswahl für die
ganze Kohorte trifft der Gutachter/Nutzer). Set A = 64 Sessions (bids/demdas,
GM-Beispiel, FreeSurfer 8.2 recon-all als Referenz), Set B = 40 gleiche Sessions
mit run-1 UND run-2 T1w (echter Test-Retest, Primärkriterium).

Stand dieser Auswertung (nur Kohorten-/Aggregatzahlen, keine Patientendaten):
- Übereinstimmung mit FreeSurfer 8.2 aseg auf Set A (synthseg_robust, Dice,
  n=61): cortex GM 0.78, GM total 0.80, WM 0.89, CSF/Ventrikel 0.78,
  Hippocampus 0.88, Amygdala 0.89, Thalamus 0.91.
- Laufzeit pro Fall (Median): synthseg_robust 22 s, synthseg_fast 145 s,
  fastsurfer_cnn 378 s (CPU, 6 Threads).
- Test-Retest (ICC(2,1) / SDC95) auf Set B wird erst auswertbar, wenn die
  overnight-CPU-Läufe (synthseg_fast, fastsurfer_cnn) run-1 und run-2 für
  mindestens eine ausreichende Zahl von Paaren fertig haben; danach ein
  erneutes Ausführen von benchmark.py füllt die Zeilen.

## Traegt
Die Wahl der Segmentationsmethode für die DEMDAS-Gesamtkohorte: die Tabelle
mit Rängen 1..N und Mittelrank (benchmark.csv / benchmark.html) ist die
messbasierte Grundlage; ICC/SDC95 (Primärkriterium) ist der entscheidende
Satz, sobald Set B vollständig ist.
