# 2026-09-27 — Invariant methods screened; no all-depth certificate

Step `collatz-2026-09-27-014-paired-minimum-literature` completed one
LITERATURE step with outcome EXPLORATION and classification
NOVELTY_UNCHECKED. The exact saved target was preserved in the
[assessment](../drafts/literature/2026-09-27-paired-minimum-invariant.md),
whose decision is now SPECIALIZE. The earlier inverse-arithmetic
assessment was reused for its unchanged scope.

The review read primary statements on real and integer linear invariant
synthesis, general limits of integer invariant inference, and related
Collatz affine-invariant and loop-termination results. It distinguishes
certificate verification from certificate existence, and retains the
limits of real relaxation and bounded coefficient searches. Precise
versions, theorem identifiers, links, applicability comparisons, and
unread leads are in the assessment. Known methods are recorded by
citation; no local invariant, impossibility result, or novelty claim is
added. Mathlib coverage remains not checked.

The main gap is unchanged: compensation by earlier growth has not been
excluded. The analytical three-block theorem and saved depth-11 screen
remain the achieved bounds; neither reaches arbitrary depth. Even a
successful invariant would leave the fixed-start depth estimate and
other block types open. No candidate proof or disproof appeared.

The source review justifies a specified integer certificate test using
both suffix minima and the extra inverse required by the block offset.
Its success and failure criteria are recorded in the assessment. It
does not justify further depth enumeration or an unbounded synthesis
search. This is the third consecutive exploration turn without an
advance or informative negative result. The assessment and stop decision
are complete: this exploration batch ends, while the screened target
is retained for resumption under the shared policy. Counters and runner
state are not reset; this is not a mathematical rejection of all paired
invariant methods. The sole current action remains in PROGRESS.md.

Existing unfinished changes, including L012 and the paired-state
scripts and output, were preserved. This turn edits only the assessment,
PROGRESS.md, and this history entry. PROOF.md and DAG.md are unchanged
because no mathematical statement or input changed. No mathematical
calculation was performed, and no mathematical script was run.

Validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with 12 nodes, 12 unique edges, valid links, and compact
overviews. A separate read-only check passed the single-line assessment
fields, step fields, exact target/review match, and exploration count.
All 40 files in the baseline (lemmas/, scripts/, PROOF.md, and DAG.md)
matched their turn-start hashes. `git diff --check -- .`
passed. These checks establish documentation consistency and file
preservation, not the existence or correctness of an invariant.
