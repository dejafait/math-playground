# Completed bounded zero-density common-zero source comparison

TARGET: Assess whether unconditional arithmetic results give N_common([T,2T])=o(T log T) for the exact actual F_0,G pair of L366, sufficient to contradict L385 under eventual physical D≤0.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded discrete-log-modulus, shifted/perturbed Gram-grid, coincidence-density and Lester/Hypothesis-S searches on 2026-10-10; reused the 2026-10-08 actual-common-zero-count comparison and narrowly checked the local recorded failures; exact queries and inspected ranges below.
SOURCE_EVIDENCE: Lester, arXiv:1402.0169v1 (2 February 2014), fixed-grid definition p. 2, Hypothesis S and Theorems 2.1–2.2 p. 3, Corollaries 2.3–2.4 and proofs pp. 3–5, Lemma 5.1 and complete proof pp. 13–15, complete Theorem 2.1 deduction pp. 16–17; previous Kalpokas–Steuding/Korolev/shifted-pair coverage reused.
COMPARISON: The newly inspected unconditional discrete theorem bounds an upper log-modulus tail while explicitly excluding zero ordinates; its near-zero o(T log T) lemma requires Hypothesis S. Both use fixed shifted Gram levels, not L372's full variable response phase. Neither supplies the proposed unconditional exact-grid upper count.
GAP: The unconditional exact common-zero upper count and its falsity remain unproved; no transfer from continuous sampling, conditional spacing or fixed-angle grids is justified. Eventual actual physical D<=0 is independently unproved.
REASON: New primary proof-case evidence identifies the missing spacing premise at precisely the density scale; park this direct discrete-distribution import and propose an independently testable signed-residual mean review, without claiming a literature-wide impossibility.
LITERATURE_REASON: L385's audited positive-density lower count changes the required upper-count scale from o(sqrt(log log T)) to o(T log T); density-scale value-distribution or coincidence estimates were not assessed as an adequate variable-grid specialization.
SCOPE: Fixed actual functions of L366 (1), ordinary real frequency, distinct common zeros on closed [T,2T], every sufficiently large real T, with no RH, F_0 simplicity, noncoincidence or common ODE assumed for the proposed upper bound.

This completed literature-only step is NEGATIVE / NOVELTY_UNCHECKED:
the new source comparison changes the import decision, not a theorem.
EXPLORE records adequate bounded comparison of this exact target; it
does not assert the upper count, its negation, or historical novelty.
No lemma, mathematical script, DAG edge or main argument is changed.

Essential input IDs: L366 for the exact pair, L372 for the full response
phase and simple grid, L385 for the conditional positive-density threshold;
L368, L378 and L384 are already incorporated in audited L385. The upper
bound itself must be unconditional; eventual physical D<=0 enters only
in the proposed downstream comparison with L385. No RH conclusion follows
from refuting that discriminant premise. The main mixed positivity,
total L367 margin, low-index, above-forty and endpoint arithmetic gaps
remain open.

Reuse `drafts/literature/2026-10-08-actual-common-zero-count-bound.md`
for precise previous sources and their inspected ranges. Its fixed-angle
nonvanishing lower bound of order T among order T log T samples did not
provide a tiny coincidence upper bound, and does not by itself establish
zero density either. The actual grid retains the Euler-log phase at
5/2+it and the divided carrier b(t). An ordinary-Gram or constant-angle
theorem needs a justified specialization, not an assumed grid replacement.
A continuous-height small-value theorem alone needs a sampling argument
at the exact grid; do not assume that argument is available. These are
questions for source comparison, not asserted sufficient theorems.

## New primary comparison

