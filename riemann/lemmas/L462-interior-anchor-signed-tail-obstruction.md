# Lemma 462: the conditional interior-anchor signed tail remains the full anchor

## Hypotheses

Let Ξ(z)=ξ(1/2+iz) be L018's actual entire completion. For real a put

    H_a(y)=Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0) D_n(Ξ;a)y^(2n),
    S_(K,a)(η)=Σ_(n=0)^K D_n(Ξ;a)η^(2n),    T=2+|a|.

Assume exactly L461's retained external premise: OpenAI,
*The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026, Theorem 1.1, specialized to ζ, at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
The [pinned manuscript](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
allows the pole at 1 and does not exclude the boundary Re(s)=7/8.
The manuscript and formal import closure remain locally unaudited;
see the [external-input register](../foundations/2026-10-quasi-riemann-input.md).
The present result is conditional on that premise, not its verification.

Fix 3/8<η<1/2, 0≤c<η/2 and B≥0. Logarithms are natural.
The cutoffs are integers 0≤K≤c log T+B. All parameters and constants
below are fixed independently of a and K; central zeros of Ξ and
arbitrary central multiplicities are allowed.

## Conclusion

For every fixed choice

    max(3/8,2c)<r<η,
    δ₀=η−r−2c log(η/r),    0<ε<δ₀/4,
    δ=δ₀−4ε,

one has δ₀>0, δ>0 and a constant C>0 such that for every real a
and every allowed K,

    H_a(η)>0,
    |S_(K,a)(η)|/H_a(η) ≤ C T^(−δ).                    (1)

Consequently, uniformly over all those K,

    (H_a(η)−S_(K,a)(η))/H_a(η) = 1+O(T^(−δ)) → 1       (2)

as |a| tends to infinity. This includes c=0 and every fixed B≥0.
Constants are existential; no effectivity or uniformity in parameters
approaching the excluded endpoints is asserted.

Thus a comparison that needs the omitted Taylor tail at this fixed
anchor to have absolute value at most half a positive lower bound
A(a)≤H_a(η) cannot work with these cutoffs at arbitrarily large
heights. This concerns that small-tail comparison only. It establishes
no coefficient signs, off-line zero, RH candidate, moving-anchor
obstruction or endpoint negative-witness theorem.

## Proof

### Separate admissible instances of the conditional estimates

The interval for r is nonempty because both 3/8 and 2c are strictly
less than η. Fix r in that interval. Then

    δ₀=∫_r^η (1−2c/x) dx>0,                           (3)

since r>2c. Choose ε as stated. For example ε=δ₀/8 gives δ=δ₀/2.
Fix also

    α=(3/8+r)/2,    R_*=(η+1/2)/2.

They satisfy 3/8<α<r<1/2 and 3/8<η<R_*<1/2.
Only after fixing these parameters take constants from L461.

Apply L461's equation (1) with its anchor α, outer radius r and
loss ε. Write its constants as h₁>0 and C₁≥1. Its explicit model
and ratio bound give

    A₁(a)=h₁ T^(7/2+α−2ε) exp(−π|a|/2),
    M_r(a):=max_(|y|=r)|H_a(y)|
        ≤ C₁ T^(r−α+4ε) A₁(a)
        = C₁h₁ T^(7/2+r+2ε) exp(−π|a|/2).             (4)

Independently apply the same equation with anchor η, outer radius
R_* and the same ε. Its lower bound, with h₂>0, gives

    H_a(η) ≥ h₂ T^(7/2+η−2ε) exp(−π|a|/2)>0.           (5)

Both applications obey L461's strict anchor-before-radius ordering.
In (4) multiplication uses the explicit positive model A₁, not an
upper bound on H_a(α). In (5) no growth estimate at R_* is needed.
In particular no application has reversed L461's stated radii.
Dividing (4) by (5) yields, with C₀=C₁h₁/h₂,

    M_r(a)/H_a(η) ≤ C₀ T^(r−η+4ε).                    (6)

The four losses comprise +2ε in circle growth and −2ε in the
anchor lower bound. The first application already controls the full
complex circle, not merely its real endpoints. Explicitly, at y=u+iv
its completed factors have arguments

    1/2−u+i(a−v),    1/2+u+i(a+v).

Here |u|,|v|≤r, the real parts lie in the width-r strip, and

    |a−v|+|a+v|≥2|a|,
    2+|a±v|≤(1+r/2)T.

These are exactly the shifted-height conditions underlying L461's
equation (11), so (4) retains its exponential and both polynomial
losses even when a shift crosses zero. At the independent anchor,
H_a(η)=|ξ(1/2+η−ia)|². Its line is strictly between 7/8 and 1,
so the retained premise, nonzero completed prefactors and L461's
compact-height minimum justify (5) at every real a. None of (4)–(6)
divides by Ξ(a), its derivatives or a central multiplicity.

### Coefficients and uniform cutoff

By L018, H_a is entire and even in y; it is real on the real y-axis.
Its Taylor series therefore has precisely the displayed real even
coefficients. Cauchy's coefficient estimate gives, for every n≥0,

    |D_n(Ξ;a)|≤M_r(a) r^(−2n).                         (7)

The precise supporting source is Tamara Grava, *Complex Function
Theory*, December 29, 2024, section 4.4, Lemma 4.16, printed p. 42
(PDF p. 46), [statement and proof](https://people.sissa.it/~grava/cft.pdf#page=46).
Its hypothesis is analyticity on a neighborhood of the closed disk;
entirety supplies this for every a. The bound applies to derivatives
at zero, independently of where a finite Taylor polynomial will be
evaluated. Thus η>r does not violate (7). No series expansion on
|y|=r at the exterior point η is used.

Put q=(η/r)²>1. Equations (6)–(7), the triangle inequality and the
finite geometric sum imply

    |S_(K,a)(η)|/H_a(η)
       ≤ C₀ T^(r−η+4ε) Σ_(n=0)^K q^n
       ≤ [C₀/(1−q^(−1))] T^(r−η+4ε) q^K
       ≤ [C₀q^B/(1−q^(−1))]
                              T^(r−η+4ε+2c log(η/r))
       = C T^(−δ).                                   (8)

The geometric inequality is valid also for K=0. The last inequality
uses only K≤c log T+B and q>1, so its constant is independent of
every permitted integer K. If c=0 it simply bounds q^K by q^B;
there is no division by c, K or a central value. All choices precede
variation of a; B is fixed, and its entire contribution is q^B.
Equation (8) proves (1). Subtracting the normalized finite sum from
one proves (2), with the same uniform error bound. Entirety ensures
that this difference is the actual Taylor remainder at η; there is
no exchange of infinite limits or summations.

Finally choose the height large enough that C T^(−δ)<1/2.
The real remainder in (2) is then strictly greater than H_a(η)/2,
and therefore strictly greater than A(a)/2 for any 0<A(a)≤H_a(η).
This proves the stated obstruction. No integral representation of
this same remainder can change its value. The result alone makes
no assertion about other comparisons, parameter-dependent anchors
or the endpoint c=η/2. ∎

This is a REPRODUCTION of L322's assessed smaller-circle mechanism
using the separately conditional interior estimates. L322's exterior
and ellipse conclusions remain unchanged; its ellipse calculation
is not an input here. The specialization is necessary because those
earlier anchor hypotheses exclude the present domain. No originality
beyond the checked source scope is claimed. Initial signs at unbounded
heights, bounded-height coverage and mixed positivity remain open.

### Critical audit — 2026-10-25

**Verdict.** Equations (1)–(2) and the stated small-tail obstruction
pass this separate mathematical audit under exactly the written
hypotheses. No proof correction, additional hypothesis or dependency
is needed. This validates the conditional specialization of an assessed
source mechanism, not a result beyond the sources checked. The external
September 30 Theorem 1.1 and its import closure remain locally unaudited.

**Fixed parameters and independent constants.** Because 2c<η and
3/8<η, the specified open interval for r is nonempty. On [r,η],
1−2c/x≥1−2c/r>0, so (3) gives a strictly positive δ₀. Fixing ε
with 4ε<δ₀ then fixes δ>0. The two applications of L461 are to
(anchor, radius, loss)=(α,r,ε) and (η,R_*,ε), respectively.
Both obey 3/8<anchor<radius<1/2. In particular the actual circle
of the first application is smaller than the separate second anchor;
there is no reversed ordering within either application.

L461's first ratio is M_r/A₁≤C₁T^(r−α+4ε), where A₁ is its
explicit positive model, not H_a(α). Multiplying by this exact model
gives exponent (r−α+4ε)+(7/2+α−2ε)=7/2+r+2ε.
The second application supplies H_a(η)≥A₂ with exponent
7/2+η−2ε. Dividing the former upper bound by this latter lower
bound gives exactly (6), with constant C₁h₁/h₂ and exponent
r−η+4ε. There is no inference of an anchor upper bound from a
lower bound. The two positive h constants need not agree. Every
constant is chosen after η,c,B,r,ε,α,R_* have been fixed.

**Complex heights and the all-height denominator.** Substitution of
y=u+iv into the definition of Ξ gives the two completed arguments
displayed after (6), with no real or imaginary sign change omitted.
The circle |y|=r implies |u|,|v|≤r. In L461's first instance the
strip power is q_r=7/4+r/2+ε>0. Thus its two polynomial bounds
multiply to at most a fixed multiple of T^(2q_r), since
T+r≤(1+r/2)T. Its two exponential bounds multiply to at most
exp(−π|a|/2) by the triangle inequality. L461's bound applies to
every real shifted height, so this remains valid when a±v=0;
one must not substitute a large-height asymptotic alone there.

For real η, L018's reflection and conjugation give
Ξ(a−iη)=conj(Ξ(a+iη)), and reflection also identifies
Ξ(a+iη)=ξ(1/2+η−ia). The latter real part lies strictly in
(7/8,1). At every a its completed factors are finite and nonzero:
s≠0,1, Re(s/2)>0, gamma has no zeros, and the retained premise
excludes zeta zeros. Hence H_a(η)>0, including at a=0.
L461's large-height lower bound and positive minimum of the ratio
to its model on the remaining compact interval supply a single h₂.
No assertion of nonvanishing inside the smaller strip or at the
central point is made. Arbitrary central multiplicity is harmless.

**Every coefficient and every cutoff.** L018 makes H_a entire and
even; its reality on the real axis makes all Taylor coefficients
real. Grava's cited coefficient estimate, applied at zero on the
closed radius-r disk, bounds the derivative of order 2n by
(2n)! M_r/r^(2n). Dividing by (2n)! yields (7). The later
evaluation at η>r is only of a finite polynomial, and does not
alter that estimate's domain requirement.

For q=(η/r)²>1, the exact sum is
Σ_(n=0)^K q^n=q^K(1−q^(−K−1))/(1−q^(−1)), so the bound in
(8) holds also at K=0. The cutoff gives
q^K≤q^B exp(c log T log q)=q^B T^(2c log(η/r)).
Combining exponents leaves precisely −δ₀+4ε=−δ<0. Hence
C=C₁h₁q^B/[h₂(1−q^(−1))] is finite, positive and independent
of both a and K. No rounding term is needed: the hypothesis is
an inequality for the actual integer K. For c=0, the proof uses
only q^K≤q^B; for B=0,K=0 it remains the same inequality.
These checks establish the full uniformity asserted in (1).

**Signed remainder and scope of the stop.** The entire Taylor series
converges at each fixed η, so H_a(η)−S_(K,a)(η) is its actual
remainder. The estimate uses a finite sum and no exchange of a
limit with an infinite series. Since both H_a(η) and S_(K,a)(η)
are real and H_a(η)>0, (1) gives
1−CT^(−δ)≤(H_a(η)−S_(K,a)(η))/H_a(η)≤1+CT^(−δ).
One height threshold makes CT^(−δ)<1/2 for every allowed K.
There the remainder itself is positive and exceeds H_a(η)/2,
so its absolute value exceeds A(a)/2 for every 0<A(a)≤H_a(η).
This verifies the exact comparison stopped in the conclusion.

The argument does not cover c=η/2, η=3/8, height-dependent
parameters, or a different coefficient comparison. Its constants
and onset have no asserted uniformity as parameters approach those
boundaries. L322 is a comparison with an earlier exterior-anchor
mechanism, not a needed theorem input; its ellipse conclusions are
unchanged. L018 supplies entirety and symmetry, and L461 supplies
the conditional estimates; no further local theorem is needed.
The named Cauchy estimate is cited
directly above. Initial signs, mixed positivity and realization
remain unproved; there is no RH candidate or certified off-line zero.

## Mathlib

Full matching coverage is unchecked; absence is not asserted.
Supporting Cauchy-estimate, finite-geometric-sum and asymptotic API
coverage has not been checked. L461 retains its supporting gamma
reference [NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), with
bounded-real-part uniformity, and its unchecked analytic API status.
The external theorem name `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`
is an external artifact, not a Mathlib inclusion or local-build claim.
The precise classical coefficient citation above supplies the only
additional named theorem used in this specialization.
