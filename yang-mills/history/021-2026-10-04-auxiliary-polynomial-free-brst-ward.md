# 2026-10-04 — Polynomial free BRST Ward identity and regulator removal

Completed one mathematical specialization of the exact saved target under
the unchanged SPECIALIZE [assessment](../drafts/literature/2026-10-03-auxiliary-brst-ward-identity.md).
[L014](../lemmas/L014-auxiliary-polynomial-free-brst-ward.md) extends
L013 to every auxiliary/ghost polynomial, retains the Grassmann parity
sign and the positive connection regulator's breaking insertion, and
proves convergence and zero breaking after removal at each fixed mesh.
This is ADVANCE / RESEARCH / REPRODUCTION: a relevant local Ward input
using known finite-dimensional machinery, with no claim beyond the
checked literature.

The [working record](../drafts/2026-10-04-auxiliary-polynomial-brst-ward.md)
preserves preflight, unfinished reasoning and completion. The
[exact check](../scripts/auxiliary-cochains/check_ward.py) passes 8,580
rational polynomial identities on the complete N=2 relative cube,
including nonzero regulated defects for mixed antighost insertions.
PROOF.md incorporates the free identity and its fixed-mesh limitation;
DAG.md records L013 as L014's direct mathematical input. The existing
source assessment, earlier lemmas and scripts, unfinished nonlinear
work and prior stopped mechanisms remain preserved.

No error bound toward the required interacting reflected threshold
<= c_box/2 improves. Nonlinear Wilson-measure replacement,
physical-boundary subtraction and remainder, finite matching on a
specified coupling trajectory, continuum fields, full limiting reflection
positivity, infrared removal and finite positive mass remain missing.
STATUS stays IN_PROGRESS; no complete candidate exists. The zero-regulator
joint modulus remains nonintegrable, and no mesh-limit interchange is used.

The next direction screens a global smooth compact SU(2) BRST gauge-fixing
normalization before any nonlinear replacement. Its compact nonabelian
hypotheses lie outside the completed free assessment, so a separate
[REVIEW_REQUIRED record](../drafts/literature/2026-10-04-compact-brst-gauge-fixing-normalization.md)
is saved without deriving a nonlinear result or doing literature work.
PROGRESS.md alone records the current checkpoint and exact next action.

Validation: the exact Ward check and the shared documentation checker
with --problem yang-mills passed (14 nodes, 23 unique edges). All 29
pre-existing lemma/script/assessment hashes are unchanged; metadata and
the exact next-target match pass read-only checks. The proof was checked
for phase, orientation, parity, normalization and domination of the
breaking insertion. No runner state or shared infrastructure was edited.
