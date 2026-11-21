# Fixed gamma midpoint node approximation: source nomination1698

TARGET: Assess a fixed rational-coefficient approximation to C033b's exact 4096-node gamma midpoint sum with uniform error at most 1/64 for 1<=sigma<=2 and |w|<=2, retaining the prescribed nodes and panel count.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1699 searched active literature/ATTEMPTS/foundations for gamma with node/Taylor/rational-approximation terms, inspected C033b and assessment1614/stop1616, and searched primary complex Taylor remainder and exact gamma-midpoint rational4096 terminology; no matching certified node formula was located in this bounded screen. No novelty inference.
SOURCE_EVIDENCE: https://complexanalysis.org/web/sec_taylor-series.html Theorem7.2.3, Lemma7.2.2 and complete proof through(7.2.7); https://complexanalysis.org/web/sec_convergence-theorems.html Corollary4.3.3 and proof via(4.3.4); NIST DLMF1.2.8 https://dlmf.nist.gov/4.2#iii equations4.2.19/22 and https://dlmf.nist.gov/4.28.E2; inspected statements and relevant proof cases recorded in source-notes1699.
COMPARISON: Known complex Taylor remainders and rational exponential coefficients cover the generic approximation tools; C033b already supplies the positive-real reciprocal bound. These do not supply a truncation degree, perturbed-denominator certificate or propagated4096-node error. Retain C033b's audited exact-node quadrature without reopening it.
GAP: Specialize the imported remainder to the actual argument ranges, choose fixed finite degrees, verify rational coefficients and separated approximating denominators, and propagate full-domain node-sum error<=1/64. No such formula or bound has been established in this literature turn.
REASON: Essential node-approximation source coverage is now available with direct primary URLs; proceed after separate continuation approval to ordinary specialization, not creative mathematics or a new RH mechanism.
SCOPE: Fixed rational-coefficient expression (a rational function is permitted) approximating C033b's prescribed exact sum only; real1<=sigma<=2, complex|w|<=2, n=4096,h=1/256, unchanged nodes. Taylor approximation of elementary factors, rational arithmetic and denominator perturbation accounting are covered; no floating-point stability claim.
COVERED_TARGET: Construct and certify a fixed rational-coefficient approximation to C033b's exact 4096-node gamma midpoint sum with uniform error at most 1/64 for 1<=sigma<=2 and |w|<=2, retaining the prescribed nodes and panel count.

Keep C033b's n=4096, h=1/256, v_j=(j+1/2)h, its exact
integrand I(v), and the entire existing sigma,w parameter set. A fixed
rational-coefficient expression in sigma,w is the proposed output;
the approximation target is h*sum_j I(v_j), not an adaptive quadrature
or a sampled parameter assertion. Distinguish approximation of the
symbolic function from any later floating-point evaluation of it.

First retrieve primary approximation/error statements and relevant proof
cases, then compare actual argument ranges and nonvanishing denominators.
Search specifically for existing certified gamma-node formulas and
recorded failures; reuse C033b's quadrature assessment without a new
quadrature audit. Import standard approximation results by citation and
reserve actual finite constants and specialization for a later research
turn under a separately approved exact assessment.

Continue only if a concrete finite approximation with a priori uniform
error accounting can be nominated. Abandon a sampled, adaptive or
unstated-precision substitute, or a formula whose denominator control
requires a zero assumption. No new formula is derived or approved now.
The proposed 1/64 is an intermediate component budget; its relevance to
the full evaluator still needs coefficient/error propagation. Pole,
prime and O terms, variation-2 residual<1/2, cancellation, unsmoothed
Xi realization and all-degree positivity remain open. Mathlib unchecked;
no cross-notebook input. This is literature_comparison, not creative work.

## Completed source review1699 — 19 November2026

The preceding nomination records the starting REVIEW_REQUIRED scope.
The fields above now record completed source readiness, not a derived
approximation. Full evidence and qualifications are in
[source-notes1699](2026-11-19-gamma-node-source-notes-1699.md).
The finite Taylor scheme is a concrete candidate for a priori certification;
its degree and constants are deliberately reserved for research. Import
the generic theorem by citation rather than reproving it. A rational
quotient of truncated elementary factors is within the nominated
rational-coefficient scope; a polynomial-only result is not required.

The next research step must bound every elementary-factor error before
forming the quotient and sum, with the smallest prescribed node included.
Use C033b's already proved real B lower bound as the exact-denominator
input; separately prove that the approximating denominator stays away
from zero. No complex mean-value theorem, sampled certificate or implicit
floating-point precision is permitted. Include w=0, |w|=2 and both sigma
endpoints. If these checks fail, preserve the first failed bound and
stop the particular construction without changing nodes or parameter set.

This newly ready continuation receives separate approval next turn.
No lemma, mathematical script, PROOF or DAG was modified1699.
