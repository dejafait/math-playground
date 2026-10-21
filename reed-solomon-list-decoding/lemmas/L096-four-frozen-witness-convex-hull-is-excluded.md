# L096 — The four frozen moment witnesses have no passing convex mixture

## Hypotheses

Use the ordinary union-moment slice n=1024,d=10,w=68, divided by
L053's positive rho, with L021's original pairs, L073's included-anchor
five/six/seven base, L075's complete immutable dictionary and seven-column
RREF/completion, and L076's affine columns. Freeze the columns to exactly
L086's parameters: the first four coordinates of `witness/original` in
`scripts/finite-support/affine-sign-phase-one-results.json`, followed by
L083's stationary t78=s. Keep

    p8=16792471/1181138102168120460>0.

Let z^(1),z^(2),z^(3),z^(4) be the complete `witness/z` arrays in, respectively,

    scripts/finite-support/fixed-column-new-only-results.json
    scripts/finite-support/fixed-column-zero-old-block-results.json
    scripts/finite-support/zero-block-plus-3-4-results.json
    scripts/finite-support/two-mixed-row-results.json

These are precisely L088,L090,L092,L094's frozen moment witnesses.
Their complete `witness/raw_moments` arrays are also fixed inputs.
Index all 45 coordinates lexicographically by (r,q),0<=r,q<=8,r+q>=8,
and retain the same strictly positive scaling at every vertex:

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q),
    S=diag(p8/V_rq), Y_88(8-r,8-q)=(S*z)_rq.

C(n,k)=0 outside 0<=k<=n. All 85 domain rows,90 original/weighted
kernel equations,500 types/3000 presentations,36 forced entries,
28 selected equalities,45 signs and 81 original included-anchor modes
are retained. In particular no L094 extra-row control is assumed at
the other vertices. The full anchor and whole singular ranges remain.
Foundations/04,09,10,12's ancestral PSD,uniqueness,whole-kernel and
normalization contracts are conditional imports, not recursively audited
here. Scalar upper rows,other anchors and global consistency are not
assumed to hold at any vertex or mixture.

## Conclusion

The convex hull of these four witnesses does not meet all 81 original
mode inequalities. One nonnegative row separator suffices: weight one
on i=32,mode(a,b)=(3,5), and zero on all other rows, with i=9a+b.
At the four vertices, in the order above, the normalized remainders lie
in the following exact half-open integer intervals:

| Witness | Remainder b_32-A_32*z |
|---|---|
| L088 | [-20451752,-20451751) |
| L090 | [-18663385,-18663384) |
| L092 | [-2716330,-2716329) |
| L094 | [-3232205,-3232204) |

Every convex mixture therefore has remainder strictly less than
-2716329, whereas the required lower bound is zero. This is a finite
RESEARCH / REPRODUCTION specialization of assessed methods, not a claim
of progress beyond the sources checked. It stops exactly this four-point
hull; it excludes neither all completions at L086's columns nor any
larger family. All individual subsystem passes and rejections remain.
The arbitrary-center 67/68-agreement gap and 955–957 bracket are unchanged.
The separate conditional critical proof review below retains this hull
exclusion; its ancestral qualifications and restricted scope are unchanged.

## Proof

