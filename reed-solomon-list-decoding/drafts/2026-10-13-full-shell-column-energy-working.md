# Full-shell column energy — bounded working record

Approved target: Determine whether any column in L059's complete nonnegative interval satisfies the scalar generalized-Schur energy inequality for one distance-six extension of L056's anchored shell.

Reuse the prior SPECIALIZE assessment `drafts/literature/2026-10-13-full-shell-column-energy.md`. Main gap: arbitrary-center safety at 67/68 agreements. This step decides only one retained PSD extension at unchanged pairs and shell. L059 and ATTEMPTS/041 leave this energy untested; ATTEMPTS/038–040 concern smaller or different matrices. Preserve all prior work.

Plan: normalize by positive rho; apply L059's anchor congruence to the enlarged matrix, giving retained block diag(1,p_5 R), column (p_6,p_5 v), where R=B-p_5 J and v=t-p_6*1. Use orbit-size weighted product eigenvectors, never the Euclidean inverse of the unweighted quotient. Energy is p_6^2+p_5*<v,R^dagger v>. Reconstruct all affine coefficients of t from L059's complete certificate, independently reconstruct factor relation quotients and recurrence eigenvectors, and certify inverse-action residuals. Minimize the exact quadratic over the whole audited interval, including both endpoints and any stationary point. Preserve fixed represented entries, ten zeros, diagonal and anchor.

Continuation test: a passing parameter retains this one-column extension and parks its exclusion diagnostic; a strict minimum above p_6 excludes the interval. A broader unlabeled exclusion also requires full enlarged-matrix averaging. No global consistency, other-column, scalar, labeled, measure, RS realization or boundary conclusion is authorized.

Completed: L060 records the exact interior minimum and retained one-column PSD extension. All 372 construction and 177 independent residual/bilinear checks pass; full certificates are `scripts/finite-support/full-shell-column-energy-results.json` and `scripts/finite-support/full-shell-column-energy-verification.json`. Energy/diagonal is strictly between 199/10^11 and 200/10^11. ATTEMPTS/042 parks this diagnostic only. Separate critical-audit scope approval is pending; the main boundary is unchanged.
