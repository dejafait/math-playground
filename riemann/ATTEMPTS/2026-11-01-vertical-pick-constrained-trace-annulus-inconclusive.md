# Constrained vertical trace: near annulus remains uncontrolled

WHY IT FAILS: [L642](../lemmas/L642-constrained-vertical-trace-and-uniform-distant-tail.md)
gives the exact rank-deficient projection inside E_N and removes the
complete distant zero tail at the required normalized scale. Its
O(N^(3/2)) tail is smaller than ell_X dim U_X~N^2, but the remaining
1<|Re(zeta)-(X+1/2)|<sqrt(N) annulus is not controlled. The proved
absolute envelope there is O(N^2 exp(N log(17/5)/2)); this is a failed
upper-bound certificate, not an actual-zero lower bound or a disproof
of the desired signed trace. Projection contraction loses the finer
constraints, and no uniform signed cancellation is established.

Park repeating this deterministic projection/envelope test. The
previous boundary-transfer countervectors still need not lie in U_X
and are not reused as a constrained counterexample. A new, independently
testable height average using actual horizontal-zero density is nominated
for separate source review; its exact nonnegative E_N majorant and
remaining favorable-height issue are recorded in
[the nomination](../drafts/literature/2026-11-01-vertical-pick-density-weighted-annulus.md).
Neither that mean estimate nor any density specialization is proved
here. All original arithmetic and boundary-transfer stops remain intact.
