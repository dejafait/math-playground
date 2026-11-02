# Vertical Pick concentration — bounded mathematical working note

Invocation-start gate: `literature/2026-11-01-vertical-pick-zero-count-concentration.md`, EXPLORE, exact unchanged target. This is one research attempt, not a fresh source review. Existing L640 arithmetic reductions and their two inconclusive attempts are preserved.

Main gap: actual-Xi initial signs at unbounded heights and all-degree mixed positivity. Intermediate target: a unit vector with normalized full K-Rayleigh quotient tending to zero. This would obstruct every eventual fixed relative norm reserve below one; it would not imply a negative eigenvalue or RH. Independent arbitrary-node and boundary-transfer gaps remain.

Inputs read: L018, L467 (including its audit), L640 definitions/full-Gram proof and relevant previous stop records. Reuse the inspected Suzuki (2.6), rational model-space and finite spectral source coverage in the saved gate. No cross-notebook input. L640's separate audit is still open; this attempt will use only its definitions and independently check the Gram identity needed here.

Provisional calculation, not yet a result: with a=3/2, y_j=X+j/N, let g(z)=sum_j conjugate(c_j)/(a+i(y_j-z)). Its boundary norm (1/(2pi)) integral |g(u)|^2 du equals c* C c. The anticipated zero-pair form is c* K c=sum_z g(z) conjugate(g(conjugate(z))), over all Xi zeros with multiplicity. Check the reflection sign, cancellation of compensators and absolute convergence before using it.

Discriminating test: quantify a concentration dimension surplus over all local zero constraints and the entire complex/exterior remainder. A boundary-only surplus does not pass. Test explicit rational numerators before invoking any unproved triangular-array concentration theorem. If no controlled witness or informative obstruction results, this is the third mathematical EXPLORATION on the diagnostic and must lead to a materially different target, not another reduction.

Completed bounded attempt: the canonical proof is now L641. It verifies the zero-pair identity, gives a direct finite-grid concentration trace/variance estimate, and averages the all-zero count to obtain a local interpolation nullspace of dimension at least kappa N-O(sqrt(N) log N), kappa=(arctan(1/3)+pi/4-1)/pi>0. The boundary leakage there is at most N^(-1/2).

The tested generic exterior transfer fails: in the exact rational family, L641 constructs unit vectors with leakage O(sqrt(m)(9/10)^m), m=floor(sqrt(N)), but signed energy of either sign at the admissible exterior pair 2+/-i/4 of magnitude at least (2/3)(36/149)^m(149/125)^((N-m)/2). The inner-factor cancellation is included; cross terms produce the growth. This is a test pair, not an asserted actual zero, and these countervectors are not shown to lie in the actual-zero interpolation nullspace.

Unfinished: the full exterior sum on that actual interpolation nullspace. Neither a generic boundary transfer nor dimension alone settles it. Park that transfer; nominate a separately reviewed, constraint-sensitive signed-trace test. No actual-Xi Rayleigh witness or RH conclusion. Full mathematical details belong only in L641; this note preserves the attempt's reasoning boundary.
