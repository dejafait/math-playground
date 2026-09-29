# 2026-10-03 — Support-preserving stable-lift criterion

STEP_ID: 2026-10-03-hodge-071-degree-three-stable-lifting-criterion.
Outcome: ADVANCE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint,
whole proof overview and ID-only DAG. Inspected and preserved
pre-existing changes. Reused the ready SPECIALIZE assessment
for the exact saved target without modifying its bytes.
Saved the incomplete boundary argument before completing it
in [the working record](../drafts/2026-10-03-stable-support-lifting-test.md).

The gap was compatibility of the global Hilbert-cube model
with the actual weighted support, followed by precise lift
conditions including images contained in collision strata.
The test required all-fibre agreement and correct exceptional
data; its use is screening a future independent support-map
construction for a non-scalar universal-sheaf action.

The full proof is [L040](../lemmas/L040-degree-three-support-stable-lifting-criterion.md).
The specified Yoshioka transform identifies O_Z with the
finite-length dual of the hull quotient, up to its coefficient
line. Punctual lengths are preserved, so Hilbert--Chow is
actual weighted support on every stable fibre. Agreement of
parameter morphisms uses all closed points and reducedness,
and covers entirely boundary-contained images.

The imported ideal-of-norms blowup and relative-Proj theorem
now give necessary and sufficient stable-lift data: a line
bundle quotient respecting every pulled-back Rees relation.
For maps generically outside the centre, invertibility of
the image ideal is necessary and sufficient, and the lift
is unique. Entirely exceptional maps require the full data;
a constant punctual Hilbert-cube map lifts even with zero
image ideal. No blanket lift-existence assertion is made.

Read Yoshioka's Proposition 3.4 and its actual transform,
Ekedahl--Skjelnes' section 7.24 and surface Corollary 7.28,
and Stacks Tags 01O4 and 0806 to check these applications.
The global model, blowup and Proj theorems are imported;
only the support comparison and applicability difference
were specialized. This is local progress by reproduction
of known tools, not claimed progress beyond the checked
literature. Mathlib coverage remains not checked.

The saved continuation test passes. No new non-scalar cycle
or transverse surface is supplied: span 21 on the Dickson
family, three RM directions against four required, and the
stopped scalar recipe's one direction against three required
remain unchanged. The universal Hodge gap is open, STATUS
remains IN_PROGRESS, and no complete informal candidate exists.

The next direction screens whether entirely boundary-contained
maps can supply a non-scalar action; lift existence alone
does not answer that question. The changed target is saved
as [REVIEW_REQUIRED](../drafts/literature/2026-10-03-cubic-rm-boundary-support-action.md).
No calculation on that target was performed here. Consecutive
exploration use is zero after this mathematical input; no
external research-stop state was changed.

Added L040 to the DAG with L039 as its sole direct notebook
input. Earlier recipe failures are contrasts, not inputs.
Updated the relevant overview and sole compact checkpoint;
all earlier lemmas, scripts, assessments and inactive branches
were preserved.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 41 nodes and 84 unique edges; bytecode writes were
disabled. `git diff --check -- .`, new-artifact whitespace and
lemma-section-order checks passed. The literature validator
accepted the unchanged prior SPECIALIZE assessment, RESEARCH /
REPRODUCTION and the changed next target's REVIEW_REQUIRED state.
Entry-hash comparison found only the three intended current
document changes and four new artifacts, with no deletion or
change to earlier proofs, scripts or assessments. The triangle,
punctual-length, reducedness and generic-nonzero-inclusion checks
are in the informal proof; no numerical test was needed. These
documentation checks do not verify the Hodge conjecture or
certify originality.
