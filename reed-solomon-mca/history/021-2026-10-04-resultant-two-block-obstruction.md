# 021 — 2026-10-04 — Actual resultant test and two-block restriction

Completed one mathematical attempt on the saved SPECIALIZE resultant
target, reusing its adequate source coverage without browsing. Shared
instructions, local goal, checkpoint, full overview, DAG, prior assessment
and unfinished local changes were inspected first and preserved.

The [exact test](../scripts/resultant-pencil/check.py) supplied 256
two-block partitions, 128 lines through two disjoint four-error points,
and 128 independent eight-moment pencils. None satisfied the target
squarefree fourth-power condition. These prime-subfield samples do not
exclude arbitrary inputs over F_(97^20). The
[result](../scripts/resultant-pencil/result.json) retains the seed,
histograms and a complete representative pencil. Modular Frobenius checks
extension-field splitting exactly; the representative's original event
was independently checked on all 2517 admissible supports.

Examining the actual two-block determinant yielded
[L013](../lemmas/L013-two-block-locator-and-fiber-obstruction.md): its
locator is a scalar divided difference of the two block polynomials, and
extra bad parameters are controlled by one fiber on the six remaining
coordinates. The uniform count is ten, eleven or fifteen. This verifies
the actual moments and reuses L010 for original same-support failure,
rather than treating a perfect-power product as sufficient. The proof
does not depend on the samples and eliminates a nondegenerate construction
class from sixteen-count equality. The restriction is recorded in
[ATTEMPTS/006](../ATTEMPTS/006-two-block-sixteen-resultant-witness.md).

The global interval stays 10/q–16/q against an allowable fifteen; general
equality remains undecided. Imported resultant and power tools are known.
The actual locator/fiber specialization is potentially beyond the sources
checked, not a certified originality claim. No complete resolution
candidate appeared, and STATUS remains IN_PROGRESS.

The next direction uses the already preapproved coefficient-feasibility
subtarget for arbitrary affine moments. A restriction for the stopped
two-block generator cannot settle that general system. This avoids a
repeat generic sample search and requires no new literature gate. The
July/four-block source stop and earlier exhaustion evidence remain parked.

Outcome: ADVANCE, for the relevant uniform class restriction;
STEP_KIND: RESEARCH; STEP_CLASSIFICATION: POTENTIALLY_NEW.
Resultant-target mathematical attempts: one; consecutive uninformative
mathematical turns: zero. No scheduler, launcher or retry state was changed.

Validation: `python3 scripts/resultant-pencil/check.py` passes the 512
supplied-pencil tests, 256 actual divided-difference identities, power
and exact-splitting controls, and independent support audit. The full
proof was checked for the constant-scalar step, repeated residual-root
case, singular parameters and original input failure. The proof imports
L008's construction and L010's original-event converse; sampled data is
not a proof premise.
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
passes with fourteen nodes and eight edges, valid links, and compact
overviews. The next action exactly matches a preexisting COVERED_TARGET
in the same ready assessment. Existing unfinished work is preserved.
