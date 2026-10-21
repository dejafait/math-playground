# L079 — L078's fixed separator has an attained positive family maximum

## Hypotheses

Use L021's entire original pair prescription, L053's positive singleton
rho, L073's included-anchor PSD base C, and L075's entire unchanged
unordered moment dictionary on 68-subsets of a 1024-point set. Divide
matrices by rho. In particular

    p8=16792471/1181138102168120460>0.

Retain the original seven-column RREF at (0,v_dagger,w_star), all old
entries, and all 28 forced/36 completed seven/seven entries. Fix a
68-subset D and add the indices {D,G} at half-distance eight from D.
Against the old base, use one COMMON real vector t in L076's original
four-parameter family

    f=c+A*t,  t=(t56,t63,t69,t78).

Here c and A are exactly L076's 85-coordinate intercept and four slopes,
with nonpivots 56,63,69,78. Each free column moment is p8*f_j; every
fixed lookup, anchor and Boolean diagonal stays unchanged. Transport
these same coefficients to every new column by point bijections.
Impose full unordered atom-key consistency, old-base kernel compatibility,
and nonnegativity of all column moments. Scalar upper rows and other-anchor
PSD conditions are not imposed.

For eight/eight entries retain all forced unordered values, and keep all
45 unrepresented moments nonnegative, with L078's original positive
scaling. Evaluate exactly L078's 81 mode weights y, as specified by its
canonical I,J system. No separator, pair, base or seven/seven coefficient
is retuned. Write Phi(t) for the weighted right side y^T b(t) of the
original 81 Schur inequalities A_mode*z<=b(t), z>=0.

## Conclusion

There are no additional atom-key equalities or mode-range restrictions
on this four-parameter family. Its column domain is exactly

    T={t in R^4: c+A*t>=0}.

The fixed pairing has the identity, for every real t,

    Phi(t)=V-kappa*(t78-s_star)^2,  kappa>0,
    351861924105/10^6 <= V < 351861924106/10^6.

The maximum V is attained at an explicitly specified rational t in T
with 83 positive free coordinates and exactly f33=f56=0. Thus these
unchanged weights cannot strictly exclude the whole compatible-column
family. They retain their original strictly negative value at L076's
active-set column; L078's immutable-column obstruction is unaffected.

This is a finite REPRODUCTION/specialization of assessed results, not
a source-level novelty claim. Positive pairing is only nonexclusion by
this one separator. It does not give a simultaneous PSD completion,
other-anchor feasibility, global moments, packing or RS list. Arbitrary-
center 67/68-agreement safety and the 955–957 bracket remain open.
The separate critical proof review below retains this result.

## Proof

**Imports and specialization.** The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-17-eight-column-family-fixed-separator.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Factors 68,956 and layers 0,5,6,7,8 satisfy its index
ranges. All 81 modes, including the anchor, singular old blocks and
new-only cases, are required. L078's audited coherent congruence uses
only factors, layers and mode norms, independently of the entries Y;
its positive normalization therefore applies to the affine family too.
Foundations/04,09 retain the source qualifications. No complement
prefactor or labeled averaging is used.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2 and Theorem 2.6. A finite real symmetric block
extension of a PSD base requires range compatibility and a nonnegative
generalized Schur remainder. Singular bases are allowed. L073 supplies
the fixed PSD base; all affine ranges are verified below rather than
inferred from the old active point.

For equal-union moments and permissible ordinary averaging import Sven
C. Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and indicator proof,
p.2, Section 1.2, p.3. Foundations/12 records the constant-weight display
qualification. Here n=1024,d=10,w=68. The ordinary invariant family
preserves complete atom keys and signs; no actual-label exclusion or
representing measure is imported.

