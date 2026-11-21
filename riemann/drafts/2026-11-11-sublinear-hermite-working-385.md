# Sublinear Hermite attempt — step385 working checkpoint

Approved target and unchanged gate: review383, completed in step384;
the two-center interpolant has m=min(n,ceil(2n/log n)) derivatives at
a=exp(i(n+1)/(4n)) and ell=n+1-m at b=exp(i(n+1)/(2n)).
Only this allocation is being tested. Main gaps remain L030–L032/C032a,
L966/L968 forcing and L984(H). A complete uncapped residual bound would
bound exact-band-null unit-TV target action; the cap and Xi transfer
remain independent unpaid conditions.

Inputs read: C997c(1),(4)–(6), C997s complete kernel and step373 pairing/
kernel audit; review381's inspected Calvi Theorems1.9/1.17/1.18.
C997v's balanced stop is motivation only, not a quantitative premise.
No source refresh, mathematical script or cross-notebook input is needed.

Promising specialization, not yet a checked conclusion: use the circle
centered at b with radius R=9/32, with branch rotated by theta=(n+1)/(2n).
For n>=64 both nodes and both full windows lie inside; the distance
from a to the circle is at least 1/64. On the circle,
|f_n|<=exp(B n), B=-1/4+(7/2)log(32/23)+9/46<307/276.
Thus the contour remainder is bounded by a fixed constant times
exp(B n) (64|y-a|)^m (|y-b|/R)^ell.

On the upper window, |y-a|<=5/16+7/(8n) and
|y-b|<=1/16+5/(8n). Since m/n->0, the logarithmic upper rate after
the complete variation cost tends to at most B+9/32+log(2/9).
On the lower window |y-a|<=1/(4n), |y-b|<=1/4+1/(2n),
and m log n/n->2; its rate is at most B-1/16-2+log(8/9).
Both appear strictly below -1/64. Need finish all branch/enclosure,
coefficient, asymptotic and polynomial-slack checks before claiming it.

Bounded test: rigorous complete C exp(-n/64), or a candidate-specific
obstruction; an insufficient upper envelope parks this allocation.
Do not infer a cap estimate, residual lower bound, or RH progress beyond
the stated intermediate action bound. Preserve earlier stops.

Completed: [C997w](../lemmas/C997w-sublinear-hermite-complete-residual-bound.md)
now contains the full construction, cited input, geometry, complete
bounds and strict-rate proof. The approved target was achieved locally:
the residual is at most 2 exp(-n/32) beyond one existential onset.
Independent conceptual audit remains pending. The early calculations
above are preserved as working history, not a second canonical proof.
