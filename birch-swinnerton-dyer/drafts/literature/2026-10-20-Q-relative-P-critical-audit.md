# Fixed Q-relative local congruence — critical-audit source approval

TARGET: Critically audit L096's exact Q-relative residue and full local seven-divisibility congruence on the conductor-389 curve.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged depth-one assessment's exact-curve searches and Wuthrich/Sage overlap comparison; inspected complete L096, L083 local proof and step-319 audit, histories 372–373, the step-373 working record and ATTEMPTS/045. No fresh external search or arithmetic replay was performed.
SOURCE_EVIDENCE: Reuse Silverman (2009), III Algorithm 2.3 pp.53–54, VII Propositions 2.1–2.2 pp.188–191, IV Lemma 6.3(b)/Theorem 6.4 pp.131–132, with author errata 2022-10-13, as recorded with inspected proof cases in the ready 2026-10-18 known-point assessment and 2026-10-20 relative-congruence assessment; compare the completed L083 local audit.
COMPARISON: L096's new arithmetic and assembly stay within the inspected exact group-law, minimal good-reduction and strict-radius formal-logarithm hypotheses. L081/L083 already cover the P input and full quotient; neither their audits nor L096's construction replay replaces a later audit of L096.
GAP: No essential source gap remains for this fixed audit. Complete certificate inspection, fresh replay, an independent valuation check and both-direction full-group applicability review remain mathematical work for the next turn.
REASON: Separate comparison closes the newly proposed audit-scope coverage gap; approve one bounded audit of the unchanged instance, without redoing source discovery or reopening the parked order route.

SCOPE: Only L096 on model [0,1,1,-2,0], P=(0,0), Q=(1,0), prime seven and depth one; exact saved arithmetic and its full local quotient interpretation. No global saturation, higher depth, changed input or order iteration.
LITERATURE_REASON: The newly proposed critical-audit target was REVIEW_REQUIRED; this separate scope comparison reuses ready primary coverage rather than seeking additional literature for the already approved calculation.

## Relevance, primary coverage and audit boundary

The main gap is rank E(Q)=m(E) for arbitrary analytic order at least two.
The intermediate target is the exact TARGET above. A successful later
audit would make the explicit local relation a checked input for future
rational Kummer-kernel work. Global nonzero-class membership and an
actual rational point of zero logarithm remain independent obligations;
no general BSD progress beyond this fixed local input is claimed.

Reuse the primary-hypothesis and proof-case record in
`drafts/literature/2026-10-18-known-point-local-seven-test.md` and the
changed-point comparison in
`drafts/literature/2026-10-20-Q-relative-P-local-seven-congruence.md`.
Silverman, *The Arithmetic of Elliptic Curves*, second edition (2009),
[III Algorithm 2.3, pp.53–54](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=71),
covers every identity, inverse, chord and tangent case on the general
Weierstrass model. The audit must retain a_2=a_3=1, scalar labels,
nonzero denominators, and the short-model translation in both directions.
On-curve outputs alone do not verify multiplication labels.

[Same source, VII Propositions 2.1–2.2, pp.188–191](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=204),
requires a complete discretely valued field, perfect residue field and
minimal integral equation. The ready record includes Hensel-surjectivity,
reduction proof cases and the parameter proof. Q_7 and the L030/L033
model/reduction inputs are unchanged. Good reduction is essential when
passing from E_0 to the entire group. The audit must check primitive
projective reduction before using t=-x/y on E_1, and must not evaluate
this parameter at the original affine points with y=0.

[IV Lemma 6.3(b) and Theorem 6.4, pp.131–132](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150),
requires characteristic zero and integer radius r>v(p)/(p-1).
The unchanged radii one and two over Q_7 are the assessed strict radii;
no ramification or boundary-convergence extension is proposed. Retain
the [author errata dated 13 October 2022](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf),
especially the integrality qualification of IV.6.3(a). The ready record
covers both directions of the logarithm isomorphism and its strict
valuation estimate. Import these named theorems; no general reproof
is needed. The remaining work is finite evidence and applicability.

The local portion of L083, including its step-319 audit, already checks
both quotient containments, exclusion of division points outside E_1
and generation by P. L096 uses only that local portion: L034's rank
computation and L082's Sha computation are not essential to this audit.
The source review has inspected the proof passage that separates them;
it has not independently certified any new scalar or valuation value.

The duplicate comparison in the depth-one assessment remains adequate.
L096 is the new assembly, while L081 and L083 are upstream results.
The step-373 working record explicitly leaves this later audit pending.
ATTEMPTS/045 and step 371 stop the distinct order implementation; their
source-adaptation failure gives no reason to repeat that route here.
No fresh external theorem lead or changed hypothesis requires browsing.
The Wuthrich/Sage passages were checked for overlap in step 372 and are
not substitutes for exact evidence or inputs to this audit.

No full matching Mathlib theorem or supporting coverage was checked;
no absence is inferred. Approval of source scope is not approval of
L096's correctness. No certificate replay, new deduction, lemma edit
or mathematical script is part of this literature-only step.

## Proposed scope, essential inputs and stopping test

Keep the exact model [0,1,1,-2,0], P=(0,0), Q=(1,0), prime seven
and depth one. Reuse L030/L033 for the model and order-13 reduction,
L081 for the audited P input and [7]E_1=E_2, and the local part of
L083 for full quotient comparison and P generation. L034's point
provenance does not supply a newly assumed seven-saturation assertion.

The proposed audit should inspect L096 and the complete saved
`scripts/Q-relative-seven-373/certificate.json` and
`verification.json` evidence, replaying in a fresh audit destination
without overwriting the original artifacts. Test every scalar label,
group-law branch/denominator and exact parameter valuation, including
all seven candidates and primitive projective reductions. A distinct
check of the load-bearing local valuation evidence is preferable to
merely rerunning a PASS label. Verify both directions of the congruence
using the full local quotient and invertibility of 13 modulo seven.

Continue only if the entire unchanged instance survives; preserve any
actual failure. Do not extend depth, change points/prime, construct
global saturation evidence or resume the parked order chain. Nonzero
global quotient membership, an actual zero-log rational point, uniform
input production and arbitrary-curve BSD remain separate unresolved
assumptions/targets. This document approves no new mathematics.
