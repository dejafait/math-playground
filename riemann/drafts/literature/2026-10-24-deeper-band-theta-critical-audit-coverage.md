# Coverage: critical audit of the deeper-band theta reduction

TARGET: Critically audit L460's whole-plane theta reduction on 13/16≤m/r≤7/8, including every sector error, cutoff equality, exact positive normalization and one uniform onset.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed exact-band discovery and theorem comparison in 2026-10-24-deeper-band-whole-plane-theta-coverage.md; read L460 Sections 1–4 and Mathlib, L269's initial contour passage, C294b's complete proof, L455's explicit identity/primitive/translated-amplitude passages and separate audit, L458's entire separate audit, and the L323/L327 ATTEMPTS records. No new external search or novelty claim.
SOURCE_EVIDENCE: Reused inspected Csordas arXiv:1309.0055v2 (21 February 2014), Definition 1.2, Theorem 3.5, Lemma 3.6 and Theorem 3.7, (3.10)–(3.14), statements and proofs; NIST DLMF 2.3(iv), hypotheses (a)–(d), (2.3.21)–(2.3.23), and 7.2(iii), (7.2.6)–(7.2.9), reopened on 2026-10-24 in the construction assessment. No primary passage was newly retrieved this turn.
COMPARISON: Existing exact-band coverage covers the explicit identity and oscillatory methods used in L460; L455/L458's narrower conclusions and audit verdicts do not certify its changed domain. Primary sources provide no matching moving-domain, growing-index uniform error theorem. Their covered cases and the written local estimates suffice for a separate bounded proof audit.
GAP: Independently validate or identify a failure in L460 (1), including every complete error, cutoff/band endpoint, normalization and common onset; this scope review supplies no correctness verdict or sign assembly.
REASON: The newly nominated audit scope is now compared with the ready exact-band assessment and all written proof cases. No essential unread source is needed for the explicit audit; no general uniform stationary-phase theorem is silently imported.
SCOPE: L460 only, positive real r tending to infinity and positive even m with 13/16≤m/r≤7/8, exact a(r,m), full signed S and positive P; no arithmetic sign, external-premise audit or every-height transfer.
LITERATURE_REASON: The saved critical-audit target was REVIEW_REQUIRED; its proof-case coverage needed a separate comparison after construction. Reuse exact-band source coverage without repeating browsing solely for the new audit.

## Source reuse and limits

The [construction assessment](2026-10-24-deeper-band-whole-plane-theta-coverage.md)
records the exact-band searches, primary passages, version information and
comparison with rStation paper 41 v3, Theorems 1/1a/3/4 and Section 4.1.
Its pointwise range is higher; its lower-order conclusions allow exceptional
heights. No theorem from that preprint is imported here. Reuse also the
[L458 audit assessment](2026-10-24-lower-band-theta-critical-audit-coverage.md).
Neither predecessor's correctness verdict is extended to L460.

