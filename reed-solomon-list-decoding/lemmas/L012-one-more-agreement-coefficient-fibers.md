# L012 — One more agreement through a fixed coefficient fiber

## Hypotheses

Let F be a finite field of cardinality q, let L consist of n distinct
evaluation points, and let 1 <= k < n and m >= 1. Messages have row degree
strictly less than k. Use B_m and closed simultaneous column-Hamming balls
from the [pinned model](../foundations/02-pinned-list-model.md). Put s=k+1
and, for b in F, define

\[
 M_L(s,b)=|\{S\subseteq L:|S|=s,\ \sum_{x\in S}x=b\}|.
\]

Where a subfield is used, assume E=F_Q is a subfield of F, H is a
multiplicative subgroup of E's units of order n, and L=aH with a in F
nonzero. The pinned smooth cases have n a power of two, n>=16 and
k=n/2,n/4,n/8 or n/16. Fix 0<epsilon<1 when comparing thresholds.

## Conclusion

For every b, the entire list at radius (n-k-1)/n around the single array

\[
 Y_b(x)=(x^{k+1}-b x^k,0,\ldots,0)
\]

has cardinality exactly M_L(k+1,b), for every m>=1. Its candidates are

\[
 \left(X^{k+1}-bX^k-\prod_{x\in S}(X-x),0,\ldots,0\right),
 \qquad |S|=k+1,\quad \sum_{x\in S}x=b,                 \tag{1}
\]

evaluated on L, with exactly k+1 simultaneous agreement columns. In
particular, L001's upper bound gives

\[
 \max_b M_L(k+1,b)\le B_m((n-k-1)/n)
 \le\left\lfloor\frac{\binom nk}{k+1}\right\rfloor.    \tag{2}
\]

For L=aH in the subfield setting,

\[
 M_{aH}(s,ac)=M_H(s,c)\quad(c\in E),\qquad
 B_m((n-k-1)/n)\ge\left\lceil\frac{\binom ns}{Q}\right\rceil.
                                                               \tag{3}
\]

Fibers outside aE are empty. E=F and a=1 always give the corresponding
q-denominator averaging bound for a multiplicative subgroup. The threshold
still uses the ambient q, even when Q is smaller.

If H=E^*, the exact fiber counts are the named Li-Wan theorem below. Let
p=char(E), j=floor(s/p), C=binomial(Q-1,s),
c_0=binomial(Q/p-1,j), and eta=(-1)^(s+j). Then

\[
 M_H(s,0)=\frac{C+\eta(Q-1)c_0}{Q},\qquad
 M_H(s,c)=\frac{C-\eta c_0}{Q}\quad(c\ne0).            \tag{4}
\]

A fixed admissible instance is F=F_{17^{32}}, E=F_17, L=E^*, n=16,
epsilon=2^(-128), and arbitrary m>=1. The largest coefficient fibers and
L001's upper bounds at this radius are

| k | Rate | b attaining the fiber | Exact list at Y_b | Upper bound for B_m |
| --- | --- | --- | --- | --- |
| 8 | 1/2 | 1 | 673 | 1430 |
| 4 | 1/4 | 1 | 257 | 364 |
| 2 | 1/8 | 1 | 33 | 40 |
| 1 | 1/16 | 0 | 8 | 8 |

All four listed centers are unsafe because

\[
 1<\epsilon q=\frac{17^{32}}{2^{128}}
     =\left(\frac{17}{16}\right)^{32}<8.               \tag{5}
\]

L001 therefore supplies an existing largest safe grid index and yields
t_star<=n-k-2 in all four cases. This excludes one additional grid point
inside the endpoint. No general equality in the left side of (2), sharp
boundary below this excluded point, or ABF26 equivalence is asserted.

## Proof

