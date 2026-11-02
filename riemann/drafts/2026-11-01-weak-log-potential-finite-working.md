# Finite weak-potential collision — working record

2026-11-01. Approved SPECIALIZE target from
`literature/2026-11-01-weak-log-potential-finite-test.md`; one mathematical
attempt, REPRODUCTION/development. No Xi input or claim of novelty.

Read L487's exact heat polynomial and zero calculation, and reused the
completed weak-potential source comparison and recorded duplicate/stop
checks. Other L487 energy claims are not used. Existing changes remain.

Main gap: actual-Xi all-degree signs at unbounded heights. Target: the
specified common-epsilon weak balance near (lambda,z)=(0,1). A defined
collision term could help test propagation; sign, Xi transfer, tails,
zero time and initial signs remain independent. Continue only with
separately defined limits or a precise obstruction, not a tautological
grouped limit.

Partial calculation saved before singular-limit work:

    H=z^4-(2+12lambda)z^2+1+4lambda+12lambda^2,
    H_lambda=-H_zz, Q=|H|^2+epsilon^2,
    S_epsilon=(1/4)log Q,
    (S_epsilon)_z=H_z conjugate(H)/(4Q),
    (S_epsilon)_zz=H_zz conjugate(H)/(4Q)-4((S_epsilon)_z)^2,
    (S_epsilon)_lambda=-(1/2)Re(H_zz conjugate(H)/Q).

Thus the proposed exact complex-derivative balance has no omitted
epsilon remainder; its real-x form must retain the Laplacian term
epsilon^2 |H_z|^2/Q^2. Need prove all claimed limits rather than infer
them from this cancellation.

Provisional singular-limit route (not yet a proved result): factor the
two roots near 1 and the two remote roots near -1. The local separation
is comparable to sqrt(|lambda|); pair kernels have spatial L1 norm
O(1+|log|lambda||), hence an integrable real-time majorant. Diagonal
squared Cauchy kernels require a circular finite part. At lambda=0
the scalar regularization should give that finite part without an
extra delta. One-sided time limits may differ because the pair splits
along real versus imaginary directions. Verify the coefficient via
the distributional identity partial_barz(1/z)=pi delta_0. A spacetime
atom, a fixed-slice divisor mass and a one-sided trace defect are
different assertions. Full estimates and source normalization pending.

Singular-limit development saved before canonical write-up:
with K(w)=1/w, partial_z K=-Pf(1/w^2) and
partial_barz K=pi delta_0. The local pair has roots c+-a, where c is
real analytic, c(0)=1 and a^2=2lambda(1+3lambda)/c^2. Thus

    1/((z-c)^2-a^2) -> Pf(1/(z-1)^2)-pi sign(lambda) delta_1

as a one-sided time trace, by the translated-Cauchy-kernel difference
quotient. This is not the fixed-lambda=0 epsilon limit. The proposed
traces are T_0+-pi delta_1 for T=partial_lambda S, and
B_0-+(pi/8)delta_1 for B=lim((S_epsilon)_z)^2. The spacetime limit
has no delta(lambda): diagonal finite parts have uniformly bounded
test pairings and pair kernels have the integrable logarithmic bound.
The real-x balance retains (1/2)Delta S, the usual divisor measure;
it is supported on all zero paths and is not collision exclusion.
Canonical proof in preparation; these notes do not substitute for it.

Completion: the full proof and exact qualifications are now canonical
in `lemmas/L616-quartic-weak-potential-collision-traces.md`. The
spacetime limits and distinct one-sided/slice limits were established
as a finite specialization, pending independent conceptual audit.
The extra first-order event-atom inference is parked; no coercive or
actual-Xi conclusion follows. These preliminary notes are retained as
unfinished-work history, not a second proof or current checkpoint.
