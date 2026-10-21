# L070 — The fixed zero point passes the necessary tight-mode equalities

## Hypotheses

Retain L061's entire anchored five/six-shell PSD base, the complete L062
moment dictionary, original pairs and singleton normalization, and L065's
specified affine family. Thus

    rho=(binomial(1024,64)/binomial(68,64)+1)/(2 binomial(1024,68))>0,
    p7=3539/248922676958508>0.

Use exactly L069's point u=v=0,w=w_star. L065's RREF defines
f=c+u*a^27+v*a^33+w*a^42, and L068's objective matrix M defines
alpha=-M33>0, beta=M03 and w_star=beta/alpha. This is distinct from
L067's older immutable point w=-c4/a^42_4. Keep every old, five/seven
and six/seven entry, anchor, Boolean/forbidden entry and unordered equality.

In L067 (1), use the original 36 variables indexed lexicographically
by (r,q) in {0,...,7}^2 with r+q>=7, scaled as

    Y_(7,7,7-r,7-q)=p7*z_(r,q)/v_(r,q),
    v_(r,q)=binomial(7,r)binomial(61,r)binomial(7,q)binomial(949,q)>0.

Allow these variables to be signed. Test equality only in the 24 rows
with a=0,...,5 and b=0,...,3, the positive-weight modes of L067's
unchanged product dual. Impose no remaining PSD or scalar inequalities
and do not vary the point, base, pairs or weights.

## Conclusion

This rational 24-by-36 equality system is consistent. Its coefficient
and augmented ranks are both 23, giving a 13-dimensional affine solution
space. An explicitly specified rational solution has zero residual in
every original scaled row and every corresponding raw-Y Schur equality.

These necessary equalities therefore do not reject the fixed point.
No nonnegativity assertion about the 36 new variables is made. Remaining
mode inequalities, new/new scalar rows, simultaneous PSD, the whole zero
plane, global moments, labels, measures and RS realization remain open.
The 955–957 bracket is unchanged. This is a local REPRODUCTION of
assessed tools, without a novelty claim. The separate critical review below
retains this equality-only conclusion.

## Proof

