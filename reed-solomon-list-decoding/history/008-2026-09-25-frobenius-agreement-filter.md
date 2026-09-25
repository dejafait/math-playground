# 2026-09-25 — Frobenius agreement filtering

Read the shared and local instructions, current checkpoint, full overview,
DAG, relevant proofs, and existing changes. Preserved prior work and
rechecked the [prize statement](https://proximityprize.org/). The
[focused draft](../drafts/2026-09-25-frobenius-agreement-filter.md) saved
the proposed count before its full proof and rate analysis.

[L007](../lemmas/L007-frobenius-fiber-agreement-bound.md) proves that a
fixed derivative fiber reduces to a lower-degree RS list and gives an
explicit second-moment bound for simultaneous interleaving. It determines
the four pinned rate regimes, retains the useful floor correction at
the limiting slack equality, and excludes characteristic two from the
pinned smooth-domain specialization. The result is ADVANCE; exploration
turns are 0/3 and STATUS remains IN_PROGRESS.

The result shows that the previously identified geometric dimension
obstruction need not force a large agreement-filtered list. It controls
one affine family only. The comparison with epsilon* q still needs the
explicit sufficient field inequality, and neither the number of fibers
for a general interpolant nor the original sharp boundary is determined.
Below the stated slack cutoff, failure of the second-moment denominator
is not a large-list witness. No complete target candidate appeared.

The reason for the subsequent direction is that a variable-coefficient
linear differential equation is the simplest extension beyond a fixed
derivative fiber. Its common polynomial factor, if a representation
exists, may have evaluation zeros that consume agreement and remove the
advantage. Further improvement of the already constant bounds for the
single fiber would not address the missing family description.

`python3 scripts/frobenius-filter/verify.py` passed 252 exact cutoff,
171 strict-bound, and 81 equality-slack checks; the output is retained
under `scripts/frobenius-filter/`. These are arithmetic checks, not an
enumeration of lists or a substitute for the proof. The new lemma has
no earlier lemma inputs: the derivative-kernel, root, and counting
arguments are proved within it. The prior cover obstruction motivates
the test but is not a mathematical input to its bound.

The required
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with eight nodes and five edges, with bytecode writes disabled to
keep shared infrastructure read-only. `git diff --check -- .` also passed.
The proof overview and compact checkpoint include the scope limitation;
structural validation does not certify mathematical correctness.
