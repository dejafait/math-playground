# Weighted centered-gap Picard attempt — step 142

Approved target: the unchanged TARGET in
`drafts/literature/2026-11-03-centered-gap-gevrey-profile-scope.md`
(SPECIALIZE, available at invocation). This is one mathematical
specialization attempt, not a new source review. Main gap: actual-Xi
mixed positivity and unbounded-height signs. The possible intermediate
use is signed interior/transition truncation control; no finite-response
or logarithmic-charge conclusion is being attempted.

Local orientation used the supplied complete overview and DAG, then
L694 in full, L696 Section 2, and L702 Section 2 and the corresponding
parameter-selection audit. L695's statement and the L702 stop were
checked. Existing untracked/modified work is preserved. No matching
weighted local result is identified in the ready assessment or the
scoped previous Picard/audit comparisons. No novelty claim follows.

Saved before completing the proof: choose the initial Phi and eta in
Gevrey order 2. For real |s|<=1, write

    g_s(t)=Phi(t)*(exp(2*pi*i*s*t)-1)/s,
    g_0(t)=2*pi*i*t*Phi(t).

The analytic factor is 2*pi*i*t*integral_0^1 exp(2*pi*i*theta*s*t)dtheta.
Uniform analytic derivative bounds on the fixed support, combined
with Phi's fixed factorial-squared bounds, should give common Gevrey
constants. Imported Fourier decay would then give a common majorant
D*exp(-delta*sqrt(|k|)) for g_s-hat(k), including k=0. The exact
parameter integral for E_m(v)-E_m(u) should retain r*|v-u|.

The intended compatibility argument is to bound the convolution
constant uniformly for 0<=c<=delta/2, choose the Lev constant/radius
also to control that bound and L702's width-uniform unweighted B, and
only then choose w and a smaller c allowed by Q_w. No small weighted
Q_w norm is required if the same Y-ball iterates converge geometrically
in the weighted norm. Psi is not assumed globally Gevrey; Q_w equals
the fixed analytic phi times the two Gevrey bumps on their support.

Unfinished checks: common derivative/Fourier constants, exact reflected
data regularity, weighted absolute summation and source-limit identity,
invariance of the original Y ball, and the full order of fixed choices.
Continue only if these all hold simultaneously with r<=1/8,
r*sum|e_m|<=1/(16*pi^2), fixed positive centered width, real shifts,
unit masses and anchor. Stop this sufficient mechanism if a parameter
dependence is unpaid or the prescription changes. Such a stop would
not exclude every weighted profile.

Later finite-response work would still require the L666 family with
n=12q+3, both actual endpoints, j=0, inverse angle and every M spatial
moment. L695's absolute-cost and L702's endpoint-only stops are retained.

Completion: the scoped attempt succeeded at the informal-proof level;
full proof and citations are canonical in
`lemmas/L703-gevrey-weighted-centered-gap-picard-profile.md`. The
common kernel bound is paid for all c<=delta/2 before selecting r
and w; the exact data then select a smaller positive c without
changing those choices. The same iterates converge in the weighted
norm and L702's unweighted bound pays smallness. This does not assert
independent audit or any finite-response/Xi estimate. The unfinished
checks above describe the preserved initial checkpoint; L703 contains
the completed arguments and is nominated for separate critical audit.
