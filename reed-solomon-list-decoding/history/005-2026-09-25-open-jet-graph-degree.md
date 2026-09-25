# 2026-09-25 — Degree of open jet graph closures

Read the shared rules, local goal/checkpoint, whole overview, DAG, existing
changes, and relevant proofs and failed approaches. Unfinished work was
preserved. The prize page and September 5 TR26-169 source passage were
rechecked; the frozen target and ABF qualification remain unchanged.

The [focused review](../drafts/2026-09-25-open-jet-graph-degree.md) passes its
test. [L004](../lemmas/L004-degree-of-open-jet-graphs.md) supplies explicit
polynomial cumulative-degree bounds for a nonsingular chart closure and a
separately closed fixed-parameter chart. The proof controls proper
intersections by remaining dimension and pulls a general graph section
back to bounded-degree equations on the base. Its exponent is independent
of the growing number of lifted coefficients.

Exact examples check that naive denominator clearing can add an entire
spurious component and that closure need not commute with specialization,
even for a primitive Q. The second example attains the fixed-chart bound
when s=0. Empty charts, mixed dimensions, d=s, and constant nonzero H were
reviewed symbolically; no new numerical experiment was needed.

This is ADVANCE, with exploration turns 0/3, as a relevant local input to
the geometric cover. It gives no unconditional list bound or sharp safe
radius. The reason to address singular coverage is that graph degree for
each nonsingular chart is now controlled, while covering all solutions
and bounding the number of charts remain essential. Full field scope,
interpolation, the finite-code threshold, and the ABF comparison stay open.
STATUS remains IN_PROGRESS; no complete challenge candidate appeared.

L004 uses L003's rational coordinates and residual bounds as its sole
earlier local mathematical input; the new DAG row records exactly that
edge. Standard geometric inputs are stated in the existing foundation.
The required
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with four nodes and one edge; `git diff --check -- .` also passed.
These checks concern documentation, not mathematical correctness.
