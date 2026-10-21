# L064 — All anchors pass the fixed seven-distance four-index diagnostic

## Hypotheses

Let H be a 1024-point set and V its universe of 68-subsets. Use exactly
L021's rational primal a_i and L053's unchanged normalization

  U=binomial(1024,64)/binomial(68,64),
  rho=(U+1)/(2 binomial(1024,68))>0,
  p_0=1, p_1=...=p_4=0,
  p_i=a_i/(2 binomial(68,i)binomial(956,i)), 5<=i<=68.

In particular p5=1/68881143660, p6=133/9357995374380 and
p7=3539/248922676958508. The singleton and pair moments are rho and
rho*p_i. Use L056's complete, unchanged 21 coefficients z_rq,
v_rq=binomial(5,r)binomial(63,r)binomial(5,q)binomial(951,q),
and represented unordered triple moments rho*p5*z_rq/v_rq,
exactly as retained by audited L062. All moments and matrices are real.

Take D,E,F,G in V with half-distances

  (DE,DF,DG,EF,EG,FG)=(5,5,7,6,5,5).

At each A in {D,E,F,G}, consider the union matrix with indices {A}
and {A,B} for the other three supports. Boolean repetition uses the
lower-order coordinate. No new triple value, fourth-order moment,
retuned pair, label constraint, full PSD or measure is assumed.

## Conclusion

All four matrices are positive definite for every such quadruple.
There are exactly 110 feasible ordered sixteen-atom incidence vectors,
440 matrices and 6600 strictly positive exact principal minors. Every
matrix has an independently verified invertible congruence to a strictly
positive diagonal. There are no singular matrices or zero minors.

This parks exclusion by this pattern at this assignment only. E/F are
covered consistency controls; D/G test a distance-seven neighbor beyond
the retained five/six layers. This is local REPRODUCTION of assessed
moment and matrix tools, with no originality claim. Global moments/PSD,
other assignments or patterns, actual labels, representing measures,
packings and RS realization remain unresolved. The above-threshold
objective (U+1)/2 and the 955–957 bracket are unchanged. The separate
critical proof review below retains this finite conclusion.

## Proof

**Source imports and specialization.** Reuse the prior SPECIALIZE gate
`drafts/literature/2026-10-14-reanchored-seven-distance-principal.md`.
Import Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800;
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and its complete indicator proof,
printed p. 2. Its proof establishes A(n,d,w), retaining the qualification
to the displayed A(n,d) in foundations/12. At n=1024,d=10,w=68 and
order three, a singleton anchor allows exactly these index families:
|{A}|+2|I\{A}| is one or three. Every entry union contains at most
three supports, even though the matrix has four indices. The six
specified distances are at least ten in binary Hamming distance.
This is a necessary principal condition, without a completion theorem.
No hierarchy theorem is reproved. L053 supplies the support setting
and positive normalization, rather than its superseded trial triples.

Import A.E. Brouwer and W.H. Haemers, *Spectra of Graphs*, Springer,
2012, ISBN 978-1-4614-1938-9,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), printed p. 36, and Section 2.9 through Lemma 2.9.1
and its proof, p. 37. An invertible congruence to a strictly positive
diagonal proves real positive definiteness. No singular inverse is used.
The finite substitutions below are the identified difference from the
imported theorem; neither theorem is reproved.

**Complete removed/added enumeration.** Write
E=(D\X_E) union Y_E, F=(D\X_F) union Y_F and
G=(D\X_G) union Y_G. The removed sets lie inside D and the added
sets outside D, both with sizes (5,5,7). Write a,b,c for the three
removed pair intersections EF,EG,FG and h for their triple intersection.
The added pair intersections must be

  (A,B,C)=(4-a,7-b,7-c),

since the half-distance between two supports is the sum of the two
removed sizes minus the removed and added pair intersections. Let H'
be the added triple intersection. All feasible parameters are exactly

  0<=a<=4, 2<=b,c<=5,
  max(0,a+b-5,a+c-5,b+c-7)<=h<=min(a,b,c),
  max(0,A+B-5,A+C-5,B+C-7)<=H'<=min(A,B,C).

