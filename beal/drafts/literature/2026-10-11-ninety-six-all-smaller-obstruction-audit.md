# All smaller auxiliaries — critical-audit source coverage

TARGET: Assess source and verification coverage for a critical audit of L056's exhaustive subgroup enumeration and rank-14 obstruction for all smaller auxiliary fields in MN.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-group discovery in drafts/literature/2026-10-11-ninety-six-all-smaller-auxiliaries.md; inspected L056, L055's canonical audit, ATTEMPTS/022-023 and history/155; compared the custom evidence schema with primary enumeration methods.
SOURCE_EVIDENCE: Reuse Etienne https://arxiv.org/pdf/2411.13124v2 Proposition 2.7 pp.12-15 and orbital correspondence pp.5-9, and the prior FNS/Milne field-interface review; newly inspected Hulpke https://arxiv.org/pdf/2012.01595v1 Section 3.2 pp.8-9 and GAP https://gap-system.github.io/gap/doc/ref/chap39_mj.html Section 39.21-1; reuse pinned GAP v4.15.1 bounded-index coverage.
COMPARISON: Known criteria cover the finite Galois overfield, all rational maps and arbitrary copies; documented cyclic extension requires perfect seeds and does not directly certify L056's custom arbitrary-element backend. Its existing completeness proof and full evidence require independent audit.
GAP: Independently reconstruct the audited group/action and multiplication, verify every class/normalizer/reducing orbit/fusion witness and exhausted frontier, then every index-below-36 map and exact rank; none was executed this turn.
REASON: The changed implementation's verification obligations are covered for a separate reproduction audit; source approval neither confirms L056 nor changes the existing MN-only stop.
SCOPE: Exactly TARGET and the covered audit below, including corrections to existing L056 claims; no new auxiliary mechanism, subgroup classification, arithmetic or branch exclusion.
COVERED_TARGET: Critically audit L056's exhaustive subgroup enumeration and rank-14 obstruction for all smaller auxiliary fields in MN.
LITERATURE_REASON: The saved gate requires separate review of the custom backend and its independence obligations; ready Etienne coverage is reused rather than rediscovered.

Essential inputs are L051's degree-36 field, audited L055's actual MN and
sign fiber-product group, L056's entire proof and complete certificate,
and Etienne's cited arbitrary-copy criterion. No cross-notebook input.
The original pair stop and ATTEMPTS/018-023 are retained.

The proposed audit must check the equivalent enumeration's coverage,
especially perfect subgroups, all conjugacy fusion witnesses and the
unfiltered frontier, rather than assume GAP was run. Independently
verify every index-below-36 subgroup and every orbital map, the
coordinate-sum upper bound and the audited-pair lower bound 14 (or exact
rational rank). A correction requires preserving prior evidence and
revising the actual failed claim. Confirmation parks smaller auxiliaries
in MN only. Auxiliary arithmetic, all original descent obligations,
other twists and residual signatures remain unresolved.

## Primary comparison and applicability

The main gap remains unconditional emptiness of L032's 96a1 branch.
The intermediate target is independent verification of the existing
smaller-field obstruction. Its downstream use is reliable routing before
auxiliary arithmetic. Complete coverage and rank evidence retain the
MN-only stop; an error requires correction and reassessment with prior
evidence preserved. An incomplete check leaves verification pending.

Reuse the theorem/proof coverage in
`drafts/literature/2026-10-11-ninety-six-smaller-auxiliary-coverage-test.md`
and field-interface coverage in
`drafts/literature/2026-10-11-ninety-six-two-auxiliary-obstruction-audit.md`.
Etienne v2, April 23, 2025, Proposition 2.7 and Definition 2.9 cover a
finite group, target subgroup H and nontrivial auxiliary subgroups, with
arbitrary module multiplicities. Proposition 1.3 and the assessed
Definitions 1.8/1.10, Lemmas 1.11-1.12 and Proposition 1.13 cover the
orbital/compositum interface. L051 and audited L055 supply the actual
overfield MN, H and degree 36. Bound 35 leaves all auxiliary subgroups
nontrivial; conjugacy representatives require all maps. No normality of
L96, GRH or class completeness is needed here. Cite these criteria;
no general theorem reproof is justified.

