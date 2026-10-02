---
name: bianca-flair-wmh
description: WMH-Segmentierung auf FLAIR mit FSL BIANCA und vortrainiertem Klassifikator. Preprocessing (HD-BET, FAST, SynthSeg, SynthSR, FLIRT), Inferenz, Postprocessing (Schwelle, WM-Masking, periventrikulär/tief), QC. Verwenden, wenn WMH-Volumina aus FLAIR-Daten in BIDS gerechnet oder ein Methodenteil dazu geschrieben werden soll.
---

# WMH-Segmentierung auf FLAIR mit BIANCA

So rechnet Mendel WMH. Der Ablauf ist aus dem Code des Projekts BIANCA Inference abgeschrieben, nicht aus der Literatur. Die Befehle unten stehen so im Code; in dieser Wiki-Umgebung gelaufen ist nur der Rechenkern des Postprocessings (`wmh_post.py`, siehe README).

## Wann anwenden, wann nicht

Anwenden: FLAIR je Subject vorhanden, BIDS-artiger Baum, ein vortrainierter BIANCA-Klassifikator liegt vor, gewünscht sind WMH-Volumen gesamt, periventrikulär und tief.

Nicht anwenden:
- Kein FLAIR. Der Klassifikator ist FLAIR-basiert, Subjects mit T2w als einzigem fluid-sensitiven Bild fallen raus. Ausnahme: eine als T2w benannte Datei, die laut JSON-Sidecar eine dark-fluid-FLAIR ist (`ScanningSequence` enthält IR oder `SeriesDescription` enthält dark-fluid/flair).
- Kein Klassifikator. Training ist nicht Teil dieses Ablaufs.
- Gesucht sind Läsionszahlen oder Clustergrößen. Die gibt es hier bewusst nicht.

## Eingaben

- FLAIR je Subject (Pflicht), natives T1w (optional), Infarktmaske im FLAIR-Raum (optional).
- MNI152 T1 1 mm, hirnextrahiert.
- BIANCA-Klassifikator, gespeichert mit `--saveclassifierdata`. Der hier benutzte (Tag 201) wurde auf 201 manuell segmentierten FLAIR/T1-Paaren trainiert, davon 60 aus dem öffentlichen Trainingssatz der MICCAI WMH Challenge 2017, der Rest aus internen Kohorten. Er liegt nicht in dieser Wiki.
- Software: FSL 6.0.7.18 (bianca, fast, flirt, fslmaths, bet), FreeSurfer ab 7.2 (mri_synthseg, mri_synthsr, mri_synthstrip), HD-BET, Python mit nibabel, numpy, scipy, pandas.

## Ablauf

Alles wird im nativen FLAIR-Raum gerechnet und gemessen. Die MNI-Registrierung liefert BIANCA nur die Ortsinformation, kein Bild wird für die Messung umgerechnet.

### Stufe 1: Preprocessing

1. Hirnextraktion der FLAIR: `hd-bet -i FLAIR -o FLAIR_brain -device cpu --disable_tta`. Bei Fehlschlag `bet FLAIR FLAIR_brain -R -f 0.3 -m`, dann `mri_synthstrip -i FLAIR -o FLAIR_brain -m brainmask`. Festhalten, welches Werkzeug griff, es gehört ins Paper.
2. Bias-Korrektur: `fast -B -o <base> FLAIR_brain`, das `_restore`-Bild ist BIANCA-Feature 1.
3. Gewebe: `mri_synthseg --i FLAIR --o synthseg.nii.gz --threads 8 --robust`. Ergebnis liegt im isotropen 1-mm-Gitter. Daraus Masken: WM = Label 2, 41, 77; Ventrikel = 4, 43, 5, 44, 14, 15.
4. Distanzkarte: euklidische Distanztransformation außerhalb der Ventrikelmaske, in mm, gerechnet im 1-mm-Gitter.
5. T1 im FLAIR-Raum, BIANCA-Feature 2:
   - natives T1w vorhanden: `flirt -in T1w -ref FLAIR -out T1_inFLAIR -dof 6 -cost corratio -interp spline`
   - sonst: `mri_synthsr --i FLAIR --o T1_1mm --threads 8`, dann `flirt -in T1_1mm -ref FLAIR -out T1_inFLAIR -applyxfm -usesqform -interp spline`
   - danach `fslmaths T1_inFLAIR -mas brainmask T1_brain` und `fast -B`.
