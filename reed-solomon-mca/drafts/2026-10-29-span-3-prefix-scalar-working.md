# Span-3 scalar test — step 549 working checkpoint

Approved target: test universal row-0 scalar vanishing on the exact-rank-one
locus of actual prefix (0,51,98), with saved completeness and no new block
rank tests. Reuse the invocation-start SPECIALIZE assessment
`literature/2026-10-29-span-3-prefix-scalar-test-review.md`.

Main gap: uniform twelve-row exclusion for an unspecified pair. A prefix
exclusion could inform later gate-aware cover work, while representation,
challenge equivalence and all other prefix obligations remain open.
Continue only after a homogeneous proof and independent coefficient/input
checks; a rank-one survivor with nonzero scalar rejects this mechanism.

Inspected all six saved span-3 vectors and all three actual transition
records. The basis consists precisely of e_1 wedge e_x for x in
S minus {1}. Thus p=e_1 wedge w with w_1=0, all six other coordinates
arbitrary. Nonzero p gives independent e_1,w and their unique plane.
Original Q_0 e_1=0. If its restriction has rank one then Q_0 w is nonzero,
so the recovery line is E e_1 and lambda_0=h_12/44=0. Rank zero must be
retained and rejected by L109, not divided away. No other row map is
needed to prove this implication on the smaller three-gate locus.

Completed: all 27 coefficient/provenance checks pass, including 126/126
basis entries and 3/3 actual transitions. Full proof is canonical in
`lemmas/L173-span-3-prefix-universal-row-zero-scalar-obstruction.md`;
certificate: `scripts/span-3-prefix-scalar/certificate.json`. Saved
elimination is reused, not recomputed or audited. No cover modification
or pruning. A separate critical audit of L173 is still pending.
L172 and L115 are comparisons, not premises. L109 necessity alone is
used; its r>=6 converse is unavailable. Preserve original coding weights,
chart and finite-certificate qualifications. Discovery is due; this
specialization supplies no new central mechanism by itself.
