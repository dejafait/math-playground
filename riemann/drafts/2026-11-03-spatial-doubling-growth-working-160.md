# Spatial doubling growth attempt — step 160

Invocation-start EXPLORE scope:
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
The target is its unchanged full-family B_sp(n)=o(n), with s=65/64
and |u|=1/2. One actual L703 profile is fixed before n=12q+3.
All L666 weights, both signed node sums, the anchor, inverse angle,
j=0 and all M=n/3 moments are retained. L706 supplies nonzero
slices and finite-n logarithmic integrability; L657 is downstream
accounting, not a positivity input.

Main gap: actual-Xi all-degree positivity. Locally, L706 leaves the
complementary spatial Jensen defect unpaid. A sublinear B_sp could
pay it, with angular amplitude, full charge, H/support and actual-Xi
realization still independent. A positive lower limiting B_sp/n
would stop only this sufficient mechanism.

Saved preliminary reasoning (not yet an audited result): write
b(u)=log(S_s(u)/S_1(u)). Three-circles at 1/2,1,s gives
log S_1-log S_(1/2) <= (log 2/log s)*b(u). At a nonzero
maximizing point of the closed radius-1/2 disk, boundary Poisson--Jensen
and the Poisson-kernel minimum >=1/3 give
Delta(u)<=3*(log S_1-log S_(1/2)). Thus the prospective transfer
constant is 3*log 2/log(65/64), with no additive error. Constants,
degree drops and boundary zeros require explicit final treatment.

The exact spatial finite-sum identity is G=F-T with
F=R^(-1)*sum_a W_a/(1-a*z/R) and
T=R^(-1)*sum_a W_a*(a*z/R)^M/(1-a*z/R).
The maximal node modulus is rho=sqrt(2824/3025), so s*rho<1.
The resulting absolute geometric error is not yet relative to S_1.
The remaining attempt will test whether the complete signed moment
structure supplies a useful bound for that normalization. L683's
absolute remainder, L686's full-support clearing failure and L702's
global endpoint omission stop do not supply it. No whole-circle
endpoint approximation or arbitrary residue weights are assumed.

No external source refresh is needed: the saved assessment contains
the inspected three-circles and boundary-Poisson hypotheses/cases.
No script, numerical sample or generic polynomial example settles
the fixed-profile asymptotic.

## Completed attempt

Canonical proof and qualifications are in
`lemmas/L707-spatial-growth-transfer-and-cancellation-budget.md`.
The transfer has no additive error, and the enlarged-radius remainder
has v^2=59657/61952<1. The full-moment Lagrange certificate fails to
make that remainder relative: its computed upper bound grows
exponentially. This is not a lower bound for the actual error.

The coefficient-cutoff calculation exposes a sufficient averaged
cancellation budget Cbar_n=o(n). Neither that budget nor the original
B_sp=o(n) has been proved or refuted. The recorded outcome is
EXPLORATION, with the known transfer distinguished from the unresolved
family estimate. One mathematical exploration was used; no budget
reset or mathematical advance is claimed. No mathematical script ran.

Before another attempt, review the stronger Cbar target against known
signed-moment estimates and Fourier-gap obstructions. The new assessment
is REVIEW_REQUIRED, not a same-turn approval. Keep L666, L703, L706 and
L707, the exact fixed profile and all moments; L657 remains downstream.
The uniform interpolation certificate itself should not be repeated.
