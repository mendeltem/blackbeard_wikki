---
id: readme-for-a-research-package
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-16
herkunft: user requests on Alita 2026-10-16 while rewriting the README of cmb_3d_unet_experiments; jehna/readme-best-practices; GitHub Docs "About READMEs"
verweist_auf: [public-code-knows-no-dataset, tests-prove-claims-not-plumbing]
---

# README of a research package: copy-paste blocks, one figure, details elsewhere, hardware last

## Aussage
1. One line what the package does, then one figure of how it works (no second figure that repeats the first).
2. Every command in its own copy block; under it one line what happens and where the output lands.
3. Every block runs verbatim from a fresh clone (examples shipped in the repository, no placeholders in commands that
   are meant to run); check them before every push.
4. As few sections as possible, as many as needed: install, data layout, train, predict, options (short table),
   differences to the method it follows, links, licence and citations.
5. Long material (all options, provenance of defaults, validation) in docs/DETAILS.md, linked.
6. Hardware and software requirements at the very bottom in small print.
7. When a collaborator already uses another tool, mirror its commands, option names and folder layout so that their
   scripts run unchanged; list the differences in a table with measured effects.

## Trägt
The user asked for exactly these points; jehna's template puts a one-line description, "Installing / Getting started"
with copy-paste commands and short sections first; GitHub's own guidance says the README should say what the project
does, why it is useful and how to start, and move longer documentation elsewhere.

## Trägt nicht
Packages for end users without a command line need a different first page.

## Bruchindikator
Readers who cannot run the first block of the README without asking.

## Ablesung
jehna, readme-best-practices, https://github.com/jehna/readme-best-practices (README-default.md). GitHub Docs, About
READMEs, https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes.
Applied in https://github.com/mendeltem/cmb_3d_unet_experiments (2026-10-16).
