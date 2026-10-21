# Bounded principal-power test: backend preflight stop

2026-10-12. The approved ten-exponent test stopped before arithmetic:
none of the bounded local Python probes imports the documented SymPy
backend. The full diagnostic is
scripts/power-order-principal-power/backend-certificate.json; reasoning
and scope are recorded in drafts/2026-10-12-bounded-principal-power-attempt.md.
Audited L058 and L045 remain unchanged. Zero candidates were tested.

WHY IT FAILS: No working exact lattice-reduction backend is available
among the interpreters actually checked. This is an implementation
blocker, not failure of a principal-power relation or a class obstruction.
No rank, stability, compression or equality calculation ran. Do not
repeat interpreter probes as mathematical work. Resumption of the same
ready test requires making the documented backend available, then
performing the original bounded computation without expanding its scope.
The obstruction is local to this implementation; no global route is banned.
