# Approved annular first-moment test — working checkpoint

Completed in [L856](../lemmas/L856-positive-annular-collars-with-first-moment-obstruction.md).
The scratch plan below is retained as the pre-proof checkpoint; the
canonical result includes the chart, angular and boundary-sign checks.

6 November 2026. Work under the invocation-start SPECIALIZE assessment
`literature/2026-11-06-positive-annular-gluing-boundary-moment.md`.
Not yet a reviewed result. Essential inputs L855/L775/L847, with the
fixed pair and finite n hypotheses unchanged; no global Xi signs follow.

Candidate calculation: in omega=w^n dw wedge dv, the boundary primitive
for weight w^j is -w^(n+j) v dw. Inner radius r/2 uses L855's
v0=Aw+i conjugate(w)^(n+1)/(n+1). On an outer collar of radius r use
vout=v0+i b w^(-n-2), b=2[1-2^(-2n-2)]r^(2n+3)/(n+1)>0.
The added term is holomorphic on that collar, so its full density is
unchanged. Expected annular moments M0=2pi[1-2^(-2n-2)]r^(2n+2)/(n+1)
and M1=2pi b=2r M0, violating |M1|<=r M0 for a nonnegative density.

Remaining checks before claiming this: signs and both boundary
orientations; strict full-density positivity on an open outer collar;
uniform O(r^(n+1)) value and O(r^n) derivative estimates as r->0
for the added Laurent term, common inverse-chart confinement and
strict original angular determinant via L855's positive tangent.
Smooth interpolation, even if complex moments pass, is not asserted.
No automatic higher-moment continuation. Preserve prior route stops.
