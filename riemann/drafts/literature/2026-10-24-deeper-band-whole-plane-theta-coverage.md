# Coverage: matching deeper-band whole-plane theta reduction

TARGET: Establish a whole-plane theta reduction matching L459 on 13/16≤m/r≤7/8, with the exact positive normalization and a uniform additive error O((1+r)^2 exp(-r/200)).
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed L455/L458 theta searches and assessments; compared their full written proofs/audits, L269's parameterwise contour passage, C294b's full proof, L459's exact interface and the L323/L327 failure records. Two changed-scope queries and a new primary preprint lead are recorded below. No inspected theorem states this exact deeper-band reduction; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Csordas, arXiv:1309.0055v2 (21 February 2014), Definition 1.2, Theorem 3.5, Lemma 3.6, Theorem 3.7 and proofs, (3.7)–(3.14); NIST DLMF 2.3(iv), (a)–(d), (2.3.21)–(2.3.23), and 7.2(iii), (7.2.6)–(7.2.9). Reopened relevant primary passages on 2026-10-24; screened bramble_trace, rStation paper 41, v3, 23 October 2026, Theorems 1/1a/3/4 and Section 4.1. Direct links and applicability limits below.
COMPARISON: Existing sources cover the coefficient identity and explicit oscillatory methods, while L455/L458 state narrower bands. Their proof bounds expose containing domains that include the proposed parameters; C294b already covers the mixed sectors. The new preprint's pointwise range is higher and its lower-order results allow exceptional heights. A written uniform-domain specialization remains necessary.
GAP: Establish the changed-band high-strip majorant and every complete mass, clipping, translated-tail, local-patch and sector budget with the exact positive normalization and one common onset. No new bound, correctness verdict or Laguerre sign is established here.
REASON: Essential source/mechanism comparison is complete; the exact target admits one bounded explicit specialization attempt without an unread general error theorem. The changed-domain conclusion cannot be imported by citing L458's narrower theorem.
SCOPE: Positive real r tending to infinity and positive even m on 13/16≤m/r≤7/8, with the exact full S, coupled a(r,m), factorial and reflection normalization; theta reduction only, without an external zero-free premise, arithmetic assembly or every-height transfer.
LITERATURE_REASON: The saved target changes L458's closed theta band; the ready arithmetic assessment does not cover its sector estimates. Reuse existing primary coverage and compare the changed parameter uses rather than repeat arithmetic or zero-free research.

## Completed comparison and relevance

The original nomination required a separate source comparison, not a
derivation. This literature-only step preserves its exact TARGET and
changes coverage to SPECIALIZE. This newly ready continuation receives
separate supervisor approval next turn; no research is invoked here.

The main gap remains initial low-index signs and global mixed positivity.
The intermediate target is the matching additive theta reduction. Its
plausible downstream use is a separate comparison with L459's audited
conditional subexponential arithmetic margin. Assembly, every-height
transfer, smaller indices and bounded heights remain independent gaps.

Reuse [the L458 comparison](2026-10-23-lower-band-whole-plane-theta-coverage.md),
[its audit coverage](2026-10-24-lower-band-theta-critical-audit-coverage.md)
and [the L455 comparison](2026-10-23-subendpoint-theta-sector-reduction-coverage.md).
Their source mechanisms remain applicable for assessment; their narrower
theorem conclusions and correctness verdicts do not transfer automatically.

## Primary sources and their limits

