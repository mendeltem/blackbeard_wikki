# brain_volumetry: Kurzstand

**Neu 2026-10-16:** Sequenzen derselben Sitzung (FLAIR auf T2*/SWI) per Header-Weltkoordinaten zusammenbringen; ein FLIRT-Start im Voxelraum drehte LPS- gegen RAS-Dateien falsch. SynthSeg aus FLAIR nur, wo es die Hirnmaske abdeckt ([same-session-sequences-align-by-header-not-voxel-flirt](findings/same-session-sequences-align-by-header-not-voxel-flirt.md)).

Stand 2026-10-13. Prefill fuer Chats und Agenten. Details in [INDEX.md](INDEX.md).

Verlaufs-Volumetrie liefert zwei Seiten: die Trendseite (gemischtes Modell, Steigung je Proband, Seitenvergleich)
und die Fehlerseite. Die Fehlerseite hat vier Bausteine: Test-Retest je Struktur aus zwei Segmentierungen derselben
Sitzung (SDw, CV, ICC(2,1), SDC95 = 1,96 * sqrt 2 * SDw, Bland-Altman), Laengsschnitt-Residuen und kuerzestes Intervall,
Nachweisbarkeit (Jahre bis eine Person die SDC ueberschreitet, KI in denselben Einheiten), Ausfall/QC je Zeitpunkt.
Laesionsausschluss nur, wenn die Maske in allen Sitzungen existiert, sonst entstehen Maskeneffekte von +1400 %.

**Lesen bei:** Volumetrie, SynthSeg, FreeSurfer, Atrophie, Verlauf, Laengsschnitt, Test-Retest, SDC, ICC, Messfehler, Hippocampus.

**Neu 2026-10-12:** SynthSeg in FreeSurfer 8.2 rechnet nur auf CPU (85 s je Sitzung mit --robust); Vollkohorten in Ordner-Batches, 3 parallel. Nach jeder Kohortenkopie gzip -t ueber alle NIfTI (eine abgeschnittene T1 lag 5 Wochen unbemerkt). Rechenplan-Literatur: FreeSurfer longitudinal stream (Reuter 2012) und Euler-Zahl als QC-Gate (Rosen 2018) sind die belegten Hebel; FastSurfer-Dicke ICC 0,92 vs 0,87.

**Neu 2026-10-13:** recon-all 8.2 braucht seine 26 GB nur in den ersten ~15 Minuten (SynthSeg/SynthMorph), danach 2-4 GB; wer ganze Laeufe statt dieser Phase begrenzt, laesst die halbe CPU brach (gemessen: 3,4 Sitzungen je Stunde bei MAX_P=2, 174 OOM-Kills bei MAX_P=5). Vorschlag: Schleuse nur um autorecon1 (~7,5 je Stunde, DEMDAS-Vollkohorte ~9 statt ~20 Tage); auf Slurm je Sitzung 36 GB, 4 CPU, 6 h. Example-Set: 61/65 Sitzungen mit Thickness fertig (13.10. 00:01).

**Neu 2026-10-13 (mit Quellen):** FreeSurfer-Plan fuer Schlaganfall-Laengsschnitte: Long-Stream statt Einzelsitzungen (Vidal-Pineiro 2025: +0,25 ICC; 0-6 Monate ist Rauschen, Raten aus 0/36/60), Laesionen vor recon-all fuellen (Chard 2010, Battaglini 2012, Magon 2014; ONDRI Ozzoude 2020: Fehlrate 62 % -> 8 %), Euler-Zahl als QC-Gate (Rosen 2018, Monereo-Sanchez 2021), eigene SDC95 aus 40 Doppelaufnahmen, longComBat (Beer 2020). Jeder Wiki-Eintrag nennt ab jetzt seine Quellen (Nutzerregel 13.10.).

**Neu 2026-10-13 (nachmittags, mit Quellen):** Durchsicht aller 17 Mehrfach-Sitzungs-Probanden: Ausrichtung und Serienregistrierung ueberall gut; chronische Infarkte bei Folgesitzungen ohne Maske (DWI-Modell nur akut), SynthSeg gibt Hoehlen Label 0 -> vorwaerts getragene Maske noetig. Euler-Zahl nur aus dem Binary (LD_LIBRARY_PATH), nie aus dem Log-Ende. Protokoll v1 eingefroren. HPC-Messung: SynthSeg robust 50 s / 19,9 GB je Sitzung, SAMSEG 7 min / 11 GB.
