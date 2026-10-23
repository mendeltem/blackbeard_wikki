---
id: derived-artifacts-carry-their-source-class
typ: befund
status: getragen
thema: agent_coordination
stand: 2026-10-22
herkunft: own run 2026-10-22 (building and exporting data-free prefill packages on Alita)
verweist_auf: three-data-classes-decide-what-may-leave-the-institution
---

# Derived artifacts carry the source class: a KV cache is a copy in number form

## What was found

A prefill package was built from data-free fragments (16 fragments, 19 packages), then an
optional layer was added: precomputed KV caches, one per package, ~1.1 GB each, held under
`system/logs/kvcache/`.

The source fragments passed the outgoing guard. The caches derived from the *same* fragments
were treated differently, and that is the correct reading, not an inconsistency:

- A KV cache is the processed prompt state in number form. It is a copy of the text it was
  computed from, not a summary of it.
- If the source text was cohort-bound, the cache carries that binding even though no cohort
  name is readable in it. The guard blocks by readable content, so it will not catch this.
- Three older caches (`thema-mb-arena`, `thema-valdo-t2s`, `thema-wmh-arena`) belong to themes
  the guard blocks as cohort-bearing. They were excluded from the export for exactly this
  reason, though nothing in them is searchable.

Measured, same run: the file-level cache saves almost nothing. With the running service, a
cold prefix took 4.4 s, the identical prompt right after took 0.4 s, and after a distractor
0.8 s. The whole agent turn is 29-34 s, dominated by process startup. The 21 GB of caches buy
roughly the seconds a warm slot already provides.

## Why it matters

1. **Class inheritance applies to derived artifacts, and it survives redaction.** A mask,
   an embedding, a QC page or a model trained on class-3 input is class 3. A KV cache is the
   same kind of object: it cannot be promoted to "data-free" by showing that no identifier is
   visible inside it.
2. **Guard coverage is by content, not by provenance.** A cache of blocked source material
   passes a content check because it contains no readable strings. So the exclusion has to be
   a rule, not a scan result.
3. **Group drives are a destination, not a sieve.** On a Charite-internal group drive,
   pseudonymised patient data may legitimately live. That is what makes it the wrong place for
   derived artifacts of unknown provenance: the destination permits the material, so nothing
   else will stop it. Only data-free source files belong in a package folder there.
4. **Cost is a separate question from permission.** The caches were dropped from the export on
   both grounds, and the 21 GB mattered less than the class argument. Had they been cheap and
   useful, the class rule would still have excluded them.

## How to check (repeatable)

1. For every derived artifact ask: what was the maximum class of the text that produced it?
   If that is not knowable, treat the artifact as the higher class.
2. Do not try to decide it by grepping for names or identifiers. Absence of a match is not
   evidence of absence of the binding.
3. Export only source-level, data-free material to shared destinations
   (`system/themen/auf-alita.sh` stages only `bausteine/ briefe/ werkzeuge/` and refuses the
   `kvcache/` directory by design).
4. Weigh the speed claim before shipping bulk: measure the warm-slot case first.

## Trägt

- A concrete instance of the class-inheritance rule on a real export, with the destination
  being an internal group drive rather than an external API.
- The distinction between guarding by content (what the guard can do) and ruling by provenance
  (what a person must do).

## Trägt nicht

- The number of caches or the byte sizes are specific to this run; they are not a property of
  the method.
- No claim that the three excluded caches are a leak. They are prompt state of cohort-bearing
  themes kept on the local route, nothing confirmed to have left.

## Bruchindikator

Would be wrong if a KV cache were shown to be a lossy encoding that provably cannot be matched
back to its source content, or if a shared destination were shown to strip provenance in a way
that the class rule already accounts for.

## Ablesung

Before copying any derived artifact to a shared or group destination, name the source class in
one sentence. If the sentence needs a hedge, the artifact stays local.
