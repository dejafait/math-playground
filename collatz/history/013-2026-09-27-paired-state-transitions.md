# 2026-09-27 — Paired backward rules leave compensation unresolved

Step `collatz-2026-09-27-013-paired-state-transitions` completed one
RESEARCH step with outcome EXPLORATION and classification REPRODUCTION.
The saved SPECIALIZE assessment was ready before this invocation and
was reused. Its existing changes and the unfinished literature history
were preserved; only the Collatz notebook was edited.

[L012](../lemmas/L012-paired-backward-transitions.md) adds the forced
(1,1) companion block, a five-row inverse table, and an exact affine
test retaining the one-block offset and both original starting values.
This specializes the known inverse-word machinery. The checked
literature does not supply the desired all-depth descent implication,
and no novelty claim is made for the arithmetic specialization.

The [test record](../drafts/2026-09-27-paired-state-transitions.md)
explains the target, stopping threshold, and auxiliary diagnostics.
The [paired output](../scripts/paired-state/result.json) reports no
admissible counterexample through depth 11: 196,468 equal-depth classes
were tested at that last depth. Direct shortcut iteration checked
17,688 class realizations and 154 transition-table realizations.

The decisive gap remains compensation by earlier growth. No invariant
valid at every depth, reduction preserving the two starts, or
counterexample was obtained. The finite bound does not meet the required
all-depth threshold, and even rigidity would leave the fixed-start depth
estimate and other block types open. STATUS remains IN_PROGRESS; no
complete candidate appeared.

Two consecutive exploration turns are now used. Increasing enumeration
depth is stopped because it leaves the same gap and rapidly increases
the class count. A linear invariant using the paired states and their
suffix minima is the different mechanism to assess. Its
[new review](../drafts/literature/2026-09-27-paired-minimum-invariant.md)
is REVIEW_REQUIRED; no calculation on it was performed. The third turn
must finish that assessment and a continuation/stop decision.

PROOF.md records the changed tail restriction and its limits. The sole
new DAG row uses L010 and L011, the actual mathematical inputs; the
standard parity-word source is a supporting citation. Mathlib coverage
is not checked.

Validation: `python3 scripts/paired-state/check_pairs.py` completed the
bounded test. `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with 12 nodes and 12 unique edges. The completed-step fields,
prior SPECIALIZE assessment, and exact next-target/review match passed
a separate read-only check. `git diff --check -- .` passed. These checks
validate the recorded finite arithmetic and documentation; they do not
verify an all-depth descent argument.
