# Corollary 460b: every-height interior deeper-band transfer

## Hypotheses

Use the actual theta transform Ξ with
Ξ(a+iy)Ξ(a−iy)=Σ_{j≥0}D_j(Ξ;a)y^(2j). Assume exactly C460a's
external premise: the zeta specialization of OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
The half-plane is strict, the pole at one is allowed, and nothing is
asserted on its boundary. Retain the
[external-input register's qualifications](../foundations/2026-10-quasi-riemann-input.md):
the external manuscript and complete formal import closure have not
been independently audited locally. This application does not audit them.

Let a>2π be real and n a positive integer in the closed interval

    (53/256)L≤n≤(27/128)L, L=log(a/(2π)).             (1)

Put R=L/2 and m=2n. Define r>0 by the exact equation

    4π²exp(4r)=a²+(9/2+n/r)².                       (2)

Existence and uniqueness are proved below. Set exactly

    h=9/2+n/r, τ=arctan(a/h)/2,
    Φ_*=m log r+9r−h−2aτ, C₀=(8π²)²,
    P=[2^(m−1)/m!]C₀exp(Φ_*)π/a>0.

After checking C460a's domain, use its moving-saddle scale with
N=m+1, x₀=N/(2r), d=1/4096 and

    H(x)=2rx−N log x+log|ζ(1/2+x+ia)|²,
    H'(x*)=0, x*∈[x₀−d,x₀+d], λ=H''(x*),
    A_m=m!/(2r)^m,
    M*=A_m exp(2rx*) (x*)^(−N)|ζ(1/2+x*+ia)|²
                                             /sqrt(2πλ).

The square root is positive real. The stationary point is unique
in this local interval; global uniqueness is not claimed. M* is not
used to define r.

## Conclusion

There are fixed existential a₀,C,K>0, independent of n, such that
for every real a≥a₀ the interval (1) contains a positive integer,
and every integer n in that interval satisfies

    13/16≤m/r≤7/8, M*>0, |log M*|≤K r^(15/16),
    |D_n(Ξ;a)/(P M*)−1|≤C(log r)^3/sqrt(r),          (3)
    D_n(Ξ;a)/P≥M*/2≥(1/2)exp(−K r^(15/16))>0.      (4)

The error in (3) is uniformly O((log L)^3/sqrt(L)). The complete
additive theta error is negligible relative to (4), as quantified
in the proof. No effective numerical onset is claimed.

This is a conditional partial result and local REPRODUCTION of the
assessed parameter method. It awaits a separate critical audit, makes
no originality claim and is not an RH candidate. Initial low indices,
bounded heights, global mixed positivity and zero exclusion remain open.

## Proof

The prior SPECIALIZE
[exact transfer assessment](../drafts/literature/2026-10-24-deeper-band-every-height-interior-transfer-coverage.md)
covers this rectangle. Audited C460a is the only direct mathematical
input. C458b is a parameter-method precedent; its different sign band
and exponent 2/3 are not applied here. We prove the new endpoint and
quantifier assertions because no assessed citation states this rectangle.
No analytic saddle or theta-sector theorem is reproved.

For fixed a,n>0 the continuous function

    F(r)=4π²exp(4r)−a²−(9/2+n/r)², r>0,

tends to −∞ as r→0+ and +∞ as r→∞. Its derivative is

    F'(r)=16π²exp(4r)+2(9/2+n/r)n/r²>0.

The intermediate value theorem and strict monotonicity give exactly
one positive root. Since a²=4π²exp(4R), equation (2) gives the
exact identity

    r=R+(1/4)log(1+h²/a²)>R>0.                      (5)

In particular a is exactly C460a's positive square root
sqrt(4π²exp(4r)−h²), with h=9/2+m/(2r). No replacement height
or continuity estimate for D_n enters.

Using L=2R and m=2n, the requested range is exactly

    (53/128)R≤n≤(27/64)R,
    (53/64)R≤m≤(27/32)R.                            (6)

Before assuming any desired band inclusion, (5)–(6) imply

    9/2<h≤9/2+27/64=315/64<5.

Thus log(1+t)≤t for t≥0 gives

    0<Δ:=r−R≤25/(4a²).                              (7)

Take a≥100 and R≥1. The upper inclusion follows directly:

    m/r≤(27/32)R/r≤27/32<28/32=7/8.                (8)

For the lower inclusion, positivity of all denominators gives

    m/r≥(53/64)R/(R+Δ)≥52/64=13/16                 (9)

provided R≥52Δ. This condition follows uniformly from (7), since

    52Δ≤325/a²≤13/400<1≤R.

Both closed endpoints of (1) are included, with slack in (8)–(9).
The root r is real and is not rounded; m=2n remains exactly even.

The real interval in (1) has length

    ((27/128)−(53/256))L=L/256.

If L≥256, its length is at least one. For its lower endpoint u,
the integer ceil(u) satisfies u≤ceil(u)≤u+1, which is at most
the upper endpoint. Also u≥53>0. Thus the requested positive
integer range is nonempty at every such real height, independently
of any analytic sign theorem.

Let R_*≥128 be a single real-r threshold for all C460a conclusions,
enlarged to include e, the existence of x*, positive λ, its log M*
bound, complete relative error and positive margin. Fixed additional
thresholds for the error comparisons below are also included before
defining

    a₀=max(100,2πexp(2R_*)).

For every real a≥a₀, R≥R_* and r>R≥R_*. Thus (8)–(9)
place every requested n in C460a's closed band beyond the same
onset. Also L=2R≥256 proves nonemptiness at every such height.
C460a now supplies its unique local x*, λ≥2r, positive M* and
|log M*|≤K r^(15/16), and its entire comparison gives (3)–(4)
with constants independent of a,n. This uses one threshold for all
real heights and all their requested indices, not an index-dependent
limit or a subsequence.

For completeness, the exact sum and the two complete errors imported
through C460a are

    S=Σ_{j,k≥1}(jk)^(−1/2)(1−log(jk)/(2r))_+^m
                                      exp(ia log(k/j)),
    S=M*(1+δ), |δ|≤C_A(log r)^3/sqrt(r),
    D_n=P(S+ε), |ε|≤C_E(1+r)²exp(−r/200).           (10)

The sum is finite and its weight is zero whenever log(jk)≥2r,
including equality. Swapping j,k proves S real. The positive M*,
real D_n and positive P make δ and ε real. The arithmetic error
δ includes both original residues and the entire deformed contour;
ε includes all theta sectors, boundaries, clipped patches and cutoff
terms. L460, the additive input inside C460a, needs no external
zero-free premise. The unchanged pinned premise is needed for the
arithmetic comparison. Exactly,

    D_n/(P M*)−1=δ+ε/M*,
    |ε|/M*≤q(r):=C_E(1+r)²exp(−r/200+K r^(15/16)). (11)

Taking C_E,K>0 enlarged if needed, choose fixed eventual thresholds
such that, for every real r beyond them,

    K r^(15/16)≤r/800,
    log(2C_E)+2log(1+r)+(1/2)log r≤r/800.

These exist because each left side divided by r tends to zero.
Then log(2sqrt(r)q(r))≤−r/400. In particular

    2q(r)→0,
    q(r)/((log r)^3/sqrt(r))≤exp(−r/400)/(2(log r)^3)→0.

The entire additive theta error divided by the guaranteed lower
margin in (4) is bounded by

    C_E(1+r)²exp(−r/200)/[(1/2)exp(−K r^(15/16))]
        =2q(r)→0.                                  (12)

Thus (11) retains the full relative rate even at the smallest M*
allowed by the logarithmic bound. The achieved margin dominates
the complete error, not just a local saddle remainder. All these
thresholds can be included in R_* above; none depends on n.
Since r≥R=L/2→∞ uniformly over requested n, these limits remain
uniform after substitution.

Finally (7), a≥100 and R≥1 give Δ≤R and hence L/2≤r≤L.
For L≥256 all relevant logarithms are positive, so

    (log r)^3/sqrt(r)≤sqrt(2)(log L)^3/sqrt(L).

This proves the asserted height-rate conversion without presuming
finite-range monotonicity of that rate.

All factors in P are positive. Its exact theta factor is
2^(m−1)/m!, and π/a contains the same-sign reflection once.
The separate factorial A_m=m!/(2r)^m and positive sqrt(2πλ)
in M* are retained. No factor is inserted, removed or replaced by
a fixed-center zeta square, and no reciprocal Euler expansion below
one is assumed.

The continuation test therefore passes on the whole approved rectangle.
The L323/L327/L456 and fixed-r unit-phase stops retain their scopes:
here the exact r varies with a,n and the moving saddle is retained.
This is no assertion of arbitrary-height positivity with r fixed.
The new contribution is local parameter transfer of an assessed
conditional input, not progress beyond the checked source methods.
Initial indices, bounded heights, mixed positivity and selected-law/
regulator realization remain independent unresolved gaps. ∎

## Mathlib

Full matching Mathlib coverage has not been checked; absence is not
asserted. Intermediate value, strict derivative monotonicity,
log(1+t)≤t, ceiling bounds and exponential domination are standard
inputs specialized explicitly above. C460a retains the analytic and
external-manuscript qualifications. The external artifact
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` is not asserted to
be a Mathlib theorem or a locally built/import-audited result.
