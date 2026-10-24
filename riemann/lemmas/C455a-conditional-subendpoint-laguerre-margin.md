# Corollary 455a: conditional uniform subendpoint Laguerre margin

## Hypotheses

Use the actual theta transform Ξ with
Ξ(a+iy)Ξ(a−iy)=Σ_{n≥0}D_n(Ξ;a)y^(2n). Assume the zeta
specialization of OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re s > 7/8*, September 30, 2026,
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
This is the same pinned external premise as L454: nonvanishing on
Re(s)>7/8, allowing the pole at 1, with no boundary assertion.
The [external-input register](../foundations/2026-10-quasi-riemann-input.md)
records its unaudited manuscript and local formal import-closure limits.
This corollary does not independently verify that premise.

Let r be positive real and m a positive even integer, with

    31/32≤m/r≤63/64, n=m/2,
    h=9/2+m/(2r), a=sqrt(4π²exp(4r)−h²)>0,
    τ=arctan(a/h)/2, Φ_*=m log r+9r−h−2aτ,
    C₀=(8π²)², σ=(1+m/r)/2, B=|ζ(σ+ia)|²,
    P_{r,m}=[2^(m−1)/m!]C₀exp(Φ_*)π/a.

Use L454 and L455 at these identical parameters. In particular their
full finite sum is exactly

    S=Σ_{j,k≥1}(jk)^(−1/2)(1−log(jk)/(2r))_+^m
                                    exp(ia log(k/j)),

with zero weight when log(jk)≥2r, including equality.

## Conclusion

There are fixed positive constants C,C_B,R, independent of r,m on
this closed band, such that for every admissible r≥R,

    |D_{m/2}(Ξ;a)/(P_{r,m}B)−1|≤C r^(−1/6),            (1)
    D_{m/2}(Ξ;a)/P_{r,m}≥B/2
                          ≥(1/2)exp(−C_B r^(1/3))>0. (2)

The entire sector/cutoff error is negligible relative to the stated
lower margin. Constants and onset are existential, not numerically
evaluated. This local REPRODUCTION assembles already audited inputs;
the separate critical audit below validates this assembly. It is a conditional partial
result, not a complete candidate resolution of RH. No arbitrary
unpaired-height sign, smaller-index completion, bounded-height
extension, mixed positivity or zero-exclusion range is asserted.

## Proof

The approved scope is the
[assembly assessment](../drafts/literature/2026-10-23-subendpoint-laguerre-assembly-coverage.md).
No Mellin or stationary-phase mechanism is reproved: their audited
uniform conclusions in L454 and L455 are used only on their common
domain. This elementary comparison is needed because neither input
alone states the Laguerre sign.

L454 gives fixed constants C_A,C_B>0 and R_A such that, for every
admissible r≥R_A,

    S=B(1+δ), |δ|≤C_A r^(−1/6),
    B≥exp(−C_B r^(1/3))>0.                            (3)

The sum S is real: interchange j,k in the finite sum to conjugate it.
Thus δ is real. Crucially 63/64≤σ≤127/128<1; the lower bound in
(3) is L454's analytic-logarithm bound under the pinned input, not
an Euler or reciprocal Dirichlet bound below one.

L455 supplies fixed C_E>0 and R_E on exactly the same domain with

    D_{m/2}(Ξ;a)=P_{r,m}(S+ε), ε real,
    |ε|≤C_E E(r), E(r)=(1+r)²exp(−r/200).             (4)

This ε includes the full same-sign interiors, moving boundary strips,
clipped patches, mixed sectors, reflection and cutoff errors. No
additional sector error needs to be added to (4). The definitions
of S, h and a coincide exactly in the two inputs, including cutoff
equality. P_{r,m} is positive since a,r>0, m!>0 and C₀>0.
The π/a factor already includes the single same-sign reflection;
2^(m−1)/m! is L455's exact coefficient normalization. No further
factorial or factor of two is introduced.

Dividing (4) by P_{r,m}B and using (3) gives

    D_{m/2}/(P_{r,m}B)=1+δ+ε/B,
    |ε|/B≤q(r):=C_E(1+r)²exp(−r/200+C_B r^(1/3)).    (5)

For every fixed p≥0,

    log(r^p q(r))/r
      =log(C_E)/r+2log(1+r)/r+p log r/r
                         −1/200+C_B r^(−2/3) →−1/200.

Hence r^p q(r)→0; in particular q=o(r^(−1/6)) and q→0.
This calculation compares the complete additive error with the
non-Euler lower bound, uniformly in m, rather than comparing two
unnormalized errors. Equations (3) and (5) prove (1).

For explicit uniform quantifiers choose R_Q so that, for every
real r≥R_Q,

    r/200−C_B r^(1/3)−2log(1+r)≥log(4C_E).

Such R_Q exists by the displayed limit. It gives q(r)≤1/4.
Take R at least R_A, R_E, R_Q and (4C_A)^6, enlarging it if
needed for the hypotheses a>0 and m>0. These are finitely many
fixed thresholds independent of m. Then |δ|≤1/4 and |ε|/B≤1/4,
so the real identity (5) gives D_{m/2}/(P_{r,m}B)≥1/2.
This proves (2) for every admissible pair beyond one onset, including
both closed band endpoints and cutoff transitions. Also

    [(1/2)exp(−C_B r^(1/3))]/E(r)
      =exp(r/200−C_B r^(1/3))/[2(1+r)²] →∞,

