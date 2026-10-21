# Coupled table execution — BSD-190 working record

Approved target: construct and independently verify all 72 normalized
generator values from L054's fixed coupled T_5 geometry and L055's
H=4860 exponential-tail plan, including finite-sum containment,
total-period division and 24-scaled integer isolation. The unchanged
SPECIALIZE assessment is
`drafts/literature/2026-10-12-conductor36-coupled-generator-table.md`.

The main gap is arbitrary analytic-order-at-least-two rank equality.
This target can finish the independent full-relative normalization
benchmark at composite conductor 36; its CM restriction prevents using
L027 and it supplies no rational directions, Sha or complex-order
comparison. Essential inputs: audited L038 N=36/P-empty domain, L049,
L050, audited L051 and L052, L053's audited endpoint assignments,
audited L054 geometry and audited L055 full tails. No cross-notebook
input. The supplied assessment already compares known sources,
duplicates and ATTEMPTS/025--028; those failures are preserved.

Execution contract: exactly 98 primitive points, 16 heights, 144 endpoint
occurrences, 72 generators and 1316 uncombined signed occurrences;
4860 terms per point, 476280 <= 1000000 overall. Retain every finite
term, including zero coefficients, reduced phase/remainder, power,
signed contribution and partial sum. Cache only identical exact phases
or heights. Use L055's full q^4861/(1-q) upper radii, outwardly rounded.
Replay the independent positive total period; use all four quotient
endpoints. Require each actual width <=2^-38 and equal ceil/floor after
scaling by 24, including zeros. Only then test all 144 source relations,
59 saturated columns and full 13-dimensional quotient reconstruction.

Continuation test: complete independent replay and all thresholds must
pass. A failed record, missing containment or ambiguous isolation is
saved as an exact failure; refinement may use the assessed arithmetic
with this same geometry and cutoff. Success still awaits a separate
critical audit and is reproduction of known methods, not a BSD candidate.

Completed implementation: separate streamed per-point term certificates,
manifest and independent Fraction-endpoint verifier reconstruct every
required list and operation. Complete report is
`scripts/conductor36-table/table_verification.json`. Canonical result and
full proof are L056. All 476280 terms and 72 integer isolations pass;
actual max width is 27940579275/39614081257132168796771975168<=2^-60,
with all source/saturated relations and quotient reconstructions passing.
There are 16 zero generator values and common reduced denominator 12.
Two malformed/missing-data cases are rejected; original hashes persist.
No fixed precision refinement was needed. Separate critical audit remains
pending, proposed with REVIEW_REQUIRED coverage for next-turn approval.
