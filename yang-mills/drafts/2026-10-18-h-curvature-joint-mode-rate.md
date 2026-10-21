# H curvature static replacement — bounded attempt

STEP_ID: YM-20261018-321-h-curvature-joint-mode-rate

Approved target: determine whether L097(4)'s full-prefix static-replacement
error is O(N^(5/2) log(eN)^2) for both actual probes. Coverage is the
unchanged EXPLORE assessment
`literature/2026-10-18-h-curvature-static-replacement-rate.md`.

Saved before completing the proof: use L097's actual Y_k=Zeta_k G,
with increment blocks G_st=1_(t<=s)P. For a unit transverse curvature
vector e, each axial sine output row has increment block
sum_(s=t)^(N-1) phi_m(s)e^T Zeta_k(s)P. Abel summation retains its
upper endpoint. L097(9)'s total variation is O(a p(k)), and the sine
partial sum is O(1/sqrt(N mu_m)); summing the N-1 input blocks gives
a candidate row-square bound C a^2 p(k)^2/mu_m. P stays on the right,
with norm one; no commutation or smooth rough-prefix assumption enters.

The test is to combine that row bound with L097(13)'s *own* identity
(B-B_0)^*(B-B_0)=mu_m/(mu_m+lambda_j) on im D_T. The resulting
joint inverse trace should give ||(B-B_0)Y_k||_HS=O(p(k)N).
Both full-curvature factors, M_0, X_(k,F) and the complete heat sum
must then give the exact static expression with O(N^(5/2)) error.
If the spectrum/domain or row count fails, retain L097's original
O(N^(27/10)); do not infer signed growth from a failed norm argument.

The downstream use is one H-curvature component in quantitative L011
control. The independent static-to-continuum rate, other response rates,
interacting reflected error <=c_box/2, continuum axioms and finite
positive mass remain open. L223 supplies the Abel method only; its
E theorem and scalar residual bound are not H estimates. Recorded
ATTEMPTS/024–025/030/045 are preserved and use different shortcuts.

Completed: [L233](../lemmas/L233-h-curvature-static-replacement-joint-mode-rate.md)
proves the stronger O(N^(5/2)) replacement error under exactly L097's
imported hypotheses. Its proof checks the actual projected increment
rows, uses L097's full-curvature spectral map, and retains M_0 and both
factor differences before the full heat sum. No mathematical script
or numerical certificate is needed for these finite analytic inequalities.
This is local ADVANCE / REPRODUCTION, not a discovery beyond the
sources checked. The separate critical audit remains pending.

The one continuation is the independent critical audit of L233.
Its newly registered assessment is REVIEW_REQUIRED, for separate
source-scope approval next turn. Essential audit inputs are L008,
L086, L088, L097 and L223, with L097's original hypotheses inherited
unchanged. Check the N-1 increment count and nonzero upper coefficient,
the projected row domain, zero curvature complement, joint spectral
multiplicities, both full M_0 pairings and the unchanged heat envelope.
Acceptance requires all these checks with no added hypothesis; a
failure must identify the precise inequality and restore L097's
surviving O(N^(27/10)) allowance as necessary. Static-to-continuum,
other component and interacting estimates remain independent gaps.
