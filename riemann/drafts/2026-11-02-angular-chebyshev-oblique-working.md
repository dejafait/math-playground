# Oblique-grid upper Chebyshev band — working record

STEP_ID being prepared: 2026-11-02-angular-chebyshev-oblique-01.
The invocation-start EXPLORE assessment is reused unchanged:
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
One bounded mathematical attempt tests its angular detector via the
saved refinement u=exp(i*pi/6), odd m, n=3m, unit Chebyshev residues,
9/20<=r<=1/2. Existing work is preserved.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs. Intermediate target: a uniform angular coefficient lower bound
with exponent strictly less than 1/32 on this remaining radius band.
Downstream use: rule out this synthetic subfamily as a full-angular
countersequence and support a possible common-pole detector. General
distributions, other radii, layer isolation, other poles, census and
clearance, simultaneous realization and an independent upper bound
remain unresolved; no Xi conclusion is assumed.

Inputs inspected: C645g normalization, C645o exact weights, C645l's
finite-node identity (23)--(24), and the full audited C645r proof.
Scoped duplicate/failure check includes the endpoint working/audit
records and the angular ellipse, full-energy, inner-input, entry-sign
and zero-evaluation stops. None treats the nominated oblique band.
Reuse the ready residue, contour and scalar Fourier citations; do not
reprove their general theorems or refresh unchanged source coverage.

Bounded test: retain both complex endpoint contributions, prove a
uniform relative endpoint error, and compare the connector and exact
finite-node errors to the surviving endpoint rate. Use a fixed angular
interval, or explicitly charge its measure. Continue on a strict
uniform exponent margin, a decisive obstruction, or a saved refined
inequality; otherwise park this variant. Numerical diagnostics are
not a proof or an admissible angular countersequence.

The diagnostic `scripts/one-sided-hankel/angular-oblique-diagnostic.json`
samples endpoint rates .0378845 and .0391825 at r=1/2, both above
1/32. These values are not certificates. The nominated positive test
therefore needs a rigorous obstruction check, not extrapolation of
C645r or further angle sweeps.

Refined test within the same attempt: at r=1/2 certify both endpoint
gains >=.036, positive real horizontal logarithmic derivative, connector
gain >=.0375 and ellipse factor ratio <=11/10. With ellipse width .1,
the exact finite-node denominator gives remainder exponent >.03539.
An angular interval |arg(u)-pi/6|<=10^(-6) costs at most .000004 in
each exponent. If these inequalities hold, both retained coefficients
are O(sqrt(n)*exp(-.035*n)) on that interval, stopping this particular
two-coefficient endpoint test. This would not bound the full constant
input, operator norm or full angular mean.

Completed bounded test: the exact certificate and analytic proof are
canonical in [C645s](../lemmas/C645s-oblique-chebyshev-two-coefficient-obstruction.md).
It gives ||(c_0,c_1)||<=C sqrt(n) exp(-.035n) uniformly near pi/6
at r=1/2. The endpoint lower rates exceed .036, the connector rate
exceeds .0375 before angular loss, and the finite-node error rate is
.035396 after that loss. All 19 rational checks passed; the full
selected bound/check/failure fields were inspected. No floating-point
diagnostic is a proof premise. A separate conceptual audit remains open.

Decision: NEGATIVE for this nominated oblique two-coefficient test,
not for the angular operator detector. The contour argument uses an
upper bound, so it needs neither phase cancellation nor a Laplace
asymptotic expansion. Other angles and coefficients are uncontrolled.
The small-radius result C645r and prior stops are unchanged.

Continuation nomination only, with no calculation here: test a unit
Hardy input formed from the outer half of the grid factors, retaining
the full output. The ready Fourier/residue assessment and C645n's
exact projection mechanism apply to such finite analytic inputs; its
full-product rate obstruction does not decide the partial product.
The scoped read of C645n and the angular input/projection working
records found no earlier test of this outer-half choice. This is a
new noncancellation mechanism to be tested, not a claimed estimate;
it does not depend on accepting C645s as an audited theorem.
