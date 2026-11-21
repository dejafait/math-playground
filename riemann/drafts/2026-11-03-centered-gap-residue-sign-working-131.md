# Actual centered-gap residue sign test — step 131

Invocation target: Assess whether some fixed reflection-symmetric centered-gap profile selected by L699 has nonzero scalar residues rho_(j,n) of one common sign for every 1<=j<n on an unbounded sequence n=12q+3.

The prior EXPLORE assessment is
`literature/2026-11-03-centered-gap-real-residue-sign.md`, supplied in
full at invocation. This is one mathematical attempt, reusing that
coverage. Main gap: actual-Xi all-degree mixed positivity. The potential
use is L699's conditional scalar-log lower bound and its integrated
full-spatial comparison; H/support and realization remain independent.

Fix the complete L694/L696 Picard choices and g>0 before n. Keep real
l1 shifts, cap 1/8, reflection, unit masses, anchor, j=0, denominator
angle 1/u, exact -2q<=m<2q and every M moment. The step-127 finite
profile is not an input. L699 is unaudited. Its exact residue formula,
not its unproved strict-sign hypothesis, is the starting point.

Bounded test: first resolve j=1,2 asymptotically, seeking an eventual
opposite-sign witness. Failure for one fixed profile rejects only that
choice; positive success still requires every interior residue on an
unbounded sequence for one fixed profile. If this endpoint test gives
no such certificate, retain the calculation and reassess the mechanism;
this is the third mathematical compensation exploration unless a real
advance or informative negative changes the decision.

Existing stops checked: step-127 finite-screen asymptotics, step-129
unpaid scalar charge, and the supplied source review's preservation of
L695/step-115. The inspected Pick-cluster and nonuniform-lattice source
comparisons concern other residue normalizations. No duplicate actual
sign result was found in those scoped inputs. No novelty is inferred.

## Initial algebra and uncertainty

For a=x+i*y let w=x/a=(1-i*y/d)^(-1). At p_j=x*j/(U*n),
direct factorization of L699 (7) gives

    (x/a)*C_a(p_j)/A_a(p_j)
      =[(n-1)!/n^(n-1)] * w
        * product_(k=1)^(n-1) (1-j*w/k)/(1-j*k*w/(U*n^2)).

The scalar outside this expression and L699's prefactor are nonzero;
the latter has sign (-1)^(j-1). Fixed j therefore probes an endpoint
sum of analytic products, not automatically a positive kernel.
In particular w has an imaginary part for every nonanchor node. A
prospective large-n analysis must retain oscillation in log n and
cannot infer signs from absolute values. This note saves the algebra
before further work; no sign assertion has yet been obtained.

Prospective endpoint calculation: set Y=9/20, w_*=(625+225*i)/706,
alpha=625/706 and beta=225/706. For fixed j, the normalized product
appears to have the uniform form n^(-j*w) times a nonzero analytic
factor away from the integer zeros. Riemann summation and integration
by parts at +/-Y would then give a leading oscillation with frequency
j*beta*log n. The l1 perturbation has mesh size O(1/n), so its error
should be smaller than this boundary term. This must be proved with
absolute, rather than relative, product errors at w=1. If j=1,2 have
compatible sign windows, a finite set of fixed j may still give an
incompatible-sign test for every phase; that remains the same actual
residue condition, not a changed scalar-log target.

The bounded extension (J<=64, one diagnostic) finds first sampled
incompatibility at J=33, margin about 0.0594, and a margin about 0.963
at J=64. These remain uncertified. Save them in
`scripts/one-sided-hankel/centered-gap-residue-sign-131.json` with their
failure list. No finite Picard coefficients were sampled.

Proposed rigorous transfer, still to be written canonically: define
E(z)=lim_(K->infinity) K^z product_(k=1)^K(1-z/k). Local uniform
convergence follows by subtracting the harmonic sum and bounding the
quadratic log tail. Then the normalized residue sum has leading form

    [2*n^(1-j*alpha)/(A*log n)]
       Re[B_j*exp(-i*j*beta*log n)],
    B_j=i*d*E(j*w_*)*exp(j*w_*/(2*U))/(j*w_*).

At w=1 use absolute analytic errors, because E(j)=0. Midpoint
Riemann error is O(log n*n^(-j*alpha)); the exact l1 shift correction
is at most O(E*log n*n^(-j*alpha-1)). Integration by parts has zero
lower endpoint since E(j)=0; the outer endpoint remainder is
O(n^(1-j*alpha)/(log n)^2). Thus every fixed j has an o(1) normalized
error. All these estimates require complete justification before use.

For phase certification choose K=32768 and j<=64. The logarithmic
tail bound can be taken as

    delta_j=j/K+j^2/[2*K*(1-j/(K+1))].

It bounds the phase difference between E(j*w_*) and the finite Euler
product times K^(j*w_*). Exact interval arithmetic on that finite
product and a 2048-point phase grid, with Lipschitz cost 64*pi/2048,
should certify both signs at every phase. This is one continuation of
the same finite-endpoint attempt, not a second target. No mathematical
conclusion is claimed in this checkpoint note until both parts finish.

## Completed attempt

The full proof is now canonical in
[L700](../lemmas/L700-centered-gap-eventual-mixed-residue-obstruction.md).
Both the endpoint estimate and the exact interval phase calculation
finished. The paid phase margin is >0.8038 against the required >0.5,
with all 2048 cells checked and no certificate failures. An initial
range-reduction assertion caught a factor-of-two implementation error;
the corrected run passed. The original floating diagnostic remains
nonrigorous and retains its own failure list.

L700 yields a qualified NEGATIVE: the strict common-sign condition
fails eventually for every fixed selected profile, not merely one
choice or finitely many n. It remains unaudited, and the scalar rate,
full-spatial compensation, H/support and Xi transfer remain open.
The prior two mathematical exploration turns are preserved in history;
this informative negative ends that streak rather than recording a
third inconclusive test. The only nominated continuation is a separate
conceptual audit under `literature/2026-11-03-centered-gap-mixed-residue-audit.md`,
currently REVIEW_REQUIRED. No same-turn approval of that new scope occurs.
