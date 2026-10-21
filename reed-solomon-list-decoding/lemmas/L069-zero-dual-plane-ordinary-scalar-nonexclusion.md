# L069 — Ordinary scalar rows leave the zero-dual plane nonempty

## Hypotheses

Retain L053's original positive singleton normalization rho on all
68-subsets of a 1024-point set, L021's full rational pair prescription,
the entire L061 anchored five/six-shell base, and every unchanged L062
moment and ordinary scalar row. In particular

    p0=1, p1=...=p4=0,
    p_h=a_h/[2 binomial(68,h) binomial(956,h)]  (5<=h<=68).

Use exactly L065's coordinate order and affine kernel-compatible family

    f_j=c_j+u*a^27_j+v*a^33_j+w*a^42_j,  j=0,...,48.

Here c and the three a vectors are uniquely specified by L065's complete
49-equation system and its RREF; no coefficients are fitted anew. A free
conditional triple moment is y=p7*f_j. Fix w=w_star=beta/alpha, where
alpha=-M33>0 and beta=M03 in L068's exact objective matrix M. Retain
both real parameters u,v, all fixed entries, Boolean/forbidden rules,
complete unordered-key equalities and the entire retained-base kernel
condition. Add the ordinary scalar rows at all six presentations of
all 85 five/seven and six/seven types, using original pairs through p13.
No seven/seven completion variables or new/new scalar rows are included.

## Conclusion

This two-variable scalar-feasibility problem has the exact rational
solution u=v=0. Thus L068's attained zero survives all 1530 added rows,
with the same 47 positive free coordinates and two zeros at indices
27,33. Every old scalar row remains unchanged. For every new permitted
triple, the largest ratio y/min(p_a,p_b,p_h) is strictly below 10^(-9),
where (a,b,h) are its three half-distances; the required upper bound is 1.
The overall minimum new scalar slack is zero.

Consequently these ordinary scalar rows cannot repair strict exclusion
by L068's unchanged weighted dual. L067's immutable-point obstruction
is unaffected. This supplies neither a simultaneous PSD completion nor
global feasibility, a measure, packing or RS list. The 955–957 boundary
and arbitrary-center safety at 67/68 agreements remain unresolved.
This is a finite REPRODUCTION/specialization, without a novelty claim;
the separate critical proof audit below retains this conclusion.

## Proof

**Imported scalar theorem and specialization.** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-15-zero-dual-plane-ordinary-scalar-feasibility.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65) and the explanation following (65), printed p. 7.
Cross-check Hyun Kwang Kim and Phan Thanh Toan, *Improved Semidefinite
Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), 14 December 2012,
III.A Remark 11 and III.B (31)–(35), conditions (i)–(iv), printed pp. 8–9.
The hypotheses even d>=4 and d<2w<=n hold at d=10,w=68,n=1024.
The canonical source qualifications are in foundations/04. No general
scalar or SDP theorem is reproved. Neither source supplies a verdict for
these prescribed coefficients, so exact substitution is necessary.

Retain Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE TIT 65 (2019), 28–38,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and its indicator proof, p. 2, with the
constant-weight qualification recorded in foundations/12. This supplies
the union-index interpretation, without asserting a representing measure
or allowing actual-label averaging. L065 supplies the already justified
complete retained-base kernel condition for the whole affine family.

**Exact pair and normalization imports.** Independently substitute the
full saved vector (a5,...,a68) into all 64 defining L021 equations
Ax=1, using its specified coefficients; every residual is zero. Retain
L053's factor two in the pair definition. In particular

    a13=808753696404081487284494974858496/11,
    p13=26968792942808537/1896913598738625271419892200.

All pairs through thirteen satisfy 0<=p_h<=p5 for h>=1. The old pairs
through twelve agree exactly with L062. Put

    N=binomial(1024,68),
    U=binomial(1024,64)/binomial(68,64),
    M_list=(U+1)/2, rho=M_list/N>0.

The notation M_list distinguishes the list objective from L068's
four-by-four matrix M. For a presentation (a,b,t,s), its positive orbit
multiplicity is

    O=multinomial(68;t,a-t,b-t,68-a-b+t)
      *multinomial(956;s,a-s,b-s,956-a-b+s).

The invariant actual triple moment is rho*y. There are N*O ordered
ground-set triples in this orbit, so its source coefficient is
(N*O*rho*y)/(M_list*O)=y. Consequently the three source slacks are

    y, p_a-y, 1+y-p_a-p_b.

The normalization is checked coefficientwise on the entire affine plane,
not only at the witness. Repeated words in the inherited dictionary use
the corresponding pair moment. All new triples here are distinct.

**Exhaustion of the new rows and their equalities.** For l=5,6 and
0<=i,j<=l, use precisely the eight atoms, masks 0,...,7 with D,E,G
bits 4,2,1,

    (949-l+j,7-j,l-j,j,i,l-i,7-i,61-l+i).

