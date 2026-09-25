# L002 — Agreement isolation in a geometric cover

## Hypotheses

Let F be a finite field, K an algebraic closure of F, and x_1,...,x_n distinct
elements of F. Let 1<=k<=A<=n be integers. For y in F^n let T_y be the set
of coefficient vectors in F^k of polynomials P of degree less than k with
at least A coordinates satisfying P(x_i)=y_i.

Suppose T_y is contained in a finite union of affine algebraic sets V_j in
K^k such that dim(V_j)<=s and sum_j cdeg(V_j)<=Delta, where s is a
nonnegative integer and Delta>=0. Degree and cumulative degree have the
[projective-closure convention](../foundations/03-proper-hyperplane-sections.md).
The sets may be reducible or singular and may contain points outside T_y.
Existence of this cover is an explicit hypothesis.

For the uniform/interleaved conclusion below, suppose such a cover exists
for every y with the same s and Delta. Let m>=1, 0<epsilon<1, q=|F|, and use
the [pinned column-Hamming model](../foundations/02-pinned-list-model.md).

## Conclusion

Put beta = Delta times sum_{a=0}^s n^a. Then

\[
 |T_y|\le\lfloor\beta\rfloor. \tag{1}
\]

Under the uniform hypothesis, the interleaved list satisfies

\[
 B_m((n-A)/n)\le\lfloor\beta\rfloor^m. \tag{2}
\]

In particular q>=epsilon^{-1} beta^m is a sufficient additional condition
for this radius to meet the threshold epsilon q. If Delta<=C n^c and s is
fixed, then beta^m <= [C(s+1)]^m n^{m(c+s)}. This is a conditional polynomial
bound for fixed m,c,s, not a construction of the cover or a sharp boundary.
The implication itself has no characteristic restriction.

This is the singleton-list, linear-equation specialization of
[TR26-169, Lemma 6.2 and the support step in Theorem 6.3, printed pp. 26--27](https://eccc.weizmann.ac.il/report/2026/169/download#page=26).
The paper's September 5, 2026 version was read on September 25. The proof
below checks that passage; it does not adopt its jet-decomposition theorem.
No novelty is claimed.

## Proof

**Isolation over K.** For p=(p_0,...,p_{k-1}) put

\[
 h_i(p)=\sum_{b=0}^{k-1}p_b x_i^b-y_i.
\]

For a candidate p let S_p be its full agreement set. The common zero set
in K^k of all h_i with i in S_p is {p}. Indeed |S_p|>=A>=k. If p' were
another zero, the polynomial with coefficients p'-p would have degree less
than k and at least k distinct roots in K. By the factor theorem it is
zero, so p'=p. Equivalently, any k of these equations have an invertible
Vandermonde matrix. This uses algebraic, not merely F-rational, uniqueness.

**A path for each candidate.** Decompose every V_j into irreducible
components, retaining repeated occurrences if covers overlap. Their total
degree is at most Delta. Choose a component W containing p. If W has
positive dimension, some h_i with i in S_p does not vanish identically
on W: otherwise W would be contained in the singleton {p}. Its intersection
with {h_i=0} contains p, and at least one irreducible component of that
intersection contains p. Pass to one such component.

This is a proper hyperplane section. The standard result in the cited
foundation gives a dimension drop and bounds the sum of degrees of all
children by deg(W). Repeat until the current component has dimension zero.
Over K an irreducible zero-dimensional affine set is a single point; since
it contains p it is {p}. At most s cuts are used. Initial isolated points
require zero cuts. The path may depend on p; no common agreement support
for all candidates is assumed.

**Counting all paths.** Fix an ordered tuple I=(i_1,...,i_a) of indices in
{1,...,n}. Start with the above multiset of cover components. At stage b,
replace each positive-dimensional component W on which h_{i_b} is not
identically zero by all irreducible components of W intersect {h_{i_b}=0}.
Discard branches for which this is not a proper cut, including branches
already of dimension zero. Empty intersections have no children.

For this fixed tuple, the sum of degrees at any stage is at most Delta,
by the hyperplane bound applied separately to every occurrence. In
particular there are at most Delta terminal point occurrences at depth a.
This argument does not multiply the number of components by an uncontrolled
factor: their degrees, rather than just their count, are the quantity
carried through each intersection.

Every candidate's chosen path is among these paths for its ordered tuple,
and ends at that candidate. Two distinct candidates cannot be the same
terminal point. There are n^a ordered tuples of length a. Summing over
0<=a<=s gives |T_y|<=Delta sum_{a=0}^s n^a. Duplicate paths or overlapping
cover components only increase the count. Since |T_y| is an integer, (1)
follows. A zero-degree or empty cover forces T_y to be empty and satisfies
the same argument.

**Interleaving and threshold.** If an m-row candidate agrees with an
m-row center in at least A whole columns, each of its rows belongs to the
corresponding scalar list T_y. The tuple is uniquely specified by its rows,
so the interleaved list injects into the product of those m lists. The
uniform form of (1) gives (2). Since floor(beta)^m<=beta^m, the stated
inequality on q implies B_m<=epsilon q. Finally n>=1 gives
sum_{a=0}^s n^a<=(s+1)n^s, proving the displayed polynomial estimate.

**Scope check.** If A<k, agreement equations need not isolate a point:
A distinct prescribed values leave an affine space of dimension k-A.
Even with A>=k, isolation alone supplies no small s or Delta. The trivial
cover K^k has s=k, giving a bound exponential at fixed positive rate.
Small dimension without degree control is also insufficient: a union of
N distinct points has dimension zero but cumulative degree N. Thus the
unproved cover bound cannot be omitted, inferred from interpolation
uniqueness, or replaced by counting only F-rational components.

## Mathlib

Full result (1)--(2), the geometric cover, and the supporting degree and
polynomial-root results: **not checked** in Mathlib in this step. The named
Bezout input and Stacks dimension reference are recorded in the foundation;
neither is a full list-decoding theorem. The cited TR26-169 result is a
matching mathematical source for the scalar counting passage, not a
Mathlib coverage claim or verification of the rest of that preprint.
