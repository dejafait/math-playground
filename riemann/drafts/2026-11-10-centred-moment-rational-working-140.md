# Rational replay — step140 working checkpoint

Approved target: unchanged exact target in the step138 SPECIALIZE assessment,
separately reviewed in step139. Actual task: implementation, REPRODUCTION.
Main gap: L030–L032/C032a. Target: both natural-index walls and all 151
complete-support moment leaves; downstream pays only one L960 premise.
Continue only on all 914 original gates plus arithmetic/error checks and
maximum certified upper endpoint <81/4; definite failure or infeasible cost
parks this implementation; overlap is inconclusive. Preserve steps136–139.

Plan: fixed 256-bit dyadic intervals; exact integer floor/ceiling operations;
log range reduction with positive atanh series; positive exp Taylor series
with geometric remainder then squaring/reciprocation; sqrt by integer square
comparison; Machin pi. Integrate after affine substitution to [0,1] using
4096 even Simpson subdivisions and explicit fourth-derivative enclosure.
Quadratic exponent grid permits an exact multiplicative recurrence, avoiding
600000 separate transcendental evaluations. Prove inclusion/error bounds in
L960 before trusting the run. Save a certificate after every leaf. Each
execution slice at most60 seconds; partial output is not a completed bound.

Unresolved: actual finite enclosures, runtime and all independent L960
analytic/stability/global/zero-time premises. No new central mechanism is
justified by this arithmetic task; no RH candidate. Mathlib unchecked.

## Completed checkpoint

The first bounded run passed all914 original gates/all151 leaves in20.975
seconds; no failed, inconclusive or unpaid gate. Maximum is on leaf1,
<20213859/1000000<81/4. Full proof and exact maximum are canonical in
L960 step140. Full evidence inspection passes; first helper report with
its unnecessary failed guessed20.2137 display threshold is preserved.
The actual evaluator/certificate was unchanged by the helper correction.
PROOF was shortened to its required byte budget; scoped structure check
passes. Continuation is independent conceptual audit, with proposed
unchanged-source coverage for separate next-turn approval. This is
ADVANCE/REPRODUCTION, not a new result beyond the source or an RH candidate.
