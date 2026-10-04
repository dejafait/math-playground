# 2026-10-04 — Two fixed coefficients: three unsafe-grid certificates

Completed one mathematical attempt on the unchanged saved SPECIALIZE
target. Reused its inspected scalar coefficient dictionary and collision
coverage; no new literature work or optional source retrieval was performed.
All prior changes, lemmas, scripts, outputs and inactive branches remain.

[L013](../lemmas/L013-two-leading-coefficient-fibers.md) identifies the
entire k+2-agreement list at one two-coefficient center with its joint
subset fiber, including ambient-extension messages and every m>=1.
Partitioning subsets into 65537^2 source-field coefficient pairs supplies
an attained existential list of at least ceil(binomial(1024,k+2)/65537^2).
At rates 1/2,1/4,1/8 it exceeds the actual ambient threshold, giving
t_star<=509,765,893 respectively, one grid point inside C012a's bounds.
These certificates do not compute the maximizing pairs or full-code lists.

At rate 1/16 the same lower certificate is below 2^317 while the threshold
exceeds 2^320, so the proposed lower-certificate test fails for that rate.
The existing t_star<=958 remains. Preserve this informative limitation in
[the attempt record](../ATTEMPTS/004-rate-sixteenth-two-coefficient-averaging.md).
It proves neither safety nor an upper bound on actual joint fibers.

The proof uses an elementary block-selection lower bound for the three
successful rates, an exact factorial upper comparison for the remaining
rate, and C012a's field/order and threshold facts. Computational checks
corroborate its integer comparisons and sharper per-rate brackets. On a
small proper subgroup, candidates were independently reconstructed by
interpolation, with selected scalar and width-two lists exhausted. Results
are in [the saved output](../scripts/coefficient-fibers/two-coefficient-results.json).
No 1024-point joint fiber or ambient extension field was enumerated.

Outcome: ADVANCE, a relevant local threshold/application input; STEP_KIND:
RESEARCH; classification: REPRODUCTION. The scalar mechanism is known,
and no advance beyond the checked literature is claimed. Exploration
turns used remain 0/3 after this advance. No complete candidate appeared;
STATUS remains IN_PROGRESS. Arbitrary-center upper bounds, sharp boundaries,
general interpolant coverage and the ABF26 comparison remain missing.

The next direction is a uniform quantitative upper comparison on the
unresolved rate-1/16 joint fibers. That could stop this particular center
family, while leaving the full-code boundary open. Its changed conclusion
is outside the prior collision-only SCOPE, so the
[pending assessment](../drafts/literature/2026-10-04-rate-sixteenth-joint-fiber-upper-bound.md)
is REVIEW_REQUIRED. No second mathematical step was attempted here.

The ID-only DAG adds only L013's genuine uses of L001 and C012a. The
overview and sole current checkpoint record the sharper bounds and the
one pending target. Exact-arithmetic and independent interpolation checks
passed. The required command
`PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with 15 nodes and 14 edges; `git diff --check -- .` passed. Unique
completed-step fields, prior ready coverage and the exact pending target
match passed. The checkpoint has 14 lines and the overview 99. Structural
validation cannot certify mathematical correctness; the two new graph
inputs were reviewed against their explicit mathematical uses.
