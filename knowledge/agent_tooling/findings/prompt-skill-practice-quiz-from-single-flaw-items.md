---
id: prompt-skill-practice-quiz-from-single-flaw-items
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-22
herkunft: own build and tests of a public browser trainer for prompt writing (github.com/mendeltem/Prompt_trainer), with a literature search on skill tests and feedback, 2026-11-22
verweist_auf: [check-every-cited-source-and-summarise-it]
---

# A prompt-skill quiz built from single-flaw drafts, with a writing mode beside it

## Aussage
1. No validated test of prompt-writing *performance* was found. Published scales measure self-rated competence or self-efficacy (Prompt Engineering Competence Scale, n = 437; a teacher self-efficacy scale as a preprint). A quiz built for practice should say "practice, not a certification".
2. Changing questions come cheaply from complete good examples: one model prompt per situation, split into five sentences (task, source, limit, "Done when …", form), and nine flaw operators that change exactly one part (task as a question, source or limit or done-sentence or form removed, done-sentence written as a fact, an exact phrase replaced by a vague one, a second task appended, an irrelevant fact inserted). Five question types (best of four prompts, biggest gap, best fix, ambiguous phrase, sentence that can go) give over 1000 distinct questions from 42 situations. A program checks every situation x flaw x type for four distinct options and exactly one correct one.
3. Every option carries its own explanation, and an optional "try again until correct" mode counts only the first try. This follows the feedback research: explained feedback beat right/wrong and correct-answer feedback in a meta-analysis, and answer-until-correct with explanations ranked first in a network meta-analysis.
4. A multiple-choice scenario samples judgement, not the performance itself (situational judgement test literature). The trainer therefore has a writing mode: the learner writes a prompt for a situation, gets rough pattern hints in the browser (ends with "?", starts with "Can you", no "Done when", vague or wish words, unclear boundaries such as "from 5", file from the situation not named, irrelevant fact copied), ticks a self-check on the six criteria and sees the model answer. No AI service is needed; the hints are labelled as rough.
5. The quiz score uses the same six weighted criteria (goal 25, scope 20, done and form 20, unambiguous 15, one task per sentence 10, concise 10) as an earlier chat training, so the percentages can be compared.
6. Web pitfall found by the browser test: a class rule `display: inline-flex` on buttons overrides the HTML `hidden` attribute, so a "Next" button meant to appear after an answer was visible from the start. Fix: `[hidden] { display: none !important; }`. The test caught it because it checked visibility, not the attribute.

## Trägt
Own build 2026-11-22: static HTML/CSS/JavaScript on GitHub Pages, https://mendeltem.github.io/Prompt_trainer/ (repo https://github.com/mendeltem/Prompt_trainer, MIT code, CC BY 4.0 content). Node 22.22.2 `node --test`: 9/9 (all 42 situations, every combination, three runs with no shared question, weighting, hints clean on all model answers). Playwright 1.62.1 and the newest npm Playwright with Chromium headless shell v1255: 12/12 locally, from a fresh clone and on the live site (three runs shared 0 questions; retry mode; phone width; dark mode; no page errors).
Sources (read as abstracts or summaries, not full text):
- Van der Kleij FM, Feskens RCW, Eggen TJHM (2015). Effects of feedback in a computer-based learning environment on students' learning outcomes: a meta-analysis. Review of Educational Research 85(4):475-511. DOI 10.3102/0034654314564881 (DOI from memory, unverified); not in PubMed. Shows: effect sizes 0.49 for elaborated feedback, 0.32 for the correct answer, 0.05 for right/wrong.
- The Impact of Computer-Based Feedback Strategies on Students' Learning: A Network Meta-Analysis (2024), HAL hal-04607898 (authors unverified). Shows (secondary summary): 46 studies; answer-until-correct with explanations ranked first; only elaborated feedback helped learners with low prior knowledge significantly.
- Westacott R et al. (2023). Automated Item Generation: impact of item variants on performance and standard setting. BMC Medical Education. DOI 10.1186/s12909-023-04457-0, PMID 37697275 (checked). Shows: item variants from one question model compared on performance and standard setting in final-year medical students.
- Lievens F, Motowidlo SJ (2016). Situational judgment tests: from measures of situational judgment to measures of general domain knowledge. Industrial and Organizational Psychology 9(1):3-22. DOI 10.1017/iop.2015.71 (unverified). Shows: SJTs measure procedural knowledge in a low-fidelity written format.
- Zamfirescu-Pereira JD, Wong RY, Hartmann B, Yang Q (2023). Why Johnny Can't Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts. CHI '23. DOI 10.1145/3544548.3581388 (unverified). Shows: 10 participants explored prompts opportunistically and wrote them like instructions to a person.
- Gibreel O, Arpaci I (2025). Development and validation of the prompt engineering competence scale (PECS). Information Development. DOI 10.1177/02666669251336455. Shows: a self-report scale validated on 437 users; the item count differs between sources (unverified).
- Swanson K, Bent D, Ludwig Z, Dakan R, Feller J (2026-02-23). The AI Fluency Index. Anthropic, https://www.anthropic.com/research/AI-fluency-index (read through its redirect to the Claude Academy copy). Shows: in 9,830 Claude.ai conversations, users clarified the goal in 51.1 % and specified the format in 30 % (per conversation, by classifier).

## Trägt nicht
No learner has used the site yet: whether quiz scores rise over runs, and whether they predict better written prompts, is not measured. The difficulty of the generated variants is not measured either, so two runs are not proven equally hard. The writing hints are English pattern checks and miss anything outside their word lists. The feedback studies are about learning in general, not about prompting.

## Bruchindikator
Learners score high in the quiz but their written prompts keep the same gaps (recognition without production); one flaw type is solved far more often than the others (an option gives itself away, for example by length); the hints flag a model answer; a variant set shows large differences in the share answered correctly.

## Ablesung
For a skill quiz without an item bank: start from complete good examples, generate drafts by changing exactly one part, test every combination by program, explain every option, count the first try, and add a mode where the learner produces the thing. Call it practice until it has been validated against real performance. In web UIs that use the `hidden` attribute, add `[hidden]{display:none!important}` and test visibility.