**Known inputs and specialization.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-19-fixed-column-four-witness-convex-hull.md`.
Michel X. Goemans, *Advanced Algorithms*, Lecture 3,19 September 2001,
Theorems 1 and 3,printed pp.1–2,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
supplies the standard named Farkas alternative for finite linear systems.
MIT 6.854 (2020 compilation),
[*Linear Programming* notes](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction and Linear Equalities and Basic Feasible Solutions through
tight-system reconstruction, covers rational standard-form certificates.
Here the certificate is simply one row; no LP solve or general theorem
reproof is needed.

For the conditional matrix interpretation reuse Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*,IEEE TIT 51 (2005),2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47),Theorem 1 (51),III.A (52)–(59),III.B (64),
printed pp.5–7. Ground sets 68,956 and layers 0,5,6,7,8 satisfy its
unequal-layer hypotheses; both rectangular directions and the fixed
positive congruence are retained. No actual-label averaging or suspect
complement prefactor (61) is used. The ordinary union-moment input is
Sven C. Polak,[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017,Section 1.1 (1)–(3),Proposition 1.1 and indicator proof p.2,
Section 1.2 p.3, with constant weight retained. For old PSD,whole range
and a scalar new coordinate reuse Takashi Sano,*Moore-Penrose inverse,
generalized Schur complement and inertia*,27 February 2026 version of
record,[Section 2](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Corollary 2.2,Theorem 2.6 including both singular directions,and Lemma 2.7.
The concrete negative quadratic form below does not require old-block
invertibility. These inputs and their qualifications are unchanged.

**Original and raw rows.** Use the complete original formulas retained
in L094,L095. Define

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

Write S_l=C(68,l)C(956,l). For mode i=9a+b,old layers l,m in
{5,6,7} at least max(a,b),and the fixed raw dictionary,put

    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m,
    B_i=(T_lm), c_i=(T_l8), B_i*x_i=c_i.

Reconstruct both rectangular directions,all old principal minors and
every affine range equation. Choose a nonsingular principal submatrix
of maximal size,solve there by Cramer's rule and fill zeros outside.
Check every coordinate of B_i*x_i=c_i,including empty and singular
cases,and agreement of c_i^T*x_i with the full affine inverse action.
The current columns,base and inverse costs are identical at all four
vertices; only the 45 moments vary.

Let F_i be the full forced diagonal contribution,including its affine
evaluation at the frozen columns,and H_i=1_(i=0)*p8^2*S_8^2. Put

    D_i=C(68-2a,8-a)C(956-2b,8-b)>0, M_i=p8*D_i>0,
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    b_i=(F_i-H_i-c_i^T*x_i)/M_i.

Then the complete raw Schur remainder is exactly

    R_i(z)=F_i-H_i-c_i^T*x_i
           +sum_(rq) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)*(S*z)_rq
          =M_i*(b_i-A_i*z).

All 81 diagonal terms are retained,including forced and free entries,
and the constant anchor correction is used in mode zero. At i=32 the
mode is nonconstant,so H_32=0. For the full block
K_i(z)=[[B_i,c_i],[c_i^T,d_i(z)]],the fixed vector v_i=(-x_i,1)
satisfies v_i^T K_i(z)v_i=R_i(z) by direct multiplication. Thus a
negative normalized remainder excludes that block also when B_i is
singular. The coherent positive source congruence preserves this sign
under the stated ancestral contracts.

**Complete finite evidence.** Full array/hash binding checks identical
points,coordinate orders,p8,volumes,scales and every coordinate of all
four z/raw pairs. The 85 domain factors are nonnegative. All 90 original
and weighted kernel equations,500 full records with all 3000 ordered
presentations,and the exact 36-forced/45-free partition are retained.
The full original coefficient arrays are compared with the independent
original reconstruction and separately audited source arrays. Complete
singular ranges and all 306 old principal minors pass. All 28 original/raw
equalities are zero at every vertex,and every vertex's own retained
controls is checked in its own saved row order. No additional L094 row
is silently imposed on another vertex.

All 81 normalized remainders at all four vertices are computed by
b_i-A_i*z. Independently sum the full 81-term raw diagonal at every
vertex and mode,subtract the full anchor and fresh inverse cost,and
check R_i=M_i*(b_i-A_i*z). The independent verifier also uses

    e(n,a,r)=sum_(h=0)^r (-1)^h C(a,h)C(8-a,r-h)C(n-8-a,r-h),
    beta(n,8,8,a,8-r)=C(n-2a,8-a)*e(n,a,r),

checking every coefficient identity against a separate beta
implementation. It obtains the bounds from the full affine inverse
action and directly checks all ranges,principal minors and all 324
original/raw residual identities. Full rational arrays,all raw diagonal
terms and original remainders are saved,not inferred from previews.
The negative-row counts at the four vertices are 16,14,13,14. The
common negative indices are {32,42,50,52,60,68}; only index 32 is needed.
Every interval in Conclusion is checked by exact rational comparison.

The complete 81-vector w with w_32=1 and w_i=0 otherwise is nonnegative.
Its four vertex pairings are precisely the four displayed remainders.
For any lambda_k>=0 with sum_k lambda_k=1,the same fixed b_32 gives

    b_32-A_32*sum_k lambda_k*z^(k)
      =sum_k lambda_k*(b_32-A_32*z^(k)) < -2716329 < 0.

The strict inequality holds because every summand's remainder is
strictly below -2716329 and at least one lambda_k is positive.
This contradicts the required mode inequality. Positive raw scaling
gives the same contradiction in raw coordinates. Mixing columns would
change inverse costs and is not part of this argument.

The completed commands were

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/four_witness_hull.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_four_witness_hull.py

The first has 1662 passing checks; the independent verifier has 916,
with no failures. Complete exact certificates are
`scripts/finite-support/four-witness-hull-results.json` and
`scripts/finite-support/four-witness-hull-verification.json`.
Both scripts refuse to overwrite existing evidence. A reproduction
should set the imported module's OUT to a fresh notebook-local path
before invoking main; the verifier calls no constructor or optimizer.
An initial normalization-field exception and subsequent L090 control-
order mismatch are preserved in the initial-binding and control-order-
failure certificates described in the working record. Both were schema
issues; the final complete original/raw arithmetic and retained controls
pass without changing any mathematical input or target.

No hull enlargement,free-moment solve,column variation or full-row/conic
restart occurred. Scalar upper rows,other anchors,other columns/base/pairs,
global moments,representing measures and RS realization remain open.
The original calculation above is arithmetic verification of the restricted
hull certificate. Its later conditional critical review follows.

**Separate conditional critical proof review — step 352, 2026-10-19–20.**
The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-four-witness-hull-critical-audit.md`
authorizes this exact audit. The review retains the stated conclusion;
no mathematical coefficient, input vector, hypothesis or bound changes.
This is local progress from an unaudited to a conditionally reviewed
finite input, RESEARCH / REPRODUCTION, not a new mathematical discovery
or an improvement of the RS bracket. The cited primary results above
are reused; no general theorem is reproved.

