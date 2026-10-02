---
id: wayback_snapshot
bereich: tools/general
stand: 2026-10-02
herkunft: Projekt ai_modellkurve
sprache: python
---

# wayback_snapshot

## Zweck
Holt die archivierte Fassung einer Seite zu einem Stichtag aus der Wayback Machine, wandelt sie in Fließtext und schneidet den Bereich um ein Stichwort heraus. Gibt die Archiv-URL und den Zeitstempel mit aus, damit die gefundene Zahl ein belegbares Datum bekommt.

Gebaut für Preis- und Spezifikationsarchäologie: Anbieter überschreiben ihre Preis- und Datenblattseiten ohne Versionierung. Will man eine Zeitreihe statt nur des heutigen Stands, ist das Archiv oft die einzige zitierfähige Quelle. In Projekt ai_modellkurve lieferte das Werkzeug die historischen Preise für GPT-3.5, GPT-4, GPT-4 Turbo, o1, GPT-5, Gemini 1.5 Pro und DeepSeek.

## Wann verwenden, wann nicht
Verwenden, wenn eine Zahl zu einem vergangenen Zeitpunkt belegt werden soll und die Originalseite nur den aktuellen Stand zeigt.

Nicht verwenden bei Seiten, die ihren Inhalt erst im Browser nachladen. Das Archiv speichert dann nur das leere Gerüst; erkennbar an einer Ausgabe wie "You need to enable JavaScript to run this app". Betroffen sind unter anderem die alte beta.openai.com/pricing, anthropic.com/pricing und client-seitig gerenderte Leaderboards. Dort stattdessen die Ankündigung oder die Dokumentation suchen.

Nicht verwenden als Ersatz für eine Primärquelle, wenn es die noch gibt. Ein Archivschnappschuss ist Tier 1b, nicht 1a.

## Aufruf
```
python src/wayback_snapshot.py <url-ohne-schema> <JJJJMMTT> [-s STICHWORT] [--vor N] [--nach N] [--alle]
```

Beispiel:
```
python src/wayback_snapshot.py "ai.google.dev/pricing" 20240701 -s "Gemini 1.5 Pro Our next" --nach 420
```

Als Bibliothek:
```python
import sys; sys.path.insert(0, "src")
import wayback_snapshot as w
url, ts = w.schnappschuss("api-docs.deepseek.com/quick_start/pricing", "20251015")
text = w.zu_text(w.hole(url))
print(w.ausschnitt(text, "deepseek-chat")[0])
```

## Eingabe und Ausgabe
Eingabe: URL ohne Schema, Stichtag als `JJJJMMTT`, optional ein Stichwort.
Ausgabe auf stdout: zwei Kommentarzeilen `# quelle:` und `# zeitstempel:`, danach je Treffer ein Textausschnitt.
Rückgabewerte: 0 Treffer, 2 kein Schnappschuss, 3 Stichwort nicht gefunden.

Der Zeitstempel ist der tatsächliche Schnappschuss, nicht der angefragte Stichtag. Die Wayback Machine liefert den nächstgelegenen, und der kann Monate danebenliegen. **Immer den ausgegebenen Zeitstempel zitieren, nie den angefragten Stichtag.**

## Teststand
2026-10-02, Windows 10, Python 3.13, im Werkzeugordner:
`python -m unittest discover -s tests` → 10 Tests, 9 ausgeführt, 1 übersprungen, bestanden.
`WAYBACK_NETZ=1 python -m unittest discover -s tests` → 10 Tests, alle ausgeführt, bestanden.
Beispielaufruf oben am selben Tag ausgeführt, lieferte Schnappschuss `20240701171821`.

## Grenzen
- Nur Standardbibliothek, aber auf das Netz und die Verfügbarkeit von archive.org angewiesen. Kein Caching, kein Wiederholversuch.
- `zu_text` ist eine Regex-Reinigung, kein Parser. Tabellenstruktur geht verloren; Zahlen und ihre Beschriftungen stehen danach in einer Zeile hintereinander und müssen gelesen, nicht automatisch zugeordnet werden.
- Ohne Treffer wird nichts geraten: leere Liste und Rückgabewert 3.
- Die Wayback-Verfügbarkeits-API läuft über `http`, nicht `https`; das ist die dokumentierte Adresse.
