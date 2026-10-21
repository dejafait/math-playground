# L063 — The unchanged witness passes the complete complemented five/six-shell test

## Hypotheses

Use n=1024,w=68,v=956,d=10 and L053's positive singleton rho.
Use exactly L021/L053's fixed pairs: p_0=1, p_1=...=p_4=0 and
p_i=a_i/[2 binomial(68,i)binomial(956,i)] for 5<=i<=68, where
L021 specifies the complete rational a_i by its nonsingular system.
Fix any 68-subset D. Retain the support indices D and all
E=(D\X) union Y with |X|=|Y| in {5,6}.

Use exactly L056's five/five entries, L059's complete affine five/six
column at L060's unchanged minimizer, and L061's audited 28-coordinate
six/six completion. L062 supplies the audited represented scalar and
unordered-moment dictionary. Write y(D,E,G)=x({D,E,G})/rho with
Boolean repetitions evaluated by the pair/singleton coordinate.
No moment, pair, coefficient or optimization parameter may be retuned.

The tested matrix is the source's excluded-anchor invariant matrix

  K_(E,G)=p_(|E\G|)-y(D,E,G)

on these retained indices. This is a fixed ordinary unlabeled matrix;
global triple extensions, other anchors, actual-label restrictions,
measures, codes and RS lists are not hypotheses. The ready SPECIALIZE
assessment saved before invocation is
`drafts/literature/2026-10-14-complemented-five-six-shell.md`.

## Conclusion

K is PSD. Its entire D row is zero; its restriction to both complete
shells is positive definite. All 49 complete source blocks pass:
36 shared two-layer blocks and 13 six-only blocks. The independent
subset-action reconstruction gives 85 positive normalized elimination
pivots, all at least 1/2, with minimum exactly 1/2.

This parks exclusion by this fixed complemented constraint, preserving
the unchanged included-anchor and represented scalar passes. It is a
finite REPRODUCTION of the assessed source algebra, not an original
general theorem or progress beyond the checked literature claimed as
new mathematics. No larger SDP feasibility, support cap, measure,
packing or common-center RS list follows. Arbitrary-center safety at
67/68 agreements remains open and the 955–957 bracket is unchanged.
The separate critical proof review below retains this finite application.

## Proof

**Imported source theorem and applicability.** Import Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE Trans. Inform. Theory 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (64), printed p. 7, specifically its second affine PSD matrix.
Cross-check Hyun Kwang Kim and Phan Thanh Toan, *Improved Semidefinite
Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
14 December 2012, III.B (33), printed p. 9, with normalization (31).
Their code hypotheses even d>=4 and d<2w<=n hold since 10<136<=1024.
This constraint is necessary for ordinary nonempty binary
constant-weight codes; no RS or field hypothesis is part of it.
Here we evaluate a prescribed matrix, without assuming a code exists.

Import Schrijver (7), Proposition 5 (44)–(47), Theorem 1 (51),
III.A (52)–(59), printed pp. 2,5–7, for the complete mixed-layer
block algebra. Foundations/04 and 09 retain the inspected theorem,
hypotheses and proof cases. The algebra applies to any invariant
relation coefficients, including affine differences without a measure.
For factor sizes 68,956, source mode (a,b) retains layer l exactly
when l lies in {a,...,68-a} intersect {b,...,956-b}.
Selecting layers {0,5,6} therefore gives precisely a,b<=6, with layer
5 iff a,b<=5, layer 6 always, and layer 0 only in mode (0,0).
All positive rescalings in the source formula are within their ranges.
No general source theorem is reproved; the finite evaluation below is
necessary because no inspected source supplies this assignment's verdict.
Schrijver (61)'s suspect complement prefactor is unused.

