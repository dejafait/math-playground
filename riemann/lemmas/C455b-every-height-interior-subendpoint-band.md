# Corollary 455b: every-height interior subendpoint band

## Hypotheses

Use the actual theta transform Ξ and the coefficients defined by
Ξ(a+iy)Ξ(a−iy)=Σ_{j≥0}D_j(Ξ;a)y^(2j). Retain C455a's pinned
external premise: the zeta specialization of OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Nonvanishing is asserted only on Re(s)>7/8, allowing the pole at 1.
The manuscript proof and formal import closure remain unaudited locally;
see the [external-input register](../foundations/2026-10-quasi-riemann-input.md).
This corollary imports C455a conditionally and does not reprove that input.

Let a>2π be real and n a positive integer with

    (249/1024)log(a/(2π))≤n≤(251/1024)log(a/(2π)).       (1)

Set R=log(a/(2π))/2 and m=2n. Define r>0 by the exact equation

    4π²exp(4r)=a²+(9/2+n/r)².                         (2)

Put h=9/2+n/r, τ=arctan(a/h)/2, Φ_*=m log r+9r−h−2aτ,
C₀=(8π²)², σ=(1+m/r)/2 and

    B=|ζ(σ+ia)|²,
    P=[2^(m−1)/m!]C₀exp(Φ_*)π/a.

## Conclusion

Equation (2) has exactly one positive solution. There are fixed
positive constants A,C,C_B such that for every real a≥A and every
integer n satisfying (1),

    31/32≤m/r≤63/64,
    |D_n(Ξ;a)/(P B)−1|≤C r^(−1/6),                    (3)
    D_n(Ξ;a)/P≥B/2≥(1/2)exp(−C_B r^(1/3))>0.         (4)

The constants and real-height onset are independent of n. The error
in (3) is also O((log(a/(2π)))^(−1/6)), uniformly in (1).
The complete sector/cutoff error remains negligible relative to (4).
All normalizations and the non-Euler lower bound are unchanged from
C455a. Constants and onset are existential, not numerically evaluated.

This is a local REPRODUCTION using an already audited conditional
input. The separate critical audit below validates the transfer. It is a partial sign band,
not a complete candidate for RH or an exclusion of any new zero range.

## Proof

The [prior coverage assessment](../drafts/literature/2026-10-23-subendpoint-every-height-interior-band-coverage.md)
approves exactly this parameter transfer. The existence argument is the
elementary monotone-crossing method used in L269; no proportional-index
asymptotic or contour estimate from that lemma is needed. We give the
argument explicitly to verify its hypotheses at these smaller indices.

For fixed a,n>0, the difference

    F(r)=4π²exp(4r)−a²−(9/2+n/r)²

is continuous on (0,∞), tends to −∞ as r→0+, and tends to +∞ as
r→∞. Moreover

    F'(r)=16π²exp(4r)+2(9/2+n/r)n/r²>0.

The intermediate value theorem and strict monotonicity prove existence
and uniqueness. Taking logarithms of (2) yields the exact identity

    r=R+(1/4)log(1+h²/a²)>R.                          (5)

In particular the solution recovers precisely the height in C455a:
a=sqrt(4π²exp(4r)−h²)>0, with h=9/2+m/(2r).
There is no height approximation in this substitution.

Rewrite (1) as

    (249/512)R≤n≤(251/512)R,
    (249/256)R≤m≤(251/256)R.                          (6)

Since r>R>0, it follows that

    9/2<h≤9/2+251/512=2555/512<5.

Using log(1+x)≤x for x≥0 in (5) therefore gives

    0<r−R≤25/(4a²).                                  (7)

Take a≥100 and R≥1. These two elementary restrictions suffice for
both closed-band inclusions. Indeed

    m/r≤(251/256)R/r≤251/256<252/256=63/64.

For the lower inclusion, (6)–(7) give

    m/r≥(249/256)R/(R+25/(4a²))≥248/256=31/32,         (8)

where the last inequality is equivalent to R≥1550/a². That inequality
holds because R≥1 and a≥100 imply 1550/a²≤31/200<1.
Thus (8) includes the requested endpoints, and the upper inclusion is
strict even at the upper endpoint of (1). The integer n is never
rounded or varied continuously in this argument. If (1) contains no
integer at a particular height, its universal assertion is vacuous.

Let R_*≥1 be C455a's common real-r threshold, chosen to include both
its relative-rate and positive-margin conclusions. Set

    A=max(100,2πexp(2R_*)).

For every real a≥A, R≥R_* and r>R≥R_*. By (8), the parameters
satisfy all of C455a's hypotheses: r is positive real, m is positive
even, its closed ratio band holds, and its height is exactly a.
Consequently C455a gives (3)–(4) with fixed constants independent of
both a and n. Also r≥R=log(a/(2π))/2 proves the asserted logarithmic
error rate by r^(−1/6)≤2^(1/6)(log(a/(2π)))^(−1/6).
No further uniform limit in n or choice of n-dependent onset is used.

For clarity, the imported full sum is exactly

    S=Σ_{j,k≥1}(jk)^(−1/2)(1−log(jk)/(2r))_+^m
                                      exp(ia log(k/j)),

with zero weight at log(jk)≥2r, including equality. C455a gives
D_n=P(S+ε), with |ε|≤C_E(1+r)²exp(−r/200), and the stated B
lower bound. Thus the complete additive error divided by the lower
margin in (4) is at most

    2C_E(1+r)²exp(−r/200+C_B r^(1/3))→0.