6. Ortsfeature: `flirt -in FLAIR_biascorr -ref MNI152_T1_1mm_brain -out FLAIR_mni -omat FLAIR_to-MNI.mat -dof 12`.
7. Leeres Label-NIfTI im FLAIR-Gitter als Platzhalter für das Masterfile.

### Stufe 2: BIANCA

Masterfile mit einer Zeile je Subject: `FLAIR_biascorr T1_biascorr FLAIR_to-MNI.mat label_empty`.

```
bianca --singlefile=<masterfile> --brainmaskfeaturenum=1 --querysubjectnum=1 \
       --featuresubset=1,2 --matfeaturenum=3 --spatialweight=2 \
       --loadclassifierdata=<modell> -o <sub>_LPM.nii.gz -v
```

Ausgabe ist nur die Wahrscheinlichkeitskarte (LPM). Hier wird nichts geschwellt.

### Stufe 3: Postprocessing

Rechenkern: `wmh_post.postprocess()` in diesem Ordner.

1. WM-Maske, Ventrikelmaske und Distanzkarte vom 1-mm-Gitter auf das LPM-Gitter legen, über Weltkoordinaten. Masken nearest neighbour, Distanzkarte trilinear.
2. Falls Infarktmaske vorhanden und gewünscht: um 1 Voxel dilatieren (26er-Nachbarschaft), LPM dort auf 0.
3. Schwelle 0.90 auf der LPM. Für Sensitivität parallel 0.85; beide Sätze nebeneinander ablegen (`thr090`, `thr085`).
4. Mit der WM-Maske schneiden. Das ist das berichtete Ergebnis.
5. Periventrikulär: Distanz zur Ventrikelmaske höchstens 10 mm. Tief: der Rest. PV + tief ergibt exakt das WM-maskierte Volumen.
6. Volumen in ml: Voxelzahl mal Voxelvolumen des FLAIR-Gitters durch 1000.
7. Hirnvolumen als Bezugsgröße: alle SynthSeg-Label außer Hintergrund und extrazerebralem CSF (24), gezählt im 1-mm-Gitter. Ventrikel sind drin, entspricht BrainSegVol.

Keine Cluster-Verarbeitung: nichts wird nach Größe verworfen, nichts gezählt.

### QC

Jedes Subject wird angesehen. Axiale Mosaike der bias-korrigierten FLAIR, nur Schichten mit WM-Maske, links ohne Overlay, rechts PV (rot) und tief (cyan), umschaltbar zwischen den Schwellen. Als eine HTML-Datei mit eingebetteten Bildern, ohne Server. Korrekturen laufen über einen Editor, der geänderte Voxel als JSON ausgibt; ein zweiter Schritt schreibt daraus korrigierte Masken in einen eigenen Ordner. Originale werden nie überschrieben.

## Setzungen

Diese Werte sind Konvention, nicht hergeleitet. Sie gehören in jede Ergebniszeile und in den Methodenteil.

| Größe | Wert | Quelle |
|---|---|---|
| Schwelle auf der LPM | 0.90, parallel 0.85 | Griffanti 2016, gilt nur bei vergleichbarer Trainingskonfiguration |
| PV-Grenze | 10 mm zur Ventrikelmaske | Griffanti 2018, DeCarli 2005 |
| spatialweight | 2 | muss dem Training entsprechen |
| Clusterfilter | keiner | Setzung |
| Messraum | nativer FLAIR-Raum | Setzung |

## Fallen

Jede davon ist im Projekt aufgetreten.

