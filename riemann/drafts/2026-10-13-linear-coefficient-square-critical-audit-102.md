# Full-square critical audit — step 102 working checkpoint

RESEARCH / REPRODUCTION / proof_audit under the prior SPECIALIZE assessment
`drafts/literature/2026-10-13-linear-coefficient-square-critical-audit.md`.
The sole target is the complete L405 benchmark; no clipping calculation
or new source theorem is being attempted.

Main gap: global actual-theta mixed positivity. Intermediate target:
validate L405's physical replacement, scalar coefficient and complete
sharp limit. A reliable unclipped benchmark could support a later joint-sign
test; it does not decide that test. Accept only with error o(H log^4 H),
all scalar signs and normalizations checked, and fixed-head/fixed-width
limits justified for all real H. Otherwise correct or suspend the claim.

Read L405 completely, the exact L369 polarization, L370's curvature
identity, L390's full ordinary response triple and audited quartic bound,
and L401's statement, physical algebra, complete moment table, endpoints,
full tails and separate audit. The supplied assessment is reused;
L394/L399/L400 stops and the step-99 clipping coverage gap remain intact.

Checks so far: the exact polarization gives Bcal=-c(ab+hy)+O(sqrt(U)/L),
b=z-x/4. Its square replacement is O(U/L), and multiplication by the
complete bound |Delta|<=CU costs O(H log^3 H). Both c^2 factors are
required. All six matrix and nine moment contributions have been read
in full and compared with L401's printed table. The original failed
negative-sign assertion is preserved and is not a negative coefficient.

Still to complete: rerun finite verification, inspect its load-bearing
residual and exact coefficient, finish the independent carrier-polynomial
and sequential-limit check, and record the verdict canonically in L405.
Independent unresolved matters remain clipping sign imbalance, regulator
scale, the total L367 margin/remainder and actual common-zero upper counts.

## Completed audit

The canonical separate audit in L405 validates the complete benchmark
without changing its hypotheses or coefficient. Outcome ADVANCE records
local verification of the known-tool specialization, not progress beyond
the inspected source theorems. The independent carrier-polynomial check,
absolute physical error and explicit sequential-limit argument are in
that canonical proof; no new lemma or DAG edge is needed.

The verifier passed with both exact totals 233/4989600 and zero polynomial
residual. All six matrix and nine moment rows were inspected in full.
The preserved initial diagnostic has those same positive totals and fails
only its imposed negative-sign assertion. Its evidence remains intact.

The continuation is a separately gated source comparison for the signed
cubic mean, recorded in PROGRESS.md and its REVIEW_REQUIRED assessment.
It changes the statistic and does not reopen clipping without coverage.
