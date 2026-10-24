# Fixed residual-corrected mode-one estimate — inconclusive and parked

WHY IT FAILS: With z=C^T*w fixed from L112's saved preconditioner, the
full original-box derivative defect gives a centered enclosure of
(lambda_1(K(x*))+R0)/R0 strictly straddling zero. Its outward grid bounds
are [-8460928885,8462190625]/10^6, against required lower endpoint >=0.
This is failure of this enclosure to certify a sign, not evidence that
the actual root functional is negative or that full PSD is impossible.
The prescribed stop parks this single estimate without another weight,
new point, solve, coordinate refinement, higher-order rescue or midpoint
verdict. The earlier ATTEMPTS/098–099 remain unchanged.

The full specialization, imported theorem, hypotheses and proof are
canonical in [L120](../lemmas/L120-full-product-global-comparison-inconclusive.md),
section “Residual-corrected mode-one test”. Complete evidence is in
`scripts/finite-support/root-residual-functional.json.gz` and
`scripts/finite-support/root-residual-functional-verification.json`:
all 81,355 source coefficients, 28,215 collected cubics, 64 exact
residuals and 64 whole-box derivatives checked; 56,821 independent
checks pass with zero failures. Separate critical review of this
addition is not claimed. No source-PSD or 955–957 boundary improvement
follows. A future actual-principal Rayleigh test is REVIEW_REQUIRED;
no such test or new formula is derived in this step.