The limit is uniform after substitution: C_E,C_B are fixed and
r≥R→∞ for all requested pairs. The expression tends to zero since
its logarithm divided by r tends to −1/200. This is exactly the
inherited comparison, not a new Mellin or sector estimate. The positive
P retains the factorial and single reflection factor from C455a.
Here σ<1; the B lower bound is its analytic-logarithm estimate under
the pinned premise, never an absolutely convergent reciprocal Euler
series on this line.

The parameter-transfer test therefore passes without modifying the
approved band. L323/L327 and fixed-r negative-phase stops remain valid
on their stated domains. The present r varies with a,n, so no positivity
at arbitrary height with r fixed follows. Initial smaller indices,
bounded exterior heights, global mixed positivity and the independent
selected-law/regulator gaps remain unresolved. ∎

### Separate critical audit — 2026-10-23

**Verdict and scope.** The exact saddle transfer and conclusions
(3)–(4) pass on the full stated closed index band, conditional on
audited C455a and its pinned external premise. No mathematical repair,
extra hypothesis or narrower band is required. The pre-existing
[audit assessment](../drafts/literature/2026-10-23-every-height-interior-band-critical-audit-coverage.md)
authorizes this check. It validates this local reproduction, not the
external manuscript or formal import closure, and adds no sign range.

**Root and exact height.** For every fixed a>2π and positive n,
the term −n²/r² forces F(r)→−∞ at zero; exponential growth forces
F(r)→∞ at infinity. Differentiating the entire squared term gives
+2(9/2+n/r)n/r² in F', so the displayed strictly positive derivative
has the correct sign and factor. Continuity and strict monotonicity
therefore give exactly one positive root. Dividing its equation by
a²=4π²exp(4R) gives exp(4(r−R))=1+h²/a², proving (5)
exactly. The recovered positive square root is a itself, so no
continuity argument for D_n in height, rounding error or replacement
of the requested height by a nearby coupled height is involved.

**Both closed inclusions.** Since log(a/(2π))=2R and m=2n,
the factors in (6) are correct. The strict inequality r>R gives
h≤9/2+251/512=2555/512<5; hence (7) follows from
log(1+x)≤x without using the desired band as a premise. The upper
bound is m/r≤251/256<252/256=63/64. For the lower bound,
put d=25/(4a²). All denominators are positive, and the required
inequality is equivalent to

    249R≥248(R+d), that is R≥248d=1550/a².

For a≥100 and R≥1, its right side is at most 31/200<1.
This verifies the lower endpoint with slack, including when n equals
the lower endpoint of (1); the upper endpoint likewise causes no
exception. Only positive integers n are quantified, so m is always
positive even. Empty integer bands require no separate existence claim.
The proof neither interpolates n nor assumes that r is integral.

**Uniformity and rate.** Take C455a's audited real-r threshold
R_*≥1 to include its rate and positive-margin thresholds. The single
number max(100,2πexp(2R_*)) then gives simultaneously a≥100,
R≥R_*≥1 and r>R for every real a on that ray. The preceding
inclusions hold for every requested n at that same a. Thus C455a's
constants apply to all these pairs without any index-dependent
threshold or subsequence. Its error satisfies
r^(−1/6)≤2^(1/6)(log(a/(2π)))^(−1/6), with the inequality
direction correct for the negative power. The proof asserts only
existential constants and onset, not an effective numerical certificate.

**Full input and normalization.** With m=2n the definitions of h,
τ, Φ_*, σ, B and P coincide term for term with C455a. In particular
P has exactly 2^(m−1)/m!, the same C₀ and the already reflected
factor π/a; every factor is positive. The imported S has the same
exponent m and phase exp(ia log(k/j)), and finite support jk<exp(2r).
At cutoff equality its weight is zero because m>0. There is no
discarded diagonal, cutoff term or extra reflection multiplier.
C455a's identity D_n=P(S+ε) includes the entire sector/cutoff
error, while its relative comparison includes the full arithmetic
error. Consequently applying its conclusion introduces no additional
Mellin or sector remainder. On the transferred domain
63/64≤σ≤127/128<1; the lower bound for B is the inherited
analytic-log bound, not reciprocal Euler convergence on this line.

The complete additive error divided by the stated lower margin is
bounded by Q(r)=2C_E(1+r)²exp(−r/200+C_B r^(1/3)). Its
logarithm divided by r tends to −1/200. Thus Q(r)≤exp(−r/400)
for every sufficiently large real r. Since r≥R→∞ uniformly over
the requested integers, this verifies a uniform vanishing comparison,
not merely convergence along one chosen saddle sequence. C455a already
absorbs this error in (3) and fixes the factor 1/2 in (4).

The direct mathematical input remains C455a; no DAG change is needed.
The L323/L327 obstructions and fixed-r negative-phase results retain
their domains: here r changes with a and n. Smaller indices, bounded
exterior heights, global mixed positivity and selected-law/regulator
gaps remain open. The overview's mathematical argument is unchanged;
the completed audit verdict is recorded here rather than adding a new
lemma or repeating the overview.

## Mathlib

Full matching coverage has not been checked; absence is not asserted.
The intermediate value theorem, logarithm inequality and monotonicity
are standard elementary inputs whose specialization is proved above.
No new analytic theorem or verified formal import is claimed. C455a's
Mathlib and external-manuscript qualifications remain unchanged.