They are nonnegative and give three 68-subsets; the half-distances are
l,7,l+7-i-j. These are the entire L065 column domain, not a selection
of its rows. At every one of the six support orders regenerate all eight
atoms and put

    a=atom4+atom5, b=atom4+atom6,
    t=atom4, s=atom3, h=atom2+atom6=a+b-t-s.

Each source orbit has O>0 and preserves t-s=i-j. All original pairs
through p13 are retained, including at anchors outside the PSD layers.
The complete canonical atom keys, minimized over six orders, partition
the 85 types into 20 represented, 16 forbidden and 49 free keys. Check
every key against the unchanged full L062 dictionary first. Forbidden
nonzero distances 1,...,4 require zero, consistently with any represented
lookup. Free keys occur in exactly L065's order. All cross-type shared
keys have identical affine values, so one common (u,v,w_star) suffices.
The source equalities also follow directly: (a,b,h) and t-s determine
t+s=a+b-h, hence t,s and every atom. Preserving t-s while permuting the
distance triple is therefore covered by the six presentations. Both the
complete-key identities and this source indexing test are checked.

As an independent realization check, take D={0,...,67}, U={0,...,6},
V={68,...,74}, X={0,...,i-1} union {7,...,7+l-i-1}, and
Y={68,...,68+j-1} union {75,...,75+l-j-1}. Then
E=(D minus X) union Y and G=(D minus U) union V. Count all 1024 points
at every support order; these produce exactly the above atoms and all
510 source presentations. No distance-only dictionary is used.

**Exact witness and all signs.** Restrict each free expression to the
plane as

    f_j=(c_j+w_star*a^42_j)+u*a^27_j+v*a^33_j.

L068's exact square matrix gives alpha>0,
alpha*M00+beta^2=0, with all rows/columns indexed 1,2 zero. Thus
Phi(u,v,w_star)=0 for all real u,v, in particular for u=v=0.
The complete four coefficient vectors satisfy every original L065
kernel equation; substituting the plane gives constant right side and
zero u,v coefficients in all 49 equations. At u=v=0 all 49 free entries
are nonnegative, precisely 27,33 are zero, and every fixed entry agrees
with its inherited lookup. The 49 original weighted whole-kernel
residuals also vanish directly, retaining the anchor p7 and the actual
86 orbit weights. No unweighted quotient inverse is used.

Direct rational substitution gives nonnegative slacks in all 85*6*3=1530
new rows. For a permitted triple, exact comparison gives

    0<=y/min(p_a,p_b,p_h)<=R<1/10^9<1,

where the exact rational maximum R is saved at `/maximum_upper_ratio`
in both certificates below. A maximizing type is (l,7,i,j)=(6,7,2,6).
Every forbidden triple has y=0. All supports are distinct and
p_a,p_b<=p5, so the lower slack is at least

    1-2*p5=34440571829/34440571830>0.

The scalar minimum zero comes from nonnegative/upper rows, including
forbidden zeros. All old 2178 source slacks are retained and checked
unchanged as well. An explicit point proves existence in the whole
two-variable domain; no exclusion of that domain is inferred from
checking only u=v=0.

**Complete reproducible arithmetic evidence.** Run from the notebook

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/zero_dual_plane_scalars.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_zero_dual_plane_scalars.py

The constructor passes 1621 checks. Its full certificate is
`scripts/finite-support/zero-dual-plane-scalars-results.json`, containing
pinned input hashes, original pairs through thirteen, the complete
two-variable inequalities, all 85 types/510 presentations, positive
orbit denominators, every evaluated slack, and all 49 witness entries.
There are no failures or violating rows.

The independent verifier imports no constructor, notebook implementation,
optimizer or floating arithmetic. It reconstructs L021's defining
coefficients by polynomial convolution, rather than the constructor's
coefficient formula; regenerates every pair and rho; obtains w_star
from the unchanged exact square matrix; reconstructs all plane entries,
old keys, new keys and source presentations; uses factorial multinomials
for orbit sizes; and checks every saved affine inequality, every sign,
all source equalities, all 2178 old rows and all 49 original weighted
whole-kernel residuals. Its 8526 checks pass without failures. Full
evidence is `scripts/finite-support/zero-dual-plane-scalars-verification.json`.
Its exact maximum ratio, full summary, failures, maximizing type, p13
and complete original-kernel residual list were inspected. The programs
consume every relevant row and coefficient; previews are not proof.

This witness stops only the proposed scalar repair of the unchanged
weighted dual. Independent mode inequalities, simultaneous completion,
global consistency, actual-label restrictions and RS realization remain
unresolved. Preserve ATTEMPTS/044,050 and L067's distinct fixed-point
obstruction. No full feasibility or boundary improvement follows.

