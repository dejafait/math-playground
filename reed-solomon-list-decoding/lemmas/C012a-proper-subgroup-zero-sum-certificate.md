# C012a — A zero-sum list on a proper smooth subgroup

## Hypotheses

Let Q=65537, E=F_Q and F=F_{Q^28}, with E identified with the prime
subfield of F. Let H be the subgroup of E^* of order n=1024 and put
L=H. Let k be one of 512,256,128,64, and let m>=1. Messages have row
degree strictly less than k. Use B_m and closed simultaneous column-Hamming
balls from the [pinned model](../foundations/02-pinned-list-model.md), with
epsilon*=2^(-128). All field sizes in the safety threshold are ambient:
q=Q^28.

## Conclusion

At the explicit common center Y_0(x)=(x^(k+1),0,...,0), its entire list
with at least k+1 simultaneous agreements has cardinality M_H(k+1,0),
and

\[
 B_m((1024-k-1)/1024)\ \ge M_H(k+1,0)>2^{322}
 >\varepsilon^*q,\qquad
 2^{320}<\varepsilon^*q<2^{321}.                         \tag{1}
\]

Thus this grid radius is unsafe for every m, and the largest safe grid
index exists and satisfies

| k | Rate | Unsafe error index | Upper bound on t_star |
| --- | --- | --- | --- |
| 512 | 1/2 | 511 | 510 |
| 256 | 1/4 | 767 | 766 |
| 128 | 1/8 | 895 | 894 |
| 64 | 1/16 | 959 | 958 |

This is a lower certificate at one center on a proper subgroup, not an
exact fiber count, an upper bound for all centers, or the sharp boundary.

## Proof

