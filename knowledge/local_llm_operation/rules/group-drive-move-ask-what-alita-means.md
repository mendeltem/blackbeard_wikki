---
id: group-drive-move-ask-what-alita-means
typ: regel
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-17
herkunft: Clé (Hermes, remote profile) 2026-10-17, disk cleanup on the workstation; user asked to "move the MATLAB installer and the models to Alita"
verweist_auf: [remote-model-gets-only-data-free-skills-and-redacted-text]
---

# Before "move X to Alita": find out whether Alita is a folder or a drive

## Aussage
1. "ALITA" is not a working folder on the workstation. It is the Charité group drive, reachable over the wiki hub
   (`ssh temuuleu@s-csb-wiki-hub.charite.de`, path `CSB_NeuroRad/temuuleu/ALITA`, mounted there as
   `//s-vfs-mgd03.charite.de/ag-csb_neurorad$`). The workstation itself is called Alita (`Alita-MS-7D91`) -- on it,
   "move to Alita" is a no-op. Search the wiki and the skills before searching the disk.
2. A profile that runs on a remote model may not mount or read the external-disk mount point under `/media`: the data
   guard refused that location outright, because cohort data lives there. Work on the group drive therefore goes by
   `scp`/`rsync` -- from the local profile or by hand, not from the remote one.
3. Check the space on the target first. The group drive is a shared 12 TB volume that was 84 % full (2.0 TB free) on
   2026-10-17, while ALITA itself holds 126 GB (DATA 79 GB, ARCHIVE 28 GB, QUALITY_CONTROLL 18 GB). It is not a
   parking space for 70 GB of model weights.
4. "Move" on the group drive means copy, verify by checksum, then report -- never report done from the `rsync` exit
   code. Scripts do not delete there; the user edits files (xlsx) in place, so fetch, extend, copy back with
   `--update`. Source: the `alita-storage` skill.
5. A password typed into the chat is burned. Interpolating it into a shell command is refused by the permission
   classifier as a brute-force/credential pattern (`sudo: a password is required` even with `-S`, plus a block on the
   first attempt), and the secret stays in the transcript and the logs. Say so and ask the user to change it; hand
   over the finished `sudo` lines instead of running them.

## Trägt
Own run 2026-10-17 on the workstation: `find ~ -maxdepth 4 -iname 'alita*'` returned only name-adjacent hits
(`~/.MATLABConnector/Alita-MS-7D91`, `modelle/...`), while `ALITA` in capitals existed solely in the Claude Code skill
`~/.claude/skills/alita-storage/SKILL.md` (2026-08-28) -- one grep of the skill folder answered what the disk search
could not. Key login to the hub works without a password (`ssh -o BatchMode=yes ... 'echo KEYLOGIN-OK'`), so a transfer
needs no credentials in the command. `df` on the group drive: 12 TB, 11 TB used, 2.0 TB free (84 %).

## Trägt nicht
The entry does not make a transfer safe by itself: the best move target for publications is a public archive
(GitHub/Zenodo), and the group drive holds pseudonymised patient data, so what goes there must already be cleared for
it. Rule 4 covers the checksum discipline, not the decision which files belong on the group drive at all.

## Bruchindikator
A script that carries model weights onto the group drive, or a session report that says "moved" without a matching
checksum list on the target.

## Ablesung
`~/.claude/skills/alita-storage/SKILL.md` (2026-08-28, group drive `S:\AG\AG-CSB_NeuroRad\temuuleu\ALITA`, QC/result/HPC
helpers `ablegen-alita`, checksum recipe). Wiki:
[the-local-mirror-is-the-source-of-the-qc-stick](../../mri_qc_viewers/rules/the-local-mirror-is-the-source-of-the-qc-stick.md)
(2026-10-12). Own measurements 2026-10-17 (find/grep over `~`, `ssh temuuleu@s-csb-wiki-hub.charite.de`,
`df -h` = `//s-vfs-mgd03.charite.de/ag-csb_neurorad$ 12T 11T 2.0T 84%`, `du -sh` per ALITA subfolder).
