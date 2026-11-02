# Positive-cone distance: bounded mathematical attempt, step 38

Invocation-start coverage is the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
The only target is its exact affine nonnegative distance at rate 1/100.
The supplied overview/DAG and the relevant L666/L672 proofs were read;
the L647 and scalar/entrywise-Gram failures were compared. Existing
unfinished work is preserved. No new source theorem is needed so far.

The main gap is actual-Xi all-degree mixed positivity. The intermediate
test is whether nonnegative auxiliary coefficients protect the anchor
in the complete L666 angular family. A bound could apply at b_a=1 to
the existing full-spatial Jensen bridge; that applicability, H, support,
Xi realization and signs remain separate. Continue only on the required
uniform rate, a continuous-norm asymptotic countersequence, or an
intermediate identity with a separately evaluated decisive cost.

## Work in progress

L672 uses the analytic pole-parameter interpolation remainder with
lambda_r=exp(-4*n*i*y_r/3)*P(0)/((-i*y_r)*P'(i*y_r)). Its weights are
not real nonpositive, so it is not yet a cone witness. The attempted
mechanism is a sign-compatible interpolation/positive combination,
paying the angular error on the entire circle. No conjugation or real
part is being assumed to preserve that error.

For the symmetric undisplaced grid, the real Lagrange weights at the
positive nodes h*(k+1/2) alternate in sign. A real exponential gauge
must therefore be checked for exact phase alignment, not just magnitude.
A symmetric cosh multiplier can have the needed alternating signs at
the nodes, but it introduces both real-direction exponential branches;
whether their contour cost meets 1/100 is unresolved. These observations
are provisional until the precise algebra and costs are written out.

A bounded floating cone screen, if used, will retain every product and
the j=0 factor, record its coefficients and residuals on disk, and be
treated only as a diagnostic. It cannot prove a uniform lower bound or
the logarithmic countersequence discriminator.

## Refined mechanism saved before contour work

Let rho=h/10 and c=pi/(n*h)=10*pi/27. For 0<=k<2q define s_k as
the unique solution of

    s_k=k+1/2+atan(1/(10*s_k))/pi.

It lies between k+1/2 and k+5/8. Put y_k=h*s_k and choose the
symmetric allowed outward displacements giving nodes +-i*y_k. Use
g(z)=(1-z/rho)*exp(-c*n*z). At z=i*y_k its phase is exactly
-pi*(k+1), and at the negative node it is the conjugate. The real
Lagrange weights at zero have sign (-1)^k. Thus the auxiliary
interpolation coefficients lambda_k=g(i*y_k)*ell_k are strictly
negative real: b_k=-lambda_k is admissible. This is a candidate exact
coefficient conversion, not an assumption that its error is small.

The essential change is the linear zero and outward shifts; simply
taking real parts of L672's coefficients does not give this construction.
The contour exponent is F(z,u)-(10*pi/27)*Re z+K(z), with only
polynomial extra costs from the linear factor and shifted nodes.
The old 4/3-centered certificate cannot be reused unchanged. A bounded
floating contour design is running; any rate claim needs a complete
enclosure. Optional real even quadratic gauges preserve all nodal
signs, but their entire boundary costs must also be included.

The bounded design tested quadratic gauges and even polynomials through
degree eight. Its best sampled exponent was about -0.00693664, short
of -0.01 and not certified. No claim of optimality follows. The simpler
quadratic -3*z^2/5 on |Re z|<=3/50, |Im z|<=1/2 sampled below
-0.00588. An exact continuous certificate for <=-1/200 is running.
The proposed finite-n cost is at most 14*exp(18)*n^2: the shifted
interpolation product costs less than an additional 3 in its logarithm,
the full rational left sum costs less than 9, the old midpoint product
cost is log n+6, and the linear multiplier is at most 2n. This would
give a relevant positive-coefficient construction but would NOT refute
or prove the required rate 1/100.

Completion: the exact full-contour certificate passed with upper bound
-49171680019/9000000000000<-1/200; all 98,978 sample enclosures and
218 mesh rows were checked. The final safe prefactor is 14*exp(18),
using only pi>3 in the contour-length estimate. The full node/sign,
finite-product and continuous error proofs are canonical in
`lemmas/L673-positive-cone-phase-aligned-interpolation.md`.
The same exact interval method certifies a contour point above -1/100,
so tighter rounding of this unchanged gauge/contour cannot meet that
rate. This is not an obstruction to the cone target itself.

The result is a partial mathematical input, not a complete solution of
the approved test or RH. The floating screens did not establish a global
minimum or an optimal contour. Separate conceptual audit remains needed;
the invocation-start assessment is unchanged and reusable for the same
exact cone target. The preliminary reasoning above is retained as work
history, not a second canonical proof.
