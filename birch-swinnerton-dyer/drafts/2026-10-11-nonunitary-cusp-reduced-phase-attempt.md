# BSD-168 — reduced-phase enclosure attempt

Initial reasoning saved before implementation (completed below). The unchanged SPECIALIZE
gate is `drafts/literature/2026-10-11-nonunitary-cusp-enclosure-production.md`.
Main gap: arbitrary analytic-order-at-least-two rank equality. The exact
approved target remains the single {1/6,infinity} normalized interval of
width <2^-20, testing L049's executable normalization layer. Essential
inputs are audited L049 and L050's exact fixed arithmetic. No cross-notebook
input, rational reconstruction, full generator table or L027 application.

Preserve the original failed files. New files will evaluate the real part
only, since that is the requested functional: for each term reduce n*x
modulo one exactly, enclose cos(2*pi*n*x) independently, and multiply by
a positive interval for exp(-2*pi*y)^n. Positive scalar powering avoids
the complex wrapping recorded in ATTEMPTS/025. All finite operations and
Taylor remainders, all coefficients/matrices/tails and the minimal-target
period must be replayed independently. Continue only on full replay and
actual width <2^-20; otherwise preserve and diagnose the new failure.
This uses the already covered finite Taylor arithmetic, with no new
analytic theorem or mathematical mechanism. Sha, rational directions,
uniform coefficient production and complex-order comparison remain open.

## Completed result

ADVANCE; RESEARCH; REPRODUCTION; ACTUAL_TASK_TYPE implementation.
Full mathematical details are canonical in
[L051](../lemmas/L051-nonunitary-cusp-reduced-phase-enclosure.md).
The producer and separate full replay both pass: normalized width
38839602421900655/19807040628566084398385987584 <2^-38 <2^-20.
All 181410 finite Fourier terms, 3672 phase polynomials, 19 damping
polynomials, 69 primitives, full tails, 38 transports, arithmetic and
period division were replayed. Evidence is under
`scripts/nonunitary-cusp/reduced_phase_*`. The original failed schedule
is hash-bound and preserved. No exact rational recovery or BSD claim.
The current checkpoint proposes a separate critical audit with
REVIEW_REQUIRED coverage, leaving the completed production valid.