**Separate critical proof review — step 238, 2026-10-15.** Reuse exactly
the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-zero-dual-plane-scalar-critical-audit.md`.
The audit retains the statement without a mathematical repair. This is
validation of the finite reproduction, not a new general theorem or a
boundary improvement. Foundations/04 and 12 supply the already inspected
source statements with their qualifications: positive orbit denominators,
Boolean union indices, equality preserving t-s, and ordinary unlabeled
constraints. The source parameters satisfy even d>=4 and d<2w<=n.
No complement prefactor, representing measure or labeled averaging is used.

The complete original verifier was rerun: all 8526 checks pass. A separate
standard-library audit imports no notebook implementation or optimizer.
It consumes both complete L069 certificates and the complete load-bearing
pair vector, L062 dictionary, L065 kernel/RREF/affine coordinates and
L068 objective matrix. These last three mathematical inputs are established
by their separate canonical audits; their entire ancestral proofs are not
claimed to be independently reproved here.

Reconstruct all 64 L021 equations by starting with the coefficient list
binomial(68-j,k)binomial(956-j,k) and multiplying by (1-Z) exactly j
times. Every residual is zero. All 64 a-values are positive; the original
factor-two pairs, displayed a13,p13, positive rho,p7 and old dictionary
through p12 agree. Reconstruct every coordinate of c and the three
directions from L065's RREF and its nonpivots 27,33,42. All 49 affine
vectors match the imported family. The complete symmetric matrix M
agrees with alpha>0, zero u,v rows/columns and
alpha*M00+beta^2=0. Thus w_star and every restricted affine coordinate
are the same ones used in L068, not a newly chosen approximate zero.
All 49 evaluated coordinates agree with both constructions: 47 positive,
with exactly indices 27,33 zero.

Independently enumerate the 121 old and 85 new types from their prescribed
integer ranges. For every type build actual sets D,E,G using the explicit
representatives above (with general m=5,6 for old types). Under every
support order compute the eight regions by set intersections and
differences. They are disjoint, exhaust 1024 points and reconstruct three
68-subsets. Their complete counts and direct source indices agree with
every saved presentation. Independently compute its orbit size as

    O=68!*956! / product_(eight atoms A) |A|!.

The denominator divides the numerator and O>0 in every case. This checks
the orbit count itself, in addition to the coefficientwise normalization
(N*O*rho*y)/(M_list*O)=y. All 1236 presentations are consumed, including
the 12 old Boolean and 228 old forbidden presentations. New supports
are distinct. Directly compare every saved old pair/slack and every new
affine scalar inequality with these reconstructed indices.

Canonical atom keys and the source identity (sorted(a,b,h),t-s) are
checked jointly across both complete domains. Since ordered (a,b,h)
and t-s uniquely determine t,s and all eight atoms, these checks cover
all source identifications, including shared old/new types. The 49 free
keys and their first-occurrence ordering agree exactly with L065; all
20 represented and 16 forbidden entries retain their values, with
forbidden zeros checked even when a key is represented. No extra
parameter equality or distance-only replacement is introduced.

Reconstruct all 86 positive orbit weights by the four-region binomial
formula; their two layer sums equal binomial(68,l)binomial(956,l).
Include anchor entry p7 with weight one. For each of the 49 original
kernel vectors, reconstruct the unscaled free coefficients
W_a*v_a*p7 and the fixed right side, then divide by the maximum absolute
free coefficient as in L065. All 49 original equations agree exactly.
Substitute all four affine coefficient columns before restricting w:
all 196 weighted coefficients vanish. The 49 point residuals also vanish
and match the original verifier. L065's justified finite averaging and
kernel exhaustion identify these weighted tests with the whole-base
kernel condition; quotient dimension alone is not used for this inference.

All 2178 inherited and 1530 new scalar slacks agree with both complete
certificates. Their minimum new slack is zero. The exact maximum ratio R
is unchanged and satisfies 0<=R<1/10^9<1. Its maximizing types are
(5,7,1,5) and (6,7,2,6), each at all six presentations. The manuscript
correctly named the latter as **a** maximizing type. An initial audit
assertion incorrectly required it to be the unique type; the only failed
check was `exact_extremum`. Preserve that full report at
`scripts/finite-support/zero-dual-plane-scalars-critical-audit-initial.json`.
Correcting the audit assertion to include both ties changes no witness,
slack, maximum, kernel identity or lemma statement.

Run `python3 scripts/finite-support/verify_zero_dual_plane_scalars.py` and
`python3 scripts/finite-support/critical_audit_zero_dual_plane_scalars.py`.
All 10073 additional audit checks pass. Complete reconstructed sets of
atom presentations, affine rows, original equations, weights, residuals
and exact extrema are saved in
`scripts/finite-support/zero-dual-plane-scalars-critical-audit.json`.
The full summary, empty failure list, exact ratio, all maximizing
presentations and all point residuals were inspected. The programs consume
every relevant rational array; bounded previews establish no identity.
This retains only the scalar nonexclusion. L067's immutable obstruction,
simultaneous seven/seven PSD, other duals, global constraints and RS
realization retain precisely their previous status.

## Mathlib

Full matching constant-weight scalar theorem, the complete inherited
affine-family kernel calculation and this finite exact certificate:
not checked in Mathlib. The cited primary scalar theorem and audited
local inputs supply the mathematics used here; unknown library coverage
is not evidence of absence.
