---
id: three-data-classes-decide-what-may-leave-the-institution
typ: regel
status: vorschlag
thema: knowledge/agent_coordination
stand: 2026-10-21
herkunft: user decision 2026-10-21 ("drei verschiedene klassen": fully open / institution-usable / completely private)
verweist_auf: [remote-model-gets-only-data-free-skills-and-redacted-text, public-code-knows-no-dataset]
---

# Three data classes decide what may leave the institution

## Aussage
Every dataset gets exactly one class before any agent touches it. The class decides the route, not the tool and not the
question. This is a main rule: it applies to every area of this wiki, not to one project.

1. **Class 1 - fully open.** No registration, no data use agreement; open challenge data (e.g. VALDO, the WMH
   challenge of the MICCAI line). May go anywhere open data may go: public GitHub, any cloud, any remote model, any
   agent. The limit is the licence, not the route - if a platform forbids redistribution, the platform copy stays out
   even though the data is open.
2. **Class 2 - institution-usable, access-restricted.** Access was granted to the institution under a data use
   agreement or registration, and that grant is what permits processing. Example: HCP-Aging (AABC). Its terms allow a
   local copy "for non-commercial research use" and allow sharing **within my institution (e.g. on a shared server)**
   under the same terms, with every individual user bound. So the institutional hub (Cle, Charite-internal) **may**
   process class 2. Not permitted: GitHub, public cloud, external APIs, redistribution outside the institution.
3. **Class 3 - completely private.** Own patient cohorts. The data stays local: no case on GitHub, no case in any
   cloud, institutional one included. Local profile and local model only.

The class belongs to the **data**, not to the **task**. This is the decisive point: a class-3 job is not
automatically a local job. Thinking, reasoning, planning and coding about class-3 work contain no patient data as
long as no case id, image, path or report sentence enters the prompt, and that part belongs on the institutional hub
(Cle) like any other class-2 work. Only the piece that actually has to read the data runs in the local profile.

So every class-3 task is cut in two before it starts:

- **Local, unavoidable:** reading the images/records, computing metrics, comparing segments, extracting the numbers.
  Here the patient data exists and must not leave the machine. Keep this part as small as it can be made.
- **Cle, everything else:** the design of the method, the code, the pipeline, the evaluation logic, the write-up.
  These consume a *result* (an aggregate, a redacted line) and need no case. Against a data-free contract they are
  class-2 work and go to Cle - no reason to burn local capacity on them.

Minimise the local share, maximise the Cle share. The test is not "does this touch the dataset" but "does this
prompt contain patient data": if the prompt is data-free, it runs on Cle even when the surrounding job is class 3.

## Where the scheme sits next to established practice

The nearest established counterpart is the **Turing Data Safe Haven** sensitivity tiering (Tier 0-4, preprint
arXiv:1908.08737, docs fetched 2026-10-21). Roughly: Tier 0 "personal data ... for eventual publication" maps to
class 1, Tier 2 (pseudonymised, no outbound internet) to class 2, Tier 3 (personal data, restricted networks) to
class 3. Two differences matter:

1. The tiers judge by **harm on disclosure and degree of pseudonymisation**, and they count what is *generated*
   ("processed, combined or generated") - hence the inheritance rule above. This scheme judges by **route**; the
   inheritance clause is what keeps the two from drifting apart.
2. Established trusted research environments (Turing, UK Biobank RAP, SAIL, the Five Safes airlock) control the
   **output**: only summary results pass a statistical disclosure check. This scheme's class 2 has no such output
   check - it says "may compute here". That is a real gap: class 2 permits processing, it does not by itself certify
   that the result is releasable.

DUO gives the vocabulary to say which restriction is meant (see above); FIDES (Microsoft Research, arXiv:2505.23643)
is the closest published idea to enforcing such labels against agent tool calls - labels on the data decide which calls
are allowed. No scheme that tiers *datasets* to gate *agents* was found in the research-data field; that part looks
unpublished.

The class is a property of the data, not of the folder it happens to sit in: a class-2 copy stored outside the usual
data location is still class 2, and sitting next to private cases does not promote it to class 3.

## Derived artefacts and the person behind "institution"

The class is inherited, not reset. An artefact carries the **maximum class of its inputs**: a mask, an overlay, an
embedding, a quality-control page, a log line or a model trained on class-3 data is itself class 3. A vector store has
the class of its source, because embeddings can be inverted back towards the input (Morris et al. 2023,
arXiv:2310.06816, recovered 92 % of 32-token inputs). Pushing such an artefact to a repository publishes the data
indirectly, so every artefact needs one line recording its origin class, and the push check reads that line.

"Institution" is a set of persons, not a building. Inside the institution, access to patient data is bound to a role
(GDPR Art. 9(3), under professional secrecy), not granted to every instance that happens to sit on the same campus.
Cle counts as institutional because the grant names the institution and the group behind it; a copy handed to an
unrelated instance still needs its own basis. "Class 2 may run here" is therefore only as good as the name attached to
*here*.

