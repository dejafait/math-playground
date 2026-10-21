# L057 — L056's represented triples pass every reanchored small principal

## Hypotheses

Use L053's ground set H of size 1024, its universe V of 68-subsets,
positive singleton moment rho, and unchanged pair moments rho*p_i.
Thus p_0=1, p_1=...=p_4=0 and p_5=1/68881143660.
Use exactly audited L056's 21 rational z_rq values, with

  v_rq=binomial(5,r)binomial(63,r)binomial(5,q)binomial(951,q),
  d_rq=z_rq/v_rq, for 0<=r,q<=5 and r+q>=5.

The represented triples have two distance-five pairs sharing one
support. Their full eight regions are L054's

  5-r, r, r, 63-r, 5-q, q, q, 951-q.

Distinct represented triples have normalized moment y=x({A,B,C})/rho
equal to p_5*d_rq when r+q>=5, and zero when 1<=r+q<=4.
At (0,0), the two nonanchor supports coincide and the normalized
moment is p_5. L056 establishes consistency under all represented
unordered-orbit identifications. Boolean repetitions elsewhere retain
the lower-order coordinate. All moments and matrices are real.
No unrepresented distinct triple value, actual-label zero, larger PSD
matrix or global moment extension is assumed.

## Conclusion

For every represented triple, each of its three supports D as anchor,
and both orders of the other supports E,F, the union matrix with indices
{D}, {D,E}, {D,F}, after removing duplicate indices, is PSD.
The Boolean lower-order closure also passes, including three equal
supports and repeated pairs at every represented pair half-distance
0,...,10. Thus L056's fixed witness survives this necessary small
principal test, including anchors with a neighbor outside distance five.

This parks only this fixed-witness exclusion diagnostic. Larger
other-anchor/cross-shell PSD, unrepresented triple completion,
actual-label restrictions, the full SDP value, a useful uniform bound,
representing measures and RS realization remain unresolved. It neither
proves an unsafe list nor changes the 955–957 boundary. This is local
REPRODUCTION of assessed moment methods, without a novelty claim.
The separate critical proof audit below retains this conclusion.

## Proof

**Imported necessary condition.** Reuse the unchanged SPECIALIZE gate
`drafts/literature/2026-10-12-released-zero-reanchored-principals.md`.
Import Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 (1)–(3), Proposition 1.1 and complete proof, printed p. 2.
Its indicator proof supplies the constant-weight union-matrix condition
with the displayed A(n,d) endpoint qualified as in
[foundations/12](../foundations/12-global-degree-three-moment-source.md).
At order three every singleton anchor permits these indices. L053
already justifies the support specialization for arbitrary received
arrays and every tuple width. We apply the known condition to a fixed
partial assignment; no hierarchy result is reproved or full feasible
point asserted.

Import the real symmetric Schur congruence from Brouwer–Haemers,
*Spectra of Graphs*, Springer (2012),
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), printed p. 36, and its PSD quadratic-form criterion,
Lemma 2.9.1, p. 37. Only the leading positive scalar is inverted.
No invertibility or strict positivity of the residual matrix is needed.

**Exhaustive finite scope.** Construct disjoint membership atoms with
the eight specified sizes and choose consecutive distinct point labels
in each atom, obtaining three complete 68-subsets of H. The sizes are
nonnegative for all 36 r,q and sum to 1024. Conversely any represented
triple has these atom sizes. Bijections within corresponding atoms carry
it to this representative and preserve all moments in this fixed
assignment. This concerns the specified coefficients only, without
averaging labeled RS constraints. There are no other represented
relations or hidden point-capacity restrictions.

For each representative, explicitly permute all six orders (D,E,F)
and regenerate all regions and pair distances by full set operations.
If i=|D\E|, j=|D\F|, h=|E\F|, then, for distinct supports,
the normalized matrix is exactly

  K=[1,p_i,p_j; p_i,p_i,y; p_j,y,p_j].

These entries follow by taking unions of families of supports, rather
than unions of their ground-set points. The triple value y remains
unchanged by reanchoring, by L056's unordered consistency. Its distance
multiset is (5,5,r+q); when r+q is not five, a different anchor has
one neighbor at half-distance r+q. The calculation uses the actual p_h
there, never p_5 in its place.