The independent source recipe checker reconstructs L021's original
pairs and positive rho, the entire L073/L075 dictionary and seven-column
completion, L076's original RREF family, and the frozen L086 point.
It checks all 85 domain rows, all 90 original and weighted kernel
equations, and all 500 actual-support types with their 3000 presentations.
All 36 forced entries and the 45 distinct free keys agree. The 220
subset-transition matrices are reconstructed in both rectangular
directions, and their orthogonal bases and positive congruence factors
are checked. This is a finite recheck of the imported recipes; it is
not a recursive proof of foundations/04,09,10,12's ancestral contracts.

The complete original hull and verification certificates, all four
complete z/raw arrays, and their recorded inputs are consumed and bound.
Every coordinate has the same positive scale and the same frozen point.
The independent verifier is rerun to a fresh path and all its mathematical
arrays agree with its earlier certificate. A further audit compares all
81 complete source rows with the freshly reconstructed rows, including
all 306 old principal minors, every whole range equation, inverse vector,
energy, forced term and the full constant anchor correction. It checks
each vertex's controls in the order derived from its own defining set:
17,43,44,45 mode rows respectively. All 28 equalities hold at each vertex,
and all 180 original/raw moment sign pairs pass. No extra mixed row from
L094 is imposed at another vertex.

Here is the full weighted transport checked by this review. For a mode
(a,b), let N be the product of the squared norms of the freshly generated
monic degree-a and degree-b orthogonal vectors on layer eight of the two
Johnson factors. Let D=D_i from the proof above. Both N and D are
strictly positive. In a factor of size n, write n_(l,a) for that squared
norm on layer l and g_(n,l,8,a,k) for the checked scalar action of the
intersection-k transition from layer eight to layer l. For each retained
old layer l define

    r_(n,l,a) = n_(l,a)*g_(n,l,8,a,l)/beta(n,l,8,a,l),
    h_l = r_(68,l,a)*r_(956,l,b)/(N/D).

