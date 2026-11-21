# Fixed actual-theta Gram metric: bounded quadratic-cost test

TARGET: Test the fixed actual-theta Gram companion metric by identifying its full Schmeisser cost and checking whether the prescribed degree scaling forces a positive linear floor from the quadratic orthogonal-polynomial residual.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1694 completed nomination1693's theorem discovery, metric comparison and recorded-failure screen; queries/read limits are in drafts/literature/2026-11-19-actual-theta-gram-source-notes-1694.md. No exact evaluated theta cost was located; no originality assertion.
SOURCE_EVIDENCE: Schmeisser2002 Lemmas1/4/5 pp211-213 and full Theorem1 proof pp213-214 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf ; DLMF18.2.11_4-8,18.2.21,(viii) https://dlmf.nist.gov/18.2 ; Simon2011 Proposition1.3.6/Theorems1.3.7-8 pp16-17 https://assets.press.princeton.edu/chapters/s9377.pdf ; reuse1523 Higham2021 identity(*) https://nhigham.com/2021/03/23/what-is-a-companion-matrix/ . ETNA54 Theorem2.2/Section2.2 is a convention comparison with an interval qualification, not an unbounded-theta estimate.
COMPARISON: The method is known; the difference is the fixed measure, Cholesky orientation, coefficient scale and residual norm. C028a/c are restricted reference families; C028h/i are restricted similarities. Review495 is a different Gram object and stops551/571 forbid unsupported reference-root hypotheses.
GAP: No specialized basis correspondence, quadratic residual formula or cost floor has been proved. An actual o(d) root-height payment remains open. A small retained residual cannot establish small full cost.
REASON: One exact coefficient/norm test can discriminate this metric before high-degree computation. This newly written continuation requires separate next-turn approval and is not executed by its source review.
SCOPE: Full K of L019; dmu(u)=K(|u|)du/Z on R, Z=2 integral_0^infinity K(u)du; integer d>=3; G_d=(integral (d*u)^(i+j)dmu(u))_(0<=i,j<d); positive upper Cholesky S_d with G_d=S_d^T S_d; exactly C028h's A_d and B_d=S_d A_d S_d^(-1). No fitted scale, truncation, unknown real roots or positive symmetrizer.

## One bounded test

Keep nomination1693's definitions. Justify normalization, all absolute
moments, infinite support and strict positive Gram forms from L019.
Keep scaling d exactly; changing it is a different target.

Identify coefficient-space multiplication modulo Q_d and the orthonormal
basis determined by upper Cholesky. Check the direction of every basis
map and any transpose or orthogonal equivalence before importing full
cost. A characteristic-polynomial match alone does not establish norm
equality. Use Schmeisser's unbounded-measure hypotheses, without silently
extending the separate ETNA closed-interval statement.

Expand through the quadratic coefficient below the leading term only.
C028h supplies the exact centered first/second coefficients and S_2>0.
Compare the external measure's monic recurrence, carrying all degree
factors and norm ratios. Test whether this nonnegative full-cost
contribution forces cost>=c*d for some fixed c>0 and all sufficiently
large d. No residual formula or desired inequality is asserted here.

If support is used to control cumulative recurrence data, justify the
implication: Simon's bounded-support construction alone does not identify
an arbitrary supplied measure. Verify identical normalized moments and
use the inspected uniqueness statement, or give the finite-moment
argument needed for the specialization. Do not assume polynomial density
for an arbitrary unbounded measure or individual recurrence asymptotics.
No detailed rapid-weight theorem is a premise.

A proved linear floor abandons this majorant only: it lower-bounds an
upper estimate, not actual root heights. A complete o(d) full bound
would pay C028b and require later critical review. A small retained term
or unverified correspondence is inconclusive; preserve that limitation
and stop after this test. No parameter variation or finite-degree sweep
is approved. Any unrelated continuation needs its own assessment.

Essential inputs: L019, C028h's A_d/established second coefficient,
C028b's criterion. C028a/c/i and review495/stops551/571 are comparisons.
No Xi root premise, actual Favard realization, Newton-sum positivity,
backend certificate or cross-notebook input. Mathlib matching unchecked.

Intended work: calculation/standard/high, RESEARCH/REPRODUCTION. This is
known-method specialization, not creative work. Separate approval is
pending; further browsing is unnecessary unless that review exposes an
essential missing hypothesis.
