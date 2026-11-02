# Angular Hardy-kernel test — working record

Prepared STEP_ID: 2026-11-02-angular-hardy-kernel-01.
Invocation-start coverage is the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
This is one bounded mathematical attempt on that exact angular target.

Main gap: actual-Xi mixed positivity and unbounded-height signs.
Intermediate target: on C645t's odd m>=5, n=3m, r=27/50, unit-residue
Chebyshev family, test the full response to
`k_w(zeta)=sqrt(1-|w|^2)/(1-conjugate(w)*zeta)`, |w|=1-1/n,
with its argument allowed to depend on the grid angle. A lower bound
`c exp(-n/32)` could supply a detector input; a rigorous smaller upper
bound would stop this input on this family. The general common-pole
bound, other poles, census/clearance, simultaneous realization, an
independent matching upper bound, and actual-Xi signs remain open.

Inputs inspected: C645g normalization; C645n analytic-input projection;
C645l Chebyshev contours; audited C645t's radius and input obstruction;
C645q's complete signed spatial energy. The related saved failures
do not test these kernels. Reuse the assessed Fourier and residue
sources; no fresh source approval or novelty claim is made.

For alpha_a=a/R and c_a=r_a B_u(x)/(R B_u(a)), the exact response is
`sqrt(1-s^2) sum_a c_a/[(1-s exp(-i psi) alpha_a)(zeta-alpha_a)]`,
where s=1-1/n. The kernel is analytic near the closed disk for finite n,
so C645n's projection identity applies. The output square must retain
every cross term. All poles obey |alpha_a|<=273/275<1.

Continue only after controlling the whole response and its angular
mean at the asymptotic threshold, or after finding a justified refined
mechanism. A finite sample or selected small response settles neither
the optimized-kernel target nor the operator target. If the attempt
is inconclusive, save the exact unresolved inequality and route for
reassessment; do not claim an advance merely for another representation.

## Completed bounded attempt

[C645u](../lemmas/C645u-hardy-kernel-full-symbol-rate-comparison.md)
contains the full proof and precise source reuse. If Q_n is the angular
root mean square of the complete symbol (the constant-input response),
then

    sqrt(2n-1)/n * Q_n <= T_n <= sqrt(2n-1)*Q_n.

The kernel-angle average also has an exact nonnegative spatial-series
formula. These standard Fourier specializations retain all signed pole
terms and prove only a polynomial comparison. Optimizing the nominated
kernel cannot change Q_n's exponential rate; Q_n's rate on r=27/50
remains unevaluated. This is EXPLORATION, not a new angular bound or an
informative asymptotic negative. There is no upper bound for A_n.

The diagnostic `scripts/one-sided-hankel/angular-hardy-kernel-screen.py`
and its JSON retain n=51,99,195,387, 128 grid angles, 64 kernel angles,
and 512 spatial modes. Apparent kernel root rates were approximately
-0.03646, -0.01683, -0.01167 and -0.00916, compared with 1/32.
These are finite sampled values, not certified exponential rates.
At n=387 the sampled winning grid argument was 13*pi/16; its complete
spatial response was approximated by the saved 512 coefficients, with
the largest squared coefficient at index zero. The symmetric direction
also merits the same interpretation. The negative real grid itself
had a much smaller response. None of these observations certifies an
angular integral, a tail, an optimized kernel norm or an asymptotic.

The initial run failed because mpmath was absent. The retained script
now records the optional 90-digit finite-Gram checks as NOT RUN when
that module is unavailable; there was no package installation. The
complete `/failures` and the selected `/records/3/maximum` and
`/records/3/negative_ray` values were inspected with the shared JSON
inspector. No interval arithmetic or high-precision validation was
completed, and none enters C645u's proof.

## Concrete continuation within unchanged ready scope

The rate question is still

    T_n >= c exp(-n/32), or T_n=o(exp(-n/32)),

along this fixed admissible Chebyshev family. C645u transfers any
strict exponential margin for Q_n to T_n. Repeating a kernel-angle
optimization would not address the missing estimate. Instead test
the signed finite-node contribution in the new oblique negative-grid
sector |arg(u)-13*pi/16|<=10^(-6). This is distinct from C645r's
positive-ray endpoint band and C645s's pi/6 two-coefficient stop.

For the proposed test define, without asserting any asymptotic,

    F_n(t,u)=B_u(x)/B_u(x+i*(27/50)*cos(t)),
    b_l(u)=(1/(2*pi))*integral_0^(2*pi) F_n(t,u)*exp(-i*l*t) dt.

Use C645l's exact finite-node formula (23) to test first-alias
domination. Seek constants c>0, A>=0 and gamma<1/32, uniform on
that fixed sector, such that

    |b_0-2*b_(2m)| - 2*sum_(h>=2)|b_(2mh)|
          >= c*n^(-A)*exp(-gamma*n).

This is a proposed sufficient inequality, not an established estimate
or a claim that the first alias dominates. The branch geometry,
all signed contributions, full higher-alias remainder and angular
uniformity must be justified. A positive exponential margin would
give a constant-input lower bound with polynomial losses, then the
kernel and operator lower bounds for this subfamily. If a different
alias dominates or the remainder cannot be controlled, preserve that
evidence and reassess instead of repeating the finite screen. General
pole families and every actual-Xi bridge remain separate gaps.

The ready parent assessment already covers angular Fourier/coefficient
and residue tests of this unchanged family. No new assessment is
written or approved. C645l, C645g, C645n, C645t's admissibility and
C645u are the exact local continuation inputs; the old failure
records are retained. PROOF.md is unchanged because its assembly and
unresolved angular gap have not changed.
