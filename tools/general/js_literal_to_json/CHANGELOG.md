# Changelog

- 2026-10-02: erste Fassung, verallgemeinert aus `daten.py` der Verbundseite ki-anwendungsschicht. Pfade und Konstantennamen sind Parameter statt fest eingetragen; projektspezifische Ableitungen (Deckungsquoten) entfernt. Fehler des Vorläufers behoben: Schlüsselmuster wie `, bar:` innerhalb von Zeichenketten wurden dort fälschlich quotiert; jetzt werden Schlüssel, Kommentare und Kommata nur außerhalb von Zeichenketten behandelt.