The finite nonnegative linear certificate uses Michel X. Goemans,
*Advanced Algorithms*, Lecture 3, 19 September 2001, Theorems 1 and 3,
pp.1–2, [MIT notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
Singular quadratic curvature and affine feasible domains are covered by
Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, revised
[402-page author slides](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
PDF pp.54,105,174–175, slides 4.18 and 5.19–5.20, as inspected in the
assessment and foundations/10. Here an explicit square identity and
admissible point suffice, so no Slater, strict-curvature, compactness or
general attainment theorem is assumed. These known results are imported
without reproof; the prescribed coefficients and sign are the necessary
finite specialization.

**Exact family domain.** Index the retained relations by (l,m,i,j),
l<=m in {5,6,7,8}, 0<=i,j<=l. For E=(D\X) union Y and
G=(D\U) union Z, take |X|=|Y|=l, |U|=|Z|=m,
i=|X intersection U|, j=|Y intersection Z|. The eight membership
atoms, with D,E,G carrying bits 4,2,1, are

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

They are nonnegative, sum to 1024 and give three 68-subsets; choosing
these regions realizes every listed relation. All six permutations of
the atom bits give the complete unordered key. Use constants from L075
for l,m<=7. For l<8,m=8 use L076's constant lookups or p8*f_j.
Evaluate Boolean repetitions at their original lower-order moments;
distinct half-distances 1,...,4 force zero. For every relation and
every available anchor presentation compare ALL FIVE affine coefficients
(constant plus four parameters), including reanchorings outside the
selected shell set. All shared-key differences vanish identically.

This exhausts 500 relations and 3000 presentations. Exactly 36
eight/eight values are forced, as in L078: p8 at r=q=0; zero at
1<=r+q<=4; and Y_(r+q,8)(q,r) at 5<=r+q<=7, where r=8-i,q=8-j.
The other 45 keys, r+q>=8, are distinct and share no fixed lookup.
They remain separate nonnegative variables

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_rq/V_rq,  z_rq>=0.

Here C(n,k) denotes binomial(n,k), zero outside its ordinary range.
The forced values are nonnegative on T: they are a positive fixed
moment, zero, or a column value with f>=0. Every other immutable
column entry is nonnegative by the inputs. Substitution of c and all
four columns of A in all 90 original compatibility equations succeeds
coefficientwise. L076's reviewed whole-kernel exhaustion therefore
applies to every t. The independent mode calculation below confirms
the same statement after full anchor transport. No additional equality
or sign restriction is lost, proving the asserted domain T for this
test. This makes no claim about omitted scalar upper rows.

**Full original-coordinate quadratic.** Define S_l=C(68,l)C(956,l), and

    beta(n,l,m,a,k)=sum_(u=max(a,k))^min(l,m,n-a)
      (-1)^(u-k) C(u,k)C(n-2a,u-a)C(n-a-u,l-u)C(n-a-u,m-u).

For each a,b in {0,...,8}, retain every old layer l in {5,6,7} with
l>=max(a,b). After eliminating the positive anchor, form

    T_lm(t)=sum_(i,j=0)^min(l,m)
       beta(68,l,m,a,i)beta(956,l,m,b,j)Y_lm(i,j;t)
       -1_(a=b=0)*p_l*p_m*S_l*S_m.

Let B_ab be the constant old block and q_ab(t)=(T_l8(t)) its cross
vector. All 306 old nonempty principal minors are nonnegative. Choose
a largest positive principal minor of B_ab and solve its subsystem
for each of the five affine coefficients, setting other inverse
coordinates to zero. Substitution checks every original row of
B_ab*x_ab(t)=q_ab(t), coefficientwise, including singular and zero
blocks. New-only modes have empty old blocks and zero cost. Thus all
81 ranges hold throughout the family.

Put D8_ab=C(68-2a,8-a)C(956-2b,8-b)>0 and write

    R_ab(t)=q_ab(t)^T*x_ab(t)/(p8*D8_ab),
    F_ab(t)=sum_(r+q<=7) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)
                    *Y_88(8-r,8-q;t)/(p8*D8_ab),
    b_(9a+b)(t)=F_ab(t)-1_(a=b=0)*p8*S8-R_ab(t),
    A_mode(9a+b;r,q)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)
                         /(D8_ab*V_rq).

The original inequalities are exactly A_mode*z<=b(t). In particular
the positive p8^2 anchor correction has not been dropped. Each R_ab
is a symmetric quadratic in (1,t); exact inverse-action residuals
justify it without using an unweighted quotient pseudoinverse.

Reconstruct y by L078's canonical 42-by-42 I,J system. Its 81 weights
are nonnegative, sum to one, and have exactly 27 positive entries.
Recomputing all original beta columns gives exactly L078's scaled and
raw moment coefficients: 44 vanish and only the (3,6) coefficient is
positive. These coefficients do not depend on t. Consequently a
negative Phi(t)=y^T b(t) excludes nonnegative completions at that t;
positive Phi(t) gives no such contradiction.

Let zeta=(1,t56,t63,t69,t78), and let M be the unique symmetric
5-by-5 coefficient matrix assembled from the displayed F_ab and R_ab
with these weights: put the affine constant in M00 and split each
affine linear coefficient equally between M0j and Mj0. Then
Phi(t)=zeta^T M zeta. Exact reconstruction gives

    H=-M[1:5,1:5], g=(M01,M02,M03,M04),
    H44=kappa>0, all other H entries zero,
    g1=g2=g3=0.

Indices 1,...,4 here correspond to the four ORIGINAL parameters.
Define s_star=g4/kappa and V=M00+g4^2/kappa. This proves the square
identity in the conclusion. The complete fractions defining M, H, g
are saved without truncation in the certificates; this coefficient
recipe is their exact mathematical specification, not a numerical fit.
Substitution of L076's original active column reproduces exactly L078's
strictly negative pairing. Integer cross-multiplication gives the stated
strictly positive interval for V.

