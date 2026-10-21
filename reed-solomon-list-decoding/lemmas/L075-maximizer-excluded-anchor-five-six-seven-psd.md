# L075 — The unchanged maximizer passes the excluded-anchor five/six/seven matrix

## Hypotheses

Use n=1024,w=68,n-w=956,d=10. Retain L053's singleton

    rho=(binomial(1024,64)/binomial(68,64)+1)/(2 binomial(1024,68))>0

and L021's complete pair prescription

    p0=1, p1=...=p4=0,
    p_h=a_h/[2 binomial(68,h)binomial(956,h)] for 5<=h<=68.

The rational vector a is the unique solution of L021's 64 defining
equations. In particular p14 is retained as
2825730193896494219/198754391512280403438773149400, as in L074.
Fix a 68-subset D. Use exactly L074's assignment: all L062 old entries,
L065's original RREF column at L068/L072's exact
(u,v,w)=(0,v_dagger,w_star), and L073's 28 forced and 36 completed
seven/seven entries. All pairs, rho, parameters and entries are immutable.

Write Y(D,E,G)=x({D,E,G})/rho with Boolean repetitions evaluated using
the singleton/pair coordinates. On D and every E with half-distance
|D\E| in {5,6,7}, test the ordinary invariant source matrix

    K(E,G)=p_(|E\G|)-Y(D,E,G).

