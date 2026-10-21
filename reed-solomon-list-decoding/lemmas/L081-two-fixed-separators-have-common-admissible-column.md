# L081 — The two fixed separators admit a common nonnegative column

## Hypotheses

Use n=1024,w=68, L021's entire original pair prescription, L053's
positive singleton rho, L073's included-anchor PSD base, and L075's
entire unchanged unordered moment dictionary. Matrices are divided by
rho. Retain the original seven-column RREF at (0,v_dagger,w_star),
all 28 forced and 36 completed seven/seven entries, and

    p8=16792471/1181138102168120460>0.

Use L076's original affine family f=c+A*t, with 85 factors and original
parameters t=(t56,t63,t69,t78). The nonnegative column domain is

    T={t in R^4: c+A*t>=0}.

Every free column moment is p8*f_j; fixed lookups, anchor and diagonal
remain unchanged. Use the same parameters in every transported column.
Preserve all full unordered keys, Boolean repetitions, forbidden
distinct half-distances 1,...,4 and the 36 forced eight/eight moments.
The 45 remaining eight/eight moments are nonnegative, with precisely
L078's original positive scaling z. Retain all 81 included-anchor modes,
the full anchor correction, and singular/empty old blocks.

Evaluate exactly L078's and L080's unchanged canonical 81-weight
separators, denoted y^(1),y^(2). In L079's original mode notation write

    A_mode*z<=b(t), z>=0,
    Phi_h(t)=(y^(h))^T b(t), h=1,2.

This tests only the two aggregate separator inequalities. No scalar
upper row, other-anchor matrix, alternate dual, changed pair/base
moment, actual-label constraint or global extension is imposed.

## Conclusion

There is an explicitly specified rational t_dagger in T with

    351861924105/10^6 <= Phi_1(t_dagger) < 351861924106/10^6,
       401569066/10^6 <= Phi_2(t_dagger) <    401569067/10^6.

Both pairings are strictly positive. Exactly f56=0; the other 84 factors
are positive. Thus these two separator inequalities have a common
admissible column and cannot together exclude the entire L076 family.
Taking all 45 z coordinates zero satisfies these two aggregate
inequalities; individual mode inequalities are not asserted.

This is a local REPRODUCTION of assessed finite methods, without a
source-level originality claim. It preserves L078's immutable-column
rejection, L079's attained positive old-weight maximum and L080's
different fixed-point rejection. It provides no simultaneous PSD
completion, signed-completion verdict, global moments, packing, RS list
or arbitrary-center safety improvement. The 955–957 bracket is unchanged.
The separate critical proof review below retains this result.

## Proof

