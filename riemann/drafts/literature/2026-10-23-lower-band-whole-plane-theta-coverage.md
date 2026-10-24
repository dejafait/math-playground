# Coverage: lower-band whole-plane theta reduction

TARGET: Attempt a uniform whole-plane theta reduction to L457's arithmetic sum on 7/8≤m/r≤31/32, with exact positive normalization and additive error O(r^K exp(-b r)) for fixed K and b>0.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed subendpoint theta-sector search and critical-audit source comparison; searched the changed target with queries recorded below and compared L455's complete proof/audit, C294b's complete proof, L269's parameterwise contour passage, L457's exact interface and L323/L327's statements and failure records. No inspected matching whole-plane theorem or duplicate lower-band conclusion was found; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Csordas, arXiv:1309.0055v2 (21 February 2014), https://arxiv.org/html/1309.0055v2, Theorem 3.5, Lemma 3.6 and Theorem 3.7, equations (3.7)–(3.14), statements and proofs; NIST DLMF https://dlmf.nist.gov/2.3#iv, hypotheses (a)–(d), 2.3.21–2.3.23, and https://dlmf.nist.gov/7.2#iii, 7.2.6–7.2.9. Relevant primary passages reopened on 2026-10-23; reused the earlier full L324/L325 comparison and the October overlap/input register rather than reopening external zero-free proofs.
COMPARISON: L455 states only 31/32≤m/r≤63/64, but its explicit smaller-strip proof exposes broader mass, tail, translated-variation and patch estimates. C294b already covers the new h interval. Known sources cover these mechanisms and the coefficient identity, not the changed-band uniform conclusion; the necessary difference is an explicit uniform-domain recheck and complete assembly.
GAP: Recheck every parameter use, especially L455 (12)'s stated beta interval, and prove one full normalized exponentially decaying error on the closed lower band with all discrete cutoffs, clipped patches, moving edges, factorial/reflection factors and one common onset. This review proves no changed-band bound or sign.
REASON: Essential source comparison is complete and no unread general error theorem is needed for the explicit local method. A bounded specialization attempt is justified after separate supervisor approval; citing L455's narrower conclusion alone is insufficient.
SCOPE: Positive real r tending to infinity, positive even m, 7/8≤m/r≤31/32, h=9/2+m/(2r), a=sqrt(4*pi^2*exp(4r)-h^2)>0 and exactly L457's finite signed sum, including zero weight at the product cutoff. Theta reduction only; no arithmetic sign assembly, every-height transfer, smaller-index completion or RH conclusion.
LITERATURE_REASON: The saved target changes L455's closed proportional band; the existing assessment did not yet compare its parameter-dependent sector bounds on this domain. L457's ready arithmetic assessment does not cover the missing theta reduction.

## Completed source comparison

The action at invocation start was “Assess a uniform whole-plane theta
reduction to L457's arithmetic sum on 7/8≤m/r≤31/32, with exact positive
normalization and additive error O(r^K exp(-b r)) for fixed K and b>0.”
This literature-only step preserves that research target and completes
its coverage assessment. The mathematical continuation above is newly
ready and receives a separate supervisor approval next turn. No estimate
on the changed band is derived or critically validated here.

The main gap is the initial low-index signs and global mixed positivity.
The intermediate target is an additive theta reduction with a fixed
exponentially decaying normalized error. Its plausible downstream use
is a separately assembled conditional coupled Laguerre sign band, by
comparison with L457's audited exp(-C r^(2/3)) margin. That arithmetic
margin does not imply a theta error estimate. Every-height passage,
smaller indices and bounded heights remain independent obligations.

## Primary evidence and reuse limits

