# Common-zero count-loss proof attempt

Approved target: Assess whether D≤0 and L(G)>0 imply N_G([H,X])−N_F^mult([H,X])≤N_common([H,X])+C_H for nonzero real-analytic pairs, where N_common counts distinct common zeros.

Prior ready assessment: `drafts/literature/2026-10-08-count-bound-with-common-zeros.md` (EXPLORE), supplied at invocation start and reused unchanged.

Main gap: actual-theta mixed positivity and the total L367 signed margin.
Intermediate target: the displayed generic quantitative count bound.
Downstream use: with L377, an eventual actual D≤0 premise would force
common-zero counts at least as large as the negative count excursions,
up to a constant. Actual D≤0 and an upper bound on actual common-zero
counts remain independent unproved premises; no application is attempted.

Continuation/abandonment test: obtain an X-independent finite C_H with
all multiplicities and closed endpoints, or refute it by an exact pair
with unbounded deficit after subtracting distinct common zeros.

Saved unfinished reasoning: L374's pencil square completion and
finite-order contradiction are local. For a globally independent pair,
they should make W nonzero at every noncommon interior point, regardless
of future shared zeros. Splitting the compact interval at its k common
zeros gives at most k+1 common-free pieces. If piece i contains r_i
noncommon G zeros, the interval-sign argument should give at least
max(r_i−1,0) noncommon F zeros. Then q=sum r_i and full F multiplicity
at the common points contribute at least k, yielding
N_G−N_F^mult≤q−sum max(r_i−1,0)≤k+1.
Still check independent restrictions by analytic identity, finiteness,
local proof use at boundaries, dependent pairs and X=H. Do not invoke
L374's disjoint-ray conclusion on a bounded piece, deflate the functions,
or assume W has the same sign on different pieces.

Existing L373/L371 failures are preserved; L373 disproves the bound
without a growing common-zero loss and does not refute this target.
No new literature search is needed. Full matching Mathlib coverage is
not checked. The saved reasoning above was unfinished at creation.

Completed outcome: ADVANCE / RESEARCH / POTENTIALLY_NEW proof_attempt.
Canonical L378 proves the inequality with universal C_H=1. Its local
Taylor argument uses the right neighborhood of each noncommon point,
not L374's disjoint-ray conclusion. Independence on restrictions follows
from analytic identity. Strict L(G)>0 makes every G zero simple; the
proof leaves common F multiplicities unrestricted and restores their
full contribution. Compact finiteness, pieces with zero or one G zero,
common H/X, X=H and globally dependent pairs are all treated in L378.
The only direct mathematical lemma input is L374. L373 and L377 remain
comparison and downstream context; no actual-family application is
performed. No mathematical script is needed for this exact argument.

Separate critical review is still required for L378. The next audit
assessment is REVIEW_REQUIRED; no uncovered audit or new target is
approved or executed in this attempt. The claimed advance is a local
conditional input, without certified historical novelty, a new actual
theta sign/exclusion range, or a complete RH candidate.
