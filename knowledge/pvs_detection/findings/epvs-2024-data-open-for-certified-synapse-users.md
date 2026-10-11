---
id: epvs-2024-data-open-for-certified-synapse-users
typ: befund
status: widerlegt
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: Synapse-REST-API direkt abgefragt (repo-prod.prod.sagebase.org), PVS-Cluster Alita, 2026-10-07
verweist_auf: [public-pvs-reference-data-and-models-2026-10]
---

# Die EPVS-Challenge-Daten 2024 brauchen keinen Antrag, nur ein zertifiziertes Synapse-Konto

## Aussage
Das Synapse-Projekt syn54100278 (EPVS Segmentation Challenge, MICCAI 2024) traegt laut API keine Access
Requirements, restrictionLevel OPEN, canPublicRead true. Der Ordner Train (syn60055636) listet 100 Fall-Ordner
(ED_* Edinburgh, SG* Singapur ...), dazu Val.zip (syn61767476), eine Beispielmaske und die Terms of Use v3
(syn59814292). Anonym ist nur Lesen moeglich (Download 403, isCertificationRequired true): noetig sind ein
kostenloses Konto, das Certified-User-Quiz und ein Personal Access Token; dann `synapse get -r syn60055636`.
Die Vorrecherche ("nur auf Anfrage") war falsch; sie stammte aus der Challenge-Webseite, nicht aus der API.

## Traegt
Beschaffung der einzigen oeffentlichen PVS-Referenz mit Handmasken in CSO und Basalganglien, drei Standorte,
T1+T2+FLAIR. Allgemein: Zugangsbedingungen eines Synapse-Datensatzes an der API (accessRequirement,
restrictionInformation) ablesen, nicht an der Projektseite.

## Traegt nicht
Ob Val.zip Labels enthaelt und was die Terms of Use erlauben, ist bis zum Download offen.

## Bruchindikator
Download mit zertifiziertem Konto wird mit einem Access Requirement abgewiesen.

## Ablesung
GET /repo/v1/entity/syn54100278/accessRequirement (0 Ergebnisse), POST /entity/children, POST
/entity/syn61767476/bundle2 (restrictionLevel OPEN), GET /entity/syn61767476/file -> 403 anonym. 2026-10-07 20:25.

## Nachtrag 2026-10-08: Bruchindikator eingetreten, es braucht doch einen Antrag
Mit zertifiziertem Konto (Quiz 15/15) und Token: canDownload false fuer alle Dateien, obwohl
restrictionLevel OPEN und keine Access Requirements. Der Download haengt an der ACL: nur das Team
"EPVS Challenge Participants" (3502876) hat DOWNLOAD. Beitritt nur mit Zustimmung; Weg laut
Teambeschreibung: Terms of Use unterschreiben und an epvs.challenge@gmail.com mit Betreff
"[EPVS Challenge Registration Request]" schicken, dann Mitgliedschaft beantragen. Lehre: neben
accessRequirement und restrictionInformation auch die ACL und `permissions.canDownload` im bundle2
pruefen, bevor man "offen" schreibt.

## Nachtrag 2026-10-11: weiterhin gesperrt
Erneute Pruefung mit zertifiziertem Konto: canDownload fuer Val.zip (syn61767476) weiterhin false, Team-Mitgliedschaft
noch nicht erteilt. Eigener Download-Versuch (lade_jetzt.sh) sauber abgebrochen; Waechter warte_und_lade.sh und
Clara-Auftrag wp10 warten auf die Freigabe. Die Huerde ist extern (Challenge-Organisatoren), nicht technisch.

## Verknuepft
- [public-pvs-reference-data-and-models-2026-10](public-pvs-reference-data-and-models-2026-10.md)