**Exact admissible maximizer.** All following small systems are rational
and nonsingular. For row sets I0=(27,33,56,63) and J0=(5,26,33,56),
in the stated order, define

    t0=-(A_I0)^(-1)c_I0,  t1=-(A_J0)^(-1)c_J0.

The first is L076's original admissible point. Independent substitution
gives c+A*t1>=0 as well. Row 5 of A has only its fourth entry nonzero,
and that entry is negative. Let lambda=-1/A_(5,4)>0 and U=lambda*c5.
The exact identity

    lambda*f5(t)=U-t78

holds coefficientwise, with all other inequality multipliers zero.
Hence t78<=U on T. The second point satisfies t1_78=U, so this bound
is attained. A rational solve of A_J0^T times the four active multipliers
equals -e4 independently reproduces this certificate; only row 5 has
positive weight. No Decimal solver status supplies the bound.

The exact comparisons give

    t0_78 < s_star < U=t1_78.

Define alpha=(s_star-t0_78)/(U-t0_78), and

    t_star=(1-alpha)*t0+alpha*t1.

Then 0<alpha<1; the affine domain T is convex, so t_star is admissible,
and t_star_78=s_star. Direct substitution checks all 85 signs, all 90
original compatibility equations and every fixed/forced moment. Exactly
f33 and f56 vanish; the other 83 free values are positive. Thus
Phi(t_star)=V, attaining the global upper bound from the square identity.
This establishes the claimed fixed-weight nonexclusion, without needing
to choose any of the 45 free eight/eight moments.

**Complete evidence, failures and scope.** Run from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_family_fixed_separator.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_family_fixed_separator.py

The constructor passes 2137 exact checks. Its full certificate is
`scripts/finite-support/eight-family-fixed-separator-results.json`:
input hashes, original c,A, all presentations, every affine range,
all original beta rows, complete quadratic matrices, canonical weights,
raw/scaled coefficients, domain primal/dual, interpolation and signs.
The standard-library-only independent verifier imports no notebook
constructor or optimizer. It passes 7158 checks with no failures;
full evidence is
`scripts/finite-support/eight-family-fixed-separator-verification.json`.
It reconstructs mask permutations independently of actual-support
enumeration, every affine lookup, all old minors and inverse residuals,
every quadratic coefficient, canonical dual weights, all raw/scaled
coefficients, rational domain systems, strict parameter bracket, exact
interpolation, original equations and every forced moment sign. All
load-bearing arrays are consumed, not checked through previews.

The initial zero-nonpivot stationary point has f33<0; a tested flat
boundary and the t78 axis also failed admissibility. An initial attempt
to bound U below s_star failed because the reverse strict inequality
holds. The complete failed certificate is preserved in
`scripts/finite-support/eight-family-fixed-separator-initial-domain-bound.json`;
the final argument uses the verified reverse inequality and interpolation.
No failed assumption is retained. Decimal simplex only proposed J0;
both the feasible point and its domain bound are exact certificates.

This arithmetic verification belongs to the original attempt; the separate
critical proof review below retains it. ATTEMPTS/060 and L078 remain
valid for their immutable column. ATTEMPTS/061 stops only strict family
exclusion by these same weights. Other separators, simultaneous completion,
scalar upper rows, excluded anchors, global consistency and RS realization
are unresolved. A positive separator pairing is not a PSD witness or an
unsafe-list construction.