Class 2 is also the softest of the three and must be looked up per dataset. Class 1 is bounded by a licence, class 3 by
law, but class 2 is a **method label** whose reach is set by the individual data use agreement. Two labels from the
GA4GH Data Use Ontology (DUO) frame it: `DUO:0000028 IS` *institution specific restriction* ("use is limited to use
within an approved institution", verified in `duo.csv` 2026-10-21) fits; `DUO:0000015 NMDS` *no general methods
research* does not - it forbids method development such as software or algorithms, and that collides with the wiki rule
that public code knows no dataset. Assume class 2 is heterogeneous until the agreement says otherwise.

## Trägt
The scheme corrects a real over-block. HCP-Aging was treated as if it were private ("local only") because it carries an
access restriction - but its own terms allow institutional sharing, so the institutional hub may use it. Blocking it
was stricter than the contract requires and cost usable work. In the other direction the scheme keeps the guard's
purpose intact: private cases still never leave the local profile.

## Trägt nicht
The class must be looked up, not inferred. "Open" (class 1) and "usable here" (class 2) are different questions, and an
access restriction alone does not settle which one applies - read the terms. Class-1 and class-2 data also carry case
ids that look like subject ids; a guard that blocks on id shape alone will fire on them, so the guard has to be
class-aware rather than pattern-only.

The split also has a cost: it only works if the seam between "has to see the data" and "consumes only a result" is
drawn honestly. A local step that quietly hands whole records to Cle is not a split, it is a leak. And a plan that
keeps reasoning local "to be safe" defeats the rule - being stricter than the contract costs capacity the same way
over-blocking costs work.

The enforcement is also weaker than it looks, and two of the weak points are measured (own runs 2026-10-21):

- **A proxy log cannot see the main route.** `no_proxy` on this machine contains `.charite.de`, `10.0.0.0/8` and
  `141.42.0.0/16`, so requests to Cle bypass the proxy entirely. Any evidence built on proxy traffic is blind exactly
  where the institutional path runs. The strong version is an isolated network namespace with loopback only, plus a
  counter-test in the same run: `curl` to Cle must fail. Then the path out does not exist and nobody has to trust a log.
- **The network fence is written but unproven here.** `werkzeuge/netzsperre/netzsperre.sh` states about itself
  "GESCHRIEBEN AUF VICTUS, NICHT AUF ALITA GELAUFEN". It exists; on this machine it has never been run. Built is not
  the same as in force.
- **The guard's rejections have no target values.** `guard/log/vorgaenge.jsonl` held 255 entries (156 rejected,
  99 sent). That shows the guard does not reject blanket-wise; it does not show that its decisions are *right*, because
  nothing states what the right answer would have been. A guard that always says no looks identical by count.

So the guard needs a self-test, not a traffic count. With synthetic values only, expect reject-pass-reject:
an invented id in the text must be rejected; a public challenge id next to plain numbers must pass (proving the guard
is not blanket-rejecting); the same id split up, base64-encoded, in a filename or in a NIfTI `descrip` must be
rejected. Then a mutation probe: switch off one rule in a *copy* of the guard and the series must go red - otherwise
the test is vacuous. Finally reconcile the counts: requests sent by the sending layer must equal the entries marked
sent in the log; any mismatch means a path around the guard.

The most likely false assurance, all three measured or documented above: a proxy log that never sees the institutional
route, a redaction that checks only text while ids also sit in filenames and image headers, and a "local" profile that
quietly points `base_url` outward. The strongest counter-evidence is the counter-test, not the protocol.

## If an agreement forbids AI, it forbids it locally too

The route rules above answer "may this leave the institution". They do not answer "may a model touch this at all", and
those are different questions. An agreement can forbid AI processing outright - local model included, institutional
machine included. When one does, obey it locally.

The reasoning is not legal caution, it is arithmetic: following such a clause costs almost nothing (run the step by
hand, script it, or leave it), while ignoring it risks the whole data access. There is no version of "we only used the
local model" that the data provider will accept as compliance with a no-AI clause. Local execution is a *route*, not an
exception.

This is why the class is not a substitute for reading the agreement. A dataset whose terms contain such a clause has no
usable class under this scheme: it is not class 1 (not open), not really class 2 (the institutional route is allowed but
the processing is not), and not class 3 (it is not ours to decide). Read the agreement first, assign the class second.

**Still open:** two claims that real agreements do this - ADNI forbidding AI tools including local ones, HRS forbidding
LLM processing - could not be verified from this machine (the ADNI PDF is blocked by the proxy, the HRS page returns no
text; see Ablesung). Until they are read, treat "an agreement may forbid AI" as a live possibility to check per dataset,
not as a settled label for any named dataset.

