# Step 71 working record: positive blend of the two existing weights

The invocation-start target and unchanged EXPLORE assessment are in
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
This is one mathematical attempt on that target. Main gap: actual-Xi
mixed positivity. Intermediate test: whether the convex blend of L673
weights b and L681 weights w cancels the leading full residual with a
uniform rate strictly above 1/100. Such an approximation could support
discrete-sign transfer; original H, support and Xi realization remain open.

Exact inputs read: L666 (6), L673 (1)--(10) and audit, L681 (1)--(8),
C681b's finite norm result and alias proof. The prior unmodified-weight
finite test and fixed-rectangle stop are preserved. Neither proves an
asymptotic obstruction for this blend. Preexisting edits are untouched.

For 0<=theta_n<=1, use v_a=(1-theta_n)b_a+theta_n w_a. These weights
are nonnegative, independent of u, and retain anchor one. Put
F_b=W_(-R)-1-sum b_a W_a and F_w=W_(-R)-1-sum w_a W_a;
the full blend residual is (1-theta_n)F_b+theta_n F_w, including all
cross terms. A finite fit cannot pass the continuation test.

Continue only on a common leading profile with a positive cancellation
coefficient and a paid uniform remainder at a rate >1/100, or a useful
rigorous intermediate estimate toward that test. Stop this blend on
certified incompatible leading coefficients or an unavoidable remainder
rate <=1/100. At present no such coefficients or remainder are proved.

Investigating exact signed residual structure before asymptotic estimates.
At u=-1 the full parameter kernel has positive real parameter poles;
its rational formula may permit a discriminating linear functional.
This is a possible method, not an established positivity assertion.

Candidate obstruction now being checked (not yet a proved result): use
S_b=1+sum bW and S_w=1+sum wW at u=-1. Both right-contour integrands
are negative on the positive real parameter axis. Their limiting real
exponents are E_w(s)=F(s,-1)-2cs and
E_b(s)=F(s,-1)-cs-(3/5)s^2+K(s), c=10*pi/27,
K(s)=(10/27) integral_(-9/20)^(9/20)(log|t|-log|s-it|)dt.
Expected saddles lie in (1/20,1/10). A common lower exponent bound
-121/13000 follows if 0<2c-F'(0)<11/50, F''>=13/5 and E_b>=E_w.
The required end-edge bounds and uniform local remainder are still being
verified. Same negative leading signs would prevent any convex blend,
including n-dependent coefficients, from cancelling this packet.

Planned norm transfer: reuse the already assessed Danchenko--Semin
Theorem 2 through L666, enlarging its reflected pole set to include -R.
Choose its quadrature phase to include u=-1. If all pole/order hypotheses
hold, its positive weights give ||F_blend||_2>=|F_blend(-1)|/sqrt(18K),
K<=n(n+2)/3. This would retain all modes and cross terms. Source hypotheses,
real-axis signs and each analytic remainder must be verified before any
claim; no finite norm fit or absolute-contour stop suffices.

Continuation of the preserved unfinished draft, 2 November 2026:
the 18 scalar checks replay successfully. The intended completion uses
separate right edges at the two real stationary points, not a claim that
the profiles coincide. On those edges both integrands are negative at
the real point. The full vertical integrals have the same negative
Gaussian leading sign. The finite-product top/left exponents are at most
-3/200 and -3/80; the Robin complementary edges are at most -1/50
eventually. Uniform log-derivative errors O(1), rather than only o(n),
are needed for the centered signed limit. They follow from smooth
Riemann sums for denominator logarithms; the singular numerator
normalization costs O(log n) and has zero z-derivatives. Details are
being written canonically. These observations are not yet independently
audited; no arbitrary-positive-weight conclusion is intended.

Completed locally in `lemmas/C681c-positive-blend-signed-saddle-obstruction.md`.
The canonical proof uses two separate saddles with the same negative sign,
not the initially contemplated common-profile cancellation. Its 22 exact
scalar checks pass; the analytic argument awaits a separate conceptual
audit. The earlier candidate reasoning above is preserved as unfinished
work history, not an additional theorem or independent source.
