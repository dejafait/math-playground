# L076 — A distance-eight column annihilates the complete three-shell base kernel

## Hypotheses

Use L021's complete original pair prescription, L053's positive singleton
rho, and exactly L075's represented unordered moment dictionary on the
68-subsets of a 1024-point set. In particular

    p8=16792471/1181138102168120460>0.

The retained matrix is L073's entire included-anchor PSD matrix on {D}
and {D,E} for every E at half-distance 5,6,7 from D, divided by rho.
Its anchor diagonal is 1, anchor/layer-l entry is p_l, and shell entries
are Y(D,E,F)=x({D,E,F})/rho. Preserve L075's original pairs, original
L065 RREF at (0,v_dagger,w_star), all L062 old entries, and all 28 forced
and 36 completed seven/seven entries. No coefficient is retuned.

Fix a 68-subset G at half-distance eight from D. Add the column indexed
by {D,G}, with anchor entry and diagonal p8. Every represented complete
unordered triple key must keep its L075 value, even when represented
at a different eligible anchor. Boolean repetitions use lower-order
moments; any distinct half-distance 1,...,4 forces zero. Only genuinely
unrepresented permitted unordered keys are free nonnegative moments.
No upper scalar rows, actual-label nonfaces, scalar energy, simultaneous
new columns or global extension are imposed in this test.

## Conclusion

An explicitly specified rational nonnegative column annihilates the
entire retained matrix kernel. Its stabilizer description has 150
coordinates: one anchor, 45 represented entries, 19 additional forbidden
zeros and 85 free unordered keys. The invariant action has rank 60 and
kernel dimension 90. The compatibility equations have rank 81 and a
four-dimensional affine solution set. The specified solution has 81
positive free entries and exactly four zero free entries.

These are invariant-space dimensions, not ranks or kernel dimensions
of the enormous original matrix. This is a finite REPRODUCTION of
assessed tools with a new local feasibility verdict, without a claim
of progress beyond the checked sources as original mathematics. It
parks the necessary kernel-exclusion diagnostic for this immutable
assignment. It supplies no energy inequality, enlarged PSD matrix,
full SDP feasibility, measure, packing or common-center RS realization.
Arbitrary-center safety at 67/68 agreements and the 955–957 bracket
remain unchanged. The separate critical proof review below retains this result.

## Proof

