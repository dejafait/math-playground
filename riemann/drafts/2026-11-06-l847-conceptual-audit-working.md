# L847 conceptual audit — working checkpoint

2026-11-06. One mathematical audit under the pre-existing EXPLORE
assessment `drafts/literature/2026-11-06-actual-g-product-radial-graph-obstruction-audit.md`.
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: verify L847(1)–(15) at fixed r=2,k=1; its downstream
use is to exclude independent radial contour choices, not coupled graphs.
Continue only if every essential implication survives; repair or narrow
the stated obstruction if one fails. No cross-notebook input.

Read the full L847, L018, the definitions/coefficient passage in L775,
and L846 through (3). Reused the supplied complete source assessment,
including its Ng–Yao overlap; read the existing product failure and
construction history. L846's relative-cycle obstruction is not used.

First pass: the two factors 1/i cancel F's minus sign. Directly expanding
det(I-i Du) gives 1-det(Du)-i tr(Du). The angular projection is a left
inverse of each graph. The C^2 homotopy stays in compact annuli, including
all numerator zeros. For the product curves gamma'=gamma(v'+i) is
nonzero. Isolated G zeros and fixed-point coincidences give only finite
exceptional sets. The ratio's square root is the reciprocal of the
prefactor in (7), as required. The resulting real polynomial is a genuine
circle or line through two distinct points. Continuity restores every
excluded parameter; radial coverage rules out a line and forces the
entire circle enclosing zero. Repeating with one point fixed forces the
second curve onto the same circle. No defect found in these steps.

Outstanding before acceptance: spell out C^1 Stokes on the parameter
cylinder and the two boundary signs; verify both orientation changes,
the diagonal limit, centered coefficient mismatch, entire remainder,
all terms/signs of (14), and the nonzero quadratic leading coefficient
needed for the full root limit. Audit remains unfinished at this checkpoint.
No mathematical script or numerical certificate is needed.

Completed later in the same bounded step: every outstanding item passed.
The canonical proof in L847 now includes explicit C^1 parameter-cylinder
Stokes applicability, both boundary signs, the expanded polynomial in
(14), its eventual two-sided quadratic bound, precise standard citations,
and the independent audit verdict. The coefficient thresholds are exact:
positive root limsup 0 versus negative root limit |c|/rho>0 off center;
centered b_-2=0 versus b_2=a_3 rho^2>0. No theorem was strengthened and
no new general rationality result was obtained. The initial unfinished
checkpoint above is retained as a record, not a current pending task.
