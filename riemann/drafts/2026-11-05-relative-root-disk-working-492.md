# Relative root disks — step492 working checkpoint

Approved target: the exact TARGET in
`literature/2026-11-05-mesh-losing-root-disk-specialization.md`.
This is a conventional SPECIALIZE calculation, not a new central mechanism.

Main gap: actual-Xi all-degree mixed positivity. A uniform all-coefficient
tolerance could support a later particular-model residual comparison;
growing-degree model existence, separation and actual residual bounds
remain independent gaps. No actual-Xi theorem is a premise here.

Proposed prescription: h=(Q-1)/(Q+1), eta=h/2, and
epsilon=h/[2(4+h)] * [h/(2+h)]^(d-1).
For p=a product_j(z-rho_j), positive roots imply
sum_j |p_j| t^j=|a| product_j(t+rho_j), t>=0.
On |z-rho_i|=eta rho_i, the matching factor in
|p(z)|/[sum_j |p_j||z|^j] is at least eta/(2+eta)=h/(4+h).
For j!=i, |rho_i-rho_j|>=h(rho_i+rho_j); the triangle inequality
gives a factor at least (h-eta)/(1+eta)=h/(2+h).
Thus the boundary ratio is at least 2epsilon uniformly in i and
all root scales. Need finish checking disjoint disks, degree exhaustion,
real/simple/positive conclusion and d=1. No numerical script is needed.

Continue only if the complete all-root proof survives those checks;
abandon this prescription if any uncontrolled scale enters. Its small
tolerance is sufficient only; optimality and actual residual comparison
are outside this step. Preserve the older universal/same-mesh stops.
