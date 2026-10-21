# Conditional pair-link witness test — working checkpoint

Approved target: Determine whether L028's averaged lift extends to graph-link theta bodies with both determinant-link edges and pair-conflict edges.
Prior assessment: drafts/literature/2026-10-06-conditional-pair-link-obstruction-test.md (EXPLORE).
Inputs read: L027, L028, foundations/07-core-conditioned-theta-source.md; ATTEMPTS/010 and ATTEMPTS/019 retained.

Main gap: arbitrary-center 68-agreement safety; fixed bracket 955–957.
Test: certify all strengthened rows, or exclude one actual row. Feasibility stops this repair for the fixed witness; exclusion only motivates a separately assessed global-cap test.

Construction to verify: fix C,A; the outside set has 956 points. Identify an abstract 955-point subset with {0,...,4} x F_191, with one spare point. Inject the 21 pairs U of A into the 191 slopes. For each U and b in F_191 use the vertex U union {(x,s_U*x+b): x=0,...,4}. Within U the outside parts are disjoint; across distinct U they meet at most once. Consequently all these 21*191 vertices avoid pair conflicts and determinant-link edges, independent of actual labels. Average only bijections of the abstract outside points to the actual outside set, then restrict every independent set to original W_A. Each actual vertex in W_A has probability 191/binomial(956,5). Thin the mixture by 136/191, with remaining mass on the empty set, to recover tau=136/binomial(956,5) exactly.

Pending: check primality, intersection cases, exact probability, singular/empty-link qualifications and arithmetic. No conclusion asserted by this working checkpoint. Separate assembled-model soundness and any new global-cap target remain outside approved scope.

Completed: all pending construction and arithmetic checks pass. Full proof
is canonical in L029; do not treat the tentative paragraph above as an
independent proof. NEGATIVE for this repair, with no change to the radius
bracket. Exact finite audit and the complete inspected relevant fields
are in scripts/finite-support/conditional-pair-link-results.json.
