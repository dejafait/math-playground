# L013 — Two fixed coefficients and the next unsafe grid radius

## Hypotheses

Let F be a finite field of cardinality q, let E=F_Q be a subfield, and
let L consist of n distinct elements of E. Let 1<=k<=n-2 and m>=1;
messages have degree strictly less than k in every row. Use B_m and
closed simultaneous column-Hamming balls from the
[pinned model](../foundations/02-pinned-list-model.md). Put s=k+2, and
for b,c in E define

\[
 N_L(s;b,c)=|\{S\subseteq L:|S|=s,\ e_1(S)=b,\ e_2(S)=c\}|,
 \quad e_1(S)=\sum_{x\in S}x,\quad
 e_2(S)=\sum_{\{x,y\}\subseteq S}xy.
\]

The last sum is over unordered two-element subsets, without an ordering
of the field or any division by two. For the fixed instance take the
field and domain of C012a: Q=65537, F=F_{Q^28}, L=H of order 1024,
k=512,256,128,64, and epsilon*=2^(-128).

## Conclusion

For every b,c, the entire list at radius (n-k-2)/n around the single
received array

\[
 Y_{b,c}(x)=(x^{k+2}-b x^{k+1}+c x^k,0,\ldots,0)
\]

has cardinality exactly N_L(k+2;b,c), for every m>=1. Its candidates
are the evaluations of

\[
 \left(X^{k+2}-bX^{k+1}+cX^k-\prod_{x\in S}(X-x),
       0,\ldots,0\right),
 \quad |S|=k+2,\ e_1(S)=b,\ e_2(S)=c,                 \tag{1}
\]

and their simultaneous agreement sets are exactly S. Consequently,

\[
 \left\lceil\frac{\binom n{k+2}}{Q^2}\right\rceil
 \le\max_{b,c\in E}N_L(k+2;b,c)
 \le B_m((n-k-2)/n)
 \le\left\lfloor\frac{\binom nk}{\binom{k+2}k}\right\rfloor.
                                                               \tag{2}
\]

For the fixed instance let a_k=ceil(binomial(1024,k+2)/65537^2).
Exact integer comparisons give:

| k | Rate | Collision certificate a_k | Tested error index | Consequence |
| --- | --- | --- | --- | --- |
| 512 | 1/2 | 2^986 < a_k < 2^987 | 510 | Unsafe; t_star <= 509 |
| 256 | 1/4 | 2^796 < a_k < 2^797 | 766 | Unsafe; t_star <= 765 |
| 128 | 1/8 | 2^525 < a_k < 2^526 | 894 | Unsafe; t_star <= 893 |
| 64 | 1/16 | 2^316 < a_k < 2^317 | 958 | Lower certificate inconclusive |

The first three unsafe claims hold for every m>=1 at an existential
common coefficient pair. They move C012a's bound inward by one grid point.
At rate 1/16, (2)'s averaging certificate is strictly below the ambient
threshold; the previous t_star<=958 remains the established bound. No
upper bound on all two-coefficient fibers below that threshold, explicit
maximizing pair, or full-code sharp boundary is asserted.

## Proof

