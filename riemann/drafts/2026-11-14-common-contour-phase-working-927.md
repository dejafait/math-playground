# Common-contour phase specialization — working927

Approved input: test925 SPECIALIZE; normalized p and h from C466a,
x=B'(1). Work in progress, not yet an audited result.

The signed N=2 Andreief integrand should be
`-(gamma(v)-gamma(u))^2 w_gamma(u) w_gamma(v)/(2(2pi)^2)`.
Both Jacobians are inside w_gamma; no conjugation or orientation reversal.
Thus simultaneous scalar positivity and pair nonnegativity force all
secants vertical. Locally gamma=1+i t with t'(0)=1. Scalar positivity
then makes exp(ixt)h(1)/h(1+it) real near zero.

Remaining rigorous checks: weighted inversion at s=1 from C466a's
large-complex-z estimate, full constants and cross-product L1;
tilted-law mean x; characteristic function holomorphic for Im(t)>-1,
so its difference with the reflected function is holomorphic on
|Im(t)|<1. Only after the identity theorem on that connected strip
can the whole-axis symmetry criterion be imported. A symmetric
centered law cannot have support [-x,infinity) with strictly positive
density above -x. No deformation, endpoint estimate, global PF or RH
conclusion is asserted. Original working925 and all unfinished work
are preserved.

Completion927: the checks above are now written in canonical C466k.
The signed formula and holomorphic-strip bridge yield the support
contradiction, without deformation. This working note is retained
as unfinished-stage provenance; C466k is the proof record and awaits
separate critical audit. No mathematical script was needed.
