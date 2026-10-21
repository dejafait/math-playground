# Step 186 — fixed released-zero witness, reanchored principals

Approved target: Test whether L056's fixed shell witness satisfies every reanchored three-index conditioned principal matrix on its represented triples.

Gate: `drafts/literature/2026-10-12-released-zero-reanchored-principals.md`,
unchanged SPECIALIZE; actual work is calculation / REPRODUCTION.
Inputs: L053 fixed positive rho and all p_i; L054 eight regions;
audited L056 exact 21 z coefficients, valency normalization and
represented unordered consistency. No new coefficients or zeros.

Main gap: arbitrary-center safety at 68 agreements (and independently
67 agreements). The test decides whether this fixed shell optimizer
can survive necessary three-index PSD before larger coupled work.
Continue only on a complete pass; any negative minor rejects this
fixed witness alone. Larger other-anchor/cross-shell PSD, unrepresented
triples, actual-label zeros, full SDP bound, measures and RS realization
remain open. The 955–957 boundary is unchanged.

Existing comparisons: ATTEMPTS/035–038 have no verdict on these
reanchored matrices. Known union-matrix and Schur tools are imported
with the precise citations in the approved assessment and L053.

Execution scope: reconstruct all 36 relations as complete point sets,
all six support permutations, remove repeated union indices and test
every principal minor over the rationals. Save all matrices, values,
minor signs and any failures, including singular cases.

Completed: PASS on all 216 represented ordered matrices, with 1488
nonnegative minors (224 zero), plus 31 Boolean-closure matrices with
91 nonnegative minors. Constructor: 1170 reconstruction checks;
independent serialized-value verifier: 5435 checks, all 1579 minors,
no failures. Canonical result: L057; complete certificates under
`scripts/finite-support/released-zero-reanchored-{results,verification}.json`.
The verifier initially had a line-continuation syntax error, corrected
before execution; no mathematical check failed. A documentation update
initially stopped on a case-sensitive replacement assertion; it was
corrected before checkpointing. Separate critical proof review remains
pending, with a new REVIEW_REQUIRED assessment.