For three sets of sizes (u,v,w), pair intersections (l,m,n), triple
intersection t and part capacity K, their eight exact membership atoms
in mask order 0,...,7 are

  K-u-v-w+l+m+n-t, u-l-m+t, v-l-n+t, l-t,
  w-m-n+t, m-t, n-t, t.

Nonnegativity of the six nontrivial private/pair-only atoms gives the
displayed bounds on h and H'; pair intersections with a size-five set
are in [0,5], giving the bounds on a,b,c from both parts. The atom for
absence from all three sets is automatically nonnegative: each union
has size at most 17, below both capacities 68 and 956. Conversely every
allowed parameter gives disjoint nonnegative regions and hence sets
with exactly those sizes and intersections on both disjoint parts.

With D,E,F,G as bits 0,1,2,3, removed-mask s contributes its atom to
mask 1+2*(7 xor s), while added-mask s contributes to mask 2*s.
This retains all sixteen atoms, including outside and common-four.
Parameters are recovered from the atoms, so the enumeration is injective
and every specified quadruple is covered. Summing the two explicit
inclusive h,H' range lengths over a,b,c gives 110 atom vectors.

For an independent exhaustive parameterization set f(empty)=1024,
f(singleton)=68 and f(pair)=68 minus its specified half-distance.
The only free intersections are the four triples and the common four:

  58<=|DEF|<=62, 58<=|DEG|,|DFG|<=61,
  58<=|EFG|<=62, 51<=|DEFG|<=61.

For each triple, two pair intersections of sizes s,t inside a 68-set
have intersection at least s+t-68; take the greatest of these bounds.
Containment in each pair gives its upper bound. Removing 5+5+7 points
from D gives the intentionally loose common-four lower bound 51;
containment in DG gives upper bound 61. Thus these boxes include every
case. Boolean-lattice inversion gives each exact atom

  n_S=sum_(T superset S) (-1)^(|T|-|S|) f(T).

Retain precisely the box vectors with all sixteen n_S nonnegative.
Conversely these atoms reconstruct every specified intersection by
f(S)=sum_(T superset S) n_T, so they give valid supports. The verifier
checks every one of these inverse identities. This independent
enumeration yields exactly the same 110 atom vectors, with no duplicates.
Both enumerations are finite complete constructions, rather than samples.

Any quadruple with the same atom vector admits a bijection of H between
corresponding regions. The present fixed dictionary depends only on pair
distances and complete triple regions, so this transports the matrices
being tested. No actual-label RS symmetry or labeled averaging follows.

**Represented moments and all anchors.** Define y1,y2,y3,y4 to be the
moments of DEF,DEG,DFG,EFG respectively divided by rho. Their unique
two-five shell anchors are D,E,F,G respectively. For each eligible order
(S,T,W), reconstruct the complete regions in L056's order as

  (5-r,r,r,63-r,5-q,q,q,951-q),
  r=63-|S intersection T intersection W|,
  q=|T\W|-r.

The triples DEF/EFG have r+q=6; DEG/DFG have r+q=7. The above
intersection boxes give respectively r in [1,5] and [2,5], so both
r,q are at most five and belong to the represented dictionary. Their
values are y=p5*z_rq/v_rq. All six presentations of every triple are
checked, including both orders at its eligible anchor. Canonical minimum
eight-atom tuples with support bits 4,2,1 agree with L062's existing
unordered keys and exactly the same rational moments. Distances alone
are never substituted for region data; no unrepresented triple is used.

In the order anchor, then the other supports in D,E,F,G order, the four
matrices divided by rho are exactly

  K_D=[1,p5,p5,p7; p5,p5,y1,y2; p5,y1,p5,y3; p7,y2,y3,p7],
  K_E=[1,p5,p6,p5; p5,p5,y1,y2; p6,y1,p6,y4; p5,y2,y4,p5],
  K_F=[1,p5,p6,p5; p5,p5,y1,y3; p6,y1,p6,y4; p5,y3,y4,p5],
  K_G=[1,p7,p5,p5; p7,p7,y2,y3; p5,y2,p5,y4; p5,y3,y4,p5].

