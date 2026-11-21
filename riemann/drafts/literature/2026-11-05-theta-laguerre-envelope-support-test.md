# Theta/Laguerre logarithmic support test: proposed narrow specialization

TARGET: Prove or refute exponential localization of L795's absolute theta-Laguerre integral outside I_d=[(log d)/4,3(log d)/4], relative to A_d(kappa)=integral_(I_d) K(u)exp(kappa*d*u^2/[8(log d)^2])du, uniformly for 1<=kappa<=2.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step561 searched Laguerre/theta/Jensen localization and uniform remainder terminology, and scoped local literature/attempt records; no matching logarithmic-window estimate was located. No novelty claim; the estimates to specialize are standard.
SOURCE_EVIDENCE: DLMF 18.15.17–20 (fixed-alpha Bessel expansion and uniform remainder), 10.16.1 (exact half-order Bessel formulas), and L019/L021/L795 were read; source domains and access qualifications are recorded in the completed uniform-oscillatory assessment.
COMPARISON: Known uniform kernel bounds and the exact finite polynomial are available. The target asks only for a theta-weighted support comparison, not a signed asymptotic or real-rootedness theorem; no source supplies this precise comparison verbatim.
GAP: The two complementary integrals and their degree-uniform ratio to the positive denominator must be estimated; no c>0, onset, or successful bound is established here. Signed cancellations inside I_d remain independent.
REASON: This pays a concrete missing unbounded-support interface without assuming a barrier margin; it is distinct from repeating a generic relative-sign budget or the failed full-support interlacer.
SCOPE: d is an integer tending to infinity, d>=3, kappa in [1,2], x=kappa*d/(log d)^2, actual K and F_(d,u) of L019/L795; only the one absolute-support inequality below is covered. Separate approval is required before research invocation.

## Exact bounded test

Use L795's F_(d,u)(x)=d!/(1/2)_d L_d^(-1/2)(u^2*x/4), and define

\[
 B_d(\kappa)=\int_{(0,\infty)\setminus I_d}
       K(u)|F_{d,u}(\kappa d/(\log d)^2)|\,du.
\]

Test whether there exist constants c>0 and d_0>=3, independent of
kappa, such that

\[
 B_d(\kappa)\le e^{-cd}A_d(\kappa)
 \quad(d\ge d_0,\ 1\le\kappa\le2).
\]

The denominator is an explicitly specified positive envelope integral,
not |P_d|, not a signed leading term, and not an asserted approximation.
No estimate for it is proved by defining it. Normalizing K by m_0 would
cancel in this ratio. A statement at fixed d or fixed kappa is weaker
than the test. Finite numerical samples cannot establish or refute the
eventual uniform assertion.

Continuation criterion: obtain such constants and justified uniform
onset (an existential onset suffices if every limiting inequality is
proved). This would remove the exterior at the envelope scale and
permit a later, separately assessed cancellation test inside I_d.
Abandon or refine this particular window if a rigorous competing
support region prevents exponential separation. Failure to close an
estimate in one attempt is not a counterexample; preserve partial
bounds and do not rename the same exhausted test.

## Source reuse and specialization contract

The source evidence is in
[step561's completed comparison](2026-11-05-theta-laguerre-uniform-oscillatory-localization.md).
Import NIST [DLMF 18.15.19–20](https://dlmf.nist.gov/18.15.E19)
with n=d, alpha=-1/2, nu=4d+1, t=u^2*x/(4nu), fixed truncation
order and a fixed distance from t=1. Keep every normalization factor.
Use [10.16.1](https://dlmf.nist.gov/10.16.E1) for the half-order
factors; justify small-u limits rather than importing the general
nonnegative-order ODE theorem at negative order.

For any u-region outside that Bessel theorem's domain, use L795's exact
finite polynomial with a proved bound and L019's actual theta decay;
do not extrapolate the oscillatory expansion. The Airy theorem from
the completed review is available if necessary, but no Airy remainder
integral from the inaccessible Frenzen–Wong paper is assumed. A
pointwise bound must be integrated with its dependence on d retained.

The local work is the weighted domain split, denominator comparison
and uniform constants. Reproving the classical asymptotic theorem
is unnecessary. Expected completed classification is REPRODUCTION:
ordinary specialization and estimates, with no certified originality.
No mathematical script is necessary unless a specific calculation
needs a full saved certificate.

Essential inputs: L019 (K positivity and tail bound), L021 (finite
moments), L795 (normalization, exact polynomial, integrability).
L810 and the previous interlacing/Favard/compensation stops are
contrasts only. No cross-notebook input or RH assumption. Positive
signed margins, the adequacy of the proposed x scaling, edges,
initial degrees, shifted/mixed transfer and all-degree positivity
remain unresolved even if this test succeeds. Mathlib full matching
coverage is unchecked; no formal theorem is claimed.

This is a new continuation nomination, not a completed calculation.
The next invocation must separately approve its source scope before
dependent mathematical work, as required by the supervisor rule.
