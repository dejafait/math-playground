# Weighted tilted-Pollaczek convergence assessment2003, completed2004

TARGET: Determine whether Kuznetsov's Jensen-weighted tilted-Xi Pollaczek truncations converge locally uniformly on C to exp(-pi*t/4)Xi(t), with the exact normalization and hypotheses.
CHECKED: 2026-11-20
DECISION: IMPORT
SEARCH_EVIDENCE: Exact Kuznetsov convergence/normalization and Banach Silverman-Toeplitz searches; scoped Pollaczek duplicate/failure checks reused2000/2001/2003. Queries and actual reads in convergence-source-review2004.
SOURCE_EVIDENCE: Kuznetsov2008 DOI10.4153/CMB-2008-055-0 p561 definition, Theorem2.1/proof pp563-564, Remark3 p565 and exact weighted assertion p568 inspected; Parise arXiv2302.06770v2 Sections2/4.9/5.1-5.2, Theorems5.2/5.5 and complete sufficient proof inspected. drafts/literature/2026-11-20-tilted-pollaczek-convergence-source-review-2004.md
COMPARISON: The source explicitly states the exact all-C weighted compact limit with the requested normalization. This is known, not a new convergence claim; ordinary Theorem2.1 and Banach summability cover a route to explicit applicability without coefficient asymptotics or root-preserver hypotheses.
GAP: No source gap for the stated limit remains; finite summation-by-parts and endpoint checks are a separate known-result specialization, not performed2004. Uniform nonreal-root bounds, multiplicity and Xi transfer remain open.
REASON: Import the exact source statement; avoid a new asymptotic proof. Newly nominated standard applicability check gets separate approval before research; degree24 runtime route remains parked.
LITERATURE_REASON: The scope changes from finite degree24 inertia to weighted compact convergence; source-notes2000 explicitly leaves the relevant asymptotic convergence inputs and upstream [7]/[9] unread.

Completion2004: exact statement, hypotheses and sufficient proof coverage
are recorded in [source review2004](2026-11-20-tilted-pollaczek-convergence-source-review-2004.md).
The remainder preserves the original nomination and its then-open questions;
these are not renewed source-access instructions.

The exact family nominated for assessment was

    T_N(t) = sum_(k=0)^N [N!/((N-k)! N^k)] beta_k p_k(t), N>=1,
    p_k(t)=P_k^(3/4)(t/2;pi/2),

with Kuznetsov's beta_k from (4)/(13), renamed as in source-review2001.
The intended limit is the source's exp(-pi*t/4)Xi(t); confirm the Xi
definition and all scalings from the primary text rather than assuming
the normalization. Do not drop odd terms or replace beta by C028b's
coefficients. The exact family and proposed limit are a question for
review, not an established identification.

Start with the publisher paper's exact convergence statements, their
proof cases and the weighted remark. Follow only references essential
to their applicability. Existing local source-notes2000/source-review2001
can be reused for finite formulas but not promoted to asymptotic
coverage. Compare ordinary and weighted convergence without silently
transferring one to the other. No fresh calculation is authorized by
this nomination.

Continue if an inspected theorem covers the exact family on every
compact subset of C, or identifies a specific remaining estimate with
a justified downstream use. If it covers only the real axis/a strip,
uses incompatible normalization, or leaves an essential tail estimate
unproved, record that difference and keep the compact-limit gap open.
Do not assert a negative mathematical result merely from source access
failure. Uniform negative index, multiplicities and Xi symmetry transfer
remain separate even if convergence is imported. Mathlib is unchecked.
