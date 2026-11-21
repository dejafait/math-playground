# Jensen-weight summability specialization2004

TARGET: Verify the Jensen-weighted convergence by applying Banach-space Silverman-Toeplitz to Kuznetsov's ordinary partial sums, including all endpoint weights.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact weighted-convergence/normalization and Banach Silverman-Toeplitz searches plus scoped Pollaczek duplicate/failure checks; queries and actual primary reads in convergence-source-review2004. No novelty claim.
SOURCE_EVIDENCE: https://doi.org/10.4153/CMB-2008-055-0 and https://arxiv.org/html/2302.06770v2 ; Kuznetsov2008 DOI10.4153/CMB-2008-055-0 Theorem2.1/(3)-(5)/proof pp563-564 and exact weighted assertion p568; Parise arXiv2302.06770v2 Sections2/4.9/5.1-5.2 Theorems5.2/5.5, Banach discussion and complete sufficiency proof. Exact links, assumptions and qualifications in drafts/literature/2026-11-20-tilted-pollaczek-convergence-source-review-2004.md.
COMPARISON: The exact limit is already stated by Kuznetsov. The necessary local work is solely finite summation-by-parts and verification of standard summability hypotheses in C(K), supplying an explicit applicability argument absent from the weighted passage. This is reproduction/specialization, not new mathematics.
GAP: Verify transformed rows, endpoints N=1/k=0/k=N and k>N zero extension, bounded absolute row sums, fixed-column decay and row-sum limit; conclude uniform convergence on arbitrary compact K from imported ordinary convergence. No coefficient asymptotic or uniform root bound is licensed.
REASON: Independently testable analytical task bypasses the parked Arb runtime and unnecessary upstream asymptotic retrieval. New ready continuation requires separate approval next turn; no specialization was derived in literature turn2004.
SCOPE: Exact T_N=sum_(k=0)^N N!/((N-k)!N^k) beta_k P_k^(3/4)(t/2;pi/2), N>=1; beta_k is Kuznetsov b_k from (3)-(4); ordinary compact convergence imported by Theorem2.1. Complex Banach-valued Silverman-Toeplitz sufficiency only.

Use full source review2004 and reuse normalization review2001. Preserve
odd terms and the exponential tilt. Apply summability to ordinary partial
sums, not individual terms. Import the named theorem; write only needed
finite weight checks and identification of the Banach norm and limit.
A short replay of its initial-segment/tail argument is justified only
if needed to make uniformity explicit; no reproof of the general theorem.

Continue if the exact finite identity and all row conditions hold for
every N>=1. Otherwise identify the failed condition and leave the
specialization unresolved. A pass supplies only the known compact limit.
Upstream9 proof verification is outside scope: ordinary Theorem2.1 is
an explicit imported input, not a local reproof.

Direct inputs are the two primary sources. L030-L032/C032a and
C028b/d/f/C029j identify unresolved context only. No RH, simplicity,
uniform one-pair count or realization of Xi jet laws is assumed. Later
zero transfer needs its own coverage. Mathlib coverage remains unchecked.
No mathematical script or runtime installation is needed.
