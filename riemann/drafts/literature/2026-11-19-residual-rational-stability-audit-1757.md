# Rational-stability application audit1757

TARGET: Audit C033n's positive argument neighborhoods, coefficient budget, two-sided signed supremum error and rational nonzero choices under the unchanged C033l/C032q qualifications.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment1756 and source-notes1756's exact-target searches, local duplicate comparison and stops1571/1576; no fresh literature search is claimed or needed for auditing the same specialization.
SOURCE_EVIDENCE: Mimica, Laplace transform, Dresden course 27April-1May2015, Remark1.2(i), Proposition1.4(i)-(ii), printed pp5-7, https://web.math.pmf.unizg.hr/~amimica/lt.pdf ; C032q's signed bounded integration and C033l's finite real separator; standard mean value theorem and rational density. The exact source statement and applicability are recorded in source-notes1756 and C033n.
COMPARISON: This audit checks only the finite uniform error propagation developed in C033n from the already covered general tools. It must not reprove general Laplace differentiation or re-audit C033l's separation, C033m's evaluator or their source-wide inputs.
GAP: Independently check equations(2)-(11), including the positive lower argument bound, both sides of the full signed supremum, nonzero rational choices and retention of epsilon/2; no numerical separator or wider mathematical conclusion is covered.
REASON: The completed specialization is a useful local interface but has not had its separate application audit; unchanged source coverage is adequate. Separate literature approval1758 is complete; the unchanged audit target is ready for the next research turn.
SCOPE: C033n's exact finite data n,s_j,a_j,epsilon and full mass-one signed Borel class on [1,2] with TV<=2; C033l/C032q's probabilities, signed integration and inherited external qualifications. Atoms at zero, singular widths, zero original coefficients and arbitrarily small positive arguments remain allowed; no moment at zero or numerical margin is assumed.

Audit the claimed bounds D<=epsilon/6, residual error<=D, and
support error<=2D, with explicit treatment of the reversed supremum
inequality. Check tau<=A/2 for an index attaining A, the positivity
of every d_j, and rational density when an original coefficient is
zero. A failure should identify and repair the precise bound or
state the missing hypothesis without changing the target's scope.

Essential local inputs are C033n, C033l and C032q; C033i's residual
and C033j/C032s's exclusion/error qualifications enter through C033l.
Retain divisor/conjugation/multiplicity, excluded ordinate zero,
strip/counting/first-zero/through100/retained real zero, heat,
both fixed-v1 and half-variance qualifications. Their external
correctness and finite-zero data are not independently verified.
C033m is downstream context only. Full matching Mathlib coverage
is unknown. This is a routine application audit of known-tool
specialization, not discovery or a candidate RH audit.

## Separate source-coverage approval1758 — 19 November 2026

This is a literature-only approval, not the application audit. Reused
assessment1756 and source-notes1756, read C033n in full to identify its
source obligations, and inspected C033l's hypotheses/conclusion and
C032q's hypotheses, bounded-integration statement and proof section.
Read the actual stop1571 and stop1576 history entries. The existing
exact-target searches remain adequate; no new search or novelty claim
is made. No source or target hypothesis has changed.

Reopened the primary author PDF, Ante Mimica, *Laplace transform*,
2015 Dresden course, Remark1.2(i), printed p5, Proposition1.4(i)-(ii),
printed p6, and its proof of parts(i)-(ii), printed p7 (PDF indices4-6):
https://web.math.pmf.unizg.hr/~amimica/lt.pdf . The theorem assumes a
positive measure on [0,infinity) with finite transform at every
positive argument. It supplies smoothness and exponentially damped
derivatives there. Part(ii) separately concerns moments and limits
at zero. Its proof uses local exponential domination for difference
quotients and monotone convergence for the zero-limit assertion.
The previously noted extracted equality missing a limit persists;
use the stated theorem and domination argument, not that equality.
No additional proof case or converse is needed for this target.

Coverage map for the pending audit: C033n equations(6)-(8) invoke
that positive-measure derivative theorem and the standard mean value
theorem; their uniform constant and positive neighborhoods are local
application obligations. Equations(9)-(11) use finite sums, bounded
signed integration and the definition of supremum; the reversed
supremum comparison remains an explicit audit obligation. Equation(2)
and the final coefficient/rational choices use finite inequalities
and density of nonzero rationals. The general source is not asserted
to prove these particular budgets. No new derivation, independent
verification of the constants or pass verdict for C033n is recorded.

The finite probability hypotheses required by Mimica are expressly
present in C033l and C033n, conditionally on their inherited inputs.
The source is not being applied directly to the signed width law.
C032q permits bounded real Borel tests and controls variation for the
full signed class; C033l retains all external qualifications listed
in SCOPE. Its numerical finite data and positive gap are parameters,
not evaluated evidence. C033m is downstream context only. Neither
stop1571's enclosure loss nor stop1576's evaluator cost invalidates
this finite-data audit or authorizes restarting either implementation.
Full matching Mathlib coverage remains unknown.

Decision remains SPECIALIZE: coverage is sufficient for the exact
saved audit, without a new stronger input. This is a process approval
with no new mathematical evidence: STEP_OUTCOME is STALLED rather
than a claimed advance. The subsequent audit must test every listed
bound under unchanged hypotheses, and report any failure precisely.
Do not broaden it to support optimization, numerical data generation,
source-wide verification or actual-Xi realization. Discovery priority
remains recorded, but no independently justified central mechanism
has been supplied by this narrow source review.
