# L001 — Common-support list bound and a large-field boundary

## Hypotheses

Let F be a finite field of cardinality q, let L be n distinct evaluation points,
and let 1 <= k <= n and m >= 1 be integers. Let C be the evaluations of
polynomials of degree less than k on L. Use simultaneous column agreement,
closed Hamming balls, and the worst-case list size B_m(delta) from the
[pinned model](../foundations/02-pinned-list-model.md). Fix 0 < epsilon < 1.
No smoothness, prime-field, or characteristic restriction is required.

## Conclusion

For every integer t with 0 <= t <= n-k,

\[
 B_m(t/n)\le
 \left\lfloor\frac{\binom nk}{\binom{n-t}{k}}\right\rfloor. \tag{1}
\]

At the next grid point after n-k errors,

\[
 B_m((n-k+1)/n)\ge q^m>\varepsilon q. \tag{2}
\]

A safe nonnegative radius exists if and only if epsilon q >= 1. When it
exists, there is a unique largest safe error index t_star in {0,...,n-k}, and
the safe real radii in [0,1] form exactly

\[
 \{\delta:B_m(\delta)\le\varepsilon q\}
     =[0,(t_\star+1)/n). \tag{3}
\]

Consequently t_star/n is the largest **grid** radius, (t_star+1)/n is the
supremum of safe real radii, and there is no attained largest safe real radius.

In the additional regime

\[
 q\ge\varepsilon^{-1}\binom nk, \tag{4}
\]

one has t_star=n-k. Thus the largest safe grid radius is 1-k/n, and its next
grid point 1-k/n+1/n is unsafe. Condition (4) is sufficient, not necessary.
This is a restricted result, not a determination of t_star for every instance
satisfying only epsilon q >= 1, and not a disproof of the ABF challenge.

## Proof

**Uniqueness from k columns.** If two polynomial tuples agree on k distinct
evaluation points, their row-wise differences have degree less than k and
vanish at all k points, so every difference is zero. The polynomial root
bound used here follows from the factor theorem: successive distinct roots
give successive factors X-a, since earlier factors are nonzero at a later
root. A nonzero polynomial of degree less than k cannot have their degree-k
product as a divisor. In particular evaluation on L is injective.

Fix a center Y and let A_P be the set of columns on which a candidate P agrees
with Y. For P in its t-error list, |A_P| >= n-t >= k. Associate to P all
k-element subsets of A_P. If distinct candidates shared one such subset,
they would agree with each other on its k columns and hence be equal by the
preceding argument. These collections of k-subsets are therefore pairwise
disjoint. Each contains at least binomial(n-t,k) subsets of L, while L has
only binomial(n,k) k-subsets in total. Double counting gives

\[
 |\{P:d_{\rm col}(Y,P)\le t/n\}|\binom{n-t}{k}\le\binom nk.
\]

The denominator is positive. Divide, use integrality, and maximize over Y to
obtain (1). Counting the common support directly is why no power m appears.

**An unsafe next point.** Choose S contained in L with |S|=k-1, and put
h(X)=product over a in S of (X-a), with the empty product equal to 1. For
b=(b_1,...,b_m) in F^m let P_b be the evaluation of
(b_1 h,...,b_m h). Each row has degree at most k-1. At a point of S all rows
vanish. At any point outside S, h is nonzero, so a nonzero b gives a nonzero
column. Thus each nonzero P_b has exactly n-k+1 nonzero columns.
The tuples P_b are distinct: L has a point outside S, and division by h at
that point recovers b. All q^m tuples, including P_0, lie in the closed ball
of radius (n-k+1)/n around zero. Since m>=1 and epsilon<1, q^m>=q>epsilon q.
This proves (2), including k=1 and k=n.

**Threshold and radius conventions.** B_m(0)=1: a radius-zero ball contains
at most its center, and the zero center belongs to the code. Hence epsilon
q>=1 is necessary and sufficient for some safe radius, by monotonicity.
If it holds, zero is a safe grid index and n-k+1 is unsafe by (2).
The safe indices therefore have a unique largest member t_star<=n-k.

For 0<=delta<1 a distance e/n is at most delta exactly when the integer e
is at most floor(n delta). Hence B_m(delta)=B_m(floor(n delta)/n).
Monotonicity and the definition of t_star now give (3) for delta<1.
Radius 1 is unsafe by (2) and monotonicity, so (3) holds on all of [0,1].
Its right endpoint is positive and at most 1. Every point inside the interval
has a larger point still inside it (take its midpoint with the right endpoint),
which proves the nonattainment statement. This elementary argument agrees
with the pinned ArkLib boundary theorem cited below; it is not a claim of
novelty for that existing fact.

Finally (1) at t=n-k has denominator binomial(k,k)=1. Under (4), it certifies
B_m((n-k)/n)<=epsilon q. Equation (2) excludes the next and every larger
grid point, proving t_star=n-k.

**Quantitative limitation.** At any fixed prize rate R=k/n, the sufficient
field size in (4) grows exponentially with n. Indeed

\[
 \binom nk=\prod_{i=0}^{k-1}\frac{n-i}{k-i}
       \ge(n/k)^k=R^{-Rn},
\]

since (n-i)/(k-i)>=n/k for each i when n>=k. Mere existence asks only for
q>=epsilon^{-1}. The added binomial factor cannot be inferred from that
condition. Failure of (4) also does not imply the code is unsafe at t=n-k;
the upper estimate may be loose. This proof supplies no polynomial-in-n
list estimate near capacity and does not review the September preprints.

**Verification.** The proof is symbolic. The independent small-field check
in `scripts/finite-support/verify.py` enumerates all polynomial tuples and
all received words up to code translation for its stated cases. Translation
preserves every list size. Every prefix of k columns occurs exactly once
among the tuples (also checked computationally), so subtracting its unique
codeword leaves a center with zero prefix; enumerating all suffixes is exhaustive.
This check is evidence against counting mistakes, not a proof for arbitrary
fields or a test at the cryptographic threshold.

## Mathlib

Full result (1)--(4): **not checked** in Mathlib. Supporting polynomial-root
theorem coverage in Mathlib: **not checked** in this step.

The floor-cell and conditional boundary statements are **present** in the
separate pinned ArkLib library as
[`ProximityGap.GrandChallenges.lambda_eq_of_floor_eq`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/GrandChallenges.lean#L359)
and
[`ProximityGap.GrandChallenges.GrandListResolution.sublevel_iff`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/GrandChallenges.lean#L427).
They support (3) once adjacent inequalities are known; they are not a match
for the support count, the explicit q^m witness, or the field condition (4).
