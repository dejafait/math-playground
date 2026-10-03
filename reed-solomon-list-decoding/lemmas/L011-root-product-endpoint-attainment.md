# L011 — Root-product attainment of the common-support endpoint

## Hypotheses

Let F be a finite field of cardinality q, let L consist of n distinct
evaluation points, and let 1 <= k <= n and m >= 1 be integers. Let C be
the evaluations on L of polynomials of degree strictly less than k.
Use closed column-Hamming balls and the worst-case list size B_m from the
[pinned model](../foundations/02-pinned-list-model.md). Fix 0 < epsilon < 1.
In particular, these hypotheses include every pinned smooth multiplicative
coset of power-of-two size n >= 16 at the four prize rates. No change of
the given field or restriction on its characteristic is made.

## Conclusion

The endpoint common-support bound is attained:

\[
 B_m((n-k)/n)=\binom nk. \tag{1}
\]

It is attained at the single received array Y(x)=(x^k,0,...,0). Its list
consists exactly of the tuples (f_S,0,...,0), evaluated on L, where

\[
 g_S(X)=\prod_{a\in S}(X-a),\qquad f_S(X)=X^k-g_S(X),
 \qquad S\subseteq L,\quad |S|=k. \tag{2}
\]

Every such tuple has exactly k simultaneous agreement columns. Therefore

\[
 B_m((n-k)/n)\le\varepsilon q
 \quad\Longleftrightarrow\quad
 q\ge\varepsilon^{-1}\binom nk. \tag{3}
\]

When epsilon q >= 1, L001's largest safe grid index satisfies
t_star=n-k if and only if (3)'s field condition holds. If
1 <= epsilon q < binomial(n,k), the endpoint is unsafe at this explicit
center and t_star<n-k. The remaining boundary below it is not determined.
At fixed prize rate R=k/n, the endpoint condition requires
q>=epsilon^(-1) R^(-Rn), by L001's elementary binomial lower bound.
The field-existence proviso alone does not imply this condition.

## Proof

**Known input and the specialization being reproduced.** The monic
root-polynomial/common-pivot construction appears in Ben-Sasson, Kopparty
and Radhakrishnan, [Subspace Polynomials and List Decoding of Reed-Solomon
Codes](https://www.math.utoronto.ca/swastik/rsld.pdf), author-hosted eight-page
manuscript, Sections 1.2-1.3, pp. 2-3, and Proposition 3.4 with its proof,
p. 6. That presentation uses the full field and degree at most K. Li and
Wan, [Distance Distribution in Reed-Solomon Codes,
arXiv:1806.00152v3](https://arxiv.org/pdf/1806.00152v3), 2019-07-30,
Corollary 1.6, p. 4, give the scalar full-field degree-k-center root
distribution; its r=k case is binomial(q,k), for 1<=k<=q-1. Their Section 2
also explicitly counts the interpolation conditions on distinct subsets.
These are known scalar inputs and supporting constructions, rather than an
inspected theorem matching the entire prescribed-domain, interleaved claim.

The saved assessment
[approves this specialization](../drafts/literature/2026-10-03-root-product-endpoint.md).
The checks needed here are strict message degree, a prescribed subset in
the given field, distinct evaluation tuples and simultaneous column
agreement for every m. The argument below reproduces that construction
directly; it does not reprove the full distance-distribution formula or
claim progress beyond the checked literature.

**Degree cancellation and one common center.** For each k-element subset
S of L, g_S is monic of degree k. Its leading term is X^k, so f_S=X^k-g_S
has degree less than k (including the possibility f_S=0). All coefficients
belong to the given field F. Thus (f_S,0,...,0) is a valid message tuple.
Use the same received array Y(x)=(x^k,0,...,0) for every S.

For x in L, the difference of its first coordinate from that codeword is
g_S(x). A product in a field is zero if and only if a factor is zero;
therefore g_S(x)=0 exactly when x belongs to S. The other m-1 coordinates
agree everywhere. Consequently the whole column agrees exactly on S,
and the normalized distance is (n-k)/n, including equality in the closed
ball. This uses one row with a nonzero difference and works also when m=1;
it does not combine separate row lists.

**Distinctness.** If S and T are different k-subsets, take x in their
symmetric difference. At x, exactly one of g_S(x),g_T(x) is zero, so the
first coordinates of the two evaluation words differ. Hence there are
binomial(n,k) distinct candidate tuples in the single ball around Y.
L001's bound at t=n-k is binomial(n,k), independently of m. This lower
count and that upper bound prove (1).

**Exact description of this center's list.** To check independently that
the witness has no extra candidates, let (h_1,...,h_m) be any message tuple
in the ball around Y and let S be its simultaneous agreement set. Then
|S|>=k, and X^k-h_1 is monic of degree k and vanishes on S. A nonzero
degree-k polynomial has at most k distinct roots, by the factor theorem,
so |S|=k. The product g_S divides X^k-h_1; the equal degrees and monic
leading coefficients imply X^k-h_1=g_S. For every row j>=2, h_j vanishes
on S and has degree less than k, so the same root bound gives h_j=0.
The tuple is exactly the one in (2). This also explains why increasing m
does not multiply the witness count. The root bound remains valid in
every characteristic. For k=n this center has one matching codeword, and
for k=1 all f_S are constant; neither endpoint creates an exception.

**Threshold comparison.** Substitute (1) into the inclusive list-size
inequality and divide by epsilon>0 to get (3). Equality is safe. If the
field condition fails, (2) is an actual list exceeding epsilon q at the
endpoint, rather than merely failure of an upper-bound certificate.
Under epsilon q>=1, L001 supplies the existing safe index t_star and
excludes every grid index above n-k by its q^m witness at the next point.
Thus safety at n-k is equivalent to t_star=n-k, proving the boundary
qualification. L001's binomial estimate gives the stated exponential
necessary field size at fixed rate.

This does not locate t_star for the smaller-field regime, prove a bound
at k+1 or more agreements, supply a general differential cover, or
complete the parked ABF26 comparison. It is a local reproduction and an
endpoint sharpness result, not a complete candidate for the challenge.

**Computational corroboration.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/root-product-endpoint/verify.py`.
The independent check reconstructs every candidate on a nontrivial
16-point multiplicative coset over F_97 by Lagrange interpolation, rather
than subtracting root products, at all four prize rates and widths 1 and 3.
It also reuses `scripts/finite-support/verify.py` to enumerate all toy-code
centers modulo translation and check the endpoint maximum and threshold
comparison, including equality, below and above the endpoint count.
The output is saved in `scripts/root-product-endpoint/results.json`.
The toy enumeration is exhaustive only for its stated cases; neither it
nor the F_97 check is a proof for arbitrary fields or a computation at the
cryptographic epsilon. The proof of (1)--(3) above is symbolic.

## Mathlib

Full endpoint equality and the prescribed-domain, simultaneous-interleaving
statement: **not checked** in Mathlib. Supporting factor, degree and
polynomial-root theorems: **not checked**. The two directly linked scalar
source results above support the mechanism; no full matching interleaved
theorem or formal library version is asserted. The pinned ArkLib definitions
are **present** as recorded in the model, and fix the metric and threshold;
they do not prove (1).
