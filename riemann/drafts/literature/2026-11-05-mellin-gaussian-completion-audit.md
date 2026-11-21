# Finite Gaussian completion: critical-review continuation

TARGET: Critically audit L800's Gaussian completion identity and 2.35/1.65 uniform allowance on all D, including branches, closed boundaries and unbounded u.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step518's exact Gaussian-tail comparison and scoped duplicate/failure search in 2026-11-05-mellin-gaussian-completion-scope.md; unchanged domain and observable, no new discovery or originality claim.
SOURCE_EVIDENCE: NIST DLMF7.7.6 https://dlmf.nist.gov/7.7.E6 and 7.8.1–7.8.2 https://dlmf.nist.gov/7.8.E1 https://dlmf.nist.gov/7.8.E2 directly reinspected 2026-11-05 in step520; paper23 v1 Section3 Lemma2 (10)–(14) https://rstation.ai/problems/riemann_hypothesis/papers/23 remains the step518 source extraction; L798 (5)–(7) and L800 supply the local audit scope.
COMPARISON: Known exact Gaussian integration and the real Mills upper bound suffice after the explicit branch and rational-constant specialization; L800 is a reproduction awaiting independent review, not a new central mechanism.
GAP: Independently check the finite-to-complete identity, admissibility of the imported real bounds, the direction of the curvature inequalities and the exact 2.35/1.65 comparison on all D.
REASON: A separate proof audit can verify or correct this completed local component without reopening global supplementary sources.
SCOPE: Source-URL recovery completed in step520; exact target and mathematics unchanged; independent mathematical audit still pending. Permitted classification REPRODUCTION. No global assembly or new mathematical target is covered.

Essential input is L798, with L797 supplying its saddle geometry. Review
L800's complete proof and the needed L798 branch/curvature ranges;
reuse the inspected exact NIST statements. L799 is context only and is
not a mathematical input to L800. Check absolute convergence, the factor
of two in completion, positivity before removing absolute values,
principal sqrt(2pi/A)=a sqrt(2pi/B), t>0, the Mills-bound direction,
819200<894645 and 15/8-33/20=9/40. Require the proof to cover both
closed boundaries, both signs of h, h=0 and unbounded u without a
sample or endpoint heuristic. Correct any actual mathematical failure;
do not treat a failed sufficient estimate as a counterexample to T_G.

The downstream use is a verified separate finite Gaussian component.
Global tails, continued endpoint, Mellin assembly, quotient/inversion,
certificates and sufficient Xi signs remain unresolved. No cross-notebook
input or full matching Mathlib coverage is asserted. This ordinary
normalization and scalar-inequality replay is routine_audit; the local
tail calculation offers no justified creative central sign mechanism.

## Step520 direct-source repair and comparison

LITERATURE_REASON: The supervisor reported missing direct source URLs in
this ready audit assessment; this bounded reinspection repairs that
specific evidence field rather than extending the target or repeating
discovery. The step518 overlap/failure assessment remains applicable.

Directly inspected the live NIST DLMF pages on 2026-11-05:
[7.7.6](https://dlmf.nist.gov/7.7.E6), equation and attached hypothesis;
[7.8.1](https://dlmf.nist.gov/7.8.E1), definition; and
[7.8.2](https://dlmf.nist.gov/7.8.E2), inequality and attached domain.
The site serves the equation permalinks within sections 7.7 and 7.8.
These are the live web edition, identified by equation numbers and
access date; no release number was established in this reinspection.

Equation 7.7.6 integrates exp(-(a t^2+2bt+c)) from real x to
infinity, with Re a>0, and prints the factor (1/2)sqrt(pi/a),
exp((b^2-ac)/a), and erfc(sqrt(a)x+b/sqrt(a)). Equation 7.8.1
defines M(x)=exp(x^2) integral_x^infinity exp(-t^2)dt. Equation
7.8.2 gives M(x)<=1/(x+sqrt(x^2+4/pi)) for real x>=0,
along with a lower bound not needed here. These match the imported
statements in L800; no large-argument or complex-sector condition
is attached to the selected real Mills bound. This confirms source
coverage, not the correctness of L800's application or constants.

For the future audit the proposed substitutions remain a=B/2,
b=c=0, real x=d, and real Mills argument d sqrt(B/2).
L798's hypotheses and (5)–(7) are the local places to check positivity,
curvature and branch normalization. No substitution proof or new bound
is established in this literature-only turn. NIST supplies the generic
identity and tail bound, not the moving-domain 2.35/1.65 comparison;
SPECIALIZE and REPRODUCTION therefore remain the appropriate gate
and future classification. The exact uniform specialization and all
closed-boundary cases remain for the saved audit.

Paper23 was not retrieved again: its role here is only the already
inspected budget provenance, not a theorem imported to prove the
allowance. Its supplementary derivations and NIST's cited original
Mills references remain unread and are not premises. Mathlib matching
coverage remains unchecked. No lemmas, mathematical scripts, DAG or
proof overview were changed. This is an honest process repair with
no new mathematical evidence or advance toward RH.
