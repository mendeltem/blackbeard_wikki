---
id: secure-boot-kernel-update-unloads-nvidia-dkms
typ: risiko
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita (Ubuntu 24.04, RTX A5000), 2026-10-02 bis 2026-10-07
verweist_auf: [restart-loop-is-an-alarm-not-a-repair]
---

# Ein Kernel-Update nimmt bei Secure Boot den NVIDIA-Treiber mit

## Aussage
Bei eingeschaltetem Secure Boot laedt der Kernel nur signierte Module. Nach einem
Kernel-Update (hier 7.0.0-31 auf 7.0.0-34) baut DKMS das NVIDIA-Modul fuer den neuen
Kernel neu und signiert es mit dem **lokalen** MOK-Schluessel
(`/var/lib/shim-signed/mok/MOK.der`). Ist dieser Schluessel nie in der Firmware
eingetragen worden, verweigert der Kernel das Modul: `modprobe nvidia` meldet
`Operation not permitted`, `nvidia-smi` findet keinen Treiber, und jeder Dienst, der
die GPU braucht (llama-server, Training), steht -- ohne dass irgendein Log einen
Treiberfehler nennt. Auf Alita blieb das fuenf Tage unbemerkt wirksam, ein zweiter
Neustart aenderte nichts.

Drei Auswege, alle mit sudo:
1. Das von Canonical signierte Modulpaket zum neuen Kernel installieren:
   `apt install linux-modules-nvidia-<treiber>-<kernelversion>-generic` (zieht die
   passende Treiberversion nach), dann Neustart. **Gewaehlt, funktioniert.**
2. Den eigenen MOK-Schluessel eintragen (`mokutil --import MOK.der`, beim Booten
   bestaetigen). Danach laedt jedes DKMS-Modul, auch kuenftige.
3. Im GRUB den alten Kernel booten, fuer den das signierte Paket noch da ist.

**Nachtrag 07.10. 10:45 (Ursache eingegrenzt):** Nach einem weiteren Kernel-Update lagen fuer den
laufenden Kernel ZWEI Module: `updates/dkms/nvidia.ko.zst` (DKMS, lokaler MOK-Schluessel, nicht
eingetragen) und `kernel/nvidia-580/nvidia.ko` aus `linux-modules-nvidia-580-<kernel>` (vom
Distributor signiert, laedt unter Secure Boot). `modprobe` nimmt `updates/` zuerst, daher
"Operation not permitted", obwohl ein lauffaehiges Modul daneben liegt. Pruefen: `modinfo` beider
Pfade (Zeile `signer`), `modprobe -n -v nvidia` zeigt, welches gewaehlt wird. Abhilfe ohne Neustart:
`dkms remove nvidia/<version> -k <kernel> && depmod -a && modprobe nvidia`; dauerhaft den
MOK-Schluessel eintragen, sonst kommt das DKMS-Modul beim naechsten Kernel-Update wieder davor.

## Traegt
Jede Workstation mit Secure Boot, NVIDIA-DKMS und automatischen Kernel-Updates
(Ubuntu `unattended-upgrades`). Pruefbefehl vor dem Neustart:
`dkms status` zeigt das Modul fuer den neuen Kernel, `mokutil --sb-state` sagt
`SecureBoot enabled`, `mokutil --list-enrolled | grep -c Canonical` -- steht dort
nur Canonical, fehlt der lokale Schluessel und Weg 1 oder 2 ist faellig.

## Traegt nicht
Maschinen ohne Secure Boot, oder mit eingetragenem MOK. Dort laedt das DKMS-Modul
nach dem Update normal.

## Bruchindikator
`cat /proc/driver/nvidia/version` liefert etwas, obwohl `dkms status` nur ein
lokal signiertes Modul fuer den laufenden Kernel zeigt -- dann ist die Aussage
ueber die Signaturpruefung falsch oder Secure Boot aus.

## Ablesung
Eigene Messung auf Alita, Tier 1a (Journal, `dkms status`, `mokutil`), 2026-10-02
und 2026-10-07. Die Dauer des Ausfalls (fuenf Tage) kam daher, dass der Waechter des
Modellservers den Treiber nicht prueft, siehe
[restart-loop-is-an-alarm-not-a-repair](../../agent_tooling/rules/restart-loop-is-an-alarm-not-a-repair.md).

## Verknuepft
- [restart-loop-is-an-alarm-not-a-repair](../../agent_tooling/rules/restart-loop-is-an-alarm-not-a-repair.md)
