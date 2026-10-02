---
id: yt-dlp-windows
bereich: tools/general
stand: 2026-10-02
herkunft: Gespraech Victus, 2026-10-02
sprache: bash
---

# yt-dlp unter Windows betriebsfertig machen

## Zweck
Ein langes YouTube-Video herunterladen, ohne an drei Stellen hintereinander zu
scheitern, die alle gleich aussehen ("Befehl nicht gefunden", "This video is not
available") und verschiedene Ursachen haben.

Dieser Eintrag ist kein Skript, sondern eine Einrichtung plus drei Fallen.
`yt-dlp` selbst ist fremde Software; hier steht nur, was auf einem
Windows-Rechner mit Anaconda zusaetzlich noetig ist.

## Wann verwenden, wann nicht
Verwenden, wenn ein Download mit `yt-dlp` auf Windows nicht laeuft. Die drei
Fallen unten decken alle Faelle ab, die in dieser Sitzung aufgetreten sind.

Nicht verwenden als Begruendung, einen Download durchzufuehren: ob ein Video
heruntergeladen werden darf, entscheidet die Rechtelage, nicht dieses Blatt.
Unproblematisch sind eigene Videos, CC-lizenzierte Inhalte und ausdrueckliche
Erlaubnis des Rechteinhabers.

## Aufruf

Formate ansehen, bevor irgendetwas geladen wird -- bei langen Videos entscheidet
das ueber zweistellige Gigabyte:

    yt-dlp -F "https://www.youtube.com/watch?v=<id>"

Dann laden. Ohne `-f` waehlt `yt-dlp` die hoechste Bitrate, meist AV1:

    yt-dlp -f "bv*+ba/b" -o "%(title)s [%(id)s].%(ext)s" "https://www.youtube.com/watch?v=<id>"

Maximale Kompatibilitaet statt kleinster Datei (H.264 plus AAC, sauberes mp4):

    yt-dlp -f "137+140" --merge-output-format mp4 -o "%(title)s [%(id)s].%(ext)s" "<url>"

Nur einen Abschnitt eines langen Videos:

    yt-dlp --download-sections "*00:10:00-00:25:00" "<url>"

## Eingabe und Ausgabe
Eingabe: eine Video-URL. Ausgabe: eine Datei im aktuellen Verzeichnis, Name nach
`-o`-Vorlage. `-P <pfad>` legt das Zielverzeichnis fest.

Bricht ein Download ab, setzt **derselbe Befehl** an der `.part`-Datei wieder
auf. Das ist bei mehrstuendigen Videos der eigentliche Grund, `yt-dlp` zu nehmen.

## Teststand
2026-10-02, Windows 10, Anaconda-Umgebung aktiv, Python 3.13.13, ffmpeg 8.0.1,
yt-dlp 2026.08.19, Deno 2.9.6.

Geprueft an zwei Videos: ein zweiminuetiges (Formatliste ging auch ohne
JS-Laufzeit, allerdings nur bis 1080p) und ein 1:45:37 langes (ohne JS-Laufzeit
brach es mit "This video is not available" ab, mit Deno plus EJS vollstaendige
Liste inklusive AV1). Ausgewaehlt wurde selbsttaetig `399+251`, rund 479 MiB.

## Grenzen

### Falle 1 -- die falsche Python-Umgebung
`pip install yt-dlp` landet in der Umgebung, in der `pip` laeuft, nicht in der,
in der die Shell steht. Zusaetzlich: **Anaconda blendet beim Aktivieren einer
Umgebung das Benutzer-Site-Verzeichnis aus.** Ein `pip install --user` ist danach
installiert und trotzdem nicht importierbar -- `python -m yt_dlp` meldet
"No module named yt_dlp", waehrend dieselbe Datei auf der Platte liegt.

Ein Installieren direkt in die Conda-Umgebung scheitert an Schreibrechten, wenn
Anaconda unter `C:\ProgramData` liegt.

Loesung, die alle drei Varianten umgeht -- eine eigene venv im Heimatverzeichnis:

    python -m venv %USERPROFILE%\venvs\ytdlp
    %USERPROFILE%\venvs\ytdlp\Scripts\python.exe -m pip install -U yt-dlp

Die `yt-dlp.exe` liegt dann unter `%USERPROFILE%\venvs\ytdlp\Scripts\` und ist
von jeder Shell aus aufrufbar, unabhaengig von Conda. Fuer den kurzen Befehl ein
Alias im PowerShell-Profil, nicht eine PATH-Aenderung.

### Falle 2 -- YouTube verlangt eine JavaScript-Laufzeit
Ohne JS-Laufzeit faellt `yt-dlp` auf einen Notfall-Client zurueck. Bei kurzen
Videos liefert der eine verkuerzte Formatliste (kein AV1, Ende bei 1080p), bei
anderen bricht er mit **"This video is not available"** ab -- eine Fehlermeldung,
die wie ein gesperrtes oder geloeschtes Video klingt und keines ist.

Zwei Teile, beide noetig:

    winget install DenoLand.Deno        die Laufzeit
    --remote-components ejs:github      das Loesungsskript, das yt-dlp bei
                                        Bedarf aus seinem eigenen Repo holt

Der zweite Teil ist **nicht** Vorgabe. Deno allein reicht nicht: die Warnung
wechselt dann nur von "keine Laufzeit gefunden" zu "challenge solver script
skipped", und der Fehler bleibt derselbe.

### Falle 3 -- Backslashes in der Konfigurationsdatei
`yt-dlp` liest `%APPDATA%\yt-dlp\config` mit **Shell-Regeln**. Dort ist `\` ein
Escape-Zeichen. Ein Windows-Pfad mit Backslashes kommt zerstueckelt an:

    --js-runtimes deno:C:\Users\x\...\deno.exe
      wird gelesen als
    deno:C:Usersx...deno.exe

Die Datei **wird** gelesen, der Wert ist nur zerstoert -- die Fehlermeldung ist
deshalb identisch mit der, die man ohne Konfigurationsdatei bekaeme. Sichtbar
nur mit `-v`, das die geladene Konfiguration ausgibt.

Loesung: **Vorwaertsschraegstriche** in der Konfigurationsdatei.

### Was dieser Eintrag nicht loest
`yt-dlp` veraltet schnell, weil YouTube regelmaessig etwas aendert. Bei
"Unable to extract" ist die Version die erste Vermutung, nicht die URL.
Die hier genannten Flags koennen sich mit einer neuen Fassung aendern.
