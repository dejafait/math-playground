# Rational centred-moment replay — source-gate-reviewed specialization

TARGET: Implement and test a dependency-free rational interval replay of both natural-index walls and all 151 complete-support M32<81/4 leaves, using the saved L960 reduction and certified series/quadrature bounds.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step138 completed the changed-method search and package/source comparison in drafts/literature/2026-11-10-centred-moment-rational-coverage-137.md; reuse it unless the method or hypotheses change.
SOURCE_EVIDENCE: Direct primary sources inspected in step139: https://arxiv.org/html/0708.3721 (v1, III, Propositions 9/10/12); https://dlmf.nist.gov/3.1#ii; https://dlmf.nist.gov/3.5#ii (3.5.6–8); https://dlmf.nist.gov/4.6.E4; https://dlmf.nist.gov/4.2.E19; https://dlmf.nist.gov/4.24.E3. Reuse step135 for Planat–Raymond v1 Theorem 3.3 and L960 for the saved reduction.
COMPARISON: Known algorithms cover the arithmetic mechanism, while Planat–Raymond v1 Theorem 3.3 states the desired inequality; independent finite specialization is justified reproduction, not a new moment theorem.
GAP: Prove finite truncation and endpoint/derivative-error specializations, verify the implementation, and execute all gates with certified leaf upper bounds below 81/4; cost and success are unknown.
REASON: This replaces the parked flint-dependent evaluator using inspected primary algorithms. Step139 separately reviews the saved continuation and repairs missing direct URLs without changing its target, hypotheses or execution contract; no dependent derivation or code runs in that literature-only approval turn.
SCOPE: Full source rectangle/natural-index convention; exact 151-leaf recurrence C=690988 to H=3100000; K=128,a=98/625,T=1/5,X=6000000185827,W=120000000000000; same eight global and six per-leaf gate families as step135, plus separately recorded arithmetic/error checks.

Read the completed comparison for direct citations and qualifications.
Essential inputs are L960's step136 partial reduction and the step135
domain/leaf contract. L019/L058 concern downstream normalization only.
Preserve the incomplete Arb script and all certificates.

The bounded work is one standard-library implementation and rigorous
attempt at these finite inequalities. First save enclosure definitions and
finite-error proofs canonically, with cited inputs and Mathlib qualification.
Use exact rational endpoints; prove outward inclusion if rounding to dyadics
for cost. Check denominator/sqrt/log domains, exp positivity, series
truncations, absolute-value cases and lower/upper parity. Use the inspected
NIST formulas where the printed source branches are suspect. Do not assume
the author's numerical margin or claim a PVS-verified port.

Apply the cited Simpson rule to the saved real integral with justified
endpoint transformation/enclosure and complete fourth-derivative bounds.
These specializations are future proof obligations. Retain the full 128-term
prefix, n=1, exact n=32, both walls, all shared closed endpoints and auxiliary
integral positivity gates. Recheck cover and gate count; new error checks
must not replace any original obligation.

Use a finite first-attempt budget: at most 60 seconds per yielded run,
4096 quadrature subintervals per leaf initially, and 256-bit outward endpoint
precision initially. These are resource limits, not sufficiency claims.
Record truncations and actual errors. Save partial certificates before
lengthy work and report exact unpaid gates/cost if the budget is inadequate.
Full rational certificates must include inputs, enclosures/errors, every
leaf upper bound, thresholds and failures. Print compact summaries and
inspect complete load-bearing evidence.

Continue only if both walls/all leaves pass and max certified upper
endpoint<81/4. A definite failed inequality parks this reduction; interval
overlap is inconclusive. Infeasible denominator/mesh growth or unjustifiable
endpoint handling parks this implementation pending a materially different
test. Source coverage does not promise numerical success.

A pass pays one L960 premise only. Remainder/derivative, companion,
phase/support, stable model/modulus, initialization/recovery, seams/exterior,
zero-time and L030–L032/C032a signs remain unresolved. Mathlib unknown;
no cross-notebook input. Proposed task: implementation, standard/high,
REPRODUCTION. No creative central mechanism or RH candidate is claimed.

## Separate source-gate review, step139 (2026-11-10)

Decision remains SPECIALIZE. This is approval of the existing target's
coverage, not certification of its arithmetic or an extension of scope.
The direct URLs above were opened; theorem-level passages were inspected,
not merely search snippets. Reuse the completed step138 comparison for
searches, package limitations and printed-formula cautions; no new novelty
search is warranted by a URL-only repair.

[Daumas–Lester–Muñoz v1](https://arxiv.org/html/0708.3721), Section III,
Propositions 9 and 10 cover inclusion and endpoint comparisons; division
requires a zero-free divisor interval. Proposition 12 covers elementary
function inclusion, with nonnegative square-root and positive logarithm
inputs. This licenses a method, not an unexamined Python port or a claim
that PVS has checked that port.

[NIST interval/rational arithmetic](https://dlmf.nist.gov/3.1#ii),
Sections 3.1(ii–iii), equation 3.1.6, specifies inclusion operations,
appropriate endpoint rounding and exclusion of zero from divisors.
Exact integer-based rational operations or justified outward rounding
remain implementation obligations.

[NIST Simpson rule](https://dlmf.nist.gov/3.5#ii), equations 3.5.6–8,
references Davis–Rabinowitz (1984), pp.57–58. The composite rule uses an
even subdivision count and a fourth-derivative remainder. Application
requires C^4 regularity on the actual closed integration interval and a
uniform fourth-derivative bound. Variable endpoints and parameter intervals
are not resolved by the citation. Preserve the saved affine-endpoint/error
obligation; no derivative or finite error bound is derived in this review.

[NIST logarithm series](https://dlmf.nist.gov/4.6.E4) covers positive real
inputs. [NIST exponential series](https://dlmf.nist.gov/4.2.E19) and
[NIST arctangent series](https://dlmf.nist.gov/4.24.E3) supply the stated
series; the latter covers the real Machin arguments 1/5 and 1/239.
Finite remainder bounds, range reduction, parity and positivity before
reciprocation remain the future specialization, using the named
alternating-series theorem where applicable. No new remainder formula
is asserted here.

The original theorem/domain assessment is
`2026-11-10-centred-moment-independent-audit-135.md`, with direct
[Planat–Raymond v1 source](https://arxiv.org/html/2611.06245v1#S3) and
pinned checker URLs. It is reused, not independently reaudited in step139.
L960's partial reduction, not the cited theorem's PASS label, remains the
local consumer. Steps136–137's missing-flint stops are retained; this review
neither repeats installation nor executes the unfinished evaluator.
The complete-success/definite-failure/inconclusive tests above are unchanged.
Mathlib matching coverage remains unchecked.