**Imports.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-zero-point-tight-mode-consistency.md`.
Import Yinyu Ye, *Conic Linear Programming*, December 2004, revised
October 2017, [author monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Section 2.3 opening, printed p. 42 (PDF p. 55), for scalar
complementarity; Section 1.3.1 Theorem 1.11, printed p. 13
(PDF p. 26), and Section 1.5.1, pp. 23–24 (PDF pp. 36–37), for the
linear-system alternative and elimination. Foundations/10 records these
inspected passages. Only nonnegative scalar slacks with zero weighted
sum are used; no Slater condition, attainment, strict complementarity
or full-SDP optimality is assumed. The specialization evaluates the
prescribed finite system, without reproof of any general theorem.

L067's necessary inequalities specialize Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
and Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://doi.org/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. Factors 68,956
and layers 0,5,6,7 stay in the assessed ranges; singular range conditions
and the entire anchor congruence are retained. Ordinary averaging uses
Sven C. Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 Proposition 1.1 and its indicator proof, p. 2, and
Section 1.2, p. 3, with foundations/12's constant-weight qualification.
No actual-label condition is averaged. These imported results establish
necessity, not this system's consistency. The ancestral dictionary and
mixed-layer decomposition are imported established inputs, not reaudited
in their entirety here.

**Original data and the necessary system.** For each type (l,m,i,j),
the eight atoms with D,E,G bits 4,2,1 are

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

Use (l,m)=(5,5),(5,6),(6,6),(5,7),(6,7),(7,7), with 0<=i,j<=l.
These exhaust 270 types and 1620 ordered presentations. Retain all old
lookups and obtain new column entries from the original RREF at exact
w_star. All original 49 whole-base weighted kernel residuals vanish,
including anchor and actual 86 orbit weights; this is not an unweighted
quotient test. Every complete atom key agrees under all six orders.

At seven/seven, r=7-i,q=7-j give exactly these forced entries:

    Y77(7,7)=p7;
    Y77(7-r,7-q)=0 for 1<=r+q<=4;
    Y77(7-r,7-q)=Y_(r+q,7,q,r) for r+q=5,6.

The remaining 36 complete atom keys are distinct and impose no further
identifications. Preserve their original positive v scaling.

The following finite recipe specifies the entire system without a solver
choice. Use L067's beta sums, S_l, D7 and Johnson eigenvalues E.
After eliminating the full anchor, form its retained old block B_ab
and cross vector t_ab at w_star. Set

    R_ab=t_ab^T B_ab^dagger t_ab/(p7*D7),
    F_ab=sum_(r+q<=6) (Y77(7-r,7-q)/p7) E_(68,a)(r)E_(956,b)(q),
    A_ab=1_(a=b=0)*p7*S7,
    K_(ab,rq)=-E_(68,a)(r)E_(956,b)(q)/v_(r,q),
    b_ab=F_ab-A_ab-R_ab.

The equalities are Kz=b, in lexicographic mode order on
{0,...,5} x {0,...,3}. All 64 old-block range conditions are checked
before selecting the rows. The old blocks are unchanged PSD and every
range condition holds. Exact positive-pivot elimination computes R;
independent two-by-two determinant formulas verify it, including singular
cases. Both retain p_l*p_m*S_l*S_m in the constant correction, giving
the original A_00=p7*S7, rather than an altered normalization.

Let lambda_ab=h_a*k_b be exactly L067's displayed weights. Each of the
24 selected weights is strictly positive. Exact reconstruction gives

    lambda^T K=0 in all 36 columns,     lambda^T b=0.

For any hypothetical PSD completion its selected Schur slacks are
s=b-Kz>=0. The cited scalar complementarity then requires all 24
entries s_ab=0. This makes the equality test necessary. Weighted zero
alone does not prove consistency; the substituted solution below does.

**Solution and rank certificate.** Take exact Gauss–Jordan RREF of
[K|b], scanning pivot columns from left to right. Number the variables
from zero in their specified lexicographic order. Its pivot columns are

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,21,22,23,28,29.

There are 23 pivots; the final augmented row is entirely zero. Set all
13 nonpivot variables to zero, and each pivot variable to the rightmost
entry of its RREF row. This uniquely specifies the rational witness z.
Its full 36 fractions, original K,b, RREF and complete left row
transformation are saved at `/certificate/z`, `/matrix`, `/rhs`,
`/rref` and `/left_row_transform` in
`scripts/finite-support/zero-point-tight-modes-results.json`.
Each transformed row is checked against the original augmented system.
Substitution in all original rows gives (Kz-b)_i=0 for i=0,...,23.
Independent forward elimination on K gives rank 23 and the same pivots;
the substituted solution gives augmented rank 23. Hence the solution
space has dimension 36-23=13. No numerical rank or optimizer status
is used. No sign check of these 36 variables, or verdict on a zero-weight
mode inequality, is used or asserted.

The independent verifier imports no notebook code, optimizer or floating
arithmetic. It realizes each type by actual 68-subsets and counts every
region under all six orders, comparing all keys and forced values.
It recovers the original RREF point and checks all 49 original weighted
kernel residuals. Direct source beta sums reconstruct K independently
of the constructor's Johnson eigenvalue formula; determinant-based
inverse costs reconstruct every right side. Every witness fraction,
all 36 cancellations, the exact weighted zero and all 24 original
selected rows are consumed and checked.

Finally convert z to raw Y by p7*z/v and reconstruct the whole C77
source entry. For every selected mode independent substitution gives

    C77/(p7*D7)-R_ab=0.

Thus all 24 raw-Y and all 24 scaled residuals are zero. The raw check
jointly verifies the scaling, row sign, forced entries and entire anchor
correction. All data are rational; these are exact finite identities.

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/zero_point_tight_modes.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_zero_point_tight_modes.py

The constructor passes 2825 checks with no failures; its complete
certificate is `scripts/finite-support/zero-point-tight-modes-results.json`.
Independent reconstruction passes 1456 checks with no failures; its
complete certificate is
`scripts/finite-support/zero-point-tight-modes-verification.json`.
Both pin input hashes. Full summaries, empty failures, pivots, and all
original/raw residuals were inspected. Programs consume all load-bearing
data; previews are not used to establish an identity.

This parks only equality-based exclusion at this fixed point. Preserve
L067's different immutable-point obstruction and ATTEMPTS/049–051.
The omitted constraints require a separate assessed attempt. An equality
solution is neither simultaneous PSD nor an RS list. No complete
resolution is proposed. The separate critical review below retains this
finite result.

**Separate critical proof review — step 242, 2026-10-15.** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-15-zero-point-tight-mode-critical-audit.md`.
The audit retains all hypotheses, coefficients and conclusions. It reruns
the independent verifier above, passing all 1456 checks, and adds
`scripts/finite-support/critical_audit_zero_point_tight_modes.py`, which
passes 4330 exact checks with no failures. The complete additional
certificate is
`scripts/finite-support/zero-point-tight-modes-critical-audit.json`.
This is a REPRODUCTION audit of the local finite certificate, not a new
general theorem or progress beyond the cited sources.