**Exact dictionary and zero anchor.** Put l=|D\E|, m=|D\G|,
i=|(D\E) intersection (D\G)| and
j=|(E\D) intersection (G\D)|. In mask order 0,...,7,
with D,E,G having bits 4,2,1, the complete atom vector is

  (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

For l,m in {5,6}, every 0<=i,j<=min(l,m) occurs. Atom bijections
give exactly these stabilizer orbits; thus 36 five/five, 36 five/six
and 49 six/six types exhaust the entries. Swapping E,G supplies the
whole six/five rectangle. In particular h=|E\G|=l+m-i-j ranges
through 12; no p_10,p_11 or p_12 is omitted.

For the established d5,t,d6 of L056,L059,L060,L061 the fixed y is

  y55(i,j)=p5*d5_(5-i,5-j),
  y56(i,j)=p5*t_(i,j),
  y66(i,j)=p6*d6_(6-i,6-j).

L056 specifies all 21 nonzero-allowed z5 values and
d5_(r,q)=z5_(r,q)/[binomial(5,r)binomial(63,r)
binomial(5,q)binomial(951,q)], with d5_(0,0)=1 and the remaining
coefficients zero. L059 gives t as the complete affine column at
s_*=-B0/(2A), with A,B0 from L060. L061 specifies all 28 z6
values by its unique 26-by-26 rational system and z_21=z_22=0;
d6_(r,q)=z6_(r,q)/[binomial(6,r)binomial(62,r)
binomial(6,q)binomial(950,q)] for r+q>=6. Its other entries are
d6_(0,0)=1, zeros for 1<=r+q<=4, and
d6_(r,5-r)=(p5/p6)*t_(5-r,r). These recipes fix every rational
entry; no feasible point is chosen during this test.

L062 proves that the source y equals the union moment divided by rho,
rather than d5 or d6. For all six orders reconstruct every atom and
(a,b,t,s), with h=a+b-t-s. Complete checks compare the same y and
source permutation equalities preserving t-s. The affine coefficient
in each ordered presentation is its own third-pair p_h minus this y;
it need not be the same coefficient after changing the anchor.
The underlying unordered moment must, and does, remain the same.

If E=D, then h=m and y=p_m, so K_(D,G)=0; the same holds if G=D.
When all three coincide p_0-y=1-1=0. Thus all five layer cases
(0,0),(0,5),(5,0),(0,6),(6,0) vanish identically. Removing this
verified zero coordinate is legitimate. When E=G lies in layer l,
K_(E,E)=1-p_l; this is positive and is retained. If the E,G distance
is forbidden, both p_h and y vanish. If a different incident pair is
forbidden after reanchoring, y=0 alone does not force p_h=0.
All such presentations are evaluated without changing this rule.
No positive-anchor elimination or p_l*p_m*J subtraction is used in K.

**Complete rational block test.** Define the source integer

  beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m) (-1)^(u-t)
    binomial(u,t)binomial(n-2a,u-a)
    binomial(n-a-u,l-u)binomial(n-a-u,m-u),

with binomials zero outside their ordinary range. For each 0<=a,b<=6
let T_ab={l in {5,6}:a,b<=l}. The entire retained source block is

  B_ab(l,m)=sum_(i,j=0)^min(l,m)
    beta(68,l,m,a,i)beta(956,l,m,b,j)
    [p_(l+m-i-j)-y_lm(i,j)],  l,m in T_ab.

The sums run over all admissible intersections. Its anchor coordinate
at (0,0) is exactly the zero coordinate proved above. Every surviving
binomial scale D_l=binomial(68-2a,l-a)binomial(956-2b,l-b) is positive.
The source theorem supplies complete-space exhaustion with multiplicity

  (binomial(68,a)-binomial(68,a-1))
  *(binomial(956,b)-binomial(956,b-1))>0.

Their sums recover the exact dimensions
binomial(68,l)binomial(956,l) on both layers. This dimension check
supplements the imported full decomposition; it does not replace it.

Exact substitution at the fixed rational inputs gives, in every shared
mode, B55>0, B66>0 and B55*B66-B56^2>0. In every six-only mode
B66>0. These are all principal minors of these one- and two-dimensional
blocks. They therefore prove positive definiteness of every shell
block, and the source algebra proves positive definiteness of the
whole two-shell restriction. Adding the verified zero anchor gives PSD.
The full evaluated fractions of all 49 blocks and all 121 diagonal
and determinant minors are in the certificate below, consumed in full
by the independent verification.

**Independent subset-action normalization and signs.** To verify the
rectangles without depending only on the beta implementation, fix a
six-set U in an n-set, n in {68,956}. A layer-l subset X has type
i=|X intersection U| with weight W_l(i)=binomial(6,i)binomial(n-6,l-i).
The relation |X intersection Y|=t from layer m to l has quotient

  Q_lm^t(i,j)=sum_x binomial(i,x)binomial(6-i,j-x)
    binomial(l-i,t-x)binomial(n-6-l+i,m-j-t+x).