The (0,0) relation has two distinct supports; duplicate family-indices
are removed. Every order then gives [1,p_5; p_5,p_5]. For the Boolean
lower-order closure, the represented pair distances exhaust 0,...,10:
all r+q occur, as well as the two distance-five pairs. At a positive
distance b each of the three placements of the repeated support gives
[1,p_b; p_b,p_b]. At distance zero all three supports are equal and
the sole matrix is [1]. No distinct-triple recipe is used in these cases.

**Complete exact signs, including singular cases.** The seven principal
minors of K, with a=p_i, b=p_j, c=y, are

  1, a, b, a(1-a), b(1-b), ab-c^2,
  a(1-a)b(1-b)-(c-ab)^2.

The last expression is the determinant after the imported leading-one
Schur congruence; the residual matrix has diagonal a(1-a), b(1-b)
and off-diagonal c-ab. Nonnegative diagonals and determinant imply PSD:
if its first diagonal is positive, completing a square leaves a
nonnegative second coefficient; if it is zero, the determinant forces
c-ab=0 and the remaining diagonal is nonnegative. This explicitly
includes singular cases. For a Boolean two-index matrix, all minors
are 1,p_b,p_b(1-p_b), which are nonnegative. For [1] the sole minor is 1.
The actual matrix is rho times the normalized one, so every size-s
minor is multiplied by rho^s>0.

The constructor parses all 21 z values directly from L056's manuscript,
compares each to its saved exact vector, reconstructs all 69 p_i from
L053's imported L021 primal by
p_i=a_i/(2 binomial(68,i)binomial(956,i)) for i>=5, and checks complete
agreement with the unchanged L053/L056 pair inputs. All 21 free-relation valencies
used for normalization are checked against the displayed binomial product. It constructs actual membership
sets, all six orders and Boolean family-unions; it computes every minor
using the determinant permutation formula and checks every sign.
It also compares each 3x3 determinant with its Schur determinant and
checks full-region equality, orbit distinctness and eligible-anchor
consistency. All 1170 input/reconstruction checks pass.

The complete exact certificate is
`scripts/finite-support/released-zero-reanchored-results.json`.
Its 36 records cover 216 ordered matrices: 210 distinct-support
matrices and six Boolean matrices. All 1488 principal minors are
nonnegative; 224 are zero. The Boolean closure adds 31 matrices and
91 nonnegative minors. No negative minor or reconstruction error occurs.
All matrix entries, permuted regions, Schur matrices and rational minor
values are saved, including zero values and empty failure lists.

An arithmetic verifier imports no constructor or notebook module.
It reparses the complete canonical z vector and reconstructs all p_i,
rho, valencies and y. From the original pair distances (5,5,r+q) it
regenerates every permuted distance and matrix, checking every stored
entry. It uses the seven closed formulas above, rather than the
constructor's determinant algorithm, to compare every serialized
minor value and sign and check complete minor-subset coverage. All
1579 minors, including the full Boolean closure, are checked. Its 5435
checks pass with no failures. Full evidence and the source-certificate
hash are in `scripts/finite-support/released-zero-reanchored-verification.json`.
These complete rational substitutions supply the finite signs;
neither a preview nor a saved success flag is used as proof.

Reproduce from this notebook:

  `python3 scripts/finite-support/released_zero_reanchored.py`

then

  `python3 scripts/finite-support/verify_released_zero_reanchored.py`.

The necessary small matrices therefore all pass. The fixed objective
remains L053's above-threshold M, but no extension to omitted matrices
or actual-label constraints is supplied. Preserve L054/L055's different
restricted exclusions and L056's shell-only optimum. The separate critical
review below inspects the mathematical scope and complete evidence;
the arithmetic verifier alone is not that review.

**Separate critical proof review — step 188, 2026-10-12.** Reuse the
unchanged SPECIALIZE gate
`drafts/literature/2026-10-12-released-zero-reanchored-critical-audit.md`.
The conclusion and hypotheses are retained. This is a local verification
of the fixed certificate, not a theorem exceeding the assessed sources.

