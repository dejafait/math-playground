# Full-marginal equal-neighbor allocation: one first-lobe discriminator

TARGET: Determine the sign of the equal-neighbor first-negative-lobe budget J at x=16,y=0 for L898's full difference marginal, certifying the complete theta and spatial errors and the half-share resource accounting.
CHECKED: 2026-11-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step133's exact/standard/stronger-result queries and scoped duplicate comparison in 2026-11-08-full-difference-marginal-signed-discovery.md. No matching inspected theorem determines J; no originality or comprehensive absence claim.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/pdf/1802.07942v1 (Johansson Section2 steps2–4, pp2–3, Section2.1 pp3–4) and https://arxiv.org/pdf/1309.0055v2 (Csordas Theorems3.5–3.7 pp6–8, Theorems4.5–4.6 pp11–12), reopened in step134; reused Tuck2006 pp133–136, (3)–(4) and origin/contour qualifications; Csordas1309.0055v2 Definition1.2, Theorems3.3–3.7, Lemma3.6/proof, Remarks3.8/3.11, Proposition3.10/proof and Theorems4.4–4.5 (full Theorem4.6 scope reused); Johansson1802.07942v1 Section2 steps2–4 and Section2.1; all inspected in step133. L898 supplies the full law/domination, L312 supplies explicit theta/derivative envelopes under L037 contracts. Exact primary URLs and proof-case qualifications are retained in that assessment.
COMPARISON: Classical shape-based pairing and associated-kernel positive definiteness do not sign this three-lobe resource budget. L312's conditional-order counterexample, L603's separate-family tail and L609/L814's different allocations do not decide J. L313 already gives a positive total first sign at 16, so J tests a local sufficient allocation rather than reproving that total sign.
GAP: J, its finite-domain application and a complete certificate are uncomputed. Other lobes, nonzero heights, a signed complete residual, growing-frequency control and higher mixed forms remain unresolved.
REASON: A specific half-share allocation provides a bounded actual-theta discriminator distinct from conditional ordering, primitive-family signing and the stopped Stein/event allocations. Attempt only this one test after separate approval; no source result or missing sign is assumed.
SCOPE: Exactly x=16,y=0 and the three intervals defined below, using all theta indices and all of the other spatial direction, with certified truncation errors if truncated computationally. No parameter/frequency sweep, global compensation theorem, curvature replay, or new general quadrature method.
COVERED_TARGET: Determine the sign of the equal-neighbor first-negative-lobe budget J at x=16,y=0 for L898's full difference marginal, certifying the complete theta and spatial errors and the half-share resource accounting.

Step134 repairs the missing direct source URLs and approves this unchanged
calculation scope after primary-source checking. No mathematical identity,
sign calculation or theorem application has been carried out in this review.
LITERATURE_REASON: Supervisor-required repair of missing direct source URLs;
reuse the prior discovery and failure comparisons without a new search campaign.

## Proposed quantity and exact hypotheses

Use L898's Phi(u)=K(|u|)/2, p=u+v, q=u-v, W_0=p^2 Phi(u)Phi(v),
and A_0(0)>0. Define the probability measure mu on the real line by

    mu(B) = integral_R² 1_{u-v in B} W_0(u,v) du dv / A_0(0)

for Borel B. This definition keeps the complete two-variable theta law;
it does not condition on p or separate theta-index families. Let a=pi/16,
and define the closed lobe intervals

    I_0=[-a/2,a/2], I_1=[a/2,3a/2], I_2=[3a/2,5a/2].

The single test quantity is, by definition,

    J = (1/2) integral_{I_0} cos(16q) dmu(q)
        + integral_{I_1} cos(16q) dmu(q)
        + (1/2) integral_{I_2} cos(16q) dmu(q).

The hypothesis to test is J>=0. The first and third integrals have
positive cosine interiors and the middle has a negative cosine interior;
the endpoint weights vanish. The half shares are fixed in advance.
No density formula, shifted second-difference identity, resource theorem
or claimed sign is imported from a source by this definition.

## Mathematical work required by the proposed continuation

First justify the normalization, any change of variables and the exact
allocation interpretation. A full-line positive lobe is proposed to give
half to each neighboring negative lobe. Include the symmetric negative-q
part of I_0; in half-line notation retain the initial half-lobe. Prove
that no resource would be counted twice under this convention. Do not
replace this allocation by the mere fact that the total Fourier transform
is positive, or assume every local budget is nonnegative.

Then obtain a rigorous interval enclosure for this one J. Direct real
box inclusion, as covered by Johansson's algorithm step2, is sufficient
in principle. L036/L037 and the full L312 quadrature construction are
available supporting methods if more efficient. No new analytic Gaussian
integration premise is covered. Explicitly state every implementation
trust assumption rather than treating Decimal or a preview as a proof.

