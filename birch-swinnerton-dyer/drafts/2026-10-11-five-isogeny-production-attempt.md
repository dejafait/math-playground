# Degree-five instance production — working record

Approved target: the exact TARGET in the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-11-conductor-eleven-five-isogeny-production.md`.
Main gap: rank equality for arbitrary analytic order at least two.
Intermediate target: verify the candidate (5,5), a complete normalized
Vélu quotient, minimal models and differential, then apply audited L045
to every audited L043 value. Downstream use: fixed nonoptimal-model
normalization/denominators for L027; no coefficient or rank conclusion.

Inputs read: L039 arithmetic/full-relative identification; L043 full
normalization and twelve generator values; complete L045 and its audit;
ATTEMPTS/023--024 and the existing exact-instance source comparison.
Those stops prohibit repeated conditional audits as production, not this
independently checkable instance. The Sage overlap makes this reproduction.
No new external search is needed: essential construction coverage is ready.

Continuation test: exact order five, quotient identity including projective
exceptional points, nonzero discriminant, integral minimality and final
minimal-differential pullback must all pass before transfer. Failure parks
this instance. Preserve all prior notebook work. Mathlib remains unchecked.

Unfinished calculation plan: use X=x-1/3, Y=y+1/2 to obtain
Y^2=X^3-(31/3)X-2501/108. Compute the finite cyclic subgroup by
rational addition. Build the quotient from paired versions of Vélu (7),
check the equation and differential as full polynomial identities, and
retain every coordinate transformation and every reduced generator value.
At that initial checkpoint no instance result was claimed.

Completed: exact order five and all four nonidentity multiples pass. The
quotient is [0,-1,1,-7820,-263580], with discriminant -11 and no further
minimalizing transformation. Complete paired-equation-(7), target and
differential identities, finite exceptional poles and infinity pass
distinct full replay. All witnesses and arithmetic are canonical in
[L046](../lemmas/L046-conductor-eleven-five-isogeny-normalization.md) and
`scripts/conductor-eleven/five-isogeny/`; the fresh verifier reports 56
checks and no failures. Audited L045 gives R=5 and the twelve L043 values
give exact denominator two. This satisfies the instance continuation test.
The new assembly awaits a separate critical audit; its scope approval is
REVIEW_REQUIRED. No mathematical advance beyond the known algorithms or
any BSD-rank conclusion is asserted.
