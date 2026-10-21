# L057 critical audit — working record

Approved target: critically audit L057's complete triangle recovery
criterion, including all projected ranks, both-zero lifts, original finite
exclusions, zero recovered weights and all-eight-moment recovery.

The arbitrary L010 equality-family gap remains open. A correct L057 can
support simultaneous triangle counting; this audit does not attempt that
count. Continue only if every lost coefficient and every exceptional lift
is recovered without a rational original chart. A failed implication must
be recorded before counting.

Read the complete L057 and its prior derivation assessment, L010's kernel,
uniqueness and pointwise identities, L041's local converse and audit, and
ATTEMPTS/008–009,022–024. Reuse the supplied SPECIALIZE audit assessment;
no new source discovery is required. Existing unfinished work is retained.

Initial symbolic checks: (16) has the correct alpha signs and scale;
mu=-rho(1-t)/((1-rho)t) has inverse t=rho/E with precisely the listed
finite exclusions. The eliminated columns have rank m; their polynomial
annihilator has rank 4-m over every allowed extension. Under projected
compatibility, the first-m-row Lagrange solution solves the whole system,
even if beta^Y and beta^Z do not do so separately. Both-zero requires m=3.
No defect found at this checkpoint. Exceptional lifts, full regression
values and final proof qualification were subsequently checked below.

The existing regression script has been read in full. It compares the
formula with direct four-row Gaussian recovery and all eight residuals,
over three selected prime-field pencils only. Its certificate root preview
is not verification.

## Completed verdict

No mathematical defect was found. The full audit reasoning and positive-row
details are canonical in L057's separate critical-audit subsection. The
both-zero affine system, nonzero pivot, finite gates, eight-moment recovery
and same-support contradiction survive arbitrary extension-field weights
and parameters. Zero recovered weights are covered symbolically; the
selected regression has only full-weight positives.

Read the saved primary recurrence, distance and shortening extracts named
by the approval. Their hypotheses match L057 and L041. This reuses existing
source coverage without fresh retrieval or external discovery.

Reproduction: `python3 scripts/triangle-recovery/check_selected.py`.
Actual/required discrepancies: 0/0. Each of three pencils has 1817/1817
support rows and 94/94 eligible parameters per row. Complete positive rows
at `/cases/1/rows/1167` and `/cases/2/rows/1140`, complete `/failures`, and
exact actual/required failure values were inspected with the shared JSON
inspector. The program exhausts all selected supports and parameters; its
direct eight-moment comparator does not use the projected criterion.
The certificate is `scripts/triangle-recovery/selected-regression.json`.

This verifies an existing local reproduction, not a new theorem, count or
originality claim. No formula or direct input changed; PROOF.md and DAG.md
are retained unchanged. Recorded stops retain their original scopes and
the global interval remains 11/q–16/q.

The proposed next target is high-count descent of the three normalized
pair weights. L057's isolated recovery missing every shared label already
descends them, but does not force such a recovery or control simultaneous
both-zero lifts. A new REVIEW_REQUIRED assessment records this gap; no
descent theorem or count is derived in this audit.
