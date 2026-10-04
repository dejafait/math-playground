# L014 — Uniform upper bound for the rate-1/16 two-coefficient centers

## Hypotheses

Take the fixed rate-1/16 instance of L013: Q=65537, E=F_Q,
F=F_{Q^28}, H<=E^* of order n=1024, k=64, and m>=1. Messages in
each row have degree strictly less than k. Use the closed simultaneous
column-Hamming metric from the
[pinned model](../foundations/02-pinned-list-model.md), with epsilon*=2^-128.
For b,c in E let

\[
 Y_{b,c}(x)=(x^{66}-b x^{65}+c x^{64},0,\ldots,0),
 \quad
 N_H(66;b,c)=|\{S\subseteq H:|S|=66,
                     e_1(S)=b,\ e_2(S)=c\}|.
\]

## Conclusion

Put C=binomial(1024,66), D=binomial(579,66), and

\[
 U=\left\lfloor\frac{C+(Q^2-1)D}{Q^2}\right\rfloor.
\]

For every b,c in E and every m>=1, the entire list around Y_{b,c}
at radius 958/1024 has cardinality N_H(66;b,c), and

\[
 N_H(66;b,c)\le U<2^{317}<2^{320}
       <\varepsilon^*|F|=65537^{28}/2^{128}.             \tag{1}
\]

More precisely, uniformly in b,c,

\[
 \left|N_H(66;b,c)-C/Q^2\right|
       \le(1-Q^{-2})D.                                 \tag{2}
\]

Thus this entire center family supplies no unsafe witness at 66
agreements. This is not an upper bound for the maximum over arbitrary
received arrays. In particular it does not prove that the full code is
safe at error index 958 or locate t_star.

## Proof

