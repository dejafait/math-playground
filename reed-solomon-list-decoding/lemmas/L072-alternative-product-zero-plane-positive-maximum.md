# L072 — The alternative product pairing has an admissible positive maximum

## Hypotheses

Retain L061's entire anchored five/six-shell PSD base and all L062
moments and scalar rows on the 68-subsets of a 1024-point ground set.
Use the original singleton normalization and pairs from L069:

    rho=(binomial(1024,64)/binomial(68,64)+1)/(2 binomial(1024,68))>0,
    p5=1/68881143660, p6=133/9357995374380,
    p7=3539/248922676958508>0,
    p13=26968792942808537/1896913598738625271419892200.

All other pairs through p13 remain exactly L069's original pairs.
Use L065's original RREF, coordinate order, particular vector c and
directions a^27,a^33,a^42, with one common real column parameter triple

    f=c+u*a^27+v*a^33+w*a^42.

Fix w=w_star from L068, retaining every fixed entry, the anchor,
Boolean/forbidden lookups, unordered identifications and whole-base
kernel compatibility. Require all 49 free f_j>=0 and all 1530 column
scalar rows of L069 on the complete 85-type five/seven and six/seven
domain, with all six presentations and original pairs through p13.
The 2178 old scalar rows remain unchanged.

Test exactly L071's product weights, with no retuning. There are 36
remaining seven/seven variables, in L071's original positive scaling;
no new/new scalar upper row is imposed or tested. In particular the
parameter v above is distinct from the positive orbit factors v_(r,q).

## Conclusion

The maximum of this product dual's fixed pairing over the specified
scalar-admissible plane is attained and lies in

    [174659686133710,174659686133711).

It is strictly positive. An exact rational maximizer has u=0,
v=v_dagger>0,w=w_star. Its 49 free column coordinates have 48 positive
entries and exactly one zero, f_27=0. All column scalar rows, original
weighted kernel equations and forced entries are retained.

Thus L071's unchanged product weights cannot strictly exclude this
whole plane. This preserves L071's negative pairing at u=v=0 and
L067's different immutable-column obstruction. It supplies neither
a simultaneous PSD completion nor its impossibility at this new point,
and gives no global moment, support/list bound or RS realization.
Arbitrary-center safety at 67/68 agreements and the 955–957 bracket
remain open. This is a finite REPRODUCTION/specialization of assessed
methods, without a novelty claim. The separate critical proof review below
retains this conclusion.

## Proof

**Imported tools and scope.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-16-alternative-product-dual-zero-plane.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B
(64)–(65), printed pp.5–7. The factors 68,956 and layers 0,5,6,7
are within its ranges. Use exactly L067's audited coherent mixed-layer
normalization, with the full anchor transported before taking Schur costs.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://doi.org/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. The retained
old blocks are PSD, and the varying cross vectors must annihilate their
whole kernels; singular blocks are allowed. Import ordinary union moments
and constraint-preserving averaging from Sven C. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and indicator proof, p.2, and Section 1.2,
p.3, with foundations/12's constant-weight qualification. Only the
ordinary unlabeled slice is used. There is no actual-label averaging
or representing-measure assertion.

