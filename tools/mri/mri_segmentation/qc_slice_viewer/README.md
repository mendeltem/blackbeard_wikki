---
id: qc_slice_viewer
bereich: tools/mri/mri_segmentation
stand: 2026-10-08
herkunft: Projekte valdo-t2s (cmb/review/build_slice_viewer.py), mb-arena, pvs-arena (skripte/qc_belove_bauen.py); aus beiden zusammengefuehrt
sprache: python
---

# qc_slice_viewer

## Zweck
Erzeugt aus einem Manifest die Qualitaetskontroll-Seite fuer Laesionsdetektion auf MRT nach den
Setzungen in [qc-slice-viewer-conventions](../../../../knowledge/mri_qc_viewers/rules/qc-slice-viewer-conventions.md):
zwei grosse axiale Bilder je Fall, links Referenz (blau) oder Vergleichsmaske, rechts schaltbare
Umrisse beliebig vieler Laeufe, Zaehler je Schicht und Fall, F1 je Fall und gepoolt, Tasten,
Zoom, Fall-Checkliste. Optional: Urteilsfarben fuer EIN Modell (`--verdict`), Liquor-Ebenen
(SynthSeg-Fuellung und was die Liquor-Regel entfernen wuerde, getrennt nach Fehlalarm und Treffer).
Eine HTML-Datei plus `img/`, kein Server noetig. Damit faengt eine neue Laesionsart nicht von
null an, siehe [qc-build-order-for-a-new-lesion-type](../../../../knowledge/mri_qc_viewers/rules/qc-build-order-for-a-new-lesion-type.md).

## Wann verwenden, wann nicht
Verwenden fuer Detektion und Segmentierung kleiner Laesionen (CMB, PVS, WMH, Infarkt) auf einem
gemeinsamen Gitter, mit Handreferenz oder nur mit Vergleichsmaske (`reference_is: comparison`,
dann heissen alle Zaehler Uebereinstimmung). Nicht verwenden fuer Volumetrie ohne Komponenten,
nicht fuer Laeufe auf anderem Gitter als das Bild (werden uebersprungen), nicht als Rating-Seite
(verblindetes Urteil je Kandidat ist eine eigene Seite, siehe Regel 6 der Bauordnung).

## Aufruf
    DL=/home/uchralt/miniconda3/envs/dl/bin/python
    $DL tools/mri/mri_segmentation/qc_slice_viewer/src/qc_slice_viewer.py MANIFEST.json --out OUT_DIR
    $DL .../qc_slice_viewer.py MANIFEST.json --out OUT_DIR --verdict          # ein Lauf, Farben = Urteil
    $DL .../qc_slice_viewer.py MANIFEST.json --out OUT_DIR --refresh-html      # nur Seite neu aus data.json
    $DL .../qc_slice_viewer.py MANIFEST.json --out OUT_DIR --on run1 run2      # Laeufe beim Start an

Manifest (JSON), ein Eintrag je Fall; Pfade absolut:

    {"dataset": "VALDO T2*: our model", "cohort": "valdo",
     "reference_is": "reference",            # oder "comparison" (Maske ist nicht die Wahrheit)
     "image_as_acquired": true,              # false: gespeichertes Bild ist 1 - I und wird zurueckgedreht
     "csf_overlay": false,                   # true: Liquor-Ebenen (braucht synthseg je Fall)
     "runs": [{"name": "our-3D-U-Net", "kind": "prob", "threshold": 0.3, "min_mm3": 2.0,
               "max_voxels": 2100, "csf_rule": false, "info": "ein Satz fuer das ?-Fenster"},
              {"name": "pipeline", "kind": "mask"}],
     "cases": [{"id": "sub-104", "image": ".../sub-104_image.nii.gz", "reference": ".../sub-104_label.nii.gz",
                "runs": {"our-3D-U-Net": ".../sub-104_pred_proba.nii.gz", "pipeline": ".../mask.nii.gz"},
                "synthseg": ".../sub-104_synthseg.nii.gz", "slice_mm": 4.0}]}

Live-Modus (Seite laedt sich nach jedem Neubau selbst): `cmb.review.live_server` aus valdo-t2s,
`python -m cmb.review.live_server OUT_DIR --port 8765`, nur 127.0.0.1.

## Eingabe und Ausgabe
Eingabe: NIfTI auf einem Gitter je Fall (axial = dritte Achse, RAS), Wahrscheinlichkeiten als uint8
0..255 oder float 0..1, Masken > 0, optional SynthSeg (anderes Gitter wird mit naechstem Nachbarn
umgerechnet). Voxelvolumen aus dem Header. `slice_mm` = erfasste Schichtdicke, bestimmt die
Buendelung der Gitterschichten je Kachel (hoechstens 80 Kacheln je Fall).
Ausgabe: `OUT_DIR/quality_control.html`, `data.json` (je Fall: n_ref, ref_ml, tiles mit Zaehlern je
Schicht, stats je Lauf tp/fp/fn/n/ml, bei Liquor-Ebenen csf_drop_fp/csf_drop_tp), `img/<id>.jpg`
und `img/<id>_<ebene>.png`, `build_args.json`.

## Teststand
2026-10-08, Linux, Python 3.12 (conda dl: nibabel 5, scipy, Pillow): `python tests/test_synthetic.py`
bestanden (zwei synthetische Faelle, 3 Kugeln Referenz, 2 Treffer + 1 Fehlalarm + 1 Blob unter der
Groessenregel: tp/fp/fn = 2/1/1; Urteilsmodus; Vergleichs-Wortlaut; Maskenlauf; Fall ohne Referenz).
Gegenprobe an drei VALDO-Faellen gegen den CMB-Generator (gleiche Schwellen, Liquor-Ebenen):
siehe CHANGELOG.

## Grenzen
Keine Klick-Werte je Komponente (offen, siehe Pruefpunkt slice-viewer-as-shared-tool). Keine
Einzeldatei-Variante fuer den Versand (im CMB-Generator vorhanden, hier noch nicht). Die Seite ist
Englisch; Laufnamen ohne Leerzeichen (Dateinamen der Ebenen). Patientendaten: nur lokal bauen und
nur auf 127.0.0.1 ausliefern.