These four choices partition Y into X intersection U, U outside X,
X outside U and the complement of X union U; they count all Y exactly.
Each row sums to binomial(l,t)binomial(n-l,m-t). Weighted Gram–Schmidt
on 1,i,...,i^l yields monic h_l,a with positive norm N_l,a.
Every complete coordinate action Q_lm^t h_m,a is checked to be
gamma_lm,a(t) h_l,a for a<=l, and zero if a>l. For equal layers,
gamma is the imported Eberlein eigenvalue, identifying the modes.
For unequal layers the action/beta ratio is one positive rational
number throughout each mode, including zero-beta annihilation cases.
This checks signs as well as normalization, before summing relations.
The full source decomposition supplies mode exhaustion beyond this
quotient calculation.

Tensor the two factor actions and sum the actual affine coefficients
to obtain A_lm in each mode. Put N_l=N_(68,l,a)*N_(956,l,b).
The verification checks A_ll=B_ll/D_l,
N5*A56=N6*A65, and A56*A65=B56^2/(D5*D6), together with the
positive signed rectangular action/beta ratio. Thus the actual symmetric
bilinear matrix is (N_l*A_lm)_(l,m). In shared modes its normalized
elimination pivots are

  B55/D5, (B66-B56^2/B55)/D6;

in six-only modes the pivot is B66/D6. Complete exact substitution
gives 85 positive pivots, with minimum 1/2. Hence the independent
actions confirm every source sign and singular-anchor qualification.
These pivots are normalized elimination values, not asserted
eigenvalues of the original enormous matrix.

**Reproducible full evidence.** Run from the active notebook:

  `python3 scripts/finite-support/complemented_five_six_shell.py`

It checks all 726 actual support presentations, all lower-order cases,
the five zero-anchor cases, the complete rectangles, all source blocks
and the unchanged included-block overlap. In that last comparison it
undoes the old included-anchor correction only to reconstruct y;
the complemented blocks themselves receive no Schur subtraction.
All 2445 reconstruction checks pass. The complete rational dictionary,
pair and y blocks, affine blocks, minors, hashes and failures are in
`scripts/finite-support/complemented-five-six-shell-results.json`.

Then run
`python3 scripts/finite-support/verify_complemented_five_six_shell.py`.
It imports no constructor or optimizer. It substitutes the full L021
pair vector into all 64 defining equations, regenerates p_0,...,p_12,
extracts L056's manuscript coefficients and L060's quadratic, rebuilds
all 36 affine column entries from L059's complete input and compares all
28 z6 coordinates with the audited unchanged witness. It independently
bit-permutes all full atom vectors and compares every affine presentation.
It counts all subset-transition relations directly, verifies complete
weighted actions and signed rectangular normalization, and compares all
source diagonal and determinant minors, including all 85 pivots.
All 2814 checks pass; the full fractions, weighted bases/actions, source
blocks, pivots and failure list are in
`scripts/finite-support/complemented-five-six-shell-verification.json`.
The full summaries and empty failure lists were inspected; all
load-bearing entries are consumed by verification, not established from
a bounded preview. A preliminary verifier schema mismatch on the audited
witness list was corrected before either verification conclusion; it
changed no mathematical input.

The outcome is nonexclusion only. This does not evaluate omitted source
blocks or other assignments, transport labeled constraints by averaging,
construct global moments or infer a representing measure. The unchanged
above-threshold objective is not an actual list. ATTEMPTS/015,038,043,044
remain distinct valid stops; the present test parks one additional
necessary constraint at exactly this witness.

