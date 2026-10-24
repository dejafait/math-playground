# Corollary 452a: eventual positive coupled-endpoint Laguerre margin

**Hypotheses.** Let n tend to infinity through positive integers and put

    r=2n,  a=a_n=sqrt(4π²exp(4r)−25),
    τ=(1/2)arctan(a/5),  Φ_*=2n log r+9r−5−2aτ,
    c=1/2+1/r,  σ=1+1/r,  C₀=(8π²)²,
    B_r=|ζ(σ+ia_n)|²,  E_r=(1+r)²exp(−r/256).

Use the actual theta transform Ξ, its coefficients defined by
Ξ(a+iy)Ξ(a−iy)=Σ_(j≥0)D_j(Ξ;a)y^(2j), and the whole-plane
integral I_n of L302. Use Z_r(a_n;c) of L303. Assume the precise
external input of L452: OpenAI, *The Quasi-Riemann Hypothesis:
A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
in its zeta specialization. Its conclusion is nonvanishing for
Re(s)>7/8, allowing the pole at 1; boundary zeros are not excluded.
The [pinned source and verification qualifications](../foundations/2026-10-quasi-riemann-input.md)
remain load-bearing. The external manuscript's full proof and formal
import closure have not been independently audited locally.

**Conclusion.** Define the explicitly positive multiplier

    P_n=[2^(2n−1)/(2n)!] C₀ exp(Φ_*) π/a_n.

Then, with constants independent of n,

    D_n(Ξ;a_n)/(P_n B_r)=1+O(r^(−1/6)).                    (1)

In particular there is one integer n₀ such that for every n≥n₀,

    D_n(Ξ;a_n)/P_n ≥ B_r/2 ≥ 1/[2(r+1)²] >0.             (2)

The corresponding I_n bound is
I_n(a_n)/[C₀exp(Φ_*)π/a_n]≥B_r/2. The normalized positive
margin dominates the complete sector/cutoff error scale:

    [1/(2(r+1)²)]/E_r=exp(r/256)/[2(r+1)^4] →∞.           (3)

The constants and common onset are existential, not numerically
evaluated. This is an application of L330's existing conditional
margin implication using audited L452, not a new positivity
principle or an independent zero-free theorem. The conclusion is
restricted to these paired indices and heights. The separate critical
audit below validates this assembly under its stated external input;
it is a partial result, not a complete candidate resolution of RH.

**Proof.** All uses below are at exactly the parameters in the
Hypotheses. In particular c>1/2, σ>1, r=2n, and a_n>0. The
Mellin integral in L303 is therefore absolutely convergent even
though c varies with r, and is real. The latter follows from its
exact finite phase-sum identity and interchange of the two indices;
it does not require a positive Mellin kernel or conjugacy of the
two zeta factors away from the central height.

The audited estimate L452 (2), applying L330's relative freezing
bound to both heights a_n+v and −a_n+v, supplies fixed C_F and an
eventual onset such that

    Z_r(a_n;c)=B_r(1+δ_n),  δ_n real,
    |δ_n|≤C_F r^(−1/6).                                  (4)

Here B_r>0 because σ>1. L452 includes the entire complement of
the shrinking Mellin window in (4). Its superpolynomial tail is
compared with B_r before (4) is obtained; no comparison of that
tail directly with E_r is needed.

For the lower bound, L304 uses the absolutely convergent reciprocal
Euler series on σ>1:

    |1/ζ(σ+ia_n)|≤Σ_(m≥1)|μ(m)|m^(−σ)
                 ≤ζ(σ)≤1+∫_1^∞x^(−σ)dx=r+1.

Consequently B_r≥(r+1)^(−2). This uses neither continuation of
the reciprocal series left of 1 nor a lower bound at a zero.

L303 (2), including its cutoff replacement of L302, gives a fixed
C_E and an eventual onset with

    I_n(a_n)/[C₀exp(Φ_*)π/a_n]=Z_r(a_n;c)+ε_n,
    ε_n real,  |ε_n|≤C_E E_r.                            (5)

The finite-index replacement error O(r exp(−9r/128)) is already
included here: its ratio to E_r is
r/(1+r)²·exp(−17r/256)→0. L302's complete six-region sector
error, including both mixed sectors and both same-sign strips,
is also included in (5). Thus no region or cutoff error is omitted.
By L302 (2) the conversion from I_n to D_n is exactly
2^(2n−1)/(2n)!, so (4) and (5) imply

    D_n(Ξ;a_n)/P_n=B_r(1+δ_n)+ε_n,
    |ε_n|/B_r≤C_E(r+1)^4exp(−r/256).                     (6)

Every factor of P_n is positive. Its factor π/a_n already includes
the same-sign reflection factor and coordinate Jacobian accounted
for in L302; there is no additional factor of two. The factorial
conversion is the coefficient-extraction normalization inherited
there, not an application of L269's proportional-index asymptotic
at this endpoint.

The second bound in (6) is o(r^(−1/6)), because any fixed power
of r is dominated by exp(r/256). Dividing the first identity in
(6) by B_r proves (1). More explicitly, choose one n₀ beyond all
the onsets already used and large enough that for every n≥n₀

    C_F r^(−1/6)≤1/4,
    C_E(r+1)^4exp(−r/256)≤1/4.

