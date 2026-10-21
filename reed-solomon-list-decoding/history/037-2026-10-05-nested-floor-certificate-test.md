# 2026-10-05 — Nested floors fail at both undecided indices

Applied the pre-existing SPECIALIZE gate to exactly its two-index target.
[C001b](../lemmas/C001b-nested-floor-packing-certificate-limitation.md)
records the known theorem application and exact comparisons. Both upper
certificates exceed threshold, by factors in [2.763,2.764) and
[46.978,46.979). All 128 ordered divisions and independent rational-floor
checks passed. This REPRODUCTION is an informative NEGATIVE for the
method, not actual unsafety or progress beyond the inspected theorem.
C001a's bracket and unfinished work are preserved.

[ATTEMPTS/009](../ATTEMPTS/009-nested-floor-packing-bound.md) stops this
refinement as an improvement route. The next source target is separately
REVIEW_REQUIRED in `drafts/literature/2026-10-05-rs-support-realizability.md`:
inspect bounds using RS-specific realizability rather than unrestricted
packing. No such theorem was derived or approved here. Mathematical
exploration usage remains 0/3 after the informative negative.
