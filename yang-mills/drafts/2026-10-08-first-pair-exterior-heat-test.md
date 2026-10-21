# Actual exterior/axial heat diagnostic: bounded test

STEP_ID: YM-20261008-090-first-pair-exterior-heat-test

The unchanged SPECIALIZE assessment `literature/2026-09-26-current-target.md`
covers the complete response target. This step tests an intermediate
signed exterior contraction suggested by L070, before attempting a
pinned-trace expansion. Known bulk flow and matching results in that
assessment are reused; they do not compute this contraction. L062/L064,
L066–L070 and ATTEMPTS/019–022 have been checked for duplicates and
failed shortcuts. Neither automatic angular cancellation nor the generic
residual norm is a valid closure mechanism.

Unfinished setup: define a finite mesh diagnostic using the actual
Hodge covariance, heat operator, both Q_i, upper curvature rows, and
right straight-forest lift. The frozen mean in L070 pairs an upper
curvature vector with a transverse lifted vector, multiplied by u_1
and the axial level. Center these vectors on transverse vertices;
retain every level 1<=s<N, including end edges. This centering is a
specified diagnostic, not a proved principal coefficient of L070(1).
Evaluate its full-spectrum heat contraction with reproducible randomized
trace samples; store every sample and checks. Sampling estimates cannot
prove a nonzero value or an asymptotic. Continue toward a deterministic
or symmetry test only if there is an informative signal; otherwise
reassess the diagnostic rather than interpreting noisy zero as cancellation.

Essential inputs: L008, L018, L026, L028, L062, L064, L066–L070.
Outstanding assumptions: the centered contraction need not agree with
the staggered principal trace; axial embedding factors, variable
coefficients, four-dimensional covariance and pinned-boundary remainder
have no established asymptotic reduction. Other monomials and all
remaining response jets stay open. No full logarithm, matching,
reflected-error <=c_box/2, continuum field or mass-gap result is claimed.

Completed test: L070 section 6 now holds the exact definition (9),
finite trace representation (10), sampling identity (11), normalization
qualifications and full verification details. The script and full
certificate are in `scripts/combined-ward-response/`. All retained
samples and dense-check records were inspected; means and sample
standard errors were independently recomputed from every stored sample.
The three dense checks pass, but none is an interval/sign certificate.

For N=24,32 the triplet means/sample SE are -180.3972/60.5287 and
-271.1691/69.5446. The shear means/sample SE are -24.5679/57.8138
and 99.3451/100.6373. These are noisy diagnostic estimates, not
mathematical signs or coefficients. Outcome EXPLORATION / RESEARCH /
REPRODUCTION; mathematical exploration usage is 1 of 3. The main
argument in PROOF.md is unchanged; only L070's local diagnostic and
its direct inputs were extended.

The next bounded test is the x_2<->x_4 symmetry of diagnostic (9),
with the actual u_1, Sigma, heat, upper curvature and forest lift held
in their defined order. Determine whether it kills the Psi_24 part
of each Q_i. Continue to deterministic Psi_13 evaluation only after
exact equivariance is proved; failure abandons this symmetry shortcut.
No new assessment or newly ready target is asserted: this remains a
bounded intermediate calculation under the unchanged approved complete
response target. Essential inputs and unresolved reduction assumptions
are recorded above and in PROGRESS.md. The numerical signal alone
does not justify a pinned-trace expansion or a nonzero leading power.
