# Generator insertion coefficient — source-review record

STEP_ID: YM-20261024-436-generator-insertion-coefficient-source-review

This is a LITERATURE-only step on the exact saved V_N-to-K_(i,V)
rate target. No comparison bound is derived. Existing unfinished work
and all lemma/script files are preserved.

The complete supplied overview and DAG locate the main construction
gap and the independent coefficient comparison. L120's full proof was
read: its sections 2--5 first fix spatial/axial/heat cutoffs, replace
the projection on compact adjacent rows, take fixed-offset Riemann
limits, and finally remove tails without a rate. L268 concerns the
different Delta_V-V_N error.

Inspected supporting coverage: L119's exact insertion, tail definition
and finite trace envelope; L267's pointwise matrix decay and its scalar
normalization; full L114; L248 sections 1--2, its raw/probe audit cases
and Mathlib/source paragraph; L222's quantitative mode and rectangle
quadrature ranges. Reused the ready primary assessments rather than
reprove their imported scalar Green or Taylor theorems.

Coverage decision to record in the canonical assessment: SPECIALIZE for
one later RESEARCH / REPRODUCTION attempt, retaining the exact target.
No inspected theorem gives the full pinned coefficient rate. The test
must quantify the joint kernel tails and coefficient differences,
justify growing cutoffs within fixed interior clearance, and match
exactly L120(3), including its a^4 spatial/axial normalization. L248's
compact-row raw matching must not be applied globally to remote inputs.

The main gap, downstream use, source versions, bounded queries,
duplicates/failures and continuation test belong in the canonical
assessment. Mathematical exploration usage is zero; this review neither
proves the rate nor audits upstream inputs.

Completed: the canonical assessment records SPECIALIZE for the unchanged
target, and history/436 records EXPLORATION with no new mathematics.
PROGRESS.md holds the sole current continuation and routing.
