# Mixed-moment collision — proposed separate critical audit

TARGET: Critically audit L046's nine-set collision certificate and fixed-map nonseparation conclusion.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the bounded searches recorded in 2026-10-10-column-aware-syndrome-packing.md and the separately approved fixed-map comparison; inspected L046, L045 hypotheses, ATTEMPTS/030 and history/134–135 for scope and duplicates.
SOURCE_EVIDENCE: Harm Derksen, Error correcting codes and B_h-sequences, arXiv:math/0311385v1 (21 November 2003), https://arxiv.org/pdf/math/0311385v1, Definition 1, Proposition 2/full proof, Corollary 4/full proof and Theorem 5(a,b), printed pp. 2–3; reuse the primary-text inspection recorded in 2026-10-10-mixed-moment-syndrome-test.md.
COMPARISON: Derksen requires a B_4 sequence on indexed points; no inspected theorem asserts separation for this mixed-moment map. L046 claims a direct finite obstruction, so auditing it requires no new theorem application or reproof of Derksen.
GAP: Independently verify the two complete nine-sets, profiles, all four syndrome coordinates, full intersection and the limited nonseparation inference; the certificate and proof have not been critically verified in this literature turn.
REASON: Separate approval of the saved critical-audit target reuses adequate unchanged coverage; it is a process step, not fresh mathematical evidence or a novelty claim.
SCOPE: Only independent critical audit of the existing L046 witness and its fixed-map conclusion; no new map, packing bound, exhaustive search or RS realization.

Proposed inputs: L046 and L045's universe/conflict definitions;
the complete selected witness in
`scripts/finite-support/mixed-moment-collision-results.json`.
Independently reconstruct the arithmetic, without requiring search
exhaustiveness or implying that every fiber conflicts. Check the
canonical DAG input and the restriction of the stop to this map's
universal-separation prescription. No new map, packing bound or
source theorem application is proposed.

## Separate scope approval, 2026-10-10

The saved parent assessment contains the actual search queries and
the inspected primary hypotheses/proof cases. Its comparison remains
within scope: Definition 1 allows repeated indices, and Proposition 2's
cancellation/padding proof requires the B_h property for indexed terms,
including smaller differences. For these nine-sets the indices are
pairs (c,x), whereas the first three coordinates use x alone.
Theorem 5 requires distinct field labels and a polynomial nonzero at
them; it is not a theorem about the displayed mixed moments.
Corollary 4's pigeonhole guarantee is therefore not an imported premise
of this audit. No source refresh or new broad search is necessary.
The unread Graham–Sloane lead recorded in the parent assessment is
not essential to checking this explicit finite witness.

L045's hypotheses fix all labeled profile placements and the conflict
threshold. L046's full statement and proof were read to identify the
load-bearing checks, not to certify their correctness. ATTEMPTS/030
and history/135 preserve the same map-specific stop; history/134
approves the original test, not the separate critical audit. No duplicate
completed independent audit was found in those records.

Approve EXPLORE for the exact TARGET in the next research turn. Read
the complete selected /witness certificate value using the local JSON
inspector with --full, reconstruct its blocks independently and compare
all load-bearing entries against L046. Check that ordered pairs, not
values alone, determine intersection, all modular reductions are exact,
and the DAG's L045 input covers the definitions. No search-exhaustiveness
claim is needed for a negative witness. Retain the stop only if the full
checks pass; otherwise record the specific failed assertion and repair
or withdraw that assertion while preserving prior evidence. Passing
checks cannot exclude all fibers or compatible subfamilies.

This approval contains no new derivation and does not complete the
audit. Its later research classification is REPRODUCTION: independent
verification of an existing local result, without an originality claim.
Mathlib coverage is unchecked. L043 is downstream context only. Useful L041 caps,
L042/application audit, actual-label transfer, cross-core consistency,
common-center RS realization, 67/68 safety and ABF comparison remain open.
