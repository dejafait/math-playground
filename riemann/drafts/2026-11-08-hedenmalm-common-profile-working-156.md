# Approved common-profile attempt, step156

The gate is the unchanged SPECIALIZE assessment
`literature/2026-11-08-hedenmalm-large-real-zero-common-profile.md`.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
This step tests only the proposed alpha^2 normalization of the existing
L-image in logarithmic L2, with the source's unchanged primitive.
Success could exclude this metric using sufficiently large real-zero
pairs; it would not construct a replacement or resolve the main gap.

Inputs read: audited L906 (all derivative estimates and curvature),
L907 (primitive and ODE), L908(1)-(3) (normalization, exact-zero tails
and q bound). The step154 addition is not an input. Relevant scoped
domain, metric-import, first-pair phase and certification stops are
preserved. Prior coverage supplies DLMF2.3(i) and Hardy1914; no new
source review, root computation or mathematical script is planned.

Unfinished reasoning saved before the norm argument: put z=i alpha and
T_alpha h(x)=exp(-z x) integral_(-infinity)^x exp(z s)h(s) ds.
At an exact real zero every full derivative transform of W vanishes,
so each T_alpha W^(j) also has the negative upper-tail representation.
Candidate F=-i(W''-q W'), q=W'/W. Three endpoint terms for both U
and U' appear to leave a scaled error bounded by alpha^(-1) times
|W'''|+|q W''|+integral_(|x|)^infinity |W^(4)|
+|q| integral_(|x|)^infinity |W'''|.
The full envelope's L2 integrability, exact signs and derivative
commutation must still be proved. W''(0)<-1/6 and q(0)=0 would make
F nonzero once the formula is justified.

Continuation/abandonment test: prove a common finite L2 envelope and
strictly positive limiting norm, or identify a rigorous scaling failure.
A formal expansion, pointwise convergence or an unpaid q-weighted tail
does not pass. No claim is made at this checkpoint.

Completion: the saved reasoning above is superseded by canonical L909,
which supplies the complete estimate and metric obstruction. It remains
unaudited; use the canonical proof for every mathematical claim. No
unpaid norm estimate remains in this attempt. The actual-Xi positivity
gap and the independent metric/symmetry construction remain unresolved.
