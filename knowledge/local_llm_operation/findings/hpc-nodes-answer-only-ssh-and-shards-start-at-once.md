---
id: hpc-nodes-answer-only-ssh-and-shards-start-at-once
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-10-16
herkunft: tests from the institute intranet against the institute SLURM cluster, 2026-10-16
verweist_auf: []
---

# Cluster nodes answer only on SSH from the intranet; a GPU share starts at once, a whole GPU waits

## Aussage
1. From two intranet hosts, the cluster's compute and login nodes accepted only port 22; 8000, 54321 and 443 on the
   nodes were refused ("No route to host"). A service on a node (an LLM API) is therefore reachable from the intranet
   only through an SSH tunnel or a gateway inside the intranet.
2. GPU partition inventory (`sinfo -o "%N %G"`): 20 x A100 40 GB, 7 x A100 80 GB, one node with 2 x L40S 48 GB; each GPU
   offers 4 GRES `shard`s. A job asking `--gres=gpu:1` was scheduled about 9 h ahead; the same job with `--gres=shard:1`
   started within seconds. A training needing ~1.8 GiB fits a share. A model needing a whole 80 GB card competes for 7.

## Trägt
Port probes with bash `/dev/tcp` from two hosts; `squeue --start` and job start times of 2026-10-16.

## Trägt nicht
Queue times change by the hour; the port policy can change with the cluster configuration.

## Bruchindikator
A port probe that connects; `squeue --start` that shows short waits for whole GPUs.

## Ablesung
Own measurements 2026-10-16. SLURM GRES sharding: https://slurm.schedmd.com/gres.html#Sharding (Slurm documentation).

## Verknüpft
-
