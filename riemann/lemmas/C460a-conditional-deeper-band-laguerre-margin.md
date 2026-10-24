# Corollary 460a: conditional uniform deeper-band Laguerre margin

## Hypotheses

Use the actual theta transform Ξ with normalization
Ξ(a+iy)Ξ(a−iy)=Σ_{n≥0}D_n(Ξ;a)y^(2n). Assume the zeta
specialization of OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re s > 7/8*, September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
This is exactly L459's external premise: strict Re(s)>7/8,
allowing the pole at 1 and asserting nothing on the boundary.
Retain the [external-input register's qualifications](../foundations/2026-10-quasi-riemann-input.md):
the external manuscript and complete formal import closure have not
been independently audited locally. No such audit is supplied here.

Let r>0 be real and m a positive even integer with

    13/16≤m/r≤7/8, n=m/2,
    h=9/2+m/(2r), a=sqrt(4π²exp(4r)−h²)>0,
    τ=arctan(a/h)/2, Φ_*=m log r+9r−h−2aτ,
    C₀=(8π²)², P_{r,m}=[2^(m−1)/m!]C₀exp(Φ_*)π/a.

Use L459 and L460 at these exact parameters, with

    S=Σ_{j,k≥1}(jk)^(−1/2)(1−log(jk)/(2r))_+^m
                                             exp(ia log(k/j)).

The weight is zero for log(jk)≥2r, including equality. Put
N=m+1, x₀=N/(2r), d=1/4096 and

    H(x)=2rx−N log x+log|ζ(1/2+x+ia)|².

For sufficiently large r let x* be L459's unique real stationary
point in [x₀−d,x₀+d], λ=H''(x*) and define exactly

    A=m!/(2r)^m,
    M*=A exp(2rx*) (x*)^(−N)|ζ(1/2+x*+ia)|²
                                             /sqrt(2πλ)>0.

The square root is positive real. Constants and onsets below are
existential, uniform over this entire closed band.

## Conclusion

There are fixed C,K,R>0 such that every admissible pair with r≥R
satisfies

    |D_{m/2}(Ξ;a)/(P_{r,m}M*)−1|≤C(log r)^3/sqrt(r), (1)
    D_{m/2}(Ξ;a)/P_{r,m}≥M*/2
                                 ≥(1/2)exp(−K r^(15/16))>0. (2)

The complete normalized additive theta error is negligible relative
to the guaranteed lower margin in (2). This is a conditional partial
result and local REPRODUCTION of assessed methods; the separate critical
audit below validates this conditional assembly. It is not an RH candidate or a discovery beyond the
sources checked. It supplies no every-height transfer, initial-index
completion, bounded-height extension, global mixed positivity or
zero-exclusion conclusion.

## Proof

The prior SPECIALIZE [exact assembly assessment](../drafts/literature/2026-10-24-deeper-band-laguerre-assembly-coverage.md)
covers this application of the audited inputs. C458a gives the method
on a narrower band but its theorem is not applied on this domain.
The elementary comparison is necessary because neither L459 nor L460
alone states the combined inequality. No saddle or sector theorem is
reproved and no external premise is strengthened.

L459 supplies fixed K,C_A,R_A>0, independent of the admissible pair,
with

    S=M*(1+δ), |δ|≤C_A f(r), f(r)=(log r)^3/sqrt(r),
    M*>0, |log M*|≤K r^(15/16).                      (3)

Its arithmetic remainder includes both original residues and the
entire deformed contour. In particular M*≥exp(−K r^(15/16)).
This is the factorial-normalized moving-saddle scale, not a
fixed-center zeta square. No reciprocal Euler estimate below one
is required. Swapping j,k conjugates each term of the finite S and
preserves weight and support. Thus S and δ are real.

L460 supplies fixed C_E,R_E>0 on exactly the same positive-real-r,
positive-even-m closed-band domain with

    D_{m/2}(Ξ;a)=P_{r,m}(S+ε), ε real,
    |ε|≤C_E E(r), E(r)=(1+r)²exp(−r/200).            (4)

The two definitions of h,a,S agree exactly; neither a nor the cutoff
is approximated. This is the whole error, including all sectors,
boundaries, clipped patches and cutoff contributions. P is positive:
its π/a includes one same-sign reflection, and its 2^(m−1)/m!
is the exact theta coefficient factor. The separate factorial in M*
is part of the arithmetic scale. No factor is inserted or removed.

Divide (4) by P M* and apply (3). Exactly,

    D_{m/2}/(P M*)−1=δ+ε/M*,
    |ε|/M*≤q(r):=C_E(1+r)²exp(−r/200+K r^(15/16)). (5)

For each fixed t≥0 and r>1,

    log(r^t q(r))/r
       =[log C_E+2log(1+r)+t log r]/r
                                      −1/200+K r^(−1/16)
       →−1/200.

Consequently, for each fixed t, eventually
log(r^t q(r))≤−r/400, and r^t q(r)→0. In particular
q=o(r^(−1/2))=o(f(r)) for r≥e, and q→0. Also f→0:
putting u=log r gives f=u³ exp(−u/2).
This proves the desired relative rate with the entire additive error,
even at the smallest M* allowed by (3).

To retain one uniform onset, choose fixed real thresholds R_rate,
R_δ,R_q for, respectively, q≤f, C_A f≤1/4 and q≤1/4, holding
for every real r beyond the corresponding threshold. The limits
just proved ensure their existence. Let R be the maximum of these
thresholds, R_A,R_E and e, enlarged for L459's definition of x* and
the positive square root a if needed. All thresholds are independent
of m. Equation (5) then gives (1) with C=C_A+1, and its reality gives

    D_{m/2}/(P M*)≥1−1/4−1/4=1/2.

Together with (3) this proves (2). Both closed band endpoints and
all integer cutoff transitions are included by the input domains.
Moreover the entire normalized theta error divided by the guaranteed
lower margin in (2) is bounded by

    C_E E(r)/[(1/2)exp(−K r^(15/16))]=2q(r)→0.

Thus the achieved lower margin exceeds the required complete error;
no effective numerical onset is claimed.

L323's larger-strip failure, L327's phase-uniform PSD obstruction and
L456's fixed-center certificate failure keep their scopes. This proof
retains the full signed S at the coupled height a(r,m) and uses the
moving saddle. It asserts no arbitrary-height or arbitrary-prime-phase
positivity with r fixed. A separately assessed every-height transfer
is a plausible downstream use; initial low-index signs, bounded
heights, mixed positivity and selected-law/regulator realization remain
independent unresolved obligations. ∎

### Separate critical audit — 2026-10-24

**Verdict and scope.** Equations (1)–(2) pass on the full stated closed
band without a statement repair or additional hypothesis. The prior
SPECIALIZE [audit assessment](../drafts/literature/2026-10-24-deeper-band-laguerre-margin-critical-audit-coverage.md)
covers this REPRODUCTION audit. It checks the application of the audited
L459 and L460, not their external manuscript/import closure or a new
saddle or sector theorem. C458a's audit supplies a comparison method;
its narrower-domain theorem is not used here.

**Exact interfaces and positive scales.** Both inputs quantify over
every sufficiently large positive real r and positive even integer m
in exactly 13/16≤m/r≤7/8. Their h, positive square root a and finite
signed S agree, including phase orientation, exponent m and zero weight
at log(jk)=2r. No discretization of r, replacement of a or cutoff limit
enters. L459 uses exactly N=m+1, x₀=N/(2r), d=1/4096,
A=m!/(2r)^m and the positive sqrt(2πλ). Its λ≥2r ensures the
denominator is positive. Also

    x*≥x₀−d≥13/32−1/4096>3/8.

Thus Re(1/2+x*+ia)>7/8 and a>0, so the pinned external premise
makes the zeta factor nonzero and the pole at 1 is avoided. All other
factors in M* are positive. The two-sided bound on log M* gives
M*≥exp(−K r^(15/16)); the weaker lower bound stated separately for
S in L459 is not substituted for this bound on M*.

L460's exact coefficient identity is 4D_{m/2}=2^(m+1)I/m!.
Its positive same-sign sector has coefficient π/(2a); reflection doubles
that contribution once to π/a. These give exactly the stated positive
P=[2^(m−1)/m!]C₀exp(Φ_*)π/a. The m! already present in M* is
its arithmetic normalization; no further theta factor is introduced.
Swapping j,k proves S is real, and the real theta coefficient and
positive P make ε real. Since M*>0, δ=S/M*−1 is real as well.

**Entire relative error and rate.** L459's relative remainder already
includes both original residues and every part of its deformed contour.
L460's additive remainder already includes all sectors, boundaries,
clipped patches and cutoff contributions. Their exact substitution is
D/(PM*)−1=δ+ε/M*, with bound C_A f+q from (5). There is no
discarded additive term. To check the claimed rate directly, take
C_E>0 and K>0 enlarged if necessary, and choose an eventual real-r
threshold for both inequalities

    K r^(15/16)≤r/800,
    log C_E+2log(1+r)+(1/2)log r≤r/800.

Each left side divided by r tends to zero. The first can, for example,
be ensured by r≥(800K)^16, without asserting a known numerical K.
Consequently

    log(sqrt(r) q)≤−r/200+r/800+r/800=−r/400,
    q/f≤exp(−r/400)/(log r)^3→0.

This checks the full relative budget at the smallest scale permitted
by the input. In particular no polynomial lower bound, fixed-center
freezing or reciprocal Euler estimate left of one is assumed. The
different exponent 15/16 affects the existential onset but leaves
strict exponential domination intact.

**One onset and strict margin.** Both input statements supply uniform
constants and onsets on the closed band. Take the maximum of those
onsets, the saddle-definition and positive-a thresholds, the comparison
thresholds above, e, and thresholds for q≤f, C_A f≤1/4 and q≤1/4.
These are finitely many constants independent of m and hold for all
real r beyond their maximum. They yield C=C_A+1 in (1) and, using
reality, D/(PM*)≥1−1/4−1/4=1/2 in (2). The full normalized
theta error divided by the guaranteed lower margin is at most 2q→0.
Neither closed band endpoint nor any integer product-cutoff transition
needs an additional limit. No effective or practical onset is claimed.

The direct mathematical inputs remain L459 and L460. This audit
validates the existing conditional partial result, not an additional
sign range or progress beyond the assessed methods. The pinned external
premise remains strict Re(s)>7/8, with the allowed pole and locally
unaudited manuscript/import closure. The L323/L327/L456 stops keep
their original scopes. Every-height transfer, initial low-index signs,
bounded heights, global mixed positivity and selected-law/regulator
realization remain unresolved. No RH candidate follows.

## Mathlib

Full matching Mathlib coverage has not been checked; absence is not
asserted. The elementary exponential-versus-power comparison is proved
above. Supporting analytic-logarithm, contour, factorial and theta
coverage retains L459/L460's qualifications. The external artifact
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` is not asserted to be
a Mathlib theorem or a locally built/import-audited result.
