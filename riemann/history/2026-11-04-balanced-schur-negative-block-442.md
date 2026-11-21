# 2026-11-04 — balanced Schur test, step442

Completed the exact EXPLORE-approved target in
`drafts/literature/2026-11-04-balanced-schur-defect-test.md`.
One bounded mathematical attempt produced an informative NEGATIVE:
[L780](../lemmas/L780-actual-balanced-schur-negative-block.md) transfers
L779's complete saved factor/node/residue enclosures to a strictly
negative actual eliminated block and the identical reference block.
The full rational certificate is
`scripts/actual-fredholm/balanced-schur-certificate-442.json`.

Both inverses exist, so this is a failure of the required positive
margin, not of invertibility or the actual minor sign. The decisive
benchmark condition already fails; no reference-defect computation,
parameter sweep or whole-certificate replay was needed. The proof and
certificate are a known-method specialization, not a claim of a new
general theorem or progress beyond the inspected literature.

Stop only the specified positive-block normalization; retain the signed
Fredholm route and L779's positive determinant. The
[failure record](../ATTEMPTS/2026-11-04-balanced-schur-negative-block-stop.md)
preserves that distinction. The unfinished projection-weighting idea is
saved in `drafts/2026-11-04-balanced-schur-working-442.md`.

Nominate a different signed-inertia kernel comparison in
`drafts/literature/2026-11-04-projection-weighted-reciprocal-inertia-review.md`.
It is REVIEW_REQUIRED: no kernel identity, analytic class membership or
inertia payment is approved here. L780 remains awaiting a later independent
audit; inherited L779 arithmetic contracts remain explicit. No shared
infrastructure, scheduler state, sibling notebook or previous evidence
was changed.
