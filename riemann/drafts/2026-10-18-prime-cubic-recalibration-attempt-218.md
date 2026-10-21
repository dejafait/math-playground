# Step 218: fixed-frequency cubic recalibration

Approved target: test a fixed nonnegative trigonometric multiplier of
L421's intermediate mass against both L409/L430 cubic coefficients,
retaining every original L429 tolerance. The prior SPECIALIZE assessment
is `drafts/literature/2026-10-18-prime-cubic-intermediate-recalibration.md`.
Main gap: global mixed positivity. Downstream use: determine whether the
additional cosine cubic still admits a selected-information counterlaw.

Initial checkpoint, before calculation: multiplicativity of A_u should
reduce gamma_2/beta to the prime-2 local sums, with s=v_2(mn),
c=v_2(k), weight (s+1)4^(-s)8^(-c), and A_(2^d)=2^(-d)(1+d/2).
This identity and the exact ratio remain to be verified. A multiplier
F requires circle mean 1 and mean F cos(theta)=gamma_2/beta.
Continue only with a nonnegative fixed polynomial and complete correction
estimates; an obstruction must address all fixed degrees, not one trial.

L421/L429 proofs have been inspected. A bounded multiplier preserves
their rare-mass and full-covariance orders, but w,N_H,m,A_H must all be
redefined and verified. No new law is yet certified. Actual/global
realization, clipping, capped nondegeneracy and L413's full-error margin
remain independent unresolved assumptions. The unchanged-law L430 stop
and L427/L428 narrower stops are preserved; C426c is unused.

## Completed attempt

The one approved test succeeds. Full proof and qualifications are in
[L431](../lemmas/L431-fixed-prime-cubic-recalibration-counterlaw.md).
The exact prime-2 factorization permits a fixed degree-12 Fejer mixture;
the complete mass, mean and covariance correction preserves all original
L429 tolerances and adds the cosine cubic. The rational arithmetic is
recorded in `scripts/discriminant/prime_cubic_recalibration_certificate.json`
and reproduced by its adjacent Python script. The infinite sums and
full-law reasoning are proved in the canonical lemma, not inferred from
the certificate.

Outcome ADVANCE is a local feasibility extension, with classification
POTENTIALLY_NEW only in the recorded source-comparison sense. It is not
certified originality, an independent critical audit or an RH advance.
The new audit proposal is REVIEW_REQUIRED; no second target was tested
or approved here. Mathematical exploration usage remains 0 of 3.
