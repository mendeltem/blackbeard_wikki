---
id: disk-guard-verified-move-and-compact-literature-search
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-17
herkunft: workstation housekeeping and research tooling, Alita session 2026-10-17
verweist_auf: []
---

# Three small tools: verified move to the group drive, an hourly disk guard, and compact literature search for token-priced agents

## Aussage
1. Copy is not move: the existing group-drive copy tool frees no space. A move tool must copy, compare SHA-256 on BOTH sides
   (the remote host computes its own sums), delete locally only on full equality and leave a note file with target and
   restore command. Refuse raw data folders, folders named by a running process, symlinks.
2. Bug found in its own test: `ps ... | grep -qF path` under `set -o pipefail` reports a MATCH as failure (grep -q closes the
   pipe early, the writer gets SIGPIPE). Use `grep -c` and compare the count.
3. An hourly disk guard (systemd user timer) warns below 50 GB (board + phone, at most every 6 h) and PAUSES (SIGSTOP, not
   stop) long processing services below 20 GB, so the disk cannot hit 0 B; a `--weiter` switch sends SIGCONT. A dry-run
   mode tests both thresholds without side effects.
4. Agents billed per token waste most tokens on raw API answers (50 KB JSON/XML per search). A search tool over free APIs
   (PubMed E-utilities, Europe PMC, OpenAlex, arXiv; Semantic Scholar rate-limits without key, HTTP 429) that prints one
   short block per work (title, authors, year, journal, DOI/PMID, citations, first 300 characters of the abstract) gives
   the same choice at about 3 KB. arXiv answers "Rate exceeded" unless spaced to one request per 5 s.
5. Rules given to one agent do not reach the other: a user rule stored only in the coordinator's memory was unknown to the
   local agent. Each rule that concerns the local agent goes into its own memory file as well.

## Trägt
Tool tests 2026-10-17 (refusals, copy-only, move, restore with checksum check, busy-folder refusal after the fix; guard dry
runs; search runs against all five sources).

## Trägt nicht
Token savings of the search tool are not measured yet (compare the hub's monthly counter per research task).

## Bruchindikator
A move whose remote checksum list differs but the local folder is gone; a guard that pauses services above the threshold.

## Ablesung
- NCBI E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/ ; Europe PMC REST: https://europepmc.org/RestfulWebService ;
  OpenAlex API: https://docs.openalex.org ; arXiv API: https://info.arxiv.org/help/api/ (all checked 2026-10-17)
- own tools werkzeuge/auslagern-alita, platz-waechter, literatur (2026-10-17)