Such a common onset exists by the two limits. Equation (6) then
gives D_n/P_n≥B_r(1−1/4−1/4)=B_r/2, proving (2).
Equation (3) is the same elementary threshold comparison already
isolated conditionally in L330. This completes the approved
endpoint assembly under the cited external hypothesis. ∎

The historical L304 coefficientwise loss and L330 countermodels
remain valid on their stated hypotheses; the new input is the
audited fixed-domain estimate (4). Fixed-r arbitrary-height and
arbitrary-prime-phase obstructions do not have these coupled
quantifiers. No rounding from a_n to every height is justified.
Smaller indices, bounded exterior heights, every-height passage,
all-degree mixed positivity, selected-law realization and the
full-error regulator margin remain unresolved. No new zero-free
region or RH conclusion follows from this partial sign result.

### Critical audit — 2026-10-23

**Verdict and scope.** Equations (1)–(3) pass the separate mathematical
audit. No correction or additional mathematical hypothesis is required.
This validates an application of audited L452 and L330's conditional
consequence, with no new principle beyond that source mechanism. The
precise September 30, 2026, Theorem 1.1 and pinned commit in the
Hypotheses remain assumed. Neither its manuscript nor its formal
import closure is certified here. The verdict is conditional on that
input and has no boundary-nonvanishing or RH implication.

**Parameters and reality.** For each positive integer n, r=2n and
a_n>0. The definitions give n/r+9/2=5 and
2πexp(2r+2iτ)=5+ia_n, exactly L302's parameters. The c and σ in
L303, L304, L330 and L452 agree, with σ=1/2+c>1. L303's
absolute-integrability argument is parameterwise; its majorant need
not be uniform as c decreases to 1/2. Its exact finite full-sum
identity with symmetric real weights proves Z_r real. Equivalently,
conjugation and v↦−v preserve the vertical integral. The zeta
factors at v≠0 are not treated as conjugates. The original I_n is
real by conjugation and t↦−t, so both δ_n and ε_n are real.

**Exact multiplier.** In L267 the whole-line transform F=2Ξ gives

    4D_n=1/(2n)! ∫∫(v−u)^(2n)k(u)k(v)e^(ia(u+v))du dv.

Evenness permits v↦−v. Then u=s+t, v=s−t has absolute Jacobian
2 and contributes (2s)^(2n), yielding exactly
4D_n=2^(2n+1)I_n/(2n)!. Polynomially weighted exponential
domination justifies coefficient extraction and substitution.
L269's t-contour shift is a parameterwise identity on τ<π/4;
its proportional-index asymptotic is not used. L302's positive
interior has factor π/(2a_n), and s↦−s doubles it. Its sector
formulas already include the coordinate Jacobian, leaving π/a_n
with no extra factor of two. Every factor in P_n is finite, real
and strictly positive, even when exp(Φ_*) is extremely small.

**Complete errors and constants.** Audited L452 (2) gives a fixed
C_F and one onset valid for every sufficiently large n. Both shifted
heights are retained in L330, with M_r=O(r^(1/3)). The full
relative Mellin tail is

    O((r+1)^4exp(−(log r)^2/8))=o(r^(−1/6)):

the logarithm of its scale divided by r^(−1/6) is
−(log r)^2/8+(25/6)log r+O(1)→−∞. It is compared with B_r,
not with E_r. For the separate additive error, L302 includes the
interiors, both same-sign strips and both mixed sectors. Its other
exponential rates in r are 1/5, 1/32, 1 and log 2−1/2, each
larger than 1/256. Thus E_r absorbs every sector error. L303's
cutoff replacement has ratio r(1+r)^(−2)exp(−17r/256)→0
to E_r. The identity and cutoff bound hold uniformly in a, so
c=c(r) creates no extra constant in (5). There is one fixed C_E
for the complete additive error.

The reciprocal Euler bound is used only at σ>1, giving
B_r≥(r+1)^(−2)>0. The complete comparison is therefore

    |D_n/(P_n B_r)−1|
      ≤C_F r^(−1/6)+C_E(r+1)^4exp(−r/256).

The second scale divided by r^(−1/6) has logarithm
−r/256+(25/6)log r+O(1)→−∞. Each summand is at most 1/4
for every n beyond one common integer onset, proving (2). No
subsequence or numerical onset is claimed. The lower margin
divided by E_r has logarithm r/256−4log(r+1)−log 2→∞,
which also verifies (3).

Old coefficientwise and old-envelope failures do not contradict
the additional L452 hypothesis. Fixed-r arbitrarily late negative
arithmetic values do not contradict the coupled r,a_n claim.
No rounding estimate, smaller-index signs, global mixed positivity
or selected-law/regulator conclusion is obtained. L331's local
saddle is unnecessary and supplies no hidden premise.

**Mathlib.** Full matching statement: not checked; no absence is
asserted. L452 records supporting Euler-log coverage and distinguishes
the pinned supplied Lean artifact from Mathlib and from a locally
verified build. The reciprocal-series lower bound, complete
whole-plane formula, coefficient normalization and relative freezing
are the existing local inputs used above. No additional Mathlib
coverage or external-proof verification is claimed by this assembly.
