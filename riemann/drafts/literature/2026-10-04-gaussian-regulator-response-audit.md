# Gaussian regulator response — separate audit assessment

TARGET: Critically audit L366's moving-pole cancellation, shifted-completion response and uniform j=0,1,2 remainder on |ξ|≥40, ε(1+ξ²)≤1, checking the negative-line zeta bounds and contour differentiation against L357–L358 and L320.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged-hypothesis searches and source comparisons recorded in drafts/literature/2026-10-04-gaussian-regulator-response.md and the differentiated-gamma comparison in drafts/literature/2026-10-03-gaussian-regulated-first-spectrum.md; no new external search or novelty inference.
SOURCE_EVIDENCE: Paris, arXiv:1503.07329v1, §§1–2, (1.1), (2.1)–(2.6), Theorem 1 in §3.2, https://arxiv.org/html/1503.07329v1; NIST DLMF, 25.4.1–5, 25.5.13–14, 5.11.1–3/9–13 and §5.11(ii), 5.15.8–9, https://dlmf.nist.gov/25.4 and https://dlmf.nist.gov/5.11; previously inspected theorem/formula coverage and exact locators reused, not newly read external sources.
COMPARISON: The inspected sources provide scalar inversion and contour-residue tools, completion/reflection, and sector-controlled gamma estimates; Paris's fixed-real-exponent expansion is not a match for L366's growing complex exponent or coupled two-derivative bound. The audit must test the family-specific specialization rather than import its conclusion.
GAP: L366's claimed parameter derivative, shifted-completion normalization and regulator/frequency-uniform remainder have not received the scheduled independent critical audit; source sufficiency does not validate them.
REASON: A separate source-only recovery establishes prospective coverage of the exact audit action without changing the prior assessment during mathematics; sufficient supporting sources are already inspected and no essential unread source is identified.
SCOPE: Exact L357 family and L358 envelope A, real |ξ|≥40, 0<ε≤1/(1+ξ²), derivative orders j=0,1,2; critical audit of L366 only, including cancellation before differentiation and uniform bounds. No sign theorem, higher-level estimate, phase-return target or RH candidate is approved.

## Recovery and provenance

The supervisor reports that the preceding research invocation rewrote its prior assessment. Its appended audit COVERED_TARGET and same-target-audit paragraph are preserved as historical material; this turn does not rely on that addition as prior authorization of the preceding invocation. No attempt is made to backdate coverage or retroactively accept its outcome. The original derivation target, search record and inspected supporting results remain available for reuse.

This is a metadata recovery performed in a source-only turn. The exact audit now has its own assessment saved before any future audit invocation. The existing response assessment, L366 and all mathematical scripts remain unchanged. No new theorem, calculation, proof audit or source discovery occurs here. The outcome is STALLED as mathematics: a real process repair is not evidence of a new bound. The next invocation can reuse this SPECIALIZE assessment without editing it.

## Reused theorem-level comparison and locators

Paris, *The asymptotic expansion of a generalisation of the Euler-Jacobi series*, [v1 §§1–2 and §3.2](https://arxiv.org/html/1503.07329v1), printed pp. 1–5 and 8: (1.1) defines the series; (2.1)–(2.2) give inversion; (2.5)–(2.6) retain the finite-residue remainder. The recorded comparison reads real positive w with fixed parameters; Theorem 1 further assumes even positive integers w and p. It does not assert constants uniform for w=1/2+iξ as |ξ| grows. Retain the remainder; do not cite the theorem as the full statement of L366.

NIST DLMF [25.4.1–5](https://dlmf.nist.gov/25.4) supplies reflection and the completed xi definition; [25.5.13–14](https://dlmf.nist.gov/25.5#E13) supplies the theta integral and rational terms. These support checking the response's signs and factors, but do not establish cancellation of L358's subtraction or parameter differentiation under L357's kernel integral.

NIST DLMF [5.11.1–3](https://dlmf.nist.gov/5.11#E1), [5.11.9–13 and §5.11(ii)](https://dlmf.nist.gov/5.11#ii), and [5.15.8–9](https://dlmf.nist.gov/5.15#E8) give logarithmic/digamma/polygamma sector asymptotics, gamma modulus estimates uniform for bounded real parts, explicit remainder restrictions and fixed-shift ratio formulas. Sector hypotheses and the stated K=1 exception must be retained. L358's displayed shifted log-Stirling construction uses an analytic remainder and Cauchy's estimate for derivatives; a derivative of an uncontrolled O term is not supplied by these sources. A growing imaginary shift cannot be treated as a fixed-shift ratio.

These are supporting inputs, not a full match. The recorded DLMF version is v1.2.8 (2026-09-15); that version is inherited from the prior assessments rather than independently rechecked here. Referenced books and Paris's monograph remain unread leads, unused as essential inputs. Optional Mathlib extraction is not required for this audit.

## Relevance, redundancy and bounded test

The main unresolved claim is global actual-theta mixed positivity. L320's witness cutoff needs initial logarithmic and sublogarithmic Laguerre signs absent from L296. This audit concerns a useful intermediate approximation, with a later actual arithmetic sign margin and higher-level estimates still missing. It does not promise a complete passage to RH.

The proposed test is to examine each load-bearing passage of L366: the moving zeta pole cancels the full complex subtraction before frequency differentiation; the ε=0 derivative has a common weighted kernel majorant; the shifted-completion quotient retains its sign and normalization; horizontal contour edges vanish in the claimed domain; negative-line zeta bounds control two derivatives also where ξ+2v is near zero; Q's derivatives and the remaining integral have constants independent of ε and ξ. This lists audit obligations, not their resolution.

The recorded claimed remainder is C_j ε²(1+|ξ|)^4log^j(2+|ξ|), compared with the previous proposed test C_j ε²(1+|ξ|)^(9/2)log^(j+2)(2+|ξ|). Neither claimed upper bound is an actual sign margin; L366 itself states that the allowed upper regulator boundary gives no vanishing remainder. The audit must review that qualification along with the proof rather than count a smaller exponent as positivity.

Continue to downstream approximation only if the full claimed uniform bound survives or a precisely qualified useful correction is proved. Otherwise record the precise failure and stop or narrow this implementation. L357's absolute O(ε) estimate is already known and is insufficient at the gamma scale. L365's stopped fixed-regulator global-sign route and the retained common-threshold obstruction are not reopened or renamed. The response mechanism has one preserved prior mathematical attempt, whose reported outcome was process-rejected; this repair consumes no mathematical exploration turn and does not reset a budget.

## Mathlib

Full regulator-response/coupled-remainder statement: **not checked**. Supporting references retained in L357–L366 include [Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq) and [hasDerivAt_tsum_of_isPreconnected](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/SmoothSeries.html#hasDerivAt_tsum_of_isPreconnected). Their earlier supporting coverage concerns Poisson summation and smooth-series interchanges, not the full audit target. No absent theorem or originality claim is inferred.
