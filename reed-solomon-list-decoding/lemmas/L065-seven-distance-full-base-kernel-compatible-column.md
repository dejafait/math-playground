# L065 — A distance-seven column annihilates the complete five/six-base kernel

## Hypotheses

Use L021's rational pair prescription and L053's positive singleton rho
on the 68-subsets of a 1024-point ground set. In particular
p5=1/68881143660, p6=133/9357995374380 and
p7=3539/248922676958508. Fix D,G at half-distance seven.
Retain exactly the complete anchored five/six-shell matrix of L061,
with its unchanged L056 coefficients, L060 minimizing columns and
L061 six/six completion. Use the immutable represented moment dictionary
of L062, including all six support presentations of its 121 types.

Add the column indexed by {D,G}, whose diagonal and entry against {D}
are rho*p7. Against {D,E}, fix every represented unordered triple to
its L062 value by its complete eight-atom key minimized over all six
support orders. Fix forbidden nonzero half-distances 1,...,4 to zero.
Give every other unordered key one free nonnegative real moment.
No extra scalar upper bounds, labeled nonfaces, scalar Schur energy,
multiple new columns or global completion are required.

## Conclusion

For every D,G as above, an explicitly specified rational nonnegative
column satisfies every prescribed entry and annihilates the full kernel
of the retained anchored matrix. Its invariant description has 86
coordinates: the anchor, 20 represented entries, 16 forbidden zeros and
49 free entries. The complete invariant base action has rank 37 and
kernel dimension 49; these are quotient dimensions, not dimensions of
the enormous original base. Its compatibility equations have rank 46
and a three-dimensional affine solution set. The witness has 46 strictly
positive free entries and three zeros.

This parks the necessary kernel-exclusion diagnostic for this unchanged
prescription. It is a local REPRODUCTION/specialization of assessed tools,
without an originality claim. Scalar energy and PSD of the enlarged
matrix remain unproved, as do simultaneous new columns, global moments,
labels, measures, packings and common-center RS realization. The 955–957
bracket and arbitrary-center safety at 67/68 agreements are unchanged.
The separate critical proof review below retains this conclusion.

## Proof

