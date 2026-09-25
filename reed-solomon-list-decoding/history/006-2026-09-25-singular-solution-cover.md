# 2026-09-25 — Singular solutions in the scalar cover

Read the required instructions, whole proof overview, DAG, existing
changes, and the relevant local proofs and failure record. Unfinished
work was preserved. The prize statement and September 5 TR26-169 source
passage were rechecked; the ABF comparison remains qualified.

The [focused audit](../drafts/2026-09-25-singular-solution-cover.md) passes
its test. [L005](../lemmas/L005-singular-solutions-in-a-finite-chart-cover.md)
covers every solution of a fixed scalar differential equation, including
singular solutions, by polynomially many charts of polynomial summed
degree in large characteristic. A single highest-variable-partial chain
terminates in a nonzero polynomial in X; the first nonzero evaluation
along it and a bounded anchor set place each solution in a chart.

The exact examples in L005 check deepest singular descent, a drop in
differential order, extra points in the cover, anchors outside the base
field, and both characteristic restrictions. No computational sampling
was needed. The sole new direct lemma input is L004's fixed-parameter
chart bound; the DAG records that mathematical use.

This is ADVANCE, with exploration turns 0/3. The scalar cover gap is
removed, but a suitable interpolant has not yet been supplied for every
fixed-slack list. That is the reason for the interpolation direction in
the checkpoint. The achieved conditional polynomial field requirement
is still stronger than the target's existence proviso. Full field scope,
the exact boundary, and ABF comparison remain unresolved. STATUS stays
IN_PROGRESS, with no complete challenge candidate.

The proof overview and source qualification were updated to distinguish
the established scalar cover from the unreviewed parametric theorem and
interpolation input. The required
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with five nodes and two edges. `git diff --check -- .` passed.
The proof was reviewed against L004's hypotheses, derivative termination,
uniform anchor choice, and the exact examples above; structural validation
does not verify mathematical correctness.
