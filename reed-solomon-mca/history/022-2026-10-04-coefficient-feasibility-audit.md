# 022 — 2026-10-04 — Coefficient feasibility formulation and audit

Completed exactly one mathematical step on the saved coefficient-system
COVERED_TARGET, using the existing SPECIALIZE assessment without browsing.
Shared and local instructions, the whole overview, DAG, prior assessment
and unfinished changes were read and preserved.

[L014](../lemmas/L014-exact-coefficient-feasibility-and-affine-compatibility.md)
records the exact direct system, triangular fourth-root recursion with
48 residual checks, and an inverse 24-by-16 recurrence compatibility
matrix. The latter needs a kernel moment vector with a nonzero actual
Hankel determinant; the other algebraic gates force constant rather than
rational proportionality to the actual minors. Cleared residuals can
reach degree 4096, so a compact encoding is not a feasibility decision.

The [audit](../drafts/2026-10-04-coefficient-feasibility-audit.md) and
[exact controls](../scripts/coefficient-feasibility/result.json) preserve
the degree, simplicity, scalar, determinant and F_(97^20) splitting gates.
Three primitive actual locators have rank-fifteen compatibility matrices
and their kernels recover the minors. A persistent-support control is
excluded by the other conditions. A manufactured balanced bivariate
locator passes the scalar power, splitting, simplicity and distinct-support
tests but has rank sixteen and no compatible affine moments. Its direct
rank proof is an audit of the already excluded full-orbit mechanism,
not a new restriction on general pencils or a reopening of that branch.

Outcome: EXPLORATION; STEP_KIND: RESEARCH;
STEP_CLASSIFICATION: REPRODUCTION. The formulation reproduces L010's
equality with imported standard ingredients and adds no witness, general
obstruction or improved bound. The main pinned-model gap remains
10/q–16/q versus an allowable fifteen, with July correspondence independent
and unresolved. No complete resolution candidate appeared.

The next direction reuses the existing preapproved actual-pencil target.
The inverse compatibility and residual checks permit a constrained
candidate test rather than another unstructured sample. The two-block,
orbit and July/four-block stops are preserved. Consecutive uninformative
mathematical attempts used: one; resultant mathematical attempts: two.

Validation: `python3 scripts/coefficient-feasibility/check.py` passes the
coefficient recursions, cleared equations, affine recurrence/minor recovery,
balanced incompatible locator, non-fourth-power scalar and exact-field
splitting controls. Direct dependencies were checked mathematically:
L010 supplies the syndrome surjectivity, recurrence and full original-event
equality criterion; L009 is used only as a contrast. No scheduler,
launcher, retry state, shared infrastructure or other notebook was edited.

The documentation checker with `--problem reed-solomon-mca` passes with
fifteen nodes and nine edges. The completed and saved next actions match
preexisting COVERED_TARGET lines in the unchanged ready assessment.
