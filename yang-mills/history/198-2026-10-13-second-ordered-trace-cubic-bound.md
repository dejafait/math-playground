# 198 — 2026-10-13 Second ordered trace is cubic-bounded

STEP_ID: YM-20261013-198-second-ordered-trace-cubic-bound

RESEARCH / REPRODUCTION / proof_attempt, reusing the unchanged prior-ready
EXPLORE assessment for the complete cubic residual/action response.
[L166](../lemmas/L166-cubic-residual-second-ordered-trace-cubic-bound.md)
proves O(N^3) for L161(3)'s entire second trace. The residual/Green
kernel retains two differences in both generator orders, with both
insertion subtractions bounded. A global relative Green estimate
supplies the prefix bound with its row fixed, which was not the
placement covered by L165's compact-column estimate. Their anisotropic
product is summable before the supported residual rows are counted.

The entire upper action exterior contributes O(N^2); the smooth-residual
subtraction contributes O(sqrt(log(eN))). Analytic checks retain all
source/end rows, the exact trace order, constant mode and complete heat
sum. No mathematical script or finite-mesh extrapolation is used.
This is local standard-method progress, not a discovery beyond the
sources checked. Cubic boundedness does not prove bulk convergence or
vanishing. Only the fourth ordered trace now lacks cubic control;
the retained second/third and mixed limits remain unresolved. Continue
the unchanged complete target with that fourth order before taking
limits, preserving ATTEMPTS/009, /011, /036 and /037. Other jets,
finer scales and interacting/continuum/infrared requirements remain.