No global moments, measure, code, labeled restriction or RS realization
is assumed. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-16-maximizer-excluded-anchor-five-six-seven.md`.

## Conclusion

K is PSD. Its entire D row and column vanish; its complete three-shell
restriction is positive definite. All 64 source modes pass: 36 three-layer,
13 two-layer and 15 seven-only blocks. All their 306 principal minors
are strictly positive. There are 149 positive normalized elimination
pivots, with minimum exactly 1/2. These are elimination values, not
claimed eigenvalues of the enormous original matrix.

This is a finite REPRODUCTION/specialization of the assessed source
algebra. It parks exclusion by this fixed necessary matrix, preserving
L073/L074's same-assignment passes and L067/L071's distinct obstructions.
No source-level novelty, full SDP feasibility, uniform packing/list bound,
representing measure or common-center RS list is claimed. Other-anchor
matrices, unrepresented coefficients and global consistency remain open.
Arbitrary-center 67/68-agreement safety and the 955–957 bracket are
unchanged. The separate critical proof review below retains this result.

## Proof

**Imported source and specialization.** Import Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), and the
second affine matrix in III.B (64), printed pp.5–7. Cross-check Hyun
Kwang Kim and Phan Thanh Toan, *Improved Semidefinite Programming Bound
on Sizes of Codes*, [arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
14 December 2012, Remark 11 and III.B (31)–(35), especially (33), pp.8–9.
Their even d>=4 and d<2w<=n hypotheses hold: 10<136<=1024.
The block algebra evaluates arbitrary invariant real relation coefficients,
without a representing measure. Its coding application makes this affine
PSD constraint necessary; it does not make a finite pass sufficient for a
code. Foundations/04,09,12 retain the inspected qualifications. The
suspect complement prefactor in Schrijver (61) is unused.

For factor mode (a,b), layer l is present precisely when
l belongs to {a,...,68-a} intersect {b,...,956-b}. On layers 0,5,6,7
therefore 0<=a,b<=7; shell l is present iff max(a,b)<=l, and the anchor
is present only in mode (0,0). This gives the stated 36/13/15 split.
Every relevant binomial normalization is positive. These imported results
are not reproved; no inspected theorem supplies this assignment's verdict.

**All coefficients and the anchor.** For E=(D\X) union Y and
G=(D\U) union V put l=|X|=|Y|, m=|U|=|V|,
i=|X intersection U|, j=|Y intersection V|. The eight membership atoms,
with D,E,G carrying bits 4,2,1, are

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

All 0<=i,j<=min(l,m) occur. Bijections on these atoms prove orbit
exhaustion; there are 270 types with l<=m in {5,6,7}, and swapping
E,G supplies both directions of every rectangle. The third distance
is h=l+m-i-j, reaching 14. Use every original p_h, including p14.

For l,m<=6 import the immutable L062 coefficients. For l<7,m=7 use
L065's original column recipe with free coordinates f, recovered from
its augmented RREF by nonpivots (27,33,42)=(0,v_dagger,w_star).
Recover w_star=M03/(-M33) from L068's objective matrix, and
v_dagger=N02/(-N22) from L072's plane matrix. All original compatibility
equations are checked; the reconstructed 49 coordinates agree with L074.
For l=m=7 put r=7-i,q=7-j and retain

    Y_77(7,7)=p7;
    Y_77(7-r,7-q)=0                         if 1<=r+q<=4;
    Y_77(7-r,7-q)=Y_(r+q,7)(q,r)           if r+q in {5,6};
    Y_77(7-r,7-q)=p7*z_(r,q)/V_(r,q)       if r+q>=7,
    V_(r,q)=C(7,r)C(61,r)C(7,q)C(949,q)>0.

Here C denotes the ordinary binomial with zero outside its range.
The vector z is exactly L073's unique original-row solution, not a
new optimizer output. Re-solving its 35 stated mode equations and
z_(7,0)=0 by rational Gauss–Jordan elimination gives the same complete
vector as L073's independent verifier and L074. This also retains the
original positive valency scaling; z and f are not source moments.

For every type, reconstruct actual supports and all six presentations.
Their atom vectors, source indices (a',b',t,s), and
h=a'+b'-t-s agree with L074. Underlying unordered keys have one Y;
each presentation's affine value uses its own p_h-Y. Boolean cases
and every forbidden incident distance are checked separately. In
particular a zero Y caused by another incident pair does not erase p_h.

If E=D then Y(D,D,G)=p_m and |D\G|=m, so K(D,G)=0.
The seven layer cases (0,0),(0,5),(5,0),(0,6),(6,0),(0,7),(7,0)
exhaust this entire row and column. They are verified before deletion.
For E=G in shell l, K(E,E)=1-p_l, retained in every calculation.
There is no included-anchor elimination or p_l*p_m*J subtraction in K.

**Complete exact source certificate.** Define

    beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m,n-a)
      (-1)^(u-t) C(u,t) C(n-2a,u-a) C(n-a-u,l-u) C(n-a-u,m-u).

For each a,b in {0,...,7} let T_ab={l in {5,6,7}:max(a,b)<=l}.
Its entire shell source block is

    B_ab(l,m)=sum_(i,j=0)^min(l,m)
      beta(68,l,m,a,i)beta(956,l,m,b,j)[p_(l+m-i-j)-Y_lm(i,j)].

Every B_ab is symmetric. Its positive representation multiplicity is
(C(68,a)-C(68,a-1))*(C(956,b)-C(956,b-1)). The sum of these
multiplicities over modes containing each l equals C(68,l)C(956,l):
respectively 68643272053310642688, 114239565514722237093504,
and 137320620588104893159334400 for l=5,6,7. This checks dimension
exhaustion alongside the imported complete decomposition.

Evaluate every nonempty principal minor of every block by exact rational
determinants: 36*7+13*3+15=306 minors. All are strictly positive.
This proves each block positive definite, including all cases that could
have been singular. The entire shell restriction is therefore positive
definite by the source algebra. Restoring the proved zero anchor proves
K PSD. The 49 five/six principal restrictions agree entrywise with L063;
this overlap is a consistency check, not an inference about layer seven.

**Independent signed subset-action normalization.** Fix a seven-set
U inside an n-set, n in {68,956}. On layer l, intersection i with U has
weight W_l(i)=C(7,i)C(n-7,l-i)>0. Weighted Gram–Schmidt of
1,i,...,i^l gives monic h_l,a with positive squared norm N_l,a.
The relation |X intersection Z|=t, from layer m to l, has exact quotient

    Q_lm^t(i,j)=sum_x C(i,x)C(7-i,j-x)C(l-i,t-x)
                          C(n-7-l+i,m-j-t+x).

These four factors count Z in the four parts determined by X and U;
each row sums to C(l,t)C(n-l,m-t). Check every coordinate of
Q_lm^t h_m,a=gamma_lm,a(t)h_l,a, or zero for an absent mode a>l.
All 118 factor transition matrices and their full actions are retained.
For every present mode/direction the ratio gamma/beta is one positive
rational constant independent of t, including all zero-beta cases.

After tensoring the factors, direct actions A_lm of the actual affine
dictionary satisfy A_ll=B_ll/D_l, where
D_l=C(68-2a,l-a)C(956-2b,l-b)>0. Put
N_l=N_(68,l,a)N_(956,l,b). The actual bilinear matrix
W_lm=N_l*A_lm is symmetric. The script checks both rectangular signs,
their reciprocal products 1/(D_l*D_m), and the triangle identity
sigma56*sigma67=sigma57*sigma66 for each factor, where
sigma_lm=N_l,a*(gamma_lm/beta_lm). This establishes a single coherent
positive congruence across all three layers, not just pairwise squares.
Independently check every principal minor directly in W against

    det W[I,I] = det B[I,I] * product_(l in I)(N_l/D_l).

Every equality holds with positive multiplier. Thus direct subset counts
confirm all source signs, normalization and complete three-layer minors.
For consecutive leading determinants Delta_0=1,Delta_j of B, the
normalized elimination pivots are Delta_j/(Delta_(j-1)*D_(l_j)).
All 149 are positive; exact comparison gives their attained minimum 1/2.

**Full reproducible evidence and qualifications.** Run from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/maximizer_excluded_anchor.py

The script passes 6737 exact checks. The complete rational certificate is
`scripts/finite-support/maximizer-excluded-anchor-results.json`:
all input hashes, original pair-system checks, reconstructed parameters,
column and z, all 270 entries/1620 presentations, seven zero-anchor cases,
weighted bases, all 118 transitions and actions, all 64 complete source
and weighted blocks, every principal minor, 149 pivots and empty failures.
The original included-anchor blocks are recovered from Y by undoing
their own correction solely for overlap comparison; no such correction
enters the affine blocks. All load-bearing blocks and minors are fully
evaluated and compared by the script; the inspected summary is not their
proof. Use PYTHONINTMAXSTRDIGITS=0 with the shared JSON inspector.

The preserved `scripts/finite-support/maximizer-excluded-anchor-initial.json`
has one failed schema check: the saved final defining-row tag is `sign`,
where the first implementation expected `zero`. It already reconstructed
the same vector from the manuscript equations. Correcting the tag changes
no coefficient, block or mathematical verdict. The final run has no
failure. A first inspector invocation also encountered Python's integer
string limit; rerunning with the stated environment variable succeeded.

The source decomposition is an imported general theorem, and the distinct
beta/subset calculations are arithmetic validation within this attempt.
The separate critical proof review below retains this certificate. A finite
necessary-matrix pass supplies neither omitted matrices nor a measure or actual code.

**Separate critical proof review — step 262, 2026-10-16.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-16-maximizer-excluded-anchor-critical-audit.md`.
The review retains the exact theorem without changing any coefficient,
source convention or qualification. This establishes an independently
reviewed local input, not a new mathematical discovery beyond the sources.

