# Full zero-index witness diagnostic — working record

Approved target: Test L022's explicit rational triple assignment against both full (0,0) Schrijver blocks for A(1024,10,68), with exact PSD or negative-quadratic certificates.

Main gap: arbitrary-center safety at 67/68 agreements. Intermediate target:
evaluate only the prescribed extension, on the two full matrices indexed
0,...,68. A negative rational quadratic identifies a constraint excluding
this extension; exact PSD in both parks this diagnostic. Neither decides
the full SDP or the threshold, nor excludes different extensions. A
resource interruption leaves an unfinished diagnostic, not a matrix sign.

Inputs: L001, C001a, L021, L022 and foundations/04; the ready SPECIALIZE
assessment is drafts/literature/2026-10-05-full-zero-block-witness-test.md.
The selected-batch stop in ATTEMPTS/012 remains valid. The exact source
formula is Schrijver III.B (64), with beta from III.A (58), independently
corroborated by Kim–Toan (32)–(33). No new source review is needed.

Execution plan: stream actual admissible (i,j,t,s) per matrix entry;
preserve source beta coefficients and their sums by h=i+j-t-s. Evaluate
the forbidden-distance, repeated-word, product branches in that order.
Check every old orbit value and both old principal matrices. Save all
completed matrices before exact elimination; independently reconstruct
entries and negative quadratics or all PSD congruence identities. No
optimization, altered assignment, additional block or full scalar audit.

Independent unresolved assumptions: full-SDP feasibility, actual packing
or RS-list realization, safety at either unknown grid index, interleaving
sharpness and ABF equivalence. Mathlib matching coverage is not checked.

Completed: both full matrices are exactly PSD, independently verified
from all source sums and all congruence identities. Family y has 65
positive/4 zero pivots; family p_h-y has 68 positive/1 zero pivot.
All 7093 old orbit values and 32 principal entries agree. The diagnostic
is parked as an exclusion of this extension; other omitted constraints
remain unknown. Canonical proof: L023. Full generation and independent
audit certificates are scripts/finite-support/full-zero-block-results.json
and scripts/finite-support/full-zero-block-audit-results.json. Their
large integers require PYTHONINTMAXSTRDIGITS=0 with the JSON inspector;
shared infrastructure is unchanged. All verification failures are empty.
