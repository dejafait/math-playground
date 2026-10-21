# Bounded matching-two full-rank falsification attempt

Completed bounded test, October 6, 2026. The saved EXPLORE assessment is
`drafts/literature/2026-10-06-matching-two-uniform-rank.md`; its exact
COVERED_TARGET approves this attempt. No new source review is needed.

The main gap is sixteen-count equality versus the allowable fifteen in
L010's frozen four-omission cell. The intermediate target tests whether
every admissible matching-two support family has full alternating rank
28 at every fixed-H labeling. A future universal proof could exclude
that branch through the audited alternating mechanism. Larger matching
number, arbitrary triples, ABF26 identification and the global bound
remain independent gaps. A rank defect rejects the universal criterion;
it does not supply decomposability, full weights or distinct parameters.

Before calculating ranks, save the full ordered plan on disk: the 62
saved cyclic entries plus L023's two-block family, each under four
explicit bijections (powers of 8, sorted H, powers of 8 with vertices
0 and 1 exchanged, and one seeded shuffle). This is 252 distinct
family/labeling pairs, below the approved bound 256. Put the proved
0125 and 0135 controls first, then the two-block family, then the other
cyclic entries. Check all family hypotheses directly; no containment
search or arbitrary-family classification is performed. Record rejected
candidates and failures. Stop on the first defect or failed control.

Use L029's lexicographic six-by-28 block convention, all sixteen blocks.
For positive tests save a nonzero maximal minor. A defect must have a
nonzero rank-sized minor, the complete kernel, all matrix rows and an
independent reconstruction from moment nullspaces. Verify every matrix
entry and every kernel residual, retaining the full certificates on disk.
All-positive evidence is EXPLORATION only. A certified defect is NEGATIVE
for this universal-rank mechanism and requires a different next target.

Existing L023/L024, L025/L027, L028 and L029/L030 retain their scope;
ATTEMPTS/019's exhausted containment route is preserved. Ready source
comparisons and proof audits are reused. No cross-notebook input or
Mathlib coverage claim is made.

## Completed evidence and limits

The frozen `scripts/matching-two-rank/plan.json` contains all 252
distinct ordered family/labeling pairs before any rank calculation.
It has 63 distinct families as labeled vertex-set collections: the
62 saved cyclic entries and the two-block family. This does not mean
63 isomorphism classes. The four full label lists are explicit in the
plan. All candidate families passed simplicity, edge size, degree,
disjoint-pair and exhaustive disjoint-triple checks; there were no
rejected families. This test generated no switched families.

`scripts/matching-two-rank/result.json` saves the complete 1697 support
blocks used, all 252 tested input references, selected row indices and
nonzero 28-by-28 minor determinants. Every 96-by-28 stack has rank 28.
All eight 0125/0135 control pairs passed. All four labelings of the
two-block family also passed. No defect, failed control or partial
matrix exception occurred. The target threshold was 28 and every
actual rank was 28, over F_97; these individual rank certificates
remain valid under scalar extension, without extending the coverage
to other labelings or families.

`scripts/matching-two-rank/verification.json` records independent
verification by `verify.py`, which imports no calculation code from
`search.py`. It reconstructs every polynomial row by elementary
symmetric functions rather than sequential multiplication, compares
every saved matrix entry, constructs each annihilator independently
as the nullspace of the four actual moment columns, and checks equality
of the corresponding six-row exterior spaces. It independently
computes the rank of each full moment-annihilator stack and verifies
each saved maximal minor using column elimination. All 677376 matrix
entry uses, all 1697 distinct blocks, all 252 minors and all 63
incidence families pass. In particular, a preview or control does
not substitute for the full entry and determinant checks.

Reproduce from the notebook root:

```sh
python3 scripts/matching-two-rank/search.py
python3 scripts/matching-two-rank/verify.py
```

This is EXPLORATION, not a theorem about every matching-two family,
an informative negative result, a new equality exclusion, or a global
count improvement. The existing known controls are reproduction;
the remaining finite tests are local evidence beyond the inspected
source statements, without certified originality. No lemma was added,
and the mathematical assembly in PROOF.md and DAG.md is unchanged.

The full-rank route remains testable beyond these cyclic collections.
The already assessed scope permits degree-preserving changes of
supplied families. A single further bounded test can exchange vertices
between two edges, retain only simple four-regular matching-two
families, and test fresh pairs. It must distinguish edge collections
that fail invariance under the standard vertex translation from saved
full translation orbits, without claiming new abstract isomorphism
classes, record rejected candidates, and stop on an independently
certified defect or failed control.
The current checkpoint selects that discriminating continuation under
the unchanged assessment; no rank of a switched family is inferred here.
