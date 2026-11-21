# Frozen complete Schur residual — step532

The gate-approved target and assessment529/530 are reused unchanged.
Main gap: L030-L032/C032a actual-Xi positivity. Intermediate target:
C744v(C) at N=512, penalty256 and tau=1.43, uniformly in phase.
This could supply the separation-seven input to C744r's detector;
other separations, C744q margin, non-neutral coverage and assembly
remain independent. No new source sign or numerical artifact is used.

Inputs read: C744v in full, C744r hypotheses and (7)-(12),
L742(8)-(12), L744(6),(8), the supplied assessment, and the scoped
separation-seven/five-cell failure comparison. Earlier unfinished
work is preserved. The previous 64-mode samples are not evidence
for this 512-mode Schur residual.

Bounded test: assemble the retained phase family and its complete
covariance, with an analytic bound for every omitted response/mode.
Certify positivity uniformly, or certify a negative retained direction
of the sufficient residual. If the covariance cannot be paid, end
the attempt without changing N, penalty, tau, separation or ratio.
A negative sufficient residual alone is not a smooth neutral violation.

This file preserves unfinished reasoning before calculation. Any
floating diagnostic will be labeled as such and saved in full; a
sign conclusion needs separate error bounds. No RH candidate exists.

## Completed bounded attempt

The initial4096-mode diagnostic is preserved in
`scripts/separation-seven/residual-locator-532.json`. It was not
promoted to a certificate. The completed argument is canonical in
[C744w](../lemmas/C744w-separation-seven-full-schur-certificate.md):
all six covariance products through65535, the full omitted-mode
operator bound below.5, verified factors at65 phases and the exact
second-derivative interpolation give residual>=.030999>1/40.
N=512, penalty256, tau=1.43, separation7 and target ratio1 stayed
fixed. The numerical cutoff only subdivides the already fixed
infinite covariance.

The claimed fixed inequality is a local ADVANCE/POTENTIALLY_NEW
under the existing EXPLORE coverage, without an originality claim.
C744v and C744w remain unaudited. The new conceptual-audit target
has REVIEW_REQUIRED coverage and must receive separate approval;
no self-approval or additional mathematical attempt occurs here.
Other separations, the strict margin, non-neutral signs and global
assembly remain open. PROGRESS.md owns the sole current next action.
