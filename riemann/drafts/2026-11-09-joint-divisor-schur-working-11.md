# Joint divisor Schur attempt — working checkpoint, step 11

Approved target and coverage: the unchanged TARGET in
literature/2026-11-09-joint-divisor-contraction-test-9.md (EXPLORE).
Main gap: L030-L032/C032a actual-Xi mixed positivity. Intermediate
use: a strict L928(11) margin could support a later joint bump projection.
Threshold: coefficient-uniform relative norm <=1-eta, eta>0 fixed,
or a joint margin surviving L928(3)-(5). No joint result yet.

Read full audited L928, L737 finite identities and step261 audit,
L637 normalization and phase bounds, L926 finite conditioning, and the
scope-8 source comparison and three preserved route stops. Existing
notebook changes are extensive and remain untouched. No new source
or cross-notebook input is needed for this approved attempt.

Working notation, not yet a proved result: G(d,n)=1_(d|n)*sqrt(phi(d)/n),
y_s=G D_s c_s. The exact diagonal metrics should be
H_s=a_s I+2 diag(kappa)-K-K*, where a_s=T^-1 integral w_XT A_(t,s).
The candidate cross matrix is alpha_+ M^T diag(j_+) M+alpha_- diag(j_-),
M=G diag(n^(-2i/L)) G^-1, j_+=J_(1+2i/L)/phi, j_-=conjugate(j_+),
alpha_±=integral w_XT exp(i epsilon_t) exp(±i ell_t/L)
*zeta(1±2i/L) dt. Check all orientations before accepting this.

Selected test: weighted Schur applied to the nonnegative majorant that
separates the two conjugate terms, in the exact H_-,H_+ energy metrics.
Potential obstruction: the d=1 divisor direction sees unit diagonal
entries in both incidence terms and energy a_s~log T, so separate
moduli may have a norm floor tending to 1. Must prove this with both
metrics, exact phase and all weighted orientations; a floor for a
majorant does not imply failure of the true contraction. Preserve the
full residual if this occurs; do not follow it with matrix samples or
larger dictionaries. No lemma or conclusion has yet been asserted.

## Completion

The proposed orientations and full energy normalization were resolved in
lemmas/L929-joint-divisor-termwise-schur-floor.md. Its proof, not these
working guesses, is canonical. Outcome NEGATIVE: the selected majorant
has a unit limiting Schur floor for every positive weight choice.
The combined operator remains unresolved. No mathematical script was
needed. The new continuation is source-only and REVIEW_REQUIRED in
literature/2026-11-09-joint-combined-operator-coverage-11.md; no integral
representation was derived or approved in this step.
