# Averaged finite prime remainder — bounded attempt

Started 2026-10-30 under the unchanged EXPLORE gate
`drafts/literature/2026-10-30-weil-averaged-prime-remainder-coverage.md`.
The supplied startup overview, DAG and assessment were read. Existing
notebook changes and unfinished work are preserved.

Main gap: actual-Xi all-degree positivity. Intermediate target: L516 (6)
with one K on the specified positive simple eigenbranch as lambda tends
to zero at finite A. Its possible use is the eigenvalue-relative trace
bound; the imported realization, collar/support law, multiple branches
and Xi transfer remain separate unresolved inputs.

Use L516's exact finite sum with N=floor(exp(2A)), all prime powers and
equality atoms retained, and 0<epsilon<h<log(A/a). Apply Molteni revision
9.0 Proposition 1.3 only to finite sequence values. First investigate
the signed increments, then the complete-sum epsilon limit; no
individual improper average, H1 bound, monotonicity, uniform dilation
rate or uniform spectral gap is assumed. The pole and H term stay in
the required comparison P-H+K lambda.

Continuation test: produce a signed estimate at this threshold or a
precise narrower arithmetic input. Park this implementation if only an
absolute estimate, an unverified sign or a reformulation remains. A
generic-vector obstruction would concern the proposed estimate only;
it would not disprove the exact eigenbranch inequality or RH.

Local checks: L516's complete proof and audit read; nearby Weil draft
and ATTEMPTS searches show the scalar-shift, automatic-support,
withdrawn-Pohozaev and rank-trace stops, with their original scopes.
No new source review is needed for the approved finite-sum test.

Work in progress: isolate the exact finite Abel coefficients without
discarding signed terms or differentiating rough translations. No
mathematical conclusion or new lemma is asserted at this checkpoint.

## Partial calculation saved before completing the proof

For 0<epsilon<h, average each finite-r quotient into F_n(epsilon,h).
With W(j)=sum_(n<=j) Lambda(n)/sqrt(n), finite Abel gives exactly
W(N)F_N-sum_(n<N)W(n)(F_(n+1)-F_n). For an actual eigenvector, only
this complete combination is passed to epsilon=0, using L516's
aggregate convergence. No individual improper integral is needed.

For a smooth compact test f, the complete limit instead equals
-2 sum w_n log(n) C_f'(log(n)), C_f(s)=integral f(x)f(x+s)dx.
This differentiation is restricted to smooth tests. Candidate
obstruction: put ell=log(2), choose two narrow identical packets at
plus/minus ell/2, and modulate their sum by cos(kx), with
k ell=2pi j plus/minus pi/2. The packets can be chosen so every
shift log(n), n>=3, has disjoint supports. Direct calculation gives
norm squared exactly one and C_f'(ell)=-k sin(k ell)/2. Thus the
signed limit is plus/minus (log(2))^2 k/sqrt(2).

To test an energy-only closure, add k^(-1/4) times this packet test
to a fixed normalized smooth seed and renormalize. Its logarithmic
energy perturbation tends to zero because the packet form norm is
O(sqrt(log k)); the signed prime cross terms should decay by repeated
integration by parts, leaving a remainder of order plus/minus sqrt(k).
The complete proof, especially normalization, finite averaging limits
and low-positive-energy qualification, is still being checked. These
are not eigenvectors; no failure of the exact eigenbranch bound follows.

## Completed bounded attempt

Canonical statement and complete proof are in
[L517](../lemmas/L517-averaged-prime-abel-energy-obstruction.md).
The proper finite Abel transform and the complete aggregate limit are
justified. The smooth packet calculation is exact; its small
perturbations converge in logarithmic form norm and L-infinity while
the signed prime remainder diverges with either sign. In any existing
open positive Rayleigh-energy band this disproves a bound by form
energy alone. This is informative NEGATIVE evidence for the tested
implementation, not a counterexample on the actual eigenbranch.

The full eigen-equation, not merely its Rayleigh quotient, would need
to supply a new signed input. No such input was found in this one
attempt. Park this implementation. A different proposed next target
is adjoint cancellation in the signed renewal trace formula at a
simple nullvector; its coverage is REVIEW_REQUIRED and no mathematics
on that target was attempted here. L517 remains separately unaudited.