The full manuscript and constructor were checked against the input
recipes and foundations/04,09,12. Import the cited Schrijver Theorem 1,
III.A (52)–(59) and III.B (64), with Kim–Toan (33) as cross-check.
Zero padding outside layers 0,5,6,7 and the source's complete orthogonal
decomposition justify restriction to every surviving source coordinate.
The positive binomial scalings are invertible. Modes with either index
above seven have no retained layer; mode (0,0) alone has layer zero.
The full-space conclusion follows from this theorem, not from a quotient
calculation or a dimension sum. No complement prefactor is used.

The new independent standard-library verifier imports no notebook code
and uses only exact rational arithmetic. It checks all 64 defining
L021 pair equations using the Eberlein finite sum, retains the original
factor two, rho and p14, and reconstructs L068/L072's exact parameters.
It recovers all 49 column coordinates from L065's original RREF,
substitutes every original compatibility equation, and verifies all 49
weighted kernel residuals including the anchor. The earlier proofs of
pair uniqueness, RREF/kernel exhaustion and the parameter recipes are
imports; their entire upstream proofs are not claimed reaudited here.

All 28 forced seven/seven entries are reconstructed first. For each of
the 64 modes the verifier recomputes the original included-anchor
completion row and right side from beta sums and the closed two-by-two
inverse/range formulas, covering positive, rank-one and zero old blocks.
It reads the 35 defining indices from L073's manuscript, adds e_28, and
solves the square system by reverse-column forward elimination and back
substitution. All 36 pivots are nonzero. Every resulting coordinate agrees
with both the original and independently verified z; all original mode
inequalities and signs pass. This use of the included-anchor correction
is confined to identifying the prescribed completion. It never enters K.

