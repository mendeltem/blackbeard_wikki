---
id: dora-baseline-is-plain-unet-and-field-evaluates-on-t2w
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: Synapse-REST-API mit Nutzer-Token (Wiki-Seiten 639483/639429, bundle2, entity/children), PVS-Arena Alita, 2026-10-11 04:03
verweist_auf: [epvs-2024-data-open-for-certified-synapse-users, public-pvs-reference-data-and-models-2026-10]
---

# Die DoRA-PVS-Baseline ist ein einfaches U-Net (nicht DRIPS), und das Feld misst PVS fast nur auf T2w

## Aussage
Das DoRA-PVS-Projekt (syn72039291) liefert als Baseline `pvs_segmentation.py` ("U-Net-based", "not intended to be competitive"),
eine einfache Domain-Randomisierung und `Atlas.zip` (Labelkarten). Das ist nicht der DRIPS-Code (Bernal), nur dessen Prinzip;
DRIPS selbst liegt bei uns als Docker vor und ist das staerkere Verfahren. Alle fuenf Baseline-Dateien sind trotz canView
canDownload=false (Registrierung), die Challenge endete am 28.08.2026, Daten werden nicht verteilt. Die DoRA-Testkohorten
(LBC1936, Sleep, MSS3, STRADL, PCB, ADNI-3, 7 weitere) sind zu vier Fuenfteln T2w mit 0,5-1 mm; T1w nur PCB (0,8 mm) und ADNI-3.
Der EPVS-2024-Ordner "submitted method description" (syn64956514) enthaelt sieben PDFs (Abdul, BIG_AEHRC, CCNU_CS_24_EPVS,
HufsAIM, SHIVA, bear_walker, nic-vicorob); der RSS-Sieger TheGPU fehlt; alle gesperrt bis zur Team-Mitgliedschaft.

## Traegt
Methodenwahl: Zeit nicht in die DoRA-Baseline stecken; DRIPS ist bereits die bessere Vertretung dieser Idee. Domaenenfrage:
eine T1+FLAIR-Kohorte ohne T2 (BELOVE) liegt ausserhalb des Feldes -- Vergleiche mit Challenge-Zahlen sind deshalb nicht
uebertragbar. Die Teamnamen sind der Suchschluessel fuer oeffentlichen Code (Frage F7.1 der Arena).

## Traegt nicht
Was in den PDFs steht; ob TheGPU je eine Beschreibung geliefert hat; die abgeschnittene Tabellenhaelfte der DoRA-Kohorten.

## Bruchindikator
Ein Download der Baseline zeigt DRIPS-Quelltext oder -Gewichte; oder ein DoRA-Report nennt ueberwiegend T1w-Testkohorten.

## Ablesung
GET /entity/syn72039291/wiki/639483 und /639429; POST /entity/children (syn72039291: 5 Dateien, syn64956514: 7 PDFs);
POST /entity/<id>/bundle2 mit includePermissions -> canDownload false fuer alle. Arena-Notiz pvs-arena/literatur/dora_baseline.md.

## Verknuepft
- [epvs-2024-data-open-for-certified-synapse-users](epvs-2024-data-open-for-certified-synapse-users.md)
- [public-pvs-reference-data-and-models-2026-10](public-pvs-reference-data-and-models-2026-10.md)
