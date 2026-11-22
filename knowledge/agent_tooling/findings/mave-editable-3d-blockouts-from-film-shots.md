---
id: mave-editable-3d-blockouts-from-film-shots
typ: befund
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-11-22
herkunft: pointer to an external preprint, noted on request on 2026-11-22 for later use; arXiv record, project page, code repository and dataset card read on 2026-11-22; the PDF itself was not read, nothing was run
verweist_auf: [model-hub-writes-explainer-films-under-a-harness]
---

# MAVE: an agent rebuilds a film shot as an editable 3D scene in Blender, each step checked against measured evidence (preprint, code not released yet)

## Aussage
1. **What it is.** MAVE (Chang et al., 2026, arXiv preprint) takes a film shot and gives back an editable Blender scene made of named simple shapes ("blockout": rough set, camera path, where the people stand and move) plus a blockout video aligned frame by frame with the shot.
2. **How it works, in three stages.** (a) *Metric observation*: cameras, human motion and geometry are recovered from the footage in one shared frame with real-world scale. (b) *Agentic modeling*: a language-model agent builds the scene in Blender under these measured constraints. (c) *Evidence-based verification*: programmatic checks compare each step with the measured evidence and steer the next correction.
3. **Numbers the authors report** (their own benchmark, not reproduced): MAVEBench has 50 film shots and 416 keyframes and scores camera motion, spatial layout and character blocking. Against the same agents without MAVE, the overall score rises by 27.5 to 41.1 points for three agents. With one of the agents (DeepSeek-1017) the score is 73.2 at USD 0.054 API cost per shot, and reconstruction time falls by 53 %. The measuring stage adds 1 min 28 s per shot (project page).
4. **State of release on 2026-11-22.** Paper and project page are public. The code repository holds folders but calls the implementation "coming soon", has no licence file ("open-source licence to be announced") and no install steps. The annotation dataset on Hugging Face is an empty scaffold; film media sit in a separate gated repository and stay with their rights holders. MAVEData-3K (3,000 pairs of blockout and video) is announced, not released. Model weights are not mentioned.
5. **The transferable pattern** is the order: measure first, let the agent build only inside the measured constraints, and check every step by program against the measurement instead of asking the agent whether it looks right. This is the same lesson as the rule check in the loop for model-written films in this wiki.

## Trägt
- Chang Y, Yang J, Shao J, Wang X, Fan Z, Xu R, Lu M, Wang X, Zhu Z (2026). MAVE: Reconstructing Editable 3D Blockouts from Film Shots. arXiv:2611.22464 (cs.CV, cs.AI), v1 2026-11-17, v2 2026-11-18. DOI [10.48550/arXiv.2611.22464](https://doi.org/10.48550/arXiv.2611.22464). No PMID (not indexed in PubMed). Record checked 2026-11-22: title, author order and dates as given here. *Summary: benchmark of 50 film shots, a three-stage video-to-blockout method, gains of 27.5 to 41.1 points over the bare agents, a planned dataset of 3,000 pairs.*
- Project page: <https://yfchang-cv.github.io/MAVE/> (read 2026-11-22). *Summary: method in three stages, example shots, the timing and cost figures of point 3.*
- Code repository: <https://github.com/yfChang-cv/MAVE> (read 2026-11-22). *Summary: release list with paper and page ticked, code, annotations and data open; no licence file.*
- Dataset card: <https://huggingface.co/datasets/yfChang/MAVE> (read 2026-11-22). *Summary: "empty scaffold for now", licence label "research-annotations" without terms; film media in a separate gated repository.*

## Trägt nicht
A preprint without peer review, two versions within two days. All scores come from the authors on their own benchmark; no independent run exists and none was done here. The figures in point 3 are taken from the abstract and the project page, not from the tables of the PDF (unverified against the full text). Which language models and which programs the pipeline needs to run, the Blender version, the GPU need and whether a local model can drive the agent are not stated in the sources read. Without a licence the code may not be reused even once it appears. Film clips are third-party material: nothing from them belongs in own films or pages.

## Bruchindikator
The code is released with a licence that excludes the intended use, or needs paid cloud agents only; an independent run on other footage does not reach the reported gains; the measuring stage fails on footage without people or with a still camera.

## Ablesung
Come back when the repository's release list ticks "code". Then read the licence first, then the requirements (agent model, Blender version, GPU), then try one short public clip. Until then only the pattern is usable: measured constraints first, agent second, a programmatic check after every step.
