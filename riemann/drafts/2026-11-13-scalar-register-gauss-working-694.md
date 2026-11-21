# Scalar-register Gauss implementation694

Main gap: L030-L032/C032a actual-Xi positivity and signed remote-plus-induced
S3 coupling. The sole approved intermediate target is assessment687's exact
all261 Gauss-node/weight setup test; possible downstream use is the shared
bank square service. Independent signs, inverse debt, bank errors and global
assembly remain open. Supplied687 and inspected source-notes688 are reused;
C998n/audit693 supplies the component defect, C998l/m the fixed-prescription
stops. No new literature, source scope or cross-notebook input is used.

## Prescription fixed before execution

Keep692's numerical mesh, D=2^640, adaptive threshold, 17 prefix trials,
12 Newton updates, full derivative bounds, node-width2^-550 gate,
conversion-width floor2^-560, weights and reflection. Replace its scalar
implementation with a finite single-assignment register program. Constants,
including powers and recurrence tables, are generated in counted registers.
Fixed loops over degrees, mesh slots, recurrence stages and bounded trials
are macro-unrolled: their indices are static instruction addresses, not
real-valued counters. No approximate seed or numerical table is imported.
A register label is a symbolic operand reference, not a scalar copy; explicit
copies/output stores are counted. Each arithmetic instruction costs2
(one arithmetic plus its destination assignment), copy/literal costs1,
comparison costs1. Selection uses a comparison plus a counted copy.
Every executed instruction, including constant setup and failed guards,
will be saved in a compressed full instruction transcript. Exact replay
from its initial small-integer literals is possible without any oracle.
Output/error evidence will be saved separately, not printed as a preview.

The only unbounded numeric loop is conversion. It uses counted width and
depth comparisons, exact real midpoint/width halving, endpoint copying,
and depth increment. It contains no remainder or floor primitive. Starting
from the mesh, endpoints are dyadics on the D grid, at depth14 or finer;
induction shows each endpoint is divisible by2^(640-depth). The counted
check depth<640 before each new midpoint implies exact grid halving.
Intersections/expansions preserve that property. All derivative midpoint
uses also check depth<640. Each binary pass therefore needs no numerical
parity guard. This is a new explicit scalar implementation, not a repaired
claim about692's literal source or its rejected12-rate charge. Transcript
administration, exact rational serialization and independent checking are
outside the numerical service, as in692; no numeric service computation
may bypass the register engine.

Bounded test: stop this ONE prescription at any failed guard, exhausted
schedule, or scalar total>5000000. Continue only if all261 outputs pass
both independent2^-512 radius tests and the complete register program
cost<=5000000. Verify every mathematical trace value against692's complete
independently replayed accuracy certificate and replay the full register
instruction transcript independently. This shares no asserted cost rate
with692. No retuning/retry is authorized within this attempt. A service
implementation at these scalar-model costs is not a bit-complexity claim.

General source statements/hypotheses and Mathlib limits are canonical in
C998n. No general source theorem is reproved. A successful finite result
would be local reproduction, not mathematics beyond the checked sources.

## Execution checkpoint before full replay

One construction completed with no guard failure: all63+81+117 outputs,
separate radii passing, register cost3290939, headroom1709061. The new
complete mathematical trace (all mesh, prefix, Newton, conversion and
weight fields) equals692 exactly, not merely at final outputs. Full
instruction replay is in progress. Its first pass stopped on a verifier
schema lookup (`source_sha256` versus the existing692 field
`source_certificate_sha256`); the failed report is preserved separately.
Only that lookup was corrected. No construction, numeric schedule or
register transcript was rerun or changed. No paid-service conclusion
will rely on the failed verification pass.

## Completed bounded attempt

Canonical result: C998o. The single scalar-register construction completes
all261 pairs, with the same full numerical trace and radii as C998n:
node<=2^-551, weight<=2^-542. Full transcript cost3290939<=5000000,
headroom1709061. Independent replay passes5791600 checks, with complete
exact rational comparison/operand/output verification and no failures.
All1388040 arithmetic instructions,1479293 scalar assignments and423606
comparisons are counted; division guards are included. The full compressed
instruction transcript is retained. A separate conceptual audit should
check source/program correspondence, fixed macro unrolling and wire-versus-
copy distinctions before downstream service reliance. C998n's old source
stop is preserved. No endpoint bank or complete square service is paid.
This is local REPRODUCTION using known methods, not new general mathematics
or an RH candidate. PROGRESS.md alone gives current routing/Next action.
