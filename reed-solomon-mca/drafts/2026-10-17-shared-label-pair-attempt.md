# Shared-label isolated-pair attempt

STEP_ID: 2026-10-17-mca-273-shared-label-pair-test

The unchanged EXPLORE assessment is
`literature/2026-10-17-shared-label-isolated-pair-test.md`.
The main gap remains L010's sixteen-count equality. The intermediate
target is exactly the two full isolated recoveries through the named
shared label a, with all five supports pairwise linear. Exclusion could
obstruct equality's two additional occurrences at a; a full witness
abandons only that shortcut. Independent completion, uniform triangle
twelve, arbitrary support families and challenge definitions remain open.

L057's full statement and proof and L041's local-converse statement and
standard-input specialization were read. ATTEMPTS/036–037 stop disjoint-P
cross-differences and common-weight elimination; neither is resumed.
L053's different tau-one scope was compared and is not invoked.

## Saved before calculation

Linearity with A0={a,b,Y} and A1={a,c,Z} forces an additional support
through a to be {a} union S, with S in H minus (A0 union A1), |S|=3.
Linearity with A2={b,c,W} requires |S intersect W|<=1; two such
supports are linear iff their outside triples are disjoint. Thus J={b,c}
in L057, its two projected vectors have length two, and equations
(10)–(11) determine q,r but impose no equation on p. The test is to
find two isolated rows with distinct eligible mu and the same gated q,r,
then choose gated p and an original finite chart, and verify both full
errors by all eight moments. This is a direct use of L057 rather than
a disjoint-P elimination or an asserted rational-weight reduction.

A deterministic actual-label enumerator will search triangle assignments
and admissible outside triples, stopping on a complete candidate for
independent verification. It begins with a=1 but loops actual labels;
no role permutation or label symmetry is assumed. Search-prefix failures
will prove no exclusion. A candidate is not evidence until every finite
gate, recovered nonzero weight and all ten intersections are checked.
The complete positive certificate, if found, is sufficient; a full label
census is unnecessary for an existence claim. No new recurrence theorem
or general coding theorem is to be reproved.

Continuation/abandonment test: accept coexistence only on the full
certificate, or accept uniform exclusion only on a proof covering every
label, extension weight and finite chart. Stop this attempt without a
new theorem if it produces only projected candidates, negative samples
or the stopped L064-style comparisons.

## Completed result

The search found a projected pair after 155,829 triangle assignments.
The separate Gaussian/eight-moment replay completed the full witness:
40/40 moment equations, five full errors, two nonzero isolated
proportional projections, five distinct finite parameters and all ten
linear intersections, with zero failures. Complete relevant certificate
fields were inspected. The canonical exact proof and tables are
[L101](../lemmas/L101-shared-label-isolated-pair-witness.md); do not
duplicate them here. The certificate is
`scripts/triangle-recovery/shared-label-pair-verification.json`.

Outcome NEGATIVE: coexistence refutes the local exclusion shortcut;
ATTEMPTS/039 preserves this stop. The search prefix is not a uniform
census, and the result supplies no equality completion or count bound.
No originality beyond the checked coverage is asserted. L101 needs a
separate critical audit; its newly proposed scope is REVIEW_REQUIRED,
not approved or audited in this construction step. The direct existing
inputs are L010/L041/L057; L086 motivates the explicit linearity gate
only and is not invoked as an equality theorem here.
