# Changed-tail integer-exclusion assembly — 2026-10-14

Approved target: Assemble L067 and L066 to exclude integer unshifted junctions satisfying the endpoint/J subsystem for every intact order of the changed-tail allocation, including cyclic relabeling.

Prior gate: `literature/2026-10-14-changed-tail-integer-exclusion-assembly.md`,
SPECIALIZE. One RESEARCH/REPRODUCTION applicability assembly; no new
modular search, source review or actual-cycle bridge is authorized.

Checkpoint before writing the assembly: L067's audited hypotheses and
uniqueness match L066's tails and unshifted coordinate. With row 24 at
position t, rotate position k to (t+1+k) mod 25, taking its input and
outgoing row together. This must preserve the old cut edge and the new
closing edge. L067 then forces the literal order; endpoint uniqueness
must identify that tuple with L064's j=23 root, whose unshifted coordinate
L066 proves nonintegral. Require all original unshifted junctions integral
in the contradiction, rather than asserting nonintegrality of each one.

Main gap: universal eventual descent. This intermediate exclusion could
remove one more fixed integer allocation; other allocations, entry,
unrestricted cycles, divergence and descent remain independent gaps.
Continue only if domain, guards, tails, rotation and root identification
match exactly. A mismatch stops this application without establishing
feasibility. Both rational witnesses and Attempts 027–031 are preserved.

Essential inputs: L051 endpoint/J formulas, L055's indexed J,H table,
L064's j=23 literal root, audited L066 and audited L067. L065 names the
tails only; no H/seed conclusion is used. Full matching Mathlib unchecked.

Completed: the canonical proof is C067a. All 25 edge cases are accounted
for symbolically, including t=24 when the old cut is also the new closing
edge. L067 forces literal order under matching hypotheses; its endpoint
uniqueness identifies L064's root, and L066 gives the contradiction in
the unshifted coordinate. No calculation or source refresh was needed.
This is ADVANCE as a local conjunction of audited inputs, not a theorem
beyond the checked literature or a complete solution. Separate critical
review of the assembly is proposed with REVIEW_REQUIRED coverage.
