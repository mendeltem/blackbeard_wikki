# mri_qc_viewers: Kurzstand

Stand 2026-10-07. Prefill fuer Chats und Agenten. Details in [INDEX.md](INDEX.md).

Wie eine QC-Seite fuer Laesionsdetektion gebaut wird, damit Mendel sie benutzt: Einzeldatei-HTML,
links die Referenz, rechts dieselbe Schicht mit schaltbaren Modell-Umrissen; Referenz **blau**,
Modellfarben meiden das Blau; Pfeil hoch/runter = Proband, links/rechts = Schicht; Klick auf eine
Komponente zeigt Groesse, Schichten, Wahrscheinlichkeit, Status und die zugeordnete Referenz, die
Angeklickte wechselt die Farbe; alles Englisch; Datei heisst `quality_control.html`.
Offen: den Generator als Tool mit Test einstellen.

**Lesen bei:** QC-Seite, Betrachter, Schichtbetrachter, NiiVue, Referenz gegen Vorhersage, Fehlalarme ansehen, Laesionen zaehlen.

**Regel, neu 2026-10-08:** Qualitaetskontrolle fuer eine neue Laesionsart wird in fester Reihenfolge gebaut, nie von null: Lader statt neuer Seite; ohne Referenz heisst die Maske Vergleich und die Zaehler Uebereinstimmung, gepoolt gleich dem Messskript; ein Modell in Urteilsfarben, mehrere in Modellfarben; jede anatomische Regel als eigene Ebenen vor der Kette; je Fund das Warum mit Nachbarschichten; Rating als eigene verblindete Seite mit sofortigem Speichern; Patientendaten nur auf 127.0.0.1; Pruefung headless und gegen das Messskript; Vorlesung als eigenes Artefakt. Der PVS-Betrachter fuer 73 Faelle entstand so in einer Stunde.