All denominators in these expressions are nonzero and all h_l are
positive; this is checked in every represented mode. Put h_8=1 and
H=diag(h_l for old layers,1). The full symmetric weighted block is

    K_weighted(z) = (N/D)*H*K_i(z)*H.

Every old, cross and new diagonal entry satisfies this identity, including
the anchor subtraction when i=0. In particular, with the complete fixed
range solution x_i, the vectors

    v_i=(-x_i,1), v_weighted=(-x_(i,l)/h_l for old layers,1)

have quadratic values R_i(z) and (N/D)*R_i(z), respectively. These
identities hold for empty and singular old blocks as well. They are
checked by full matrix multiplication at all four vertices and all 81
modes: all 324 normalized/raw/weighted remainder comparisons pass.
The entire four source and four weighted offending blocks at i=32,
the test vectors and their exact rational values are saved in the audit
certificate. No numerical eigenvalue, inverse of a singular block or
quotient pseudoinverse supplies the sign.

The complete 81-vector separator is checked to equal the unit vector
at 32=(3,5), not merely to have a nonempty positive support. Every one of
the four manuscript intervals is checked by exact integer/rational
comparison. The certificate stores the four strictly positive margins
-2716329-(b_32-A_32*z^(k)). With fixed columns and scales, the coefficient
of each simplex variable lambda_k in the affine remainder is exactly
its corresponding vertex remainder. Since lambda_k>=0 and their sum is
one, the weighted sum of these positive margins is positive: at least one weight
is positive. This verifies strict separation on the whole simplex,
including its boundary, without sampling mixtures or varying columns.

The preserved normalization-field exception has the same complete input
binding as the final result. The preserved control-order failure has
identical complete reconstructed rows and vertex arrays; its only nine
failures are the recorded L090 control-order comparisons. The audit
checks all 43 L090 rows in their actual order, resolving that mismatch
without changing mathematics. The initial exception itself was recorded
historically, not re-executed as part of this audit. An initial use of the
JSON inspector during this review encountered Python's integer-digit
limit; setting PYTHONINTMAXSTRDIGITS=0 allowed bounded inspection without
changing shared infrastructure or certificate data.

The completed reproduction command is

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_four_witness_hull.py

It invokes only the independent source checker and verifier, not a
constructor or optimizer. The source reconstruction passes 7993 checks,
the hull verifier 916, and the additional critical audit 1309, all with
zero failures. Full certificates are
`scripts/finite-support/four-witness-hull-critical-source.json`,
`scripts/finite-support/four-witness-hull-critical-verification.json`
and `scripts/finite-support/four-witness-hull-critical-audit.json`.
The wrapper refuses to overwrite any of these files; reproductions must
use fresh notebook-local paths for all three outputs. The full input
arrays and mathematical identities, not hashes or summary flags alone,
establish the finite verdict. No new mathematical dependency is added.

The audit closes only the pending conditional review of this four-point
hull. It preserves each subsystem witness, all capped prescriptions and
all original failure evidence. Arbitrary other completions at these same
columns, scalar upper rows, other anchors/columns/base/pairs, global
moments, representing measures and RS realization remain undecided.

## Mathlib

Full matching four-frozen-witness hull exclusion: not checked.
Supporting Farkas,convex combinations,singular Schur and unequal-layer
decomposition coverage: not checked here. Unknown coverage is not
absence. General inputs are imported by precise citation without a
novelty claim.
