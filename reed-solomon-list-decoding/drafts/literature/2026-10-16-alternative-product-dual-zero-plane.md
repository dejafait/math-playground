# Alternative product weights on the zero plane — source scope approved

TARGET: Test whether L071's unchanged product weights give a strictly negative fixed term throughout L068's w=w_star plane satisfying L065 nonnegativity and L069's column scalar rows.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 247 compared the ready affine-family, zero-plane scalar and fixed-point remaining-mode assessments, targeted canonical proof passages and ATTEMPTS/049–053; bounded fresh searches for constrained quadratic certificates and prescribed constant-weight columns are recorded below. No inspected source evaluates this exact objective/domain.
SOURCE_EVIDENCE: Reuse foundations/04,09,10,12: Schrijver Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64)–(65); Sano Corollary 2.2, Theorem 2.6, Lemma 2.7; Polak v1 Sections 1.1–1.2; Boyd–Vandenberghe slides 4.18 and 5.19–5.20. Freshly reopened the 402-page author slides, PDF pp.174–175, and read the complete KKT sufficiency argument; precise citations and qualifications below.
COMPARISON: Known polyhedral convex-QP certificate scope already permits multiple affine scalar rows, boundary points and singular Hessians; changing the prescribed weights requires fresh coefficient and curvature verification, not a new general theorem. L068 uses different weights, L069 proves domain nonemptiness only, and L071 rejects only u=v=0. None settles the requested plane-wide sign.
GAP: Reevaluate L071's unchanged product pairing on the complete scalar-admissible two-parameter plane, verify curvature and all original cancellations/ranges, and obtain a strict exact bound or an exact admissible nonnegative-pairing point. No new objective, optimum or sign is calculated in this review.
REASON: The enlarged parameter domain and scalar hypotheses fit the reused general coverage; one bounded later REPRODUCTION calculation is approved without reproof of standard tools. No essential source blocker remains.
LITERATURE_REASON: The fixed-point approval omitted varying u,v under every column scalar row; this required a separate comparison with the ready multivariable affine-family and scalar assessments. This turn closes that scope gap without evaluating the new objective.
SCOPE: Exactly TARGET, unchanged L071 product weights and L061/L062 base/pairs, one common real (u,v,w_star), original positive rho,p7 and original RREF/scaling; every column scalar row through p13, all unordered identifications, 28 forced entries, 36 free seven/seven entries, 64 singular ranges and full anchor correction. No new/new scalar upper rows, alternate weights, bases/pairs or global feasibility claim.

## Relevance and bounded proposed test

The main gap remains arbitrary-center safety at 67/68 agreements. A
strict uniform negative bound for these different weights would exclude
the remaining compatible family at the fixed base/pairs, since L068's
old weights already require w=w_star. A surviving admissible point with
nonnegative pairing would instead stop strict exclusion by this particular
dual. Neither outcome would settle other bases, pairs, global moments,
actual labels, measures or the RS target.

Essential inputs: L061,L062,L065,L067,L068,L069,L071 and foundations/04,09,10,12.
Retain positive original rho,p7, all original RREF coordinates, the exact
w_star, 36 original v-scaled seven/seven variables, 28 forced entries,
all unordered presentations, all 64 singular ranges and full anchor
transport. The column domain must include every one of L069's ordinary
rows through original p13; do not silently replace it with a bounded
rectangle or only sampled points. No new/new scalar upper row is included.

Continue the proposed mechanism only with an exact strict uniform
certificate, or an exact discriminating intermediate computation leading
to such a certificate. Abandon these weights as a strict-exclusion test
if an admissible point has nonnegative pairing; a zero supremum without
attainment must be qualified. Failure here does not establish simultaneous
PSD feasibility. No calculation of this new objective was performed in
step 246. Step 247 completes the separate source-scope review below;
the original proposed calculation remains for a later research turn.
No novelty claim is made.

## Inspected sources and scope comparison — step 247

