# Full Robin residual diagnostic, step 70

Invocation-start gate: unchanged EXPLORE assessment
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
Main gap: actual-Xi mixed positivity. Target: the prescribed-node positive
approximation stated there. This bounded subtest evaluates L681's existing
weights at q=1,2,4,8, retaining W_(-R), the unit anchor and the whole sum.
Independent H/support/realization/sign gaps remain open.

Continue asymptotic cancellation development only if the two largest
rigorous effective-exponent intervals lie above 1/100; otherwise park
this finite diagnostic, without claiming asymptotic impossibility.

Inputs inspected: L666 (6) and its quadrature scope; L673's exact root
equation and uniqueness proof; L681 (1)--(11); C681a's restricted
fixed-rectangle stop. Existing floating screens concern the contour
integrand, not the residual. The paired angular-mean attempt was
inconclusive and supplies no norm upper bound. No new sources are needed.

Uncertified initial dense-grid values of the full norm are approximately
3.45697, 3.03835, 2.14583, 1.98751, respectively. They are design data,
not evidence for a theorem. A certificate must still enclose exact roots,
rounding and the continuous circle mean. Planned implementation: outward
interval products on a complete roots-of-unity grid, with a rational
annulus/Cauchy bound for the omitted Laurent aliases. All error estimates
and full output will be retained. No asymptotic conclusion is intended.

Completed disposition: [C681b](../lemmas/C681b-robin-full-continuous-finite-residual.md)
contains the full proof and evidence paths. The initial rectangular
propagation failed at q=4,8 and is preserved; centered complex balls
give all four enclosures with the complete angular error paid. All
63 norm checks and four exact-logarithm checks pass. Both largest
effective exponents are negative, so this finite diagnostic is parked
under its predeclared test. This is no asymptotic obstruction. The
sole current continuation is in PROGRESS.md, using the unchanged
ready assessment and a different positive-weight construction.