**Known result and local difference.** Li and Wan, [On the subset sum
problem over finite fields, arXiv:0708.2456v1](https://arxiv.org/pdf/0708.2456v1),
2007-08-18, Theorem 1.2, p. 2, supply (4) for unordered subsets of E^*.
Their Section 5, pp. 14-15, especially the coefficient/factorization passage
on p. 15, relates root subsets and matching leading coefficients on
arbitrary scalar evaluation sets. Ben-Sasson, Kopparty and Radhakrishnan,
[Subspace Polynomials and List Decoding of Reed-Solomon Codes](https://www.math.utoronto.ca/swastik/rsld.pdf),
Section 1.3, p. 3, and Proposition 3.4, p. 6, give the known
high-coefficient/common-pivot construction. These are supporting scalar
results; none is imported as the full pinned interleaved statement.

The [prior SPECIALIZE assessment](../drafts/literature/2026-10-03-root-product-one-more-agreement.md)
covers precisely the strict degree, prescribed-domain, coset/subfield,
simultaneous-column and ambient-threshold checks below. We import (4)
without redoing the counting sieve. The construction and elementary
averaging are reproduced for these applicability differences; no novelty
or progress beyond the checked literature is claimed.

**The coefficient sign and strict degree.** For an s-element subset S,
g_S=product over x in S of (X-x) is monic of degree k+1. Its X^k
coefficient is -sum(S): in expanding the product, exactly one constant
term must be selected to obtain degree k. Thus sum(S)=b makes both the
X^(k+1) and X^k terms cancel in X^(k+1)-bX^k-g_S. The resulting f_S
has degree at most k-1, with zero allowed, and all its coefficients
belong to the given F. The remaining rows in (1) are zero. This is a
valid message tuple without changing the code or its field.

At a column x in L, Y_b minus this tuple has first coordinate g_S(x)
and zero in every other coordinate. A product of field elements is zero
exactly when a factor is zero, so simultaneous agreement is exactly S.
The distance is (n-k-1)/n, including the boundary of the closed ball.
If S and T differ, a point in their symmetric difference gives a zero
for exactly one root product and hence different evaluation words.
There are M_L(s,b) distinct tuples at this one common center.

**There are no additional candidates at this center.** Suppose
(h_1,...,h_m) has degree less than k in every row and agrees with Y_b
on at least s columns. The monic degree-s polynomial
X^(k+1)-bX^k-h_1 vanishes on its simultaneous agreement set. By the
factor theorem and the nonzero-polynomial root bound (as proved in
L001), that set has exactly s points, say S, and the polynomial equals
g_S. Matching the X^k coefficients forces sum(S)=b. For j>=2, h_j
vanishes on these s>=k columns and has degree less than k, so h_j=0.
The candidate is exactly (1). This proves the exact center-list count
for every width; there is no product or power m in it. L001 at
t=n-k-1 has denominator binomial(k+1,k)=k+1, proving (2).

**Cosets, subfields and averaging.** Multiplication by a is a bijection
H -> aH and on their s-element subsets. It sends a sum c in E to ac in
F, giving the first identity in (3). All subset sums lie in aE, which
has Q elements even if a does not lie in E. There are binomial(n,s)
subsets, so at least one of these Q fibers has cardinality at least
ceil(binomial(n,s)/Q). Combining with the exact center construction
proves the second assertion in (3). A fiber outside aE is empty.

The construction counts messages over F, not only over E. The preceding
exact-list argument shows that any F-valued message agreeing on s points
is still the polynomial forced by that root product (and its other rows
are zero). Passing to the ambient extension introduces no extra candidates
at Y_b and does not change the fiber count. It does increase epsilon q;
using epsilon Q instead would give the wrong threshold.

**Imported count and fixed instance.** When H=E^*, apply Li-Wan's
Theorem 1.2 directly with subset cardinality s. Its v(0)=Q-1 and
v(c)=-1 for c!=0 give exactly (4). No arbitrary subgroup is substituted
for E^* in that theorem.

For E=F_17 the four cardinalities s are 9,5,3,2, all less than p=17.
Hence j=0, c_0=1 and eta=(-1)^s. The binomial values C are
11440,4368,560,120. For the first three, each nonzero-sum fiber has
(C+1)/17 elements, namely 673,257,33; the zero-sum fibers have
(C-16)/17 elements, namely 672,256,32. For s=2 the zero-sum fiber is
(120+16)/17=8 and the nonzero-sum fibers are (120-1)/17=7.
These give the maximizing b and exact lists in the table. The upper
column is simply floor(binomial(16,k)/(k+1)) from L001.

The standard existence of finite fields gives F_{17^{32}} with its prime
subfield E. E^* has order 16, so L=E^* is precisely a multiplicative
subgroup coset in F of power-of-two size n=16. All four k meet the
pinned smooth requirements. The lower inequality in (5) follows from
17>16. For the upper inequality, direct integer multiplication gives
3*17^8=20927272323<21474836480=5*16^8. Therefore
(17/16)^8<5/3, and raising to the fourth power gives
(17/16)^32<625/81<8. This proves (5) by exact arithmetic.
Each table count is at least 8, so (5) strictly violates the inclusive
safety threshold. Safety exists at zero since epsilon q>1. By L001,
monotonicity and the unsafe index n-k-1, the largest safe index satisfies
t_star<=n-k-2. The exact counts certify unsafety only: a lower bound at
or below epsilon q could not certify safety. Equality in the safety
condition remains safe and is not used here.

This is a local reproduction at one further agreement level, with an
explicit ambient-field instance. It leaves the general smaller-field
boundary, nonlinear covers and the parked primary-source comparison
unresolved; it is not a complete candidate resolution.

**Computational corroboration.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify.py`.
It enumerates subset sums over F_17^* to check the imported counts,
and reconstructs candidates by Lagrange interpolation on only k of
their agreement columns, independently of root-product subtraction.
It also checks a nontrivial smooth coset 2<8> in F_97, including the
rescaling of every coefficient fiber, and widths 1 and 3. The cryptographic
threshold comparison uses exact integer/rational arithmetic. All checks
passed; results are saved in `scripts/coefficient-fibers/results.json`.
On the F_97 coset the largest fibers have sizes 144,61,11,8 at these
four rates; these are finite corroboration, not a general subgroup formula.
Exhaustive scalar-message checks at k=1,2 confirmed that the respective
center lists contain no other candidates. Finite checks corroborate the
symbolic proof; the extension field itself is not enumerated.

## Mathlib

Full coefficient-fiber/common-center result with simultaneous interleaving
and the specified smooth-domain threshold instance: **not checked** in
Mathlib. Supporting coefficient, factor, root and finite-field/subfield
results: **not checked**. Formal versions of the cited Li-Wan and
common-pivot statements: **not checked**. Their direct links above support
the scalar inputs, without asserting a full matching library theorem.
The pinned ArkLib definitions are **present** as recorded in the model;
they fix the conventions and do not establish (1)--(5).