so the stated margin dominates the complete additive error scale.

L323's larger-strip summed-modulus obstruction and L327's
phase-uniform PSD obstruction are preserved: neither certificate is
used here. L454 controls actual zeta at the coupled height, while
L455 retains the original signed arithmetic sum. This does not
contradict fixed-r/arbitrary-phase negative examples. Smaller indices,
bounded exterior heights, global mixed positivity and the independent
selected-law/regulator gaps remain open. ∎

### Separate critical audit — 2026-10-23

**Verdict.** Conclusions (1)–(2) pass on their stated coupled domain,
conditional on the precise external premise in the Hypotheses and the
audited L454/L455 inputs. No repair of a mathematical claim or new
assumption is needed. The unchanged
[audit assessment](../drafts/literature/2026-10-23-subendpoint-laguerre-margin-critical-audit-coverage.md)
covers this check. This is validation of a local reproduction, not a
new source theorem, external-manuscript verification or RH resolution.

**Identical domain and sum.** Substitution of the two closed endpoints
gives h in [319/64,639/128] and σ in [63/64,127/128]. These are
exactly the ranges in the audited inputs. Both use positive real r,
positive even m, the same positive square root defining a and the
same exponent m in the complete double sum. Its support is finite
because jk<exp(2r); equality has weight zero since m>0. Thus no
cutoff term, endpoint half-weight, rounding restriction or change of
phase is hidden in passing from L454 to L455. Exchanging j,k proves
S is real even at a cutoff transition. The arithmetic estimate is
used only at the same coupled height a, not at arbitrary heights
with r fixed.

**The denominator and all errors.** L454 Section 1 supplies
B≥exp(−C_B r^(1/3)) directly from its analytic logarithm; its
proof bounds both signs of the real part of that logarithm. This is
a lower bound for B itself, not just for S. Squaring the modulus
and replacing log a by O(r) only enlarge a fixed C_B. Since σ<1,
an absolutely convergent reciprocal Euler series would not justify
this step and is not used. L454's relative error already includes
both shifted-line residues and all Mellin tails. L455 (1)–(2)
already include both same-sign regions, strips, patches, mixed
sectors and cutoff errors. Consequently the entire assembled relative
error is δ+ε/B, with no additional omitted term, and its absolute
value is at most C_A r^(−1/6)+q(r) from (5).

For every fixed p≥0 the displayed logarithmic limit in the proof
is strictly negative. In particular, eventually
log(r^p q(r))≤−r/400, which proves the claimed limit rather than
merely a boundedness statement. Taking p=1/6 and p=0 checks both
the relative rate and the positive margin. All constants here are
fixed independently of m. Equivalently, the complete additive error
divided by the stated lower margin is at most 2q(r)→0; this
comparison includes C_E and not only its exponential scale.

**One real-r onset.** To make both conclusions hold with the same
explicit choice of thresholds, let R_rate give q(r)≤r^(−1/6)
for every real r≥R_rate and let R_Q be the proof's threshold
giving q(r)≤1/4. Take the maximum of R_A,R_E,R_rate,R_Q,
(4C_A)^6 and 1, enlarged if needed to ensure the stated positive
square root. All are fixed thresholds. On this ray (1) holds with
C=C_A+1, and the real identity gives (2) since each error has
absolute value at most 1/4. No monotonicity of q at small r, sequence
of sample heights or m-dependent onset is needed. Enlarging the
proof's existential R to include R_rate changes no assertion.

**Exact normalization.** L455's parameterwise coefficient identity
is D_{m/2}=2^(m−1)I_{m/2}/m!. Its audited normalization can also
be checked in the L267 identity inherited through L269: the two
whole-line transforms contribute 4D_{m/2}, evenness changes their
difference variable to the sum variable, and u=s+t,v=s−t has
Jacobian 2 and power (2s)^m. Thus 4D_{m/2}=2^(m+1)I_{m/2}/m!.
L455 already doubles the positive same-sign coefficient π/(2a)
once by reflection, obtaining π/a in I_{m/2}. Multiplying these
two identities gives exactly P_{r,m}, with a single m! and no
extra reflection factor. Every factor of P is real and strictly
positive, so division preserves the claimed sign. These are checks
of L455's inherited identities, not additional independent inputs.

The direct uses remain L454 and L455; no DAG change is needed.
The external manuscript and formal import closure remain unaudited.
The L323 strip-modulus and L327 phase-uniform PSD stops are untouched,
as are fixed-r/arbitrary-phase negatives. This audit establishes no
unpaired-height extension, initial low-index completion, bounded-height
result, mixed positivity or zero-exclusion consequence. The argument
in the overview is unchanged; its current audit verdict is recorded here.

## Mathlib

Full matching Mathlib coverage has not been checked; absence is not
asserted. The elementary exponential-versus-power comparison is
proved above without an unverified library claim. The underlying
analytic-logarithm and theta-sector coverage remains as qualified
in L454 and L455. The external supplied theorem
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` is not asserted to
be Mathlib membership or a locally compiled/import-audited input.
