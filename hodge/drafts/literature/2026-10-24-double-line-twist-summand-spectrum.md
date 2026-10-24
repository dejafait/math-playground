# Double line twists — summand-spectrum source comparison

TARGET: Assess whether double line twists and the opposite hyperkahler transform constrain every nontrivial slope-zero line summand of L147's M.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched hyperkahler Fourier/ Nahm transforms of zero-degree lines, IT and K3 line-summand multiplicities; freshly inspected BBHR Sections 3.1–3.3 and 4.1, Pareschi–Popa Lemmas 2.1–2.2 with proofs, and Stacks projection/concentration/Leray/duality statements and relevant proofs; compared L093/L147/L154/L155 and the October 12 failure.
SOURCE_EVIDENCE: BBHR (1998), Definition 2 p. 244, Section 3.3 Lemmas 1–2/Theorem 3 pp. 245–246 and Section 4.1 pp. 246–247; Pareschi–Popa author-hosted 28-page GV.pdf, Lemma 2.1 p. 5 and Lemma 2.2 p. 6; Stacks 20.54.2–3 (01E6), 20.13.4 (01F2), 36.31.3 (0BDK), 48.15.7 (0BRT); reuse assessed 0A1H, Fulton GRR and Huybrechts/Perego stable-Hom and Mukai-index coverage below.
COMPARISON: General results cover separate endpoint checks for the opposite transform of each line power, preservation conditional on those checks, the two-projection hypercohomology bridge and stable-type numerical tests. They do not assert acyclicity, scalar self-duality or a multiplicity bound for the added-twist images; L155's untwisted acyclicity cannot be transferred.
GAP: One bounded mathematical specialization remains: prove the new opposite endpoint/rotation conditions, compute its own signed character and cross-twist duality, and compare line multiplicities against the full M constraints after justifying a finite exponent range. No new transform, comparison isomorphism or restriction is proved by this review.
REASON: Essential theorem coverage is ready for the unchanged target as a separate REPRODUCTION attempt; import the cited general results and derive only these data-specific obligations, stopping if the selected constraints supply no additional control.
LITERATURE_REASON: The startup REVIEW_REQUIRED target adds a nonzero source line input to the opposite transform; its every-parameter and duality hypotheses were outside the prior endpoint assessment and are now compared separately.
SCOPE: All nonzero integral base powers L_B^r for the fixed hypothetical equality kernel, with the preferred HE line connections at the original metric; ordinary forward M and W retained, opposite concentration to be proved independently, and only line-type multiplicity constraints and their necessary stable-index tests.

The main gap remains universal primitive rational Hodge realization.
This proposed intermediate target concerns rank-one constituents of the
actual conditional ordinary rank-24 M. A nontrivial restriction could
supply input to a later common-kernel or stable-decomposition test;
it need not exclude F and is not promised to improve 119. Continue
only if the source comparison identifies a controlled multiplicity
constraint or a finite, evaluable test. Park it if every comparison
merely replaces a line multiplicity by an uncontrolled transform.

Retain inputs L052's exact-h line lattice, L071's full equality-kernel
data, L093's untwisted opposite concentration, L147's ordinary complex,
L153's same-h polystability and L155/L156's actual section/dual-section
vanishings. The contemplated coefficients are
F tensor p_1^*L^{-1} tensor p_2^*L_B^r for nonzero integers r, with
L_B of class k on B. This notation is a target, not an assertion of
whole-base twisted IT in either direction. The review must compare
both projections of the same coefficient, retain all point sheaves
and test every required endpoint before importing preservation.

Retain identical marked K3 factors/common g,h, fixed chamber,
hypothetical locally free Omega-polystable rank-two F, integral c_1=0,
ch_2=-14e_1-21e_2-tau_D, k=(-4,-2,1,2), k.h=0,
k^2=-14 eta and integral eta=1; Z finite and possibly empty.
F, nonempty Z, lower control and transport remain unresolved.
M is not assumed simple or self-dual. No mathematical test of these
new twists was performed in step 510. No cross-notebook input is
proposed, and full matching Mathlib coverage is not checked.

