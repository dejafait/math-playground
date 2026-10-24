# Corollary 458a: conditional uniform lower-band Laguerre margin

## Hypotheses

Use the actual theta transform Ξ, normalized by
Ξ(a+iy)Ξ(a−iy)=Σ_{n≥0}D_n(Ξ;a)y^(2n). Assume the zeta
specialization of OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re s > 7/8*, September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
This is precisely L457's external premise: nonvanishing strictly on
Re(s)>7/8, allowing the pole at 1 and making no boundary assertion.
Retain the [external-input register's qualifications](../foundations/2026-10-quasi-riemann-input.md):
the external manuscript and formal import closure have not been
independently audited locally. This corollary does not verify them.

Let r>0 be real, m be a positive even integer, and

    7/8≤m/r≤31/32, n=m/2,
    h=9/2+m/(2r), a=sqrt(4π²exp(4r)−h²)>0,
    τ=arctan(a/h)/2, Φ_*=m log r+9r−h−2aτ,
    C₀=(8π²)², P_{r,m}=[2^(m−1)/m!]C₀exp(Φ_*)π/a.

Use L457 and L458 at these identical parameters, with their full sum

    S=Σ_{j,k≥1}(jk)^(−1/2)(1−log(jk)/(2r))_+^m
                                      exp(ia log(k/j)).

The weight is zero at log(jk)≥2r, including equality. For the positive
scale in L457, set N=m+1, x₀=N/(2r), d=1/4096 and

    H(x)=2rx−N log x+log|ζ(1/2+x+ia)|².

For sufficiently large r, let x* be L457's unique real stationary
point in [x₀−d,x₀+d], and λ=H''(x*). Define exactly

    A=m!/(2r)^m,
    M*=A exp(2rx*) (x*)^(−N)|ζ(1/2+x*+ia)|²
                                            /sqrt(2πλ)>0.

## Conclusion

There are fixed C,K,R>0, independent of m,r throughout the closed
band, such that for every admissible r≥R,

    |D_{m/2}(Ξ;a)/(P_{r,m}M*)−1|≤C(log r)^3/sqrt(r), (1)
    D_{m/2}(Ξ;a)/P_{r,m}≥M*/2
                                  ≥(1/2)exp(−K r^(2/3))>0. (2)

The entire additive theta error is negligible relative to this lower
margin. Constants and onset are existential, not numerically evaluated.
This is a local REPRODUCTION assembling audited inputs; the separate
critical audit below validates the assembly. It is a conditional partial
result, not a complete candidate resolution of RH. No every-height
transfer, smaller-index completion, bounded-height extension, global
mixed positivity or zero-exclusion conclusion is asserted.

## Proof

The prior SPECIALIZE [assembly assessment](../drafts/literature/2026-10-24-lower-band-laguerre-assembly-coverage.md) covers this application. No saddle or theta-sector theorem is reproved.
The elementary error comparison is needed because neither of the two
inputs alone states the Laguerre sign on this band.

By L457 there are fixed K,C_A,R_A>0 such that, on every admissible
pair with r≥R_A,

    S=M*(1+δ), |δ|≤C_A f(r), f(r)=(log r)^3/sqrt(r),
    |log M*|≤K r^(2/3), M*>0.                         (3)

In particular M*≥exp(−K r^(2/3)). This is the moving-saddle
scale, not the fixed-center square |ζ((1+m/r)/2+ia)|².
Its lower bound is the inherited analytic-logarithm bound; no
reciprocal Euler expansion below one is used. The finite sum S is
real because interchange of j,k conjugates each summand and
preserves its weight and support. Thus δ is real.

L458 supplies fixed C_E,R_E>0 on exactly the same positive-real-r,
positive-even-m domain with

    D_{m/2}(Ξ;a)=P_{r,m}(S+ε), ε real,
    |ε|≤C_E E(r), E(r)=(1+r)²exp(−r/200).             (4)

This is its complete error, including all sectors, boundary strips,
clipped patches and cutoff contributions. The definitions of h,a,S
coincide, including zero cutoff equality. The normalization P is
unchanged: its π/a already contains the same-sign reflection once,
and 2^(m−1)/m! is the exact coefficient multiplier. Every factor
of P is positive. No extra factorial or reflection factor is added.

Divide (4) by P M* and apply (3):

    D_{m/2}/(P M*)=1+δ+ε/M*,
    |ε|/M*≤q(r):=C_E(1+r)²exp(−r/200+K r^(2/3)).    (5)

For every fixed p≥0,

    log(r^p q(r))/r
      =log(C_E)/r+2log(1+r)/r+p log r/r
                                      −1/200+K r^(−1/3)
      →−1/200.

Hence eventually log(r^p q(r))≤−r/400, so r^p q(r)→0.
In particular q=o(r^(−1/2))=o(f(r)), and q→0. Also f(r)→0;
for example, on writing t=log r it becomes t³exp(−t/2).
Thus (5) gives the relative rate in (1).

To specify one onset for both assertions, choose fixed thresholds
R_rate,R_δ,R_q so that for every real r beyond the respective
threshold, q(r)≤f(r), C_A f(r)≤1/4 and q(r)≤1/4.
These exist by the preceding limits. Take R to be the maximum of
these three thresholds, R_A,R_E and e, enlarged if needed for the
positive square root and L457's definition of x*. All are fixed,
independent of m. On every admissible pair with r≥R, (5) proves
(1) with C=C_A+1 and gives the real inequality

    D_{m/2}/(P M*)≥1−1/4−1/4=1/2.

Together with (3) this proves (2), including both closed band
endpoints and every cutoff transition. The full additive error
divided by the lower margin in (2) is at most 2q(r)→0;
equivalently

    [(1/2)exp(−K r^(2/3))]/E(r)
         =exp(r/200−K r^(2/3))/[2(1+r)²]→∞.

This compares actual bounds, not just the formal names of errors.
L457 already includes both residues and its whole deformed contour;
no arithmetic remainder is omitted from δ.

L323's larger-strip obstruction, L327's phase-uniform PSD obstruction
and L456's fixed-center obstruction retain their scopes. The present
application uses L458's full signed sum and L457's moving saddle at
the coupled a(r,m); it claims no arbitrary-height result with r fixed
or arbitrary unit-prime-phase positivity. Initial low indices, bounded
heights, global mixed positivity and selected-law/regulator gaps remain
independent and unresolved. ∎

### Separate critical audit — 2026-10-24

**Verdict and scope.** Equations (1)–(2) pass on the complete stated
domain, without a mathematical repair or additional hypothesis. This
REPRODUCTION audit uses the prior SPECIALIZE
[audit assessment](../drafts/literature/2026-10-24-lower-band-laguerre-margin-critical-audit-coverage.md).
It checks the downstream application of L457 and L458, reusing their
separate correctness audits. It does not reverify the external theorem,
its manuscript or its formal import closure, or extend either input.

**Exact interfaces.** Both input conclusions quantify over all sufficiently
large positive real r and positive even m with 7/8≤m/r≤31/32, with
constants independent of the pair. Their h and positive a coincide.
Their finite S has the identical phase, exponent m and weight zero at
log(jk)=2r. Thus no limiting cutoff convention or approximation of a
is needed. In the positive scale the exponent is N=m+1, x₀=N/(2r),
A=m!/(2r)^m and the denominator is sqrt(2πλ), exactly as in L457.
Its audited λ≥2r and positive real x* ensure the stated positive
Gaussian scale; the assumed nonvanishing ensures its zeta factor is
nonzero. Its bound on |log M*| gives the lower bound used in (5).
The full L457 remainder includes both residues and all contour tails;
L458's remainder includes every sector and cutoff contribution.

**Normalization and reality.** L458's exact coefficient identity is
4D_{m/2}=2^(m+1)I/m!, hence D_{m/2}=2^(m−1)I/m!.
Its positive-sector coefficient π/(2a) is doubled exactly once by
same-sign reflection. These give precisely P in the statement. The
factorial in M* is part of the arithmetic normalization and is not
another theta coefficient to cancel or insert. All factors of P are
positive. Swapping j,k makes S real, while the original real theta
identity makes D and ε real; consequently δ is real as required by
the final inequality, not merely bounded as a complex error.

**Complete relative comparison.** Division gives exactly
D/(PM*)−1=δ+ε/M*, so the bound is C_A f+q, with q as in (5).
For a direct check of its rate, choose one eventual real-r threshold
such that

    K r^(2/3)≤r/800,
    log C_E+2log(1+r)+(1/2)log r≤r/800.

Both inequalities hold for every sufficiently large real r, since
their left sides divided by r tend to zero. They give

    log(r^(1/2)q)≤−r/400,
    q/f≤exp(−r/400)/(log r)^3→0.

Thus the stated relative rate retains the entire additive error even
if M* is as small as its allowed lower bound. It does not presume a
polynomial lower bound or fixed-center freezing. Also f→0. Taking
the maximum of these thresholds, the two input onsets, a threshold
for the definition of x*, and thresholds for C_A f≤1/4, q≤1/4 and
q≤f yields one R independent of m. This verifies C=C_A+1 in (1)
and the real lower bound 1−1/4−1/4=1/2 in (2). Dividing the
complete normalized theta error by the guaranteed lower margin gives
at most 2q→0. Closed band endpoints and integer cutoff transitions
require no separate limiting argument.

This is validation of an existing conditional input, not an additional
sign range or progress beyond the assessed source methods. The direct
mathematical inputs remain L457 and L458. L323/L327/L456 failures
retain their scopes. No every-height transfer, initial-index completion,
bounded-height extension or global mixed positivity is obtained. The
external premise remains precisely the pinned strict-half-plane theorem
in the Hypotheses, with its pole and unaudited-import qualifications.

## Mathlib

Full matching coverage has not been checked; absence is not asserted.
The elementary exponential-versus-power comparison is proved here.
Underlying analytic-logarithm, contour and theta coverage remains as
qualified in L457 and L458. The external artifact
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` is not asserted to
be a Mathlib theorem or a locally compiled/import-audited input.
