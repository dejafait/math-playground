# Mixed determinant scale estimate — working record

STEP_ID: YM-20261007-078-mixed-curvature-column-estimate

Reuse SPECIALIZE coverage in `literature/2026-09-26-current-target.md`
for the unchanged complete response target. Main gap: the interacting
response has no ultraviolet-uniform estimate or complete logarithm.
Intermediate test: estimate L061's complete mixed determinant derivative
sum at order a^-2, with its actual probe columns and rough residual.
Downstream use: compare the full mixed group with L059's conditional
coefficient before returning to subleading powers and the logarithm.
Continue if the complete contraction admits that bound or a useful
strictly subleading subterm estimate; otherwise identify the missing
rough estimate and retain the signed sum without a growth claim.

Checks: L048 already has the general contraction; L054–L057 estimate
top/top blocks only. L058's circulation identity and L060's axial-zero
regression are reusable. L061 removes the first-row gradient exactly
throughout the tilt. ATTEMPTS/017–018 still exclude uniform rough-product
smallness and unweighted eta localization. No new literature is needed.

Attempt in progress: for four ordered plaquette edges y1,...,y4, the
sum of their four increasing scalar triples equals
det(y1+y2+y3+y4, y1+y2, y2+y3). This exposes a curvature column.
Its base covariance with either upper potential is zero (DT=0), but
derivatives of that zero under the actual quadratic tilt need not vanish.
Subtracting the upper endpoint rows also exposes Tu without discarding
any derivative placement. Smooth exterior sizes are potentially
(a^2,1,a) on the upper side and (a^2,a,a) on the transverse side;
residual-on-smooth-column sizes gain a^2. These estimates alone do not
control a residual derivative connecting two rough columns.

Unresolved while working: justify full axial sums for the rough mixed
residual block; do not transfer L054's NG^(1/2) R G^(1/2) representation
from the upper/upper compression to upper/interior rows. No completed
estimate or new lemma is claimed at this checkpoint.

Completed partial result: [L062](../lemmas/L062-mixed-same-row-derivative-bound.md)
proves the exact curvature-column regrouping and bounds the entire
three-term same-row Z sum by O(a^-3/2). The complete axial Hilbert–Schmidt
norms are O(N^3/2) for the upper-curvature cross arrays and O(N^3) for
upper-potential/path arrays. Actual smooth exterior bounds, including
the residual-on-smooth-column gain a², give the stated subleading sum.
The full proof and all hypotheses are canonical in L062. No numerical
evidence, new mathematical script or beyond-source claim is involved.

The full intermediate a² test remains incomplete: the six distinct-row
U',V' determinants contain the unestimated rough mixed residual block.
The curvature-column zero holds only for the base covariance, so deleting
its derivatives would be invalid. Next, test those six terms jointly
using L062's exact representation and actual pinned residual operator;
do not extend the top/top compression bound without proving its mixed
analogue. This remains within the unchanged approved response target.
