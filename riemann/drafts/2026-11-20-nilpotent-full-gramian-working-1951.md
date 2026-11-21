# Nilpotent full Gramian attempt1951: saved reasoning

Approved target: assessment1949, unchanged; research under EXPLORE.
Main gap: C028b H_d=o(d), actual full k_d=o(1), actual-Xi positivity.
Test: establish o(1) or a fixed eventual positive floor for the nilpotent
unit subdiagonal shift with exactly T=d^2 and the full realified Gramian.
Neither model outcome transfers automatically to the actual companion.

Working claim, not yet verified: liminf k_d(S)>=7/16.
Let U=diag(i^(d-j)), 1<=j<=d. Then U^* S U=iS and U^*G U=K,
where K=(2T)^(-1) integral_(-T)^T exp(tS^T)exp(tS)dt.
Thus U^* J U=(B+B^*)/2, B=K^(1/2) S K^(-1/2).
Identify v with p_v(t)=sum_j v_j t^(d-j)/(d-j)!.
Its K-norm is the sum of L2 energies of every derivative, with measure
dt/(2T). S represents differentiation, with the top derivative zero.
The scalar Markov theorem already assessed in source-notes1950 at
lambda=1/2 gives ||p'||<=q_d||p||, q_d=(d+1)/(2 sqrt(2)d)<1.
Iterating this same bound on all lower-degree derivatives gives
||p||_Sob^2 <= (1-q_d^2)^(-1)||p||_L2^2, uniformly in degree.

Candidate witnesses: even and odd endpoint kernels built from Legendre
polynomials through degree d-1, coefficients 2m+1. Their scalar norm
squares and endpoint values are E,O with E+O=d^2 and |E-O|=d.
Every nonzero derivative at the positive endpoint is nonnegative.
The Sobolev symmetric-derivative pairing is a boundary sum, so these
witnesses give a lower bound retaining all observation channels.
After Sobolev normalization the off-diagonal pairing should be at least
(1-q_d^2)*sqrt(E*O)/(2T). The full trace norm should be at least twice
that value by a rank-two trace dual witness of operator norm one.
This yields (1-q_d^2)*sqrt(1-d^(-2))/2 and limiting floor 7/16.

Still to check before a canonical result: phase conjugation including
complex adjoints, positive-square-root covariance, all derivative
orders and parity orthogonality, endpoint integration factors, exact
Legendre normalizations/signs, and full trace-norm duality factor.
Known general Gramian/Markov/Schatten inputs are imported, not reproved.
Elementary polynomial identities may be derived to make the specific
normalization reproducible; no scalar-channel replacement is allowed.
No numerical values, conditioning assumptions, Xi transfer or RH
candidate are being used. Prior attempts1948/1949 remain parked.

Completion: the proposed floor has now been proved in canonical
[C029c](../lemmas/C029c-nilpotent-full-gramian-positive-floor.md),
including the finite-d lower bound, phase signs, all derivative orders,
Rodrigues normalization and rank-two compression factor. The proof
awaits an independent critical audit. The saved reasoning above is
retained as the pre-completion checkpoint, not a second canonical proof.
