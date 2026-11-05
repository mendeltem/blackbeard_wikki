# mri_qc_viewers: Kurzstand

**Neu 2026-11-05 (rule):** QC slice images: window in float, then 8-bit PNG, size from the rotated array, Lanczos upscale in the generator, overlay as transparent layer ([qc-slice-images-png-window-aspect](rules/qc-slice-images-png-window-aspect.md)).

**Neu 2026-10-18 (Literatur):** Bild-Sprachmodelle als QC-Vorsortierer sind nicht belegt; Orientierung und reine Bildfragen sind schwach, Kappa ~0,6, nur ueberwacht und nach lokaler Validierung ([research-vision-language-models-for-image-qc-2026-10](findings/research-vision-language-models-for-image-qc-2026-10.md)).

Stand 2026-10-12. Prefill fuer Chats und Agenten. Details in [INDEX.md](INDEX.md).

Wie eine QC-Seite fuer Laesionsdetektion gebaut wird, damit Mendel sie benutzt: Einzeldatei-HTML,
links die Referenz, rechts dieselbe Schicht mit schaltbaren Modell-Umrissen; Referenz **blau**,
Modellfarben meiden das Blau; Pfeil hoch/runter = Proband, links/rechts = Schicht; Klick auf eine
Komponente zeigt Groesse, Schichten, Wahrscheinlichkeit, Status und die zugeordnete Referenz, die
Angeklickte wechselt die Farbe; alles Englisch; Datei heisst `quality_control.html`.
Offen: den Generator als Tool mit Test einstellen.

**Lesen bei:** QC-Seite, Betrachter, Schichtbetrachter, NiiVue, Referenz gegen Vorhersage, Fehlalarme ansehen, Laesionen zaehlen.

**Regel, neu 2026-10-08:** Qualitaetskontrolle fuer eine neue Laesionsart wird in fester Reihenfolge gebaut, nie von null: Lader statt neuer Seite; ohne Referenz heisst die Maske Vergleich und die Zaehler Uebereinstimmung, gepoolt gleich dem Messskript; ein Modell in Urteilsfarben, mehrere in Modellfarben; jede anatomische Regel als eigene Ebenen vor der Kette; je Fund das Warum mit Nachbarschichten; Rating als eigene verblindete Seite mit sofortigem Speichern; Patientendaten nur auf 127.0.0.1; Pruefung headless und gegen das Messskript; Vorlesung als eigenes Artefakt. Der PVS-Betrachter fuer 73 Faelle entstand so in einer Stunde.

**Regel, neu 2026-10-11:** Jede QC-Seite ist Englisch, auch Index, Verlaufs-Plots, NiiVue-Seiten, Rating-README und Manifest-Titel; die Uebersetzung sitzt im Generator. Laengsschnitte (DEMDAS M0..M60) werden im selben Fenster per Sitzungsknopf umgeschaltet, Pfeil hoch/runter = Sitzung desselben Probanden bei stehender Schicht, Bild hoch/runter = Proband, Tabelle "Across sessions" daneben. Excel-Schluessel seit 12.10. englisch; Nutzerregel: jede Ausgabe Englisch, Chat Deutsch, CSF statt Liquor.

**Regel, neu 2026-10-12:** Jede Zahl auf einer QC-Seite erklaert sich beim Hovern (title= mit Software, Version, Rechenweg, Label-Menge), dazu ein Knopf "? Methods" (Taste M) mit Overlay aller Texte, Bauzeitpunkt und Wiki-Link; fehlende Werte nennen Grund und Stand ("recon-all not finished, 31 of 63 sessions"), die Zahlen setzt der Generator ein. Langfassung fuer DEMDAS-GM als englischer Befund.

**Regeln, neu 2026-10-12 (nachmittags):** Striche unter dem Schichtregler zeigen, wo Funde liegen (N/P springen); der lokale Spiegel ~/QUALITY_CONTROLL ist die Quelle des Sticks (sync, cmp, lsof vor dem Abziehen).

**Pruefpunkt, neu 2026-10-12 (16 Uhr):** Index und Sprites einer Seite nur gemeinsam kopieren (rsync des ganzen Ordners); bunter Streifen am Bildrand = Kachelraster passt nicht zur Sprite-Groesse, nicht die Segmentierung. Pruefung: qc_mirror_check.py (Bau, Spiegel, Stick).
