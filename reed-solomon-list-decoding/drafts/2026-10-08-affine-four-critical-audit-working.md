# L036 critical audit — working checkpoint

Approved target: Critically audit L036's fixed-family four-neighbor exclusion, its complete head and intercept reductions, and both full finite certificates.

Prior SPECIALIZE coverage: `literature/2026-10-08-affine-four-exclusion-audit-coverage.md`.
Inputs read: L036 in full; L035's fixed family and proof of pair intersections;
L031's incidence hypotheses and necessity/sufficiency framework; L034's exact
admissibility definition; L032's opposite-edge reuse witness; ATTEMPTS/019–021,
023–024 and history/089. No new source assessment or construction is needed.

The main gap remains arbitrary-center safety at 67/68 agreements. The
intermediate target is reliability of this fixed-family exclusion; its
downstream use is one necessary condition in a later admissibility analysis.
Retain only on complete proof and certificate verification; correct a missing
case or withdraw the exclusion on a verified witness. Other restrictions,
the family cap, RS realization and the 955–957 boundary remain unresolved.

Pre-computation audit: equal heads cannot occur; distinct slopes contribute
at most one tail point per pair. Twelve head memberships and empty triples
force six distinct head points of multiplicity two, one per K4 edge.
The 24 vertex permutations act freely on six-edge bijections, giving 840
unordered configurations. Vertical translation has a unique b1=0
representative; all crossings with line 1 determine the other intercepts.
Only the producer discards repeated incident coordinates. Opposite-edge
coordinate reuse must remain allowed. Bijection transport preserves these
set statements without preserving actual-label polynomial ranks.

Next within this approved audit: reconstruct heads from edge assignments,
construct full tagged blocks for all 105000 normalized candidates, compare
every row of both saved certificates and independently recover every
producer field crossing. Preserve original certificates rather than overwrite
them. This is verification, not an expansion to other incidence restrictions.

## Completed audit

The full separate audit and qualifications are canonical in L036. The
new verifier generated every head via K4 edge assignments and compared
every stored row of both original certificates via complete block
intersections. All 858 checks passed; full-pattern successes and both
failure arrays are zero/empty. Both original files remain unchanged.
The full new certificate is
`scripts/finite-support/affine-four-critical-audit-results.json`.
No proof correction or boundary improvement was found. The next proposed
target changes to nonanchored L033 incidences in this fixed family and
requires its own literature approval; no such theorem is derived here.
