# L019 — A pole-at-zero sum/product fiber excludes error index 958

## Hypotheses

Use the admissible instance of C012a: Q=65537, E=F_Q embedded in
F=F_(Q^28), H<=E^* of order n=1024, k=64, and epsilon*=2^(-128).
Let m>=1 and let every message row have degree strictly less than k.
Use closed simultaneous column-Hamming balls and B_m from the
[pinned model](../foundations/02-pinned-list-model.md). Set A=k+2=66.
For b in E and d in H, define

\[
 N(b,d)=|\{S\subseteq H: |S|=66,\ \sum_{a\in S}a=b,
                                      \prod_{a\in S}a=d\}|,
 \qquad Y_{b,d}(x)=(x^{65}-bx^{64}+d/x,0,\ldots,0).
\]

The received array is defined only on H; zero is excluded, so division
by x is valid. No polynomial-degree restriction applies to a received word.

## Conclusion

The entire list around Y_(b,d) with at least 66 simultaneous agreements
has cardinality N(b,d). Its candidates are precisely the evaluations of

\[
 (h_S,0,\ldots,0),\qquad
 h_S(X)=\frac{X^{66}-bX^{65}+d-\prod_{a\in S}(X-a)}{X},
                                                               \tag{1}
\]

for the subsets counted by N(b,d). Each h_S is in E[X], has degree
at most 63, and agrees at exactly S. In particular, for every m>=1,

\[
 B_m(958/1024)\ \ge\max_{b\in E,d\in H}N(b,d)
 \ge\left\lceil\frac{\binom{1024}{66}}{65537\cdot1024}\right\rceil
 >2^{322}>\varepsilon^*|F|.                              \tag{2}
\]

Thus error index 958 is unsafe and the largest safe grid index satisfies
t_star<=957 at rate 1/16. The lower certificate is between 7.204 and
7.205 times the actual threshold. A maximizing pair (b,d) is not computed.
This is neither an exact maximum list nor a sharp-boundary resolution.

## Proof

