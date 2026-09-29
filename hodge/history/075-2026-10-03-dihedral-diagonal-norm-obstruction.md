# 2026-10-03 — Dihedral-plus-diagonal stable-lift obstruction

STEP_ID: 2026-10-03-hodge-075-dihedral-diagonal-norm-obstruction.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint,
whole proof overview and ID-only DAG. Inspected existing
changes and preserved them. Reused the unchanged prior
SPECIALIZE assessment; the norm, addition and full
alternating-determinant ideal inputs were already read.
No source comparison or calculation for the changed next
target was started.

The gap was a different representative with a possible
transverse use. The intermediate target was the prescribed
regular degree-three support map on S and its stable lift.
A positive result would permit a later universal-sheaf
deformation test; one noninvertible image-ideal stalk was
the stop threshold. The embedded-union and boundary-action
failures were checked as scoped comparisons, not invoked
as blanket obstructions for this map.

[L042](../lemmas/L042-dihedral-plus-diagonal-has-no-stable-lift.md)
gives the decisive result. The finite flat normalization
cover and norm/addition framework construct the regular
map at every resolved fibre. At each of the three fixed
points over infinity, the full pulled-back norm ideal is
(uv,u^3,v^3)^2, with five minimal monomial generators.
It is nonzero and primary for the height-two maximal ideal,
so it is not invertible. The correctly scoped necessity
criterion in L040 rules out a stable lift on S.

This is new local negative evidence for the notebook's
route decision, obtained as a reproduction of known tools;
no discovery beyond the checked literature is claimed.
The attained span remains 21 on the Dickson family, and
three RM directions remain short of four. No stable family,
transverse surface, new algebraic class or complete informal
candidate was produced; the universal target stays open.

The [stopped attempt](../ATTEMPTS/031-dihedral-plus-diagonal-stable-lift.md)
preserves why the original recipe fails. The retained
[working reasoning](../drafts/2026-10-03-dihedral-diagonal-norm-test.md)
was saved before the proof was completed. PROOF.md records
the changed route and DAG.md adds only genuine mathematical
inputs. Mathlib coverage is not checked, with direct primary
citations retained for the imported portions.

The failure is specific to the original parameter S.
Changing it to a resolution of the image-ideal blowup is
an explicit different mechanism, proposed only for a later
relative-deformation test. Its construction, correspondence
descent and transverse use are not assumed. A fresh
[REVIEW_REQUIRED assessment](../drafts/literature/2026-10-03-resolved-parameter-hilbert-cube-deformation.md)
restricts the following turn to literature review. It must
separate ordinary principalization from actual deformation
and compare any overlap with L009, rather than repeat the
stopped regular-map recipe.

The preceding one exploration turn ended with this decisive
failure, so there are zero consecutive exploration turns.
No launcher, retry state or external research-stop state
was modified. The single authorized research step is complete.

Validation: the exact determinant and monomial script passed.
`python3 -B ../scripts/docs/check_structure.py --problem hodge`
passed with 43 nodes and 88 unique edges. The literature
validator accepted RESEARCH / REPRODUCTION against the
unchanged prior SPECIALIZE assessment and the exact new
REVIEW_REQUIRED target binding. Entry hashes confirmed
only the three current overview files changed and six
intended artifacts were added; all prior work was preserved.
Section order, whitespace, final-newline and git diff checks
passed. Bytecode writes were disabled. These checks support
the exact algebra and documentation; they do not verify
the global mathematical proof.