Stephen J. Lester, *a-Points of the Riemann zeta-function on the
critical line*, [arXiv:1402.0169v1](https://arxiv.org/pdf/1402.0169v1),
2 February 2014; related IMRN DOI
[10.1093/imrn/rnt356](https://doi.org/10.1093/imrn/rnt356), as listed
on the arXiv landing page. The DOI endpoint was inaccessible; all
theorem/page citations here refer to the inspected arXiv version.
The inspected version has 20 printed pages. The arXiv version history
lists only v1; an initial v2 request returned 404, then v1 was accessible.

The grid is theta(g_n)=pi n−phi with constant −pi<phi≤pi;
Psi=(log log T)/2. Theorem 2.1 unconditionally bounds the normalized
upper-tail count of log|zeta(1/2+ig)|/sqrt(Psi) by the standard Gaussian
upper tail plus o(1), explicitly restricting g!=gamma. Its complete
deduction uses a one-sided off-line comparison, not a lower-tail bound.
Theorem 2.2 assumes Hypothesis S. Lemma 5.1 gives an o(T log T)
count within 1/[log(g+2) log log(g+3)] of a zero ordinate under that
same hypothesis. S requires, for each positive integer m,

\[
\lim_{\epsilon\downarrow0}\limsup_{T\to\infty}
\frac{\#\{T<\gamma,\gamma'\le2T:
 |(\gamma-\gamma')\log T/(2\pi)-m|<\epsilon\}}{T\log T}=0.
\]

The complete lemma proof uses overlapping finite grid blocks to force
many near-integer zero differences, retains enlarged-endpoint
O(log²T) errors, and invokes S for its contradiction. Corollaries
2.3–2.4 concern a!=0; their proofs do not permit setting a=0.
Only the stated comparisons are used; the remaining CLT proof and
its cited Hough source are not imported.

For our target the omitted ordinates are the sought coincidences,
and S is unavailable. Independently, L372 (2)–(6) retains the
variable Euler logarithm at 5/2+it and polynomial carrier b.
No fixed-grid replacement is proved. These are separate failures of
applicability. Exact closed endpoints and distinct counting must be
handled by any later theorem; no such theorem is supplied here.

## Search, reuse and route decision

Queries actually submitted included:

- `zeta zero Gram points proportion zeros o T log T discrete Selberg central limit Lester Hypothesis S`
- `Riemann zeta value distribution perturbed Gram points variable phase zero density nonvanishing`
- `common zeros Riemann xi shifted real part zeta 5/2 Gram points`
- `Lester a-points Riemann zeta critical line shifted Gram points arxiv`
- `"Gram points" "zeros" "proportion" Lester`
- `"perturbed Gram" zeta central limit`
- `"Gram points" "log" "Hypothesis S"`
- `"Lester" "Gram points" "Hypothesis" zeros 2024 2025`
- `"Gram points" "non-vanishing" "proportion" zeta`
- `zeta "variable" "Gram points" value distribution`
- `"Gram points" "zero density" coincidence`
- `"Lester" "Hypothesis S" "Gram" unconditional`
- `"zeta" "Gram points" "zero" "density" "nonvanishing"`

Search hits on approximation models, universality, empirical value
distributions and secondary surveys remain unread leads, not theorem
evidence. No later matching unconditional statement was identified
by this bounded search; that is not a claim of absence. No blocked
Gonek–Ki or Das–Pujahari access search was repeated.

Read L366 (1), L372's phase/count proof through (12), L385's proof and
its relevant audit cases, the previous actual-common-count assessment,
and the adjacent-response-grid source comparison. Scoped searches
found no recorded Lester density comparison in the relevant October
response/count assessments. L379's absolute-margin failure, L383's
positive fixed correlation and the two-cell large-gap stop remain intact;
L375/L376's generic geometry is not reopened. No other notebook was read.

The continuation/abandonment test was an unconditional matching density
theorem with justified variable-grid hypotheses. The inspected lead
fails that test in the explicit zero-ordinate case. Park this import;
do not turn the conditional theorem into an unconditional calculation.
No upper bound, noncommon witness or contradiction of D<=0 follows.

The proposed different intermediate target reviews the signed residual
already isolated in L370, using the now-audited L381 moment/contour
mechanism rather than returning to the persistently blocked sharp-moment
source. Narrow reads of L370 (1)–(8), the blocked October 5 mean
assessment and L381's saved calculation/audit coverage identify that
new idea. Scoped searches found no prior residual-mean result there.
This is continuation selection only: the order-two signed-jet and sharp
tail coverage is not approved and no mean is derived. Its separate
assessment is `drafts/literature/2026-10-10-signed-residual-mean-coverage.md`.
Full matching and supporting Mathlib coverage is **not checked**.
