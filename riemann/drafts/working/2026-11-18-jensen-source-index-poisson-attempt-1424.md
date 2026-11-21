# Source-index Poisson attempt1424 — working checkpoint

Approved target and scope are the unchanged SPECIALIZE assessment1421,
reviewed in 1422/1423. Work is a local specialization of Evertse Theorem
9.2, not new source discovery. The supplied overview and DAG were used;
C020c's exact two channels, C019's scales, C019y's finite decomposition,
source-notes1422 and stops1417/1419 have been inspected. Prior files stay.

Candidate calculation, not yet a retained result: put lambda=vr/(ns).
In C020c (5), the plus source weight is
f_Z(y)=y^(-1/2-iZ) E_y(Z). In the minus term,
m^(ih)*(m*lambda)^(-ih)=lambda^(-ih), leaving conjugate(f_Z(m)).
The source cutoff is the integer N(Z) in both channels, with outer
domains [X,sqrt(2)X-h], n<=N(Z+h), and [X+h,sqrt(2)X], n<=N(Z-h).

Use the original analytic formula for E_y with principal Log y on Re y>0.
Its conjugate on the real axis extends by reversing the imaginary
coefficient, not by conjugating the complex argument. Expected uniform
source derivative bounds: |f|<=C y^(-1/2), |f'|<=CX y^(-3/2),
|f''|<=CX^2 y^(-5/2), from t=O(q^(-2)), |u-log y|=O(q).

For integer N>=2 import finite Poisson with its full half-endpoint
correction. Two integrations by parts pair the k and -k boundary
jumps, leaving a tail bounded by C(|f'(1)|+|f'(N)|+integral|f''|)/K.
Candidate common cutoff K=ceil(X^3) would give O(X^(-1)) per source
sum. The remaining absolute outer mass is O(X^(3/4)R(1+log R)^2)
and Z length O(X), suggesting total O(X^(3/4)R(1+log R)^2)=o(B).

Still to check before retaining: exact outer coefficients and conjugation,
paired-tail constants/signs, moving integer crossings, empty/singleton
sums, and the uniform bound with all original heat weights/tapers. A
long finite dual expression pays representation error only; it does not
bound the retained arithmetic sum or the quotient. Canonical proof, if
successful, will be C020e. Actual-Xi signs and the independent channels
remain open. No mathematical script is needed for this analytic test.

Completion: the checks above are finished in canonical C020e (1)--(13),
including exact phase combination, both domains, holomorphic source
derivatives, paired Fourier tails and the full outer payment. The
candidate calculation is now a retained, independently unaudited local
specialization. PROGRESS.md alone records the current continuation;
this saved working checkpoint is historical reasoning, not a second
proof or an instruction to repeat the completed checks.
