# Complete pole correction: Mellin specialization nomination

TARGET: Derive or obstruct an exact formula for the complete C999h correction Q(w,t) using Lagarias–Rains Theorem 5.1 at s=w/2+i*t on [1,3/2] x [40,45], retaining the rational pole term and proving local uniformity, so Q can be evaluated independently of G_w and curvature without asserting a residual sign.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step436's completed event-conditioned comparison in drafts/literature/2026-11-11-event-conditioned-jump-split-review-435.md and review421's Theorem5.1 assessment. Named local searches found no existing complete-Q reduction in C999g/C999h or the relevant theta/nonlocal reviews and failure records. No novelty claim.
SOURCE_EVIDENCE: J. C. Lagarias and E. Rains, On a Two-Variable Zeta Function for Number Fields, arXiv:math/0104176v5, 7 July2002, Theorem5.1/(5.1), proof pp24–27, including the Re(s)>0 logarithmic-theta Mellin integral and the Re(s)>2 series evaluation, https://arxiv.org/pdf/math/0104176v5 . C999h's fully audited definition(1) supplies the exact correction to be matched. See review435 step436 for the inspected statement and proof cases.
COMPARISON: The known Mellin transform and zeta-product evaluation cover the required source function. Only their matching to the completed correction, including both half-line contributions and the rational pole term, remains to derive. Import the source theorems without reproof; a new sign estimate is outside scope.
GAP: No exact complete-Q reduction has been established locally. Even a successful reduction supplies neither a signed far-jump comparison nor eventwise curvature control. It cannot by itself determine G_w*G_tt.
REASON: An independently evaluable complete correction could preserve cancellation that separate absolute pole and theta bounds destroy. This is a narrow reproduction/specialization after the sign nomination failed its readiness test, not a creative proof of positivity. Newly written readiness requires separate next-turn approval.
SCOPE: Exact formula and local uniformity on the stated rectangle and a surrounding neighborhood only. No jump-split theorem, sign proof, new event search, numerical backend, script, rectangle change or RH claim is approved.

Main gap: L030–L032/C032a actual-Xi positivity; L966/L968 forcing,
L984(H) and the capped C997s bridge remain separate. This intermediate
target addresses one explicit unpaid term in C999h, not those gaps.

Essential inputs: C999h, C999g's audited theta normalization and inherited
L018/L019; review421 and the completed review435 step436 source evidence.
Review425 supplies context only. C999f is not a premise. No other
notebook input is used or proposed.

Use the source Mellin integral in its actual right-half-plane domain,
with the source theta convention. The necessary half-line split and
modular substitution must retain their boundary/pole contribution.
The zeta-product theorem may be cited in the smaller right half-plane
by its established continuation; the uncontinued Dirichlet series may
not. Keep the full correction together until equality is checked.
No candidate formula for Q is proved or asserted in this assessment.

Continuation test: obtain exact equality with C999h(1), correct factors
and a compact-neighborhood convergence argument with no unpaid term;
otherwise exhibit the precise domain or uncanceled-term obstruction.
Do not count a formal Mellin analogy, a separately divergent integral
or a signed numerical preview as success. No curvature division is
needed for this target. Do not reprove the entire-family theorem or
the source Mellin/zeta-product result.

Downstream use: an explicit source-function correction can be estimated
independently of the unknown event product and paired with a future
signed far-jump analysis. That analysis needs separate source scope.
Event existence, nondegeneracy, curvature, multiplicities, initialization,
other heights and global transport remain unresolved. Full matching
Mathlib coverage is unchecked and unknown. STATUS remains IN_PROGRESS.