The source application uses real moments on the 68-subset universe.
For Polak's order-three singleton-conditioned matrix, the indices are
the singleton anchor and its unions with one additional support.
Thus the displayed family indices qualify; repeating a support repeats
an index, rather than creating another independent coordinate. Pair
moments are used whenever their family union has size two, including
the diagonal. The positive normalization is exactly
rho=(binomial(1024,64)/binomial(68,64)+1)/(2 binomial(1024,68)).
The imported Schur congruence uses only its normalized leading one;
neither a zero pair moment nor a singular residual block is inverted.

Exhaustiveness uses full regions, not just distances. In an ordering
with the two distance-five pairs incident to A, write B=(A\X) union Y
and C=(A\X') union Y', where all four sets have size five, the X sets
lie in A and the Y sets outside it. Then r=5-|X intersection X'| and
q=5-|Y intersection Y'| give exactly the eight displayed sizes. Both
ground parts contain at least ten points, so every r,q occurs. Any two
such partitions are related by a bijection on the 1024 points. The
prescribed moments depend only on these regions and pair distances, so
that bijection transports this particular matrix. It does not transport
actual-label RS restrictions. L056's audited unordered consistency
applies: if r+q=5 every support is an eligible shell anchor and all
pair-only sizes are r, all private sizes q; otherwise the eligible
anchor is unique. Common size 63-r, together with the distance multiset,
prevents cross-relation identifications. The repeated relation (0,0)
is handled by family unions. All six orders are retained even there.

The existing arithmetic verifier was inspected and rerun: all 5435
checks pass. A further independent reconstruction, importing no notebook
modules, is reproduced by

  `python3 scripts/finite-support/critical_audit_released_zero_reanchored.py`.

It reparses the complete canonical 21-entry vector and all 69 fixed pair
values, checks rho and the saved input hashes, and constructs supports
using removed/added five-sets instead of the constructor's membership
atoms. Explicit point membership reconstructs all eight regions for
all 216 orders. Every saved distance, family-index record, union-matrix
entry and Schur entry is compared exactly. Canonical full-region keys
check all cross-relation collisions and eligible reanchorings. The
Boolean audit reconstructs actual 68-subsets at every distance 0,...,10
and checks every repeated-support placement, including its multiplicity.

Every saved rational minor is recomputed by Gaussian elimination with
row swaps, independently of both the constructor's permutation formula
and the earlier verifier's closed formulas. Exact positive-pivot Schur
elimination also checks PSD directly: a zero pivot is accepted only
when its entire remaining row is zero. The full records contain every
matrix, minor, Schur complement and pivot, not just successful flags.
All 7254 additional checks pass, covering 216 represented matrices and
31 Boolean matrices, all 1579 minors and the complete original verifier
report. Evidence and input hashes are in
`scripts/finite-support/released-zero-reanchored-critical-audit-results.json`.

The singular cases are exhaustive. Among the represented matrices,
56 are singular, exactly those with a zero pair diagonal: there are
14 relations with 1<=r+q<=4, and four of the six orders put that pair
at the anchor. Their triple moment and corresponding row are zero.
The two orders anchored at the common distance-five neighbor are
nonsingular, as checked by the exact pivots. The Boolean closure adds
12 singular matrices, the three placements at each distance 1,...,4.
There are 224 zero represented minors and 24 additional zero Boolean
minors, for 248 total. No other pivot or minor vanishes in this finite
certificate. In every zero-pivot case the saved residual row is exactly
zero. Hence no positive-definiteness assumption hides a singular case.

All remaining matrices pass the same exact rational tests, using p_h
when reanchoring requires distance h rather than five. This independently
retains the finite nonexclusion verdict. The full source program,
larger coupled matrices, unrepresented triples, actual-label zeros,
measures and RS lists remain outside the conclusion. L053's fixed
objective is unchanged, so the 955–957 boundary is unchanged as well.

## Mathlib

The full matching fixed-coefficient certificate, union program and
Schur coverage are not checked in Mathlib. Supporting finite-set and
linear-algebra coverage is also not checked. Unknown availability is
not evidence of absence; the precise imports and full rational
verification above supply this result.
