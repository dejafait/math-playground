# L604 layer-scale calculation: working checkpoint

Approved target: determine L604's separate M/R frequency scales under
its unchanged density hypotheses. Main gap: actual-Xi all-degree signs.
This is a standard specialization under the prior SPECIALIZE assessment
in drafts/literature/2026-11-01-l604-layer-cancellation-scale.md, not a
new positivity mechanism. L233 normalization and full audited L604 read;
pointwise and generic monotone-Stein stops retained. No scripts required.

Preliminary calculation, not yet independently audited: let ell=lim tau,
q=-tau', J_a=2 integral_0^a p(u)cos(xu)du. Nonstrict monotone substitution
should give M=ell F^2+integral_0^infinity q(a)J_a^2 da, without an inverse
derivative. The endpoint theorem gives J_a=2p(a)sin(xa)/x+E_a/x^2,
|E_a|<=B=2(sup|p'|+integral_0^infinity |p''|), uniformly in a.
Thus the error after squaring/integrating is bounded by
4 sup(p) B(c-ell)/|x|^3+B^2(c-ell)/|x|^4.
The leading weight w=q p^2=u p^2+h p' is nonnegative, integrable, and
w'=p^2+u p p'+h p'' is integrable. Expected coefficient
A=2 integral_0^infinity w>0 for nonconstant smooth monotone tau.
Endpoint Fourier bound gives |integral w cos(2xa)|<=||w'||_1/(2|x|).
Expected conclusion M=A/x^2+O(|x|^-3); floor is rapidly decreasing.
Hunter's Schwartz theorem should give D rapidly decreasing, so L604
would imply R=-A/x^2+O(|x|^-3), with superalgebraic relative cancellation.

Remaining checks before canonical write: substitution at flat fibres and
endpoint levels; all weight/derivative integrability; exact constants;
constant-tau comparison; no density-uniform constants or sign inference.
Test succeeds only with error below the leading scale; otherwise record
the exact hypothesis obstruction. No Xi transfer or higher-sign claim.

## Completed calculation

The checks above were completed in canonical C604a. The exact bound is
(W+4PBV)/|x|^3+B^2V/|x|^4 after retaining ell F^2, where V=c-ell
and W=integral |w'|. Nonstrict substitution uses the Borel layer
function on compact tau intervals and monotone convergence; equality
with J_a is needed only where q(a)>0. The formula for w' avoids any
unproved ratio-derivative bounds. A>0 for nonconstant tau; the floor
and constant case are accounted for. D is Schwartz, giving rapid
relative cancellation and eventual R<0, without signing D.
No numerical check or script is necessary for these analytic bounds.
Independent audit is nominated separately; the preliminary text above
is preserved as a checkpoint, not as a second canonical proof.
