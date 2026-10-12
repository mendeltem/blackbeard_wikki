---
id: native-run-of-the-edinburgh-pipeline-what-it-takes
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-12
herkunft: Vorbereitung des Nachlaufs der 30 Typfehler-Faelle auf Alita, 12.10.2026 (~/data/work/pvs/nachlauf30/)
verweist_auf: [numeric-ids-became-char-codes-in-filenames, pipeline-failures-and-names-before-tuning]
---

# Die Edinburgh-PVS-Pipeline laeuft ohne Docker-MATLAB, wenn fuenf Dinge stimmen

## Aussage
Der Original-Container (MATLAB R2022b, FreeSurfer 7.4.1, FSL, TractoR, RORPO) war auf Alita nicht baubar (Docker-Build brach
im apt-Schritt ab). Nativ geht es so, alles ohne sudo, gemessen am 12.10.2026:
1. **MATLAB R2026b** (Online-Lizenz, `matlab -batch` laeuft; `ver` in -batch haengt minutenlang -- `license('test',...)` statt ver).
   Die Pipeline braucht **Image Processing Toolbox** (bwconncomp 28x, imfill, strel, imerode, niftiread) und **Statistics Toolbox**
   (kmeans); ohne sie startet nichts. `ls $MATLABROOT/toolbox` zeigt, was installiert ist.
2. **RORPO** aus dem GitHub-Quelltext (path-openings/RORPO): conda-Env mit `libitk-devel` (5.4.7) + Compiler; cmake braucht
   `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` und `-DCMAKE_C_FLAGS=-std=gnu11` (mcimage.c scheitert an C23-`bool`). Wrapper-Skript setzt
   LD_LIBRARY_PATH auf conda-lib + rorpo-lib, weil RORPO_multiscale.m den Pfad sonst auf /usr/local/lib umbiegt.
3. **TractoR 3.5.2** mit conda-R: `xz` (liblzma) in die Env, sonst scheitert `littler`; der kompilierte Launcher `libexec/tractor`
   findet libR.so nicht -> umbenennen, `bin/tractor` faellt auf den R-Skript-Weg zurueck (reg-linear/reg-nonlinear/reg-apply = FSL
   flirt/fnirt/applywarp, alle vorhanden).
4. **FreeSurfer 8.2.0 kann SamSeg nicht**: fspython ist 3.8, `samseg/gems/gemsbindings.cpython-312*.so` ist fuer 3.12 gebaut ->
   ModuleNotFoundError. Loesung: `freesurfer/freesurfer:7.4.1` als Docker-Image (30 GB), Wrapper je Kommando (`run_samseg`,
   `mri_synthseg`, `mri_synthstrip`, `mri_label2vol`, `mri_convert`) mit `--user $(id -u)`, Datenbaum und Lizenz gemountet.
   Gleiche FreeSurfer-Version wie der Original-Container = vergleichbar mit den 73 vorhandenen Masken.
5. **Pfade**: der Datenordner ist ein Symlink auf die externe Archiv-SSD (Pfad mit Leerzeichen!) -> im Container die SSD mit
   mounten, in den CSVs nur den Symlink-Pfad ohne Leerzeichen benutzen (die Pipeline baut Shell-Kommandos ohne Anfuehrungszeichen),
   Ausgaben lokal, nicht ins Archiv. Kennungen als Text (`case9`), nie Zahlen. MATLAB gibt Kindprozessen seine eigenen
   Bibliothekspfade mit -> im Treiber `setenv('LD_LIBRARY_PATH','')`.

## Traegt
Jeden Nachlauf der Pipeline auf Alita oder einem anderen Rechner ohne den Original-Container; die Entscheidung, FreeSurfer-Teile
ueber Docker zu holen, wenn die lokale Version Bindings nicht laedt.

## Traegt nicht
Die Ergebnisqualitaet (nicht geprueft, Lauf wartet auf die Toolboxen); Rechner ohne Docker-Gruppe.

## Bruchindikator
Ein FreeSurfer-8-Release, dessen fspython zu den SamSeg-Bindings passt; eine RORPO-Version, die mit C23 baut.

## Ablesung
`~/data/work/pvs/nachlauf30/` (pvs_nachlauf.sh, nachlauf30.m, tools/), Logs conda_create.log, tractor_install*.log, docker_pull.log; 12.10.2026 09:25-10:25.

## Verknuepft
- [numeric-ids-became-char-codes-in-filenames](numeric-ids-became-char-codes-in-filenames.md)
- [pipeline-failures-and-names-before-tuning](../../lesion_detection_method/rules/pipeline-failures-and-names-before-tuning.md)
