# Fixed-parameter inverse dilation score: bounded shape test

TARGET: Test convexity of the inverse of h_(1/40)=-sigma_(1/40) on h_(1/40)((0,infinity)), proving it or certifying one full-theta negative-curvature witness without assuming a contact.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed step187 two-cancellation source comparison, including exact/stronger generalized-convex, theta dilation-score/contact and square-coordinate shape queries, and its duplicate/failure comparison. No inspected source supplies inverse-dilation-score convexity at this parameter; this is limited coverage, not a novelty assertion.
SOURCE_EVIDENCE: Karlin–Novikoff, Pacific J.Math.13(1963), Section1 pp1252–1253 and Section3 Theorem1 p1264, https://msp.org/pjm/1963/13-4/pjm-v13-n4-p18-s.pdf ; Leskela–Vihola arXiv:1404.0999v3 Section2.2 Proposition2.3/Remark2.4 p5, https://arxiv.org/pdf/1404.0999v3 ; Csordas arXiv:1309.0055v2 Theorems4.1/4.2(b), https://arxiv.org/pdf/1309.0055v2 , reused through audited L915. Exact inspected passages and extraction limits are recorded in 2026-11-09-two-cancellation-integrated-tail-coverage.md.
COMPARISON: The convex-order theorem requires a convex comparison observable. L915's decreasing sigma supplies an invertible coordinate h=-sigma, but its first-derivative bound and the assessed log-kernel concavity do not state inverse-score convexity. This fixed-parameter actual-kernel shape check is independent of the null contact and the desired flux sign.
GAP: Determine the actual inverse's curvature using the complete theta kernel with justified differentiation and full remainder control. No curvature formula, sign, witness or asymptotic is proved by this assessment. A successful shape test alone would leave all signed-residual and applicability obligations open.
REASON: Test this prerequisite before investing in a contact-dependent hinge residual. One rigorous negative inverse curvature at lambda=1/40 abandons the proposed global-convex sufficient comparison; it does not refute the flux inequality. Positive curvature at samples is insufficient, and a proof at this parameter does not cover the full lambda band.
SCOPE: Newly written ready nomination for separate next-turn approval; no mathematics has been invoked. One fixed parameter, the actual full kernel and its inverse-score shape only. No contact search, parameter sweep, replacement law, polynomial-dual enlargement or general signed-comparison theorem is included.

Use L019/L058/L915's exact definitions, with

    B(x)=log K(sqrt(x)),
    ell_lambda(x)=lambda*x+B(x),
    sigma_lambda(x)=1+2x*ell_lambda'(x),
    h_lambda(x)=-sigma_lambda(x).

The needed monotonicity is audited L915's h_lambda'>19/10 on x>0
for 0<lambda<1/20. The named Csordas shape theorem remains an input,
not a request to reprove it. Any higher derivatives used in the test
need their own justification from the full-series formula. A finite
theta truncation, floating-point plot or unsigned remainder is not a
certificate of the full kernel's curvature.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Downstream use: decide whether the comparison observable in step187's
two-cancellation hinge proposal even belongs to the required convex
class. Keep its residual
`integral (h_lambda(x)-t)_+*(-Q(x)) dnu_lambda(x)>=0`
unproved. The present test does not assert a contact exists.

Continuation/abandonment: prove inverse convexity on the entire image
at this fixed parameter, or give one rigorous negative-curvature witness
with all theta tails retained. If neither is achieved in the bounded
attempt, save the unresolved derivative/tail term and reassess without
an automatic wider sweep. A negative witness closes this global-convex
application only; signed local comparisons would need a different,
separately assessed mechanism.

Essential input IDs: L019/L058/L915. L874 supplies the motivation and
later flux interface, not a premise of the shape test. L914's arithmetic
contracts and c2!=0 are unnecessary. Future contact work must retain
nonzero real c, H2>=0, all three H2c=0 rows and all support patterns;
normalization, inverse endpoint extension, comparison integrability,
hinge sign, flux, initialization, tangency, other parameters, all-degree
continuation and RH remain unresolved. No cross-notebook input.
Full/supporting Mathlib coverage is unchecked, not asserted absent.
