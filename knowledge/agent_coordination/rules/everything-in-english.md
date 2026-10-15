---
id: everything-in-english
typ: regel
status: getragen
thema: knowledge/agent_coordination
stand: 2026-10-15
herkunft: Mendel, chat on workstation Alita, 2026-10-15 ("ein Hauptregel in wiki sollte alle Arbeiten sollten auf Englisch sein")
verweist_auf: [humans-read-html-agents-write-markdown]
---

# Main rule: all work is in English

## Statement
Everything an agent produces is written in English: wiki entries (title, body, section headings), code, comments,
commit messages, file and folder names, QC pages, tables and their column/sheet names, reports, primers and figures.
The chat with Mendel may stay in German; the artefacts do not. Existing German entries are translated when they are
next touched (no big-bang rewrite); a new entry is never written in German.
Exception: the frontmatter keys and their fixed values (`typ: regel`, `status: getragen`, `stand`, `herkunft`, ...)
stay as defined in templates/knowledge-entry.md, because wiki_maintenance --check validates them.

## Applies to
All agents and chats that write to this wiki or produce files for Mendel's projects.

## Does not apply to
Quotes of what a person said (keep the original wording, add an English gloss if needed); data that arrives in
another language (e.g. German DICOM series names) is kept as it is.

## Break indicator
A new entry, page or table in German, or a translated entry whose numbers no longer match the original.

## Source
Mendel's instruction 2026-10-15; earlier the same rule for outputs (QC pages, Excel, GitHub) since 2026-09-29/10-12.

## Linked
- [humans-read-html-agents-write-markdown](humans-read-html-agents-write-markdown.md)
