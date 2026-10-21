# First overorder: full integral ideal-power witness cap

2026-10-17, step 293. The one approved producer stopped at the combined
134217728-byte limit while serializing the power-16 reduction witness.
The complete failure report is
[producer-report.json](../scripts/seven-torsion/first-overorder-293/producer-report.json);
[the working record](../drafts/2026-10-17-first-31-overorder-attempt.md)
records limits, preserved inputs and missing obligations.

## WHY IT FAILS

Binary multiplication of complete rank-48 ideal bases with all reversible
integer reduction operations generates large coefficient witnesses: the
power-8 artifacts already persist about 39.6 MB, and the power-16 write
would exceed the fixed total cap. No complete B^46, source lattice or
new order was produced, and the partial arithmetic has no independent
replay. This refutes feasibility of this particular witness representation
under the approved bound, not the existence of a strict overorder or the
source theorem. Stop this execution permanently, preserve all partial
files, and do not resume or retry with compression or a larger cap.
A separate source review may test a different prime-local quotient
certificate directly from the original inputs; its exact denominator
and integral generation requirements remain uncovered. No global research
ban or mathematical nonexistence conclusion follows.
