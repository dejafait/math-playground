# Even-quartic phase gauge: bounded attempt, step 43

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
Its exact cone-distance target is the only research target. The supplied
overview and DAG were used before reading L666's exact family and L673's
full proof. The fixed-gauge contour and strict-slack stops, and the earlier
rectangular even-polynomial diagnostic, were compared. Prior work is intact.

Main gap: actual-Xi mixed positivity. Intermediate test: a phase-compatible
even-quartic gauge could produce an admissible nonnegative approximation
with absolute exponent strictly below -1/100. This would stop the sufficient
cone bound, not the unit-residue Jensen/H application or RH. Those transfers,
general support and Xi realization remain independent gaps.

Use L673's exact nodes, rho=h/10, c=10*pi/27 and gauge

    (1-z/rho)*exp(-n*(c*z+gamma_2*z^2+gamma_4*z^4)),

with real gamma_2,gamma_4. At the imaginary interpolation nodes the added
even-power factor is positive real, so L673's sign argument remains the
candidate coefficient construction. Its quantitative remainder is not yet
controlled. Test the full continuum exponent F+K-c*Re(z)-gamma_2*Re(z^2)
-gamma_4*Re(z^4), allowing a shaped contour in the common pole-free region.
This changes both the old fixed gauge and the rectangular design screen.

Continue on a rigorous continuous exponent below -1/100 by a fixed margin
with all finite-product/prefactor costs paid, or on a quantified obstruction
or a concrete refined mechanism. A floating grid is only a design diagnostic;
it supplies neither continuous coverage nor an asymptotic countersequence.
If the bounded test supplies neither, park this gauge family. No new source
theorem is needed for this use of the already assessed Cauchy interpolation.

## Completed bounded calculation

Outcome: EXPLORATION. No lemma, cone bound, countersequence or certified
quartic obstruction was obtained. The new test allowed connected shaped
contours, beyond the previously recorded rectangular polynomial screen.
The full diagnostic and reproduction command are

    python3 scripts/one-sided-hankel/positive-cone-quartic-screen.py
    scripts/one-sided-hankel/positive-cone-quartic-screen.json

The script evaluates the continuum F of L673 by its elementary integrated
logarithm formula and K by L673's primitive; it does not replace finite W
in a norm claim. All exponent calculations use floating arithmetic and
sampled angles. The data retain all parameter tests, envelope samples,
selected paths, angular indices and threshold failures.

First, independently minimizing each horizontal slice gave a misleading
very low sampled value: the slice minimizers need not connect or enclose
the nodes. This was rejected as a contour test. The subsequent four-neighbor
minimax path search connects negative to positive real-axis points in the
upper half-plane, removing the full limiting segment i[0,9/20] and the
parameter pole disk |x+z|<=1. Reflecting a simple such path gives the intended
contour shape. The path search is finite design, not a continuous extremum.

The connected coarse search used Re(z) in [-.60,.50], Im(z) in [0,1.20],
spatial step .01, and 1024 angles. It tested gamma_2 in [0,4] with step .2
and gamma_4 in [-5,35] with step 2, then a 21-by-21 local parameter mesh.
The best sampled connected maximum was -0.006349867903655752.
The local refinement used spatial step 1/400 on [-.25,.40]+i[0,.70],
1024 angles, and 81 nearby parameter pairs. Its best pair was approximately
(gamma_2,gamma_4)=(.89,-1.7), with sampled maximum
-0.006384223727049528. Testing that path at eight subdivisions of every
edge and 2048 angles gave -0.006382253185456955, at approximately
z=.075+.0690625i and angle 3.034213998437798. The required value is strictly
below -.01 with a fixed margin; the dense diagnostic misses it by about
.0036177468. Both spatial and parameter searches are bounded. There is
no claim that these parameters, paths or sampled extrema are optimal.

Exact rational checks of the selected polygon's edges, pole-disk clearance,
node-segment avoidance, distinct vertices and axis endpoints are included
in the same artifact. These check geometry only; they do not enclose F or
K, establish coefficient error bounds, or certify a continuous maximum.
No finite-product/prefactor certificate was pursued after the design failed
the required exponent. The original L673 proof and all prior stops remain
unchanged. The failure record is
`ATTEMPTS/2026-11-02-even-quartic-connected-contour-inconclusive.md`.

## Continuation, not a result

Park further bounded quartic tuning. A different, independently testable
candidate within the unchanged cone target is to factor out the exact even
part of the rational response at u=-1, rather than a truncated polynomial:

    g_n(z)=(1-z/rho)*exp(-c*n*z)
           /sqrt(W_(x+z)(-1)*W_(x-z)(-1)).

This expression is only a nomination for the next invocation. Essential
inputs are L666's full rational W and L673's phase nodes and Cauchy remainder.
The branch must be normalized at zero and proved single-valued and nonzero
on the proposed contour interior; nodal signs, all parameter poles and
zeros, continuous angular error, and all finite-n costs must be checked.
No favorable branch, sign, exponent, or Xi realization is assumed here.
The bounded next test is whether this exact even-factor gauge admits one
fully paid continuous exponent below -1/100, or a rigorous cost barrier
showing that it cannot supply that sufficient estimate. Stop it if the
branch or cost test fails without a material refinement. Its target and
existing EXPLORE assessment are unchanged; no new assessment was written
or approved during this research step.
