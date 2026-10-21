# Full scalar extension — working checkpoint

Gate-approved target: Test L022's unchanged extension against all Schrijver
scalar orbit constraints for A(1024,10,68), with an exact exhaustive
certificate. Prior SPECIALIZE assessment:
`literature/2026-10-05-full-scalar-extension-test.md`.

Main gap: arbitrary-center safety at 68 agreements. This finite diagnostic
can expose a necessary missing scalar constraint, or park scalar exclusion
for the fixed assignment if all rows pass. It does not test full SDP
feasibility, packing/list realization, sharpness, scalar/tuple equality,
an exponent m, 67-agreement safety or ABF equivalence.

Inputs inspected: foundations/04, L021–L024, selected/full-zero generators
and independent audits, and ATTEMPTS/012–014. Preserve all earlier work.
The imported result is Schrijver 2005 III.B (62)–(67), with actual-orbit
scope and repeated words; no reproof or tuning is needed. Classification:
REPRODUCTION. Mathlib full matching coverage remains not checked.

Implementation plan: store every ordered (i,j) source range and a lossless
map from h to a numerical cache. Different t-s orbits remain distinct.
Clear all pair denominators D; writing p_i=A_i/D and lambda=A_68/D,
use the positive common denominator H=D^2 A_68 for product values and
all three slacks. An independent auditor will reconstruct p from the
L021 witness and check its defining first-64 equations by polynomial
convolution, regenerate orbits from nonnegative multinomial parts, check
every mapped scalar row, all six distance permutations preserving t-s,
distance zeros, normalization and old scalar/value overlaps. Full exact
integers and lossless maps go under scripts/finite-support/ before
interpretation. A resource failure is unfinished work, not feasibility.

Completed: generation and the independent audit pass all 1500625 ordered
orbits, 4501875 scalar rows and 9003750 permutation checks, with no
violations or verification failures. Full proof is appended to canonical
L023; no new lemma identifier is added. Certificates are
`scripts/finite-support/full-scalar-results.json` and
`scripts/finite-support/full-scalar-audit-results.json`. Ordinary scalar
exclusion is parked for the unchanged extension. The next proposed source
comparison concerns a strengthened Kim–Toan constraint; it is separately
REVIEW_REQUIRED, with no new inequality imported or tested in this step.
