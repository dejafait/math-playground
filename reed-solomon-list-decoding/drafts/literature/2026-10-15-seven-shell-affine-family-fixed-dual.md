# Seven-shell affine-family fixed-dual test — source scope approved

TARGET: Test whether L067's 24-weight dual remains strictly obstructing over every nonnegative column in L065's three-parameter affine family, retaining L061/L062 and the original pairs.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 231 compared L065's complete affine parametrization, L067's joint inequalities/dual, ready kernel/energy/simultaneous assessments and ATTEMPTS/043,048,049; searched prescribed-column constant-weight SDP, affine constrained completion and convex quadratic dual certificates. Exact queries and comparison are below; no inspected result evaluates this family.
SOURCE_EVIDENCE: Reuse Schrijver DOI 10.1109/TIT.2005.851748 Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64); Sano DOI 10.1007/s44146-026-00231-y Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7/proofs; Polak arXiv:1703.05171v1 Sections 1.1–1.2. Freshly inspected Boyd–Vandenberghe author slides PDF pp. 53–54,97–98,105,174–175, including the KKT sufficiency proof; canonical records foundations/04,09,10,12.
COMPARISON: Known mixed-layer and singular-Schur tools allow varying cross blocks with an unchanged singular base. General convex-QP and sufficient KKT certificates cover multiple real parameters and affine equality/inequality constraints, including singular Hessians. They give no family-specific coefficients, curvature, consistency or optimum. L067 settles only its immutable point; earlier gates explicitly excluded family optimization.
GAP: Reconstruct the full nonnegative and unordered-consistent parameter domain, the unchanged dual's exact weighted right side and all singular ranges; certify strict negativity throughout that domain or an exact admissible nonnegative value. Neither alternative is evaluated in this review.
REASON: Essential coverage is adequate for one bounded exact specialization; no source blocker or known verdict requires another literature turn. Import the standard tools without reproof and verify their application to this family.
LITERATURE_REASON: Replacing L067's fixed columns by L065's family changes the approved scope; this separate turn checks multivariable optimization and simultaneous moment consistency while reusing the ready mixed-layer and singular-Schur assessments.
SCOPE: Exactly TARGET with one common real (u,v,w), positive original rho and p7, unchanged L061/L062 and original pairs; nonnegative columns, original Boolean/forbidden rules and every unordered identification. Only L067's unchanged 24 weights are tested; no new scalar upper rows, pair/base retuning, new dual or global feasibility claim.

Main gap: arbitrary-center safety at 67/68 agreements, bracket 955–957.
The proposed intermediate target tests the scope of one already verified
dual while allowing the exact compatible columns to vary. Essential
inputs are L061,L062,L065,L066,L067, with their transitive inputs and
foundations/04,09,10,12. Preserve the original positive rho and p7 and all
old moments. Use one common parameter triple (u,v,w) for every new column,
with f=c+u*a^27+v*a^33+w*a^42 and every column entry nonnegative. Keep
the original Boolean and forbidden-distance rules and all unordered
moment equalities. No extra scalar upper constraints, pair retuning or
label averaging are proposed.

The desired test is whether the same 24-weight dual has strictly negative
weighted right side throughout that admissible parameter family. A
rigorous uniform negative bound would eliminate this wider family and
motivate a change of base/pairs or mechanism. An exact admissible
parameter choice with nonnegative weighted right side would stop this
fixed dual as a uniform-family obstruction; it would not establish a
simultaneous PSD extension. Failure to certify either should be recorded
without treating numerical optimization as proof. This is a proposed
test and threshold, not a derived family formula or a known result.

The pointwise stop in ATTEMPTS/049 remains final for its immutable
parameters. Other duals, global moments, measures, actual labels, packings
and RS realization remain independent gaps. No main-target candidate is
claimed. The initial proposal required source comparison only. Step 231
completes that comparison and approves one later mathematical attempt;
no family calculation, lemma or mathematical-script change occurred here.

## Reused primary coverage and duplicate comparison