## Bruchindikator
A class-2 or class-3 case reaches a public repository, a public cloud or an external API. A class-2 dataset is refused
on the institutional hub on the grounds of "patient data" although its terms permit institutional use. A data-free
planning or coding prompt for a class-3 job runs in the local profile instead of Cle, or a local step forwards raw
records rather than an aggregate. An artefact (mask, embedding, log, quality-control page, trained weights) is pushed
without a class line, or with a lower class than its inputs. Class 2 is treated as one uniform permission when its own
agreement is narrower. A release decision rests on proxy traffic although the institutional route bypasses the proxy,
or on a guard's rejection count although no target values exist. Case-level content (ids, paths, values, image headers)
is written into a log, cache or agent session store beyond the run that needed it, is kept because it "might be useful
later", or is placed next to the data instead of in the run's own temporary space.

## Ablesung
VALDO (registration and grand-challenge terms of service): https://valdo.grand-challenge.org/ ,
https://grand-challenge.org/policies/terms-of-service/ . WMH challenge: https://wmh.isi.uu.nl/ . HCP-Aging Data Use
Terms, fetched 2026-10-21: https://www.humanconnectome.org/study/hcp-lifespan-aging/data-use-terms - wording quoted
above is from there ("solely for academic research ... at a non-profit or government institution", "sharing of the Data
OUTSIDE of my institution is NOT PERMITTED", "share the Data WITHIN MY INSTITUTION (e.g., on a shared server)").
Class-3 rule from the cohort-guard, own runs 2026-10-21.

Prior art and vocabulary, checked 2026-10-21 by three separate research passes plus own verification: Turing Data Safe
Haven sensitivity tiers (https://data-safe-haven.readthedocs.io/en/latest/overview/sensitivity_tiers.html ,
preprint arXiv:1908.08737); UK Biobank research analysis platform output rules
(https://community.ukbiobank.co.uk/hc/en-gb/articles/31972311370013 ) and airlock plan
(https://www.ukbiobank.ac.uk/about-our-data/protecting-the-data/data-security-updates/); SAIL (PMC8142954); Five Safes
(vendor description only, https://lifebit.ai/blog/what-is-five-safes-framework/ , official ONS/HDR-UK page unverified);
GA4GH DUO, labels read from the source file
(https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.csv - `DUO:0000028 IS`, `DUO:0000027 PS`, `DUO:0000026 US`,
`DUO:0000007 DS`, `DUO:0000021 IRB`, `DUO:0000022 GS`, `DUO:0000015 NMDS`, `DUO:0000042 GRU`, `DUO:0000004 NRES`); NIH
dbGaP Data Use Certification, cloud service provider clause from search excerpts only, PDF returned 403
(https://www.grants.nih.gov/node/1245); HIPAA Limited Data Set agreement
(https://contracts.med.wisc.edu/wp-content/uploads/sites/1494/2025/02/Data-Use-Agreement-for-Disclosure-of-LDS.pdf);
FIDES, Microsoft Research (https://arxiv.org/pdf/2505.23643v2). **Unverified, needs network access:** claims that the
ADNI agreement forbids AI tools including local ones (PDF https://adni-lde.loni.usc.edu/wp-content/themes/adni_2023/documents/ADNI_Data_Use_Agreement.pdf
blocked by the proxy, CONNECT 503) and that HRS forbids LLM processing (https://hrsdata.isr.umich.edu/node/72486
returned no text). If those hold, `IS` is the wrong label for class 2 and the class is contractual per dataset. Do not
treat the class-2 wording above as settled until they are read.

Embedding inversion: Morris et al. 2023, arXiv:2310.06816 (recovered 92 % of 32-token inputs; arXiv preprint, not
peer-reviewed). Re-identification from face reconstruction of head MRI: Schwarz et al. 2019, N Engl J Med, PMID
31644852, "Identification of Anonymous MRI Research Participants with Face-Recognition Software" - title, authors,
journal (N Engl J Med 2019;381:1684-1686) and DOI 10.1056/NEJMc1908881 verified against PubMed 2026-10-21. It is a
brief report with no abstract, so its specific figures were **not** read here; do not quote a number from it without
opening the paper. A demographic-uniqueness claim (Rocher et al. 2019, Nature Communications)
reached this wiki through a research pass but its PMID could **not** be verified on 2026-10-21 and the citation was
removed; do not restore it without reading the paper.

**Correction, same day:** an earlier version of this reads section carried the PMIDs 31657887 and 31427575 for Schwarz and
Rocher. Both are wrong - 31657887 is a surgical-residency burnout paper (Hu YY, NEJM) and 31427575 is an inner-ear gene
transfer paper (Tan F, Nat Commun). They came from a research pass and were not checked before being written down. The
lesson is in the rule itself: a PMID is not evidence that the source says what one believes it says.

## Verknüpft
[remote-model-gets-only-data-free-skills-and-redacted-text](../../local_llm_operation/rules/remote-model-gets-only-data-free-skills-and-redacted-text.md)