**Separate critical proof review — step 213, 2026-10-14.** Reuse the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-14-complemented-five-six-shell-critical-audit.md`.
This audit retains the statement without retuning or mathematical repair.
It verifies a local reproduction, without a claim of originality.

The source applicability is precisely Schrijver III.A (57)–(59)'s
complete layer decomposition and III.B (64)'s second affine matrix,
with the independent Kim–Toan (33) comparison recorded above. Principal
restriction selects layer 0 only in mode (0,0), layer 5 in the 36 modes
a,b<=5 and layer 6 in all 49 modes a,b<=6. Equivalently, pad all other
layer coefficients with zero in the full algebra, apply its complete
orthogonal decomposition, and discard the zero coordinates. Positivity
of the retained original matrix is equivalent to positivity in every
retained source block. The source's positive diagonal scales are
invertible on these layers. This is the exhaustion justification;
neither the small stabilizer quotient nor its dimension count alone
would license the conclusion. Every multiplicity is positive.

The audit builds D,E,G from eight disjoint consecutive point intervals
of the stated sizes, independently of the constructor's set formulas.
It counts actual membership and set differences in all six orders,
compares every field of all 726 saved affine presentations and every
one of the 121 independent reconstructed entries, and checks their
identity with the audited L062 moments. Grouping by
(sorted(a,b,h),t-s) checks all represented source equalities. The
12 Boolean and 228 forbidden presentations retain their exact values.
All five anchor records are compared, including (0,0): p_h-y=0
before deletion. In contrast, shell diagonals remain 1-p_l. Reanchoring
does not replace the actual third pair by the original anchor distance.

The complete saved polynomial bases are verified, not assumed: on
i=0,...,l, the a-th forward difference is the constant a!, establishing
the monic degree-a polynomial; every weighted inner product against
an earlier basis vector vanishes, and every squared norm is positive
and equals its saved value. These conditions uniquely identify the
monic orthogonal basis for the strictly positive weights W_l(i).
Independently enumerate the occupancies (u,v,w,z) of Y in the four
regions X intersection U, U outside X, X outside U, and their
complement. They have sizes i,6-i,l-i,n-6-l+i and satisfy
u+v+w+z=m. Their contribution is

  binomial(i,u)binomial(6-i,v)binomial(l-i,w)
  binomial(n-6-l+i,z),

to quotient entry j=u+v of relation t=u+w. This exhausts every Y
once and reproduces all four layer directions. Projection by the
weighted inner product computes each action scalar; every coordinate
of the action is then checked, including annihilation of absent modes.
For each factor, mode and direction separately, the ratio to nonzero
beta coefficients is a single positive number, and zero beta gives
zero action. Thus neither a squared comparison nor cancellation of
two incorrect factor signs can conceal a rectangular sign error.
Both directional adjoint identities are verified relation by relation.

The audit sums these freshly checked actions against p_h-y. It also
independently reconstructs all pair, y and affine source blocks, then
compares every field of the constructor's 49 blocks and the verifier's
49 weighted-action blocks. The y blocks agree with the included-anchor
certificate after undoing that certificate's own constant correction;
no correction is applied to the complemented matrix. All 28 six/six
coordinates agree across the audited input certificates, and all saved
input hashes agree. The rerun independent verifier reconstructs the
complete L021 pair recipe, L056 coefficients and L059/L060 minimizer,
so unchanged witness identity is checked before the signs.

For each shared mode, the actual bilinear form is symmetric with
positive first pivot N5*B55/D5 and second pivot
N6*(B66-B56^2/B55)/D6. Each six-only mode has positive value N6*B66/D6.
All 121 source principal minors are strictly positive and all 85
normalized pivots are strictly positive, with exact minimum 1/2.
In addition to both dimension identities, the complete reconstructed
diagonal actions satisfy

  sum_(a,b admissible at l) m_(a,b)*A_ll
    =binomial(68,l)binomial(956,l)*(1-p_l),  l=5,6,

as required by the original Boolean diagonal. These trace checks
supplement the complete decomposition and sign checks.

Run `python3 scripts/finite-support/verify_complemented_five_six_shell.py`,
then `python3 scripts/finite-support/critical_audit_complemented_five_six_shell.py`.
All 2814 substitution checks and 4080 additional critical checks pass.
The latter imports no notebook program or optimizer and writes the full
presentations, quotient transitions, factor actions, signed ratios,
weighted blocks, identical witness, dimensions, traces and failure list
to `scripts/finite-support/complemented-five-six-shell-critical-audit.json`.
The complete summary and empty failure list were inspected. Every
load-bearing entry and block of the original two certificates is consumed
and compared, rather than inferred from a preview. No proof defect was
found. The zero anchor and positive definite shell restriction establish
exactly the stated PSD verdict. Global moments/PSD, omitted constraints,
other assignments, labels, measures, packings and RS realization remain
unresolved, with the 955–957 boundary unchanged.

## Mathlib

Full matching complemented finite certificate, constant-weight mixed-layer
Terwilliger reduction and prescribed normalization: not checked.
Supporting exact rational, finite-subset, block PSD and congruence
coverage: not checked. Unknown availability is not evidence of absence.