Csordas, [*Fourier transforms of positive definite kernels and the Riemann
ξ-Function*, v2](https://arxiv.org/html/1309.0055v2), Definition 1.2,
requires smoothness, positivity, evenness, positive-axis decrease and
super-Gaussian decay of every derivative. Theorem 3.5 additionally assumes
strict logarithmic concavity; its proof separates s<t and s>t.
Lemma 3.6 and Theorem 3.7, (3.10)–(3.14), provide the coefficient identity,
with Jacobian and factorial. All-level positive definiteness remains a
premise for real zeros. The audit uses the already normalized local
identity, not a source positivity conclusion.

[DLMF 2.3(iv)](https://dlmf.nist.gov/2.3#iv), hypotheses (a)–(d),
(2.3.21)–(2.3.23), treats smooth real phase/amplitude, positive phase
derivative off the stationary endpoint, differentiable endpoint expansions
and controlled endpoint limits or uniform convergence at infinity. Both
finite endpoints contribute. [DLMF 7.2(iii)](https://dlmf.nist.gov/7.2#iii),
(7.2.6)–(7.2.9), supplies scalar Fresnel definitions and limits.
Neither supplies L460's two-dimensional moving-domain uniformity.
Its explicit primitive, variation and real-phase estimates must supply it.
Olver/Lyness and the older SIGMA lead remain unread and unimported;
no essential audit case depends on them. Full matching and supporting
Mathlib coverage remain unchecked, not absent.

## Bounded audit scope

The main gap is initial low-index signs and global mixed positivity.
The intermediate target is an independent correctness verdict on L460's
complete additive reduction. Its plausible downstream use is a separately
scoped assembly with L459's conditional arithmetic margin. Every-height
transfer, initial indices and bounded heights remain separate gaps.

Read L460's full proof for this scope comparison. The following are
obligations extracted from it, not estimates validated in this turn:

- Section 1, (2)–(6): retain beta∈[1/8,3/16], h∈[157/32,79/16],
  nu∈[29/32,15/16], exact saddle relation and even m. Use only L269's
  parameterwise shift/Fubini identity; its proportional-index asymptotic
  is outside this use. Check theta phases, polynomial derivatives through
  zero, finite-interval primitives and every rectangular edge/corner.
- Section 2, (7)–(12): check the full discrete mass with corner and both
  edges; the first discrete-tail comparison begins at K−1. Check zero
  weight at log(jk)=2r, low-strip derivative endpoints, Gaussian sums
  before polynomial estimates and the changed beta high-strip inequality.
  Include both strips, their intersection, infinite edges and Fatou.
- Section 3, (13)–(16): retain the exact translated index exponent before
  weakening it. Check the entire Gaussian index tail, including indices
  beyond exp(b), and every moving complement rectangle. For full/clipped
  patches inspect the positive polynomial argument, all needed derivatives,
  real phase map, inverse Jacobians and per-weight error before summation.
  Assign equality at b−epsilon to the tail and at b+epsilon to zero area;
  product-cutoff summands without a patch still need the full complement.
- Section 4, (17)–(18): compare C294b's hypotheses with the exact h,H,p
  parameters and inspect all load-bearing mixed-sector proof cases.
  Account for both mixed sectors, one same-sign reflection, Jacobian 1/2,
  opposite Fresnel factors, whole-line transform 2Ξ and m! exactly once.
  Test every complete normalized term against C(1+r)^2 exp(-r/200),
  with one C,R throughout the closed band and all cutoff transitions.

L455/L458's explicit estimates and separate audits locate the cases;
the subsequent audit must independently check their use in L460.
Trace L324/L325 through these proofs if a load-bearing issue requires it.
The ancillary rational checks are not a substitute for the entire proof.

## Duplicates, failures and decision test

L460 already states this reduction; the next step audits it rather than
creating a duplicate. The narrower L455/L458 statements do not import
its conclusion. Read the [r/4-strip failure](../../ATTEMPTS/2026-09-24-below-five-boundary-strip-test.md)
and [balanced-AFE failure](../../ATTEMPTS/2026-09-24-below-five-balanced-afe-test.md).
L323 obstructs a summed-modulus estimate with its stated larger cutoff;
L327 retains an unsigned ratio form and obstructs a PSD replacement at
its precision. L460 uses r/20 and retains signed S. Preserve these stops
without extending their scope or using them as correctness certificates.

Continue to separately assessed assembly only if the independent audit
validates the entire real-r/even-m statement, complete error, exact positive
P and one common onset. If any term fails, record its exact claim and
uncontrolled region before repair or abandonment. Source approval alone
cannot establish a sign or excuse a missing boundary.

Essential inputs: L269's initial identity, C294b and L455/L458's explicit
proofs and separate audits, with L324/L325 traced only as necessary.
L459 is downstream only; no external zero-free premise enters theta.
Its later use retains September 30 Theorem 1.1 at commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a, strict Re(s)>7/8,
allowed pole and unaudited manuscript/import closure. Initial indices,
bounded heights, global mixed positivity and selected-law/regulator
realization remain unresolved. No RH candidate is supplied.

This literature-only step completes scope comparison, not mathematics
beyond the inspected source methods. No lemma, mathematical script,
DAG or PROOF.md is changed. The ready continuation requires separate
next-turn approval before its audit is executed.
