# Capped rational-kernel proof audit — source coverage approved

TARGET: Critically audit L102's capped rational Taylor kernel enclosure proof, including uniform radius, constant and coefficient rounding, full-product integration, and finite replay-cost bounds.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the queries, stronger-method comparison and failure/duplicate record in drafts/source-notes/2026-10-21-rational-kernel-source-review.md and drafts/literature/2026-10-21-rational-kernel-plan.md; searched the specific 2026-10-21 assessments and history/39* for a completed duplicate audit, then read the complete L102 and needed L031/L101 passages. Exact audit-scope comparison is recorded in drafts/source-notes/2026-10-22-rational-kernel-audit-coverage.md.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15): https://dlmf.nist.gov/1.4.vi equations 1.4.35--37 (C^(n+1) hypothesis and both remainders); https://dlmf.nist.gov/1.4.v equations 1.4.26/28/29; https://dlmf.nist.gov/4.6 equations 4.6.1/4; https://dlmf.nist.gov/4.7 equations 4.7.3/7/8; https://dlmf.nist.gov/4.8.E2 principal-log additivity; https://dlmf.nist.gov/4.8.E16 exponential product law. Step 401 reconfirmed the Taylor and exponential-product primary passages and URL resolution; reuse the step-400 source-case map and prior inspected 4.2.19, 4.7.10 and 1.2.11, with L031 endpoint rules and audited L101 definition/contract.
COMPARISON: The inspected sources cover the smooth positive-real Taylor/integration and scalar identities used throughout L102; exact endpoint rules and finite algebra supply the remaining audit framework. They do not state L102's uniform rounding, radius or operation-count conclusions. These must be independently checked as fixed known-method specializations; no reproof of the imported theorems or numerical execution is needed for this audit.
GAP: Essential source coverage for this exact proof audit is now sufficient. L102's claimed constants, complete rounding/convolution/integration bounds and endpoint-operation count remain unaudited; no actual parameter, kernel or derivative certificate exists.
REASON: A separate literature-only comparison now maps every proof section to inspected inputs and distinguishes theorem applicability from the unverified quantitative specialization; proceed to one critical audit under the unchanged caps, not implementation.
LITERATURE_REASON: Step 401 is the supervisor-required repair of missing direct source URLs in this ready assessment; the exact audit target, hypotheses, SPECIALIZE decision and prior source-case comparison are unchanged. No additional mathematical approval or discovery is claimed.
SCOPE: One proof-only audit of L102 for rational c_* in [3/10,1/2], n=1,...,128, the fixed 1016 panels of length 1/8, degrees 128+64+64 with complete product degree <=256, scalar series <=256 terms, <=16 exponential squarings and outward grid 2^-256; no implementation, cap enlargement or derivative evaluation.

The separate source approval is complete; the mathematical audit is not.
The detailed source-case map and remaining audit obligations are in
`drafts/source-notes/2026-10-22-rational-kernel-audit-coverage.md`.
Essential numerical inputs are L031's
exact endpoint rules and L101's finite-kernel definition/contract.
The downstream analytic premises remain L030, L031's independent
coefficient/sign and elementary parameter rules, audited L099 and
foundations/02 through L101. Exclude L035/L100, published basis/Sha
premises, the unavailable library and the unread optional Taylor-model
paper from the proof's inputs.

The discriminating audit is containment and radius under exactly 1016
panels of length 1/8, degree <=256, scalar series <=256 terms, <=16
squarings and grid 2^-256. Check both scalar remainder/enlargement
errors, all coefficient recurrences, convolution signs/full slots,
analytic integration and summed radius <2^-183<=2^-50. Also distinguish
endpoint operation count from arbitrary-input bit complexity and any
unproved practical resource claim. Failure retains the actual failed
bound and parks these caps; no enlargement or implementation occurs
in that audit. Success only validates a numerical plan, not actual
kernels, L'' nonvanishing or BSD. Mathlib remains not checked.

## Step 401 — direct-source URL repair

2026-10-22. The ready assessment's SOURCE_EVIDENCE field omitted direct
URLs even though the step-400 source note contained them. Added the
primary links above. Opened DLMF 1.4.vi and 4.8.E16 and confirmed their
resolution to sections 1.4 and 4.8; inspected the Taylor hypothesis and
equations 1.4.35--37 and the complex-variable identity 4.8.16. The
reported online version remains 1.2.8, released 2026-09-15. All other
source cases are reused from step 400, not newly reread or reapproved.

This is a STALLED literature metadata repair, not an advance in source
coverage or mathematics. The unchanged SPECIALIZE assessment permits
the saved audit next turn; no audit, new bound, lemma or execution has
been performed. The numerical threshold and exclusions above remain.
