# Signed rectangle: limit of the first-mode absolute-norm closure

The completed boundary balance, full proof and constants are canonical in
[L503](../lemmas/L503-signed-rectangle-transverse-boundary-leakage.md).
The result is unaudited and is a partial necessary condition, not a
nonexistence theorem for the signed detector class.

WHY IT FAILS: the first transverse mode controls the adverse upper
horizontal flux using positivity on the long rectangle, but it leaves
negative side flux in the gap between that rectangle and the real axis.
The available unconditional Fourier estimate for this complete gap term
has factor L^(R/2)/log L. Its combination with the exact boundary balance
gives a vanishing cost lower bound and excludes only c>=R/2 in the
proposed cost, leaving every 0<c<R/2 compatible with this bound. No
unknown boundary term has been set to zero and no impossibility of the
remaining class follows. The prior full-strip stop remains separate.

Stop repeating this identity with the same absolute-value norm closure.
L503 now quantifies the residual: a hypothetical small-cost family must
have negative side-gap flux of order a. Further work must use materially
stronger control of that signed flux from rectangle positivity or change
mechanism. The conditional one-sided O_R(a M) bound is nominated for
separate source review; it has not been derived or approved. Negative
actual-zero contributions, moving-test transfer and RH remain open.
