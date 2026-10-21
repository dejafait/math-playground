# Complete quartic response: nested quadratic-flow attempt

Approved target: Determine whether L011's complete quartic probe-jet response kappa_0(f_(i,2),r_0) has a finite a^3-scaled limit for both actual L010 probes.
Reuse the unchanged EXPLORE assessment in
`drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md`.

The main gap remains ultraviolet-uniform interacting reflected comparison,
continuum axioms and infrared finite mass. Within the approved target,
test the entire nested DQ_2(y_s) Z_s contribution to the co-closed
F_(i,4)(z) in L212. A subcubic estimate would remove this complete
flow summand from the coefficient comparison. It would leave C212c's
initial square, Q_3, the other observable jets, dF_(i,3)[b] and
C212b's endpoint limit unresolved. Continue only with full-spectrum
estimates retaining both endpoints and the nonlinear output's gradient
part; abandon estimates requiring rough-tilt smoothness or termwise
forest-to-Hodge transfer, excluded by L022 and ATTEMPTS/010.

Work in progress. Use L011(11), L212's signed covariance tilt and
C212c's exact action split grad S_3=C^T W+V and pointwise input bounds.
Seek full-jet bounds ||Z_s||_(4,2)<=C a^-2 and
||C Z_s||_(4,2)<=C a^-1(s+a^2)^(-1/2), uniformly on [0,tau].
The first retains the gradient part through ||E_t||<=1; only E_t C^T
and C E_t receive derivative heat gains. Contract the smoothed
external leg h_s=H_(tau-s) Q_i H_tau z before estimating the three
placements of d^2 S_3(y_s)[h_s,Z_s]. Its per-row bounds should be
O(a^3), with O(a^4) after circulation, including s=tau by L193's
compact-stencil regularity. Proposed integrated L1 polynomial bound
is O(a^-1 log(e/a)); replacing any input by the actual tilt v=2SAz
costs N, suggesting O(N^2 log(eN)) response, not yet accepted.

All norms refer to ordinary dimensionless full-link coordinates.
The two time integrals, all colors, end rows, action faces, constant
own-direction modes and both insertion subtractions remain. No
independence of correlated fields, separate convergence or full
compensation is assumed. This draft preserves the unfinished power
count pending detailed checks of both time convolutions and every
tilted derivative placement. No scripts are needed for these analytic
inequalities.

Completed: [C212d](../lemmas/C212d-nested-quadratic-flow-response-subcubic.md)
proves both full-jet estimates above and O(N^2 log(eN)) for the
entire selected nested response, hence its zero a^3-scaled limit.
The two dimensionless convolutions are uniformly controlled by
splitting at half the outer time; the undamped V contribution is
kept in the full-jet norm. L193(5)--(7) supplies the needed actual
external-mode bound through s=tau. The exact Hessian has all three
types Ch*y*Z, CZ*y*h and Cy*h*Z; differentiating the outer y, external
h and complete inner Z costs N by positive covariance domination of
the actual tilt direction. No polynomial independence, smooth rough
tilt or nonlinear Hodge-heat replacement is assumed. The response
keeps L212's single-polynomial factor 1/2. This is local reproduction
using existing estimates, without a result beyond checked sources.

Independent power check: the three Hessian types, after the outer
a^-2 and the O(a^-2) square-root row count, have bounds respectively
C a^-1(s+a^2)^-1/2, C a^-1(s+a^2)^-1 and
C a^-1(s+a^2)^-1. Their integrals are O(a^-1 log(e/a)); the
signed derivative adds N. Thus the response is O(N^2 log(eN)),
and its cubic-scaled bound is O(log(eN)/N), below the required
vanishing threshold. This does not shrink C212c's retained square,
evaluate C212b, or bound the Q_3/observable/derivative corrections.

Duplicate/failure check: the exact-notation search in the current
quartic drafts and C212a--c located this nested contribution only as
uncontrolled, while L011 fixes its recurrence. L189 and C212c supply
inputs, not this nested response. L193's established endpoint
regularity is imported, not rederived as a new result. ATTEMPTS/010
and L022 forbid isolated forest transfer, avoided by working within
L212. ATTEMPTS/039--045 remain relevant failures for different prefix
contractions; no factorwise prefix gain is used here. The unfinished
work in those drafts is preserved. No mathematical script was added
or run; verification consists of the analytic complete-endpoint
inequalities in C212d.
