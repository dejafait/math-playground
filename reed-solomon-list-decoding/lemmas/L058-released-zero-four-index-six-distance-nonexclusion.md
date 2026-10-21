# L058 — The fixed mixed-shell four-index test passes exhaustively

## Hypotheses

Use L053's universe V of 68-subsets of a 1024-point ground set H,
positive singleton rho and unchanged pair moments rho*p_i. In particular

  p_5=1/68881143660, p_6=133/9357995374380,
  rho=(U+1)/(2*binomial(1024,68)), U=binomial(1024,64)/binomial(68,64).

Use exactly audited L056's 21 rational coefficients z_rq, its
v_rq=binomial(5,r)binomial(63,r)binomial(5,q)binomial(951,q),
and represented unordered triple moments rho*p_5*z_rq/v_rq.
The full eight-region convention is L054's. Moments and PSD are over
the reals. Take four supports D,E,F,G with half-distances

  (DE,DF,DG,EF,EG,FG)=(5,5,6,5,5,5).

Consider only the union matrix with indices {D},{D,E},{D,F},{D,G}.
No unrepresented triple coordinate, fourth-order moment, labeled zero,
other matrix PSD or representing measure is assumed.

## Conclusion

Every such four-index matrix under this fixed partial assignment is
positive definite. There are exactly 150 feasible ordered 16-region
atom vectors; all 2250 principal minors are strictly positive, and
each matrix has a complete exact invertible congruence to a positive
diagonal matrix. Thus this coupled diagnostic cannot reject L056's
prescription. Audited L057's smaller-principal pass is preserved.

This is local REPRODUCTION of assessed moment and matrix tools, with
no originality claim. The singleton objective remains (U+1)/2, above
the threshold. No full SDP feasibility, useful uniform bound, packing,
RS list, or improvement of 955<=t_star(m)<=957 follows. The separate critical
proof review below retains this finite specialization.

## Proof