The original positive rho and p7 are checked, and the 49 fixed-point
coordinates are recovered directly from L065's original RREF and L068's
objective matrix. All 16 entries of that matrix satisfy the stated
negative-square form. The exact w_star agrees with L069 and differs
from L067's immutable point. All 49 reduced compatibility equations are
checked. Independently recomputing each of the 86 orbit weights as
binomial(7,i)binomial(61,l-i)binomial(7,j)binomial(949,l-j), with anchor
weight one, gives zero in all 49 original weighted kernel equations.
The full 121-entry old dictionary and all 86 column entries are retained.
The ancestor kernel and mixed-layer decomposition theorems are imported
established results; their complete earlier derivations are not reaudited.

The rerun verifier reconstructs actual subsets and all eight regions.
The additional audit separately regenerates every atom permutation and
compares all 270 complete records, including all 1620 presentations,
with both saved certificates. Every Boolean, forbidden and represented
lookup agrees. Grouping by (sorted half-distances,i-j) agrees with the
complete atom keys, retaining the source equality invariant. All 28
forced seven/seven entries have precisely the values above, and the
remaining 36 keys are distinct. No extra identification is imposed.

For each of the 64 modes the audit reconstructs the old block and cross
vector directly from the beta sums and fixed entries, retaining the full
p_l*p_m*S_l*S_m anchor correction. It eliminates old layer 6 before
layer 5, independently of the constructor's forward order and the
verifier's determinant formula. All nonzero pivots are positive, and
every zero-pivot cross and residual row vanishes. The 36 two-layer modes
have ranks two in 9 cases, one in 8 and zero in 19; the 13 one-layer
modes have ranks one in 10 cases and zero in 3; 15 modes are new-only.
In every case the cost divided by the original positive p7*D7 equals
the saved R_ab. The coherent positive source congruence is the one
already checked in L067; it depends on the factor sizes and layers,
not on the changed column entries. No ordinary inverse is applied to a
singular old block, and no zero-weight mode inequality is tested here.

The displayed h,k in L067 yield exactly the unchanged 24 positive weights.
Every selected row is independently reconstructed both from the Johnson
formula and the source beta formula, with positive original v scaling.
All 864 coefficients agree with the corresponding original L067 rows;
every new right side agrees with L070. The 36 separate weighted column
sums and the weighted right side are exactly zero. Thus the cited
nonnegative-slack implication applies to hypothetical PSD completions
at this point, without an optimality or attainment assumption.

The audit consumes all 36 witness fractions and verifies zero in each
of the 24 scaled residuals. After replacing the free raw entries by
p7*z/v and retaining all forced entries, it independently reconstructs
C77, including the subtraction p7^2*S7^2 in the constant mode. All 24
raw-Y residuals C77/(p7*D7)-R_ab are exactly zero as well.

All 888 entries of the saved identity L[K|b]=RREF([K|b]) are checked.
Fresh exact elimination, reversing both row and column scan order,
gives rank L=24, rank K=23 and rank [K|b]=23; its complete echelon
matrices and invertible row operations are saved. The specified RREF
pivot columns have unit columns and leading ones, the last augmented
row is zero, and the zero-nonpivot recipe reconstructs the entire saved
witness. These checks justify both ranks and the affine dimension 13
without relying on saved rank summaries or a numerical solver.

Reproduce the additional audit from the notebook with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_zero_point_tight_modes.py`.
Full summaries, failures and both complete residual vectors were inspected;
all other load-bearing arrays were consumed in exact checks, not inferred
from previews. No mathematical repair was needed. Nonnegativity of new
variables, the remaining 40 mode inequalities and new/new scalar rows
remain untested. This audit supplies no simultaneous PSD, global moment,
label, packing or RS conclusion and leaves the 955–957 bracket unchanged.

## Mathlib

Full matching theorem for this prescribed system, scalar complementarity,
and the linear-system alternative: not checked in Mathlib. The cited
primary results and exact certificates supply the inputs used here.
Unknown library coverage is not evidence of absence.
