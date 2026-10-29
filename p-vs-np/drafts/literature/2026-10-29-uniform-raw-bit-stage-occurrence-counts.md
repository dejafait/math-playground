# Uniform raw upper-bit stage occurrence counts — source review required

TARGET: Derive exact occurrence counts for every fixed upper-bit raw stage at N=2^k and decide whether 2*sum_H g(H) <= C*S*(1+k) holds uniformly.
CHECKED: 2026-10-29
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Reuse the finite recipe's step-557/558 source and duplicate comparisons; no theorem-level search for this uniform raw-conjugation occurrence-count statement has been performed.
SOURCE_EVIDENCE: Mereb https://arxiv.org/pdf/2210.12913v1 §2 Remark 2 p.2 supplies binary upper Pascal factors; Arıkan https://arxiv.org/pdf/0807.3917v5 §VII pp.13–15 concerns arithmetic circuits. Exact versions and finite-scope qualifications are in drafts/2026-10-29-staged-dyadic-source-review-work.md and the prior finite-test assessment.
COMPARISON: L129 realizes the fixed raw recipe at N=4,8 with complete certificates, but its finite charges 601/2141 do not establish or reject a uniform bound. Arithmetic circuit size does not bound the sum of materialized occurrence graphs. This asks for graph charge only, before uniform central-map support.
GAP: Exact uniform nonzero counts after each ordered raw conjugation, cancellation cases including the fN boundary and all product connectors, and their summed growth remain unproved and outside the finite assessment's scope.
REASON: A source-only turn must compare this uniform count subtarget with known binary Pascal/shift conjugation results and the exact existing stops before approving any derivation. No uniform formula, obstruction or ready coverage is asserted here.
LITERATURE_REASON: The target moves from the approved finite N=4,8 construction to all k and an exact materialized-graph sum; essential coverage of that changed hypothesis is missing.
SCOPE: F₂, k>=1, N=2^k, original L122 endpoints with S=16N+20 and all original coordinates, upper E_u factors in increasing least-significant-bit order, raw C,D conjugation, one singleton occurrence per nonzero intermediate label entry, fresh s,t. Count both sides at every stage, including both terminal positions. This is not a new basis family, central-map optimization or general-operand claim.

The exact matrices and finite count tables are canonical in L129 §§2–5.
Reuse its complete finite evidence rather than running larger N as a
substitute for a uniform proof. Search standard terminology for binary
Pascal conjugation of a nilpotent shift, its nonzero pattern and explicit
stage factorization; retrieve primary hypotheses and relevant cases.
Compare Attempt 055's retained-register graph count, which concerns a
different graph organization and the stronger linear bound. Preserve all
earlier stops, including L117's arbitrary-operand invertibility obstruction.

The prospective downstream use is a necessary resource test for the
fixed staged unary fourth-comparison mechanism. Continue only if source
coverage allows an exact, independently checkable symbolic count or a
precise import. A superlinear ratio to S(1+k) stops this fixed raw recipe;
a bound only clears its graph-cost prerequisite, leaving uniform central
arrows and map support unresolved. Do not widen the basis or substitute
smaller endpoints to rescue a failure. Any new ready target receives the
required separate approval before mathematics. Full matching Mathlib
coverage is not checked. This file records a proposed continuation only.
