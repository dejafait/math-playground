# Joint detector rounding — working record1261

Gate: assessment1260, its exact COVERED_TARGET; one finite-error
specialization, not an implementation or a new signing mechanism.
Retain C032b's full support/mass hypotheses and exact constructed q,
degree bound M, coefficient bound C and Q(q)<=-3/2.

Proposed calculation, to be written fully in C032c: put
R=max(1,B), D=AB R^(2M), K=2M+2. Every exact Hankel entry has
absolute value <=D, including B<1. For coefficient-l1 error delta,
the moving-vector error is <=D(2C delta+delta^2). Choose
delta<=min(1,1/(4D(2C+1))); this costs <=1/4.
For uniform logarithmic-moment error eta, the matrix entry error is
<=K eta, and ||q_hat||_coeff,1<=C+1. Choosing
eta<=1/(4K(C+1)^2) costs <=1/4 more. Expected conclusions:
Q(q_hat)<=-5/4 and Q_hat(q_hat)<=-1, with exact scalar evaluation.

Checks still to spell out: absolute convergence before expansion,
conjugation/reality, both cross terms and the error square, all moment
indices 2 through 2M+2, M=0 padding and B<1. Finite real data are
certified inputs, not outputs of the argument. Do not claim RH progress
beyond this conditional certificate. No mathematical scripts are needed.

Completion: the full specialization is now recorded in C032c, including
these checks and the separate scalar evaluation allowance. Its proof
still awaits an independent audit; this working note records the
initial calculation rather than a second canonical proof. No mathematical
scripts ran.