If theta sums or the orthogonal spatial integral are cut off, enclose
the complete omitted mass in each term, with its half weight and the
actual positive normalizer. L898 supplies integrability, not an automatic
numerical tail bound. L312's envelopes can support a separately justified
bound on the new domain; its old singleton certificate cannot supply it.
A p,q parameterization must retain its Jacobian and the reflected-kernel
seams. Handle irrational endpoints by a fixed rational parameter interval
and an enclosing pi, or fully charge endpoint uncertainty. Any finite-head
reflection seams require piecewise smooth treatment or real inclusion.
Save all actual/required bounds, arithmetic contracts, failures and full
certificate values on disk; print only a bounded summary and paths.

## Test, relevance and stopping boundary

A certified upper endpoint U<0 rejects the universal J_cell>=0 version
of this fixed half-share allocation. It is compatible with L313's known
positive total sign. A lower endpoint L>0 passes only this first budget;
L=0 with an otherwise valid enclosure proves weak nonnegativity only.
An enclosure straddling zero is inconclusive. Stop after this bounded
test; refinement to finish a declared error budget is allowed, but no
frequency/height sweep or neighboring-cell campaign is preapproved.

A surviving allocation could eventually supply local signed compensation,
possibly yielding finite section margins to price with L903. This remains
a conditional downstream purpose. The rest of the cosine lobes, their
absolute summation/resource reconstruction, nonzero heights and a complete
signed remainder remain unpaid. No positive residual, finite signed
margin for C_y, all-degree transfer or RH candidate follows from J alone.
A failed allocation does not refute the full-marginal strategy or RH.

Essential mathematical inputs are L898 and its L019/L020 interfaces;
L312's explicit envelope/quadrature method with L036/L037 only if used
computationally. L313, L603, L901, C900a and L903 are scope comparisons,
not premises for J's sign. L902/L309's curvature contracts are unnecessary
for this signed integral. No cross-notebook input or uninspected theorem
is required. Full/supporting Mathlib coverage is unchecked, not absent.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed positivity.
This finite classical allocation discriminator is a calculation, not a
creative proof mechanism or a general Fourier-positivity claim. Its
selection does not revive stopped automatic shape/conditional-order,
separate-family or endpoint-deletion implications. A genuine central
creative escalation would require new independently justified signed
compensation, beyond this one local budget.


## Step134 — direct-source recovery review

Reopened Fredrik Johansson, *Numerical integration in arbitrary-precision
ball arithmetic*, version 1, 22 February 2018:
[primary PDF](https://arxiv.org/pdf/1802.07942v1) and
[primary HTML, Section 2](https://arxiv.org/html/1802.07942v1#S2).
Read Section 2 steps 2–4 (p2) and Section 2.1 (pp3–4), including the
work-limit exit. The direct box branch needs an enclosure valid throughout
the segment; the analytic Gaussian branch additionally needs analyticity
and a bound on an enclosing ellipse. Tolerance requests can fail: the
returned radius is decisive. This supports finite-box integration only;
new-domain theta/spatial tails and normalization remain calculation
obligations. No analytic Gaussian method or infinite-domain error estimate
is imported by this review.

Reopened George Csordas, *Fourier transforms of positive definite kernels
and the Riemann xi-function*, version 2, 21 February 2014:
[primary PDF](https://arxiv.org/pdf/1309.0055v2).
Rechecked Theorems 3.5–3.7 with the two sign cases in Theorem 3.5's proof,
and Theorems 4.5–4.6. Admissibility plus strict logarithmic concavity gives
admissible associated kernels; positive definiteness is an additional
requirement in the all-degree criterion. These statements do not supply
the three-lobe budget sign. No normalization-sensitive identity from
Theorem 4.6 is imported here.

The reused Tuck reference has the direct
[primary DOI](https://doi.org/10.1017/S0004972700047511),
*On positivity of Fourier transforms*, 74 (2006), pp133–138.
This turn's browser access failed at the DOI; the prior inspected
pp133–136 and their damaged-display qualification remain recorded in
step133's discovery assessment. No new reading or formula verification of
Tuck is claimed. It is contextual coverage, not an essential computational
input; the accessible Johansson source supplies the proposed finite-box
method. No persistent essential-source blocker is present.

Decision remains EXPLORE for exactly the saved target. Duplicate and
failure checks are reused from step133; no changed mathematical scope,
novelty finding, sign bound or theorem application is claimed. This is a
process repair, honestly STALLED mathematically. The next turn defaults to
the bounded calculation, with the existing pass/fail/inconclusive test and
all unresolved assumptions above. Supporting/full Mathlib coverage remains
unchecked. No lemma or mathematical script was changed.
