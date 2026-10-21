# Third placement — finite propagation at a varying mass

STEP_ID: YM-20261016-243-third-placement-mesoscopic-polynomial

The unchanged approved target is the joint cubic probe-jet limit in
drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md. The main
construction gap is still an ultraviolet-uniform interacting reflected
bound; continuum axioms and an infrared finite positive mass remain open.

Intermediate target: replace both resolvents adjacent to A in L204(20)
by polynomials of degree O(N^(7/8) log N), with o(N^3) error in the
original signed Q_3 trace. This would remove their long kernel tails
at a sublinear propagation range and separate covariance boundary
effects from the still nonlocal prefixes. It would not prove a limit.

Reuse the ready assessment and L204's mass epsilon_N=N^(-7/4).
Inspected L185, L186's differentiated-prefix bound, L187's repaired
trace order, L202--L204, L018(2), L028's full local residual composition,
and L178's different fixed-mass transverse Neumann approximation.
ATTEMPTS/040,041,044 retain the failures of the absolute count,
universal cyclic cancellation and covariance commutation. The local
search found no mesoscopic polynomial comparison for this trace.
L178's Neumann degree would scale as epsilon^(-1), above N here;
its fixed-degree limit theorem cannot be used with this mass schedule.

Before completing the attempt: use the Chebyshev residual polynomial
r_m(t)=T_m((8+epsilon-t)/8)/T_m(1+epsilon/8), with
p_(m-1)(t)=(1-r_m(t))/t. The numerator vanishes at zero, so p is a
polynomial. For t in [epsilon,16+epsilon], |r_m(t)|<=2 rho^m,
rho=(sqrt(16+epsilon)-sqrt(epsilon))/(sqrt(16+epsilon)+sqrt(epsilon)).
The filter Delta p(Delta+epsilon) differs from
Delta/(Delta+epsilon) by at most 2 rho^m in operator norm. Apply
these errors only at the ends of L204's original whitened factors.
Choosing m=ceil(6 epsilon^(-1/2) log N) should make the filter error
O(N^-2) and response error O(N^(3/2)). Every prefix, projection,
upper jump, insertion subtraction and full heat sum remains.

Continuation test: close a uniform response estimate using the exact
two filter-error placements, and verify finite propagation on all
relative component grids, including normal end rows. Abandon this
particular estimate if it needs an absolute kernel row sum, prefix
commutation, fixed-degree convergence at growing degree, or a bound
on a differently ordered trace. Subsequent coefficient freezing still
needs a uniform error estimate and a signed limiting calculation.

The preceding unfinished reasoning was saved before the full proof.

Completed: [L205](../lemmas/L205-third-placement-mesoscopic-finite-propagation.md)
establishes the relative filter error and both ordered response-error
placements. The selected degree gives O(N^(3/2)) additional response
error at L204's mass; the total comparison with Q_3 remains
O(N^(23/8)), or O(N^(-1/8)) after cubic scaling. Its propagation
range is o(N), and A's compact full stencil gives an exact
infinite-grid comparison of the polynomial legs adjacent to A.

Outcome ADVANCE / RESEARCH / REPRODUCTION. This is a local
standard-method consequence, not progress beyond checked sources.
No mathematical script or literature refresh was used. Checks cover
the full relative spectral interval, polynomial divisibility, both
filter-error orders, the mass/degree exponents and finite-path
agreement, including normal end rows. Canonical reasoning is in L205.

Remaining continuation: retain L204(1)'s exact order and use L205(7),(8)
to evaluate the two actual prefixes before coefficient replacement.
Essential input IDs are L003 L018 L026 L028 L185 L186 L187 L202
L203 L204 L205. Neither prefix is localized. The absolute response
bound O(N^(7/2)) multiplied by d_N/N is not o(N^3), so coefficient
freezing still requires a signed improvement or exact cancellation.
Do not invoke fixed-degree limits with d_N, replace the finite P,
commute prefixes or covariances, discard constant modes, faces or
the upper jump, assume rough-tilt smoothness, signed positivity,
negligible high/high terms or forest invariance. The full heat sum,
both insertion subtractions and both actual probes remain mandatory.
The unchanged ready assessment continues to cover the exact target;
no new assessment is written or approved. Independent higher jets,
full compensation, finer scales, matching, interacting reflected
error and continuum/infrared construction remain unresolved.
