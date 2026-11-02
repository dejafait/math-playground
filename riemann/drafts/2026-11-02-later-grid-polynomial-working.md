# Later-grid energy with a common multiplicity polynomial

Prepared STEP_ID: 2026-11-02-later-grid-polynomial-01.
One bounded proof_attempt/development under the unchanged ready EXPLORE
assessment `drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Intermediate target: the approved angular operator lower bound at rate
1/32. The present sufficient test is C645y's later-grid energy, starting
at K=ceil(n/2), at squared threshold c^2 exp(-n/16). Such a bound could
supply a synthetic detector; actual-Xi layer isolation, other poles,
census/clearance, simultaneous realization, a matching upper bound and
signs would remain independent gaps.

Retain n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100, t_j=j/n,
common distinct poles Re(a)=x, |a|<=R-eta, x among the poles, positive
integer simple-pole residues r_a, M=sum r_a<=n/3, and the conjugated
denominator angle. Use the same P(z)=product (z-a)^(r_a) for every
rotation. No separation, symmetry or coefficient integrality is assumed.

Read C645y's entire retained-grid proof, C645n's normalization and anchor
rate, C645g's spaces, and C645t's hypotheses and relevant prefix argument.
Checked the associated initial-prefix, angular entrywise-positivity,
inner-input and Hardy-kernel failures. C645x's fractional-pole dual stop
and C645r/w's subfamily bounds are comparisons, not universal inputs.
Scoped searches for later coefficients, degree constraints, Newton
identities and reordered grids found no matching general lower bound.
This is not a novelty claim. Reuse the assessed Fourier/residue sources.

Exact starting point (C645y, separately unaudited):

    ||q_u||_2^2=|B_u(x)|^2 (||L(R*zeta)||_2^2
                             +sum_(j<n) v_j |R_j(u)|^2),
    L=P'/P, v_j=1-t_j^2/U,
    R_j(u)=sum_a r_a/[B_{j,u}(a)*(a-t_j*u)].

The first ceil(n/2) coefficients fail on the admissible C645t family.
They must not be used as a substitute for the remaining sum. The raw
grid data also have the insufficient anchor rate lambda>47/1000.
The attempt will retain the common polynomial and test whether its
degree gives quantitative control of the later complex coefficients.

Continue only with the stated bound, a rigorous informative obstruction,
or a quantitative refinement identifying a materially narrower test.
A small tail alone does not refute the full constant-input or operator
target. Identities alone are not an advance. Save any unfinished
inequalities and their actual constants here before stopping.

## Quantitative refinement reached during the attempt

The attempted degree-M lower bound is still missing. A useful step is
to remove the separate angular-width problem without a derivative bound
that loses an exponential. For j>=1, C_j(u)=B_u(x)R_j(u) has only:
inner angular poles t_k*x/U (1<=k<n), exterior poles a/t_k
(a in Z, 1<=k<=j), and a polynomial part of degree <=n-j-1.
All inner poles have modulus <=80/121; all reflected exterior poles
have modulus <=4/5. A finite rational Hardy basis therefore gives

    |C_j(u)|^2 <= [(201/41)(n-1)+9*m*j+n-j] mean |C_j|^2,
    m=|Z|<=M<=n/3.

The bracket is <=4*n^2. Summing the later coefficient squares gives
max-angle tail amplitude <=2*n times its angular root mean square.
The full constant-input response and largest Hankel norm admit the same
factor, by applying angular point evaluation to each fixed Hardy input
before taking an operator supremum. The operator norm is never treated
as a Hilbert norm. This is a specialization of the finite rational
evaluation mechanism, not a new general Hardy-space theorem.

The completed proof and exact constants are canonical in C645z; it has
not had a separate conceptual audit. The argument keeps the polynomial
part of C_j of degree n-j-1 and both angular pole classes. For the full
operator it fixes a polynomial Hardy input before angular evaluation,
then takes the operator supremum, avoiding an operator-norm Parseval
claim. No numerical script was necessary.

It supplies no large angle itself: a uniform single-angle tail amplitude
c*n*exp(-n/32), or a strict rate gamma<1/32 with polynomial factors,
still needs proof from the common P. A finite directional screen alone
cannot settle that claim. The degree-M lower-bound attempt remains
unfinished; the actual completed input is its explicit polynomial-cost
angular reduction, a reproduction/specialization of finite rational
evaluation rather than progress beyond the sources checked.

## Continuation within the unchanged ready scope

For each allowed common P, seek a rotation u (allowed to depend on P)
with sqrt(T(u))>=c*n*exp(-n/32), or >=c*n^p*exp(-gamma*n) for
fixed gamma<1/32. Use C645y for the exact later coefficients and
C645z to pass to the mean. Retain all integer simple-pole residues and
complex cancellations; do not replace P by independently chosen angular
polynomials. C645t/y still stop the initial half of the grid, and C645x
still stops the proposed universal fractional-pole dual.

Continue only with such a uniform large-angle bound, an admissible
obstruction, or a genuinely sharper quantitative test. The unevaluated
maximum is not itself a second advance. A smaller later tail would only
obstruct this sufficient route, not the full operator target. All Xi
bridges named above remain unresolved. Reuse the same ready assessment;
no new literature target or approval is created in this step.
