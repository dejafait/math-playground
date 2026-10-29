# L133 three-shift certificate — audit coverage

TARGET: Critically audit L133's complete three-shift conflict certificate and fixed-map retention bound.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the invocation-start completed comparison in 2026-10-26-packing-assisted-independent-translations.md, including its scoped duplicate/failure search; no additional external search was performed or needed for the unchanged finite matching method. The new review object is L133 and its two finite-enumeration implementations.
SOURCE_EVIDENCE: Direct primary source: https://arxiv.org/pdf/2009.03780v1 ; Denes Konig, Graphs and matrices (1931), authorized translation by Gabor Szarnyas (2020), unnumbered main theorem p. 3 and graph proof pp. 1–2, rechecked 2026-10-26 including all four endpoint cases and the disjoint-edge lower bound on p. 2. L030 and audited L131 supply the local model; L133 and both programs still await critical audit.
COMPARISON: The standard disjoint-edge cover principle suffices once the stored edges, their actual-label intersections, distinct supports and tagged endpoints are verified. No optimality, rank theorem, random-map hypothesis or general cross-intersection theorem is needed. The instance counts are computational evidence requiring independent scrutiny, rather than a named source theorem.
GAP: Check both whole-support implementations, all original-map linkage, the full 7714059 intersection entries, all 2571301 stored qualifying edges across the three shifts, all file manifests and the sufficient-threshold arithmetic; do not assume that agreement between two implementations alone proves either uses the stated maps.
REASON: Adequate source coverage is reused for this bounded verification target, with the missing direct source URL repaired and the cited proof rechecked; only its concrete finite specialization and logical qualifications need audit. No certificate audit is performed in this literature-only recovery step.
SCOPE: Exactly TARGET; L131's unchanged q,T,cores,maps and c=0,1,-1 only; independent replay/reconstruction, certificate completeness, graph/retention logic and pending-review qualifications. No additional shifts, improved matching, arbitrary maps, rank expansion or global RS inference.

LITERATURE_REASON: Supervisor recovery requires a direct primary source URL in this ready assessment. Repair that omission and verify the cited source scope; reuse the completed duplicate/failure comparison without expanding the mathematical target.

## Source-link recovery

On 2026-10-26, opened the versioned primary PDF linked in SOURCE_EVIDENCE
and read the finite bipartite hypotheses, matching and cover definitions,
augmenting-path argument, all four endpoint cases, and concluding theorem.
In particular, p. 2 explicitly gives the disjoint-edge counting direction
needed by the proposed audit; optimality or the converse is unnecessary.
This confirms the recorded source scope, not L133's computed instance.
No new theorem, specialization or certificate verification was performed.
The completed comparison and recorded failures in
`2026-10-26-packing-assisted-independent-translations.md` remain applicable.
No essential source blocker remains for exactly TARGET. Mathlib coverage
remains not checked. Proceed next turn with the audit; retain or repair
any discrepancy rather than extending the shifts or claiming RS safety.

## Purpose and evidence to review

The main gap remains arbitrary-center 67/68 safety. L133 is a restricted
negative result: it would eliminate these fixed maps as a nonvacuous
large-packing instance, without eliminating arbitrary-map witness forcing.
Its strongest claimed inequality is |I_L|+|I_R|<=2571406, so one side
has at most 1285703 supports. The relevant integer test is matching
size >=2077715 versus two deletion budgets of 1038857; the recorded
c=-1 matching has 2571300 edges.

Read L133, `scripts/finite-support/three_shift_conflicts.c` and
`scripts/finite-support/three_shift_conflicts.py`, with the exact
L131 prescription as mathematical input. The manifest is
`scripts/finite-support/three-shift-conflicts/certificate.json`.
The complete intersection bytes and complete little-endian edge triples
are canonical evidence; a bounded preview of either is insufficient.
The production turn's replay inspected every byte and edge and saved
66 passing checks. A critical audit should verify the algorithms and
scope independently, including all map entries and binary conventions,
rather than merely accept that summary. Hashes link inputs to outputs;
they do not replace the mathematical reconstruction.

Load-bearing cases: field wraparound of u+c, exceptional signature
labels/dummies and fixed assignments, cross-column label coincidences,
support equality excluded from conflicts, within-side index injectivity,
tagged endpoint injectivity, no omitted/nonqualifying pairs, and use of
only c=-1 in the size-sum proof. Combining the three edge lists is not
asserted to be a matching. Rank and generic-coordinate invariance play
no role. The 53 nonconflicts for c=-1 remain in the complete histogram.

Continue only if this exact evidence establishes the claimed restricted
bound. A discrepancy must be retained and repaired or explicitly limit
the conclusion; it supplies no license for more shifts or a changed
target. The audit is routine finite hypothesis/arithmetic/replay checking,
not a creative mechanism or an audit of a complete challenge solution.
Full and supporting Mathlib coverage remains not checked. No new
external source, theorem, cross-notebook input or novelty is asserted.
