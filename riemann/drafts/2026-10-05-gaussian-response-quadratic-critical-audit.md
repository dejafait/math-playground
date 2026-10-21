# Response quadratic margin — audit checkpoint, 2026-10-05

The invocation uses the unchanged SPECIALIZE coverage in
`drafts/literature/2026-10-05-gaussian-response-quadratic-audit.md`.
The main gap is global actual-theta mixed positivity. This bounded audit
checks L368 as an input to L367's quadratic term, leaving the linear
term and actual-theta margin independent. Continue only if its claimed
uniform lower bound survives carrier, remainder and zero-safe checks;
otherwise record the exact failed comparison and narrow the claim.

The complete L368 proof and L005 were checked against the relevant
L358 and audited L366 identities, the saved source assessment and the
recorded L365 stop. The carrier factor and signed projection expansion
agree with independent multiplication. The rational phase correction
needs its exact logarithmic derivative recorded to make the O(t^-2)
imaginary-part estimate transparent. The normalization coefficient is
consistent with 1/(64 pi^2). Finite-onset and parity checks are pending
final consolidation; no onset is being numerically evaluated.

Pre-existing unfinished changes were preserved. This file records the
audit checkpoint, not a second canonical proof. Full verified details
will remain in L368. No new source search or mathematical script is needed.

## Completion

The audit passes. The canonical proof in
`lemmas/L368-first-regulator-response-quadratic-margin.md` now displays
the exact rational phase derivatives, checks the signed cross term,
specifies a common finite onset in terms of uniform constants, and
justifies conjugation from the scalar integral and series. No coefficient,
bound, domain or DAG input changed. The earlier pending paragraph is
preserved as a checkpoint, not a current mathematical qualification.
Local progress is verification of a previously pending input, not a new
sign theorem beyond L368 or a novelty claim. The unchanged main argument
does not require an edit to PROOF.md. Current continuation and routing
are recorded only in PROGRESS.md.