**Imports and exact scope.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-17-eight-two-separator-family-intersection.md`.
Reuse L079's family-wide full-key/range identities and original mode
formula, and the canonical weight definitions in L078 and L080. Their
general algebra imports are Alexander Schrijver, *New code upper bounds
from the Terwilliger algebra and semidefinite programming*, IEEE TIT 51
(2005), 2859–2866, [author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7; Takashi Sano, *Moore-Penrose inverse, generalized Schur
complement and inertia*, published 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2 and Theorem 2.6; and Sven C. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and indicator proof p.2, Section
1.2 p.3, with foundations/12's constant-weight display qualification.
Factors 68,956 and layers 0,5,6,7,8 stay in their assessed ranges.
Singular bases are permitted; the old PSD base and all affine ranges
are retained. No labeled restriction is averaged.

For the separator implication import Michel X. Goemans, *Advanced
Algorithms*, Lecture 3, 19 September 2001, Theorems 1 and 3, printed
pp.1–2, [MIT notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
The two existing canonical certificates have nonnegative y and
s=(A_mode)^T y, so any feasible completion requires
0<=s^T z<=Phi_h(t). These imported methods do not supply this
coefficient-specific intersection verdict. The only additional work
is finite rational assembly and a witness check, not a reproof of a
general feasibility theorem. No Slater condition, optimizer status,
rational-witness existence theorem or attainment theorem is used.

**Canonical quadratic specification.** For each original mode i=9a+b,
0<=a,b<=8, use exactly L079's affine forced-minus-anchor contribution
F_i(t) and quadratic range cost R_i(t), so b_i(t)=F_i(t)-R_i(t).
Here F_i includes -1_(a=b=0)*p8*C(68,8)*C(956,8). In particular the
full anchor correction is retained. Set zeta=(1,t56,t63,t69,t78).
For h=1,2, define the symmetric rational 5-by-5 matrix M_h by

    zeta^T M_h zeta = sum_i y_i^(h)*(F_i(t)-R_i(t)).

Equivalently add the weighted quadratic cost with negative sign,
add the affine constant at entry (0,0), and split each affine linear
coefficient equally between (0,j) and (j,0). This uniquely specifies
M_h without numerical fitting. Reconstruct y^(1) from L078's canonical
42-by-42 I,J system and y^(2) from L080's 43-by-43 system, rather than
searching for new weights. All original scaled/raw sums agree: each
has 44 zero free coefficients; the sole positive coefficients occur
at (r,q)=(3,6) and (6,3), respectively. Their nonnegative-moment signs
remain essential to their interpretation as necessary inequalities.

The assembly independently rebuilds all 81 original beta rows, constant
old blocks, five affine cross coefficients, inverse actions, range
residuals and forced contributions. Every old nonempty principal minor
is nonnegative (306 checks), and every singular/empty range holds
coefficientwise. All 500 full relation types and 3000 presentations
retain the L079 affine dictionary; no distance-only identification is
used. The original active column gives L078's old pairing, and L079's
interpolated point gives L080's old pairing. Thus these are precisely
the two unchanged separators on one identical domain.

**Exact point.** Indices of M_h run from 0 to 4. L079 gives
M_1[4,4]<0 and dependence only on t78. Define

    s=-M_1[0,4]/M_1[4,4],
    G=(M_2[i,j])_(i,j in (2,3)),
    g=(M_2[i,0]+M_2[i,4]*s)_(i in (2,3)),
    (u,v)^T=-G^(-1)g,
    t_dagger=(0,u,v,s).

Exact elimination verifies det(G) is nonzero. This is an unambiguous
rational specification of the point. It arises from a stationary
two-coordinate solve, but the conclusion uses only its substitutions;
no maximum on that slice or on T is asserted.

Independent substitution into all 85 original rows gives
c+A*t_dagger>=0, exactly factor 56 zero and 84 positive factors.
All 90 original kernel equations hold with these same factors.
The fixed old entries and all 36 forced new/new entries agree at every
presentation. Since s is L079's exact stationary parameter,
Phi_1(t_dagger) equals L079's positive maximum. Direct rational
evaluation gives the two intervals in the conclusion, with strict
upper endpoints certified by integer cross multiplication.

For an independent original-row check, rebuild the point from this
2-by-2 recipe with Gauss–Jordan elimination instead of Cramer's rule.
Construct actual 68-subsets and all six membership-atom presentations
for every relation, using the original L075 dictionary and L076 column.
Reconstruct every original B_ab and cross vector at this point. Solve
using a largest nonsingular principal subsystem and verify every row
of B_ab*x=cross, including zero/singular cases. Compute all 81 bounds
directly from forced values, full anchor and range costs, and compare
with the assembled quadratics. Reconstruct both canonical dual systems
independently and check every scaled and raw free coefficient. The
weighted original bounds equal the claimed positive pairings; weighted
forced, anchor and cost contributions also agree separately. Thus the
signs are original-coordinate rational checks, not numerical proposals.

The known certificate sign implication now gives no contradiction for
either separator at t_dagger. More concretely, z=0 is nonnegative and
has s_h^T z=0<Phi_h(t_dagger) for both h. It satisfies both aggregate
inequalities. Nothing in this argument checks all 81 inequalities
simultaneously, so it supplies no PSD completion.

**Evidence and bounded failure.** Run from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_two_separator_intersection.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_two_separator_slice.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_two_separator_intersection.py

The first program passes 3011 exact checks, rebuilds both full pairings
and verifies concave-curvature ranks 1 and 3 by positive square
decompositions with zero residual. Its 257 dyadic samples on the old
endpoint segment produce no common witness; that bounded failure is
inconclusive for T and is preserved in
`scripts/finite-support/eight-two-separator-intersection-results.json`.
The second program proposes a point in the different slice t56=0,
t78=s, then reconstructs it rationally and passes its two exact domain
and old-weight checks. The complete point, factors and pairings are in
`scripts/finite-support/eight-two-separator-slice-results.json`.
Floating arithmetic only selects the proposal, with no certified
optimization claim.

The independent original-row verifier uses no floating arithmetic or
optimizer and passes 1697 exact checks with no failures. It reconstructs
all 500 types/3000 presentations, all kernel residuals, all 81 bounds
and both raw/scaled certificates, consuming the complete relevant
arrays. Its evidence is
`scripts/finite-support/eight-two-separator-intersection-verification.json`.
Actual minimum factor is 0, meeting the required bound 0; both actual
pairings exceed the required bound 0 by the displayed strict positive
intervals. This is verification within the attempt, not the later
dedicated critical proof review. It parks only exclusion by these two
fixed weights. Other separators, full completion, scalar upper rows,
other anchors, global extension and RS realization remain untested.

**Separate critical proof review — step 286, 2026-10-17.** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-17-two-separator-witness-critical-audit.md`.
This audit retains exactly the common-witness conclusion. No point,
weight, input, or mathematical assertion is changed. It is a local
REPRODUCTION of the assessed finite methods, without a claim of progress
beyond the sources checked.

The cited Schrijver index ranges contain the layers 0,5,6,7,8 on both
68 and 956 points. Sano's singular criterion applies to each real
symmetric old block, including zero blocks; no invertible-base assumption
is made. Polak's equal-union convention and ordinary constraint-preserving
averaging apply to this unlabeled slice. Goemans's sufficient separator
implication uses nonnegative free moments: it does not require all free
coefficients to cancel. No strict feasibility, KKT condition, optimizer
or existence theorem is needed for the explicit rational point. The
source qualifications in foundations/04,09,10,12 remain in force.

