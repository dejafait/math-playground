# Completion-stripped Pick residual: bounded calculation

Work in progress, 1 November 2026. Approved target and source scope:
`literature/2026-11-01-completion-stripped-pick-residual.md` (SPECIALIZE,
saved before invocation). No source refresh or new mechanism is invoked.

Main gap: actual-Xi signs at unbounded heights and all-degree mixed
positivity. Test exactly E/G on L645's unchanged disk/nodes, conditional
on its stipulated simple zero and temporary finite PSD. The downstream
use is deciding whether removal of the completion yields an actionable
logarithmic-grid comparison. Continue for a discriminating bound or a
quantitatively different missing estimate; stop a renamed growth price.

Inputs read: L018, L645 and C645a in full; the supplied assessment already
compares L258 and the fixed-reserve stop. Preserve all prior work.

Initial reasoning to check: G is holomorphic and nonzero on a neighborhood
of the high disk. Put g=G'/G. Then E/G=Z=ζ'+(g-P)ζ, Z(s_j)=0 and
Z(rho)=ζ'(rho)≠0. Digamma gives g=O(log gamma) uniformly; the safe-line
anchor and Borel–Caratheodory give P=O_delta(log gamma), uniformly in n
and the admissible interpolant. Uniform convexity should therefore give
max|Z| <= C_delta,epsilon gamma^(1/4-delta/4+epsilon) log gamma.
This is only an upper envelope: it must not be called a lower bound on
the actual normalized residual. The derivative upper bound at rho has
exponent 1/4-delta/2+epsilon. Check the exact gap against lambda_delta
before reporting any obstruction. No derivative lower bound is assumed.

Pending: analytic-domain and sector checks, exact boundary-to-interior
application, explicit exponent inequality, strict floor comparison and
the distinction between a failed certificate and a failed actual test.

Completed: the full calculation, hypotheses, citations and qualifications
are canonical in C645b, `lemmas/C645b-completion-stripped-residual-envelope-limit.md`.
The uniform envelope is C gamma^(u+epsilon) log gamma, whereas the
derivative upper exponent is v+epsilon, u-v=delta/4. Direct algebra gives
lambda_delta<5delta/24. The envelope test therefore grows at least as
gamma^(delta/24) log gamma at N=floor(log gamma). Only this explicit
envelope fails: no lower bound on the actual residual maximum follows.
The calculation is complete but unaudited; no script or new source work
was needed. A derivative lower bound alone cannot repair this envelope;
a quantitatively controlled residual saving would also be needed.