**Imports and scope.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-seven-distance-full-base-kernel-column.md`.
Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum, version of record
27 February 2026, DOI 10.1007/s44146-026-00231-y,
[Section 2, Corollary 2.2 and Theorem 2.6](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For a finite symmetric matrix with retained PSD block C and new column b,
PSD requires b perpendicular to ker(C); this condition together with
the generalized-Schur energy bound is sufficient. Singular C is allowed.
Here L061 supplies C PSD, and only the necessary kernel condition is
tested. The imported theorem is not reproved.

The union indices and constraint-preserving finite-group averaging are
Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE TIT 65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and its indicator proof, p. 2; Section 1.2,
p. 3. The proposition's display has A(n,d), while its proof supplies
A(n,d,w), as qualified in foundations/12. The parameters n=1024,d=10,
w=68 apply. L061's complete mixed-layer PSD input imports Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Theorem 1 (51), III.A (52)–(59), pp. 6–7, including singular blocks.
No new source block theorem is proved here. The exact quotient calculation
below is necessary because no inspected theorem supplies these prescribed
column entries or their feasibility verdict.

**All column orbits and immutable lookup.** Write U=D\G and V=G\D.
Their sizes are seven; the other two membership regions have sizes
61 and 949. Let K be the product of symmetric groups on these four
regions, fixing D and G separately. Every retained layer-l support is
E=(D\X) union Y with |X|=|Y|=l, l=5 or 6. Put
i=|X intersection U| and j=|Y intersection V|. There is precisely one
K-orbit for each (l,i,j), 0<=i,j<=l, of size

  W_(l,i,j)=binomial(7,i)binomial(61,l-i)
             binomial(7,j)binomial(949,l-j).

Each size is positive. Region permutations map any such support to any
other with the same parameters. Include the singleton anchor orbit o0,
with weight one. Thus these 1+36+49 orbits exhaust the invariant space.
Their layer weight sums equal binomial(68,l)binomial(956,l).

In mask order 0,...,7 with support bits D,E,G of weights 4,2,1, the
column atom vector is

  (949-l+j, 7-j, l-j, j, i, l-i, 7-i, 61-l+i).

Its half-distances are l,7,l+7-i-j. All atoms are nonnegative and the
three support sizes are 68. For each vector form all six bit-permuted
vectors and minimize lexicographically. Look up that complete key in
L062's unchanged dictionary. Every matching key fixes y=x({D,E,G})/rho
to its stored value, regardless of its old eligible anchor. A forbidden
distance fixes zero; all such overlaps with the dictionary agree at zero.
All other keys are free. Enumerating the complete 85-orbit domain gives
20 represented, 16 forbidden and 49 free keys; the free keys are distinct.
No distance-only replacement or unrepresented extra prescription is used.
D,E,G are distinct because l is five or six and DG has distance seven.
Boolean cases inside the retained base still use their lower-order pairs.

Order the anchor first, then (l,i,j) lexicographically with l=5 before 6.
Order the free keys by their first occurrence in this order, numbering
them 0,...,48. This fully specifies all later coordinate indices.

**Whole anchored orbit action.** Divide the retained base by positive
rho and call the resulting symmetric matrix C. Denote its coefficient
between layers l,m with intersections k,h by Y_(l,m,k,h). When l<=m,
these are exactly L062's 121 normalized coefficients: p5*d5 on five/five,
p5*t on five/six and p6*d6 on six/six. For l>m interchange l,m; k,h
are unchanged. The diagonal is the corresponding pair, not a
distinct-triple expression. The anchor entry is one and its entry
against layer l is p_l.

For n=68 or 956 let

  T(n,l,m,i,u,k)=sum_(s=0)^7 binomial(i,s)binomial(7-i,u-s)
       binomial(l-i,k-s)binomial(n-7-l+i,m-u-k+s),

where binomials outside their ordinary ranges are zero. This counts
m-subsets X' with |X' intersection U|=u and |X' intersection X|=k
when X has size l and |X intersection U|=i: choose s points in X
intersection U, u-s in U\X, k-s in X\U, and the remaining m-u-k+s
outside U union X. These four disjoint choices exhaust the possibilities.
The analogous count applies independently to outside subsets Y'.
In particular sum_k T=binomial(7,u)binomial(n-7,m-u).

The exact orbit action Q, acting on orbit-constant functions, has

  Q_00=1, Q_0,(m,u,v)=p_m*W_(m,u,v), Q_(l,i,j),0=p_l,
  Q_(l,i,j),(m,u,v)=sum_(k,h=0)^min(l,m)
       T(68,l,m,i,u,k)T(956,l,m,j,v,h)Y_(l,m,k,h).

For any orbit-constant function f, the full action Cf at a point of
orbit a is sum_b Q_ab*f_b by the count just proved. Thus Q is exactly
the restriction of C to the full invariant space, including the anchor.
Its inner product is sum_a W_a*f_a*g_a; exact weighted self-adjointness
W_a*Q_ab=W_b*Q_ba is checked for every entry. No anchor congruence or
pseudoinverse transport is used: the new anchor entry remains p7.

K preserves every base entry, the immutable atom keys, forbidden zeros
and nonnegativity. Hence averaging any admissible column loses no
feasibility for this ordinary unlabeled test. More specifically, for
an invariant b and any full-base kernel vector v, its finite K-average
Pv is invariant, still lies in ker C, and satisfies <b,v>=<b,Pv>.
It follows that weighted orthogonality to ker Q is equivalent to
orthogonality to the entire ker C, including all coupled directions.
This argument does not average actual-label constraints.

**Complete exact kernel and equations.** Let S be the least common
multiple of denominators of all Y entries and retained pairs, so SQ is
an explicitly defined integer matrix. Its exact RREF has 37 pivots.
For each nonpivot j, define v^j_j=1, v^j at the other nonpivots zero,
and v^j_k=-RREF(SQ)_(r,j) for the pivot k in row r. All 49 complete
vectors satisfy (SQ)v^j=0. Their identity submatrix at the nonpivot
coordinates proves independence. Independent exact modular elimination
at the prime 2147483647 gives rank 37, supplying the matching lower
bound; primality is checked by trial division through its square root.
These lower and upper rank bounds certify kernel exhaustion without
trusting the constructor's elimination trace alone.

Write f_0,...,f_48 for the free column entries normalized by positive p7,
so a free y=p7*f_j. Keep b_0=p7 and every fixed coordinate b_a at its
immutable y value. For each v^j impose

  sum_(a free) W_a*v^j_a*p7*f_(key(a))
       = -sum_(a fixed, including anchor) W_a*v^j_a*b_a.

These are precisely all 49 whole-kernel equations. Divide each row and
right side by the maximum absolute free coefficient if nonzero; call
the resulting matrix E and right side r. This positive row scaling
does not change the solution set. Complete rational elimination gives
rank E=46 and a consistent system. Independent modular elimination
proves rank at least 46, while the three independent null vectors
below prove rank at most 46.

In the RREF of [E|r], the nonpivot variable indices are exactly
27,33,42. Set these variables to zero to obtain the particular solution
c. For s=27,33,42 let a^s be the null vector with that nonpivot equal
to one and the other two zero; its pivot entries are minus the
corresponding RREF column. Then every solution is uniquely

  f=c+u*a^27+v*a^33+w*a^42.

All 49 equations are independently checked for c and each a^s.
Their identity submatrix at 27,33,42 proves independence. These exact
definitions, the finite input recipes above and ordinary RREF uniquely
specify every rational number, with no unspecified solver choice.

**Rational nonnegative witness.** Choose

  u=v=0, w=-c_4/a^42_4.

Exact arithmetic gives a^42_4 nonzero and w strictly positive.
Substitution into every one of the 49 coordinates gives exactly
f_4=f_27=f_33=0 and f_j>0 at all other 46 indices. The three zero keys,
respectively, are

  (948,0,1,7,3,5,4,56),
  (949,0,0,7,1,6,6,55),
  (948,1,1,6,2,5,5,56).

The complete evaluated fractions and all residuals are saved in the
certificates below. The witness is also the unique solution of the
49 compatibility equations with these three coordinates zero, since
the parameter-coordinate identities and a^42_4 nonzero fix u,v,w.
Decimal phase I only suggested this active set; the explicit rational
specification, all signs and every original equation are checked without
relying on its status. All fixed entries are retained, and all 49
weighted whole-kernel residuals vanish exactly. The averaging argument
then proves b perpendicular to the full kernel. Multiplying by positive
rho gives the required actual column. Point bijections transport this
entire ordinary dictionary and construction to every D,G at distance
seven, without transporting any actual-label RS constraint.

**Evidence and limits.** Run from the active notebook:

  `python3 scripts/finite-support/seven_distance_full_base_kernel.py`

Its full certificate is
`scripts/finite-support/seven-distance-full-base-kernel-results.json`.
It stores immutable hashes, every atom presentation and lookup, all 86
orbit weights, the entire integer action, complete RREF and kernel basis,
every original equation, the affine solution and full rational column.
All 4412 constructor checks pass with no failures.

Independently run

  `python3 scripts/finite-support/verify_seven_distance_full_base_kernel.py`.

This verifier imports no constructor, optimizer or decimal arithmetic.
It reconstructs the old five coefficients from L056's manuscript,
the old column from L059's affine input and L060's manuscript minimizer,
and L061's unchanged six coefficients. It checks all 121 old moments
and six presentations against L062's certificate. It constructs the
whole action by independently convolving the two region overlap-count
polynomials, checks every action entry, every complete rational kernel
vector, rank lower bounds, lookup and free key, all affine equations,
every column sign and all original weighted residuals. All 12638 checks
pass with no failures. Complete evidence is
`scripts/finite-support/seven-distance-full-base-kernel-verification.json`.
The verifier consumes the entire load-bearing evidence; previews are
not used as verification. The separate proof review is recorded below.

The achieved condition is nonnegative kernel compatibility. The stronger
required condition for a one-column PSD extension additionally includes
p7>=b^T*C^dagger*b. That energy has not been computed here. No failure
of an exclusion certificate establishes RS unsafety, and no pass proves
global feasibility. L064 and ATTEMPTS/041,043,046 retain their earlier
distinct scopes. There is no boundary improvement or complete candidate.

**Separate critical proof review — step 221, 2026-10-14.** Reuse the
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-14-seven-distance-full-base-kernel-critical-audit.md`.
This review retains the hypotheses, dictionary and conclusion. It is
validation of a finite reproduction, with no novelty or boundary claim.
The cited Sano criterion is used only for kernel necessity. Polak's
ordinary union-index setting and constraint-preserving averaging apply;
L061 supplies the retained PSD matrix at these very entries. No source
theorem supplies the finite rank or witness, so these require the
following complete local checks.

