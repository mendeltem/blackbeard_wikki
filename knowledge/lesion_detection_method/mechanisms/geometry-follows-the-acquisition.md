---
id: geometry-follows-the-acquisition
typ: mechanismus
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekte valdo-t2s (CMB) und wmhseg (WMH), 2026-09; uebertragen 2026-10-07
verweist_auf: [anisotropic-first-level-beats-isotropic-3d-nets, patches-not-whole-images-for-small-lesions, slices-not-cases-weigh-in-2d-training]
---

# Gitter, Netz und Gewichtung folgen der Aufnahme, nicht dem Lehrbuch

## Aussage
Drei Befunde mit demselben Mechanismus: die Zahl der GEMESSENEN Abtastwerte je Richtung
bestimmt, was ein Netz sehen kann und wie viel ein Fall wiegt.
- Dicke Schichten (3 bis 5 mm) auf feinem Gitter: die erste Netzebene darf nur in der
  Schicht falten und poolen (1 x 3 x 3, 1 x 2 x 2); isotrope 3D-Netze mitteln
  interpolierte Werte und halbieren die nutzbare Aufloesung. CMB: +0,159 gegen das
  3D-Attention-U-Net, alle isotropen Netze (MedNeXt, nnU-Net-ResEnc, R2U, Swin UNETR)
  dahinter. Formfilter (Frangi, Kugeligkeit, Laufstrecke in z) scheitern auf solchen
  Gittern, weil Blooming eine Kugel zum kurzen Zylinder macht.
- Ausschnitte statt ganzer Bilder: 38 x 31 x 47 mm Patches und Schiebefenster geben
  800 Beispiele je Epoche statt 57 und 1,6 GiB VRAM statt Dutzende GB; mehr Kontext
  (24 / 38 / 48 mm) brachte nichts, Anatomie kommt nachtraeglich als Regel.
- 2D-Netze sehen Schnitte, nicht Faelle: 0,49 bis 6 mm Schichtdicke = Faktor 12 im
  Gewicht je Fall; 60 Challenge-Faelle waren 13,5 % der Schnitte (WMH).

Vor jedem Modell also: Voxelgroesse je Sequenz und je Kohorte tabellieren, die
Rechenebene (welche Sequenz traegt das Signal, welche nur eine Nebenbedingung) und das
Gewicht je Fall daraus ableiten.

## Traegt
Kleine Laesionen auf anisotropen klinischen Aufnahmen; gemischte Kohorten mit
unterschiedlicher Schichtdicke.

## Traegt nicht
Isotrope Forschungsaufnahmen (1 mm^3), dort ist das Standard-3D-U-Net richtig; bei
grossen Laesionen kann Kontext ueber dem Patch wichtig werden.

## Bruchindikator
Ein isotropes Netz, das auf dicken Schichten gepaart und mit zweitem Startwert das
anisotrope schlaegt.

## Ablesung
Eigene Messungen VALDO 2021 Task 2 und WMH Segmentation Challenge 2017. Tier 1a.
nnU-Net-Regel fuer anisotrope Daten: Isensee et al., Nat Methods 2021,
doi:10.1038/s41592-020-01008-z.

## Verknuepft
- [anisotropic-first-level-beats-isotropic-3d-nets](../../cmb_detection/findings/anisotropic-first-level-beats-isotropic-3d-nets.md)
- [patches-not-whole-images-for-small-lesions](../../cmb_detection/rules/patches-not-whole-images-for-small-lesions.md)
- [slices-not-cases-weigh-in-2d-training](../../wmh_segmentation/findings/slices-not-cases-weigh-in-2d-training.md)
