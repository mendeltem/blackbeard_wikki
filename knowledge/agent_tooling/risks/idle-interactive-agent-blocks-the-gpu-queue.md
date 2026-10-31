---
id: idle-interactive-agent-blocks-the-gpu-queue
typ: risiko
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-31
herkunft: local agentic system (grossauftrag --abarbeiten, agent_aktiv), incident 2026-10-30/31
verweist_auf: [queue-jobs-inherit-the-supervisors-cgroup-limit]
---

# An idle interactive agent session counted as "agent active" and held the GPU queue for 15 hours

## Aussage
The GPU queue may stop the local language model only when no agent is mid-call (otherwise the agent dies mid-request),
so it waits while any agent process exists. An interactive session opened in tmux sat at its own clarifying question
from 17:11 until the next morning; the queue saw a live agent process and refused to start, about 10 GPU hours were
lost, and every retry logged "agent active" without anyone noticing. Fix: prompt-mode runs always count as active;
interactive sessions only if their session log grew in the last 30 minutes; unreadable state counts as active.

## Trägt
Process list, session-log mtimes and the queue log of the incident; five-case unit test of the idle rule.

## Trägt nicht
A user typing slowly in an interactive session for more than 30 minutes without a model call could be interrupted.

## Bruchindikator
Repeated "agent active, not handed over" lines while the GPU is idle.

## Ablesung
Own incident 2026-10-31. Check the queue actually moves (log + GPU), not only that jobs are queued.

## Verknüpft
[queue-jobs-inherit-the-supervisors-cgroup-limit](queue-jobs-inherit-the-supervisors-cgroup-limit.md)