Entries are unions of support families, rather than unions of point sets.
The Boolean diagonal stays p_i; in particular the actual p7 is retained.
A four-support moment never occurs. The E/F comparison with audited
L061 is a covered control, not an extra premise needed for these direct
certificates. L057 treats smaller matrices and L058 a different distance
pattern; L063 treats excluded-anchor coefficients on different layers.

**Exact certificates and independent verification.** Run from this notebook:

  `python3 scripts/finite-support/seven_distance_principals.py`

  `python3 scripts/finite-support/verify_seven_distance_principals.py`

The constructor reparses all 21 canonical L056 coefficients, comparing
them to its existing exact certificate. It regenerates all 69 original
pairs from L021's exact primal, checks them against the retained pair
vector and all L062 pairs through 12, and checks the same positive rho.
For every case it constructs all four supports, six distances, four
triples and all six presentations, and matches every unordered value
to the L062 dictionary. Every matrix entry is reconstructed from its
actual family union. All fifteen nonempty principal subsets are retained
per matrix; determinants are computed by the permutation expansion.
Quadratic-form elimination saves all four congruence columns and the
entire resulting diagonal matrix, permitting zero pivots only when the
remaining residual row is zero. All 3646 constructor checks pass.

The full constructor certificate is
`scripts/finite-support/seven-distance-principals-results.json`.
It records every atom, all triple presentations and moments, all 440
matrices, all 6600 minors and every complete congruence. All minors are
strictly positive; no negative or singular case occurs.

The verifier imports no constructor or other notebook routines. It uses
the independent intersection boxes and Möbius inversion, comparing the
complete atom sets. It marginalizes atoms by membership predicates,
without using the constructor's consecutive point representatives or
removed/added recipes. It independently recovers all weights, distances,
parameters, six triple presentations, canonical keys and L062 values.
For all four anchors it checks every family-union entry and all fifteen
saved principal subsets. Gaussian elimination with row swaps recomputes
every minor, independently of permutation expansion.

For every saved column matrix T and reconstructed K, the verifier checks
det(T)!=0 and all sixteen entries of T^t*K*T, including all off-diagonal
zeros and every pivot. It checks the determinant identity
det(K)*det(T)^2=product(pivots). All pivots are nonnegative, none is zero,
and all independently recomputed minors agree and are strictly positive.
Consequently if v is nonzero, v=T*w for a nonzero w, and
v^t*K*v=sum_i pivot_i*w_i^2>0. Positive rho proves positive definiteness
for the actual moment matrices. This uses complete exact identities,
not a saved success flag or a preview as proof.

All 19712 independent checks pass with no failures. Full reconstructed
evidence and input hashes are in
`scripts/finite-support/seven-distance-principals-verification.json`.
The full count and failure fields were inspected; the verifier consumes
every load-bearing case, value, minor and congruence. No input retuning,
mathematical inequality failure or certificate repair was required.

The exhaustive pass supplies negative evidence for exclusion by this
specified pattern only. It asserts no full conditioned PSD, global
moment consistency, representing measure, actual code/list or safety.
All earlier stops retain their hypotheses and evidence. The finite
substitution and independent reconstruction above were subjected to the
following separate critical proof review.

