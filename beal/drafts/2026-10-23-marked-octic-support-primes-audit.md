# Support-prime critical audit in progress

Approved scope: critically audit L117's complete support-prime
decompositions, residue maps and ideal-product certificates in audited
L116's maximal ring. The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-support-prime-critical-audit.md`.

The main gap remains primitive integer emptiness for residual signatures.
This audit can secure an arithmetic prerequisite for supported square
classes on the marked octic; it cannot supply class/unit data, local point
images, point completeness or integer lifting. Continue only if all eight
exact kernels and all 68 full product reductions pass, with the number
field and maximal-ring hypotheses verified. Repair or withdraw any failed
claim. Preserve L108 and ATTEMPTS/050–051.

The full producer and support-prime replay have been inspected, along
with the L116 replay helpers actually imported. Field multiplication is
independently bound to the original polynomial, not imported from either
producer. The prime replay reconstructs the complete table, verifies all
quotient product equations and full finite-algebra discovery, and checks
integer row operations in both directions. Exact-kernel equality uses
inclusion plus the certified surjective quotient index; final product
equality is a lattice equality, not an index comparison. Further audit
checks will bind the printed basis/maps to the artifacts, explicitly
recover both kernel inclusions and check integrality of every product
generator and row matrix. No arithmetic result is declared yet.

## Evidence defect found

The first fresh replay passed its arithmetic comparisons, but the audit's
serialized actual/required consistency check failed. All 68 forward
row-operation records stored the mutable outer `rows` list; the subsequent
reverse replay replaced its rows with the original generators. Thus the
saved actual values disagreed with the saved required reduced matrices,
despite equality at comparison time. This is a real evidence defect, not
a failed ideal identity. The initial failure and replay are preserved in
`scripts/pair-genus-two/marked-octic-support-primes-audit-initial-failure.json`
and `scripts/pair-genus-two/marked-octic-support-primes-audit-initial-replay.json`.
The original producer and original replay JSON remain untouched. The
support-prime replay now snapshots all forward rows before reversal; the
new audit will require every serialized comparison to be consistent and
will save explicit two-way inclusion coordinates for all 68 products.

The next run finished the arithmetic but encountered Python's 4,300-digit
integer-output limit while serializing an expanded row-transformation
coefficient. The audit now stores that coefficient matrix exactly as its
complete reversible operation program on I_64, followed by selection of
the first eight rows. It still expands and checks the full matrix times
all original generators; the reverse inclusion coordinates are stored
explicitly. This is the same finite exact certificate, with no rounding,
omitted operations or weakened mathematical check. The output failure
was `ValueError: Exceeds the limit (4300 digits) for integer string
conversion`, in product record 49's `basis_in_generators` serialization.

## Completed audit

L117's canonical audit section records the full mathematical review.
All eight exact kernels, all 38 successive-power and 30 assembled-product
reductions pass. The corrected replay has 1,210 comparisons and the
additional audit has 428; every saved actual/required comparison is
consistent, with zero failures. The original arithmetic conclusions are
unchanged. The new audit script and full artifacts are named in L117;
the original producer and original replay JSON remain preserved.

The only continuation is source assessment for complete ordinary S-class
two-torsion, recorded as REVIEW_REQUIRED in its new assessment. No class
calculation or approval was undertaken here. The current route and exact
next action are recorded solely in PROGRESS.md.
