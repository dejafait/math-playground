# 2026-09-27 — Direct summands remove the complete-intersection degree ordering

STEP_ID: 2026-09-27-hodge-031-direct-summand-union-recovery.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Reused the unchanged prior SPECIALIZE
[assessment](../drafts/literature/2026-09-27-direct-summand-obstruction-recovery.md)
for the exact saved target. Read the shared and local rules, whole
overview and DAG, inspected existing changes, and retained prior work.
The assessed sources were sufficient; no new browsing or general
obstruction-theory reproof was needed. The
[working draft](../drafts/2026-09-27-direct-summand-recovery-test.md)
preserves the intermediate checks and their completion.

[L022](../lemmas/L022-direct-summand-recovery-all-positive-degrees.md)
proves recovery of some flat coherent ideal-sheaf lift from any lift
of the split central middle sheaf. It imports the corrected
Huybrechts--Thomas criterion and naturality, then uses the reviewed
Stacks perfectness and Tor-amplitude criteria to pass between perfect
lifts and base-flat sheaves. The central inclusion and retraction
are used only in the obstruction identity. No splitting or specified
inclusion inside the given lift is claimed. Determinant/Hartogs
recovers the embedded ideal, retaining the three singular points.

The remaining extension calculation in L018 uses only positive m,n,
not their difference; L019 supplies its required support vanishing.
Thus the union exclusion now covers every admissible m,n>0, including
m=n and m<n. This changes the route decision: the nonzero group in
L020 and further L.F>=4 inclusion-cohomology calculations cannot
provide a first-order escape. L020 and L021 remain intact. The
converse still requires H^1(X,I_C(nH))=0 to lift the chosen f; without
it only containment in V_D is proved.

This is a reproduction/application of known obstruction and flatness
theory, with a checked specialization to the saved geometric target.
The review found no statement of the full union assertion, but no
originality or mathematical discovery beyond the sources is claimed.
Mathlib coverage is not checked. The informative negative result
resets exploration turns used to zero. It leaves at most three of
four RM directions, the same 21-dimensional span and the same set
of surfaces covered. STATUS remains IN_PROGRESS; there is no complete
candidate for the universal Hodge conjecture.

Updated the overview and the existing attempt record to reflect the
all-positive-degree exclusion, preserving their earlier results. The
new DAG row records only the embedded-support obstruction, ideal
reconstruction, union sequence and support vanishing actually used.
The cohomology examples are comparisons, not extra mathematical inputs.

Registered a separate
[REVIEW_REQUIRED assessment](../drafts/literature/2026-09-27-ramified-complete-intersection-union.md)
for a ramified order-two test with arbitrary first-order motion. This
is a different mechanism because the ambient direction first appears
at order tau^2. The proof above recovers existence of some central
summand lift and does not extend prescribed earlier data. L016's
test concerns a different representative. No calculation for this
new target was performed; its next turn must be literature-only.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 23 nodes and 55 edges. The literature validator accepted
RESEARCH / REPRODUCTION against the unchanged prior SPECIALIZE
assessment and the exact new REVIEW_REQUIRED target. Hash comparison
with the entry snapshot found only the eight intended notebook
changes, with all old lemmas, scripts and assessments unchanged.
`git diff --check -- .` passed. The mathematical checks are the
central naturality identity, the two distinct derived-reduction
criteria, the extension exact sequence and ideal reconstruction
written in L022; no numerical script is needed for these arguments.
These checks do not constitute verification of the Hodge conjecture.
