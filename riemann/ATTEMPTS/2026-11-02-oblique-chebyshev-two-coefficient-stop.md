# Oblique Chebyshev endpoint test — bounded method stop

The approved angular detector target was tested via the saved oblique
grid u=exp(i*pi/6) and the first two spatial coefficients, on the
remaining Chebyshev radius band. The exact restricted obstruction is
[C645s](../lemmas/C645s-oblique-chebyshev-two-coefficient-obstruction.md),
with its full rational certificate under `scripts/one-sided-hankel/`.
It is unaudited; no full-angular countersequence is claimed.

WHY IT FAILS: At the admissible endpoint r=1/2 both endpoint weights
decay with rate greater than .036. The connector and exact finite-node
errors can also be bounded with rates greater than .035. The resulting
two-coefficient response on |arg(u)-pi/6|<=10^(-6) is at most
C sqrt(n) exp(-.035n)=o(exp(-n/32)), so this angle/interval and those
coefficients cannot extend C645r across the full upper band. This does
not bound higher coefficients, other angles, the full constant input
or the largest operator norm. It leaves the synthetic angular target
and all Xi bridges open. A subsequent partial-inner-input test would
change the response mechanism and retain the full output; it is not
a repetition of this endpoint test or the full-cancellation rate stop.
