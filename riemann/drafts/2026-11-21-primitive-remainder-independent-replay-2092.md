# Primitive remainder independent replay2092: working checkpoint

Task: independent proof audit of C034u under the unchanged SPECIALIZE
assessment2089. Main gap: L030-L032/C032a actual-Xi all-degree mixed
positivity. Intermediate target: C034u(3)-(4) on real X>=1 and integer
1<=K<=X; use: pay one finite-scale error, leaving both signed uppers,
GC6 and the cumulative/mixed transfer unresolved.

Test: recompute the weighted square, squarefree-count error, both
Stieltjes endpoints and dyadic constant independently. Continue only
if the same bound holds without GC6 or a sign assumption; otherwise
repair an exact defect or restrict/park the failed specialization.

Initial replay: the square contributes X^(-1/2)(nk)^(-1/4), the gcd
slot has outside factor X^(-1/2)(ab)^(-1/4), and the continuous
substitution contributes sqrt(X)(ab)^(-1/4). The resulting main
coefficient agrees with M_K. The count tail with floor(sqrt(Y))>=
sqrt(Y)/2 gives 3D(M)sqrt(Y), including positive arguments below one.
Completed: the independent endpoint/dyadic replay and conditional
source interface check pass. The full audit evidence is retained in
C034u's Independent replay2092 section. No estimate was strengthened,
and no mathematical script or numerical certificate was needed.

Route: close this finite-scale audit rather than repeat it. The exact
GC5/GC6 continuation is nominated in review2092 as REVIEW_REQUIRED;
its cap/operator hypotheses need a separate comparison before a proof
attempt. GC6 remains an assumption in C034u(6), not an audited input.