**Imports and scope.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-16-distance-eight-full-base-kernel-column.md`.
Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2 and Theorem 2.6. For a retained finite symmetric
PSD matrix C and an added column b, PSD requires b perpendicular to
ker C; the additional inverse-on-range energy inequality is not tested
here. L073 supplies precisely this retained C as a PSD input, including
its singular cases. No pseudoinverse or anchor congruence is needed.

Use Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE TIT 65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and complete indicator proof, p.2, and Section
1.2, p.3, for ordinary union moments and constraint-preserving averaging.
The constant-weight conclusion follows from the proof, with the display
qualification retained in foundations/12. Here n=1024,d=10,w=68.
Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Theorem 1 (51), III.A (52)–(59), pp.6–7, supplies the complete algebra
underlying L073. These general results are imported, not reproved.
L065's reviewed finite averaging argument applies after the preservation
and exhaustion checks below; its old ranks are not imported. The new
finite action is certified directly by subset counts, without assuming
that the old stabilizer has the same kernel. No inspected theorem gives
this prescribed-coordinate verdict, so the finite specialization is needed.

**Complete orbit domain and fixed lookups.** Let U=D\G, V=G\D.
The four regions U,D intersection G,V,outside D union G have sizes
8,60,8,948. Let K be the product of the four full symmetric groups,
fixing D and G separately. Write a layer-l support as E=(D\X) union Y,
where |X|=|Y|=l and l in {5,6,7}. Its K-orbit is determined by

    i=|X intersection U|, j=|Y intersection V|, 0<=i,j<=l,
    W_(l,i,j)=C(8,i)C(60,l-i)C(8,j)C(948,l-j)>0.

Here C(n,k) is the ordinary binomial, zero outside 0<=k<=n.
Region bijections prove transitivity and completeness. The anchor has
weight 1. Thus there are 1+36+49+64=150 orbits, ordered anchor first,
then lexicographically in (l,i,j). Each layer's weights sum exactly to
C(68,l)C(956,l), by independent head/tail subset counting.

The column triple (D,E,G), with membership bits 4,2,1, has atom vector

    (948-l+j,8-j,l-j,j,i,l-i,8-i,60-l+i).

Its half-distances are l,8,l+8-i-j. All atoms are nonnegative, sum to
1024, and give three supports of size 68. For every orbit, form all six
bit-permuted atom vectors and take their lexicographic minimum. Query
L075's complete dictionary by this key; do not identify by distances
alone. Independent construction of actual supports and point-by-point
membership counts reproduces all six presentations for every old type
and every new orbit. All lookups agree, including any represented
forbidden zero. There are 45 represented entries and 19 further
forbidden zeros. No column Boolean case occurs, since l<8 and the
third half-distance is at least 8-l>0. Boolean entries inside the base
are retained separately, including Y_(l,l,l,l)=p_l.

The remaining 85 orbit keys are distinct and free. Give each one a
variable f_j, numbered 0,...,84 by first occurrence in the orbit order;
its normalized moment is y=p8*f_j. Any repeated unordered key would
share a variable by this definition. Every old dictionary entry is
checked against L075 and L074's unchanged records, including the
original parameters, RREF column and completed vector. Only these
immutable entries and ordinary forbidden zeros are fixed.

**Exact restriction of the whole base action.** For n in {68,956}
and retained layers l,m define

    T_(n,l,m,k)(i,u)=sum_(s=0)^8
      C(i,s)C(8-i,u-s)C(l-i,k-s)C(n-8-l+i,m-u-k+s).

For fixed l-subset X and distinguished eight-set U with |X intersection
U|=i, this counts m-subsets X' with |X' intersection U|=u and
|X' intersection X|=k. The four factors choose X' in the four disjoint
parts X intersection U,U\X,X\U,outside U union X; their counts exhaust
all possibilities. In particular each row sum is C(l,k)C(n-l,m-k).
The same formula applies independently to the head and tail factors.

Write Y_(l,m,k,h) for L075's shell coefficients, with both rectangular
directions retained. The actual orbit-constant action Q is

    Q_00=1, Q_0,(m,u,v)=p_m*W_(m,u,v), Q_(l,i,j),0=p_l,
    Q_(l,i,j),(m,u,v)=sum_(k,h=0)^min(l,m)
       T_(68,l,m,k)(i,u) T_(956,l,m,h)(j,v) Y_(l,m,k,h).

Thus if J sends an orbit vector to its full orbit-constant vector,
CJ=JQ, and J^T J=diag(W). All weights are positive, so J is injective.
No quotient rank is asserted to be the rank of C itself.

To certify the kernel without eliminating a large dense rational Q,
use the following fully checked change of basis. On each factor n,
layer l, let h_(n,l,a) be the monic degree-a polynomial orthogonal to
lower powers at i=0,...,l with weights C(8,i)C(n-8,l-i), for 0<=a<=l.
All weights and squared norms N_(n,l,a) are positive; these polynomials
are a basis of functions on the l+1 points. They are specified uniquely
by their monic leading term and the finite orthogonality equations.
For every one of the 118 factor transition matrices, exact full-vector
substitution verifies

    T_(n,l,m,k) h_(n,m,a)=gamma_(n,l,m,a,k) h_(n,l,a)

when a<=l, and zero when a>l. Each gamma is obtained by the weighted
inner product with h_(n,l,a), divided by its positive squared norm.
All coordinates, including zeros, are checked; no presumed eigenvalue
formula replaces these identities.

Tensoring the two polynomial bases decomposes the entire 150-dimensional
invariant space into 64 modes (a,b), 0<=a,b<=7. In each mode use the
layers l in {5,6,7} with l>=max(a,b). Include the anchor only in (0,0).
Its block B_ab has shell action entries

    B_ab(l,m)=sum_(k,h=0)^min(l,m)
       gamma_(68,l,m,a,k) gamma_(956,l,m,b,h) Y_(l,m,k,h).

In mode (0,0) its anchor entries are 1, B(0,m)=p_m*C(68,m)C(956,m),
and B(l,0)=p_l. The block is self-adjoint with weights 1 at the anchor
and N_(68,l,a)N_(956,l,b) at shell l; every weighted symmetry identity
is checked. The direct-sum block dimensions sum to 150.

Take the canonical rational RREF of each B_ab. For each nonpivot j,
set local coordinate j to 1, other nonpivots to 0, and pivot coordinates
to minus that RREF column. All resulting vectors satisfy every original
block equation. Their nonpivot identity submatrices prove independence.
Independent exact elimination modulo the prime 2147483647, after clearing
row denominators and removing integer common factors, gives matching
rank lower bounds for every block. Primality is verified by trial
division through its square root. The summed ranks are 60 and the
summed nullities 90. Mapping every local null vector v to orbit values
v_l*h_(68,l,a)(i)*h_(956,l,b)(j), with its anchor coordinate retained,
gives a complete 90-vector basis z^t of ker Q. Direct-sum exhaustion,
not a sampled nullspace or a rank borrowed from L065, proves this claim.

K preserves the anchor, layers, subset intersections, every immutable
complete key, forbidden zeros and signs. Hence it commutes with C and
preserves precisely the ordinary constraints imposed here. By L065's
reviewed averaging argument, the finite K-average P is self-adjoint,
CP=PC, and for invariant b and every v in ker C,

    b^T v=b^T Pv.

Also Pv is invariant and in ker C, so Pv=Jz for some z in ker Q.
Consequently b annihilates the entire ker C exactly when
sum_a W_a*b_a*z_a=0 for every z in ker Q. This includes all anchor,
coupled and noninvariant directions of the original matrix. No actual
subgroup-label constraint is averaged.

**Compatibility equations and exact nonnegative solution.** For each
of the 90 complete basis vectors z^t impose

    sum_(a free) W_a*z^t_a*p8*f_(key(a))
      = -sum_(a fixed, including anchor) W_a*z^t_a*b_a,

where b_anchor=p8 and all other fixed b_a are their immutable y values.
Divide each row and right side by the maximum absolute free coefficient
when nonzero. Call the resulting 90-by-85 matrix E and right side r.
Only positive nonzero row scaling is used. The unscaled weighted
residuals are checked again at the end.

Exact RREF of [E|r] is consistent and has 81 pivots. Its nonpivot
variable indices are 56,63,69,78. Set those four coordinates to zero
to obtain the particular solution c; let A be the 85-by-4 homogeneous
matrix obtained by setting each of these nonpivots to 1 in turn.
Independent modular elimination gives rank(E)>=81. Exact substitution
of c and all four columns of A, together with their identity submatrix
on the four nonpivots, gives rank(E)<=81 and verifies the entire affine
solution set f=c+A*t. This does not rely solely on the RREF trace.

Define the active index set I=(27,33,56,63), in that order. Its four
rows A_I form an invertible matrix. Define exactly

    t=-(A_I)^(-1)c_I, f=c+A*t.

Independent rational Gaussian elimination reconstructs this t, verifies
every original equation and gives f_j>=0 for all 85 coordinates.
Precisely the four coordinates in I vanish; all other 81 are positive.
Their complete unordered keys, in this order, are

    (948,0,0,8,2,6,6,54),
    (947,1,1,7,3,5,5,55),
    (948,0,0,8,1,7,7,53),
    (947,1,1,7,2,6,6,54).

These finite definitions uniquely specify all fractions without rounding.
Every fixed coordinate is nonnegative by the immutable input or its
forbidden zero. The actual minimum free coordinate is 0, meeting the
required lower bound 0. All 90 original weighted residuals vanish
exactly, with anchor p8 and the actual orbit weights. The preceding
whole-kernel argument proves the conclusion; multiply by rho>0 to
restore the original column. Point bijections give the same ordinary
construction for every pair D,G at half-distance eight.

**Reproducible evidence and limitations.** Run from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_distance_full_base_kernel.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_distance_full_base_kernel.py

The constructor passes 2441 exact checks. Its complete certificate is
`scripts/finite-support/eight-distance-full-base-kernel-results.json`:
immutable hashes, all 150 orbits/weights, every six-presentation lookup,
all factor bases/transitions, all 64 blocks and complete local RREFs,
all 90 full kernel vectors, every equation, full compatibility RREF,
four affine directions and all rational witness coordinates. A Decimal
phase-I run only proposed the active set; no solver status proves a sign
or feasibility. Staged certificates were saved before lengthy reduction.

The independent standard-library-only verifier imports no constructor,
optimizer or decimal arithmetic and passes 3677 checks with no failures.
Its full evidence is
`scripts/finite-support/eight-distance-full-base-kernel-verification.json`.
It constructs actual supports and all membership atoms, reconstructs
original p8/rho from L021/L053, retains every L075 value, computes monic
polynomials by moment-equation solves instead of Gram–Schmidt, and
rebuilds transition counts by region-polynomial convolution. It checks
all factor actions, all block ranks and complete rational null vectors,
every compatibility equation and affine direction, the invertible active
system, all 85 signs and all 90 original weighted residuals. It consumes
all relevant arrays; a bounded preview is not verification. Full summaries,
zero keys and empty failure lists were inspected using the shared JSON
inspector, with PYTHONINTMAXSTRDIGITS=0 for the long rational values.

This is arithmetic verification within the attempt, not the later
separate critical proof review. The necessary test passes, so it cannot
exclude this assignment. The stronger one-column PSD condition additionally
requires b^T*C^dagger*b<=p8, not evaluated here. Other columns, anchors,
unrepresented/global moments, measures, packings and RS realization
remain open. Preserve L067/L071 and ATTEMPTS/045,055,056,057: they test
different immutable prescriptions or matrices. No uniform bound or
boundary improvement is inferred.

**Separate critical proof review — step 266, 2026-10-17.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-16-distance-eight-kernel-critical-audit.md`.
This review retains the same statement and every coefficient. It verifies
an assessed local reproduction, without asserting a new result beyond
the sources checked. The source imports above, including singular cases,
remain unchanged; no energy theorem is reapplied to claim PSD here.

