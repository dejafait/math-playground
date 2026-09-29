# 2026-09-27 — Direct-summand obstruction source comparison

STEP_ID: 2026-09-27-hodge-030-direct-summand-literature.
Outcome: EXPLORATION. Kind: LITERATURE. Classification: NOVELTY_UNCHECKED.

Completed the exact saved target's
[assessment](../drafts/literature/2026-09-27-direct-summand-obstruction-recovery.md)
with decision SPECIALIZE. Read the shared and local instructions,
checkpoint, whole overview and DAG, inspected existing changes and
the relevant recovery proofs and failures, and preserved unfinished
work. This turn contains source comparison only.

Read the corrected Huybrechts--Thomas Corollary 3.4 and universal
obstruction construction, its erratum, Buchweitz--Flenner Corollary
3.13 on naturality, and Stacks tags 07LU, 0H75 and 0654 on nilpotent
reduction, perfectness and Tor amplitude. The assessment gives direct
links, versions, theorem numbers, hypotheses and access qualifications.
The Stacks quotient remarks separate lifting a chosen quotient from
existence of an abstract sheaf lift. The algebraic universal construction
avoids depending on an unchecked passage from analytic naturality.

These are known inputs for citation. The source review supports a
specific test of summand-lift existence, while the geometric application
to all positive m,n still needs its own applicability argument. No
new obstruction formula, flat lift or enlarged union exclusion is
derived here. The proposed mechanism is standard; no originality is
claimed for it or certified for the full local specialization.

The comparison locates L018's use of the degree ordering at the chosen
inclusion step. Its extension recovery and L012's ideal reconstruction
must be checked when that step is replaced. L019 supplies the already
proved support vanishing. The target is worth testing before extending
the L.F>=4 cohomology classification: L020's nonzero group alone does
not decide whether some recovered ideal lift exists. L020 and L021
remain intact, with their stated polarization ranges.

The continuation test is to check central splitting-map naturality,
perfectness of the given sheaf lift, base-relative [0,0] Tor amplitude
of a recovered complex, and applicability of the remaining recovery
steps for every admissible positive pair. An enlarged exclusion needs
all these checks; a failure must identify its precise hypothesis.
The converse still needs the separate section-lifting condition.
No decomposition of the particular middle lift is assumed.

The proved bound remains three RM directions against four required;
the 21-dimensional cycle span and surfaces covered do not increase.
The universal Hodge gap is unchanged. STATUS stays IN_PROGRESS and
there is no complete candidate. This is the first exploration turn
after L021, not an advance or a budget reset. The exact Next action
and NEXT_REVIEW path are retained, now with a completed source screen.

Only the assessment, compact checkpoint and this history entry changed.
PROOF.md and DAG.md retain the existing argument and mathematical
inputs; lemmas/ and scripts/ remain unchanged. Mathlib coverage is not
checked. Documentation and preservation checks are recorded below.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 22 nodes and 51 edges. The shared literature validator
accepted the LITERATURE completion against the saved REVIEW_REQUIRED
entry state, with the exact retained target now assessed as SPECIALIZE.
Content hashes confirm that only the three intended documentation
files changed, including no edits to lemmas, scripts, overview or DAG.
`git diff --check -- .` passed. No mathematical scripts were run;
these checks validate documentation and preservation, not correctness
of an unproved recovery statement or the Hodge conjecture.
