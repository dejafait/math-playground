# Step510 — independent C106a audit

Invocation-start SPECIALIZE coverage:
`drafts/literature/2026-10-26-c106a-row3-guard-critical-audit.md`.
The exact approved target is C106a's fixed-tuple row3 guard verdict.
Main gap: universal descent; intermediate purpose: decide whether to park
this particular full-guard witness without undoing L106's endpoint-only
counterexample. Continue only if all same-tuple identities, cut3 counts,
complementary products, enclosure operands and strict comparisons survive;
a defect requires correction, and inconclusive evidence leaves it unaudited.
No new guard, allocation, support search or realization claim is authorized.

Read the complete C106a and L106 proofs, L055 literal table and guard
definitions, L104's matching enclosure and its audit, construction script,
the relevant working note and Attempt034. Existing unfinished changes are
preserved. Source coverage is reused, not refreshed; no new source gap.

Independent paper check: the divided recurrence gives
`n_(i+k+1)/P_(i,k+1)=n_(i+k)/P_(i,k)+eta_(i+k)/P_(i,k)` at each successive
cut-relative step, so closing at cut3 gives exactly L106's numerator/D.
Inputs3,...,24 have k=0,...,21 with factors only3,...,23. Inputs0,1,2
have k=22,23,24 and complements {0,1,2},{1,2},{2}. Each complement
is multiplied by the reciprocal full product, exp(Lambda). No factor
growth is asserted for row24. All eta are positive and below23/11 by
L106's audited hypotheses. The same original coordinate s3 is tested.

Completed: independent transcription and finite evidence replay pass729
checks with no failures. Complete rows,25 prefixes, complementary products,
enclosure operands and rational bounds were inspected. C106a's verdict
is retained without repair, with the full audit in its canonical proof.
The fixed full-guard witness is parked; the other49 guards are untested.
L106's endpoint-only counterexample, L105 and unfinished work survive.
The newly proposed support-wide continuation has separate REVIEW_REQUIRED
coverage; no new mechanism was derived or tested in this audit.
