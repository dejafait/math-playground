# Positive-real-grid endpoint test — working record

STEP_ID being prepared: 2026-11-02-angular-chebyshev-endpoint-01.
The unchanged ready assessment is
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
This bounded attempt tests the saved angular detector through the
Chebyshev subfamily n=3m, m odd, unit residues,
a_k=-5/4+i*r*cos((2k-1)*pi/(2m)), 1/4<=r<=9/20.
Seek sqrt(E_HS)>=c*n^(-A)*exp(-31*n/1000), uniformly in r and n
beyond one onset. A strict exponent margin would absorb C645q's
sqrt(m) loss and exclude countersequences in this band. Other radii,
arbitrary families, Xi realization, layer isolation, census/clearance,
other-pole control, an independent upper bound and signs remain open.

Read C645g's normalization, C645l's exact contour identity (23)--(24),
C645o's weights, C645q's complete proof, the previous full-energy
working note and the angular method-stop records. Reuse the inspected
residue/Fourier inputs in the ready assessment; no new source premise.
C645o/q remain independently unaudited. Their integral/scaling
identities, not the numerical screen, are used. Existing uncommitted
work is preserved.

Proposed mechanism: at u=1, deform the continuous arcsine integral to
two horizontal endpoint segments joined on the left. Obtain uniform
endpoint expansions for spatial coefficients k=0,1, whose two endpoint
vectors are independent. Bound the finite-node remainder on a small
ellipse using C645l (23)--(24). Then quantify an angular neighborhood;
its measure must not consume the strict exponent margin.

Continuation/abandonment test: prove the stated estimate, establish a
rigorous failure of this particular mechanism, or park it with its
precise unfinished inequalities. An endpoint modulus, unbounded
asymptotic expansion, or finite screen is not a lower bound for the
angular mean. No conclusion has yet been obtained.

## Reasoning saved before the full write-up

Use the first two spatial coefficients, with integrands
W(v,u)*v^k/R^(k+1), k=0,1. Their lack of a boundary resolvent permits
a left shift of 1/2 even outside |v|<R. At u=1 the connecting segment
has product gain at least 35*n/531; a 1/10 quadrature ellipse has
error exponent greater than 11/200. Both exceed the endpoint rate.
For |arg u|<=10^(-6), the logarithm of each weight changes by at most
4*n*10^(-6) on these contours. This is a fixed angular interval.

The exact rational endpoint check has upper bound
15559465959309/512000000000000 < 61/2000 for its continuum gain;
certificate: scripts/one-sided-hankel/angular-endpoint-rate-certificate.json.
It uses an upward rounded rational left sum of a decreasing polynomial
logarithm majorant, not sampled numerical quadrature.

On each horizontal endpoint segment, put p=-(log B)'/n. The proposed
uniform bounds are Re p>=1/100, |p|<=2, |partial_v p|<=2.
Replacing the exact exponential by exp(-n*p(endpoint)*h) costs
O(n^(-3/2))*|W(endpoint)| after integration against h^(-1/2).
The two leading spatial vectors (1/R,a_+/R^2) and
(1/R,a_-/R^2) have determinant -2*i*r/R^3, bounded away from zero.
Thus their phases cannot cancel both coefficients. This should give
sqrt(E_op)>=c*sqrt(n)*exp(-(61/2000+4*10^(-6))*n) uniformly on the
band, stronger than the nominated subfamily test. Full hypotheses,
all constants/interchanges and the error comparison are still being
written; this saved sketch alone is not a completed proof.

## Completed attempt

The full proof, exact hypotheses, uniform errors and qualifications are
canonical in [C645r](../lemmas/C645r-chebyshev-band-angular-endpoint-lower-bound.md).
It obtains sqrt(E_op)>=c*sqrt(n)*exp(-0.030504*n) uniformly on the
specified band. The proof directly uses two constant-input spatial
coefficients, avoiding the Hilbert--Schmidt rank loss. The fixed angular
interval has width 2*10^(-6); the contour connecting rate is at least
0.06 and the finite-node remainder rate at least 0.055. Both endpoint
phases remain in the invertible two-column coefficient matrix.

The exact rational rate and all nine auxiliary margin checks passed;
the complete load-bearing certificate fields were inspected. This is
an unaudited local quantitative advance, with no certified novelty or
general-family/RH conclusion. Earlier unfinished work and stop evidence
remain intact. The ready angular assessment is unchanged. The concrete
continuation within that target is a conceptual audit of C645r,
including branches/orientations, relative errors uniform in n,r,u,
two-phase noncancellation and the finite-node identity/certificate.
