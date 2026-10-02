# Installation

## Geprüfte Umgebung
Windows 10, Anaconda-Umgebung aktiv (Python 3.13.13), keine GPU nötig.
Geprüft am 2026-10-02 auf Victus.

Die Schritte gelten auch ohne Anaconda — dann ist Schritt 1 nur weniger wichtig.

## Abhängigkeiten

| Paket | Version im Test | woher |
|---|---|---|
| yt-dlp | 2026.08.19 | pip |
| ffmpeg | 8.0.1 | `winget install Gyan.FFmpeg` |
| Deno | 2.9.6 | `winget install DenoLand.Deno` |

`ffmpeg` braucht es, um getrennte Bild- und Tonspuren zusammenzufügen — ohne es
bekommt man zwei Dateien oder nur eine der beiden Spuren.

## Schritte

**1. Eigene venv, nicht in die Conda-Umgebung installieren.**

```
python -m venv %USERPROFILE%\venvs\ytdlp
%USERPROFILE%\venvs\ytdlp\Scripts\python.exe -m pip install -U yt-dlp
```

Warum nicht `pip install` in der aktiven Umgebung: siehe README, Falle 1.
Anaconda unter `C:\ProgramData` ist nicht schreibbar, und ein `--user`-Install
ist in einer aktivierten Conda-Umgebung nicht importierbar.

**2. JavaScript-Laufzeit.**

```
winget install DenoLand.Deno
```

Der PATH-Eintrag wirkt erst in einer neu geöffneten Shell. Die Konfiguration in
Schritt 3 nennt den Pfad zusätzlich ausdrücklich, damit es auch vorher läuft.

**3. Konfigurationsdatei anlegen** unter `%APPDATA%\yt-dlp\config`:

```
# Vorwaertsschraegstriche! Diese Datei wird mit Shell-Regeln gelesen,
# dort ist "\" ein Escape-Zeichen -- ein Windows-Pfad mit Backslashes
# kommt zerstueckelt an und die Fehlermeldung sieht aus wie ohne Config.
--js-runtimes deno:C:/Users/<benutzer>/AppData/Local/Microsoft/WinGet/Packages/DenoLand.Deno_Microsoft.Winget.Source_8wekyb3d8bbwe/deno.exe
--remote-components ejs:github

# Lange Videos: ein fehlgeschlagenes Fragment darf keinen
# mehrstuendigen Download wegwerfen.
--retries infinite
--fragment-retries infinite
-N 5
```

Die Datei gilt für **jeden** `yt-dlp`-Aufruf auf dem Rechner, auch aus anderen
Python-Umgebungen. Löschen stellt das Standardverhalten wieder her.

Ohne BOM schreiben. PowerShell 5.1 schreibt mit `Out-File -Encoding utf8` ein
BOM; besser `[System.IO.File]::WriteAllText(pfad, text, (New-Object
System.Text.UTF8Encoding($false)))`.

**4. Alias, damit der kurze Befehl geht.**

```
Add-Content $PROFILE "Set-Alias yt-dlp '$env:USERPROFILE\venvs\ytdlp\Scripts\yt-dlp.exe'"
```

Wirkt ab der nächsten Shell. Eine PATH-Änderung per `setx` ist der schlechtere
Weg: `setx` schreibt den aufgelösten Wert fest und schneidet bei über 1024
Zeichen ab.

## Abnahme

```
yt-dlp --version
yt-dlp -F "https://www.youtube.com/watch?v=<id>"
```

Der zweite Befehl muss eine Formatliste **mit AV1-Zeilen** (`av01.…`) ausgeben
und **ohne** Warnung über eine fehlende JavaScript-Laufzeit. Fehlt AV1 oder
erscheint die Warnung, greift Schritt 2 oder 3 nicht.

Gegenprobe bei Verdacht auf eine nicht gelesene Konfiguration:

```
yt-dlp -v --simulate "<url>"
```

Die Zeile `[debug] User config "…"` zeigt, welche Optionen tatsächlich ankommen —
dort sieht man zerstückelte Pfade sofort.
