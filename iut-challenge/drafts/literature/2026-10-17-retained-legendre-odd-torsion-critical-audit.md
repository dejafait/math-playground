# Retained Legendre odd-torsion criterion — audit coverage approved

TARGET: Critically audit L070's conditional full-15-torsion criterion over unchanged F, including the twist cocycle, complete kernel and limits of the field conclusion.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step272's exact-statement searches, inspected-source comparison and recorded stronger-field-claim warning in drafts/2026-10-17-retained-global-model-source-comparison.md; checked canonical L070, its construction assessment and history/273 for overlap. Step274 retrieved the relevant primary passages for the distinct critical-audit cases; no new discovery search was needed.
SOURCE_EVIDENCE: Sutherland Lecture 21 (6 May 2024), section 21.2 p.2, https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf; Gonzalez-Jimenez/Lozano-Robledo/York arXiv:2408.04159v1, Lemma 3.4 statement and proof pp.12-13, https://arxiv.org/pdf/2408.04159v1; Yvon arXiv:2407.14370v1, Introduction p.2, https://arxiv.org/pdf/2407.14370v1; Sutherland Lecture 20 (1 May 2024), section 20.1 pp.1-2, https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf. Relevant continuous text inspected in step274; screenshot calls supplied no readable image. Reuse foundations/05 step272 for the IUT field prescription, with its version qualification.
COMPARISON: The inspected classification, transported-basis formula, full-coordinate kernel convention and closed-subgroup correspondence cover the audit's standard inputs. SPECIALIZE authorizes only checking their retained application and proof logic in L070, including the trivial and nontrivial character cases; it does not certify that application or authorize the stronger division-field clause.
GAP: Source coverage for this conditional audit is adequate; the separate mathematical audit remains undone. Native T, the actual descent and character, minimal generation and the original numerical comparison remain unresolved and outside this approval.
REASON: The pending audit now has a case-by-case source boundary, including the formula's placement inside a stronger source hypothesis. Proceed next to mathematics using this coverage; do not repeat source approval absent changed hypotheses or a specific uncovered input.
SCOPE: Only the stated conditional criterion for the same E_0,F and specified E_L over conditional native T subset F; no actual T/lambda/character determination, new descent, field change, exact generation, numerical comparison or IUT flaw claim.

Essential inputs: L045,L048, canonical L070 and foundations/05 step272.
L060 and step271 are conditional native setup only, not proofs of T's
identification. Keep the same Omega, embedding, u,w,H,N,K_glob,
precision M>=max(M_tors,31) and changed q_0 with v_3(q_0)=30.

The review should check that nonexceptional j suffices for sign-valued
automorphisms over the common field, that a geometric pointed
isomorphism is obtained without assuming full torsion on E_L, and
that every sigma in G_F is tested using L045's trivial representation.
Confirm -Id!=Id at level 15, and that the fixed-field conclusion is
only the square-root test over F. The source inputs are approved below; the research audit must still
check their application to every claimed step.

The actual native character, T and minimal generation remain unresolved
even if the conditional lemma passes. The comparison must not silently
use the stronger part (2) equality excluded in step272. A pass validates
only this conditional known-result specialization; a failure must
identify a precise defective hypothesis or inference. Matching and
supporting Mathlib coverage remains unchecked. No mathematical audit or new derivation is performed in this literature turn.

## Step274: inspected cases and audit boundary

LITERATURE_REASON: The separate critical audit was REVIEW_REQUIRED;
its essential source cases and the boundary of the reused formula
needed approval, rather than another search for a construction theorem.

Lecture 21 section 21.2 covers twists as a cohomology set and the
nonexceptional-j sign-automorphism case, including trivial twists and
quadratic fixed fields. It supplies the classification input for a
pointed geometric comparison. The audit must check that L070 invokes
this elliptic-curve category and does not infer its geometric comparison
from the torsion rationality it is trying to test.

Lemma 3.4 is stated for a number field, a short nonsingular equation
and N>2. Its proof on p.12 specifies both transported basis points
and the scalar-sign matrix formula. The formula appears after the
extra assumption that the quadratic radical is outside the original
division field. The coordinate calculation itself uses the quadratic
isomorphism; the later choice of a nontrivial Galois element uses that
extra assumption. The audit must check this boundary explicitly for
all cases, including a radical already in the base field. Part (2)'s
stronger field equality remains excluded, with no new verdict on it.

Yvon's Introduction p.2 defines division fields using point coordinates
and identifies their kernels. Lecture 20 section 20.1 supplies the
rank-two finite torsion module and the closed-subgroup fixed-field
correspondence. These are the inputs for auditing the entire restricted
kernel, rather than an image group or one element. No effective
coefficients, native field equality or new descent theorem is required
for this conditional target.

The local duplicate/failure comparison is unchanged: L070 already
contains the construction; this approval does not repeat it.
ATTEMPTS/028 concerns a different model quantifier; the stops in
ATTEMPTS/027,031,032 are not reopened. No extra theorem is imported
from those routes. Full matching and supporting Mathlib coverage is
not checked and is not needed to authorize this informal audit.

Continue with the exact saved audit target, using L045,L048,L070 and
foundations/05 step272. A successful audit validates only the conditional
known-method specialization. Any failure must identify the defective
hypothesis or inference and preserve the unfinished work. Do not proceed
to exact generation without an independently justified actual character.
This is source-coverage progress only, with no result beyond the sources.