**Imported result and local difference.** Zhu and Wan,
[An Asymptotic Formula For Counting Subset Sums Over Subgroups Of Finite
Fields, arXiv:1101.0289v1](https://arxiv.org/pdf/1101.0289v1), dated
2010-12-31, Theorem 1.1, p. 2, give the following zero-sum estimate for
unordered s-element subsets of H<=F_Q^*, of index i and characteristic p:

\[
 \left|M_H(s,0)-\frac{1}{Q}\binom{(Q-1)/i}{s}\right|
 \le\binom{\sqrt Q+s+Q/(ip)}s,\qquad 1\le s\le |H|.     \tag{2}
\]

Here the generalized binomial means
product_(j=0)^(s-1)(u-j)/s! at top argument u. No counting sieve is
reproved. The [prior SPECIALIZE assessment](../drafts/literature/2026-10-03-root-product-one-more-agreement.md)
already covers this instance application. Li-Wan's exact full-nonzero-field
formula is inapplicable to the proper H and is not used. Corollary 4.5's
tighter error is also unnecessary. L012 supplies the entire common-center
list correspondence, including extension-field messages and every m.
The remaining work is the effective comparison of (2) with the actual
ambient threshold. This is a reproduction of known mathematics, with
no claimed progress beyond the checked literature.

**Admissible field and domain.** For completeness, primality and the
subgroup can be checked without assuming an unrecorded field instance.
Successive residues 3^(2^j) modulo N=65537, for j=0,...,15, are

```text
3, 9, 81, 6561, 54449, 61869, 19139, 15028,
282, 13987, 8224, 65529, 64, 4096, 65281, 65536.
```

Each entry is the square of its predecessor modulo N, so
3^32768=-1 modulo N. Any prime divisor r of N is odd and differs from
3. The order of 3 modulo r divides 65536 and does not divide 32768,
hence equals 65536. Lagrange's theorem gives 65536 | r-1, forcing
r>=65537=N. Thus N is prime. Standard finite-field existence gives F
and its prime subfield E. The element g=3^64=19139 in E satisfies
g^1024=1 and g^512=-1, so its order is exactly 1024. It generates H,
whose index in E^* is i=64. The domain is therefore a proper subgroup
coset of power-of-two order, with all four pinned rates admissible.

**A uniform lower count.** Put s=k+1, so s is 513,257,129 or 65, and
write C_s=binomial(1024,s) and U_s=binomial(s+258,s). Here p=Q, and
Q/(ip)=1/64. Since sqrt(Q)<257 and 1/64<1, the top argument in (2)
is less than s+258. All its product factors are positive, and each
increases with that argument. Thus (2) gives

\[
 M_H(s,0)\ge C_s/Q-U_s.                                 \tag{3}
\]

For 0<=j<s, since s+258<=771<1024,

\[
 \frac{s+258-j}{1024-j}\le\frac{s+258}{1024}<\frac45.
\]

Consequently

\[
 \frac{U_s}{C_s}
 =\prod_{j=0}^{s-1}\frac{s+258-j}{1024-j}
 <(4/5)^s\le(4/5)^{65}
 <3^{-12}<\frac{1}{2Q}.                                 \tag{4}
\]

For the penultimate inequality, 9*4^10=9437184<9765625=5^10
gives (4/5)^60<9^(-6)=3^(-12), and the remaining fifth power is
less than one. Finally 3^12=531441>131074=2Q. These are strict
comparisons, rather than a positivity-only application of the source.

The binomial coefficients binomial(1024,s) increase through s=512;
the value at 513 equals the value at 511. Hence C_s>=C_65 for all
four s. The elementary integer comparisons 65!<2^303 and
15^32>2^125 imply

\[
 C_{65}
 =\frac{\prod_{j=0}^{64}(1024-j)}{65!}
 \ge\frac{960^{65}}{65!}
 =\frac{2^{390}15^{65}}{65!}>2^{340}.                     \tag{5}
\]

Indeed 15^65=(15^32)^2*15>2^253, so the numerator exceeds
2^643. The two integer comparisons in (5) follow by multiplication;
the verification script reproduces them exactly. Since 2Q<2^18,
(3)--(5) give M_H(s,0)>C_s/(2Q)>2^322.

**Ambient threshold and radius.** The threshold is

\[
 \varepsilon^*q=2^{320}(1+2^{-16})^{28}.
\]

It is greater than 2^320. For x=2^(-16), binomial(28,j)<=28^j and
28x<1/2, so

\[
 (1+x)^{28}\le\sum_{j=0}^{28}(28x)^j
 <\frac{1}{1-28x}<2.
\]

Thus epsilon* q<2^321<2^322<M_H(s,0). L012 identifies that fiber
with the complete list at Y_0 for messages over F, independently of m.
The domain count uses Q, while the safety test uses q=Q^28. L001
gives existence of a safe index since epsilon* q>1; monotonicity and
the unsafe index n-k-1 then imply t_star<=n-k-2, yielding the table.
The strict inequality certifies unsafety; equality with epsilon* q
would remain safe under the inclusive convention.

**Exact-arithmetic verification.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_subgroup_threshold.py`.
The script checks the primality/order certificate, all integer comparisons
in the uniform proof and the per-rate ambient threshold comparisons. It
also bounds sqrt(Q) by 256+1/512, whose square is greater than Q, and
evaluates (2)'s generalized binomial with this rational upper argument.
This checks a sharper error independently of the coarse U_s used above.
Results are saved in `scripts/coefficient-fibers/subgroup-threshold-results.json`.
These finite integer/rational calculations check arithmetic in the proof;
they neither enumerate the extension field nor replace the cited theorem
with empirical list estimates.

## Mathlib

Full proper-subgroup/common-center/ambient-threshold certificate: **not
checked** in Mathlib. Formal coverage of Zhu-Wan Theorem 1.1: **not
checked**. Supporting finite-field, element-order and binomial results:
**not checked**. The named theorem and direct primary link above support
the subset-count input, not a full matching interleaved theorem. The
pinned ArkLib definitions are **present** as recorded in the model;
they specify the domain and metric but do not prove this count.
