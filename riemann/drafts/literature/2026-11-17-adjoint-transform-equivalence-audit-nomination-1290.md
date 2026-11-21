# Adjoint-transform equivalence — separate audit nomination1290

TARGET: Audit C032f's adjoint-transform equivalence (12)-(20) for g=A*(0,e^{-u}), including strip continuation, all noncompact L2 interchanges and converse Fourier uniqueness, without deciding delta.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse review1266's exact complex Fourier/Laplace uniqueness comparison and review1270's bounded Hankel/actual-range assessment; C032f explicitly separates its unaudited witness calculation from audit1282. This nomination scopes that outstanding correctness check, not another attempt to exclude a preimage by a positive-axis norm or bounded-corona estimate.
SOURCE_EVIDENCE: NIST DLMF1.14(i), Uniqueness, https://dlmf.nist.gov/1.14.i , continuous absolutely integrable input, primary coverage recorded in review1266; Douglas1966 Theorem1/proof pp413-414, reused review1270 for context only. C032e's full-theta holomorphic continuation and all real exponential weights remain explicit local inputs requiring exact use.
COMPARISON: Fourier uniqueness is known; the proposed work audits its application to a noncompact L2 preimage, the half-line-to-strip extension and the converse weighted bilateral transform. It is not a new uniqueness theorem, a Hardy/corona identification, or an audit of the already accepted bounded/core reduction.
GAP: Verify or repair the claim that an actual y in Y satisfies B*y=g exactly when its actual one-sided Laplace transforms satisfy (20) for every real r>0. Analyticity, absolute interchanges and Fourier uniqueness hypotheses must all hold. Membership itself and delta remain undecided.
REASON: This is a concrete outstanding analytic claim independent of the rejected polynomial class. Source coverage supports a conceptual audit; this newly written assessment must receive separate approval before any proof is verified or repaired.
SCOPE: Exactly C032f(12)-(20), complex unweighted H,Y, the unchanged full theta kernels and fixed c,a. Retain C032e and accepted C032f(1)-(5). No new witness, common-zero search, norm-budget replay, spectral representation or sign mechanism is authorized.

## Separate approval and mathematical purpose

This file is a source-scope nomination, not a completed audit. The next
invocation first checks this new coverage separately. No implication in
(12)-(20) was accepted as correct during the literature-only1290 review.

The main gap remains L030-L032/C032a actual-Xi Q positivity in every
degree. The intermediate target is correctness of a single exact-range
interface. Its plausible downstream use is a reliable analytic criterion
for one B* preimage, before further source-metric work. It gives no signed
realization, completed source norm, initialization, singular-case treatment
or all-degree Xi sign. A pass supplies only a validated reduction.

Reuse `2026-11-17-compact-core-branch-compatibility-review-1266.md`, especially
its inspected DLMF uniqueness and complex-input qualifications, and
`2026-11-17-normalized-approximate-branch-compatibility-review-1270.md`.
No new external uniqueness discovery is required. Read C032f's exact
(12)-(20) proof, C032e's strip/all-weight bounds and the L016/L019/L020
ranges actually used. Review1266 does not itself prove the noncompact
application: that difference is precisely the mathematical audit.

Test both directions for arbitrary actual y in L2(0,infinity;C^2).
Check the strip convention, the complete theta series and all factors
in F(z)=2Xi(2iz). Verify locally uniform L2 majorants for kernel and
first derivative before extending noncompact integrals holomorphically.
Check the product-space Fubini estimate identifying the adjoint's
continuous representative. Half-line equality initially holds almost
everywhere; justify every upgrade and the identity-theorem domain.
For the converse, verify the absolute whole-line weighted transform,
holomorphy on Re z>0, continuity and L1 hypotheses of Fourier uniqueness,
and then restriction to the original half-line. Preserve the signs and
shifts in d_sigma and the denominator r+1. Merely solving the pointwise
equation with arbitrary holomorphic functions is insufficient: both
Y_sigma must be transforms of the stated actual L2 inputs.

Acceptance test: all implications and hypotheses pass, or identify the
first invalid step and repair/withdraw the exact equivalence canonically.
A preview, finite transform check or formal convolution is not evidence.
Do not audit or extend (21)-(25) in this task. Preserve stop1273 and the
bounded-corona/fixed-boundary stops; none asserts nonmembership.

This is a delicate analytic proof_audit/conceptual_audit, not creative
mathematics or an RH candidate. Full matching Mathlib coverage is
unchecked. No cross-notebook input. No new proof is derived here.
