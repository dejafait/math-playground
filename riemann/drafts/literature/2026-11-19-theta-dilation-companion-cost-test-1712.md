# Full-theta dilation companion diagnostic nomination1712

TARGET: Test whether the quadratic and cubic orthogonal residuals force a uniform positive linear floor for C028o's companion trace-norm cost when the full-theta reference is dilated by an arbitrary positive degree-dependent scale.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery1712 compared two mechanisms, reused prior finite-free and companion assessments, and screened local even-reference/adaptive-scale/theta-Gram/Schmeisser records. Exact searches and limits are in 2026-11-19-actual-theta-height-source-notes-1712.md; no matching all-scale theta test was located and no novelty is asserted.
SOURCE_EVIDENCE: Reuse source-notes1694 and approval1696: Schmeisser2002 Lemmas1/4/5 pp211-213 and complete Theorem1 proof pp213-214 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf ; DLMF18.2.11_4-8 and18.2.21 https://dlmf.nist.gov/18.2 . Discovery1712 reopened the measure hypotheses/Theorem1/Corollary1 pp203-207; no general theorem reproof is needed.
COMPARISON: C028o proves divergence only for scale d. C028a/c/h/i/j/k stop other specified reference or similarity families. The difference is uniformity over every positive scale, retaining the full even theta measure and actual centered cubic, rather than inferring an all-scale floor from fixed-scale divergence.
GAP: No arbitrary-scale residual formula, uniform floor or escaping scale sequence is proved. The full cost and actual H_d=o(d) remain unpaid; two small residuals would not upper-bound the full norm.
REASON: The changed scale quantifier has adequate known-method coverage for one finite specialization. The sources do not evaluate the theta residual tradeoff; that check is the proposed research. This newly written nomination requires separate next-turn approval.
SCOPE: Full mu=K(|u|)du/Z of L019/C028o; d>=3 integer; unchanged centered Q_d and A_d of C028h; any s>0 allowed to vary with d; G_d(s)=(integral (s*u)^(i+j)dmu)_(0<=i,j<d), positive upper Cholesky G_d(s)=S_d(s)^T*S_d(s), B_d(s)=S_d(s)*A_d*S_d(s)^(-1), K_d(s)=||(B_d(s)-B_d(s)^*)/(2i)||_1. No translation, tilt, truncation, fitted roots or changed measure shape.
LITERATURE_REASON: Assessment1694 excludes fitted scales. Discovery1712 checks this precise extension while reusing its adequate primary coverage, rather than browsing an unchanged ready target.

## One bounded specialization, after approval

Use the exact centered quadratic/cubic identities and S_2,S_3>0
already established in C028a/h. Keep the full measure's finiteness,
positive density, all moments and parity from C028o/L019. No RH,
real/simple roots, small norm or unknown symmetrizer may be assumed.

For each scale expand Q_d in its monic orthogonal basis. Verify the
norm-preserving coordinates and scaled norm ratios against the imported
full-cost interface; retain only the degree d-2 and d-3 residuals.
Keep all other terms in the full cost. Discarding them gives a lower
estimate only. Do not replace the actual centered cubic by a symmetric
reference coefficient. No residual formula is derived in this assessment.

Seek constants c>0 and D>=3 independent of scale with K_d(s)>=c*d
for every integer d>=D and every s>0, proved from these residuals.
Such a floor stops this scale family's upper majorant as a payment
of C028b's H_d=o(d), without lower-bounding actual root heights.

Alternatively an explicit s_d>0 with the retained diagnostic o(d)
would refute this diagnostic floor, warranting a separate full-cost
assessment. It would not bound the other residuals or prove RH.
A finite grid, failed solver, one chosen scale or unspecified
optimization is inconclusive. Save an unresolved inequality after
one bounded argument and return; no matrix sweep or other measure.

Essential inputs: L019, C028a/h/o and C028b. Actual compact S_F=0,
signed cancellation, output positivity and actual-Xi realization remain
independent gaps. C028f/g's tails and older stops are comparisons,
not assumed upper payments. No cross-notebook input. Full matching
Mathlib coverage is unchecked; unknown is not absence.

This is calculation/REPRODUCTION, not a creative proof attempt or a
new general theorem. Source readiness does not bypass separate approval.