New primary inspection: Alexander Hulpke, *Calculating Subgroups with GAP*,
arXiv:2012.01595v1, December 2, 2020, Section 3.2, printed pp.8-9,
describes normalizer-element cyclic extension after perfect-subgroup
initialization. Its database alternative requires an actual isomorphism
to the concrete input. GAP Reference Manual, accessed 2026-10-11,
Section 39.21-1 warns that upward filtering can lose desired subgroups
and requires perfect seeds unless the filter implies solvability.
Neither source certifies L056's arbitrary-element procedure or counts.
Previously inspected bounded-index coverage and the pinned GAP v4.15.1
method remain alternatives, not execution claims. No runtime bound is used.

L056 already contains a generator-prefix completeness argument for its
unfiltered arbitrary-element procedure. This approval permits review of
that existing argument and implementation, not a new derivation here.
The audit must check why its reductions preserve extension classes and
its initial/frontier conditions cover every subgroup, including perfect
ones. It cannot borrow Hulpke's perfect-seed completeness while omitting
seeds. A full independent certificate check can suffice without GAP/Sage
or a classification catalogue if the existing proof obligations pass.
A backend or resource failure leaves the audit unfinished.

## Independent verification obligations

Read-only `all_smaller.py` inspection identifies the evidence layout,
not correctness: the driver reads the older group certificate and uses
the C-produced multiplication table throughout verification. Rerunning
that driver or trusting its zero-failure field does not independently
verify the group/table. The `/enumeration` JSON inspection was a bounded
preview only; no certificate was verified this turn.

The separate audit must:

1. Reconstruct L055's sign-compatible action from its audited specification,
   compare every group and target permutation, and verify the entire
   multiplication table against composition, including byte order,
   identity/inverses, generator closure and H. Check artifact provenance
   and source hashes; hashes identify evidence but do not prove it.
2. Check the trivial initial representative, every generated subgroup,
   full normalizer and reducing-orbit partition of all 3,960 elements,
   and every extension equality with its conjugating witness. Check every
   discovered class was processed and the frontier exhausted, without
   upward index filtering. Audit the existing induction/reduction proof.
3. Check each representative occurs in its full conjugacy orbit, every
   conjugating witness, distinct full subgroup sets, generator closure
   of each orbit and disjoint class fusion. Confirm 67 classes and 6,906
   actual sets from full evidence rather than summary counters.
4. Select every subgroup of exact index at most 35 after full coverage;
   reconstruct all left cosets, J-orbits on X and map entries. Confirm
   seven qualifying classes, 12 maps and 121 columns or report discrepancies.
   Check the existing Hom-space identification and conjugacy invariance.
5. Check every mixed coordinate difference, the existing dimension-14
   argument and L055 lower bound, and independently compute rational rank
   against required 36. Compare full pivots/reduced matrices if verifying
   the saved row reduction. Audit arbitrary-copy criterion applicability.

Full artifacts are L056's main certificate and classes, conjugates and
multiplication companions under `scripts/ninety-six-generalized-relation/`.
The audit must load complete relevant evidence and save its own certificate
without overwriting originals. It must not import the original backend or
driver's verification routines as its independent justification. A second
enumeration is optional; its completeness still requires justification.

## Duplicates, qualifications and continuation

ATTEMPTS/022 is the audited pair stop; ATTEMPTS/023 is the larger existing
stop pending review. Neither is reopened by this source approval.
ATTEMPTS/018-021's workload/normality failures remain. The reused exact-group
search found no inspected source deciding this field-specific enumeration
and rank; that is not evidence of novelty. Unread catalogue/book leads
remain unread and are not essential to the certificate-based audit.

Confirmation retains only the smaller-auxiliary stop in MN. Equal/larger
fields, other overfields, arithmetic completeness, saturation/transfer,
torsion lifts, support/norm maps, descent compatibility and full-disk
disjointness remain unresolved. No integer branch emptiness follows.
Mathlib matching/supporting coverage is not checked; unknown is not absence.
Completed task is LITERATURE / NOVELTY_UNCHECKED; the covered audit is
RESEARCH / REPRODUCTION under SPECIALIZE. No result, lemma, mathematical
script or calculation was supplied. The newly covered continuation receives
separate supervisor approval next turn; completed source work and prior
negative evidence stand.
