# Fixed cosh/three-factor attempt1691 — working checkpoint

Completion note: the full specialization is now canonical in C028n,
with stop1691 and separate prospective audit assessment1691. The
partial reasoning below is preserved as the pre-proof checkpoint;
it is no longer the current continuation. The proof remains pending
independent conceptual audit.

Approved target: assessment1689, unchanged SPECIALIZE scope. One law
F(s)=P(s)cosh(sqrt(s)), P(s)=(s+1)((s+2)^2+1)/5; no tuning.
Main gap remains actual-Xi all-degree positivity. This tests only the
enriched generic local-to-global PF bridge. C028m and stop1686 are
contrasts; C028g supplies the analytic motivation, not a law input.

Source-notes1689 and C028m's full determinant/interval proof have been
read; their prior duplicate/failure and primary-source assessments
are reused. Existing notebook changes are extensive and preserved.
No essential missing coverage identified; no new literature turn.

Partial reasoning (not yet a completed proof): the finite inverse is
h(t)=(5/2)[exp(-t)-exp(-2t)(cos t+sin t)] for t>0. Positivity follows
from cos t+sin t<=1+t<exp(t). Its spectral function is
k_b(t)=exp(-t)+2exp(-2t)cos t. For t<=3/2 its derivative is negative;
for t>=3/2 use |2cos t+sin t|<=sqrt(5) and exp(3)>20.
The cosh base has rates pi^2(n+1/2)^2 and the assessed real-product
theorem supplies its positive smooth density. Convolution should
give the fixed law and its smooth zero extension.

Remaining analytic obligation: with B=log F, x_s=B'(s),
sigma_s^2=-B''(s), establish Gaussian derivative limits for the
standardized negative tilt using a bound on
F(s)/F(s-iu/sigma_s) for all real u. The expected scales are
x_s~1/(2sqrt(s)), sigma_s^2~1/(4s^(3/2)). Need polynomially
weighted integrable domination, pointwise complex Taylor remainder,
and x_s strictly decreasing onto a whole interval, not sample points.
Then apply the cited Gaussian determinant/tilt congruences and
Sra C.16, and only afterwards Schoenberg's nonreal-zero obstruction.

Continuation test: every obligation for this same object must hold.
A failed obligation rejects this object only. Any complete result
will remain pending a separate conceptual audit; actual-Xi realization,
global log-concavity and S_F=0 are independent and unresolved.
