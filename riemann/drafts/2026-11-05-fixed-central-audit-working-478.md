# Step478 — fixed central model audit in progress

Completed: the canonical audit is now in L791; full rational/replay
evidence is `scripts/central-jacobi/audit-478/audit-report.json`.
The initial reasoning below is preserved as the pre-calculation checkpoint.

Approved target: critically audit L791's inherited coefficient error,
exact parameter existence and five positive model-root brackets. Reuse
the unchanged SPECIALIZE assessment for this target. Main gap remains
actual-Xi all-degree mixed positivity; this finite representation pays
none of the index5 residual or growing-degree signs.

The supplied orientation was used without rereading it. Read L791 and
its implementation, L778's exact evaluator definition, full complex tail
bound and prior analytic audit, and the step476/433 histories. Existing
work is preserved. The first attempt at listing local changes was too
verbose; subsequent inspections are restricted to the files needed here.

Analytic checks so far: P_0 denotes exact finite integrals, with quadrature
uncertainty already in its coefficient intervals. Its entire difference
from G has uniform error on the closed radius1600 disk, so Cauchy adds
E_G/1600^j to each coefficient, not a derivative of a real bound.
The matching normalization is gamma(j)=8*4^j*j!*a_j. Full-box parameter
derivatives hold with the actual D fixed; independent data intervals
enlarge the domain safely. Invertibility follows from the strict
I-M DF norm bound, and degree5 plus five disjoint strict brackets implies
simplicity. These observations still require finite-certificate checking.

Next within this audit: independently check all finite arithmetic with
rational directed enclosures, replay the original program at a fresh
output path, and compare its full certificate while preserving originals.
Do not calculate a new residual or model. A different continuation must
be nominated with REVIEW_REQUIRED, comparing it to the existing
prescribed-primitive source limitation; do not repeat source approval.
