# Nonnegative-output residual approximation: nomination1893

TARGET: Determine whether C033l's residual transform lies in the uniform closure on [1,2] of mass-one finite signed width mixtures on [1,2] with nonnegative output laws.
CHECKED: 2026-11-20
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Review1894 searched signed-mixture approximation, negative-weight positive densities and positive-cone approximation; inspected Robert--Stoehr2401.16828v1 Sections1-3 equations(1),(4)-(10). Reused source comparisons1551/1552/1562/1565 and scoped C032/C033 sharpness checks; queries, access limits and comparison are in drafts/literature/2026-11-20-positive-output-source-comparison-1894.md.
SOURCE_EVIDENCE: Robert--Stoehr2024 https://arxiv.org/html/2401.16828v1 Sections1-3 assumes nonnegative total density or verified component domination; reused Mimica2015 https://web.math.pmf.unizg.hr/~amimica/lt.pdf Proposition1.4 pp6-7 and Theorem2.4 pp14-16 via notes1562, plus signed Riesz/affine closure via notes1889. None constructs positive-output approximants for this family. Location-scale approximation and Budan--Fourier certification remain theorem/proof-unread leads; no imports from abstracts or snippets.
COMPARISON: C034n supplies unrestricted affine approximation and C034l obstructs cap-two inputs; neither controls positive output. The inspected sampler assumes output positivity or componentwise domination and retains a signed residual in general pairings. Complete monotonicity characterizes a transform after all derivative signs are proved; it does not preserve those signs in affine approximation. Audited C032u supplies exact two-width positive outputs with only a sufficient coefficient range.
GAP: The value d_pos=0 versus d_pos>0 is unresolved. No adequate actual-family closure theorem, all-Borel positive approximating construction or full uncapped separator was located. Full-target discovery remains incomplete, so REVIEW_REQUIRED is retained and dependent approximation work is parked; this is not mathematical infeasibility.
REASON: Review1894 parks automatic signed-mixture/complete-monotonicity imports and optional source-access retries. Nominate the independently testable sharpness of C032u's existing positive two-width family using ready bounded-Laplace and finite-activity coverage in assessment1894. No new lemma, limiting calculation or full-target approval occurs in this literature turn.
SCOPE: Exact C033l residual mu and C032q setwise output nu_eta on X=[0,infinity), W=S=[1,2], finite atomic real eta with eta(W)=1 and arbitrary finite total variation, nu_eta(A)>=0 for every Borel A; no full J_eta=0 condition, moment bound, rate, input positivity or Xi realization. Retain all actual-divisor, heat-error, finite-zero, Gaussian half-variance and fixed-v1 qualifications.

## One discriminating question

For the exact family, set as a prospective test (not a derived result)

    d_pos=inf sup_(s in [1,2]) |muhat(s)-integral_W k_sigma(s)deta(sigma)|,

where the infimum is over the finite atomic mass-one real signed eta
specified in SCOPE with nonnegative output on every Borel subset of X.
The class is nonempty (a single original probability law is admissible).
The useful threshold is d_pos=0 versus d_pos>0. An eventual positive
answer must construct a sequence with exact mass and prove all-Borel
output positivity; a negative answer must give a valid positive lower
bound or separating test for the full uncapped constrained class.
No value or decision for d_pos is established in this nomination.

Plausible downstream use: determine whether the C034n approximation
mechanism can survive this separate law-positivity requirement before
spending work on full odd cancellation. Even a passing test would
leave cancellation, moments, signed-height payment and Xi realization
unresolved. It is not an RH-equivalent claim or an RH candidate.

## Required narrow source review

First reuse source comparison1551 rather than repeat its unmatched
exponential-family, reference-domination, sparse-TV-minimization or
polynomial-certificate imports. Check relevant primary statements and
essential proof cases for approximation by signed mixtures with positive
output, searching exact constrained-approximation terminology and known
obstructions. Ordinary probability-mixture density theorems concern
nonnegative INPUT measures and require a separate applicability argument.
Classical complete-monotonicity characterizations are only leads until
their precise representation hypotheses and an actual-family positivity
construction or obstruction are inspected. Do not replace all-Borel
positivity by finitely many transform inequalities.

Continue to mathematics only if the review identifies a covered exact
result or a concrete bounded construction/separating test with every
extra hypothesis exposed. A restated cone alternative, an affine-density
argument, a fixed-grid solve or unsupported tail-sign recovery is not
such a test. If essential structure is still missing, record that scope
mismatch and choose a different independently testable target; do not
repeat stopped source access. Full matching Mathlib coverage is unknown.
No cross-notebook result is involved.

## Completion1894

The nomination above is preserved as the research question. The completed
comparison is in [notes1894](2026-11-20-positive-output-source-comparison-1894.md).
Additional literature was essential because the ready affine assessment
excluded output positivity. No value of d_pos is established.

The distinct bounded continuation is in
[assessment1894](2026-11-20-two-width-positive-range-sharpness-1894.md).
It tests an existing all-Borel constructor's coefficient range and cannot
decide arbitrary-width approximation. This newly written ready assessment
requires separate supervisor approval on a later turn.