**Separate critical proof review — step 217, 2026-10-14.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-14-seven-distance-principal-critical-audit.md`.
The review retains the exact statement, coefficients and scope; no
mathematical repair was needed. This establishes an audited local input,
not a new result beyond the sources checked or a global feasibility claim.

The enumeration proof was checked in both directions. Each removed or
added intersection involves a five-set, so each of a,b,c,h,H' lies in
[0,5]. The added pair intersections remain (4-a,7-b,7-c). Enumerating
all 6^5=7776 tuples in this broader box and testing all sixteen atoms
gives exactly the manuscript's restricted ranges: for every tuple,
membership in those ranges is equivalent to nonnegative atoms. The
absence atoms impose no additional bound because both capacities exceed
the sum 17. Inverting the three-set intersection counts independently
recovers the two eight-atom vectors and the stated four-support bit
mapping. The parameters are recoverable from the atoms, so neither
duplicates nor lost cases can be concealed by the total count.

For the other enumeration, the lower bound for each triple is the
largest sum of two pair intersections through one support, minus 68;
the upper bound is the smallest pair intersection. These give exactly
the four stated triple boxes. The common-four box [51,61] follows by
the union bound on D's removed points and containment in DG. All 4400
intersection tuples are tested by Boolean inversion. Every surviving
tuple satisfies all sixteen inverse identities. Nonnegative integer
atoms summing to 1024 realize disjoint regions on H, proving the
converse independently of any matrix calculation. Both enumerations
and both saved certificates contain precisely the same 110 distinct
vectors. Fresh point representatives verify all four weights and six
distances in every case.

All 64 equations defining L021's imported unique primal witness are
checked directly from its binomial formula. The complete pair vector,
positive rho, and the three displayed p5,p6,p7 fractions agree with
the saved inputs. L056's 21 manuscript coefficients are parsed directly;
every eligible triple presentation recovers its full eight regions,
r,q, and the exact value p5*z_rq/v_rq. All six orders of all four
triples match both certificates and L062's existing canonical unordered
dictionary. In particular the unique eligible anchors are D,E,F,G for
DEF,DEG,DFG,EFG, respectively. The distance-six third pairs give
r+q=6, and the distance-seven third pairs give r+q=7. No value from
L053's superseded trial is used. L021,L053,L056,L062 remain the direct
inputs; L061 and the smaller/complemented tests are comparisons only.

The four displayed manuscript matrices are evaluated literally and
compared entry by entry with the Boolean family-union construction and
both complete certificates. In particular a diagonal indexed by {A,B}
is p_(AB), not its square, and every union has at most three supports.
Every principal index subset is checked, not just the fifteen-count
claim. Clearing row denominators and using fraction-free integer
Bareiss elimination, with exact division checked at each step,
independently recomputes all 6600 determinants. They match both saved
certificates and are strictly positive. This differs from both the
constructor's permutation expansion and the verifier's rational Gaussian
elimination.

Every saved congruence column is checked against the other certificate.
The column matrix is unit upper triangular, hence invertible; its
determinant is also recomputed exactly as one. All 7040 entries of the
440 matrices T^t*K*T are recomputed, including every off-diagonal zero
and all 1760 strictly positive pivots. Each agrees with both complete
saved diagonal matrices, and det(K)*det(T)^2 equals the pivot product.
The independently recovered minimum pivot divided by its original
diagonal entry is

  27625475054848896781093537463687948454691688988471986080716357013141
  /27625475055249965723398424209705243750297065581339564831687426240340 > 0.

Thus the congruence criterion applies to all four anchors in every
case, and multiplication by the checked positive rho preserves strict
definiteness. This ratio concerns elimination pivots, not eigenvalues.
The union-matrix and congruence source imports above suffice; no source
theorem was reproved. Region bijections transport only this explicitly
invariant assignment, not actual-label restrictions.

Run `python3 scripts/finite-support/critical_audit_seven_distance_principals.py`.
All 27552 additional exact checks pass with zero failures. The complete
new certificate, including every reconstructed atom vector, triple
value, matrix, minor and congruence result, is
`scripts/finite-support/seven-distance-principals-critical-audit.json`.
It consumes both earlier certificates in full for their mathematical
evidence and verifies their input hashes. Rerunning the original verifier
also gives all 19712 checks with zero failures. The full failure list,
counts and minimum-ratio value were inspected in addition to the full
programmatic evidence consumption. The separate review retains only
this fixed-pattern nonexclusion and preserves ATTEMPTS/046 and every
earlier stop. Larger matrices, global consistency, other assignments,
labels, measures, packings and RS realization remain unproved.

## Mathlib

Full matching fixed-coefficient all-anchor certificate or moment hierarchy:
not checked. Supporting finite-set, rational determinant, congruence and
PSD coverage: not checked. Unknown availability is not evidence of absence.
