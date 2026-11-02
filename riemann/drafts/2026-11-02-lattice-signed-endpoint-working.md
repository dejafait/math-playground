# Signed endpoints of the actual L663 lattice

Prepared STEP_ID: 2026-11-02-lattice-signed-endpoint-10.
RESEARCH / proof_attempt under the unchanged invocation-start EXPLORE
assessment `literature/2026-11-02-localized-logarithmic-joint-moment.md`.

Main gap: the original integer family's paid localized logarithmic
comparison, with actual-Xi realization and signs independently open.
This bounded subtest uses precisely L663's n=6q+3>=9, Y=9/20,
h=27/(10n), a_l=-5/4+i*l*h, -q<=l<=q, unit residues and M=n/3.
Keep every grid factor, conjugated angle, all spatial moments and D's
squared residues. L662's half-turn census is a method comparison only.

Intermediate target: a complete signed endpoint expansion for k=0,1
at a suitably chosen angle, with nonzero multiplier and negligible
complete-contour remainder. Seek max_(u,k<=1)|c_k(u)| >=
n^(-C) exp(-rho*n), rho<261/20000. L661's diagonal bound and L658's
localization would then give a paid arc for this lattice only. The
coefficient-to-Mahler loss must be paid for the complete polynomial.
An endpoint rate/remainder obstruction must be quantified before
parking this subtest; a numerical sample alone is not decisive.

Read L649 definitions, L663 sections 1--4, L658 hypotheses and
localization proof through its root accounting, L662's signed contour
development and L661's general diagonal proof. Read the full-circle,
absolute-contour and half-turn stop records and the latest audit
history. The supplied assessment and these records cover the imported
residue and logarithmic tools; no changed source premise is proposed.

Unfinished reasoning saved before calculation: the kernel is exactly
K_n(y)=i*lambda*n/(exp(i*lambda*n*y)-1), lambda=20*pi/27.
At y=+/-Y+i*t/n its rescaled value is
-i*lambda/(1+exp(-lambda*t)). The local product multiplier depends on
p(u)=integral_0^1 partial_y log W_(x+i*y)(u)|_(y=+/-Y) dt.
Need 0<Im p<lambda, a nonzero signed limiting integral, and uniform
tails on both sides. The audited L663 vertical derivative bounds may
provide the tail control. Both horizontal edges still need a strict
exponential separation from at least one endpoint, and both endpoint
contributions must remain in the coefficient comparison.

## Rate obstruction identified before a signed asymptotic expansion

The continuum diagnostics (not proof) suggest that neither endpoint
can reach the proposed rate. The existing audited angular rows permit
a stronger test without another finite-n screen: use the uniform
lower second-derivative bound -100 and the chord error
100*pi^2/(8*512^2) to turn their top and both endpoint grid upper
bounds into bounds at every angle. All three appear below -29/1000.
The bottom envelope is much larger; it cannot be discarded.

If this exact aggregation passes, L663's vertical monotonicity and
finite contour imply that G minus its entire lower-horizontal-edge
integral is uniformly O(n^2 exp(-29n/1000)) on the product torus.
This would obstruct an endpoint-dominated proof at rho<261/20000
and isolate the remaining signed lower-edge term with all M moments.
It would not settle the arc criterion: the diagonal upper bound is
only a sufficient comparison, and a small additive polynomial error
does not by itself control a logarithmic mean near zeros. The lower
edge must carry the proposed two-coefficient bound if it holds.

## Completed bounded attempt

The exact test passes. The proof is canonical in
[C663a](../lemmas/C663a-lattice-endpoint-remainder-and-bottom-isolation.md),
with complete new aggregation in
`scripts/one-sided-hankel/lattice-endpoint-remainder.json`.
All 513 source rows match their audited replay; all 512 angular cells
pass each of the top and two side bounds after the chord charge.
This proves a uniform O(n^2 exp(-.029n)) remainder after retaining
the exact bottom-edge polynomial. The gap to the sufficient
two-coefficient loss .01305 is .01595, so endpoint dominance is
parked without attempting an asymptotic multiplier already below
the required scale. Outcome NEGATIVE; this is not a criterion
counterexample. The signed bottom contribution and the general
logarithmic comparison are unresolved. No new source premise was
needed, and the ready assessment remains unchanged.
