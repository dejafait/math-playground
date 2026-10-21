# Step 157: capped rare-cubic fixed-moment test

Initial reasoning was saved before completing the bounded calculation.
The prior EXPLORE assessment is
`drafts/literature/2026-10-16-capped-rare-cubic-asymptotic.md`.
The target is its exact fixed-lambda F_lambda asymptotic, with the full
actual response, curvature and sharp uniform-height marginal retained.

Use L418's rho=|X0|, D=Delta, B=Bcal, ell=log H,
M=lambda ell^2, and L409/L410's strictly positive beta_*.
L419 supplies only the independent O(ell) bulk. The proposed test splits
exactly at rho=M, and applies the assessed Curran--Heycock fixed-p
ordinary-jet envelopes for 3<=p<=4 to each region. The exponent to check
is p^2/4-2(p-3)=2+(4-p)^2/4. If the minimum is only 2 with unknown
constant, stop this certificate; do not infer either the equality or
its failure for the actual observable. Check the absolute physical
replacement before making any reduction. No generic-law replacement,
cap removal, independence or RH premise is allowed.

The main gap remains actual clipping, L413's full regulator margin and
global mixed positivity. Completing this scalar equality would only
complete one rare/bulk ansatz condition; L418's separate audit and
actual/global realization would still be missing.

Completed result: the full proof is canonical in
[L420](../lemmas/L420-capped-cubic-power-window-and-moment-budget.md).
Both outer logarithmic-power regions are negligible, but the optimized
fixed-moment certificate still stops at an unspecified O(ell^2) bound.
The [failure record](../ATTEMPTS/2026-10-16-capped-cubic-fixed-moment-certificate.md)
preserves the limit of that certificate. No capped equality or
incompatibility was established. Outcome NEGATIVE concerns the stopped
certificate, not the actual asymptotic or the conditional law.
