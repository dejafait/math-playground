# Integrated full-period curvature rows: one feasibility test2267

TARGET: Test the nonnegative-full-period-row sufficient premise for first-zero curvature by deriving its signed double-integral representation and deciding the eventual sign of the distant rows R_j(1) for C919s's quartic kernel and its certified first positive cosine zero.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Source comparison2267 searched signed sine-transform curvature, determinant integration, period comparisons and stronger preservation results; no matching row-sign theorem was identified. Local2254/2257/2260/2234 and C919s/t/u were checked for overlap and failures; no novelty follows.
SOURCE_EVIDENCE: Direct sources https://arxiv.org/pdf/1806.10411v1 ; https://arxiv.org/pdf/1606.05011v1 ; https://doi.org/10.1017/S0004972700047511 ; https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf ; https://terrytao.wordpress.com/2009/01/01/245b-notes-0-a-quick-review-of-measure-and-integration-theory/ . Forrester arXiv:1806.10411v1 equation1.7 and Section2.2 proof, pp2,4, and equation2.4 p5; Tuck2006 pp133-135 equations1-4 and complete half-period proof; Dimitrov-Xu arXiv:1606.05011v1 Theorems2.5-2.6/proof pp5-6 compared but not imported. Exact sources, reading qualifications and reusable Conrad/Tao integration hypotheses are in 2026-11-21-signed-curvature-source-notes-2267.md.
COMPARISON: This tests integrated signed rows, allowing cancellations within a period and in the other variable. C919t's failed pointwise joint-density premise and C919u's stationary source derivative are not assumed; C919s's marginal curvature at1 does not decide individual rows.
GAP: The determinant representation, absolute convergence, period decomposition, sufficiency of the proposed rowwise condition and the distant-row sign are unproved. No generic curvature theorem or actual-Xi bridge is available.
REASON: An analytic distant-period sign test can reject a stronger cancellation-aware criterion before attempting its infinitely many inequalities; the tested row sign is not the total determinant sign restated. This is a bounded feasibility test, not approval of a new theorem.
SCOPE: One analytic eventual-sign test for the fixed quartic at u=1; no parameter search, new numerical marginal-point certificate, generic invariant, perturbation family, actual-Xi application or iteration. Separate next-turn source approval is required before research.

## Definitions for the proposed test; no identity asserted

Use K(v)=exp(-v^4-v^2) and the least positive cosine zero x of
C919s; import its root bounds, positivity/regularity of G and explicit
arithmetic contracts only where used. Set a=pi/x. For u,t,s>=0 define

    A_u(t,s)=K'(u+t)K'(u+s)
       -(K''(u+t)K(u+s)+K(u+t)K''(u+s))/2.

The proposed row, subject to later integrability verification, is

    R_j(u)=integral_(2ja)^((2j+2)a) integral_0^infinity
                  A_u(t,s) sin(xt) sin(xs) ds dt,  j>=0.

The candidate sufficient premise is R_j(u)>=0 for every j and u.
Its use would require proving the prospective identity
(G')^2-GG''=x^2 sum_j R_j(u), including all absolute-convergence
and differentiation hypotheses. That identity and the implication
are NOT derived or asserted as results in this literature turn.
Forrester is a general algebraic comparison, not an exact matching
representation theorem. A direct product/Fubini justification, if
valid, is the necessary specialization; no reproof of Fubini is needed.

## One bounded test and decision threshold

After separately approved research begins, justify those interfaces
for the fixed model and decide the sign of R_j(1) for all sufficiently
large integers j. Seek an analytic strict sign with a valid remainder
bound or an explicit tail threshold; no floating point samples suffice.
Keep x at its certified actual zero, with the full bracket whenever
uniform estimates need it. Do not select a convenient nonroot.

A proof that R_j(1)<0 eventually stops the nonnegative-row premise,
while leaving the total curvature and generic preservation undecided.
If eventual nonnegativity is proved, record that limited feasibility
result and assess the remaining rows separately. Failure to control
the remainder is inconclusive; preserve it and do not repeat the same
asymptotic mechanism without a new estimate. No claim about the sign
has been evaluated in2267. The stronger premise is unpaid, but has
this test independent of proving the marginal sign itself.

Essential local input: C919s. C919t/u are failure comparisons only.
Generic K positivity, smooth even extension, quotient interpretation,
actual-Xi, iteration and all-degree transfer are not consequences of
this fixed test. Full matching Mathlib coverage is unchecked. No
cross-notebook input. This is ordinary signed-integral development,
not a justified creative central mechanism or a complete RH candidate.

## Source-link recovery2268 (21 November2026)

This literature-only review repairs the missing direct URLs in
SOURCE_EVIDENCE. The exact TARGET, EXPLORE decision and bounded
mathematical scope are preserved. Source approval is completed here;
research waits for the supervisor to accept the repaired assessment.
No identity or sign has been derived in this recovery step.

Reopened Forrester v1, Section2.2, printed p4: the proof expands a
determinant and integrates rows; it supplies no oscillatory sign.
Reopened Tuck, pp133-135, especially p134 equation(4) and its full
half-period comparison proof: convergence and decreasing amplitudes
are essential. This is a comparison, not an import for A_u.
Reopened Dimitrov--Xu explicitly version1: Theorem2.5 and its proof
are on printed p5, and Theorem2.6 with its discussion is on pp5-6.
The moment hypotheses concern frequency derivatives; positive
definiteness supplies no pointwise row sign. No normalization or
strictness assertion is imported. These version1 locators supersede
any ambiguous version/date reference for this recovery.

Reopened Conrad Theorem12.3, printed p16: continuity of the integrand
and its parameter derivative in a neighborhood, plus parameter-uniform
integrable bounds for both, are required; infinite endpoints are allowed.
Reopened Tao Theorem4(1)-(2): sigma-finite measure spaces and product
measurability are required; signed Fubini requires absolute integrability.
The fixed-model research must verify those hypotheses and period
summability. No new theorem search is needed for this unchanged target;
the duplicate/failure comparison and wider search2267 are reused.
Full matching Mathlib coverage remains unchecked. The main-gap bridge,
finite rows, generic kernels and iteration remain unresolved.
