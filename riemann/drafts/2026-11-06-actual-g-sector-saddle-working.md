# Fixed-collar actual-G saddle attempt, 2026-11-06

Approved target and source scope are the unchanged
`literature/2026-11-06-actual-g-sector-collective-saddle.md`.
The main gap remains L030–L032/C032a actual-Xi mixed positivity.
This attempt tests only the specified nonzero stationary configuration
in the closed angular collar, without a contour or sign assumption.

Initial reasoning checkpoint: put z_j=R_k exp(i zeta_j) and
A(z)=z G'(z)/G(z). At a nonzero stationary point the proposed equations
are A(z_j)-k+sum_(l!=j)(z_j+z_l)/(z_j-z_l)=0.
Multiplication by z_j and summation should give
sum_j z_j A(z_j)+(r-1-k)sum_j z_j=0. On k=r-1 this would force
sum_j z_j A(z_j)=0. Every algebraic sign and the angular-coordinate
interpretation still require checking.

Discriminating estimate: show Re(z A(z))>0 uniformly when
|arg z|<=1/2 and R_k/e<=|z|<=e R_k, for all sufficiently large k.
L775 gives R_k tending to infinity and the exact actual-G interface.
The completion formula and sectorial Stirling suggest
A(z)=(sqrt(z)/8) log(sqrt(z)/(4 pi))+O(1), with an analytic,
uniform error. This is a tentative formula, not yet a proved input;
in particular it must not be obtained by differentiating a real-axis
O-term. Nonzero G, collisions, both collar boundaries and the precise
derivative remainder remain to be verified.

Success would exclude this collar's stationary points before any
Hessian test. It would stop only this collar mechanism; participation
of other saddles, summed phases, uniform remainder, other coefficient
shifts and actual-Xi signs remain independent gaps. If the positivity
estimate fails, preserve the exact equations and unpaid inequality;
do not replace G or the sine Vandermonde.

Completed attempt: L844 now contains the full proof, source
specializations and qualifications. The tentative identity and
logarithmic-derivative formula above were established. Their combination
excludes every nonzero stationary point in the closed collar for every
sufficiently large r, so the Hessian requirement is unreachable there.
The result is unaudited; this working checkpoint is retained as the
record of the initial reasoning, not a second canonical proof.