Reuse [the prior sector comparison](2026-10-23-subendpoint-theta-sector-reduction-coverage.md)
and [its audit coverage](2026-10-23-subendpoint-uniform-sector-critical-audit-coverage.md).
Csordas, [*Fourier transforms of positive definite kernels and the Riemann
ξ-Function*, v2](https://arxiv.org/html/1309.0055v2), Theorem 3.5,
assumes an admissible kernel and strict logarithmic concavity on the
positive half-line. Its proof treats s<t and s>t separately to prove
associated-kernel admissibility. Lemma 3.6 and Theorem 3.7, (3.10)–(3.14),
give the double-integral coefficient identity, retaining the Jacobian
and factorial. The real-zero criterion still requires positive
definiteness at every level. These statements and proofs were reopened;
they provide no signed uniform-sector estimate. Reuse the previous
theta-kernel applicability comparison and retain its whole-line
transform normalization, rather than importing a positivity conclusion.

[DLMF §2.3(iv)](https://dlmf.nist.gov/2.3#iv), (a)–(d) and
(2.3.21)–(2.3.23), was reopened through the full relevant hypotheses:
smooth real phase and amplitude, positive phase derivative off the
stationary endpoint, differentiable endpoint expansions, and finite
endpoint limits or uniform convergence of the stated integrals at an
infinite endpoint. Both finite endpoints contribute. This is source
context, not a theorem uniform in growing theta indices or clipped
domains. [DLMF §7.2(iii)](https://dlmf.nist.gov/7.2#iii),
(7.2.6)–(7.2.9), supplies scalar Fresnel definitions and limits.
The existing explicit real phase change and rectangular variation
argument are therefore the covered method for the proposed attempt.
Olver/Lyness and the earlier SIGMA search lead remain unread, unimported
references; none is essential to that explicit method. Access date is
2026-10-23; no unobserved source release number is asserted.

The prior comparison of shifted Jensen/Maclaurin results is unchanged:
those conclusions do not control these original-Ξ real-height sectors.
The [October overlap review](2026-10-21-openai-quasi-rh-overlap.md) and
[external-input register](../../foundations/2026-10-quasi-riemann-input.md)
were read and reused. No new zero-free result, Euler-series continuation
or external-proof certification is needed for the theta target.

## Changed-band comparison and precise proof obligations

Read L455's complete proof, Sections 1–6, and separate critical audit.
Its hypotheses remain narrower than the target. The proposed h interval
is [79/16,319/64], inside C294b's [39/8,5]; the new beta=1−m/r interval
is [1/32,1/8]. These are domain comparisons, not a proof that L455's
conclusion extends. The following comparisons identify exactly what a
later specialization must justify.

- L269's parameterwise contour identity, read separately from its
  proportional-index asymptotic, is the normalization input. Use only
  fixed-parameter strip domination for the initial shift and Fubini;
  uniform errors as the strip edge is approached need the sector proof.
- L455 Section 2 explicitly dominates the exact finite weights by the
  3r/4-exponent weights for alpha≥3/4. Its complete corner/edge/area
  mass bound (8) and discrete clipping tail (9) are the available
  budgets. Preserve the product cutoff and its equality case.
- Section 3's low-strip proof uses alpha≥3/4 and m/r≤1, summing
  Gaussian weights before bounding P,P',P''. In (12) the written
  beta interval belongs to L455's old band. A changed-band proof must
  recheck that high-strip majorant and its edge/area integrability
  explicitly; it cannot cite the old beta sentence unchanged.
- Sections 4–5 expose the exact exponent nu=(1+alpha)/2 before
  weakening it to 7/8, retain h in [39/8,5], and use m/r≤1 for
  derivatives on every potentially clipped full square. Their full
  infinite translated-index tail, at most four complement rectangles,
  signed primitives and local per-weight errors are the covered method.
  No divergent uncut power sum or fixed-index limit may replace them.
- C294b's full mixed-sector proof was read. Its hypotheses already
  include the proposed h values and m=2n. It retains the polynomial
  through its diagonal, both finite-boundary primitives and vanishing
  infinite edges. Its stated conclusion is a reusable mixed-sector
  input, not a same-sign estimate or an arithmetic sign theorem.

The concrete test is to retain the r/20 strips and the full original
signed sum, then compare all four existing L455 normalized budgets:
the summed full-patch error, complete clipping tail, summed translated
complement and mixed sectors, plus the high-strip double exponential.
L455 (22)–(24) displays candidate budgets and the previously proved
rates; b=1/200 and K=2 are a prospective test inherited from that proof,
not a lower-band theorem established by this assessment. Any valid
fixed K and b>0 meets the saved target.

Retain the exact existing normalization template

    C₀=(8π²)², τ=arctan(a/h)/2,
    Φ_*=m log r+9r−h−2aτ,
    P_{r,m}=[2^(m−1)/m!] C₀ exp(Φ_*) π/a > 0.

The required conclusion of a later proof is
D_{m/2}(Ξ;a)=P_{r,m}(S_{r,m}(a)+ε_{r,m}) with the stated
uniform error. These are the existing L455 formula and proposed target,
not a changed-band derivation. Check the Jacobian 1/2, single
same-sign reflection, factorial multiplier, reality and one common
onset for every admissible real r and even m, including cutoff equality.

## Duplicates, failures and continuation test

The scoped comparison distinguishes L455's narrower uniform conclusion,
L324/L325's fixed alpha=3/4 proofs (reuse their inspected method
comparison), and L457's arithmetic-only margin. None states the target
lower-band theta theorem. No claim of originality follows from this
duplicate check or the bounded searches.

Read L323/L327's exact hypotheses and conclusions and both recorded
failures: [the r/4 boundary test](../../ATTEMPTS/2026-09-24-below-five-boundary-strip-test.md)
and [balanced-AFE test](../../ATTEMPTS/2026-09-24-below-five-balanced-afe-test.md).
The first places a growing stationary family in a summed-modulus error
region at alpha=3/4; the second preserves an unsigned form and obstructs
a PSD replacement at its stated precision. This target uses the smaller
strip and retains the signed sum. Neither old stop is extrapolated or
erased; neither establishes the new reduction or its failure.

Continue only if the one mathematical attempt accounts for every
complete sector budget with fixed constants and a common onset, and
recovers exactly P_{r,m}. If a summed mass, tail, derivative or boundary
term cannot be paid for at any fixed positive exponential rate, record
that specific failure and stop this implementation. Do not discard the
term or infer a negative coefficient. A successful reduction still needs
a separate audit and separately scoped arithmetic/sign assembly.

Essential continuation inputs are L455's explicit proof and audited
methods, L269, C294b, L324 and L325. L457 identifies the exact signed sum
and supplies only the prospective downstream margin. Its application
retains September 30, 2026 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, strict Re(s)>7/8,
the allowed pole and unaudited external manuscript/import closure.
The proposed theta reduction itself has no such external premise.
Global mixed positivity, every-height transfer, low indices, bounded
heights and selected-law/regulator gaps remain unresolved. Full matching
Mathlib coverage is not checked; absence is not asserted.

New queries were `"Riemann Xi" "Laguerre" "uniform" "stationary phase"`
and `"Riemann" "Laguerre" "theta" "logarithmic" saddle`.
Search snippets and unrelated orthogonal-polynomial/claimed-resolution
hits were not used as theorem evidence. No new matching primary theorem
was inspected. The primary and local method coverage above is sufficient
for this bounded specialization attempt; no novelty certification or
general stationary-phase error theorem is inferred from the search.
