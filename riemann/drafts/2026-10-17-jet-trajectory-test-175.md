# Step 175: approved finite-interval trajectory diagnostic

Initial working checkpoint (preserved). RESEARCH / REPRODUCTION / proof_attempt
under `drafts/literature/2026-10-17-jet-trajectory-compatibility.md`.
The main gap is global mixed positivity; actual clipping and the full
regulator margin remain independent gaps. The sole target is that
assessment's Gaussian-damped quadratic transport test. A nonvanishing
defect against the full vanishing endpoint/scaling budget would restrict
L423's realization by ordinary jets; failure to separate stops this test
without realizing the law or changing its selected-moment obstruction.

Read L423's full construction and its step-172 audit, L421's component
definitions and correction, L419's exact forms, weight and Borel six-state
algorithm, and L405's ordinary jet convention. Reuse the supplied primary
source assessment; no further source search is needed. L420's magnitude
stop and the earlier uncut quadratic comparison do not decide this
nonlinear test. Existing work is preserved.

Let ell=log H and a=x/sqrt(ell), b=y/sqrt(ell), d=z/sqrt(ell).
Ordinary differentiation gives x'=L y and y'=L z-(L'/L)y.
For g=psi(a,b)/L, its exact trajectory derivative is

    d g/dt = b psi_a+d psi_b-(L'/L^2)(psi+b psi_b).

The next calculation must retain both endpoints, bound the final term,
and compare this expression on the entire law. No defect has yet been
established. In particular the Borel basis must not be replaced by an
unjustified continuous limiting basis at its branch transitions.

Completed: the full proof and precise source citations are canonical in
`lemmas/L424-gaussian-jet-transport-reduction.md`. Both sharp endpoints
and the moving normalization have an explicit O(1/(H log H)) budget.
The complete law reduces to the exact six-state bulk integral, with
controlled high, intermediate and translation errors. This remaining
integral is not certified. The numerical screen is ancillary and records
all three unresolved verification obligations; it is not an input to
the proof. Outcome EXPLORATION, one mathematical exploration turn used.
The diagnostic stops without rejection or realization of L423. Separate
audit coverage is proposed in the current checkpoint, not approved here.
