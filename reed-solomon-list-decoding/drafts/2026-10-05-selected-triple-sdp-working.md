# Selected triple SDP — working record

Gate-approved target: Test whether the Schrijver triple-distance semidefinite bound for A(1024,10,68) certifies B_m(956/1024)<=65537^28/2^128, using an exact certificate.

Main gap: arbitrary-center safety at 68 agreements. Intermediate target: decide whether the approved selected-block relaxation already excludes objectives above threshold. Downstream use: L001/C001a's uniform-in-m selected-support dictionary. Continue on an exact upper certificate or an informative improved bound; stop this batch only on a fully checked above-threshold feasible primal. A failed ansatz is neither batch infeasibility nor unsafety.

Inputs: L001, C001a, L021 and foundations/04. L021 and ATTEMPTS/011 stop the basic LP; ATTEMPTS/010 refutes universal exclusion, not this SDP. No new source discovery is needed. Imported Schrijver Section III.B (64)–(67), corroborated by Kim–Toan (32)–(35), licenses exactly the assessed constraints. Full Mathlib coverage remains not checked.

Attempt in progress: scale L021's exact pair witness by 1/2 (p_0=1), and on allowed distinct triples set y=p_i p_j p_h/p_68, with repeated-word normalization and forbidden-distance zeros handled separately. This is a candidate assignment, not an assumed feasible triple lift. Enumerate the approved touched-orbit permutation closure, enforce construction caps, and check all scalar/pair conditions and selected PSD matrices exactly. No local conic solver is installed; the candidate test is finite rational arithmetic. Preserve complete coefficients, variables and PSD/failed-pivot evidence on disk before interpreting the result.

Independent gaps: safety at 67 agreements, full SDP, actual packing/list realization, determinant transfer, ABF equivalence and sharpness. No m exponent or extension-field multiplication is assumed.

Completed: the single candidate passed every retained constraint. The
independent audit checked 68805 scalar rows, all 68 pair rows, all 9101
aggregate affine coefficients and all six full congruence identities.
6978 retained variables and 68873 total rows satisfy the stated caps.
The objective exceeds threshold by a factor in (1.383,1.384), with
integer rounding also insufficient. Canonical proof: L022. This stops
only the selected batch; no numerical optimization was needed or run.
Previously untouched full (0,0) blocks are a proposed separately reviewed
continuation, not part of this completed attempt.