## Completed source comparison — step 511

This review approves coverage, without performing the proposed
mathematical specialization. The original proposal and step 510's
noncalculation record above are retained. No claim of a new bound,
line exclusion, transform existence or progress beyond the inspected
sources is made.

**General two-input comparison.** Freshly read Pareschi–Popa,
*GV-sheaves, Fourier-Mukai transform, and generic vanishing*,
American Journal of Mathematics **133** (2011), 235–271,
[author-hosted 28-page version, Lemma 2.1 and proof p. 5;
Lemma 2.2 and proof p. 6](https://people.math.harvard.edu/~mpopa/papers/GV.pdf#page=5).
The first result permits two bounded coherent inputs on projective
varieties and a perfect product kernel, without an equivalence.
The second exchanges derived duality and the dual kernel, with the
source canonical line and dimension shift. Our factors are smooth
projective K3 surfaces, F is locally free, and both proposed inputs
are lines. These hypotheses match. Research must still identify the
ordinary degree-one groups and specialize duality; the results do not
evaluate a multiplicity or identify a twisted image with its own dual.

Freshly read [Stacks 20.54.2–3 and proofs](https://stacks.math.columbia.edu/tag/01E6)
and [20.13.4 and proof](https://stacks.math.columbia.edu/tag/01F2).
Finite locally free base tensoring commutes with ordinary higher
images and derived pushforward; the Leray statement applies to a
bounded-below coefficient. Both proposed line inputs meet this scope.
For the forward projection retain the full L147 complex: tensor its
ordinary M and its top point sheaf W, rather than erase W or postulate
whole-base odd IT. A total-degree-one edge needs its own differential
check, even though L155 provides a model of that check.

**Opposite preservation has a different input.** Freshly read BBHR,
*A hyperkahler Fourier transform*, Differential Geometry and its
Applications **8** (1998), 239–249,
[Section 3.1 p. 243, Definition 2 p. 244, Section 3.3 and its
proofs pp. 245–246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
Theorem 3 permits a quaternionic-instanton source coefficient and
Hermitian quaternionic product kernel with compact source and
compatible spheres. IT requires endpoint vanishing at every target
parameter. Section 3.3 treats rotation independence; Lemmas 1–2
transfer IT and identify natural holomorphic Hermitian bundles.
The source coefficient contemplated here is L_B^r, the kernel is F;
the additional L^{-1} is on the target of this opposite projection.
Research must check the former's preferred HE connection and its
own endpoints against every charge-21 restriction, including all
rotations, before applying the theorem. It cannot use the forward
split-fibre IT failure as an opposite failure. Section 4.1's stronger
inverse/irreducibility results require special reflexive-K3 moduli
hypotheses and are not imported for this kernel.

Reuse the preferred-line HE/ASD and surface contraction coverage in
[step 485's assessment](2026-10-23-preferred-twisted-stable-open-connection.md),
including its metric and parity qualifications, and the real-h
Kobayashi–Hitchin coverage reused there. Tensor powers use the given
HE line connection; zero degree of an arbitrary connection is not a
substitute. This is an applicability obligation, not a new assertion
that the contemplated images are already polystable.

**Base change, duality and full numerical control.** Freshly read
[Stacks 36.31.3 and proof](https://stacks.math.columbia.edu/tag/0BDK):
one-degree fixed-rank derived fibres characterize the corresponding
open vector-bundle concentration locus of a perfect complex. Reuse
0A1H from the October 12 assessment for perfect proper pushforward
and derived base change. The smooth projective projection, locally
free coefficient and base flatness fit; research must supply all
endpoint vanishings and constancy of the middle rank for the new
coefficient. Generic concentration is insufficient.

Freshly read [Stacks 48.15.7 and its diagonal/Koszul proof](https://stacks.math.columbia.edu/tag/0BRT).
It identifies the right-adjoint value on O with omega_p[2] for our
smooth proper relative K3 surface over a Noetherian base. Reuse the
qualified coherent-duality coverage of step 502. For nonzero line
powers, compare the dual coefficient with the opposite power before
assigning a form. L093's symmetric self-pairing is for the untwisted
coefficient; no such form on each new image or on M is approved.

Reuse [step 502's GRR coverage](2026-10-24-opposite-transform-twisted-section-endpoint.md):
Fulton, *Intersection Theory*, second edition, Theorem 15.2,
pp. 286–287 and Example 15.2.8, pp. 291–292. Compute each opposite
image with its own source Todd factor, line exponential, full mixed
tensor, forced higher character and negative R^1 sign. Reuse
[the stable-summand assessment](2026-10-23-twisted-stable-summand-index-bound.md):
Huybrechts, *Lectures on K3 Surfaces*, author draft, Chapter 9
Sections 1.2–1.3 pp. 169–170, Section 3.1 pp. 175–176 and Theorem
4.9 p. 182; Perego (2021), Propositions 3.9–3.12/3.15 pp. 36–38
in the ordinary untwisted case. These cover stable-Hom vanishing,
dual stability, polystable decomposition and the simple Mukai bound
with arbitrary integral first classes, ranks and repeated types.
No new primary read of these reused sources is claimed. They permit
a later numerical line-multiplicity test; they supply no existence
from feasibility. No general theorem needs reproof.

**Bounded discovery and recorded failures.** Queries actually used:
`"hyperkahler Fourier transform" "line" "IT"`,
`"K3" "Fourier" "line bundles" "quaternionic"`,
`"GV-sheaves, Fourier-Mukai transform" "Lemma 2.1"`,
`"hyperkahler" "transform" "line bundles" stable K3 instantons`,
`"K3" "Fourier-Mukai" "line summands" multiplicities`, and
`"Nahm transform" K3 line bundle index stability IT`.
The exact primary comparison and preservation results above were
inspected. Bartocci–Jardim's reflexive-K3 theorem, the author lecture
notes, Jardim's thesis and other search returns are only leads here;
no additional result is imported from their snippets. No exact
all-powers multiplicity verdict for this F was found in the inspected
results; this is not a novelty or exhaustive-absence claim.

The October 12 review stops automatic forward IT, not a separately
verified opposite source-line transform. L155's comparison tests r=0
and its acyclicity is specific to that image. L154's arbitrary-type
index and ATTEMPTS/087 remain valid but supply no independent line
cohomology. Step 510's localized lower-count stop is preserved.
The added input is the same coefficient seen through both projections,
not a renamed localized formula, natural projector or inverse route.

**One ready mathematical test.** Keep TARGET verbatim. First use the
existing exact-h line lattice, full M character, nonnegative z and
stable Mukai inequalities to justify a finite range of possible
nontrivial line exponents; do not truncate by sampling. For each
candidate, test the opposite source-line concentration and preservation,
its full signed character and cross-power duality, then the actual
degree-one comparison and full stable-isotypic multiplicity constraints.
These are approved applications to perform next turn, not results of
this review. In particular no acyclicity of a nonzero-power image is
available. The target can succeed by an additional necessary constraint
or a finite evaluable test; it need not exclude F or improve 119.
If the complete selected comparisons add no restriction to existing
M constraints, record that compatibility and park this filter instead
of requesting an uncontrolled image or assuming its vanishing.

Essential inputs are L052, L071, L093, L147, L153, L154, L155 and
L156 under the retained hypotheses above. Kernel existence, nonempty
Z, independent lower control, other stable summands, transport and
universal primitive Hodge realization remain unresolved. No mathematical
calculation was executed. Full matching and supporting Mathlib coverage
for the new specialization: not checked. No lemma, mathematical script,
DAG row or PROOF argument is changed.
