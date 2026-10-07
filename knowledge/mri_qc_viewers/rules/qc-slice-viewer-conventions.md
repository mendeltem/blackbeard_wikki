---
id: qc-slice-viewer-conventions
typ: regel
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-07
herkunft: Nutzerrueckmeldungen an den CMB-Schichtbetrachter (Projekte valdo-t2s, mb-arena), 2026-09-29 bis 2026-10-07
verweist_auf: [slice-viewer-as-shared-tool]
---

# Setzungen fuer eine QC-Seite: Referenz blau, Proband hoch/runter, Klick zeigt die Werte

## Aussage
Eine Qualitaetskontroll-Seite fuer Laesionsdetektion (hier Mikroblutungen) ist so gebaut:
1. **Zwei grosse axiale Bilder je Schicht**: links das Bild mit der Referenz (Ground Truth),
   rechts dieselbe Schicht mit den Umrissen der Modelle, einzeln schaltbar. Mausrad/Pinch zoomt,
   Ziehen verschiebt.
2. **Farben:** die Referenz ist **blau** (RGB 66, 150, 255); Modellfarben kommen aus einer
   Goldener-Schnitt-Farbtonreihe, die das blaue Band (Farbton 0,50 bis 0,74) auslaesst, damit
   nichts mit der Referenz verwechselt wird. Fruehere Fassung (Referenz gelb) vom Nutzer verworfen.
3. **Tasten:** Pfeil hoch/runter = naechster/voriger Proband, Pfeil links/rechts = Schicht,
   R = Referenz aus/an. (Stand 07.10. noch alte Belegung: Pfeile = Schicht, Bild hoch/runter = Fall; Umbau offen.)
4. **Klick auf eine Komponente** (Vorhersage oder Referenz) zeigt ihre Werte: Volumen in mm3 und
   Voxel, Zahl der Schichten, Lage (Gewebeklasse), maximale und mittlere Wahrscheinlichkeit,
   Status TP/FP/FN und **mit welcher Referenz-Komponente sie zusammengebracht wurde**
   (Beruehrungsregel, Abstand der Schwerpunkte). Die angeklickte Komponente wechselt die Farbe. (Umbau offen.)
5. **Englisch** in Oberflaeche, Laufnamen (`our-U-Net`, `MicrobleedNet-finetuned`) und
   Erklaertexten; je Lauf ein Satz unter "What do the models mean?" mit F1 und Trainingsstand.
6. **Dateiname `quality_control.html`** (nicht `betrachter.html`), daneben `data.json` und `img/`;
   eine Einzeldatei-Variante mit den N laesionsreichsten Faellen fuer den Versand (< 50 MB).

## Traegt
Jede neue QC-Seite fuer Detektion oder Segmentierung kleiner Laesionen (CMB, WMH, PVS, Infarkt),
auch mit anderen Werkzeugen (NiiVue-Seiten).

## Traegt nicht
Seiten fuer Volumetrie oder Oberflaechen, wo es keine Komponenten zum Anklicken gibt.

## Bruchindikator
Der Nutzer aendert eine der Setzungen an einer fertigen Seite; dann diesen Eintrag fortschreiben.

## Ablesung
Nutzeraussagen 29.09. (Gefaesse ueber viele Schichten als Fehlalarm erkannt), 07.10. ("diese Seite
ist ziemlich gut", Tasten, Klick-Werte, Blau, Dateiname). Setzung, kein Messwert.

## Verknuepft
- [slice-viewer-as-shared-tool](../open_checks/slice-viewer-as-shared-tool.md)
