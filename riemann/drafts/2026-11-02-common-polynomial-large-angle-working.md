# Common-polynomial large-angle test

Prepared STEP_ID: 2026-11-02-common-polynomial-large-angle-01.
One bounded RESEARCH proof_attempt/development under the unchanged ready
EXPLORE assessment `drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Target: the approved angular root-mean-square largest Hankel norm at
rate 1/32. The intermediate sufficient test is one rotation with full
symbol or later-grid amplitude at least c*n*exp(-n/32), or with a strict
rate margin below 1/32. C645z transfers this to the angular mean with
loss at most 2n. A positive result would provide a synthetic detector;
Xi layer isolation, other-pole control, census/clearance, simultaneous
realization, a matching upper bound and signs remain independent gaps.

Retain n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, common distinct poles
Re(a)=x, |a|<=R-eta, x in Z, positive integer simple-pole residues,
M=sum r_a<=n/3, and the conjugated denominator angle. The same
P(z)=product_a(z-a)^(r_a), of degree M, is used at every rotation.
No separation, ordinate symmetry or coefficient integrality is assumed.

Inputs read: C645g's normalized spaces and rational symbol; C645y's
complete retained-grid identity and prefix stop; C645z's full angular
evaluation proof. The associated prefix, zero-continuation and
fractional-lattice failure records were checked. The ready source
assessment supplies the standard finite Fourier/residue machinery.
No independent audit of C645y/z is claimed by using their reductions.

The calculation will retain the full grid and the degree-M polynomial.
In particular, the line condition makes P(x+i*y)/i^M a real-rooted
monic polynomial in y, even without symmetry. This observation alone
does not bound complex cancellation in any grid coefficient.

Continue only with a uniform large-angle lower bound, an admissible
full-mean countersequence, an informative obstruction to the specific
test, or a genuinely sharper quantitative continuation. An unevaluated
maximum, a finite screen, or a small sufficient tail is not a resolution.
Record unfinished inequalities and actual versus required rates below.

## Specific test and provisional obstruction

Instead of omitting later coefficients, keep the full symbol and replace
the full inner input B_u(R*zeta) by its minimum-H2-norm interpolant at
the distinct pole locations alpha_a=a/R. If C is their finite spatial
Blaschke product, this input is E_u=P_(H2 minus C H2) B_u(R*zeta).
Its complete output is B_u(x)*L(R*zeta). The hoped-for gain is a small
norm of E_u; this uses all the common polynomial's distinct roots.

An apparent obstruction is the admissible cluster m=floor(n/3),
a_j=x+i*j*exp(-n^2), 0<=j<m, residues one. In the confluent limit
C=b_alpha^m, alpha=-10/11, a unitary disk change of variables converts
E_u to the first m Taylor coefficients of
F_u(w)=sqrt(1-alpha^2)/(1+alpha*w)*B_u(R*(w+alpha)/(1+alpha*w)).
Near w=-1 the inner phase derivative per grid factor is at most
(19/63)*(100/99)^2<5/16. Since m is near n/3, a fixed smooth arc cutoff
has vanishing Fourier energy at indices >=m by one integration by parts.
Its positive overlap with F_u would force ||E_u|| uniformly away from
zero for every rotation. Projection continuity then transfers this to
the distinct cluster above. Combined with C645n's pointwise
|B_u(x)|<=exp(-lambda*n), lambda>47/1000, the normalized input remains
too weak at exponent 1/32. This is a proposed method obstruction, not
an operator countersequence. Full constants and limiting steps are
being checked before a canonical claim is recorded.

## Completed bounded attempt

The obstruction and every load-bearing estimate are now canonical in
L646. Its full proof includes the unitary's kernel factor and direction,
one uniform integration-by-parts Fourier-tail bound, a boundary-norm
projection perturbation to distinct poles, and the actual large full
response. The exact-recovery input is optimized over all H2 interpolants;
its failure is stronger than failure of the original full inner input.
It remains a method obstruction, separately unaudited, not a refutation
of the approved arbitrary-family bound. No large-angle lower bound for
general common P or C645y's later grid energy was obtained.

The 31 rational checks in
`scripts/one-sided-hankel/minimum-interpolant-cluster-check.json` pass;
their complete selected values were inspected. They check constants,
not the uniform analytic proof independently. The rate remains
lambda>47/1000, whereas the required rate is 1/32. The large explicit
onset is sufficient for the method stop and is not an RH height bound.

Route decision: stop this minimum exact-recovery interpolation test.
The next bounded test of the unchanged approved target should critically
check L646's uniform obstruction before using it to rule out further
normalizations. Essential inputs are C645g and C645n; C645y/z remain
the separate later-grid continuation. Preserve all prior unfinished
common-polynomial reasoning. No new assessment is needed for a check
of this same Fourier/residue mechanism within the unchanged ready scope.
