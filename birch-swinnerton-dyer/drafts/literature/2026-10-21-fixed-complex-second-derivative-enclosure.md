# Fixed complex second-derivative certificate — source comparison complete

TARGET: Assess a finite outward enclosure of L''(E,1) excluding zero for E=[0,1,1,-2,0], using L030 and L099 for the model and lower vanishing, without importing L035's published analytic-order computation.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the two 2026-10-08 assessments and history/094; searched derivative/kernel/error terminology, Wuthrich's tail method, rigorous Arb/FLINT integration and logarithm inequalities. Queries and inspected ranges are in drafts/source-notes/2026-10-21-complex-derivative-sources.md.
SOURCE_EVIDENCE: Inspected Cremona, corrected second edition (1997), Section 2.13 pp.42–44, Proposition 2.13.1 and proof; Wuthrich arXiv:1608.06423v2 Lemma 4 proof pp.6–7 and Section 4.1 p.9; DLMF 4.5.4; Johansson arXiv:1802.07942v1 Section 2 pp.2–4 and FLINT acb_calc finite-integration contract and qualifications.
COMPARISON: L035 already supplies the published fixed order and passed step-094 audit. Known derivative and rigorous integration methods cover the ingredients for independent evidence; the difference is an explicit weighted-tail and finite-error specialization, not a new fixed-order result or general algorithm.
GAP: No derivative enclosure exists. Full Fourier and kernel improper tails must first be bounded together; finite coefficient/parameter/integration/signed-summation errors and backend availability remain implementation obligations.
REASON: Select a bounded proof specialization of inspected sources before numerical replay; do not approve replay before the complete error budget is established. No new estimate is derived or approved as true in this literature turn.
LITERATURE_REASON: The published analytic computation remains unreplayed; inspecting the exact second-derivative kernel and rigorous error control is essential to the newly proposed finite-certificate target and was excluded from the earlier ready scope.
SCOPE: Source comparison for the exact TARGET and preparation of a separately approved error-budget proof; no derivative computation, installation, lemma/program write or nonvanishing claim.

## Scope, relevance and decision test

The main gap remains rank equals complex analytic order for arbitrary
elliptic curves over Q of analytic order at least two. The proposed
intermediate target is a finite, outward complex second-derivative
interval for the same known conductor-389 example. Its possible use
is a complex upper-bound certificate complementary to the finite
rational lower-bound provenance checked in L099/L100. This is a
validation case for certificate production, not a new BSD case or a
uniform route. L035 already makes an adequate published mathematical
assertion; an independent replay must be justified by its explicit
finite evidence, not by any suggestion that that citation is invalid.

The review retrieved the exact derivative hypotheses and Mellin proof
before evaluation methods. The [source record](../source-notes/2026-10-21-complex-derivative-sources.md)
compares rigorous finite integration with the remaining weighted improper
tails. Neither tolerance parameters nor L031's twist tail cover those
tails. No reproof of the Mellin formula or low-order theorem is proposed.
No numerical implementation is approved yet.

Essential intended inputs: L030's exact minimal model/conductor and
newform, audited L099's rational independence, and the analytic-zero/one
theorem in foundations/02 for the proposed lower-vanishing argument.
L100 is downstream context, not a source of complex upper vanishing
order. L031 supplies only its independently certified a_389=1/sign;
its twist value and tail do not cover derivatives. L035 supplies overlap
only. The exact formula is now covered by primary inspection; fixed
applicability and complete remainder specialization remain research
obligations, not deductions made in this turn.

First seek a proof at proposed M=Y=128 that total omitted analytic error
is <=2^-30, with an explicit finite-arithmetic contract. These are sought
bounds, not established estimates. The new error-budget assessment
requires separate approval next turn. Replay remains parked until that
test succeeds; failure parks the schedule without enlargement. Any later
replay must exclude zero after every error. Do not repeat L035's audit.
ATTEMPTS/043/045 remain intact. This review spends no mathematical
exploration turn. Mathlib matching and supporting coverage are not checked.