**Precise source imports.** Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-12-released-zero-four-index-six-distance.md`.
Import Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and complete indicator proof, printed p. 2.
Its constant-weight conclusion is A(n,d,w), with the displayed A(n,d)
qualification retained in [foundations/12](../foundations/12-global-degree-three-moment-source.md).
At order three with singleton D, all four indices satisfy the index
condition; their entry unions have at most three supports. L053 supplies
the support specialization at (n,d,w)=(1024,10,68). Four indices do not
require order-four moments. No hierarchy theorem is reproved.

Import Brouwer–Haemers, *Spectra of Graphs*, Springer, 2012,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), printed p. 36, and Section 2.9 through Lemma 2.9.1
and proof, p. 37. Exact invertible congruence preserves the real
quadratic-form PSD criterion. The constructor accepts a zero pivot
only with a completely zero remaining residual row; the verifier
checks the full congruence and its invertibility. No singular block
inverse is used. This explains the certificate specialization rather
than reproving an imported matrix theorem.

**Exhaustive full-incidence parameterization.** Write

  E=(D\X_E) union Y_E, F=(D\X_F) union Y_F,
  G=(D\X_G) union Y_G,

where the removed sets lie in D, the added sets in H\D, and their
respective sizes are (5,5,6). Put

  a=|X_E intersection X_F|, b=|X_E intersection X_G|,
  c=|X_F intersection X_G|, h=|X_E intersection X_F intersection X_G|.

For two such supports the half-distance is the sum of their removed
sizes minus both removed and added pair intersections. Consequently
the added pair intersections are (A,B,C)=(5-a,6-b,6-c).
Put H'=|Y_E intersection Y_F intersection Y_G|. All possibilities
are exactly the following inclusive integer ranges:

  0<=a<=5, 1<=b,c<=5,
  max(0,a+b-5,a+c-5,b+c-6)<=h<=min(a,b,c),
  max(0,A+B-5,A+C-5,B+C-6)<=H'<=min(A,B,C).

Indeed for three sets of sizes (u,v,w), pair intersections (l,m,n)
and triple intersection t inside a part of size K, the eight atoms in
membership-mask order 0,1,2,3,4,5,6,7 have sizes

  K-u-v-w+l+m+n-t, u-l-m+t, v-l-n+t, l-t,
  w-m-n+t, m-t, n-t, t.

Their nonnegativity gives exactly the displayed triple bounds. The
outside atom is automatically nonnegative here: each side's union has
size at most 16, while its capacity is 68 or 956. Use this formula for
the removed sets with K=68,t=h and the added sets with K=956,t=H'.
With D,E,F,G as bits 0,1,2,3, removed-mask s contributes to atom
1+2*(7 xor s), and added-mask s contributes to atom 2*s. These are all
16 atoms, including the outside and the common-four atom. Distinct
parameter vectors give distinct atoms, and every specified support
configuration recovers these parameters. Thus no private, triple or
four-way region is omitted. The finite ranges have 150 feasible vectors.

Choose consecutive point labels in each atom. Any other four supports
with these same atom sizes are related by a point bijection. The fixed
assignment depends only on full represented triple regions and pair
distances, so this bijection preserves this particular matrix. It does
not transport actual-label RS restrictions or average a labeled point.

**Covered coordinates and matrix.** DEF has all three eligible shell
anchors; DEG has only E, and DFG only F. For any eligible anchor S and
the other two supports T,W, let r=63-|S intersection T intersection W|
and q=|T\W|-r. Direct set membership yields exactly L054's regions

  5-r, r, r, 63-r, 5-q, q, q, 951-q.

All resulting r,q are in L056's represented free relations. In DEF,
L056's unordered consistency makes the value independent of eligible
anchor. Denote the three normalized moments by y_DEF,y_DEG,y_DFG.
The matrix divided by rho is exactly

  K=[1,   p_5,   p_5,   p_6;
     p_5, p_5,   y_DEF, y_DEG;
     p_5, y_DEF, p_5,   y_DFG;
     p_6, y_DEG, y_DFG, p_6].

These are unions of families of supports, not point unions. Boolean
diagonals use the pair moments. EFG and DEFG never occur as entry
families. In particular p_6 is retained without replacement by p_5,
and L053's different trial triple formula is not substituted.

**Complete exact finite certificates.** Reproduce from this notebook:

  `python3 scripts/finite-support/released_zero_four_index.py`

  `python3 scripts/finite-support/verify_released_zero_four_index.py`

The constructor parses all 21 z values from canonical L056 and compares
them to its saved exact vector. It reconstructs all 69 pair values from
L021's saved primal using L053's normalization, compares them to the
unchanged L053/L056 inputs, and checks rho>0. Each of the 150 atom
vectors constructs complete sets; all six distances, eligible anchors,
full triple regions, unordered values and actual family-union entries
are checked. Every nonempty principal subset is retained: 15 minors
per matrix, computed by the determinant permutation formula. All 2250
are strictly positive. Exact quadratic-form elimination also saves
four rational congruence columns per matrix, the full resulting diagonal
matrix and its four strictly positive pivots. All 2405 constructor
checks pass without input or identity failures.

The full certificate, including every atom, triple coordinate, matrix,
minor and congruence, is
`scripts/finite-support/released-zero-four-index-results.json`.
There are no negative minors, singular matrices or zero minors.

The verifier imports no constructor or other notebook routines. Its
independent incidence parameterization uses the four triple-intersection
sizes and the common-four size. Their necessary inclusive ranges are

  58<=|DEF|<=63, 57<=|DEG|,|DFG|<=62,
  58<=|EFG|<=63, 52<=|DEFG|<=62.

The triple lower bounds follow from two pair intersections inside one
68-set. The quadruple lower bound follows inside D by removing sets
of sizes 5,5,6. Upper bounds follow from the pair intersections. For
every vector in these ranges, set f(empty)=1024, f(singleton)=68,
f(pair)=63 except f(DG)=62, and f(triple),f(quadruple) as prescribed.
Möbius inversion gives each exact membership atom

  n_S=sum_(T superset S) (-1)^(|T|-|S|) f(T).

Retain exactly the vectors with every n_S>=0. Conversely these atoms
reconstruct all the prescribed intersections and hence supports, so
this is complete. The resulting 150 atom vectors agree exactly with
the constructor's full set, with no duplication or omitted case.

The verifier reconstructs every support and matrix directly from these
atoms and reparses canonical coefficients. It compares every eligible
anchor record and every entry. It recomputes all 2250 rational minors
by Gaussian elimination with row swaps, independently of the constructor's
permutation determinants. For every saved column matrix T it checks
det(T)!=0 and every entry of T^t*K*T, including every off-diagonal zero
and all four positive diagonal values. These identities prove positive
definiteness of each K by the cited quadratic-form criterion; rho>0
then proves the same for the actual matrix. All 7506 verifier checks
pass with no failures. Full independently reconstructed evidence and
input hashes are saved in
`scripts/finite-support/released-zero-four-index-verification.json`.
An initial verifier run stopped on a Python set/frozenset method mismatch
before completing; intersection operators repaired it, and the complete
run above replaced no mathematical input or failed inequality.

This finite substitution exhausts only the specified six-distance
pattern and fixed assignment. The unchanged objective remains L053's
above-threshold value, so this pass parks the diagnostic. Other moments,
larger or full conditioned matrices, actual-label zeros, measures and
RS realizability remain open. This arithmetic reconstruction is not
the later separate critical proof review.

**Separate critical proof review — step 192, 2026-10-13.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-13-four-index-critical-audit.md`.
The review retains the conclusion without changing moments or hypotheses.
The precise Polak and Brouwer–Haemers imports above suffice; neither
general theorem is reproved. For singleton conditioning, the four index
families have sizes one or two, so the source condition is respectively
1+2*0<=3 or 1+2*1<=3. Their unions are exactly a singleton, a pair,
or one of DEF, DEG, DFG. All pair distances meet the minimum ten.
Neither EFG nor DEFG is an entry. Division by the strictly positive
rho preserves positive definiteness, and the normalized leading entry
is one. The triple recipe is L056's, not L053's earlier trial formula.

