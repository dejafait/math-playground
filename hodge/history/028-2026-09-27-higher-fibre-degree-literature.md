# 2026-09-27 — Sources for the remaining polarization range

STEP_ID: 2026-09-27-hodge-028-higher-fibre-degree-literature.
Outcome: EXPLORATION. Kind: LITERATURE. Classification: NOVELTY_UNCHECKED.

Completed the exact saved target's
[assessment](../drafts/literature/2026-09-27-higher-fibre-degree-ideal-cohomology.md)
with decision SPECIALIZE. Read the shared and local rules, checkpoint,
whole overview and DAG, inspected existing changes and relevant prior
failures, and preserved the unfinished work. The turn remained source
review only; no cohomology or deformation calculation was performed.

The new source evidence includes Franciosi--Tenni's published
[Theorem 4.2, p. 49](https://people.dm.unipi.it/franciosi/lavori/franciosi-tenni2.pdf#page=13)
on normal generation for reduced curves with planar singularities,
and Franciosi's mixed-product and subsystem criteria. Followed their
original reference, reread the K3 multiplication theorem, and reused
the sufficient prior vanishing/regularity comparisons. The assessment
records precise hypotheses, versions, pages and source-access limits.

These are known supporting inputs. None of the inspected statements
identifies the two actual projection subspaces and their global image
in the three-condition descent space. The review justifies that bounded
specialization without claiming novelty or importing the full desired
vanishing. It establishes neither an effective tail nor the required
vanishing from r=1 for every original ample L with L.F>=3.

Completing this range could locate further failures of sufficient
summand recovery for 0<m<n, or confine that cohomological exception to
the already settled range in
[L020](../lemmas/L020-fibre-degree-two-positive-ideal-cohomology.md).
A nonzero group would still leave the actual inclusion obstruction
and transverse cancellation uncomputed. The 21-dimensional span,
three-of-four RM direction bound, m>n>0 exclusion and universal Hodge
gap are unchanged. No complete candidate exists; STATUS stays IN_PROGRESS.

The exact target and NEXT_REVIEW path are retained. The first research
test must keep the original L, actual section subspaces and all three
gluing conditions. Continue this possible escape only on certified
nonzero cohomology; exclude the remaining range only with an all-degree
proof and a justified tail. A partial answer must identify what remains.
This review uses one exploration turn after L020 and does not reset
the budget. No stopped representative is reopened.

Only the assessment, compact checkpoint and this history entry changed.
PROOF.md and DAG.md retain the existing mathematical argument and inputs;
lemmas/ and scripts/ are unchanged. Mathlib coverage is not checked.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 21 nodes and 48 edges. The shared literature validator
accepted the completed turn against its saved REVIEW_REQUIRED entry
state and the exact retained target, with SPECIALIZE ready for a later
turn. Protected-file and overview hashes were unchanged, and
`git diff --check -- .` passed. No mathematical scripts were run; these
checks validate the record and preservation, not mathematical correctness.
