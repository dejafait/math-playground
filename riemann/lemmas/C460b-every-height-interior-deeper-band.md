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
assessed parameter method. The separate critical audit below validates
this conditional transfer; it makes no originality claim and is not an
RH candidate. Initial low indices,
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

### Separate critical audit — 2026-10-24

**Verdict and scope.** The entire stated transfer passes without a
statement repair, extra hypothesis or narrowed interval. This
REPRODUCTION audit uses the unchanged prior SPECIALIZE
[audit assessment](../drafts/literature/2026-10-24-every-height-deeper-band-critical-audit-coverage.md).
The full C460a assembly and audit, and L459/L460's exact statement
interfaces, were checked. Their deep analytic proofs and the pinned
external manuscript/import closure are retained inputs, not newly
audited here. C458b supplies only an audit-method precedent.

**Exact root and endpoint checks.** At fixed a,n>0, the negative
square in F tends to minus infinity as r tends to zero, while the
exponential dominates at infinity. The derivative in the proof has
both terms positive, including the positive derivative of the negative
square. The intermediate value theorem and strict monotonicity therefore
give a unique positive root. Dividing its equation by a² gives
exp(4(r−R))=1+h²/a² exactly. Thus r>R and C460a's positive height
is the prescribed a itself; no height approximation or limit in D_n
is used.

The endpoint conversion in (6) is exact: multiplication by L=2R
and then by m/n=2 gives 53R/64≤m≤27R/32. Before any domain
inclusion, r>R gives h≤9/2+27/64=315/64<5, and hence
0<Δ=r−R≤25/(4a²). The upper bound m/r≤27/32<7/8 follows
immediately. The lower-bound cross multiplication is

    (53/64)R/(R+Δ)≥52/64  if and only if  R≥52Δ.

For a≥100 and R≥1, 52Δ≤325/a²≤13/400<1≤R. All denominators
are positive, so this checks the lower endpoint without assuming the
band first. Both closed endpoints, every intervening integer n and
positive even m=2n are covered. The root itself is not rounded.

The width of the requested n interval is exactly L/256. If L≥256,
its lower endpoint u is at least 53 and ceil(u)≤u+1 is at most the
upper endpoint. This proves positive integer nonemptiness also when
the width equals one or an endpoint is integral. The statement is
stronger than C458b's vacuous-empty-interval convention, and the extra
claim has been checked rather than imported from that precedent.

**Exact normalization and retained hypotheses.** With m=2n, h,a,τ,
Φ_* and P equal C460a's parameters exactly. P is positive and retains
2^(m−1)/m! and the same-sign reflection once in π/a. The arithmetic
factorial A_m=m!/(2r)^m is separately present in M*. The stationary
point is unique only in [x₀−d,x₀+d], with N=m+1, x₀=N/(2r)
and d=1/4096. C460a supplies λ≥2r and its positive Gaussian
square root. In particular

    x*≥x₀−d≥13/32−1/4096>3/8,

so the zeta argument has real part strictly greater than 7/8; a>0
avoids the pole. This respects the exact external premise and makes
the zeta factor nonzero. All factors in M* are positive. Its two-sided
logarithmic bound gives M*≥exp(−K r^(15/16)), with no fixed-center
replacement or use of the different exponent in C458b.

The signed S has identical phase, exponent m and product cutoff in
both inputs, with zero weight at equality because m>0. It is finite,
and interchanging j,k proves reality. D_n and P are real, with P>0,
so ε is real; positive M* makes δ real as well. L460 requires no
external zero-free hypothesis. The external hypothesis enters the
arithmetic estimate through L459 and C460a only.

**Complete errors and a single onset.** Substitution gives exactly
D_n/(PM*)−1=δ+ε/M*. The arithmetic error includes both original
residues and the full deformed contour. The additive error includes
all theta sectors, boundaries, clipped patches and cutoff terms.
There is no omitted remainder. At the minimum permitted M*,

    |ε|/M*≤q=C_E(1+r)²exp(−r/200+K r^(15/16)).

The two stated eventual inequalities imply

    log(2sqrt(r)q)≤−r/200+r/800+r/800=−r/400.

Thus q/f→0 for f=(log r)^3/sqrt(r), and the entire additive error
divided by the guaranteed lower margin is at most 2q→0. These
thresholds exist for arbitrary fixed positive K,C_E because 15/16<1;
no smallness of the constants or practical onset is assumed. This is
a complete error comparison, not a local stationary-phase preview.

Take one real-r threshold R_*≥128,e including C460a's full onset,
the two comparison thresholds, and thresholds for C_A f≤1/4,
q≤1/4 and q≤f. All are independent of n. With
a₀=max(100,2πexp(2R_*)), every real a≥a₀ gives r>R≥R_* and
L≥256. The verified inclusions place all requested pairs in C460a's
domain at once. Reality then gives D_n/(PM*)≥1−1/4−1/4=1/2
and the complete relative bound with constant C_A+1. No sequence of
heights or index-dependent onset replaces this universal assertion.
Finally Δ≤R gives L/2≤r≤L; positivity of the logarithms yields
f(r)≤sqrt(2)(log L)^3/sqrt(L) factor by factor, without assuming
monotonicity of f on a finite interval.

The only direct mathematical input remains C460a. The L323/L327/L456
and fixed-r unit-phase stops retain their distinct scopes. This audit
validates an existing conditional partial band, with no additional
sign range or progress beyond the assessed methods. Initial low
indices, bounded heights, global mixed positivity and selected-law/
regulator realization remain unresolved. The external manuscript and
formal import closure remain locally unaudited, and no RH candidate
or actual off-line zero is asserted.

## Mathlib

Full matching Mathlib coverage has not been checked; absence is not
asserted. Intermediate value, strict derivative monotonicity,
log(1+t)≤t, ceiling bounds and exponential domination are standard
inputs specialized explicitly above. C460a retains the analytic and
external-manuscript qualifications. The external artifact
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` is not asserted to
be a Mathlib theorem or a locally built/import-audited result.
