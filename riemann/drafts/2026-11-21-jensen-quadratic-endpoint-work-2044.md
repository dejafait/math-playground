# Fixed N=6 quadratic/Jensen calculation2044 — working record

Approved target: exactly the TARGET in
`literature/2026-11-21-jensen-quadratic-endpoint-test-2043.md`.
The supplied ready EXPLORE assessment is reused without new literature.

Main gap: L030-L032/C032a actual-Xi all-degree positivity; C029m's
eventual Hermite index bound is unresolved. Intermediate target: test
whether the fixed quadratic/Jensen commutator has zero p_2,p_3,p_4
coefficients, after verifying the full numerator equals T_6. Potential
use: prerequisite for the proposed endpoint-only signed-defect route.
One strictly nonzero bulk coefficient rejects this ansatz; three exact
zeros give only a finite pass; enclosure overlap with zero is inconclusive.

Inputs read: C029m's full finite coefficient formulas; C029n's S
normalization, Bernoulli table and fixed rational interval proof;
completed review2043 and the distinct C029q/r/s/t stops. Recurrence(2)
and multiplication(9) will be compared by direct polynomial expansion,
including n=0,1. Preserve all odd terms and the original Jensen weights.
No changed degree, precision, root count or uniform sign claim is covered.

Completed: full numerator equality is exact; each bulk coefficient is
strictly negative in the unchanged enclosures. Canonical proof: C029v.
All exact data are in scripts/pollaczek/jensen-quadratic-endpoint-2044.json;
38 identity/implementation checks pass with no failures. The complete
load-bearing coefficients, raw endpoints, numerator residual and constants
were inspected with selected full JSON values. Stop this fixed ansatz.
Auxiliary hyperbolicity, signed index transfer, uniformity, actual-degree
control, initialization and weighted-limit/upstream[9] remain unresolved.