First, the quotient argument covers the whole kernel, not merely a
convenient family of null directions. Let J send an 86-coordinate vector
to the corresponding orbit-constant full vector. Every orbit is nonempty,
so J is injective and J^T J=diag(W). Direct counting gives CJ=JQ.
Consequently J identifies ker Q with the invariant part of ker C.
Each permutation in K commutes with C: it preserves the anchor, layers
and both subset intersections determining every retained entry. It also
preserves all full atom-key lookups, forbidden distances and column signs.
The average P of its permutation matrices is a self-adjoint projection,
since inverse permutations occur with the same weight; CP=PC.
For the constructed invariant b=J*b_hat and any v in ker C,
Pv=J*z for some z in ker Q and

  b^T v=b^T Pv=b_hat^T diag(W) z.

Thus testing every quotient kernel vector with the actual weights is
sufficient; necessity follows by taking v=J*z. This includes coupled
and anchor components without a pseudoinverse congruence assertion.
It makes no assertion that 37 is the rank of the original full matrix.

Independently construct actual 68-subsets for every one of the 121 old
types and 85 new column orbits. Count membership directly on all 1024
points under all six support orders, and compare every atom, full key,
distance, Boolean case and represented value. The unchanged dictionary
is checked against the reconstructed L056/L059/L060/L061 inputs by the
rerun verifier. Every new lookup, including forbidden represented entries,
agrees; all 49 free keys are distinct. The weights are positive and their
layer sums are the complete layer cardinalities. Transitivity follows
by bijections within each of the four regions; there are no missing
invariant coordinates. No actual-label symmetry is used.