A dedicated program, separate from the three construction programs,
reconstructs the original pair equations and factor two, positive rho,
the original seven-column RREF at (0,v_dagger,w_star), and the entire
seven/seven completion from its defining system. All 270 old dictionary
entries agree. It recovers all 85 affine factors from the eight-column
RREF rather than taking the stored affine factors as definitions. All
90 original equations hold coefficientwise and at the final point;
all 90 full orbit-weighted kernel residuals include the anchor. These
checks validate imported recipes, not recursive critical audits of every
ancestral proof. L076's full-kernel exhaustion and the stated base inputs
remain explicit dependencies, with their own review qualifications.

All 500 types are reconstructed from eight disjoint membership regions.
For each, actual 68-subsets give every one of the six ordered atom
vectors, distances and available lookups. Every shared key agrees
coefficientwise. Exactly 36 eight/eight entries are forced; the other
45 full keys are distinct. The final point also agrees with every
complete saved fixed-point presentation, not just with its distances.

For the mode normalization, reuse L078's reviewed, entry-independent
subset actions, and recompute all entries of all 220 factor transitions
from its four-region binomial formula. Check every polynomial action,
positive norm, absent mode and both rectangular directions. With
N8=N_(68,8,a)*N_(956,8,b), the positive scales d_l satisfy

    B_weighted(l,m)=(N8/D8_ab)*d_l*B_source(l,m)*d_m,
    cross_weighted(l)=(N8/D8_ab)*d_l*cross_source(l), d_8=1.

These are simultaneous whole-block identities on all five affine
coefficients, including the constant-mode anchor correction. They are
not unrelated pairwise normalizations. All 306 old principal minors are
nonnegative; both their source and weighted values are checked. Positive
mode multiplicities sum to each entire retained shell dimension.

Before constructing the point, reverse the layer order and eliminate
the weighted old block while keeping its cross vector affine in
zeta=(1,t56,t63,t69,t78). At a positive pivot d with current affine
cross row u, add the matrix u*u^T/d to its quadratic cost. At a zero
pivot, check the remaining matrix row and every affine cross coefficient
are zero. This independently recovers the entire range cost, divided
by p8*N8. Direct substitution of all five saved source inverse columns
into every original source equation gives the same cost after division
by p8*D8_ab. All 81 cases are included: 36 with three old layers, 13
with two, 15 with one, and 17 with none. All anchor terms and forced
contributions agree separately, giving every full quadratic b_i.

Read each canonical I,J list directly from its lemma manuscript and
solve the 42-by-42 and 43-by-43 systems in reverse variable order.
Their nonzero pivots and full substitutions recover the unchanged
weights, with respectively 27 and 38 positive coordinates. Recompute
every scaled and raw free-moment coefficient independently; each system
has exactly 44 zeros and its prescribed sole positive coefficient.
Summing the newly reconstructed 81 quadratic forms produces both M_h.
Only then form s, G and g and solve the manuscript's two-coordinate
system. The nonzero determinant and all original equations are checked.
The resulting point agrees exactly with both prior witness records.

At this same point all 85 factors are nonnegative: exactly f56=0 and
84 are positive. Every original mode inverse residual, forced term,
anchor term, range cost and bound agrees with the complete step-284
verification certificate. Both original weighted bounds equal their
quadratic evaluations, and their forced-minus-anchor-minus-cost sums
agree separately. Exact rational subtraction verifies the two intervals
in the conclusion, with positive strict upper gaps and positive lower
endpoints. Thus z=0 satisfies both aggregate necessary inequalities
strictly. This does not assert that z=0, or any z, satisfies every mode.

Reproduce from this notebook with

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_eight_two_separator_intersection.py

The dedicated audit passes 10318 exact checks, with no failures. Full
rational point, affine and fixed mode matrices, elimination stages,
canonical systems, all coefficients, pairings and interval gaps are in
`scripts/finite-support/eight-two-separator-critical-audit.json`.
Actual minimum factor is 0, meeting the required bound 0. Both actual
pairings lie in the stated strictly positive intervals, against the
required bound 0. Full relevant certificate arrays are consumed and
compared; summaries or hash matches alone are not verification.

The old 257-sample segment failure remains inconclusive and was not
repeated. The off-segment witness retains precisely ATTEMPTS/063's stop
on these two fixed separators. A simultaneous 81-mode completion, scalar
upper rows, other anchors, changed pairs/base, global moments and RS
realization remain independent unresolved tasks. No ancestral audit or
955–957 boundary improvement is inferred from this retained conclusion.

## Mathlib

Full matching prescribed two-separator intersection: not checked.
Supporting rational linear algebra, quadratic forms, PSD/Schur facts
and the full mixed-layer decomposition: not checked here. Unknown
coverage is not absence. The general methods are imported by precise
citations above; no source-level novelty claim is made.
