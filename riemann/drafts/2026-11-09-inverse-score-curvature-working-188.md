# Fixed-parameter inverse-score curvature working note — step188

The gate-approved target is the exact Next action in the pre-existing
`drafts/literature/2026-11-09-inverse-dilation-score-convexity-test.md`
(EXPLORE). Reuse its source and duplicate/failure assessment. Essential
inputs: L019/L058/L915; no contact, L914 arithmetic or other notebook.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Test: at lambda=1/40, test inverse-score curvature at x=1 (u=1),
retaining the full theta series. Put f(u)=log K(u). Direct chain-rule
calculation to be checked gives

    h'(x)=-2lambda-(f'(u)+u*f''(u))/(2u),
    h''(x)=(f'(u)-u*f''(u)-u^2*f'''(u))/(4u^3).

L915 supplies h'>19/10 globally. Hence a proved positive h''(1)
would give negative inverse curvature at h(1), rejecting the proposed
global-convex comparison only. Signed hinges, contact flux,
initialization, tangency, other parameters and RH would stay open.

Plan: isolate the n=1 summand, whose logarithmic derivatives are
explicit in v=pi*exp(2u), and bound the full n>=2 derivative tails
through order three relative to K_1 at u=1. Use rational, deliberately
coarse exponential bounds and exact arithmetic; no finite truncation
or sample sign will be accepted. This is unfinished reasoning, not
a result or a claim of novelty. If the signed margin cannot be paid,
save the remaining bound and stop the bounded attempt.

Resolved during this same bounded step: the complete argument is now
canonical in `lemmas/L916-full-theta-inverse-dilation-score-nonconvexity.md`.
The full-series witness rejects the nominated global-convex comparison;
its independent proof audit remains pending. The first incorrect expected
p3 coefficient list was corrected from the explicit recurrence, and its
failed certificate is preserved. This initial working note is retained
as unfinished-at-creation reasoning, not a second proof or current task.
