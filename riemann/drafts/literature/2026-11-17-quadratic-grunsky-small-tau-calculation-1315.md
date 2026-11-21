# Small-tau quadratic Grunsky first-order test1315

TARGET: Calculate the base-point residual, exact Jacobian and finite-positive-weight first-order compatibility for C031a's six equations at b=(1,0,0,0,0), tau=0, using the fixed1307 actual-Xi boxes, and decide whether a tau-parametrized C1 branch with positive finite limiting weights passes this necessary test; retain singular, fractional-power and unbounded-weight branches as unresolved.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed review1315 in nomination1314 compared the exact fixed family with C030y/C030z and1253/1307/1311 stops, searched local Grunsky assessments and external implicit-function/inverse-defect/Joukowski terminology, and found no theorem deciding this actual first-order compatibility. Reuse1312 for full-column identities; no novelty claim.
SOURCE_EVIDENCE: de Oliveira arXiv1212.2066v1 Section3 Theorem2 and complete proof, https://arxiv.org/html/1212.2066v1 ; Beckermann-Stylianopoulos1606.00553v2 Section2.1(2.21)-(2.23), https://arxiv.org/html/1606.00553v2 ; Ponnusamy-Wirths1704.08184v1 Theorem1/proof/Remark1, https://arxiv.org/html/1704.08184v1 . Exact hypotheses and comparisons are recorded in completed review1315.
COMPARISON: Known finite Grunsky formulas and the implicit-function derivative identity cover the method. The actual residual/rank/positive-weight compatibility are uncomputed. The classical theorem requires an invertible dependent-variable derivative; it cannot supply rank or global univalence by citation alone. This test imports standard tools and derives only the finite specialization.
GAP: Decide a necessary first-order condition for a tau-parametrized C1 branch with finite positive limiting weights. Passing is not existence; failure or rank deficiency must not be enlarged to exclude singular, non-C1, vanishing/diverging-weight branches or the whole family.
REASON: One exact first-order test can distinguish this proposed regular mechanism from a feasible direction or a scoped obstruction. No rank or branch derivation was performed in source review1315. Newly ready assessment requires separate next-turn approval before research.
SCOPE: C031a's five real coefficients, six full equations, b=(1,0,0,0,0), tau=0 and the unchanged fixed1307 actual constants. Only residual/Jacobian and first-order finite-positive-weight compatibility. No higher order, coordinate blow-up, parameter sweep, degree increase, new quadrature, singular-branch theorem or univalence construction.

## Bounded mathematical continuation after separate approval

Import C031a's complete finite columns and all six residuals. Retain
tau explicitly, d1=1 and both unknown strictly positive weights; do
not start from the divided reconstruction formulas at tau=0. Verify
the base residual. Use exact polynomial differentiation to determine
the Jacobian, with a stated ordering of equations and variables. Show
which dependent-variable minor the implicit-function theorem would
need when tau is a free parameter; do not infer invertibility from a
dimension count or invert a singular matrix.

For a C1 branch parametrized by tau, with b approaching the nominated
base and d2,d3 approaching finite strictly positive limits, use the
cited chain rule/derivative identity to derive and test the complete
necessary first-order equations. Give exact compatibility guards and
check actual constants using only fixed1307 outer boxes, uniformly
where bounds suffice. A solution for some tuple in outer boxes does
not establish a solution for actual constants. Preserve zero or
undecided minors and all strict-sign conditions. Do not divide by an
unproved nonzero expression or use C031a's singular reconstruction at
the base as an exclusion of limiting branches.

Continue only with a decided necessary test or a precisely saved
undecided condition. An incompatible tangent stops this regular branch
class; a compatible tangent leaves nonlinear existence unresolved.
Rank failure alone stops a direct theorem invocation, not all branches.
No follow-on higher-order calculation, Puiseux substitution, diverging
weight search or analytic realization is preapproved by this assessment.
Such changed targets require distinct evidence and source coverage.
No repetition of the completed Cauchy relaxation is authorized.

Main gap/use: an eventual actual formal solution could make a later
analytic realization test concrete and possibly yield one finite L030
mixed-form input. The present test supplies no Xi sign. All larger
blocks, initialization, singular cases and holomorphic univalence on
the entire unit disk remain open. The inspected ellipse and sufficient
meromorphic-univalence sources do not supply those hypotheses.

Essential inputs: C031a,L025,L027,C030z's fixed1307 actual boxes with
L019,L021,L036,L037,L917 contracts; L030-L032/C032a give context.
No new arithmetic-library verification, RH premise or cross-notebook
input. Reuse review1315's Mathlib supporting-tool notes; full matching
Grunsky/actual-Xi branch coverage and Lean verification remain unchecked.

If a script is necessary, save the complete residual/Jacobian, rank
evidence, tangent system, exceptional guards and actual/required bounds
under scripts/grunsky/. Print only conclusions, bounds, failures and
artifact paths, then inspect all load-bearing evidence. The script is
not a numerical branch witness. This source turn creates no script.
Recommend calculation, standard/high; ordinary finite differentiation
and compatibility specialization is not creative work. Classification
may be REPRODUCTION, or POTENTIALLY_NEW for a decided scoped result
not covered by the checked sources, without an originality claim.