**Known inputs and the specialization.** Gao, Kuttner and Wang,
[Counting Irreducible Polynomials with Prescribed Leading and Ending
Coefficients, arXiv:2109.02000v1](https://arxiv.org/html/2109.02000v1#S2),
2021-09-05, Section 2 Type I and Proposition 1, supply the known
leading/ending coefficient framework for nonzero constant terms.
Gao, [arXiv:2105.12845v3](https://arxiv.org/html/2105.12845v3#S2),
2022-11-10, Section 2 Proposition 1 and Theorem 1, supplies
leading-coefficient classes and root-factor counting. These are supporting
scalar mechanisms, not a theorem matching (2) on a proper subgroup.

The [prior SPECIALIZE assessment](../drafts/literature/2026-10-04-pole-at-zero-sum-product.md)
covers exactly this elementary construction and threshold comparison.
Following the coefficient-collision mechanism of L013, the difference
here is multiplication by X, cancellation of the constant term before
division, and a product restricted to H. The checked rational-distance
theorem excludes a denominator vanishing at zero and is not used.
No general coefficient-class theorem is reproved, no unread quantitative
source is assumed, and no character-sum or uniform-fiber estimate is needed.
This is REPRODUCTION of known methods with changed-hypothesis checks;
no originality is claimed for the finite certificate.

**Cancellation and exact agreement.** Write
g_S(X)=product_(a in S)(X-a). Because |S|=66 is even,

\[
 g_S=X^{66}-\left(\sum_{a\in S}a\right)X^{65}
       +\text{terms of degree at most }64,
 \qquad g_S(0)=\prod_{a\in S}a.
\]

The sum lies in E and the product lies in the multiplicative subgroup H.
For a subset in the fiber (b,d), the two leading terms in (1)'s
numerator cancel. Its degree is therefore at most 64. Its constant
term is d-g_S(0)=0, so it is divisible by X in E[X]. The quotient has
degree at most 63; the zero polynomial is allowed. It is a valid message
over F, and at every x in H,

\[
 x^{65}-bx^{64}+d/x-h_S(x)=g_S(x)/x.
\]

Since x!=0 and g_S is a product of the distinct factors from S, this
difference vanishes exactly at S. With zero remaining rows, its
simultaneous agreement set is exactly S and its distance is 958/1024.
If S and T differ, a point in their symmetric difference is an agreement
column for exactly one candidate at this same center. Their evaluation
words are distinct. We have not combined lists from different centers.

**Completeness, including ambient-extension messages.** Suppose a tuple
(f_1,...,f_m) of polynomials in F[X], with row degrees at most 63,
agrees with Y_(b,d) simultaneously on at least 66 columns. Then

\[
 G(X)=X^{66}-bX^{65}+d-Xf_1(X)
\]

is monic of degree 66 and vanishes on every agreement column. The factor
theorem and nonzero-polynomial root bound, as used in L001, imply that
there are exactly 66 such roots, say S, and G=g_S. Comparing the X^65
coefficient gives sum S=b, since deg(Xf_1)<=64. Comparing constants
gives product S=d. Hence f_1=h_S, forcing its coefficients into E
even though the original message was allowed over F. Every other row
vanishes at those 66 points and has degree at most 63, so it is zero.
The resulting tuple agrees exactly at S. Thus the entire list has size
N(b,d), independently of m; no exponent m arises.

**A smaller class space passes the actual threshold.** Partition all
binomial(1024,66) subsets by (sum S, product S) in E times H. This space
has Qn=65537*1024 elements, not Q^2. Some single fiber therefore has
at least ceil(binomial(1024,66)/(Qn)) members. This uses only finite
pigeonhole counting; no independence, surjectivity or uniformity of
the two statistics is assumed. It proves the first two inequalities
of (2) and produces an existential common center.

Here is the exact integer binomial used for the comparison:

```text
binomial(1024,66) =
1033124583102687354339403140244478613320805668860768156926529922156041313302689842574764646586401047354880
```

Direct integer multiplication (also checked in the saved script) gives

\[
 2^{348}\,66!<\prod_{j=0}^{65}(1024-j)<2^{349}\,66!,
 \qquad
 2^{322}<\left\lceil\binom{1024}{66}/(65537\cdot1024)\right\rceil
          <2^{323}.                                    \tag{3}
\]

C012a establishes the admissible field/subgroup and the ambient bound
2^320<epsilon*|F|=65537^28/2^128<2^321. Equations (2)--(3) give a
strictly unsafe list at error index 958 for every m. L001's zero-radius
count and epsilon*|F|>1 ensure a safe grid index exists; monotonicity
then gives t_star<=957. The earlier bounds at the other rates are not
changed by this rate-1/16 calculation. Equality with the threshold
would be safe, but here all required comparisons are strict.

The former two-leading-coefficient lower certificate used Q^2 classes.
Replacing that divisor by Qn improves the unrounded average by Q/n,
without any estimate of fiber variation. The rational center is a
different received word, so the degree-66 polynomial-family stop of
L014 does not apply. Neither the degree-67 family nor arbitrary-center
upper bounds are settled by this new unsafe witness.

**Exact and independent checks.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_pole_at_zero.py`.
It saves full certificates in
`scripts/coefficient-fibers/pole-at-zero-results.json` and prints a short
summary. Exact integer/rational arithmetic verifies (3), the ceiling,
the strict ambient comparison, and 7.204<lower/threshold<7.205.
It does not enumerate large-domain fibers or an extension field.

On the proper order-16 subgroup of F_97, it enumerates sum/constant-term
fibers for k=8,4,2,1. Selected candidate messages are independently
reconstructed by interpolation on k received values, then compared with
the root-product quotient. Their maximum fiber sizes are 9,9,4,2.
The script checks cancellation, distinct words, exact agreement sets,
widths 1 and 3, exhaustive scalar messages for k<=2, and exhaustive
width-two constant messages for k=1. An auxiliary order-5 subgroup of
F_31 checks the constant-term parity sign when -1 is outside the
subgroup; the signed product then lies in (-1)^(k+2)H. These small
checks support the algebraic argument and do not supply the large-instance
lower bound. The extension-field assertion rests on the completeness
proof above, not numerical enumeration.

**Critical audit, 2026-10-05.** A separate proof audit found no change
needed in the cancellation, exact agreement, injectivity, extension-field
completeness or simultaneous-row arguments. Only the field/domain and
threshold portions of C012a are needed here, not its character estimate;
L013 is a comparison of mechanisms, not an additional premise. The
displayed DAG inputs L001 and C012a therefore suffice. The original
verifier was rerun and its complete fixed-instance and small-case evidence
inspected. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/audit_pole_at_zero.py`
for an independent Pascal-addition computation of the binomial, Euclidean
division for the ceiling and repeated multiplication for the ambient
size. Its 14 exact comparisons pass; full values and the positive strict
comparison margin are in `scripts/coefficient-fibers/pole-at-zero-audit-results.json`.
This confirms the existing bound without establishing a new one. It does
not compute a maximizing center, prove safety at 67 agreements, or resolve
the outstanding comparison of the pinned model with the ABF source.

## Mathlib

Full pole-at-zero/sum-product/ambient-threshold statement: **not checked**
in Mathlib. Formal coverage of the cited Type I coefficient framework:
**not checked**. Supporting factor theorem, polynomial root bound,
subfield/subgroup closure, finite pigeonhole and binomial arithmetic:
**not checked**. The direct primary links above support known scalar
frameworks, without claiming a full matching theorem. The pinned ArkLib
definitions are **present** as recorded in the model; they fix the list,
domain and simultaneous-agreement conventions, not the new certificate.