**Known inputs and the authorized specialization.** The
[prior SPECIALIZE assessment](../drafts/literature/2026-10-04-rate-sixteenth-joint-fiber-upper-bound.md)
covers the present target. Import Lai, Marino, Robinson and Wan,
[Moment subset sums over finite fields, arXiv:1910.05894v2](https://arxiv.org/pdf/1910.05894v2#page=6),
2019-10-19, Proposition 1, printed p. 6: for a nontrivial additive
character and a nonconstant polynomial of degree r not divisible by the
characteristic, its sum on {x^d:x in E} has absolute value at most
r sqrt(Q), under (d+1)^2<=Q. Import also Li and Wan,
[Counting polynomial subset sums, arXiv:1507.06329v1](https://arxiv.org/pdf/1507.06329v1#page=5),
2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5, for the symmetric
weighted distinct-coordinate sieve; Lemma 2.7, p. 7, for its cycle
polynomial, and Lemma 3.1, pp. 8-9, for the Fourier/cycle factorization.
These are supporting results, not a full matching interleaved threshold
theorem. No sieve or character-sum theorem is reproved here.

The local work is deleting zero, checking all cycle lengths and both
moment coordinates, retaining the unordered normalization and comparing
effective constants with the ambient threshold. L013 already proves the
entire-center correspondence over F and for every m; that proof is reused.
This is REPRODUCTION, without a claim beyond the checked literature.

**Every nontrivial one-coordinate character sum.** The multiplicative
group of E is cyclic. Its unique subgroup of order 1024 is the image
of x -> x^64 on E^*, so the monomial image on E is H union {0}.
The character-estimate hypothesis holds since (64+1)^2=4225<=65537.
Fix the standard nontrivial character psi(t)=exp(2 pi i t/Q) on the
prime field E. For any (u,v)!=(0,0), the polynomial uX+vX^2 has degree
one or two, neither divisible by characteristic Q. Its value at zero is
zero, whose character value is one. Thus the imported proposition gives

\[
 \left|S(u,v)\right|
 :=\left|\sum_{x\in H}\psi(ux+vx^2)\right|
 \le 2\sqrt Q+1<514.                                  \tag{3}
\]

The strict final inequality follows by squaring: 4Q=262148<513^2=263169.
Replacing (u,v) by (ju,jv), for any 1<=j<=66, preserves nontriviality
because Q>66. Hence (3) holds for every character pair arising from a
sieve cycle; no cycle contributes an unexamined trivial character.

**Fourier coordinates and the weighted sieve.** In odd characteristic,

\[
 \sum_{x\in S}x^2=e_1(S)^2-2e_2(S).
\]

Thus fixing e_1=b,e_2=c is equivalent to fixing the first two power
sums at (b,b^2-2c). This coordinate change is bijective since 2 is
invertible in E. Additive character orthogonality gives, with A=66,

\[
 N_H(A;b,c)=\frac{1}{A!Q^2}
 \sum_{u,v\in E}\psi(-ub-v(b^2-2c))T(u,v),             \tag{4}
\]

where

\[
 T(u,v)=\sum_{\substack{x_1,\ldots,x_A\in H\\
                         x_i\ \text{pairwise distinct}}}
                \prod_{i=1}^A\psi(ux_i+vx_i^2).
\]

The divisor A! appears because each unordered subset has exactly A!
distinct orderings. At (u,v)=(0,0), T=(1024)_A and its contribution
in (4) is exactly C/Q^2.

For a nonzero pair, the imported weighted sieve expresses T as the sum
over permutations sigma in the symmetric group on A letters, with sign
(-1)^(A-number_of_cycles), of

\[
       \prod_{\text{cycles }\gamma\text{ of }\sigma}
                       S(|\gamma|u,|\gamma|v).
\]

The weight is symmetric and factors within each cycle, so the cited
identity applies on the arbitrary domain H, without a subfield-domain
assumption. By (3) and the triangle inequality its absolute value is at
most the cycle polynomial with every cycle weight 514. Lemma 2.7 gives

\[
 |T(u,v)|\le\sum_{\sigma}514^{\#\text{cycles}(\sigma)}
 =514\cdot515\cdots579=A!\binom{579}{66}=A!D.          \tag{5}
\]

In the cited characteristic correction, cycles divisible by Q cannot
occur because A<Q; this is why the constant-weight identity suffices.
There are Q^2-1 nonzero pairs, and each exterior phase in (4) has
absolute value one. Removing the trivial contribution and using (5)
proves (2), then integrality gives N_H<=U. No independence or exact
uniformity of the two coefficients was assumed.

**Exact threshold comparison.** Finite integer multiplication gives

\[
 C<2^{349},\qquad D<2^{293},\qquad
 C+(Q^2-1)D<Q^2\,2^{317}.                             \tag{6}
\]

For reproducibility, the two binomial integers in (6) are

```text
C = 1033124583102687354339403140244478613320805668860768156926529922156041313302689842574764646586401047354880
D = 8465305938258319483377548069142511894430704660788795080347702134232144415298207046605195
```

The executable integer certificate below verifies (6) directly and also
the threshold inequality after clearing all denominators:

\[
 2^{128}[C+(Q^2-1)D]<Q^{30}.                           \tag{7}
\]

Even without the sharper third comparison in (6), its first two give
C/Q^2+(1-Q^-2)D<2^317+2^293<2^318, already enough: Q>2^16 implies
Q^28/2^128>2^320. These are exact inequalities, not approximate
experiments or inferred counts. The sharper comparison proves (1).
The resulting integer U is

```text
240535729500077737188938388135433284866021113019746075708674243973732286501047597744182879688191
```

L013 now transfers the subset bound to the entire F-valued center list
for every m>=1. The source character field is E of size Q; the threshold
field remains F of size Q^28. Interleaving introduces no exponent m.

**Checks and limits.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_uniform_upper.py`.
Its exact certificate checks (3), (6)--(7), all cycle lengths, and an
independent rational upper bound for sqrt(Q). Results are saved in
`scripts/coefficient-fibers/uniform-upper-results.json`. The upper-to-threshold
ratio lies strictly between 11256/100000 and 11257/100000; this comparison
also uses exact rationals. No actual fiber on the 1024-point subgroup is
enumerated.

On an order-8 subgroup of F_17 with A=4, a separate exact group-algebra
calculation compares the signed permutation sieve with direct enumeration
of distinct tuples and unordered subsets at every moment pair. It checks
the coordinate signs, cycle multiplicities, A! factor and cycle polynomial.
This is a normalization check, not a substitute for the cited theorem or
for the fixed-instance threshold certificate. The global maximum over
centers and the sharper boundary remain unproved.

## Mathlib

Full uniform proper-subgroup/interleaved/ambient-threshold statement:
**not checked** in Mathlib. Formal coverage of the named monomial character
estimate, weighted sieve, cycle identity and Fourier count: **not checked**.
Supporting finite-field cyclicity, character orthogonality, elementary
symmetric identities and binomial arithmetic: **not checked**. The direct
primary links above support the scalar counting inputs, without claiming
a full matching library theorem. The pinned ArkLib definitions are
**present** as recorded in the model; they fix the metric and threshold
conventions and do not prove this upper bound.
