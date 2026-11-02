# Angular anchor distance — bounded attempt, step 35

Invocation-start coverage is the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-displaced-angular-anchor-distance.md`.
Its exact TARGET, not a replacement energy or coefficient target, is
being tested. The supplied overview and DAG were read before the
targeted L649/L666 proofs and nearby failure records. Existing work is
preserved. No external source refresh is needed for this attempt.

Main gap: the displaced full-angular bound H>=-n/100-C log n remains
open, as do actual-Xi realization and signs. Intermediate target:
the normalized angular L2 distance of 1 from the complete nonanchor
span, at rate 1/100. If the lower bound holds, its applicability to
the actual unit-residue c_0 and the full-spatial Jensen bridge must be
proved; no inverse Gram estimate or kernel identification is assumed.

Plan saved before lengthy work: retain the exact rational expression
L666 (6), all common interior angular poles, all a-dependent exterior
poles, and the j=0 factor x/a. Test a family-specific separating
functional or, in the opposite direction, approximation in the pole
parameter a. The latter must supply actual complex coefficients and
an asymptotic remainder, not only a finite condition number. A
singular span is allowed. The original residues stay one throughout.

Discriminator: prove delta_e>=exp(-n/100)n^(-C) with absolute C/onset,
or exhibit admissible e and coefficients giving unbounded
(-log delta_e-n/100)/log n. A quantitatively bounded remaining cost
may justify a refined continuation; an unevaluated Gram formula does
not. A countersequence would stop this sufficient separation mechanism
only, not refute H. L646/L650, L647, C645p and L670/L671 retain their
recorded qualifications and stops.

The finite double-precision diagnostic
`scripts/one-sided-hankel/angular-anchor-distance-screen.json` uses
e_r=0 and all columns for n=15,27,51,99,195. The doubled-grid residuals
decrease from about .0903 to 2.34e-6; ranks are full at the numerical
cutoff, and grid disagreements are at most 1.1e-11. This is not a
continuous norm enclosure, an asymptotic bound, or a singularity proof.

Refined analytic test: use the undisplaced nodes a=x+i*h*(r+1/2),
h=27/(10n), and interpolate the parameter function
F(a,u)=exp(-c*n*(a-x))*W_a(u) at these nodes. At a=x its value is 1.
The Lagrange coefficients, multiplied by the unit phase at each node,
are admissible auxiliary coefficients. A contour remainder must retain
all rational factors and bound the complete product
|F(a,u)*P(x)/(P(a)*(a-x))|. A narrow rectangle in the a-plane avoids
the poles a=t_j*u while enclosing the vertical interpolation nodes.
The phase center c may reduce the analytic envelope on both vertical
sides; its full cost must be included. This is unfinished reasoning.

Candidate quantitative reduction, not yet certified: take c=4/3,
the rectangle z=a-x with |Re z|<=9/100, |Im z|<=1/2, and r=9/20.
Write F(z,u)=integral_0^1 log|[(x-tu)/(x+z-tu)]
[(Uu-t(x+z))/(Uu-tx)]| dt and
K(z)=(10/27)integral_(-r)^r [log|t|-log|z-it|] dt.
The floating design suggests F-(4/3)Re z+K<=-.0130 on the boundary.
The bounded test is now a rigorous bound <=-11/1000 there.

Finite-grid costs derived for later checking: the full product obeys
log|W_(x+z)(u)|<=n F(z,u)+9 by a t-derivative bound <17.
For P(z)=product_r(z-i*h*(r+1/2)), h=27/(10n), midpoint monotonicity
and a Lipschitz bound 20 give log|P(0)/P(z)|<=n K(z)+log n+6.
Here r=(2q+1/2)h exactly, and every boundary distance to the real
interpolation ordinate interval is at least 1/20. These estimates
still require checking alongside the final contour certificate.
If the compact bound is verified, Cauchy's interpolation remainder
gives an explicit uniform approximation error <=5 exp(15)n
exp(-11n/1000), which would defeat the proposed 1/100 distance rate.
This would concern auxiliary coefficients only, not the unit-residue H.

Completion: the exact certificate passed, with compact upper bound
-2594211229/225000000000<-11/1000 and all 25358 sample enclosures
covered by the proved second-derivative interpolation errors. The full
proof and all arithmetic qualifications are now canonical in
lemmas/L672-angular-anchor-distance-interpolation-countersequence.md.
The explicit coefficients and uniform remainder prove the admissible
countersequence; the earlier floating screens are not proof inputs.
Outcome NEGATIVE for this sufficient distance mechanism, with a
separate conceptual audit next under the unchanged ready assessment.
The main H and actual-Xi gaps remain open. The initial partial reasoning
above is retained as history, not a competing proof or active task.
