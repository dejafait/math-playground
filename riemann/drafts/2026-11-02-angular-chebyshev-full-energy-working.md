# Radius-adjusted Chebyshev full angular energy — bounded attempt

Prepared STEP_ID: 2026-11-02-angular-chebyshev-full-energy-01.
Unchanged ready assessment:
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
This is one mathematical attempt on that exact target, using its
Fourier/coefficient and admissible-countersequence scope.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Intermediate target: decide whether the full angular mean of the largest
Hankel norm can be smaller than c exp(-n/32), using the radius-adjusted
Chebyshev family n=3m, m odd, unit residues and
a_k=x+i*r*cos((2k-1)*pi/(2m)), 0<r<=1/2. The same poles and residues
serve all angles; x=-5/4, R=11/8, eta=1/100, and the denominator has
the conjugated angle. A countersequence would stop this synthetic
detector; a positive detector would still need layer isolation, other
poles, census/clearance, simultaneous Xi realization, an independent
upper bound and signs.

Inputs read: C645g normalization, C645l admissibility and contour proof,
C645o exact angular weights and complete residue formula. C645o remains
independently unaudited. C645m and C645p are method-specific contrasts;
their failures are preserved. The related angular working notes and
ATTEMPTS were checked. Reuse the ready assessment's inspected Fourier,
operator and residue sources; no new source premise or novelty claim.

Proposed full-energy reduction: if c_k(theta) are the exterior symbol
coefficients, the Hilbert--Schmidt energy is sum_(k>=0)(k+1)|c_k|^2.
Its angular mean should be the complete signed sum with entries
U*I(a,b)/(U-a*conjugate(b))^2. This must be justified before use.
It controls the largest operator norm from above and, since the rank
is at most m, cannot change exponential rates by more than sqrt(m).

Continuation/abandonment test: a rigorous full-mean upper rate strictly
above 1/32 gives a countersequence; a rigorous obstruction for this
family/majorant changes route. Finite screens are only diagnostic and
must retain both angular signs and every spatial coefficient (or state
their unbounded tails). Save any unresolved analytic inequality rather
than infer asymptotics from a screen. No conclusion yet.

## Completed bounded attempt

The complete reduction, interchange proof, rank comparison and
varying-radius admissibility are canonical in
[C645q](../lemmas/C645q-complete-angular-hilbert-schmidt-energy.md).
It gives E_HS=sum r_a*r_b*U*I(a,b)/(U-a*conjugate(b))^2 and
E_HS/m<=E_op<=E_HS. Thus the majorant loses at most sqrt(m), with
no fixed exponential loss. At the exact target exponent, this
polynomial factor still matters. No uniform lower bound, upper decay
rate, or countersequence has been proved. This is an unaudited
standard-mathematics specialization; the step outcome is EXPLORATION.

The diagnostic file
`scripts/one-sided-hankel/angular-chebyshev-full-energy-screen.json`
contains 32 sampled families: n=51,99,195 with eight radii from 0.1
to 0.5, and n=387 with eight refined radii from 0.24 to 0.34.
It uses 2048 angular samples and 256 spatial coefficients, retaining
both angular signs. At n=387 the best sampled radius was 0.28:
root sampled/truncated energy 0.5691806815, apparent root rate
0.00145622055, versus required rate strictly above 0.03125 for the
countersequence strategy. These are neither enclosed integrals nor
asymptotic estimates. All 32 complete records were inspected using
the shared JSON inspector; there is no certificate to verify.

The screen also records endpoint product-gain diagnostics. At the
positive-real grid u=1, the sampled continuum endpoint gain for r=0.45
is about 0.0303332345, below 1/32, while r=0.5 gives about 0.0370864208.
Neither an endpoint value nor its gain proves a lower bound for a sum
of nodes or an angular mean. The strongest angular responses in the
screen often occur away from the negative-real grid; small values at
that single angle are therefore uninformative for an upper bound.

## Preserved analytic question

A concrete refinement is to test, for the compact radius band
1/4<=r<=9/20 and odd m with n=3m, a uniform lower estimate
sqrt(E_HS)>=c*n^(-A)*exp(-31*n/1000), with c>0, finite A and one
onset. By C645q this would exclude countersequences in that band at
the required exponent, despite the polynomial rank loss. It would
not settle other radii or arbitrary common-pole configurations.

The proposed mechanism uses C645l's exact finite-node contour identity
at the positive-real grid u=1, controlling both endpoint contributions
in at least two spatial coefficients so their phases cannot be
silently identified or discarded. It must bound the finite-node
remainder and then pass to an angular neighborhood whose measure and
errors have no uncontrolled exponential loss. The endpoint diagnostics
only motivate the proposed constant 31/1000; they do not establish it.
Uniformity in r and n, cancellation, the quadrature remainder and
angular integration are all unresolved. No uninspected asymptotic
theorem is an input. The ready contour/Fourier scope is reused.

The other mathematical inputs are C645g's normalization, C645o's exact
weights (its independent audit remains pending), and C645q's new
unaudited reduction. C645l's old fixed-direction product gain is not
rotation-uniform and must not be imported as such. Retain every
original family hypothesis and all independent actual-Xi gaps.
A subsequent attempt should prove this quantitative estimate, find a
rigorous failure of the proposed endpoint/remainder mechanism, or
park this refinement; another finite radius sweep is not decisive.
