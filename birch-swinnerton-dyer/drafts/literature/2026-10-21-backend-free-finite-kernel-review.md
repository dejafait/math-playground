# Backend-free finite kernels — source comparison complete

TARGET: Assess whether published exponential/logarithm Taylor remainder bounds cover a backend-free rational enclosure of all 128 L101 finite kernels on [1,128] at the unchanged M=Y=128 and kernel radius at most 2^-50.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused analytic/duplicate/failure coverage and compared elementary finite Taylor remainders with the already assessed validated integrator; exact queries, inspected cases and unread Taylor-model leads are recorded in drafts/source-notes/2026-10-21-rational-kernel-source-review.md. No novelty inference.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), https://dlmf.nist.gov/1.4.vi equations 1.4.35--37; 1.4.26/28/29; 4.2.19; 4.6.1/4; 4.7.3/7/8/10; 4.8.2; 1.2.11, with hypotheses and finite-error cases inspected. Reuse audited L101 and L031's elementary exact interval rules.
COMPARISON: Published finite remainder and integration theorems cover the positive-path ingredients without an integration library; their numerical specialization to all kernels at radius 2^-50 is not a cited result. No new bound, algorithm correctness proof or kernel evaluation is established in this literature turn.
GAP: A complete fixed-plan error and cost proof, actual narrow parameter endpoints, coefficient replay, every kernel interval and final zero exclusion remain missing. The stronger Taylor-model paper's integration/arithmetic cases remain unread and are not inputs.
REASON: Essential theorem-level coverage is now sufficient for a separately approved bounded proof test. The unavailable-library route stays parked; source readiness is not feasibility or nonvanishing.
LITERATURE_REASON: Rational integration lies outside the ready complex-integrator contract; exact primary remainder hypotheses and error coverage are essential and unread, rather than another audit of the unchanged analytic tails.
SCOPE: Source comparison for the stated 128 finite kernels and unchanged threshold; supports only a subsequent proof of finite Taylor remainder, arithmetic and integration error under the proposed caps. No execution, parameter evaluation, cutoff change or achieved-width claim.

The main gap remains arbitrary-curve rank/order comparison for analytic
order at least two. The intermediate target is source coverage for a
backend-free finite integration certificate. If feasible, it could
support independent complex upper-bound evidence alongside L099 in this
known fixed case. L035 already supplies the order by citation; this
proposes changed provenance, not another BSD case.

Essential later inputs are audited L101, L030's exact model/conductor,
L031's independent coefficient/sign and elementary parameter rules,
audited L099 and foundations/02. Exclude L035, L100 and published
basis/Sha premises. Reuse the full analytic error 2^-43 and sensitivity
constant 200 without rederiving them during source comparison.

The [completed source review](../source-notes/2026-10-21-rational-kernel-source-review.md)
records the finite remainder, integration and positive-domain cases.
The proposed capped proof test is assessed separately in
`2026-10-21-rational-kernel-plan.md`. Its newly written continuation
requires separate next-turn approval. This review neither derives nor
self-approves the missing numerical specialization.

The proposed limits are the partition 1+j/8, j=0,...,1016, panel degree
at most 256, scalar series at most 256 terms, at most sixteen exponential
squarings and the 2^-256 outward dyadic grid. A proof must justify every
error and finite cost before implementation. Failure of its 2^-50 radius
test parks the plan without enlargement. Later actual kernel evaluation,
coefficient/parameter replay and L101's signed zero-exclusion test remain
separate work. Preserve width failures and zero-containing outputs.
Mathlib is not checked; no theorem beyond the inspected sources is claimed.
