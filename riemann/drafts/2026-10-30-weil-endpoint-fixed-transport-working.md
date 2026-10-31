# Endpoint-fixed transport: bounded attempt in progress

2026-10-30. The supplied prior EXPLORE assessment
`drafts/literature/2026-10-30-weil-endpoint-fixed-transport-coverage.md`
authorizes exactly this mathematical attempt. No additional source
coverage or new theorem is being approved during it.

Main gap: actual-Xi all-degree positivity; the immediate conditional
gap is S<=P-H at L516/L522's normalized nullvector. The proposed
intermediate target is an independently signed deformation estimate
from one smooth spatial field equal to x on a fixed interior bulk
and zero near both endpoints. If it controls the prime slopes beyond
the existing identity it could force zero flux. Realization, family
O(lambda) bounds, collars and Xi transfer remain separate.

Retain L515's killed smooth-core domain, L516's complete form and
fixed c, nu_rho, pole, both prime shifts and equality atoms, L521's
BV conclusion and L522's continuous representative/prime limits.
Assume nonnegativity only on this fixed interval, a real normalized
nullvector, nonzero left trace, ell>log(2), and the excluded reflected
image collision. L523 and the L517/L518 stops are comparisons, not
additional established premises of a transport formula.

Planned check: first bound finite pullbacks on the actual reference
part-form domain. Then differentiate the whole energy by finite
changes of variables and BV measure limits, without assuming an L2
transport generator or H1 regularity. Test the signs only after this.
An exact stationarity identity, a generic absolute bound or a
trace-vanishing premise fails the continuation test. Shrinking collars
are allowed only after a favorable fixed-collar comparison is found.

Finite-transport calculation checkpoint: take F_t(x)=x+t X(x) and
W_t f=sqrt(F_t') f o F_t, with X smooth and compactly supported
inside I. With R_t=F_t^(-1), j_t=R_t', the reference energy becomes
one half the integral of
[sqrt(j_t(y))f(x)-sqrt(j_t(x))f(y)]^2 n(R_t(x)-R_t(y)).
The inverse maps are uniformly bi-Lipschitz and identity off a compact
set; their kernel ratio is bounded. Their amplitude differences are
O(|t|min(|x-y|,1)), giving boundedness on the actual smooth-core form
domain and a dominated derivative. These details still need canonical
write-up and checking.

For a continuous compact BV function the measure quotient
(W_t f-f)dx/t should converge to
X Df+(1/2)X'f dx. A mollified BV variation bound and the inverse-map
distributional change of variables justify this without an L2
generator. It gives each translated-product derivative against the
continuous tests f(.+d)+f(.-d). Equality atoms are zero at every
finite t for these support-preserving maps, unlike an outward dilation.

The continuous first-variation expression simplifies to
R_X(f)=integral X'f^2+integral integral K_X(x,y)f(x)f(y),
K_X=average(X'(x),X'(y)) [kappa(|x-y|)-k(x-y)]
       +(X(x)-X(y)) (d/ds)[kappa(|s|)-k(s)] at s=x-y.
The singular diagonal terms cancel, leaving a bounded kernel on I^2.
This preserves rho via kappa=n+rho, and the pole with its signed term.
For the chosen fixed cutoff field X=x in the bulk, X' is positive
there and negative on an open transition interval. Normalized smooth
oscillatory packets supported in either interval make the bounded
kernel contribution tend to zero and R_X tend to the corresponding
signed average of X'. Packets shorter than log(2) have no prime
overlaps. They are not nullvectors; they refute only a universal
coefficient/form-monotonicity sign, not an eigenvector-specific estimate.

Provisional decision: fixed-interval nonnegativity at the actual
nullvector gives only a two-sided stationarity identity. No independent
upper sign controlling S has emerged; do not take shrinking collars.
The exact prime formula, normalization and diagonal cancellation need
final verification before recording this as completed stop evidence.

Completed: the full calculation, including the diagonal multiplication
term, actual smooth-core admissibility, two-sided variable-flow BV
limit, signed atomic normalization and both-sign packet test, is now
canonical in `lemmas/L524-endpoint-fixed-transport-stationarity-and-sign-test.md`.
The calculation is unaudited. The bounded attempt ends with NEGATIVE
evidence for its universal coefficient-sign implementation, not an
eigenvector counterexample or a new upper bound on S. No shrinking
collars were taken. The provisional notes above are preserved as
working history; the canonical proof supersedes their tentative status.
