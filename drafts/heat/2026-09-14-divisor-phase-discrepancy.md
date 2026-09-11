# Divisor-phase discrepancy checkpoint

Date: 2026-09-14. L227 is complete; existing changes are preserved.

Scoped calculation: restrict to square-root cells wholly inside J, losing
O(N³) candidates; express the coprime open-cell count by finite Möbius
inversion and exact floor/ceiling counts. Compare the cell-length sum
against B_0 by a bounded-variation sum/integral estimate and Fubini.
The desired aggregate phase cancellation remains unproved.

For alpha=sqrt(avb-R), beta=sqrt(a(v+1)b+R-1), the exact
multiple-of-e count in the open cell is
(beta-alpha)/e + {alpha/e}-{beta/e}-1_{beta/e integer}.
The upper endpoint atom must not be discarded. On the candidate range,
ell'=a/(2 beta)-av ell/(2 alpha beta)=O(1/N).
The real inverse width is m²/[av(v+1)]+R/(av)+(R-1)/(a(v+1)).
These identities should give O(N³) aggregate benchmark error, retaining
phi(a)/a outside and phi(a)/a from finite divisor inversion inside.

Resume here if interrupted: verify boundary-cell count, the sum/integral
comparison on the contained-cell interval, and all error totals before
promoting the reduction. No little-o bound for the phase sum is claimed.

Completed: the reduction and all O(N³) errors are proved in L228.
The exact inversion test passed 12,800 cases, including 1,705 upper
endpoint atoms. The aggregate phase bound is still unproved; no draft
cancellation claim has been promoted. The current next action is in
PROGRESS.md.