The four-region stabilizer preserves the actual retained matrix because
its entries depend only on the two subset intersections and layer indices.
It fixes the anchor and preserves the complete atom keys, forbidden
half-distances and signs of this precise ordinary slice. Its orbits are
exactly the 150 listed ones: arbitrary choices in each of the four regions
are related by its independent permutations. All weights are positive.
Thus the reviewed L065 averaging argument applies with CJ=JQ and
J^T J=diag(W). For any v in ker C, its average Pv lies in J(ker Q), and
b^T v=b^T Pv. Exhausting ker Q therefore tests every full-space kernel
direction, including noninvariant ones; no actual-label constraint or
full-space rank claim is introduced.

The existing independent verifier was rerun: all 3677 exact checks pass.
It reconstructs the full 270-type input dictionary, every old/new actual
six-presentation lookup, all 150 orbit weights, 118 complete factor
transitions and polynomial identities, 64 blocks, 90 kernel vectors,
the rank-81 affine system, active solution, all signs and all original
weighted residuals. Its exact original pair reconstruction retains p8;
no different RREF point or completion is substituted. The separate audit
also matches every input hash and all input arrays to L075's reviewed
certificate, including its original parameters, column and completion.
Those reviewed upstream results are imports, not claims of a new audit
of their entire proofs.

