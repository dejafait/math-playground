# Uniform range enclosure of the exact bulk-Haar integral

Step 188's complete bound and proof are canonical in
[L426](../lemmas/L426-covariance-free-bulk-actual-height-phase-average.md),
in its bounded-enclosure section. The full 32768-cell certificate is
`scripts/discriminant/bulk-haar-integral-enclosure-188.json`.

WHY IT FAILS: The three-prime, uniform 4^3 by 512 mesh retains the entire
response and the exact mixture but gives only -0.301<=I<=0.207. Reusing
the exact complementary trace gaps reduces unresolved selector mass
from 7/16 to 3/64 on the same cells. Even then the joint strict-cell
range width is about 0.446799, with another 0.060248 from the complete
branch-cell range. Coefficient and full-tail uncertainty are included
inside those ranges, rather than discarded or assigned independent
errors. These budgets cannot certify a sign. Stop this uniform mesh;
this is no lower bound on the achievable width of adaptive integration,
no proof that I=0, and no rejection or realization of the law. An
adaptive observable-driven subdivision is a specific, independently
testable refinement within the existing ready assessment. The earlier
sampling stop remains preserved.
