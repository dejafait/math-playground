# Degree-preserving switch falsification attempt

Reasoning saved before generation and rank calculations, then completed
October 6, 2026. This step uses the unchanged EXPLORE assessment at
`drafts/literature/2026-10-06-matching-two-uniform-rank.md` and its exact
COVERED_TARGET. The completed task is a bounded mathematical calculation,
not additional literature review or a universal-rank proof.

The main gap is L010's possible sixteen-count equality versus allowable
fifteen, in the frozen four-omission model. The intermediate target is
rank 28 of the full sixteen-block alternating matrix for admissible
matching-two families, tested on fresh degree-preserving switches.
A future universal result could exclude that branch using the audited
moment-to-alternating mechanism. Larger matching number, arbitrary
triples, full-weight realization, the global bound and ABF26
identification remain independent gaps. No Mathlib coverage is claimed.

Reuse L010's moment independence and L029's exact lexicographic
six-by-28 block convention, the previously inspected exterior machinery,
L023/L024's two-block case, L025/L027 and audited L029/L030 controls,
and L028's cyclic scope limitation. ATTEMPTS/019's exhausted containment
route remains stopped. The previous calculation's complete evidence is
in `scripts/matching-two-rank/`; its all-positive cyclic tests are not
a general theorem and are not repeated as fresh evidence.

Before any rank test, construct and save one ordered plan of at most
256 distinct family/labeling pairs. Enumerate parents from the prior
plan, with 0125/0135 and the two-block family first. In each ordered
parent visit edge pairs and choices x in E_i minus E_j, y in E_j minus
E_i in lexicographic order, replacing those edges by
(E_i minus {x}) union {y} and (E_j minus {y}) union {x}.
Keep only simple sixteen-edge four-uniform four-regular collections
with a disjoint pair and no disjoint triple, unequal to any prior
collection, and failing invariance under v -> v+1 modulo sixteen.
Record every rejected candidate and its reconstructible switch.
Stop generation at 125 distinct qualifying collections, or at exhaustion
of these one-switch candidates. No abstract nonisomorphism is claimed.

Use two explicit bijections (powers of 8 and a fixed seeded shuffle of
sorted H) for each retained family. Include both labels for each known
0125/0135 control and the two-block family first: six baseline pairs,
and at most 250 fresh pairs. Save complete edges and labelings before
rank testing. Stop if there are no fresh qualifying families. A failed
control stops implementation inference; a rank defect stops testing
and must be independently certified using the complete matrix and
a nonzero kernel, not interpreted as MCA equality.

For positives save nonzero maximal minors. Reconstruct all polynomial
rows independently, compare all saved entries, reconstruct annihilators
as actual moment nullspaces, check full-stack ranks and every saved
minor. A certified defect is NEGATIVE for the universal-rank criterion.
All positives are EXPLORATION only and use the third exploration turn;
they require reassessment of the mechanism before further calculations.

## Completed evidence

The complete ordered `scripts/matching-two-switch-rank/plan.json` was
saved before any matrix or rank was formed. Generation visited 1,994
switches: 125 accepted and 1,869 rejected, each because of a saved
disjoint triple. Every visited candidate has its parent, two edge
indices, exchanged vertices, complete rejection reasons and first
disjoint-triple witness recorded. Accepted collections are distinct
from each other and all 63 previous collections, and fail standard
translation invariance. There were no other rejection reasons in this
visited prefix. Generation stopped at the predetermined cap, without
exhausting the switches: 104 retained families came from 0125
(cyclic-39), and 21 from 0135 (cyclic-43). No fresh two-block switch was
reached. These are vertex-labeled collections, not certified abstract
isomorphism classes; hidden cyclic relabelings are not excluded.

All 256 planned pairs were tested: four known control pairs, two
two-block baseline pairs and 250 fresh switched pairs. Every full
96-by-28 matrix has rank 28, exactly the threshold. All four controls
passed; no defect or calculation failure occurred. Complete edge lists
and the two labelings are in the plan. `result.json` in the same
directory saves all 437 distinct support blocks, each pair's ordered
support keys and a nonzero 28-by-28 minor with indices and determinant.
These individual ranks persist under scalar extension because the
displayed prime-field determinants stay nonzero; untested families and
labelings remain uncovered.

The independent verifier imports no search code. It separately checks
the entire saved generation prefix, switch order, all rejection reasons
and witnesses, accepted simplicity, degrees, disjoint pairs and every
disjoint triple, labels and pair identities. For every block, it
reconstructs polynomial coefficients by elementary symmetric functions,
compares every saved row and alternating entry, and independently
constructs the annihilator as the nullspace of the four actual moment
columns, with exponents 1,...,8. It checks equality of the annihilator
spaces and their six-dimensional exterior row spaces. For every pair,
it independently computes both full-stack ranks and checks the saved
minor by column elimination. All 688,128 matrix-entry uses, 437 blocks,
256 ranks and minors pass. Full evidence is in
`scripts/matching-two-switch-rank/verification.json`; previews did not
replace these checks.

Reproduce from the notebook root, preserving the prior plan:

```sh
python3 scripts/matching-two-switch-rank/search.py
python3 scripts/matching-two-switch-rank/verify.py
```

The search reuses the established polynomial/matrix routines in
`scripts/matching-two-rank/search.py`; the verifier reuses independent
coefficient and linear-algebra routines in that directory's `verify.py`.
Prior scripts and certificates are unchanged. No universal-rank
theorem is imported or reproved, and no general rank theorem, equality
exclusion or count improvement is established. Baseline cases are
reproduction; fresh finite tests give evidence beyond inspected source
statements without a novelty claim. Outcome: EXPLORATION.

## Mandatory mechanism reassessment

This is the third mathematical EXPLORATION since the latest ADVANCE.
Stop the current positive-only sampling route, recorded in ATTEMPTS/020.
Positive samples cannot decide every family and labeling; even these
fresh collections may have hidden isomorphisms. Universal rank is not
refuted, and a later independent proof mechanism is not banned.

Three directions address the equality gap. More rank sampling has no
new discriminating threshold after this budget and is not selected.
An all-family exterior-kernel proof needs coverage of arbitrary incidence
beyond L027/L029's patterns; no such target is approved here. A
conditional fixed-block obstruction asks whether six full-weight equality
supports with union at most eight are impossible. This changes L024's
exact doubled-family hypotheses and uses affine restriction, independently
of rank sampling. It need not force that cluster in every family: L025
and ATTEMPTS/017 already refute that universal incidence implication.
The previous small-union assessment explicitly left the affine-moment
application unproved and outside its scope. Select the conditional target
for separate literature review, without deriving or approving it here.
Its hoped-for use is broader conditional exclusion than L024; families
without the cluster and the global bound remain unresolved.