- WM-Maske aus FAST-PVE statt aus SynthSeg: deckte periventrikuläre und juxtakortikale WM zu wenig ab und entfernte einen großen Teil des WMH-Volumens. Deshalb SynthSeg. Zahlen dazu liegen hier nicht vor.
- Masken im 1-mm-Gitter direkt auf die FLAIR angewendet, ohne Resampling über Weltkoordinaten: Overlays verschwinden, Masking greift ins Leere.
- Distanztransformation auf dem FLAIR-Gitter: bei 3 bis 5 mm Schichtdicke in z so grob wie die Schicht. Im isotropen Gitter rechnen, danach resampeln.
- Leere Ventrikelmaske: dann gibt es keine PV/tief-Aufteilung. Nicht mit einem Ersatzwert füllen, sondern leer lassen und melden.
- spatialweight bei Training und Inferenz verschieden: `--saveclassifierdata` speichert die fertig gewichtete Feature-Matrix. Unterschiedliche Werte laufen ohne Fehlermeldung durch und skalieren Trainings- und Abfrageseite verschieden.
- Synthetisches T1 bei der Anwendung, echtes T1 im Training: Feature 2 entsteht auf verschiedenen Wegen. Gehört in die Limitations.
- LPM als Hintergrundbild im QC, wenn das FLAIR fehlt: sieht aus wie ein kaputtes MRT und prüft die Segmentierung gegen sich selbst. Lieber kein Bild und eine Meldung. Erkennbar daran, dass der Maximalwert des Hintergrundbilds bei 1 liegt.
- Volumen der dilatierten Infarktmaske als "entferntes WMH" berichten: es ist das Volumen der Maske, nicht das, was an WMH verschwand.
- Dilatation in Voxeln auf anisotroper FLAIR: ein Voxel in z ist mehrere Millimeter, in der Ebene einer.
- WM-Volumen (FLAIR-Gitter) und Hirnvolumen (1-mm-Gitter) stammen aus verschiedenen Gittern. Bei einem Verhältnis erwähnen.

Im Betrieb auf SLURM:

- Alle Stufen brauchen dieselbe sortierte Subject-Liste aus dem BIDS-Baum, sonst meint Array-Index i je Stufe ein anderes Subject.
- Ein Ergebnis-xlsx je Subject, Merge erst nach dem Array. Kein gemeinsames Schreiben.
- "Datei vorhanden" heißt nicht "Datei aktuell". Nach einer Code- oder Parameteränderung mit `--force` neu rechnen, erst die Rechenstufe, dann nach deren Ende die Reportstufe.
- Soll es mehrere Schwellen geben, müssen alle in der Konfiguration stehen (`BIANCA_THRESHOLDS=0.90,0.85`), sonst fehlt der zweite Satz ohne Fehler.
- `conda activate` scheitert in nicht-interaktiven Batch-Shells; `conda activate X || source activate X`, danach `python -c "import pandas, nibabel"` als Prüfung.
- Pfade zu Template und Modell ausdrücklich in den Job exportieren. Fehlen sie, scheitert es erst weiter hinten und ohne klare Meldung.
- BIANCA ruft FSL-Binaries: `LD_LIBRARY_PATH` mit `$CONDA_PREFIX/lib` vorn.
- In einer laufenden Python-Konsole gewinnt eine schon gesetzte Umgebungsvariable gegen die Konfigurationsdatei. Variable entfernen oder Kernel neu starten.

## Was in den Methodenteil gehört

Software mit Version (FSL, FreeSurfer, HD-BET), welches Hirnextraktionswerkzeug tatsächlich griff, T1-Quelle je Subject (nativ oder SynthSR), Trainingssatz des Klassifikators, BIANCA-Optionen, Schwelle, WM-Masking, PV-Grenze, dass nicht nach Clustergröße gefiltert wurde, Art des QC, ausgeschlossene Fälle mit Grund. In die Limitations: keine Validierung gegen manuelle Masken in der eigenen Stichprobe, falls es keine gibt; T1-Asymmetrie zwischen Training und Anwendung. Quellen mit DOI stehen in `PAPERS.md`.

## Trägt nicht

- Keine Aussage über die Genauigkeit in einer neuen Kohorte. Die ruht auf dem Trainingssatz, eine Validierung gegen manuelle Masken ist nicht Teil des Ablaufs.
- 0.90 ist nicht übertragbar auf einen Klassifikator mit anderer Zahl an Trainingspunkten (`--trainingpts`, `--nonlespts`).
- PV und tief sind eine Distanzregel, keine anatomische oder pathologische Unterscheidung.
