# brain_volumetry: Kurzstand

Stand 2026-10-12. Prefill fuer Chats und Agenten. Details in [INDEX.md](INDEX.md).

Verlaufs-Volumetrie liefert zwei Seiten: die Trendseite (gemischtes Modell, Steigung je Proband, Seitenvergleich)
und die Fehlerseite. Die Fehlerseite hat vier Bausteine: Test-Retest je Struktur aus zwei Segmentierungen derselben
Sitzung (SDw, CV, ICC(2,1), SDC95 = 1,96 * sqrt 2 * SDw, Bland-Altman), Laengsschnitt-Residuen und kuerzestes Intervall,
Nachweisbarkeit (Jahre bis eine Person die SDC ueberschreitet, KI in denselben Einheiten), Ausfall/QC je Zeitpunkt.
Laesionsausschluss nur, wenn die Maske in allen Sitzungen existiert, sonst entstehen Maskeneffekte von +1400 %.

**Lesen bei:** Volumetrie, SynthSeg, FreeSurfer, Atrophie, Verlauf, Laengsschnitt, Test-Retest, SDC, ICC, Messfehler, Hippocampus.

**Neu 2026-10-12:** SynthSeg in FreeSurfer 8.2 rechnet nur auf CPU (85 s je Sitzung mit --robust); Vollkohorten in Ordner-Batches, 3 parallel. Nach jeder Kohortenkopie gzip -t ueber alle NIfTI (eine abgeschnittene T1 lag 5 Wochen unbemerkt). Rechenplan-Literatur: FreeSurfer longitudinal stream (Reuter 2012) und Euler-Zahl als QC-Gate (Rosen 2018) sind die belegten Hebel; FastSurfer-Dicke ICC 0,92 vs 0,87.
