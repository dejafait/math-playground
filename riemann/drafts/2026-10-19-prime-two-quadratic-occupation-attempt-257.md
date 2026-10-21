# Step 257 — approved quadratic occupation attempt

Target: the exact compact-height test approved in the step-256 assessment
`drafts/literature/2026-10-19-prime-two-quadratic-occupation-test.md`.
RESEARCH / REPRODUCTION / proof_attempt; completed local specialization,
with a separate critical audit required.

The main gap is global mixed positivity. This bounded test asks whether
L438's unchanged complete law satisfies one necessary ordinary-derivative
occupation identity. It changes neither the law nor L429's thresholds.
A nonzero residual exceeding the full remainder would exclude this law
from this trajectory test; cancellation or an uncontrolled remainder
stops that conclusion. Realization, actual clipping and the regulator
margin remain independent gaps.

With L=log(2+t), omega=log 2 and e_H(t)=eta(t/H), the exact transport
integrand is

    [(e_H' sin(omega t)+omega e_H cos(omega t))/L
      -e_H sin(omega t)L'/L^2] x^2
          +2e_H sin(omega t)xy.

Both endpoints vanish. For the complete law the conditional raw matrix
is pYY^T+sum k_s Z_s Z_s^T+w(ell g_H K+A_H+mm^T).
K_12=0 does not delete its other cross terms. The following preliminary
notes were saved before the calculation: the x-square term suggested
omega/(30 sqrt(2)), subject to the following two estimates. Their
completed proofs are now in L440, as recorded below.

1. The original cutoff bounds M_j<=ell^(1/8), hence p_j<=ell^(1/4).
   Truncate each Poisson Fourier exponent at O(log ell); total frequency
   size is exp(O(ell^(1/4)(log ell)^2))=H^o(1). This may prove the
   eta-weighted prime-2 limit directly without adding thresholds.
2. Rare signed cross seconds cost O(sqrt(ell)) absolutely. Their leading
   response-angle functions appear to have zero angular mean; this must
   be established including the positive-direction projection ties.
   An O(1/ell) signed average would suffice. The translated-bulk cross
   mean and the constant full covariance correction must also be kept.

The saved preliminary calculation above was resolved in full in
[L440](../lemmas/L440-prime-two-quadratic-occupation-separates-law.md).
Both estimates succeed with the unchanged cutoff: the weighted Poisson
term tends to 1/(30 sqrt(2)), and the full signed cross contribution is
O(ell^(-1/2)). Its proof includes positive-direction tie neighborhoods,
all three rare terms, translation and the constant full covariance
correction. The complete residual is log(2)/(30 sqrt(2))+o(1), against
the exact zero trajectory requirement. This separates only this law
from the added observable. No actual-zeta moment theorem is derived.

Canonical inputs inspected: L424 ordinary dynamics; L438 (9)--(19);
L429 finite-product formulas and original stage selection; L419 exact K
and response; L437 negative direction; L421 positive-direction selection;
L369 gamma phase; L435 rational density. L439 and its preserved Gaussian
stop are contrasts only. No actual-zeta weighted moment theorem is needed
if the law residual is evaluated directly against the exact identity.

The single continuation is a separate critical audit of L440, after
approval of its audit scope. The vulnerable checks are the quantitative
zero-angular-mean estimate with nonsmooth projection selection, uniform
Lipschitz bounds on the finite-height signed calibration, and the full
Fourier truncation under every admissible original cutoff. Its source
coverage is recorded as REVIEW_REQUIRED rather than self-approved here.