Both exhaustive parameterizations were checked against the manuscript.
Each removed or added pair intersection with a size-five set lies in
[0,5], and both triple intersections lie in [0,5]. The added pair
sizes 6-b,6-c force b,c>=1. The three private atoms give each displayed
triple lower bound, and the three pair-only atoms give its upper bound.
The remaining outside atom is nonnegative because the union has size
at most 5+5+6=16. Conversely every nonnegative partition yields sets
of the required sizes in each part, with no further compatibility
condition between disjoint parts. Inside D, absence from E,F,G accounts
for the complement of the three-bit mask. This proves coverage of all
16 atoms and the bijection with the five parameters.

For the other enumeration, two intersections of sizes s,t inside a
68-set intersect in at least s+t-68 points. This gives the stated
triple lower bounds (some are intentionally loose); the minimum pair
intersection gives the upper bounds. Removing 5,5,6 points from D
gives |DEFG|>=52, while DEFG is contained in DG of size 62. Thus the
intersection boxes contain every case. Möbius inversion is exact on
the sixteen membership atoms, and nonnegative atoms reconstruct all
prescribed intersections. Equality of the two complete enumerations
therefore verifies exhaustive coverage, not just agreement of samples.
For any fixed atom vector a bijection between corresponding regions
preserves all moments used here, since they depend only on these region
sizes. No actual-label constraint is transported by this argument.

DEF admits all three anchors; DEG admits only E and DFG only F.
Every eligible ordered representation must have the eight regions
displayed above. The common region determines r=63-common; the
nonanchor pair-only region determines q=5-pair_only. Alternative DEF
anchors return the same relation by L056's audited unordered dictionary.
These observations justify the three off-diagonal entries in K and
the actual p_6 at G, including its Boolean diagonal. L057 is comparison
only, not a mathematical input to this review.

The entire existing independent verifier was inspected and rerun:
7506 checks pass. It checks both enumeration sets, all original
eligible-anchor records, complete matrices, every minor, source hashes
and every congruence. The additional independent audit is

  `python3 scripts/finite-support/critical_audit_released_zero_four_index.py`.

It imports no notebook routines. It reparses all 21 manuscript
coefficients, checks their full saved vector, and checks rho,p_5,p_6
against their exact formulas. A loose enumeration over [0,5]^5 tests
all eight atom inequalities on each part before comparing both complete
saved atom sets and all tightened manuscript bounds. It marginalizes
each 16-atom partition directly, reconstructing weights, distances and
all six orders of each of the three represented triples. Every eligible
order has the required full regions and exactly the saved moment.

For every case it reconstructs the displayed K directly and compares
both saved matrices. Laplace expansion independently recomputes every
one of the 2250 minors, comparing both saved minor lists and checking
strict positivity. It checks all 2400 entries of the saved congruences,
including all off-diagonal zeros, and all 600 positive pivots against
both certificates. The column matrices have determinant one in all
150 cases. The identity det(K)*det(T)^2=product(pivots) is also checked
separately. Thus for every nonzero vector v, write v=T*w with w nonzero;
the certified identity gives v^t*K*v=sum_i pivot_i*w_i^2>0, as in the
cited quadratic-form criterion. No singular inverse, numerical sign,
success flag or incomplete certificate preview is used as proof.

All 7956 additional checks pass with zero failures. Complete exact
matrices, all minors, permuted regions, congruences and source hashes
are in
`scripts/finite-support/released-zero-four-index-critical-audit-results.json`.
This establishes the audited local input only. The global triple
extension, other patterns or pair moments, full conditioned PSD,
actual-label restrictions, measures, RS realization and both safety
gaps remain unresolved. ATTEMPTS/040's diagnostic stop is retained;
there is no boundary improvement or claim of progress beyond the
assessed source methods.

## Mathlib

Full matching fixed-coefficient certificate, union program and Schur
coverage: not checked. Supporting finite-set and linear-algebra coverage:
not checked. Unknown availability is not evidence of absence.
