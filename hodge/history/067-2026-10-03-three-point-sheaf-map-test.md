# 2026-10-03 — One-moving-point universal-sheaf test

STEP_ID: 2026-10-03-hodge-067-three-point-sheaf-map-test.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint, the
whole proof overview and ID-only DAG; inspected and preserved
pre-existing changes. Reused the unchanged SPECIALIZE
[assessment](../drafts/literature/2026-10-03-cubic-rm-universal-sheaf-map.md)
for the exact saved map/action target. It explicitly authorizes
the one-moving-point/two-fixed-point specialization. Its audited
moduli model and universal-family prerequisites are imported.
Saved the preliminary reasoning in
[the working checkpoint](../drafts/2026-10-03-three-point-universal-sheaf-test.md)
before the full proof.

The gap is a non-scalar algebraic cubic-RM action on a surface
beyond the Dickson family. An independent global stable family
would supply a cycle through the universal sheaf. The concrete
test required a non-scalar action and stable extension across
collisions; failure of either would stop this recipe.

[L038](../lemmas/L038-one-moving-point-sheaf-map-is-scalar.md)
gives the full proof. Its kernel is flat and stable when all
three points are distinct, but has destabilizing I_p or I_q
subsheaves at the two collisions. The raw ch_2 action is -id;
the c_2 and normalized Mukai actions are +id. Markman's
arXiv:math/0305042v3, equations (32)--(33), p. 23, were re-read
to verify the sign in the already assessed convention.
Chow localization proves that any hypothetical stable extension
agreeing with this family off those two parameter points still
acts as id, including all base-line-bundle normalizations.

This is an informative negative specialization of known tools,
not a claimed new theorem beyond the checked literature. It
does not assert that a stable repair exists or is impossible,
nor classify arbitrary unordered support families or boundary
maps. The attained transcendental contribution is one scalar
dimension against three required by E. No residual cycle or
transverse surface is obtained; the known span remains 21 on
the same family, and three RM directions remain attained
against four required. The general fourfold and higher-dimensional
gaps remain open. STATUS stays IN_PROGRESS; no complete informal
candidate is present. Consecutive exploration use is zero after
this informative negative result; no external runner state was
changed.

Stopped this recipe in
[the attempt record](../ATTEMPTS/029-one-moving-point-universal-sheaf.md).
The reason for the next direction is that the scalar calculation
controls only a specified support family. Before testing other
maps, review whether the generic model admits a global
support-cycle/action reduction retaining boundary strata and
descent. Saved that exact next target as
[REVIEW_REQUIRED](../drafts/literature/2026-10-03-universal-sheaf-global-support-reduction.md);
no derivation or new source screening for it was performed here.

Added L038 to the canonical DAG with no local lemma inputs:
its proof uses the imported source statements and named standard
theorems directly. Updated the argument overview, known-trap
qualifications and sole compact checkpoint. Mathlib remains
not checked. No mathematical script or other notebook was edited.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 39 nodes and 83 edges, with bytecode writes disabled.
`git diff --check -- .` passed. The shared literature validator
accepted RESEARCH / REPRODUCTION under the unchanged prior
SPECIALIZE assessment and the exact new REVIEW_REQUIRED target.
Entry hashes found only the three current-document updates and
five new artifacts; no pre-existing lemma, script, assessment or
other file was deleted or changed. The mathematical checks were
the rank-one Hilbert-polynomial inequalities, the two explicit
collision subsheaves, the source-checked Mukai sign, and the
codimension-two localization argument in L038. No computation
was needed. Documentation validation does not verify mathematics.
