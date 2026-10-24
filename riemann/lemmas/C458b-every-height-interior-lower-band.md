# Corollary 458b: every-height interior lower-band transfer

## Hypotheses

Use the actual theta transform Ξ, normalized by
Ξ(a+iy)Ξ(a−iy)=Σ_{j≥0}D_j(Ξ;a)y^(2j). Assume exactly C458a's
pinned external premise: the zeta specialization of OpenAI,
*The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Nonvanishing is only on the strict half-plane Re(s)>7/8; the pole at
one is allowed and the boundary is not excluded. Retain the
[external-input register's qualifications](../foundations/2026-10-quasi-riemann-input.md):
the external manuscript and formal import closure have not been
independently audited locally. This corollary does not audit them.

Let a>2π be real and n be a positive integer satisfying

    (29/128)log(a/(2π))≤n≤(15/64)log(a/(2π)).          (1)

Set R=log(a/(2π))/2 and m=2n. Define r>0 by

    4π²exp(4r)=a²+(9/2+n/r)².                       (2)

The proof below establishes that this root exists and is unique. Put

    h=9/2+n/r, τ=arctan(a/h)/2,
    Φ_*=m log r+9r−h−2aτ, C₀=(8π²)²,
    P=[2^(m−1)/m!]C₀exp(Φ_*)π/a>0.

For all sufficiently large a define C458a's exact moving-saddle scale:
N=m+1, x₀=N/(2r), d=1/4096, and

    H(x)=2rx−N log x+log|ζ(1/2+x+ia)|²,
    H'(x*)=0, x*∈[x₀−d,x₀+d], λ=H''(x*),
    A_m=m!/(2r)^m,
    M*=A_m exp(2rx*) (x*)^(−N)|ζ(1/2+x*+ia)|²
                                             /sqrt(2πλ).

Existence and uniqueness of x*, its positivity and λ>0 are imported
only after verifying C458a's domain; M* is not needed to define r.

## Conclusion

There are fixed a₀,C,K>0, independent of n, such that every real
a≥a₀ and every integer n satisfying (1) have

    7/8≤m/r≤31/32, M*>0, |log M*|≤K r^(2/3),
    |D_n(Ξ;a)/(P M*)−1|≤C(log r)^3/sqrt(r),          (3)
    D_n(Ξ;a)/P≥M*/2≥(1/2)exp(−K r^(2/3))>0.         (4)

Writing L=log(a/(2π)), the error in (3) is uniformly
O((log L)^3/sqrt(L)). The complete additive theta error is negligible
relative to (4), with its bound stated explicitly below. Constants
and onset are existential, not numerically evaluated.

This is a local REPRODUCTION of the assessed parameter method using
the audited conditional C458a. The separate critical audit below validates it.
It is a partial sign band, not a complete candidate resolution of RH
or a new zero-exclusion range. Smaller indices, bounded heights and
global mixed positivity remain unresolved.

## Proof

The prior SPECIALIZE
[transfer assessment](../drafts/literature/2026-10-24-lower-band-every-height-interior-transfer-coverage.md)
covers exactly this rectangle and the unchanged C458a normalization.
C455b is a precedent for the elementary parameter method only; its
different sign theorem and fixed-center zeta square are not inputs.
We prove the new endpoint inequalities and onset explicitly because
neither C458a nor an external citation states this rectangle.

For fixed a,n>0 the continuous function

    F(r)=4π²exp(4r)−a²−(9/2+n/r)², r>0,

tends to −∞ as r→0+ and to +∞ as r→∞. Its derivative is

    F'(r)=16π²exp(4r)+2(9/2+n/r)n/r²>0.

The intermediate value theorem and strict monotonicity give exactly
one positive root. Dividing (2) by a²=4π²exp(4R) and taking
logarithms gives the exact identity

    r=R+(1/4)log(1+h²/a²)>R>0.                      (5)

In particular a is exactly the positive height
sqrt(4π²exp(4r)−h²) used by C458a, with h=9/2+m/(2r).
No nearby height or continuity estimate for D_n is substituted.

Since L=2R, (1) becomes

    (29/64)R≤n≤(15/32)R,
    (29/32)R≤m≤(15/16)R.                            (6)

Using r>R before any desired band inclusion gives

    9/2<h≤9/2+15/32=159/32<5.

Thus log(1+t)≤t for t≥0 applied to (5) yields

    0<r−R≤25/(4a²).                                 (7)

Take a≥100 and R≥1. From (6) and r>R,

    m/r≤(15/16)R/r≤15/16=30/32<31/32.               (8)

For the lower endpoint, (6)–(7) give

    m/r≥(29/32)R/(R+25/(4a²))≥28/32=7/8,           (9)

because the last inequality is equivalent, with positive denominators,
to R≥28·25/(4a²)=175/a². This follows from R≥1 and a≥100,
as 175/a²≤7/400<1. Both inequalities therefore hold uniformly at
the closed endpoints of (1), with slack. No integrality of r is
assumed, and n is neither interpolated nor rounded. If the requested
interval contains no integer at a height, the assertion there is
vacuous; it makes no extra existence claim for an integer n.

Let R_*≥1 be C458a's single real-r onset, enlarged to include its
definition of x*, logarithmic bound on M*, full relative error and
positive margin. Set

    a₀=max(100,2πexp(2R_*)).

For every real a≥a₀, R≥R_* and r>R≥R_*. Equations (8)–(9)
verify the closed band for every requested n at that same height.
Also m=2n is positive and even. Hence all hypotheses of C458a
hold at the exact recovered parameters. Its definition of x* and
positive factorial-normalized M* therefore applies, and it gives
(3)–(4) with constants independent of a,n. No n-dependent onset
or passage from a subsequence is used.

For the rate conversion, (7), a≥100 and R≥1 imply r≤2R=L.
Together with r≥R=L/2 and L≥2 this gives

    (log r)^3/sqrt(r)≤sqrt(2)(log L)^3/sqrt(L).       (10)

All logarithms in this inequality are positive. This proves the
uniform logarithmic error rate, rather than assuming that the rate
is decreasing at all finite r.

To retain the full error and normalization explicitly, the imported
finite sum and identity are exactly

    S=Σ_{j,k≥1}(jk)^(−1/2)(1−log(jk)/(2r))_+^m
                                      exp(ia log(k/j)),
    D_n=P(S+ε), |ε|≤C_E(1+r)²exp(−r/200).

The weight is zero at log(jk)≥2r, including equality. This is the
complete theta error from C458a through L458, including every sector,
boundary and cutoff contribution. The full arithmetic comparison
from C458a through L457 is S=M*(1+δ), with
|δ|≤C_A(log r)^3/sqrt(r); it already includes both residues and
the entire deformed contour. Therefore

    D_n/(P M*)−1=δ+ε/M*.

The complete additive theta error divided by the guaranteed lower
margin in (4) is at most

    Q(r)=2C_E(1+r)²exp(−r/200+K r^(2/3))→0.         (11)

Indeed log Q(r)/r→−1/200, so eventually Q(r)≤exp(−r/400)
for every real r beyond one fixed threshold. The same comparison
after multiplying Q by r^(1/2) has logarithm divided by r tending
to −1/200; hence ε/M*=o(r^(−1/2)), smaller than the rate in
(3). Since r≥R→∞ uniformly over all requested n, these are
uniform limits after substitution. Enlarge R_* once to include any
thresholds in these explicit comparisons; the same formula for a₀
still gives one real-height onset. Equivalently the lower margin
divided by (1+r)²exp(−r/200) tends to infinity. No omitted remainder
must be controlled separately at the requested heights.

Every factor of P is positive. Its coefficient is exactly
2^(m−1)/m!, and π/a includes the same-sign reflection once.
The factorial in A_m belongs to the separate arithmetic scale M*
and is also retained. No factor is cancelled, duplicated or replaced
by a fixed-center square. The lower bound for M* is its inherited
analytic-logarithm bound under the pinned premise; no reciprocal
Euler series below one or boundary nonvanishing is asserted.

The continuation test passes on the entire approved rectangle.
L323/L327/L456 and fixed-r/unit-phase failures retain their scopes:
here r changes with a,n and the moving saddle is retained. This
application asserts no positivity for arbitrary a with r fixed.
Smaller indices, bounded exterior heights, global mixed positivity
and the independent selected-law/regulator gaps remain open. ∎

### Separate critical audit — 2026-10-24

**Verdict and scope.** The full stated transfer passes, without a
mathematical repair, extra hypothesis or narrowing of the rectangle.
This REPRODUCTION audit uses the prior SPECIALIZE
[audit assessment](../drafts/literature/2026-10-24-every-height-lower-band-critical-audit-coverage.md)
and audited C458a. L457/L458's statement interfaces and audit conclusions
were checked; their contour and sector proofs are not reproved here.
The pinned external theorem, manuscript and formal import closure are
not independently verified by this application audit.

**Root and exact height.** For fixed positive n the term -n²/r²
forces F(r) to -∞ at zero, while the exponential term forces F(r)
to +∞ at infinity. Differentiating the negative square gives the
positive term 2(9/2+n/r)n/r², with the stated sign and factor.
Continuity and F'>0 give exactly one root on all positive r.
Since a²=4π²exp(4R), its equation gives
exp(4(r-R))=1+h²/a² exactly. In particular r>R, and the positive
square root in C458a is a itself. No continuity estimate for D_n,
approximation of the height or assertion about integral r is needed.

**Both endpoints without circularity.** Substituting L=2R in (1)
and then using m=2n gives 29R/32≤m≤15R/16.
Using only this and r>R gives h≤159/32<5. Thus the bound
Δ:=r-R≤25/(4a²) precedes and does not assume either ratio inclusion.
The upper inclusion is m/r≤15/16<31/32. The lower follows from

    (29/32)R/(R+Δ)≥28/32  if R≥28Δ;
    28Δ≤175/a²≤7/400<1≤R  for a≥100, R≥1.

All denominators are positive. These inequalities include both closed
endpoints of (1), and indeed have slack. Every requested integer n is
positive once R≥1, and m=2n is positive even. The assertions cover
all such integers at each real height; an empty integer interval is
vacuous. No rounding or interpolation of an index is used.

**One onset and the stated rate.** Choose C458a's single real-r onset
R_*≥e to include its saddle definition, logarithmic bound, relative
error and positive margin. Then a₀=max(100,2πexp(2R_*)) gives
r>R≥R_* for every real a≥a₀ and every requested integer n.
The endpoint checks require no additional n-dependent threshold.
Also Δ≤25/(4a²)≤R, so L/2≤r≤L. Positivity of the logarithms
therefore gives, factor by factor,

    (log r)^3≤(log L)^3,  1/sqrt(r)≤sqrt(2)/sqrt(L).

This verifies (10) without needing eventual monotonicity of the whole
rate. Any further fixed real-r threshold below can be included in
R_* before defining a₀, preserving one onset for all real heights.

**Complete normalization and errors.** Substitution m=2n makes h,
a, τ, Φ_* and P identical to C458a. The coefficient 2^(m-1)/m!
and the already reflected π/a occur exactly once, and all factors
of P are positive. The finite S retains its phase, exponent and all
pairs jk<exp(2r); its weight at equality is zero since m>0.
Conjugate interchange of j,k makes S real. C458a also supplies real
ε and δ, as required for the lower inequality in (4).

The saddle is the unique real stationary point in the stated local
interval, not an asserted global unique stationary point. Its
definition has N=m+1, x₀=N/(2r), d=1/4096 and denominator
sqrt(2πλ), exactly as in C458a; its audited λ≥2r and x*>0
ensure positivity. The factorial m!/(2r)^m is retained in M*,
separately from the theta coefficient in P. The bound
|log M*|≤K r^(2/3) gives the lower bound used here, without an
Euler reciprocal series below one or a fixed-center square substitution.

The exact identity is D_n/(PM*)-1=δ+ε/M*, with the full
arithmetic remainder, both residues and all contour tails in δ,
and every sector, boundary and cutoff error in ε. Write
q=C_E(1+r)²exp(-r/200+K r^(2/3)); then |ε|/M*≤q.
For a direct uniform rate check, choose one real-r threshold with

    K r^(2/3)≤r/800,
    log(2C_E)+2log(1+r)+(1/2)log r≤r/800.

The limits of both left sides divided by r are zero. These give
log(2sqrt(r)q)≤-r/400 and hence Q=2q→0 and
q/((log r)^3/sqrt(r))→0. This verifies the full additive comparison
even at the smallest allowed M*. C458a's common onset already gives
|δ|+q≤1/2, so the real normalized value is at least 1/2, yielding
(3)–(4). Since r≥L/2→∞ uniformly, neither comparison becomes a
subsequence-only limit after transfer.

The only direct mathematical input remains C458a; C455b is a method
precedent. No DAG edge changes. L323/L327/L456 and the fixed-r and
unit-phase stops retain their distinct hypotheses. This validates a
previously written conditional partial band, without a new sign range
or progress beyond the assessed methods. Initial low indices, bounded
heights, global mixed positivity and selected-law/regulator gaps remain
open; full matching Mathlib coverage remains unchecked. The overview's
mathematical assembly is unchanged, so this verdict is recorded here.

## Mathlib

Full matching coverage has not been checked; absence is not asserted.
The intermediate value theorem, derivative monotonicity and elementary
logarithm inequalities are standard inputs specialized explicitly
above. C458a supplies the analytic result with its existing Mathlib
and external-manuscript qualifications. The external artifact
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` is not asserted to
be a Mathlib theorem or a locally compiled/import-audited input.