The applicable convex-QP scope is Boyd–Vandenberghe, with Parth Nobel,
*Convex Optimization*, revised 402-page
[author slides](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
PDF pp.53–54,97–98,105,174–175; slides 5.19–5.20 give KKT sufficiency,
permitting singular PSD Hessians and boundary points without a Slater
hypothesis for sufficiency. Here the exact square identity below directly
certifies the bound, so no converse, compactness or attainment theorem
is needed. These general results are imported without reproof. None
evaluates the present numerical specialization.

**Exact domain and coefficients.** The complete affine family, all
unordered identities and singular ranges are those of L068; L069 fixes
its scalar rows. Let P_j=(c_j+w_star*a^42_j,a^27_j,a^33_j), so
f_j=P_j dot (1,u,v). A free moment is y=p7*f_j. For each of the 85
types (l,7,i,j), l=5,6 and 0<=i,j<=l, form all six presentations
of the eight atoms

    (949-l+j,7-j,l-j,j,i,l-i,7-i,61-l+i).

For each presentation put a=atom4+atom5, b=atom4+atom6,
h=atom2+atom6. The three affine scalar slacks are exactly

    y, p_a-y, 1+y-p_a-p_b.

Old lookups and forbidden entries precede free-key assignment. The
complete domain is the intersection of these 1530 closed halfplanes
with all 49 P_j dot (1,u,v)>=0. This description includes every row
through p13 and boundary zeros; it does not replace the domain by a
rectangle, a sample or only its active rows.

To specify the objective completely, let C(n,k)=binomial(n,k), zero
outside 0<=k<=n, and use the source coefficients

    beta(n,l,m,a,t)=sum_u (-1)^(u-t) C(u,t) C(n-2a,u-a)
                              C(n-a-u,l-u) C(n-a-u,m-u),
    E_(n,a)(r)=sum_(s=0)^r (-1)^s C(a,s) C(7-a,r-s) C(n-7-a,r-s).

The beta sum ranges from max(a,t) to min(l,m,n-a). Set
S_l=C(68,l)C(956,l), D7=C(68-2a,7-a)C(956-2b,7-b)>0. At mode
(a,b) in {0,...,7}², present old layers are l=5,6 with max(a,b)<=l.
With every Y an affine four-vector in (1,u,v,w), form

    C_lm=sum_(i,j) beta(68,l,m,a,i) beta(956,l,m,b,j) Y_(l,m,i,j)
          -1_(a=b=0) p_l p_m S_l S_m.

The fixed old-layer block is B_ab; t_ab consists of its cross entries
C_l7. Its energy is R_ab=t_ab^T B_ab^dagger t_ab/(p7*D7).
The inverse is only on the range. For B=[[x,y],[y,z]], positive
determinant gives numerator z*t5²-2y*t5*t6+x*t6² divided by xz-y²;
when singular with x>0 use t5²/x, with x=0,z>0 use t6²/z, and
with B=0 use zero. A positive one-layer block uses its scalar inverse;
a zero one-layer or new-only block contributes zero. The corresponding
range equations are checked coefficientwise before any energy is used.

Retain all 28 forced seven/seven entries:
Y77(7,7)=p7, zero for 1<=r+q<=4, and
Y77(7-r,7-q)=Y_(r+q,7,q,r) for r+q=5,6. Put

    F_ab=sum_(r+q<=6) [Y77(7-r,7-q)/p7] E_(68,a)(r) E_(956,b)(q),
    A_ab=1_(a=b=0) p7*S7.

Use precisely L071's

    h=(1,12261/455,15555/56,4099261/3640,0,0,0,0),
    k=(1,4531475/6657,136607358056/632415,27321109096/665,
       1028453048809043/210805,9295091464315239/30115,0,0),
    lambda_ab=h_a*k_b.

All weights are nonnegative and exactly 24 are positive. Define the
unique symmetric four-by-four matrix M by

    (1,u,v,w) M (1,u,v,w)^T = sum_ab lambda_ab*(F_ab-A_ab-R_ab).

The right side is a quadratic by the fixed inverse-on-range formulas;
this equality uniquely fixes every rational coefficient. For
T(1,u,v)^T=(1,u,v,w_star)^T, set N=T^T M T. All these numbers are
uniquely specified by the original RREF and the displayed finite sums;
there is no optimizer choice. Full fractions are saved in both certificates.

**Exact square and admissible maximizer.** Rational evaluation gives
N_1j=N_j1=0 for j=0,1,2 and N22<0. Set

    alpha=-N22>0, beta_v=N02, C0=N00,
    v_dagger=beta_v/alpha,
    V=C0+beta_v²/alpha.

The exact sign and bound checks give beta_v>0 and
174659686133710<=V<174659686133711. Consequently on every real (u,v),

    Phi(u,v,w_star)=V-alpha*(v-v_dagger)²<=V.

The Hessian of -Phi is PSD of rank one, with zero linear term along
its null u-direction. This calculation explicitly handles singular
curvature instead of assuming strict concavity in two variables.

At u=0,v=v_dagger, direct exact substitution gives all 49 f_j>=0,
with exactly f_27=0. All 1530 new scalar slacks are nonnegative with
minimum zero; all 2178 old rows are unchanged and pass. Every original
weighted whole-kernel residual vanishes, with the anchor and actual
86 orbit weights retained. All forced seven/seven entries are nonnegative.
Thus this point belongs to the entire specified domain and attains V.
The constrained maximum is V without any need to decide boundedness
of the parameter polyhedron. No conclusion uses an unattained supremum.

Every one of the 36 free coefficients still cancels under these same
weights, both in the original v_(r,q)-scaled variables and directly in
raw Y coordinates. The cancellations depend only on the unchanged
Johnson transforms, not the column parameters. Direct raw source sums
retain the full p7²*S7² constant-mode subtraction and reproduce every
normalized right side. The strictly positive pairing therefore stops
these weights as a strict-exclusion certificate. It does not assert that
the 64 inequalities can be met simultaneously at the maximizer.

**Complete arithmetic evidence.** Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/alternative_product_zero_plane.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_alternative_product_zero_plane.py

The constructor passes 864 checks. Its complete evidence is
`scripts/finite-support/alternative-product-zero-plane-results.json`:
input hashes, 270 types/1620 presentations, affine old blocks and cross
vectors, all 64 ranges and costs, both cancellation vectors, M,N,
the exact square data and all witness scalar slacks.

The independent verifier imports no notebook code or optimizer and
uses no floating arithmetic. Its 6114 checks all pass. It reconstructs
all actual support presentations, Boolean/forbidden and shared-key
lookups, all 1530 affine scalar rows and 2178 old rows. It reconstructs
N by polarization of six direct source-sum evaluations with sequential
positive-pivot range elimination, independently of the constructor's
determinant formulas and quadratic matrices. Since the degree is at
most two, those six evaluations determine all six symmetric coefficients.
It then checks every mode directly at the exact maximizer, the raw
anchor-corrected pairing, all scaled/raw cancellations, every sign and
all 49 original weighted kernel residuals. Full evidence is
`scripts/finite-support/alternative-product-zero-plane-verification.json`.
The full summary and empty failure list were inspected; the computations
consume complete relevant arrays, not previews.

The first constructor report's false strict-concavity expectation is
preserved in `scripts/finite-support/alternative-product-zero-plane-initial.json`;
rank-one curvature is the corrected result. The first verifier report,
`scripts/finite-support/alternative-product-zero-plane-verification-initial.json`,
preserves 268 lookup-check failures: a presentation outside retained
layers provides no lookup, while every available prescribed lookup must
agree. Correcting that distinction retains all full-key and actual-region
checks; no mathematical coefficient or witness changed. Separate critical
review of this finite reproduction is supplied below.

**Separate critical proof review (2026-10-16).** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-16-alternative-product-zero-plane-critical-audit.md`.
The 6114-check independent verifier was rerun with no failures. The
additional standard-library-only audit
`scripts/finite-support/critical_audit_alternative_product_zero_plane.py`
passes 9027 exact checks; its full certificate is
`scripts/finite-support/alternative-product-zero-plane-critical-audit.json`.
This verifies the existing finite reproduction, without a new general
result or improvement to the RS boundary. The following describes the
mathematical coverage rather than relying on check counts.

Recover all 49 affine coordinates from L065's original augmented RREF,
whose nonpivots are precisely 27,33,42. Substitution into every original
compatibility equation gives the original constant right side and zero
in each parameter direction. Obtain w_star from L068's original matrix,
checking its entire negative-square identity and its positive curvature
coefficient. The plane coefficients agree exactly with L069 and the
constructor. Recompute rho, retain the original pairs through p13, and
check p5,p6,p7,p13 against the displayed fractions. L069's pair derivation
and source scalar normalization remain imported established inputs.

Regenerate the complete type domain independently of its saved list:
36 five/five, 36 five/six, 49 six/six, 36 five/seven, 49 six/seven and
64 seven/seven types. Permuting the eight atoms gives all 1620
presentations, each with nonnegative atoms, ground-set size 1024 and
three support sizes 68. Compare every full record with the constructor;
the rerun independent verifier also counts actual subsets point by point.
Every available Boolean, forbidden or prescribed lookup agrees
coefficientwise. Canonical full keys agree across types; the source
index consisting of the sorted distance triple and t-s determines the
same key. The 36 unforced seven/seven keys remain distinct and all 28
forced entries are retained. In particular, an absent lookup is never
used to override a present one.

All 1530 affine column scalar rows are reconstructed, including the
presentations requiring p13, and all 2178 unchanged old scalar slacks
are recomputed with their actual atom data. They are exactly the domain
in the hypotheses, not a sampled or reduced set of constraints. All 86
orbit weights are independently recovered as 1 for the anchor and
C(7,i)C(61,l-i)C(7,j)C(949,l-j) for each shell orbit. Substituting every
affine coefficient of the complete column into each of the 49 weighted
kernel vectors gives zero. L065's already proved kernel exhaustion and
averaging argument supply the full-space interpretation; this audit does
not substitute quotient dimensions for full-space dimensions.

Import L067's audited coherent mixed-layer bases and full decomposition,
which are independent of the changing columns and weights. Reconstruct
all 118 direct subset-transition matrices and check their complete actions
on those bases, retaining both rectangular directions. Recover the positive
norms and use the same positive scales as in L067/L068. For each of the
64 modes, let N_l denote the product basis norm. The weighted old block
and every affine cross coefficient again satisfy

    K_lm=(N7/D7)*s_l*C_lm*s_m,  s7=1.

The constant action subtracts p_l*p_m*S_m before multiplication by N_l;
this transports the entire anchor. Cross directions agree in weighted
coordinates, not merely up to independent signs. Thus a single congruence
applies to each entire block; no isolated pseudoinverse is transported.

Eliminate the weighted old layers in the reverse order, six before five.
Every positive pivot contributes the outer product of its complete
affine residual cross vector divided by the pivot. At a zero pivot,
both its remaining old row and all four cross coefficients vanish.
Among 36 two-old-layer modes the ranks 2,1,0 occur 9,8,19 times;
among 13 one-old-layer modes ranks 1,0 occur 10,3 times; the 15 new-only
modes contribute zero cost. Divide by p7*N7. Every entry of every
resulting four-by-four energy matrix agrees with the source-normalized
constructor and L068's prior coefficientwise audit. The whole affine
family therefore satisfies the singular ranges, not just the maximizer.

Read h,k directly from this manuscript and check equality with L071's
24-positive-weight product. Reconstruct the fixed part from the raw
source beta sums on all 28 entries, subtracting p7^2*S7^2 in the constant
mode before division by p7*D7. Every fixed affine coefficient agrees.
All 64-by-36 scaled coefficients agree with L071's original matrix;
all 36 scaled cancellations and all 36 raw-Y cancellations vanish.
Summing the independently reconstructed energies and fixed parts gives
every entry of M, and restriction gives every entry of N. These agree
with both the constructor and the verifier's independent polarization.

The u row and column of N vanish exactly, alpha=-N22>0 and beta_v=N02>0.
The identity Phi=V-alpha*(v-v_dagger)^2 therefore holds for every real
(u,v), including points outside the scalar domain. For the saved full
rational V=n/d with d>0, exact integer comparisons give

    174659686133710*d <= n < 174659686133711*d.

The complete rational maximum and both bound slacks are saved in the
additional certificate. At (0,v_dagger,w_star), precisely f27 is zero;
the other 48 free entries are strictly positive. Every column scalar
slack is nonnegative; every forced entry is nonnegative. All 49 original
weighted kernel residuals vanish. Substitution into every original mode
agrees with the verifier, and the weighted raw pairing is exactly V.
Thus this actual point attains the universal square bound on the stated
domain. No compactness or strict concavity in two variables is assumed.
The old point's pairing is still exactly L071's strictly negative value.

Both initial reports are preserved. Every mathematical field saved in
the initial constructor agrees with the final constructor; its only
failure was the false expectation of strict two-variable concavity.
The verified null u row and strictly negative v curvature justify the
rank-one correction. The audit also matches each of the initial
verifier's 268 failure names to its exact type and presentation. In all
268 cases the full-key value was prescribed, but that presentation's
incident layer pair lay outside the retained six layer pairs and hence
had no lookup. Every available lookup is still checked, as are every
full-key identification and source equality. The complete initial/final
verifier mathematical fields agree, including the quadratic, maximizer,
all scalar evidence, mode values, kernel residuals and cancellations.
Neither correction changed a coefficient, constraint or witness.

Reproduce from the notebook with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_alternative_product_zero_plane.py`.
The complete summary, empty failure list and full rational maximum were
inspected; the audit consumes all relevant arrays, not previews. The
review retains only the claimed positive maximum. Seven/seven scalar
upper rows, simultaneous PSD completion, other duals, global consistency,
representing measures and common-center RS realization remain unproved.
The 955–957 bracket is unchanged.

## Mathlib

Full matching prescribed-family/product-pairing theorem: not checked.
Supporting mixed-layer decomposition, singular-Schur, rational matrix
and convex-QP/KKT coverage: not checked in Mathlib. The primary results
above and exact finite certificates are the inputs used. Unknown
availability is not evidence of absence.
