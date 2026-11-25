---
id: agent-skills-what-they-give-and-what-they-cost-2026-11
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-24
herkunft: online research on user request 2026-11-24 (sources from 11/2024 on, each opened on 2026-11-24); own counts, two own skills, an own with/without comparison and an own trigger test the same day
verweist_auf: [skill-routes-first-and-closes-its-checklist, explanation-video-is-the-standard, overlay-house-colours-and-picture-quality]
---

# Agent Skills: cheap to load and shared by all our agents, but only as good as the description, the size and the test

## Aussage
1. **What it is.** A skill is a folder with `SKILL.md` and optional `scripts/`, `references/`, `assets/`. The header has
   two required fields: `name` (at most 64 characters, lower case, digits, hyphens, equal to the folder name) and
   `description` (at most 1,024 characters: what it does and when to use it) [1].
2. **Three loading levels.** Name and description of every skill at the start of a session (about 100 tokens each);
   the body when a task matches (recommended under 5,000 tokens and under 500 lines); scripts and reference files only
   when a step needs them, and a script is run, not read [1][2][3].
3. **One format for many agents.** Introduced in October 2025 [2], an open standard since, given to the Agentic AI
   Foundation on 2026-10-22; more than 70 agent platforms read it [5]. On one workstation here, Claude Code [4],
   Hermes [8] and Codex or OpenCode [7] read the same folders.
4. **Measured gain, with conditions.** SkillsBench, version 4: 87 tasks in 8 domains, 18 model and harness
   configurations, average pass rate 33.9 % without and 50.5 % with curated skills; focused skills with at most 3
   modules beat larger bundles. Version 1 (86 tasks, 7 configurations): skills written by the models themselves gave
   no benefit on average [12].
5. **Risks of foreign skills.** Pattern scan of 31,132 public skills: 26.1 % with at least one vulnerability pattern
   (patterns, not confirmed attacks) [9]. 98,380 skills examined, 157 confirmed malicious [10]. Instructions hidden in
   skill files succeeded in up to 80 % of attempts against frontier models [11]. Consequence here: write skills
   ourselves; read a foreign skill and its scripts before installing.
6. **A skill is advice, not a lock.** What must hold every time belongs in a hook or in the tool itself [4].
7. **Own comparison with and without a skill** (skill [film-making](../../../tools/skills/film-making/README.md),
   2026-11-24, one run per cell): both sides passed all checkable statements in both cases (9 of 9, 8 of 8). In the
   build case the run with the skill used 123,452 instead of 159,879 tokens and 21 instead of 36 tool calls; in the
   planning case it saved nothing (134,812 against 129,940 tokens). The agent without the skill found the same rules
   in an older skill, this wiki and 15 to 18 memory notes. On a workstation with a full memory the gain of a skill is
   therefore one short, testable place and the same rules for agents without that memory, not more correct results.
8. **Own trigger test.** Ten fresh sessions, one request each, ending with "first tell me your plan in 5 lines", only
   the skill tool offered. With the first descriptions, 3 of 7 matching requests loaded the skill (film 2 of 4, overlay
   1 of 3; two of the four misses named the skill or its content in the plan without opening it), 3 of 3 near misses
   stayed away. After adding one sentence to each description ("Load it before planning or touching such work ..."),
   7 of 7 loaded and 3 of 3 near misses still stayed away.
9. **Own count of one home-built agent loader.** It kept the first 200 characters of a description and read the
   header line by line: of 19 linked skills, 12 descriptions were cut, 2 showed only ">" (a description that
   continues on the next line), 5 were complete; 11 of 30 existing skills were not linked. A skill can be installed
   and still be invisible. Repaired later the same day (24.11.2026): the loader now reads plain, quoted, folded
   and literal values, keeps a description whole up to 1,024 characters (the limit of the format) and marks a longer
   one; after it all 21 linked skills entered the prompt complete, at a cost of about 1,200 tokens more per system
   prompt (own run, 24.11.2026). Check that found it: print the skills block of a real system prompt and compare it
   with the SKILL.md files.
10. **Where a rule belongs.** For every session: the always-loaded instruction file, kept short. Know-how for one kind
    of task: a skill. Never to be broken: a hook or the tool. The one-off part of a task (goal, data, how we see that
    it is finished) stays in the prompt; no skill can know it.
11. **Own review of all 39 skills of one workstation (24.11.2026, reading only, no skill run on a task).** Each skill
    file was read in full against seven points (description, instructions, check before done, failure section,
    outdated content, overlap, size and focus); every finding had to rest on a passage of the file, and a program
    checked that the passage occurs there word for word. Verdicts: 1 good, 18 usable, 15 "needs work", 5 outdated;
    187 findings. Skills with at least one finding per point: outdated content 32, instructions 30, overlap 26,
    check before done 15, failure section 11, size and focus 11, description 9. The size limits of the format were
    kept by all 39, so counting lines and characters alone would have passed every one of them. The three causes
    behind most findings: (a) the agent program was replaced, the skills were not: they still call tools and
    services of the earlier program; (b) the sandbox was tightened to local connections only, and skills that
    fetch from the internet were not adapted; (c) two skills for the same job, written at different times
    (often one per language), now contradict each other in a parameter. A skill ages with the harness around it,
    not with its own text.
