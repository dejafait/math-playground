# L078's unchanged weights do not strictly exclude the full column family

WHY IT FAILS: [L079](../lemmas/L079-eight-family-fixed-separator-attained-positive-maximum.md)
checks the entire common four-parameter L076 family with L075's dictionary
and original pairs. Every full-key equality and singular range is an
identity. The unchanged 81 weights give a rank-one concave quadratic
whose global maximum lies in [351861924105,351861924106)/10^6 and is
attained at an exact admissible point. Thus a strict uniform negative
pairing is false. This stops these weights only, preserving ATTEMPTS/060
and L078's immutable-column rejection. Other separators or simultaneous
PSD feasibility, omitted rows, global moments and RS realization remain
open. The dedicated step-278 critical review retains L079 without a
mathematical correction: all 7158 rerun verifier checks and 8699 additional
exact checks pass. The complete audit is recorded in L079 and
`scripts/finite-support/eight-family-fixed-separator-critical-audit.json`.