For an additional exhaustion check independent of the polynomial block
reduction, reconstruct the full 150-by-150 Q directly from the displayed
subset-transition counts. Both rectangular orientations satisfy their
weighted double-counting identities, and diag(W)Q is symmetric in every
entry, including the anchor row and column. Clear denominators in each
row and divide by its integer gcd; these are invertible row scalings.
Exact elimination modulo the trial-division-verified prime 2147483647
then gives rank 60. Independently clear denominators and integer gcds in
each of the 90 saved kernel vectors. Their row matrix has modular rank
90, while all 150 coordinates of Q times each vector are exactly zero:
13500 integer residuals vanish. The modular ranks give rational lower
bounds; these 90 independent rational null vectors give rational rank
at most 150-90=60. Thus the direct action has exactly rank 60 and these
vectors exhaust its kernel, independently corroborating all 64 blocks.
These vectors are used with their original rational scaling when checking
the column's weighted orthogonality.

Replay every one of the 1671 saved fraction-free operations across the
64 block eliminations and the compatibility elimination. Each row scaling
has a nonzero factor, each division is exact, and each elimination has a
nonzero coefficient on its replaced row; zero-row cases are retained.
Fresh rational back reduction matches every saved RREF entry and pivot.
The actual block norms are the positive products of the factor norms,
and all weighted block symmetry identities hold. The compatibility RREF
has 81 pivots, no augmented-column pivot, and free indices 56,63,69,78.
Its reconstructed intercept and four slopes agree exactly with the
manuscript definition. The active 4-by-4 matrix has modular rank four,
and the prescribed parameter vector solves its original rational equations.
It therefore determines exactly the claimed unique active-set solution.
All 85 signs and the four manuscript zero keys agree: 81 entries are
positive, four are zero, and the minimum equals the required bound zero.
All 90 original weighted column residuals vanish, with the original
anchor p8 retained. No omitted scalar upper constraint is asserted.

Run the separate audit from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_eight_distance_full_base_kernel.py

All 2638 additional exact checks pass. Full evidence is
`scripts/finite-support/eight-distance-full-base-kernel-critical-audit.json`:
the complete direct rational action, primitive integer action/kernel,
all 13500 direct residuals, reverse transition balances, operation counts,
complete compatibility RREF, affine solution and weighted residuals.
The full summary and empty failure list were inspected. Every relevant
array was consumed by the programs; a preview was not used as proof.

The first audit report is preserved in
`scripts/finite-support/eight-distance-full-base-kernel-critical-audit-initial.json`.
Its sole failure, `canonical_affine_recipe`, arose from encoding an exact
unit slope as integer `1` instead of fraction `[1,1]`. The corrected audit
checks equality of all slope values as rationals and exact equality of
the initial/final direct actions, kernel, residuals, RREF, intercept and
solution. No mathematical coefficient or target changed.

ATTEMPTS/058 remains parked for kernel incompatibility only. The energy
inequality b^T C^dagger b<=p8 remains untested, as do simultaneous new
columns, other anchors, unrepresented/global moments and RS realization.
The reviewed input is useful for a separately assessed fixed-column energy
test; the arbitrary-center gap and 955–957 boundary are unchanged.

## Mathlib

Full matching prescribed distance-eight nonnegative-column and complete
three-shell kernel specialization: not checked. Supporting finite-group
averaging, PSD and rational linear algebra coverage: not checked. Unknown
availability is not evidence of absence.