**Separate critical proof review — step 278, 2026-10-17.** Reuse the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-17-eight-family-fixed-separator-critical-audit.md`.
The review retains the exact domain, global bound and rational attainment,
with no changed mathematical coefficient or hypothesis. This establishes
an independently reviewed local input, not new theory beyond the sources.

The essential ancestor recipes and foundations/04,09,10,12 were checked
against the full manuscript and both original programs. The Schrijver
layer ranges include exactly the stated 81 modes, with the anchor only
at (0,0). The whole-block congruence depends on layers and subset actions,
not on the particular moment coefficients. Sano includes singular and
empty old blocks. The finite point-permutation group preserves this
ordinary family, full unordered keys and nonnegativity. There is no
transport of an actual-label restriction. L076's reviewed whole-kernel
exhaustion and L078's reviewed direct subset actions are imported inputs;
this is not a fresh recursive audit of every ancestor proof.

The independent verifier rerun passes all 7158 checks, including the
complete 306 old principal minors. An additional dedicated audit
reconstructs the original pair equations, factor two and positive rho;
the exact seven-column parameters and original RREF; and the 36-coordinate
seven/seven completion by reverse-variable elimination. All 270 immutable
dictionary values agree. It reconstructs all 85 affine rows from L076's
original RREF, retains the nonpivot identity submatrix, and checks all
five coefficients of every original compatibility equation. All 450
original orbit-weighted kernel residuals vanish, retaining the anchor.

Independently enumerate all 500 relation types. Realize actual supports
by allocating points to the eight disjoint membership regions, then
recount all six ordered presentations point by point. Every atom,
distance, full key, lookup origin and all five affine coefficients agree
with the saved certificate. All shared-key differences vanish. The 36
forced new/new moments obey their Boolean/forbidden/reanchored formulas;
the 45 remaining keys are distinct. This verifies both directions of
the domain claim: the required signs are precisely c+A*t>=0, and every
such t preserves all imposed keys and ranges. No scalar upper row is
included in that claim.

Reuse the 220 complete subset-transition matrices from L078's critical
audit, with unchanged input hashes, and check every coordinate of every
action on its orthogonal bases. Recheck positive norms, signed beta
ratios and every reference-eight triangle identity. Apply these direct
actions separately to all five affine coefficients. The same coherent
positive diagonal congruence matches every old entry and every affine
cross entry, including both rectangular directions and the full anchor
term. Reverse-order elimination of each weighted old block retains every
zero-pivot row and all five zero-pivot cross residuals. All 81 ranges
pass, including 17 new-only cases. Every one of the 25 quadratic cost
coefficients per mode agrees with the independent source-block inverse
calculation. All original affine diagonal and 45 free-coordinate rows
agree as well. No quotient pseudoinverse is assumed.

Read I,J from L078's manuscript and independently solve its 42-by-42
system in reverse variable order. All 81 weights agree; 27 are positive,
all are nonnegative, and their sum is one. Reconstruct all 45 scaled
and raw moment sums: 44 vanish, and exactly (3,6) is positive. Assemble
the entire symmetric 5-by-5 pairing matrix from the direct actions and
compare every coefficient to

    V-kappa*(t78-s_star)^2.

The comparison is exact, kappa>0, and both rational interval gaps certify
the displayed positive interval for V. Substitution of the original
column reproduces L078's unchanged negative value.

Read I0,J0 from this manuscript and solve both defining 4-by-4 systems
afresh. All 85 signs hold at both vertices, with zero sets exactly I0
and J0. Row 5 has only its negative t78 coefficient; its positive
multiplier gives the entire coefficient identity lambda*f5=U-t78.
A separate transposed active-system solve recovers only that multiplier.
Both differences s_star-t0_78 and U-s_star are strictly positive.
The exact interpolation therefore has 0<alpha<1. Check all 85
interpolated values against the convex combinations of the endpoint
values: exactly coordinates 33,56 vanish and all other 83 are positive.
Its t78 equals s_star, the pairing equals V, every fixed/forced moment
is nonnegative, and all 90 original weighted kernel residuals vanish.
The global square upper bound and this explicit admissible point prove
attainment without compactness, strict curvature, or a general existence
theorem. Positive pairing is not a simultaneous PSD certificate.

Run from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_family_fixed_separator.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_eight_family_fixed_separator.py

The dedicated audit passes 8699 additional exact checks with no failures.
Full additional evidence is
`scripts/finite-support/eight-family-fixed-separator-critical-audit.json`:
input hashes, reconstructed ancestors, entire affine family and atom
presentations, weighted residuals, every direct mode and reverse singular
elimination, raw/scaled sums, the full square matrix, both vertices,
exact interval/bracket gaps and interpolated signs. The audit imports
arithmetic helpers from L078's audit but no L079 constructor, verifier
or optimizer. Complete load-bearing arrays are consumed. Its initial
serialization-only comparison failure (four integer ones versus rational
pairs [1,1]) is preserved in
`scripts/finite-support/eight-family-fixed-separator-critical-audit-initial.json`;
correct rational encoding changes no mathematical value. The original
inadmissible stationary representative and failed U<s_star certificate
are also preserved and checked as failures, not used as premises.

ATTEMPTS/061 retains only the stop on these fixed weights over this family.
ATTEMPTS/060 and L078's immutable-column rejection remain intact. Other
separators, joint completion, scalar upper rows, other anchors, global
moments and RS realization remain unresolved; the 955–957 boundary is
unchanged. No argument or mathematical dependency changed in this review.

## Mathlib

Full matching prescribed-family maximum and constrained union-moment
completion: not checked. Full mixed-layer algebra, singular generalized
Schur complements and rational LP/QP certificates: not checked. Supporting
PSD, rational arithmetic and binomial results: not checked. Unknown
coverage is not evidence of absence; general source results are imported,
and no source-level originality is claimed for this finite specialization.