**Known mechanism and the local difference.** Li and Wan,
[On the subset sum problem over finite fields, arXiv:0708.2456v1](https://arxiv.org/pdf/0708.2456v1),
2007-08-18, Section 5, printed p. 15, give the scalar dictionary between
a degree-(k+d) received polynomial and distinct root subsets with its first
d elementary symmetric coefficients fixed. Ben-Sasson, Kopparty and
Radhakrishnan,
[Subspace Polynomials and List Decoding of Reed-Solomon Codes](https://www.math.utoronto.ca/swastik/rsld.pdf),
Section 1.3, p. 3, and Proposition 3.4, p. 6, give the known coefficient
collision and common-pivot construction. Gao,
[Counting polynomials over finite fields with prescribed leading coefficients and linear factors, arXiv:2105.12845v3](https://arxiv.org/html/2105.12845v3),
2022-11-10, Section 2, Proposition 1 and Theorem 1, supplies leading
coefficient classes and an arbitrary-domain counting framework. Its
Section 4 subfield-domain estimates are not applied to H.

The [prior SPECIALIZE assessment](../drafts/literature/2026-10-04-two-leading-coefficient-fibers.md)
covers precisely this construction, collision averaging and fixed-instance
test. Import the scalar mechanism; the verification below checks the
strict message degree, signs, restricted coefficient field, extension-field
messages and simultaneous interleaving. No sieve, new character-sum estimate
or uniformity claim is introduced. This is REPRODUCTION, with no claimed
advance beyond the checked literature.

**Three terms cancel.** For an s-element subset S, its monic root product
g_S has initial terms

\[
 g_S=X^{k+2}-e_1(S)X^{k+1}+e_2(S)X^k+
       \text{terms of degree less than }k.
\]

Indeed one constant factor contributes the negative subset sum; two
constant factors contribute the positive unordered pairwise-product sum.
When e_1=b and e_2=c, all three displayed terms cancel in (1). Its
first row has degree at most k-1 (with zero allowed), and the other rows
are zero, so this is a valid F-valued message. At a column x the difference
from Y_{b,c} has first entry g_S(x) and all other entries zero. The product
vanishes exactly on S, so the simultaneous agreement set is S and the
closed-ball distance is exactly (n-k-2)/n. Different subsets have a point
in their symmetric difference; their evaluation words therefore differ.

**Completeness of each center list.** Let (h_1,...,h_m), with all row
degrees less than k, agree with Y_{b,c} on at least s columns. The monic
degree-s polynomial

\[
 X^{k+2}-bX^{k+1}+cX^k-h_1
\]

vanishes on those columns. The factor theorem and nonzero-polynomial root
bound used in L001 imply exactly s distinct agreement columns, say S,
and force this polynomial to equal g_S. Matching the next two coefficients
gives e_1(S)=b and e_2(S)=c. Each h_j for j>=2 vanishes on S, whose
size exceeds its degree, so h_j=0. Thus the candidate is exactly (1).
Although messages range over F, h_1 is now forced by coefficients in E;
the extension introduces no additional candidates at this center. The
center-list size is N_L(s;b,c) independently of m, without an exponent m.

**Collision count and upper comparison.** All root-product coefficients
lie in E. Partition the binomial(n,s) subsets by their pair (e_1,e_2)
among Q^2 possible pairs. Some class has at least ceil(binomial(n,s)/Q^2)
members, whether or not every pair is attained. This single class gives
one common center; lists from different centers have not been combined.
The exact center correspondence proves the first three terms in (2).
L001's common-k-support bound, at n-t=s, proves the last term. No
independence between the coefficients or uniform distribution is assumed.

**The first three rates pass the actual threshold.** C012a establishes
the admissible proper subgroup and prime subfield in F, and

\[
 2^{320}<\varepsilon^*q=65537^{28}/2^{128}<2^{321}.
                                                               \tag{3}
\]

For k=512,256,128, reflection s -> 1024-s puts s=k+2 at 510,258,130.
Each lies between 128 and 512, where binomial(1024,s) is nondecreasing
in s: the consecutive ratio is (1024-s)/(s+1), at least one before
the midpoint. Hence binomial(1024,k+2)>=binomial(1024,128).
Partition 1024 labelled points into 128 blocks of eight; choosing one
point from each gives 8^128 distinct 128-subsets. Therefore

\[
 \binom{1024}{k+2}\ge\binom{1024}{128}\ge 8^{128}=2^{384}.
\]

Since Q<2^17, (2) gives, uniformly at these three rates,

\[
 a_k\ge\binom{1024}{k+2}/Q^2>2^{350}
       >2^{321}>\varepsilon^*q.
\]

This suffices for unsafety without the sharper exponents in the table.
Safety exists at zero by (3). Monotonicity and L001's boundary convention
then give t_star<=n-k-3, namely 509,765,893. The coefficient pair is
guaranteed to exist by finite averaging; its coordinates are not computed.

**The rate-1/16 averaging certificate fails.** Now s=66. Direct integer
multiplication gives 66!>2^308; for complete reproducibility these integers
are respectively

```text
544344939077443064003729240247842752644293064388798874532860126869671081148416000000000000000
521481209941628438084722096232800809229175908778479680162851955034721612739414196782949728256
```

All but the first factor of product_{j=0}^{65}(1024-j) are less than
1024. Thus

\[
 \binom{1024}{66}<\frac{1024^{66}}{66!}<2^{352},
 \qquad Q^2>2^{32},\qquad
 a_{64}=\left\lceil\binom{1024}{66}/Q^2\right\rceil
       \le 2^{320}<\varepsilon^*q.                     \tag{4}
\]

The ceiling inequality holds because 2^320 is an integer larger than
the unrounded average. This stops the bare Q^2-class lower certificate
at rate 1/16. It does not show that any actual fiber is below the threshold,
that the tested radius is safe, or that another center cannot be unsafe.
The coefficient-family upper question remains separate from the full-code
upper question. Equality with epsilon* q would be safe under the inclusive
convention; every unsafe claim above uses a strict comparison.

**Exact checks.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_two_coefficients.py`.
Its integer arithmetic checks (3)--(4), the symbolic inequalities for
the first three rates and the sharper brackets in the table. It computes
binomial integers and ceilings, not exact fibers on the 1024-point domain.
Output is saved in `scripts/coefficient-fibers/two-coefficient-results.json`.

On the proper order-16 subgroup <8> of F_97, the script enumerates the
joint fibers at s=k+2 for k=8,4,2,1. It reconstructs candidates by
Lagrange interpolation on only k received values, independently of
root-product subtraction, and verifies distinctness, exactly s agreement
columns and widths 1 and 3. The largest fibers there have sizes 5,5,4,2.
Scalar-message exhaustion at k=1,2 checks selected entire center lists;
width-two message exhaustion at k=1 checks the common-column count.
Nonzero coefficient pairs test both signs. These small checks corroborate
the applicability proof; neither this field nor its exact counts replace
the stated ambient instance. No extension field is enumerated.

## Mathlib

Full two-coefficient/common-center/ambient-threshold statement: **not
checked** in Mathlib. Formal coverage of the cited scalar coefficient
dictionary, leading-coefficient classes and collision construction: **not
checked**. Supporting coefficient, root, finite-field/subfield, binomial
and pigeonhole results: **not checked**. The direct primary links above
support scalar inputs, without claiming a full matching library theorem.
The pinned ArkLib definitions are **present** as recorded in the model;
they fix conventions and do not establish (1)--(4).
