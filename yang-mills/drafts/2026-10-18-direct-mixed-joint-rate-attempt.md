# Direct/mixed rate — working record

Approved target: assess the complete L217 direct/mixed remainder at
O(N^(5/2) log(eN)^2), for both actual probes. Reuse
`literature/2026-10-18-direct-mixed-action-quantitative-remainder.md`.

The main gap is still the ultraviolet-uniform interacting comparison,
continuum construction and finite positive mass. This selected rate
would help assemble a quantitative perturbative remainder; the plateau
and other component rates remain independent.

Unfinished calculation checkpoint: the internal rows of aJ_N in L211
stay in a fixed compact physical interior. L200's image formula should
therefore give |C Sigma_N-C Sigma_infinity| <= C N^-3 on those rows,
uniformly over every source, including each actual prefix source.
Summing the product difference over the internal rows and the finite
fiber appears to cost O(N^-1), with no moving collar.

For b(s,t)=(1+|s|+|t|)^-3, t in Z^3, the proposed joint majorant is
b(s,t) sum_n b(s+n,t). Summing n first gives C(1+|t|)^-2;
splitting the region |s|+|t|>L suggests total tail O(L^-1).
Consequently its truncated first spatial moment should be O(log(eL)).
Global Lipschitz comparison of the compact, zero-extended displacement
with its value at the output would then cost O(N^-1 log(eN)).
This is a proposed finite inequality, not yet a proved response rate.

Still to verify: the complete shell estimate, finite-image product count,
both frozen half-fiber endpoints, the treatment of fixed/normal source
rows, L222's modal estimates for all four L216 traversal samples,
full heat summation and the exact response/Riemann normalization.
No rough prefix is extended smoothly across the upper pin. No claim
about signed growth, the plateau rate or interacting control is made.

Continue only if these checks close the approved complete error budget;
otherwise preserve the exact remaining loss. No mathematical scripts
or new external theorem are needed for this analytic attempt.

Completed disposition: [L230](../lemmas/L230-direct-mixed-action-quantitative-remainder.md)
contains the full finite inequalities and obtains O(N^2 log(eN)) for
the complete direct/mixed remainder. The proposed kernel/fiber tail
and compact-internal-row comparison close without a moving collar.
The raw four-traversal exterior estimate is matched before the complete
heat sum. This working checkpoint above preserves the initially
unfinished reasoning; all proof details and qualifications are canonical
in L230. Its new rate awaits separate critical audit. No script or
numerical certificate was used, and the independent gaps remain open.
