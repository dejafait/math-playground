# Exterior sign-boundary localization — 2026-09-14

Inspected the existing changes and completed L215 checkpoint; no interrupted
step was found. The current broad interior exterior bound is unproved.

Scoped calculation: let s=sqrt(2)N and restrict either c or d to distance
H from s. L195 gives |r(c/N)|<=C H/N for that factor, since tanh is
1-Lipschitz and log has bounded derivative on [1,2]. There are
O(N(H+1)) ordered pairs in the union. L213 bounds each fixed-pair
weight by O(Rh/N²), retaining exact cells and coprimality on the left.
Candidate bound: O(Rh H(H+1)/N²). At H=N^(3/4)/log N this
is o(Nh). This applies even after intersection with the remaining region.

Checkpoint: verify the Lipschitz bound, integer rounding for real N and
H=0, union count, and normalization before promoting this claim. The
complement where both factors are farther from s remains unproved.

Completed: L216 proves the bound, including absolute mass and all further
restrictions. Both factor distances must exceed H_* in the remaining
uncontrolled region; no estimate for that complement is claimed.
