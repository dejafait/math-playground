# L714 inversion and signed decomposition audit — step 185

Invocation-start coverage is SPECIALIZE in
`literature/2026-11-03-signed-bump-inversion-audit.md`; the supplied
snapshot was read and is reused without a new source search.

The main gap is actual-Xi all-degree mixed positivity and the unpaid
complementary spatial Jensen defect. This bounded audit checks only
L714 (2)--(3), so the standalone L716 ratio can be connected to the
original fixed signed bump observable. Accept only after finite-measure
identification, absolute Fubini, pointwise inversion at zero, scaling,
pole orientation and fixed-bump interchanges pass. A concrete failed
inference requires repair or explicit qualification; no signed rate is
an acceptance criterion for this narrower input check.

Read L714 in full; L713 Hypotheses and Section 1; L708 hypotheses/source
interface; L703 fixed-profile hypotheses; L715/L716 statements and the
relevant step-175/179/183 records. The signed-rate inconclusive and
absolute-contour stop records do not settle this inverse identity.
No cross-notebook input or mathematical script is needed. Existing
unfinished notebook work is preserved.

## Saved partial reasoning

The partial fractions give the proposed g_n with the positive-exponent
transform and physical scale h. L713's factor measures after scaling
have densities lambda_t exp(-lambda_t v/h)/h and possible atoms at
zero; t=0 removes any atom in the full convolution. All have finite
variation and first absolute moment. Fourier injectivity therefore
identifies the same measure, with no positivity assumption.

Convolution with q(v)=exp(c_0 v/h)1_(v<=0)/h gives a finite exponential
sum on the positive half-line and W_n(u,i c_0)exp(c_0 v/h)/h on the
negative half-line. Their values agree at zero. The one-sided
derivatives are bounded locally, so the glued representative is
locally absolutely continuous and hence locally of bounded variation.
This supplies the hypothesis actually needed by the assessed DLMF
pointwise inversion theorem; continuity alone was not enough to cite it.

Remaining checks before acceptance: finish the normalized inversion
argument, explicit O(|Re y|^-2) strip bound, positively oriented
rectangle and residue, and compact-bump absolute Fubini. Verify that
no full-family endpoint/tail identity is certified beyond this scope.
The canonical proof will be updated only after these checks.

## Completion

Those checks pass. The full proof is now canonical in L714 Section 2,
with the bounded acceptance recorded in its Section 5. In particular
the normalized DLMF inversion applies to h*p_n(h*x), the positively
oriented rectangle gives R_n=P_n+K_n, and the compact-bump double
absolute integral is finite for each fixed n,c. No numerical check,
rate assertion, new lemma or DAG edge was needed. L713's full-family
identity and envelope, and L714's residue-rate argument, are outside
this acceptance. Mathlib full matching coverage remains not checked.

The next target reuses the unchanged, ready step-174 assessment for
the actual signed remainder rate. The newly available inputs are the
audited polynomial logarithm (L715), uniform nonzero resolvent ratio
(L716), and now the audited physical inverse (L714). They permit a
test in the physical bump variable after exact inversion, instead of
repeating the stopped absolute contour bound. No rate or endpoint
asymptotic is derived here. A bounded attempt must pay the remaining
outer cancellation or isolate a concrete failure of that proposed
payment; merely restating the inverse or ratio is not progress.