For each of the 270 types, build D,E,G from eight disjoint consecutive
point intervals of the specified atom sizes, independently of the
constructor's removed/added-set formulas. Every support has size 68.
All 1620 presentations are recounted point by point, and every saved
atom, order, source index, actual third pair, Y and affine value agrees.
All Boolean/forbidden cases, full unordered keys and source keys
(sorted distance triple,t-s) pass. Every represented scalar row is also
checked for the same assignment. All seven anchor records are exactly
zero before deletion; shell diagonals remain 1-p_l. Reanchoring preserves
Y but must still use that presentation's actual p_h in p_h-Y.

The monic polynomials are reconstructed by solving weighted normal
equations against powers of i, rather than using the constructor's
Gram–Schmidt recurrence. Every coefficient vector has leading coefficient
one; every lower-degree weighted inner product is zero. All saved basis
values and strictly positive norms agree. On each layer, every diagonal
relation action agrees with the imported Johnson eigenvalue for mode a.
In particular the adjacency eigenvalues (l-a)(n-l-a)-a are distinct for
0<=a<=l (successive differences n-2a are positive here); the six finite
distinctness checks pass. This identifies the monic vector's source mode,
not just an arbitrary polynomial label. Completeness in the full subset
space still comes from the imported decomposition.

Independently enumerate occupancies (u,v,w,z) in the four regions of
sizes i,7-i,l-i,n-7-l+i, with u+v+w+z=m. Each contributes its four
binomial product to relation t=u+w and output intersection j=u+v.
This counts every target subset once. All 118 transition matrices and
every coordinate of every saved action agree. Absent modes vanish.
Weighted projection determines each action scalar gamma. In both
rectangular directions, every nonzero gamma/beta is the same strictly
positive rational ratio over the relations; zero beta has zero action.
Relation by relation the weighted adjoint and reciprocal-product
identities hold. The complete triangle identities with reference layer
seven are checked in every present mode.

For a product mode put N_l=N_(68,l,a)N_(956,l,b) and let sigma be the
factor weighted ratio N_(n,l,a)*gamma/beta. Define

    c=N_7/D_7>0,
    s_l=sigma_(68,l,7,a)*sigma_(956,l,7,b)/c>0,  s_7=1.

The freshly reconstructed weighted affine block W satisfies, entrywise,

    W_lm=c*s_l*B_lm*s_m.

This is one coherent positive diagonal congruence for the whole block;
separate squared comparisons would not establish the rectangular signs.
The verifier compares every field of all 64 saved source/weighted blocks,
uses rational elimination (rather than Laplace expansion) for every
principal determinant, and checks all positive determinant multipliers.
All 306 minors are strictly positive, including all potential singular
cases, and all 149 normalized pivots are positive with minimum exactly
1/2. The 49 L063 principal restrictions agree entrywise. The 36/13/15
mode split and all three positive multiplicity sums agree. Independently,
for each l the diagonal-action trace equals S_l*(1-p_l), which checks
the Boolean diagonal against the complete multiplicity-weighted spectrum.

Run from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_maximizer_excluded_anchor.py

All 10113 exact checks pass. The full evidence is
`scripts/finite-support/maximizer-excluded-anchor-critical-audit.json`:
input hashes, original residuals and completion equations, reverse-order
basis pivots, entire reconstructed assignment and presentations, polynomial
coefficients, every transition/action, signed ratios and coherent scales,
all complete blocks/minors/pivots and the empty failure list. The full
summary and failure list were inspected with the shared JSON inspector;
the verifier consumed and compared every load-bearing array, not previews.
The initial certificate's sole `original_defining_rows` schema-tag failure
is preserved. Every non-summary/check/failure field in that initial file
is exactly equal to the final constructor certificate, so no mathematical
array changed in its repair.

ATTEMPTS/057 remains parked. The positive shell blocks and zero anchor
certify only this fixed excluded-anchor matrix, alongside the imported
L073/L074 same-assignment conclusions. Other anchors, unrepresented
moments, measures, packing/list realization and the 955–957 boundary
remain unresolved. Mathlib coverage remains as qualified below.

## Mathlib

Full matching finite certificate and constant-weight mixed-layer
Terwilliger theorem: not checked. Supporting finite-set, rational linear
algebra and positive-semidefinite coverage: not checked. Unknown
availability is not evidence of absence. The precise informal source
imports and complete rational evidence above are the inputs used.
