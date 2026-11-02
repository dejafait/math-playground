# Peano dual / chirp derivative calculation: checkpoint

Gate: the invocation-start EXPLORE assessment
`drafts/literature/2026-10-31-density-peano-dual-chirp-pairing.md`,
exact COVERED_TARGET. One RESEARCH / REPRODUCTION calculation.

Main gap: actual-Xi all-degree positivity. Intermediate target: the
complete chirp leakage for the specified Peano-smoothed L574 dual.
Downstream use: with leakage at most c T(log T)^3/2, its positive
ratio pairing would obstruct L477's little-o fixed-square defect.
Neither the leakage nor any Xi sign is assumed.

Essential inputs read: L477, C481a, audited L574; L316's analytic
remainder was checked for phase uniformity. Existing changes to the
notebook are preserved. No new source search or mathematical script.

Reasoning being completed: compact Fubini gives exactly
integral U_T psi_T = h^(-2) integral_J D_h^2/Q_T >= c T L^3.
The convolution gives |psi_T|<=1, zero endpoint values, and a global
C^1 weight with variation at most 2|J|/h. Off-diagonal chirp phases
have f'>=log(M^2/(nm))/2 and f''>0; zero diagonal coefficients must
be removed before dividing by that logarithm. A finite integration
by parts retains the amplitude-derivative cost and all phase curvature.
The aggregate budget uses the complete sums of log(M/n)^j/sqrt(n),
j=0,1,2. No stationary case is to be discarded.

Completed: the canonical proof is
`lemmas/C574a-peano-dual-chirp-derivative-budget.md`. The exact pairing
passes. The complete direct derivative budget is at most
32 M(2L|J|+1); the trivial coefficient bound is 64 T M. Both guaranteed
budgets divided by the required (c/2)T L^3 diverge. L477's stronger
O(T L^3) bound is preserved, with no certified small constant. This
implementation is parked; the actual leakage is not proved large.
No script or numerical preview was used as proof.

The independent continuation is only an uncovered source nomination
for a bounded sine of the prime-block probe. Its changed amplitude and
finite arithmetic expansion require separate literature coverage;
no new-target estimate has been derived or approved in this turn.
