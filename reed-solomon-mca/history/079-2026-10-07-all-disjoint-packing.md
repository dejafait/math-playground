# 2026-10-07 — All-disjoint equality narrows to four matchings

STEP_ID: 2026-10-07-mca-079-all-disjoint-packing.

One mathematical attempt on the unchanged EXPLORE-ready twelve-incidence
target established [L039](../lemmas/L039-six-coordinate-equality-four-matchings.md).
L032's forbidden actual triple unions and L038's disjoint tag pairs
eliminate profiles t=1,2,3. Equality now requires t=0: four edge-disjoint
perfect matchings on six labels, with a fifth matching as leave. This is
a uniform local restriction, not the twelve bound or a global improvement
to 11/q–16/q. Outcome ADVANCE / RESEARCH / POTENTIALLY_NEW; no certified
originality or progress beyond the sources checked is claimed.

The support-only test also has a precise stopping result. L039's explicit
abstract family passes every current support condition, and its complete
case proof shows that every admissibly paired four-matching construction
has only the selected union-six triple below union size nine. The
[stop record](../ATTEMPTS/021-all-disjoint-support-only-exclusion.md) preserves
that obstruction. All weights, actual moments and finite parameters
remain unresolved. The [attempt record](../drafts/2026-10-07-all-disjoint-packing-attempt.md)
preserves the test and unfinished checkpoint before calculation.

The supplementary exact certificate at
`scripts/all-disjoint-packing/profile-witness-result.json` records all
560 triple checks and 8008 six-subset checks, with zero failures. The
actual minimum six-support union is eleven, required at least nine;
the sole small-union triple is the original six-set. Complete factor,
tagged-triple and summary values were inspected with the shared JSON
inspector. The proof is independent of the auxiliary computed minimum.

Continue the same approved target using actual moment compatibility for
the remaining matching form, a different mechanism from the exhausted
support-only exclusion. Reuse unchanged coverage; no new literature
or field-label sampling was performed. L039 and newer conditional inputs
remain subject to separate critical audits. Preserve all earlier work.

Scoped documentation validation passed: 41 nodes, 67 edges, acyclic
graph, complete file coverage, valid local links and compact overviews.
L039's five direct inputs match the proof: L010/L033 give equality,
L035 gives packing/distribution, L038 disjointness, and L032 forbidden
unions. Tracked notebook whitespace checks passed. Structure and the
supplementary checks do not replace the separate proof audits.
