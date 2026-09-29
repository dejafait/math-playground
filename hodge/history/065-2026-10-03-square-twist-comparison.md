# 2026-10-03 — Square-input-form comparison and geometric return

STEP_ID: 2026-10-03-hodge-065-square-twist-comparison.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint,
the whole proof overview and ID-only DAG. Inspected and
preserved all pre-existing changes, including L036 and the
completed 064 literature review. Reused the exact target's
prior SPECIALIZE assessment without changing it. Reopened
only its already inspected primary statements and proofs
for the required map and transpose conventions; no new
target was investigated in this research turn.

The gap is algebraic realization of U on the fourth RM
direction beyond the Dickson locus. The intermediate target
was the specified q-to-q_a comparison, with controlled action
and algebraic return maps. Its plausible use was realizing
a non-scalar element whose algebraic compositions recover U.
The stated test was an independent modified-cycle supply,
or a demonstration that the supply just encodes the missing
endomorphism.

[L037](../lemmas/L037-square-twist-kuga-satake-comparison.md)
completes that test. The square branch succeeds and the known
isogeny theorem applies. The actual q-based return realizes b
conditionally; under ordinary-kappa algebraicity, algebraicity
of the required modified cycle is equivalent to that of U.
The cycle that is immediately available by transporting the
ordinary embedding has scalar return id. The alternative
q_a tensor convention retains the missing endomorphism too.
This is new scoped evidence for stopping this automatic supply,
not a claim that the modified cycle is impossible or nonalgebraic.

The proof imports van Geemen's polarization/square criteria
and Varesco's compatible isogeny theorem. It reproduces the
conditional retraction mechanism with a geometric transpose
and polynomial inversion, retaining an invertible Gram
operator rather than imposing a scalar conclusion on the
changed form. Precise source versions, theorem numbers and
direct links are in L037 and the unchanged assessment.
Mathlib remains not checked. No originality or mathematical
progress beyond the inspected literature is claimed.

Saved initial unfinished reasoning before the return-map
proof, then linked the finished canonical lemma from that
[note](../drafts/2026-10-03-cubic-rm-polarization-comparison.md).
Preserved the failed recipe in
[ATTEMPTS/028](../ATTEMPTS/028-square-twist-kuga-satake-supply.md).
Updated the proof overview and known-trap check, and added
one DAG node with no local lemma inputs: its field and rank
are explicit hypotheses, and all mathematical tools are
standard named or precisely cited inputs. Earlier lemmas
serve only as route contrasts, not proof inputs.

The attained span remains 21 on the explicit Dickson family,
with three RM directions against four required. Ordinary
Kuga--Satake algebraicity, beta_U supply, arbitrary primitive
fourfold classes and higher-dimensional cases remain open.
There is no complete informal candidate; STATUS stays IN_PROGRESS.
The informative negative resets the consecutive exploration
count after the one review turn, not any external stop state.

The next direction is an independent universal-sheaf source
through a concrete sheaf moduli space, rather than automatic
transport of either the stopped syzygy support or the ordinary
Kuga--Satake embedding. Saved the exact proposed map/action
target with a REVIEW_REQUIRED
[assessment](../drafts/literature/2026-10-03-cubic-rm-universal-sheaf-map.md).
No source coverage, universal family, map or non-scalar
action is asserted; its next turn must be literature-only.

Validation: exact rational polynomial reduction modulo
u^3+u^2-2u-1 checked b^2=a, the displayed b inverse, and
a^{-1}=U^2-U. The proof separately audits polarization,
cohomological direction, geometric transpose, nonzero Gram
operator and algebraic normalization. The documentation checker
`python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 38 nodes and 83 edges, with bytecode writes disabled.
The shared literature validator accepted the unchanged prior
SPECIALIZE assessment, RESEARCH/REPRODUCTION report and pending
new target. `git diff --check -- .` passed. Entry hashes confirm
no deleted file or modified prior lemma, script, assessment or
history. These checks do not verify a Hodge-conjecture resolution.
