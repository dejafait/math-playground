# Two-observation primal interpolation nomination1796

TARGET: Assess whether C033w's two-observation problem S={1,2} admits a certified primal interpolation using widths {1,3/2,2}, with a finite conditioning/error budget and total variation at most2.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate review1797 inspected primary Rump Theorem10.2 and Arb2.23 solve contracts; exact queries, local comparison and bounded test are in drafts/literature/2026-11-19-two-observation-primal-source-notes-1797.md. No matching fixed-three-width result was located; no novelty inferred.
SOURCE_EVIDENCE: S.M.Rump, Acta Numerica19(2010),287-449, corrected author PDF Section10.3, Theorem10.2/(10.8)-(10.9), PDF p53, https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf ; Arb2.23 arb_mat_solve/solve_preapprox, https://arblib.org/arb_mat.html ; reuse C033m/audit1755 and C032w/audit1575 with Connes Section2(4)-(9), https://alainconnes.org/wp-content/uploads/heat-zeta.pdf .
COMPARISON: General verified-solve coverage suffices for a bounded conditional certification test, not invertibility or TV<=2. C033m already completes the residual interface omitted by the nomination; its analytic effectivity supplies no useful runtime. C032x/common-disk and Gaver stops remain intact.
GAP: Actual scalar enclosures, their attainable cost and precision, a certified nonsingular matrix, exact weights and TV<=2 remain unestablished. Approve only the fixed-support preflight and subsequent solve if its input-error budget is affordable; failure is local to this construction/evaluator.
REASON: Review1797 completes missing numerical source coverage without deriving an interpolant. Import the general verified-solve theorem; justify only the application. Same saved target is now approved for one bounded research attempt, including an informative cost rejection before any expensive evaluation.

Use C033w's exact m(s) and k(s,sigma), W=[1,2], and the full signed
mass-one cap-2 class. The proposed later test seeks real weights
w_1,w_2,w_3 at the fixed widths 1,3/2,2 satisfying mass one and exact
matching at both s=1 and s=2, with sum |w_j|<=2. These are target
conditions, not a solution or an existence assertion. A nonzero
residual from rounded weights is not exact interpolation.

The nomination originally required source comparison only; separate review1797 has now completed that comparison. Reuse adequate primary
evaluation coverage; inspect canonical evaluator statements and actual
stops before selecting an implementation. Identify how rigorous scalar
enclosures and linear-system conditioning could certify exact weights
and their full TV, or reject useful resolution before an expensive
evaluation. Do not assume total positivity, a Chebyshev property or
matrix nonsingularity from C033g's different kernel. Do not run stopped
independent boxes, common-disk or growing-order Gaver evaluation.

A verified solution with TV<=2 would be an admissible primal input for
this finite problem; the implications should be justified in the later
research step using C033w. A singular, badly conditioned or unresolved
fixed-width system would stop only this construction, not all continuum
widths or strict dual certificates. Preserve failed error budgets.
No positive lower bound for d_2, arbitrary-variation rate, full odd
cancellation, signed-height estimate or actual-Xi realization follows.

Essential continuation inputs are C033l/o/w and the exact transform and
excision evaluators selected after review. Keep all actual-divisor,
conjugation/multiplicity, excluded ordinate-zero, strict strip/gamma>14,
counting, through100/retained-real-zero, reciprocal-square-tail, heat
positivity/separate fixed-j error, half-variance and both fixed-v1
qualifications. No external data or source-wide preprint correctness is
independently verified. Matching Mathlib coverage is unknown/unchecked.

## Separate approval1797 — 19 November 2026

Use source-notes1797 for the exact preflight and stop rules. Source
coverage is ready, while every mathematical application and numerical
claim remains for research. This is the same nominated target, not a
newly derived or self-approved interpolation result. Retain the
historical nomination and its exclusions above. Reuse C033m's audited
residual evaluator, not nomination1752 alone. Full matching Mathlib
coverage remains unknown. No lemma or mathematical script changed.
