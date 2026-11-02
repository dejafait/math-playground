# Positive-residue Hankel test — working record, 1 November 2026

Approved target and source scope: the unchanged EXPLORE assessment
`drafts/literature/2026-11-01-positive-residue-hankel-exponent-test.md`.
Main gap: actual-Xi signs. The single intermediate target is its
uniform half-grid-exponent norm bound for a small positive-residue
census, with arbitrary pole collisions. A boundary application and a
smaller independent upper bound would remain necessary. No actual-Xi
census, clearance or interpolant realization is assumed.

## Saved before completing the argument

The scalar sum can cancel (C645d); C645e/C645f cover at most three
poles. The parent assessment already checked Nehari/AAK and rational
symbol literature. Its identities alone do not evaluate the required
norm. No further literature turn or mathematical script is needed for
the following concrete test.

Proposed mechanism: write Q(z)=q(z/R), let m=|Z|, and multiply Q by
D(z)=product_(a in Z)(z-a). Then D(R*zeta)q(zeta) is a polynomial.
Its normalized circle L2 norm is at most (2R)^m ||q||_2, and finite
Fourier orthogonality plus Cauchy--Schwarz bounds its interior values.
Because q is strictly anti-analytic, ||q||_2=||H_q 1||_2<=||H_q||.

Choose a small fixed radius scale s near x. Averaging
sum_a log(2R/|r-|a-x||) over s<=r<=2s should give a circle on which
|D(z)|/(2R)^m >= exp[-m(1+log(4R/s))], uniformly in all separations.
The exact grid factors should give
|B_n(z)/B_n(x)| <= exp(4ns) there. The residue of B_n Q at a is
r_a B_n(x), so the local contour integral is B_n(x) times a positive
integer, since it contains x. This avoids assuming positivity of the
weighted residues of q.

Candidate constants to verify: s=delta/64,
C=1+log(4R/s), kappa=delta/(16C),
rho_0=(d+2s)/R<1, c=sqrt(1-rho_0^2)/(2s), N=5.
The proposed bound is ||H_q|| >= c exp(-delta*n/8), which would imply
the required c exp(-Lambda*n/2) using only C645c's audited
Lambda>delta/4 product-rate statement. This is unfinished reasoning
at this checkpoint, not an audited result.

Continuation/abandonment test remains the approved one: establish all
uniform constants and quantifiers, or produce a certified violating
sparse family. Failure of the displayed proof would not itself refute
the target. Check the exact physical/unit-circle scaling, polynomial
degree, radial logarithm integral, nonzero contour residues and all
near-boundary factors before promoting the calculation.

## Completion of this bounded attempt

The proof and all constants are now canonical in
[C645g](../lemmas/C645g-sparse-positive-residue-hankel-bound.md).
The pole-cancelling polynomial sufficed; no new operator theorem,
spectral computation or mathematical script was used. The radial
logarithm integral supplies the separation-free full-census cost, and
the local residue sum uses positivity only after restoring the exact
complex grid multiplier. The result is an unaudited partial advance;
its mathematical target and source assumptions have not changed.

The next invocation can reuse the unchanged ready assessment for a
conceptual audit of this same norm claim. In particular check the
radius-averaging quantifiers, physical/unit-circle normalization,
boundary evaluation factor and coefficient in the census restriction.
The principal-part application, actual-Xi census/clearance/realization,
independent boundary upper bound and signs remain unresolved. No RH
candidate or verified originality is claimed.
