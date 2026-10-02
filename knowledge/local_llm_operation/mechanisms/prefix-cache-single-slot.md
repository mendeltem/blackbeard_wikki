---
id: prefix-cache-single-slot
typ: mechanismus
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [moe-expert-offloading, separate-prefill-from-decode]
---

# Ein Slot, und die Historie nie umschreiben

## Aussage
`llama-server` legt standardmaessig mehrere Slots an, jeder mit **eigenem**
Prefix-Cache. Ein sequenzieller Client landet dann abwechselnd in verschiedenen
Slots, und der System-Prompt wird jedes Mal neu prefillt. `-np 1` haelt alles in
einem Cache.

Daraus folgt eine zweite, wichtigere Regel: bei append-only Verlauf traegt der
Prefix-Cache den gesamten Kontext, pro Schritt werden nur die neuen Tokens
prefillt. Jede Operation, die die Historie **umschreibt** - Kompaktierung,
Zeitstempel im System-Prompt, nachtraegliches Kuerzen - wirft den Cache weg und
erzwingt vollen Re-Prefill.

Beleg aus dem Serverlog: nach einem Treffer meldet der Server
`selected slot by LCP similarity, f_sim_best = 1.000` und wertet nur noch 4 Token
statt 80 aus.

## Traegt
Die Entscheidung `-np 1` fuer jeden sequenziellen Client. Und die Entscheidung
gegen Prompt-Kompaktierung in Agent-Schleifen auf lokaler Hardware.

## Traegt nicht
Batch-Durchsatz. Dort ist das Gegenteil richtig: mehrere parallele Anfragen lasten
die Expert-Matmuls besser aus. Zwei Startprofile anlegen, eines je Zweck.

## Bruchindikator
Jeder Aufruf kostet gleich viel Prefill, obwohl der Prompt sich nur am Ende
verlaengert. Dann greift der Cache nicht.

## Ablesung
Eigene Messung, llama.cpp b10603, Serverlog mit `-lv 3`.

## Verknuepft
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
- [separate-prefill-from-decode](../rules/separate-prefill-from-decode.md)