12. **Repair of the 20 skills judged "needs work" or "outdated" (24. and 25.11.2026, own run).** Four repair passes
    in parallel, each on about five skills, changing only the instruction texts (backup first, nothing removed or
    merged); every command a text newly names had to exist on the machine. Result: 94 of 98 findings repaired, 4 left
    open with a reason (a data area the repair may not read, a link only the researcher sets, a page feature without
    code, an author name nobody can decide from the machine). What the repair showed: (a) "repaired" means the text
    was changed for that finding, not that the skill was run on a task; the verdicts were therefore not changed.
    (b) Two passes wrote opposite statements about what a segmentation tool puts into one label, each sure of it,
    in two skills for the same step; reading the label lists of the installed tool settled it (the label is not in
    them). A parallel repair needs one reading pass over all changed texts afterwards, and a claim about a tool's
    output is checked against the tool, not against another skill. (c) The repair produced about 40 decisions that
    only the researcher can take (merge two skills, retire one, who may restart a service); a text repair cannot
    close those, it can only list them.

## Trägt
All opened on 2026-11-24.
1. Agent Skills specification. <https://agentskills.io/specification> *Summary: format, header fields with limits, the three loading levels and their sizes.*
2. Zhang B, Lazuka K, Murag M. Equipping agents for the real world with Agent Skills. Anthropic Engineering, 2025-10-16. <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills> *Summary: the article that introduced skills and progressive disclosure.*
3. Skill authoring best practices. Claude platform documentation. <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices> *Summary: description with what and when, body under 500 lines, scripts for fixed steps, test with real tasks.*
4. Extend Claude with skills. Claude Code documentation. <https://code.claude.com/docs/en/skills> *Summary: where Claude Code looks for skills and how they are called.*
5. Donating Agent Skills to the Agentic AI Foundation. Anthropic, 2026-10-22. <https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation> *Summary: the standard goes to a foundation; more than 70 agent platforms read it.*
6. Willison S. Agent Skills. 2025-12-19. <https://simonwillison.net/2025/Dec/19/agent-skills/> *Summary: an outside view on why the simple folder format spread across tools.*
7. Build skills. OpenAI Codex documentation. <https://learn.chatgpt.com/docs/build-skills> *Summary: the same folder format in another coding agent.*
8. Skills system. Hermes Agent documentation, Nous Research. <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills> *Summary: skills folder and external folders.*
9. Liu Y et al. Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale. arXiv:2601.10338, 2026-01-15, preprint. <https://arxiv.org/abs/2601.10338> *Summary: pattern scan of 31,132 public skills, 26.1 % with a vulnerability pattern.*
10. Liu Y et al. "Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild. arXiv:2602.06547, 2026-02-06, preprint. <https://arxiv.org/abs/2602.06547> *Summary: 98,380 skills, 157 confirmed malicious.*
11. Schmotz D, Beurer-Kellner L, Abdelnabi S, Andriushchenko M. Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks. arXiv:2602.20156, 2026-02-23, preprint. <https://arxiv.org/abs/2602.20156> *Summary: hidden instructions in skill files, up to 80 % success.*
12. Li X et al. SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks. arXiv:2602.12670, version 4 of 2026-06-14 (version 1 of 2026-02-13: <https://arxiv.org/abs/2602.12670v1>), preprint. <https://arxiv.org/abs/2602.12670> *Summary: with and without skills, 33.9 % to 50.5 %; small focused skills beat bundles; self-written skills no average benefit.*
13. Improving skill-creator: test, measure, and refine Agent Skills. Claude blog, 2026-03-03. <https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills> *Summary: tools for testing a skill and its description with repeated runs.*
14. Evaluating skill output quality. Agent Skills documentation. <https://agentskills.io/skill-creation/evaluating-skills> *Summary: eval cases with checkable statements, comparison with and without the skill.*

Own runs 2026-11-24: skill counts on one workstation (100, 30 and 7 skill files in three agents' folders before the
two new skills); the comparison in point 7; the trigger test in point 8 (headless sessions of Claude Code).
The review in point 11: four reading passes over 39 skill files, some findings confirmed by a read-only look at the
machine (does a named tool, file or service still exist); the reading passes may differ a little in strictness.
No DOI beyond the arXiv numbers and no PMID: none of the sources is indexed in PubMed.

## Trägt nicht
Sources 9 to 12 are preprints without peer review; only abstracts and version notes were read, not the full papers.
The own comparison has one run per cell and one skill; the trigger test has one run per request and asks for a plan
only, which is harder than a real task in which the skill can still load when the work starts. Nothing was tested
with agents other than Claude Code. Claims that could not be confirmed were left out (for example a count of
"341 malicious skills" that circulates without a source that could be opened).

## Bruchindikator
A repeat with several runs per cell shows no saving in the build case; a later version of an agent loads skills
without regard to the description; the format changes its header fields.

## Ablesung
Before writing a skill: is the work recurring, and is there a script-shaped part? Write the description as what +
when + when not, with the words the user really types, and add "load it before planning". Keep the body short, put
fixed steps into scripts, write 2 to 3 eval cases, run them with and without the skill, and test the description
with a few fresh requests and near misses. After every change of the agent program, the sandbox or a service: search all
skill files for the tool, command and service names that went away, and merge twin skills instead of keeping both. Skills of this wiki: [tools/skills](../../../tools/skills/INDEX.md).
