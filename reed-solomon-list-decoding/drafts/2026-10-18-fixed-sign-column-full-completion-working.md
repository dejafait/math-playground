# Fixed L086 columns: one exact full-mode attempt

The approved target is exactly the TARGET in
`literature/2026-10-18-fixed-sign-column-full-completion.md`.
Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957.
Intermediate target: feasibility of all 81 original modes and 45 moment
signs at precisely L086's column parameters. A completion keeps this
slice available; a complete original/raw separator stops these columns.
Neither outcome addresses other plane points, scalar upper rows, other
anchors, global consistency or RS realization.

Inputs: L076,L078,L082,L083,L084,L086,L087, with L021,L053,L073,L075
and foundations/04,09,10,12's ancestral qualifications retained. The
complete step-308/310/312/314 evidence is consumed through bound hashes
and reconstructed original rows. Existing conic stops remain in force.
The three frozen L086 column coordinates were inspected completely;
the old 45-moment assignment is comparison evidence only.

Implementation decision: retain the 81 original inequalities A*z<=b
and all 45 explicit rows -z<=0, without equality elimination. Use
nonnegative z, oriented slacks, and artificial initial basis. The
explicit sign rows are retained even though the standard variables
already have that sign. For a positive Phase I optimum, lift its dual
to all original rows and absorb any remaining nonnegative z coefficient
into the explicit -z rows. Verify exact zero total coefficient and
strictly negative right side, also after positive raw-coordinate scaling.

Before pivots save the full original system, labels, conversions and
initial tableau. Use the approved least-index/ratio tie rules, one run,
10000 pivots/300 seconds, with complete state checkpoints. Any cap or
failed reconstruction is inconclusive. No new source search, scan,
retuning, extra constraint or second solver run is authorized here.

## Completed attempt

The single direct-coordinate run is inconclusive. It stops at the time
threshold after 97 complete pivots, below the 10000-pivot cap, with a
strictly positive artificial objective. There is no feasible witness or
Farkas separator. The 300-second threshold is observed at 302.638 seconds;
final state serialization/reporting brings the recorded elapsed time to
310.829 seconds. No extra pivot, resumed run or increased cap is used.
The last reported completed pivot precedes the threshold (298.5 seconds).
Positive intermediate objective is not an infeasibility certificate.

The reconstruction reuses the inspected implementation of L087's original
recipes, redirects its output to a new file and preserves every old
certificate. Its 1597 checks pass: all 85 fixed domain factors, 90 kernel
equations, 500 types/3000 presentations, complete original beta rows,
36 forced entries, full anchor, fresh principal inverse solves and all
singular/empty cases agree. The old moment assignment is used only as
a regression control. The actual LP allows all 45 moments to vary.

Full original A*z<=b, all 126 row labels, positive raw conversions,
standard matrix, initial tableau, complete final tableau, row transform,
and all 97 pivots are saved under `scripts/finite-support/`:

- `fixed-sign-column-original-reconstruction.json`
- `fixed-sign-column-full-completion-results.json`
- `fixed-sign-column-full-completion-initial-state.json`
- `fixed-sign-column-full-completion-state.json`
- `fixed-sign-column-full-completion-verification.json`

Reproduction commands (the first performs the one mathematical run;
do not invoke it again as part of this completed attempt):

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/fixed_sign_column_full_completion.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_fixed_sign_column_full_completion.py

The constructor records 28 additional passing checks and no failures.
The independent verifier reconstructs all 81 original bounds from the
ancestral forced/cross/inverse/anchor data and raw beta coefficients,
checks all 126 original/raw rows, fixed columns and source bindings,
and confirms the honest cap report in 231 checks without failures.
It checks the saved basic signs, objective and complete pivot-trace
agreement; it does not replay or critically audit all pivots. No solver
or constructor is invoked by that verifier. No new mathematical result
is asserted; no lemma, DAG edge or overview change is warranted.

Methods and their exact citations remain canonical in L078, L086 and
L087 and in the prior SPECIALIZE assessment. No source search or
general-theorem reproof was needed. Full matching Mathlib coverage
remains not checked. This is RESEARCH / REPRODUCTION / EXPLORATION,
with no progress beyond inspected sources or RS boundary improvement.

Stop this unreduced full-row prescription. A smaller independently
testable target is proposed, not attempted or approved: keep the 28
necessary equalities, 45 signs and all 17 new-only modes at these same
columns. L084's 18 free moments could make this exact subsystem more
tractable. Its feasibility would park only that subset; infeasibility
would reject the columns. The remaining 36 mixed modes outside the
selected equalities, scalar upper rows, other anchors, other plane
points, global consistency and RS realization remain unresolved.
The changed target is REVIEW_REQUIRED for a separate literature gate.
