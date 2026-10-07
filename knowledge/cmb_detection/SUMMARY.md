# cmb_detection: Kurzstand

Stand 2026-10-07. Prefill fuer Chats und Agenten. Details in [INDEX.md](INDEX.md).

Mikroblutungen auf T2*/SWI automatisch zaehlen. Oeffentliche Messlatte VALDO 2021 Task 2
(72 Faelle, drei Kohorten, 0,8 bis 4 mm Schichten), Mass Laesions-F1 gepaart mit Bootstrap.

**Getragen (Befunde, alle auf VALDO):** Die Gefaess-Uebermalung des Referenzverfahrens
MicrobleedNet loescht auf dicken Schichten die Blutungen selbst; ohne sie +0,136 F1, der
groesste Einzelgewinn. Ein 3D-U-Net, dessen erste Ebene nur in der Schicht faltet und poolt,
schlaegt alle isotropen Netze (+0,159 gegen Attention-U-Net; MedNeXt, nnU-Net-ResEnc,
R2U-Net, Swin UNETR alle schlechter). Eine parameterfreie Regel "Komponente mehrheitlich
im Liquor -> weg" (SynthSeg-Gewebekarte) entfernt die Haelfte der Fehlalarme ohne eine
Blutung zu verlieren (0,585 -> 0,646). Kette insgesamt: 0,245 -> 0,647. Zweite Stufe als EIN Modell: ein 3D-CNN auf dem
Kandidaten-Pool aller Kohorten (eine Schwelle 0,30, out-of-fold je Fall) ist auf VALDO und
T2* gleich der Liquor-Regel und auf SWI +0,061 besser; es braucht keine Gewebekarte.

**Getragen (Negativbefund):** Alles, was das Netz empfindlicher macht -- blob loss,
Zentrumskarten-Kopf, Neugewichtung verpasster Laesionen, kuenstliche Laesionen, laengeres
Training -- kauft Sensitivitaet mit Fehlalarmen; das F1 steigt nie. Der Engpass ist die
Trennung Blutung / Gefaessquerschnitt mit einer einzigen Magnitudensequenz.

**Regel:** Ein einzelnes U-Net-Training streut ~0,08 F1 zwischen Startwerten. Effekte
darunter gelten nur mit zweitem Startwert oder Intervall ohne Null; vier "bestaetigte"
Bausteine (FRST-Kanal, Gitter, Maske, Bias-Korrektur) lagen bei Nachpruefung im Rauschen.

**Datenbefunde VALDO (getragen):** Die gelieferten Masken sind nicht eng -- Kohorte 3 ist eine
Kopfmaske mit 40 % Nicht-Hirn; Abhilfe SynthSeg- oder HD-BET-Maske, und Masken immer zweifach
pruefen (schneidet ab? wie viel Nicht-Hirn bleibt?). 33 von 72 T1-Bildern tragen NaN in einer
Randschale; SynthSeg liefert dafuer lautlos ein leeres Bild bei Rueckgabewert 0. Eine Zeile
`nan_to_num` im Ladeschritt behebt es, geprueft sicher.

**Lesen bei:** Mikroblutungen, CMB, SWI, T2*, VALDO, MicrobleedNet, kleine Laesionen,
Laesions-F1, Fehlalarme, anisotrope Gitter, Nachbearbeitung mit Gewebekarten.
