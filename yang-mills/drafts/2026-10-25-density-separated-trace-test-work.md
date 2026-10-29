# Complete density: separated trace test

2026-10-25, bounded mathematical attempt under the unchanged EXPLORE
assessment `literature/2026-10-25-density-response-separated-kernel-asymptotic.md`.
Main gap: Wilson-specific signed control of L280(20); intermediate test:
the complete density response at normalization N^-2. A nonzero limiting
term would quantify compensation required in the other families.

Inputs inspected: L003 hypotheses and sections 2–4, L279 hypotheses and
exact reflected-pair interpretation, L280 hypotheses, density proof,
audit and section 7. ATTEMPTS/048–049 and the source-work handoff contain
no separated trace-norm estimate. Reuse the ready assessment; no new
source or broader target is being approved here.

Checkpoint before completing the argument: put W_pm=diag(sqrt(h_pm))
on source-supported 12-plaquettes, C_12 the corresponding rows of C,
T=W_- C_12 G C_12* W_+, and U_pm=G C_12* W_pm (rectangular restrictions
understood). Under reflection, T becomes a positive matrix by L003's
exact separated mode factorization. Its trace norm should be
m_a=a^4 sum_p f(z_p) C_a(theta z_p,z_p)=O(1).
The a^4 is essential: Cx=a^2 dA when x=aA. The one-color estimate
||U_pm||^2<=F ||G||<=F N^2/12, together with the full
||D||<=241/4, should give |Tr(D G_-+)|<=241 F N^2 m_a/8 after both
orders and three colors. This would remove the earlier sqrt(log N)
loss, but would not establish convergence, a lower bound, or a sign.

Continuation/abandonment test: verify the rectangular factorization,
reflection trace norm, counting-measure normalization, all boundary
mode sectors and color/order factors. If valid, record a bound only;
do not infer that bounded N^-2 responses have a unique or nonzero limit.
All internal anchors remain in U_+* D U_-; exact finite-domain operator
bounds may control them without a bulk replacement or termwise limit.

Completed: the factorization and all constants are written in
`../lemmas/L281-separated-complete-density-quadratic-bound.md`.
The outcome is the upper bound O(N^2), not an asymptotic equivalence.
L281(15)–(16) also give a uniform external-mode tail estimate, reducing
future convergence work to finite fixed-mode sandwich matrix elements.
All internal density anchors remain untruncated. No numerical evidence,
new external theorem, or mathematical script is used. This is local
progress beyond the prior notebook bound; originality beyond checked
sources is not certified. The next action remains the unchanged approved
target; the fixed-mode sandwich limit and its possible sign are unresolved.
