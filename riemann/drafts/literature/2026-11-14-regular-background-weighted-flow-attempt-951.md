# Regular-background stopped-density attempt — assessed scope951

TARGET: Prove or refute uniform integrability of the stopped weighted densities for S(q)=-2 log q+H(q), q(0,r)=ir, with H holomorphic and H',H'' bounded on a fixed disk, up to first zero hit or escape.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Source comparison951 completed exact/stronger-result searches for this nonzero-H target and compared local duplicates and stops; no adequate matching theorem was identified. Full queries and inspected cases are in review950, completed at step951.
SOURCE_EVIDENCE: TNV JHEP10(2017)100 arXiv1706.03822v2 Section2.2(2.19)–(2.21), footnotes1–2 p6, Sections3.1–3.2 pp7–9, AppendixB(B.1)–(B.5) p22 https://arxiv.org/pdf/1706.03822v2; Kanazawa–Tanizaki JHEP03(2015)044 arXiv1412.2802v2 Section2 pp3–6 https://arxiv.org/pdf/1412.2802v2; Tanizaki PRD91(2015)036002 arXiv1412.1891v3 IV(32)–(35) https://arxiv.org/html/1412.1891v3; LY qualifications reused from review948.
COMPARISON: Source machinery governs nonsingular raw trajectories and their real-parameter Jacobian. C466q proves the exact H=0 bound. Inspected logarithmic-zero examples, thimble constructions and changed-metric completeness do not establish the arbitrary-H stopped-density modulus.
GAP: A uniform measurable-set absolute-mass estimate with controlled parameter dependence, including moving hitting boundaries, remains unproved. No exact theorem is available for import from the inspected passages; no counterexample is known here.
REASON: One bounded attempt can test whether the full weighted Jacobian tolerates a local analytic factor. This is established-route development with no originality claim or central sign mechanism; the new assessment needs separate next-turn approval before mathematical invocation.
SCOPE: One complex variable, unit flat metric, raw upward conjugated-gradient flow, fixed physical time, analytic H on D_R with finite H(0), bounds |H'|<=M_1 and |H''|<=M_2, real 0<a<R, initial 0<|r|<a, first-hit/escape stopping; no tangential variables or actual-h/global specialization.

## Source gate and exact formulation

The complete comparison, including primary hypotheses, essential
cases, queries, unread leads and duplicate/failure checks, is
[review950 completed at step951](2026-11-14-regular-background-weighted-flow-950.md).
This companion records only the exact mathematical continuation.
No perturbed estimate has been derived or verified. EXPLORE marks
adequate bounded discovery, not an established theorem or novelty.
The supervisor's separate approval must precede this attempt.

Fix the data in SCOPE. Follow the maximal nonsingular solution of
\(\partial_Tq=\overline{S'(q)}\) from \(q(0,r)=ir\).
On surviving trajectories let \(J(T,r)=\partial_rq(T,r)\), taking
the derivative at fixed physical T, and keep the signed density
\[
 W_T(r)=-q(T,r)^2e^{-H(q(T,r))}J(T,r)/i.
\]
Set it equal to zero at r=0 and once the first zero hit or first
disk escape has occurred. At an escape approached only as a limit,
use the maximal interval in the open disk and the same zero-extension
convention. No classical trajectory or Jacobian through zero is
presumed. Branch choices for log must not change the specified weight.

Seek some \(T_0>0\) and a finite modulus \(\omega(s)\to0\)
as \(s\downarrow0\), with dependence on R,a,H(0),M_1,M_2 explicit,
such that for every Lebesgue measurable \(E\subset(-a,a)\),
\[
 \sup_{0\le T\le T_0}\int_E|W_T(r)|\,dr\le\omega(|E|).
\]
If bounds are claimed uniformly over backgrounds sharing these data,
prove that quantifier explicitly. A counterexample to a stronger
class-uniform rate must be distinguished from failure of the target
for one fixed admissible H. Measurability and the definition on
surviving branches must be justified as part of any claimed estimate.

## One bounded attempt and decision test

Use C466q as the exact control and TNV's pre-singularity variational
law as source machinery. Try a direct differential estimate for the
modulus of the full weighted density, controlling the regular terms
by the stated data. This is a proposed proof strategy only: no
differential inequality, singular-term cancellation or envelope is
asserted here. A local cutoff argument must retain its dependence
as the cutoff approaches zero; a bound only on compact zero-free
sets does not finish the target.

Continue this attempt only with a complete measurable-set modulus,
an admissible counterexample, or a precise new estimate identifying
the remaining obstruction. State explicitly which conclusion was
achieved. An integrable envelope is sufficient but not required.
Origin-neighborhood control alone does not cover moving hitting
boundaries. Do not substitute variable-time differentiation,
action-phase constancy, a divided-coefficient smoothness test,
integral invariance or modified-metric completeness. Do not infer
failure of the target merely because one stronger envelope fails.
If the attempt gives no new estimate or informative obstruction,
save the reasoning and reassess rather than replaying H=0.

The plausible use is one local analytic-factor payment before any
actual-weight deformation. C466q is the essential local control;
C466a/k/l are motivation and conventions only, not a perturbed bound.
Stops927/932/941/947/948 retain their exact scopes. Tangential coupling,
metric normalization in original coordinates, noncompact homology,
endpoint payment, global signed integration, all-order positivity and
Xi realization remain unresolved even if this estimate succeeds.
No cross-notebook input or RH candidate is involved.

Full matching Mathlib coverage has not been checked; unknown
availability is not evidence of absence. If a theorem is established,
its full hypotheses, proof and qualifications belong in a canonical
lemma file at that later research step, not in this assessment.
