# Paper und Quellen

Alle DOIs am 2026-10-02 gegen Crossref geprüft (Titel, Zeitschrift, Erstautor stimmen), sofern nicht anders vermerkt.

## Methode

| Quelle | DOI | Art | wofür |
|---|---|---|---|
| Casamitjana et al., A probabilistic histological atlas of the human brain for MRI segmentation, Nature 2025 | 10.1038/s41586-025-09708-2 | peer-reviewed | NextBrain-Atlas, Grundlage von Stufe 2 |
| Puonti et al., Fast segmentation with the NextBrain histological atlas, bioRxiv 2025 | 10.1101/2025.09.22.673638 | Preprint | schnelle Variante hinter `mri_histo_atlas_segment_fireants`. Laut FreeSurfer-Wiki bei Imaging Neuroscience angenommen; Zeitschriften-DOI nicht geprüft |
| Billot et al., SynthSeg: Segmentation of brain MRI scans of any contrast and resolution without retraining, Medical Image Analysis 2023 | 10.1016/j.media.2023.102789 | peer-reviewed | aseg-Labelsatz der Whole-Structure-Segmentierung |
| Billot et al., Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets, PNAS 2023 | 10.1073/pnas.2216399120 | peer-reviewed | SynthSeg robust, kortikale Parzellierung |
| Desikan et al., An automated labeling system for subdividing the human cerebral cortex on MRI scans into gyral based regions of interest, NeuroImage 2006 | 10.1016/j.neuroimage.2006.01.021 | peer-reviewed | Parzellen 1001 bis 1035 und 2001 bis 2035 |
| Laso et al., Quantifying White Matter Hyperintensity and Brain Volumes in Heterogeneous Clinical and Low-Field Portable MRI, IEEE ISBI 2024 | 10.1109/ISBI56570.2024.10635502 | Konferenzbeitrag, peer-reviewed | `mri_WMHsynthseg`, WMH als Label 77 |
| Griffanti et al., BIANCA: A new tool for automated segmentation of white matter hyperintensities, NeuroImage 2016 | 10.1016/j.neuroimage.2016.07.018 | peer-reviewed | eine der wählbaren WMH-Quellen in Stufe 1 |
| Isensee et al., Automated brain extraction of multisequence MRI using artificial neural networks, Human Brain Mapping 2019 | 10.1002/hbm.24750 | peer-reviewed | HD-BET in der BIANCA-Vorverarbeitung |

## Zwei Konventionen für GM, WM und CSF

| Quelle | DOI | Art | Aussage |
|---|---|---|---|
| Raciti et al., Reinforcing the Weakest Links: Modernizing SIENA with Targeted Deep Learning Integration, arXiv 2603.12951 | keine | Preprint | Abschnitt 4.2: "WM includes cerebral WM, cerebellar WM, and the brainstem." GM schließt Pallidum und Ventral Diencephalon ein. Entspricht `--pallidum-vdc gm` |
| Dimitrijevic, Noblet, De Leener, Impact of Initialization on Intra-subject Pediatric Brain MR Image Registration, Machine Learning for Biomedical Imaging 2024 | 10.59275/j.melba.2024-151b | peer-reviewed | Abschnitt 4.1: "WM encompasses cerebral white matter, brain stem, cerebellum white matter, pallidum, and ventral DC". Entspricht `--pallidum-vdc wm` |

Beide Arbeiten setzen die Gruppierung, keine begründet sie anatomisch oder vergleicht die Varianten. Eine Arbeit, die den Einfluss dieser Wahl auf Gewebevolumina misst, wurde nicht gesucht und ist hier nicht belegt.

## Dokumentation

| Quelle | Art | wofür |
|---|---|---|
| https://surfer.nmr.mgh.harvard.edu/fswiki/HistoAtlasSegmentation, zuletzt geändert 2026-04-15, gelesen 2026-10-02 | Herstellerdoku | Syntax mit `--i`, `--o`, `--device`, `--side`, `--mode`; Ausgabedateien; 0,4 mm; rund 300 ROIs je Hemisphäre |
| https://surfer.nmr.mgh.harvard.edu/fswiki/WMH-SynthSeg, gelesen 2026-10-02 | Herstellerdoku | Label 77, 1 mm, rund 32 GB RAM, laut Seite nur in der Entwicklungsversion |
| https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSeg, gelesen 2026-10-02 | Herstellerdoku | Ausgabe immer 1 mm isotrop, `--parc` ergänzt die Labelbereiche 1000 und 2000 |

## Ohne Beleg aus der Literatur
- Speicherbedarf und Laufzeit des Atlas: im Projekt gemessen, eine Umgebung.
- Die positionale Aufrufsyntax unter FreeSurfer 8.1.0: aus dem Projektskript, in der aktuellen Wiki so nicht dokumentiert.
- Die Plausibilitätsgrenzen in `src/aseg_tissue.py` (GM/WM 0,8 bis 1,8, Summe 1000 bis 2200 ml): Faustwerte für Erwachsene, als Fehlersuche gedacht, nicht als Normbereich.