For an independent action count, choose concrete U and X in an n-set,
with |U|=7, |X|=l and |U intersection X|=i. Enumerate every subset Z
of U union X, whose size is at most thirteen. Each m-subset X' is
uniquely Z union R, with R outside U union X; for fixed Z there are
binomial(n-|U union X|,m-|Z|) choices. Sort these choices by
|Z intersection U| and |Z intersection X|. This reconstructs all
transition counts for n=68,956 and l,m=5,6 without calling the original
binomial-sum implementation. Tensoring the two counts reproduces every
entry of the complete anchored action, and all weighted symmetry
identities hold. The anchor row and column are checked separately.

Consume both complete certificates. Replay all 1959 base and 937
compatibility elimination operations on freshly reconstructed matrices:
each swap, nonzero row scaling and elimination is invertible over Q,
and every claimed integer division is exact. Rational back reduction
then reproduces every row of both saved RREFs, including zero rows.
The base has precisely 37 pivots. Its 49 canonical null vectors are
regenerated and checked in every action row, with their identity
submatrix proving independence. The original modular lower bounds are
also retained by the rerun independent verifier. Every weighted
compatibility equation is reconstructed from its fixed entries including
the anchor; its exact RREF has 46 pivots and nonpivots 27,33,42.
Regenerate every coordinate of c and the three directions, including
zero nonpivot coordinates of c, and check all four sets of residuals.

The active-set coefficient a^42_4 is strictly positive and nonzero;
the complete exact fraction is saved as `active_denominator` in the
audit certificate. Regenerating u=v=0 and w=-c_4/a^42_4 gives the same
positive w, all 46 positive free coordinates and exactly the three
stated zero keys. Every fixed sign and every original weighted kernel
residual is checked. The corrected decimal-basis extraction also yields
{4,27,33}, including the two nonbasic parameter-zero constraints. Neither
the decimal phase-I value nor its status is used to establish feasibility:
the rational active set has the unique solution just verified. The
column and parameters agree completely between both original certificates.

Run `python3 scripts/finite-support/verify_seven_distance_full_base_kernel.py`
and `python3 scripts/finite-support/critical_audit_seven_distance_full_base_kernel.py`.
All 12638 rerun reconstruction checks and 16647 additional critical-audit
checks pass with no failures. The audit imports no notebook code,
optimizer or decimal arithmetic. Its complete evidence, including actual
presentations, subset counts, action, weights, full rational witness and
all weighted residuals, is saved in
`scripts/finite-support/seven-distance-full-base-kernel-critical-audit.json`.
The full summary, failure list and active coefficient were inspected;
the audit computations consume complete load-bearing arrays, not previews.
No mathematical correction was needed. This validates the necessary
kernel pass only; the scalar energy inequality, enlarged PSD and all
global/RS conclusions remain unresolved exactly as stated above.

## Mathlib

Full matching prescribed nonnegative column theorem and mixed-layer
kernel specialization: not checked. Supporting finite-group averaging,
PSD, weighted linear algebra and exact-arithmetic coverage: not checked.
Unknown availability is not evidence of absence.