Reuse the ready assessments in this directory:
`2026-10-15-seven-shell-affine-family-fixed-dual.md`,
`2026-10-15-zero-dual-plane-ordinary-scalar-feasibility.md`,
`2026-10-15-zero-point-remaining-mode-feasibility.md` and
`2026-10-16-zero-point-remaining-mode-critical-audit.md`.
Their inspected primary results, including relevant singular proof cases,
remain adequate for the unchanged matrix algebra and column rows.
This review compares their scope; it does not claim to re-audit the
ancestral finite certificates.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B
(64)–(65), printed pp.5–7: the unequal-layer reduction permits the
same factors 68,956 and layers 0,5,6,7. Scalar conditions apply to
nonzero actual triple orbits, retaining repeated words, forbidden
distances and permutations preserving t-s. The ready scalar assessment
also cross-checks Kim–Toan arXiv:1212.3467v1, III.A Remark 11 and
III.B (31)–(35), pp.8–9; its even d>=4, d<2w<=n hypotheses hold
at d=10,w=68,n=1024. No suspect complement prefactor is used.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7: for finite Hermitian
[A,B;B*,C], PSD is equivalent to C PSD, ker(C) contained in ker(B),
and A-B C^dagger B* PSD. Singular C is allowed. The inspected square-root
necessity and triangular-congruence sufficiency proofs in the ready
coverage allow a varying cross block; the range condition must hold
at every parameter used. Real symmetric mode blocks are covered.
Inverse action on the range retains the actual weighted normalization.

Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and its indicator
proof, p.2, and Section 1.2, p.3: reuse the constant-weight qualification
in foundations/12. Only constraint-preserving averaging of this ordinary
unlabeled slice is available. Parameter variation licenses no averaging
of actual subgroup labels, representing measure or RS realization.
The completion comparisons in foundations/10 remain adequate: free-entry
PSD completion does not enforce these prescribed columns or scalar rows.

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, revised
402-page author slides with Parth Nobel,
[author PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf):
reuse slide 4.18 (PDF p.105), which allows a PSD quadratic Hessian and
affine inequalities/equalities. Freshly reopened slides 5.19–5.20
(PDF pp.174–175), reading all KKT conditions and the complete sufficiency
proof. For a differentiable convex problem, feasible primal variables,
nonnegative inequality multipliers, complementary slackness and
stationarity certify global primal/dual optimality. This direction needs
no Slater condition; the stated converse uses Slater. Singular Hessians
and boundary points are allowed. Reuse the ready first/second-order
convexity coverage at PDF pp.53–54 and 97–98. No attainment, boundedness
or instance-specific curvature is asserted. PDF text was readable;
screenshot requests returned references without image data.

These optimization hypotheses are sufficient coverage for the proposed
certificate method, conditional on the later exact curvature check.
They do not evaluate L071's weights on the new domain. No general theorem
needs reproof; the only proposed reproduction is the finite specialization.
If curvature is not verified, do not invoke convex KKT sufficiency as a
global certificate. An independently checked global polynomial bound
or a feasible nonnegative-pairing point can instead decide this same
target without claiming a general optimization theorem.

## Duplicates, failures and application obligations

Targeted proof reading compared L065's original RREF definition,
L068's affine costs/range identities and exact square, L069's exhaustive
column rows, and L071's original/raw system and explicit product weights.
ATTEMPTS/049–053 preserve, respectively, the old-column obstruction,
old-weight attained zero, scalar-plane nonemptiness, tight-equality pass
and alternative-weight fixed-point obstruction. Those conclusions are
distinct from the requested uniform sign. In particular, L068's
negative-square coefficients and zero null directions cannot be copied
to the changed weights. L071's negative value at the origin cannot be
extrapolated to the plane. No stopped target is simply repeated.

The later calculation must keep the exact original c,a^27,a^33,a^42
and w_star from L065/L068. Every column has actual moment y=p7*f;
all 85 types and six presentations require the original three scalar
slacks y, p_a-y, 1+y-p_a-p_b, with original pairs through p13.
Retain all 2178 old rows and all Boolean/forbidden/equal-union lookups.
Do not infer a rectangle, discard boundary zeros or keep only sampled
rows. An outer relaxation may certify negativity, but any surviving
point must satisfy the actual complete domain.

Reevaluate L071's F,A,R and the 28 forced seven/seven entries on that
plane, using its exact unchanged h,k factors. Check every original/raw
free-coefficient cancellation, all 64 singular ranges, coherent
mixed-layer normalization and full transported anchor correction.
The family objective, its curvature, parameter-domain geometry and
sign remain uncomputed. A stationary point or numerical solver status
alone is insufficient. Do not assume an inverse exists for a singular
old block or apply an unweighted quotient inverse.

Continue with an exact uniform strict bound or a discriminating exact
computation toward one; stop these weights as a strict-exclusion test
on an exact admissible nonnegative value. Distinguish pointwise strict
negativity from a uniform margin: a zero unattained supremum alone
does not refute pointwise negativity. Report unboundedness or unresolved
attainment honestly rather than treating a supremum preview as evidence.
Other duals, base/pair choices, global moments, actual-label constraints
and RS safety remain independent gaps. Full matching and supporting
Mathlib QP/KKT, matrix and finite-instance coverage are not checked;
unknown availability is not absence.

## Bounded search record — 16 October 2026

Fresh queries:

- `"concave quadratic" "polyhedron" optimality Boyd Vandenberghe`
- `"constant-weight codes" "quadratic" "Schur complement"`
- `"S-lemma" "multiple" "linear constraints" quadratic optimization survey`
- `site:stanford.edu boyd convex quadratic programming polyhedron KKT sufficient singular`
- `"constant-weight codes" "prescribed" "Schur"`

Discovery located the already assessed author optimization material,
general nonconvex minimization, S-lemma/trust-region leads and unrelated
coding material; no inspected theorem supplies the present numerical
verdict. Only the author slides' actual statement/proof passages were
used as fresh theorem evidence. Search snippets, secondary hosts and
unread S-lemma leads are not imported. No multi-constraint S-lemma or
unconditional exact SDP relaxation is assumed. The ready polyhedral
convex-QP coverage suffices without pursuing those leads. Absence of a
search match is not evidence of novelty. This turn changes only source
assessment and checkpoint/history documentation, with no new lemma,
mathematical script, objective calculation or proof-overview change.