Reuse the ready assessments
`2026-10-14-seven-distance-full-base-kernel-column.md`,
`2026-10-14-seven-distance-fixed-column-energy.md`,
`2026-10-14-simultaneous-five-six-seven-shell-extension.md` and
`2026-10-13-full-shell-column-energy.md` in this directory. Their inspected
theorem statements and relevant proof cases are adequate for the unchanged
matrix algebra, hierarchy and inverse action; they were compared locally,
not presented as fresh external reading.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[eight-page author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp. 5–7, supplies the unequal-layer algebra. Its orthogonal
extension/reset proof and tensor reduction were inspected in the reused
assessment. Ground-set sizes 68 and 956 and layers 0,5,6,7 remain within
the same ranges; changing entries does not change that source scope.
The actual normalization and invariant slice still require verification.
No suspect complement prefactor or label symmetry is used.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7, has the full
range/Schur criterion and inverse-on-range input recorded in foundations/10.
Theorem 2.6 covers a finite Hermitian old block C and an entire cross
block B, requiring C PSD, ker(C) contained in ker(B), and a PSD
generalized Schur remainder. It assumes neither invertibility nor maximal
rank. Its square-root necessity and triangular-congruence sufficiency
proofs remain reusable for varying B. The family must satisfy the range
condition at every admissible parameter, rather than inherit a fixed
point's computed inverse action.

Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE TIT 65 (2019), 28–38,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1/proof, p. 2, and Section 1.2,
p. 3, supplies equal-union moments and constraint-preserving averaging.
Retain the source-display A(n,d) qualification: its indicator proof gives
A(n,d,w). The present n=1024,d=10,w=68 meets its hypotheses. Common
parameters do not by themselves prove every presentation consistent.
No averaging of actual-label restrictions or representing measure follows.
Stronger A4/B4 programs add constraints and do not complete these
prescribed columns automatically.

The foundations/10 comparisons of Dreyer v1 Theorem 5.2 and
Grone–Johnson–Sá–Wolkowicz Theorem 7/Proposition 2 remain sufficient:
their free-entry completion statements do not impose these unordered
identifications or entrywise nonnegativity. They are reused comparisons,
not freshly inspected passages. Albert's original proof and the formerly
inaccessible Boyd book PDF remain unread leads; the independently read
sources suffice, so neither is an essential blocker.

L065's canonical parametrization already exhausts the single-column
kernel solutions. L066 computes only its selected point's scalar energy.
L067's displayed necessary inequalities and fixed dual are the exact
inputs for this changed test; its audit proves no uniform-family verdict.
ATTEMPTS/043 and /048 preserve smaller-slice passes; ATTEMPTS/049
preserves the immutable simultaneous obstruction. None duplicates the
proposed domain-wide fixed-dual test. No historical stop is reopened at
its original parameters.

## Optimization source and precise remaining specialization

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, revised
402-page author slides (with Parth Nobel),
[author-hosted PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
retrieved 15 October 2026, publication date of this revision unasserted:
freshly read PDF pp. 53–54 (first/second-order convexity), 97–98
(complete local/global argument and differentiable optimality), 105
(slide 4.18, polyhedral QP with PSD Hessian), 174–175 (slides 5.19–5.20,
KKT and complete sufficiency proof). Canonical coverage is in
[foundations/10](../../foundations/10-psd-completion-source.md).
These are multivariable statements, permitting affine equalities,
boundary optima and singular Hessians. Feasibility, multiplier signs,
complementary slackness and stationarity suffice for a convex problem;
Slater is needed for the stated converse, not this certificate direction.
The source does not guarantee attainment or strict curvature here.
No general optimization theorem needs a local reproof.

Research must recover the common affine column from L065 and check every
eligible full-region presentation as an affine expression, retaining all
L062 lookups and original pairs. Impose any additional equality forced
by shared unordered keys; do not assume the whole single-column family
is automatically simultaneous. Every column entry must be nonnegative,
including fixed coordinates. An upper bound over a demonstrably larger
domain may certify negativity, but a nonnegative counterexample must
belong to the actual domain, not merely that relaxation.

Use exactly the weighted right side of L067's displayed inequalities (1)
with its unchanged 24 weights. Recheck all free-coefficient cancellations
and every singular range condition after substitution. Keep the anchor
correction, coherent mixed-layer normalization and actual inverse action;
do not replace them by a Euclidean inverse of an unweighted quotient.
Derivation of the family objective and verification of its curvature are
future research obligations, not mathematical conclusions of this review.
The convex-QP import applies only after its objective sign and Hessian
have been checked. A rational global bound or exact feasible witness
must be independently substituted in the original data. A numerical
optimizer, sampled parameters or only a stationary point is insufficient.

A strict uniform negative bound suffices for the desired exclusion.
Do not assume the admissible domain is bounded or the optimum attained.
A zero supremum without an admissible nonnegative point does not by
itself stop pointwise strict negativity. If the exact test cannot decide
the requested strict sign, save the complete relevant equations and
certification obstruction and report the limitation. Do not silently
change duals, base moments or the target.

The downstream use and stopping test remain those stated above: either
exclude this wider prescription by the fixed dual, or park this dual as
a uniform-family diagnostic. Other duals, full SDP feasibility, measures,
packings, labels, common-center RS realization and the 955–957 bracket
remain independent gaps. Full matching Mathlib coverage for this family
and supporting convex-QP/KKT coverage are not checked; unknown is not absent.

## Search record

Queries on 15 October 2026:

- `"constant weight" "semidefinite" "Schur complement" column completion`
- `Boyd Vandenberghe convex optimization quadratic programming optimality polyhedron concave maximization`
- `"constant-weight" "semidefinite" "prescribed" "columns"`
- `"constant-weight" "Schur complement" quadratic`
- `"constant-weight codes" "quadratic programming" "semidefinite"`
- `"constant weight" "semidefinite" "affine" "completion"`
- `"Schur complement" "dual certificate" "convex quadratic"`

Discovery returned the already assessed constant-weight SDP literature,
general optimization material and unrelated completion applications.
Secondary snippets were not imported as theorem evidence. The primary
author slides above were actually read; no inspected theorem supplies
the prescribed numerical verdict. The bounded search does not establish
novelty. No larger new source extract was needed once these hypotheses
and the relevant proof cases were covered.