Csordas, [*Fourier transforms of positive definite kernels and the Riemann
ξ-Function*, v2](https://arxiv.org/html/1309.0055v2), Definition 1.2,
requires a smooth, positive, even kernel, decreasing on the positive
axis, with every derivative O(exp(-|t|^(2+ε))) for some ε>0.
Theorem 3.5 additionally assumes strict logarithmic concavity there;
its proof treats s<t and s>t separately. Lemma 3.6 and Theorem 3.7,
(3.10)–(3.14), give the coefficient identity with Jacobian and factorial.
All-level positive definiteness remains a premise of the real-zero
criterion. Reuse the earlier actual-kernel applicability comparison
and the normalized local identity; these sources give no uniform sector
error or automatic sign.

[DLMF 2.3(iv)](https://dlmf.nist.gov/2.3#iv), (a)–(d),
(2.3.21)–(2.3.23), assumes smooth real phase/amplitude, positive phase
derivative off the stationary endpoint, differentiable endpoint
expansions, and finite endpoint limits or the specified uniform
convergence at infinity. Both finite endpoints contribute.
[DLMF 7.2(iii)](https://dlmf.nist.gov/7.2#iii), (7.2.6)–(7.2.9),
supplies scalar Fresnel integrals and limits. Neither source supplies
uniform constants for moving clipped domains and growing theta sums.
The explicit local real-phase and rectangular-variation proofs must
provide those. Olver/Lyness and the earlier SIGMA lead remain unread
and unimported; no essential step needs them. Access date: 2026-10-24.

A new search lead was inspected at its primary manuscript:
bramble_trace, [*Generalized Laguerre positivity at growing orders*,
rStation paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
displayed v3, 23 October 2026, 23:22 UTC. Theorems 1/1a require
2p/log(t/(2π))>1/2 by a fixed margin. Section 4.1 uses an
absolute-convergence arc and lower bound, plus a complementary contour
gap. Here 2p=m and log(a/(2π))~2r, so the target ratio tends
through [13/32,7/16], outside that pointwise scope. Theorems 3/4
include these lower ratios but give mean or typical-height conclusions
with exceptional heights. None states the required full-S additive
theta reduction. No theorem from this preprint is imported; the rest
of its proof is not audited. The search preview named v2; this comparison
uses the v3 primary text actually opened.

## Exact domain comparison and remaining proof obligations

Read L458 Sections 1–4 and its entire separate audit; L455 Sections
1–6 and audit; L269's initial contour passage; C294b's complete proof;
and L459's exact hypotheses, sum and arithmetic conclusion. The target
parameters correspond to

    α=m/r∈[13/16,7/8], β=1−α∈[1/8,3/16],
    h=9/2+α/2∈[157/32,79/16]⊂[39/8,5],
    ν=(1+α)/2∈[29/32,15/16].

These are comparisons of hypotheses, not new sector estimates. The
following identify the bounded difference to be proved next:

- L269's initial shift/Fubini identity uses a smaller closed strip at
  each fixed parameter. Its proportional-index asymptotic is not an
  input here, and uniformity as τ→π/4 must come from the sectors.
- L458 (7)–(10) and L455 (8)–(11) expose the mass, discrete clipping
  tail and low-strip estimates using α≥3/4. Retain the corner, both
  edges, Gaussian sums before polynomial estimates, derivatives through
  order two at zero, and the comparison starting at K−1.
- L458 (11)'s written beta interval differs. Its displayed containing
  envelope uses β≤1/4 and β/2≥1/128. The new interval must be
  checked explicitly against those conditions and through every high-strip
  edge/area limit; its old-band conclusion alone is insufficient.
- L458 (13) retains ν before weakening it to 7/8. The target ν
  lies in that containing range. Recheck the full infinite translated
  sum with its Gaussian index tail, all at most four complement rectangles
  and actual moving boundaries; an uncut power sum is not available.
- L458 (15)–(16) use m≤r and bounded h for full/clipped-square
  derivatives and the real phase map. Preserve the per-weight error
  before multiplying the complete mass, the entire discrete clipping
  tail, and every cutoff equality. A fixed-index limit is insufficient.
- C294b's stated domain already contains the new h interval, with
  H=m/(2r) and p=m=2n. Its full proof covers both mixed sectors,
  their Jacobians, finite primitives and infinite edges; no extension of
  that theorem is proposed.

The exact existing normalization template to recover is

    c=m/(2r), a=sqrt(4π²exp(4r)−h²)>0,
    τ=arctan(a/h)/2, C₀=(8π²)²,
    Φ_*=m log r+9r−h−2aτ,
    P_{r,m}=[2^(m−1)/m!]C₀exp(Φ_*)π/a>0.

The proposed statement is D_{m/2}(Ξ;a)=P_{r,m}(S+ε), with
exactly L459's full finite S and zero weight at log(jk)=2r.
Keep the area Jacobian 1/2, opposite Fresnel factors, one same-sign
reflection, whole-line transform 2Ξ, reality and m! exactly once.
This is the target template, not a changed-band identity proved here.

## Duplicates, failures and discriminating test

The scoped search and theorem comparison found no stated duplicate
on this exact closed band. L455/L458 are narrower reductions; L459
is arithmetic-only. Reuse the prior L324/L325 mechanism assessment;
their fixed α=3/4 conclusions are not silently generalized.

Read L323's hypotheses/conclusion and
[the r/4-strip failure](../../ATTEMPTS/2026-09-24-below-five-boundary-strip-test.md).
It puts a growing stationary family inside the discarded strip at
α=3/4. Retain the r/20 mechanism instead. Read L327's statement and
[the balanced-AFE failure](../../ATTEMPTS/2026-09-24-below-five-balanced-afe-test.md).
That transform retains an unsigned form and obstructs its PSD replacement
at its stated precision. This target keeps the signed S. Both historical
stops retain their scopes; neither decides this target or bans the route.

Continue the one bounded attempt only if every complete normalized
budget in the L458 (18) template, including the high-strip term, can
be bounded by C(1+r)^2 exp(-r/200), with fixed C and one real-r
onset throughout the closed band, and exactly P is recovered. Stop this
implementation if a mass, clipping, derivative, boundary or reflected-sector
term cannot meet that error; preserve the specific failure without
discarding it or inferring a negative sign. Success still requires a
separate critical audit and separately scoped assembly.

Essential continuation inputs are L458/L455's explicit methods, L269
and C294b; L324/L325 are traced through those existing proofs if needed.
L459 is downstream only. Any later use of its margin retains September
30 Theorem 1.1 at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
strict Re(s)>7/8, the allowed pole and unaudited external manuscript/
import closure. The theta reduction itself requires none of that premise.
Initial indices, bounded heights, mixed positivity and selected-law/
regulator realization remain unresolved. Full matching and supporting
Mathlib coverage remain unchecked; absence is not asserted.

New queries: `"Riemann xi" "generalized Laguerre" "stationary phase"`
and `"Riemann xi" "theta" "13/16"`. Search snippets, orthogonal-
polynomial hits and unrelated claimed resolutions are not theorem evidence.
The new primary lead was compared above; no failed search establishes
novelty. This is completed source exploration, not a new mathematical
input or progress beyond the inspected source methods. No lemmas,
mathematical scripts, DAG or PROOF.md were changed.
