---
id: anisotropic-first-level-beats-isotropic-3d-nets
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), Turnier 1 (2026-09-18) und Turnier 2 (2026-10-02)
verweist_auf: [vessel-inpainting-removes-microbleeds-on-thick-slices, two-seeds-per-decision-below-0.08]
---

# Ein 3D-U-Net mit anisotroper erster Ebene schlaegt alle isotropen Netze

## Aussage
Alle Faelle werden auf ein gemeinsames Gitter 0,5 x 0,5 x 1,0 mm gebracht. Dort faltet
(1 x 3 x 3) und poolt (1 x 2 x 2) die erste Ebene nur in der Schicht; ab der zweiten
Ebene ist das Gitter 1 mm isotrop und das Netz ein gewoehnliches 3D-U-Net (32 Basiskanaele,
InstanceNorm, 22,5 M Parameter). Begruendung: in z sind die meisten Abtastwerte
interpoliert; sie in der ersten Schicht zu mitteln, bringt keine Information und halbiert
die nutzbare Aufloesung in der Schicht (dieselbe Regel wie in nnU-Net fuer anisotrope Daten).

Turnier 1 (neun einstufige Netze, ein Rezept): 0,245 -> 0,404 gegen das 3D-Attention-
U-Net, **+0,159 [+0,091; +0,234]**, in allen drei Kohorten vorn. Turnier 2 (60 Epochen,
2026-10-02), gepaart gegen dieses Netz: MedNeXt -0,098 [-0,175; -0,018], nnU-Net-
Residual-Encoder -0,063 [-0,143; -0,002], R2U-Net 2.5D -0,141 [-0,213; -0,067],
Attention-Gates auf dem Gewinner -0,056 [-0,120; +0,004]. Kein Trainingsrezept-Hebel
(Lernrate, Stapel, Budget, Verlust, Epochen) hob das Netz weiter.

## Traegt
Kleine Laesionen auf anisotropen klinischen Aufnahmen (dicke Schichten), wenn alle
Faelle auf ein gemeinsames Gitter kommen.

## Traegt nicht
Isotrope Daten; dort ist die erste Ebene gewoehnlich. Und: der Gewinn ist gegen die
Netzfamilie gemessen, nicht gegen ein voll konfiguriertes nnU-Net-v2-Framework
(diese Messlatte ist trainiert, aber noch nicht ausgewertet).

## Bruchindikator
nnU-Net v2 mit eigener Konfiguration erreicht auf denselben Falten dasselbe F1 oder mehr.

## Ablesung
Eigene Messungen VALDO 2021 Task 2, 57 Faelle, Laesions-F1 gepaart. Tier 1a.
Begruendung des anisotropen Poolens: Isensee et al., Nat Methods 2021, doi:10.1038/s41592-020-01008-z.

## Verknuepft
- [vessel-inpainting-removes-microbleeds-on-thick-slices](vessel-inpainting-removes-microbleeds-on-thick-slices.md)
- [two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md)
