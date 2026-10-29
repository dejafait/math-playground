# Cubic mixed-covariance action term: bounded attempt

Started 2026-10-26 under the unchanged prior EXPLORE assessment
`literature/2026-10-26-complete-cubic-quadratic-asymptotic.md`.
The registered target remains the complete cubic N^2 asymptotic and
comparison with L285(4). This note preserves unfinished reasoning.

Main gap: interacting continuum existence with a nonzero physical sector
and finite positive mass. Intermediate test: control the complete
action/action group containing G_-+, including all internal vertex pairs,
using the exact curl in L286(5). Downstream use: isolate a bounded internal
operator whose source sandwich may have a limit. The two mixed groups,
distinct-line cubic group, full compensation and uniform higher remainder
remain independent obligations. Continue with a complete subfamily estimate;
stop if an internal pair or boundary sum remains unestimated.

Inputs read: L280(18)–(23), L281(9)–(16), L283(5)–(7), (18)–(19),
L284's separated kernels, L285(4)–(9), and the complete L286 proof.
The prior assessment supplies the known-result/duplicate comparison;
ATTEMPTS/047–049 were checked and preserved. This is a Wilson-specific
energy test, not generic gauge cancellation or an unweighted entry fit.

Proposed argument, not yet a result: write D S_3(x)[u]=A(u,x)+B(u,x)
according as the exact cubic curl lands on u or on x. The covariance of
A should be bounded by C log(eN)||Cu||^2 using the complete relative
row-square bound for G. The covariance of B should be bounded by
C||u||^2 using the positive Schur product of CGC* and a local edge
covariance. Apply these to U_pm=GC_pm*sqrt(h_pm), for which
||U_pm||=O(N) but ||CU_pm||=O(1). The full G_-+ group would then be
O(N^2); its external-curl pieces would be o(N^2), leaving a uniformly
bounded internal-curl operator. All internal pairs remain in the
covariance. Exact tensor factors, color independence, boundary
multiplicities and separated external tails still need verification.

## Completed partial result

The proposed estimate is proved in
[L287](../lemmas/L287-cubic-mixed-covariance-energy-bound.md).
It bounds the complete G_-+ action/action group by O_f(N^2) and
removes its external-curl pieces with the full error
O_f(N sqrt(log(eN))+log(eN))=o(N^2). The remaining operator is twice
the covariance of the internal-curl part of the differentiated cubic
vertex; it has uniformly bounded operator norm. Its complete external
mode tail tends to zero uniformly after N^-2 normalization.

The mechanism is a positive Schur-product estimate: the internal
curvature covariance is a projection, and the accompanying edge
covariance has bounded diagonal. Distinct colors make the factors of
each monomial type independent. Cross terms between types are bounded
by the L2 triangle inequality, so no color or vertex pair is dropped.
Only the external-curl piece uses the logarithmic row-square bound;
the source maps have bounded curl norm, making that loss subleading.
The proof works on the complete relative domains, including both
normal endpoints. No numerical script or new external theorem is used.

Checks made in writing the proof: the quadratic-derivative Wick factor
is 2/4=1/2, so E_N is twice that covariance; the original group's trace
factor is 1/4, and its one-color sandwich factor is 3*2/4=3/2.
The complete source-tail bound uses the new energy estimate, rather
than presuming L281's density tail applies to a cubic tensor. These
checks are part of the attempt, not a separate critical audit.

The complete cubic target is unfinished. L286 still controls only its
first group. L287 controls the scale and a leading reduction for one
additional complete group, not its limit. Both mixed insertion/action
groups and the distinct-line action/action group remain unresolved.
No sign or compensation with L285(4) follows.

Continue the unchanged approved target by testing uniform finite-range
approximation of L287's bounded internal-curl operator on the actual
source fields. A successful approximation and bulk coefficient would
determine this group's limit using the established external tail.
Unweighted entry convergence is still insufficient; operator or complete
sandwich error is required. This is a concrete continuation within the
existing assessment, not a newly approved theorem or a proved limit.
The other groups and uniform higher remainder remain open even if that
test succeeds. No localization route is declared exhausted here.
