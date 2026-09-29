# Two-way rotation-sheaf Yoneda products — literature assessment

TARGET: Compute whether the mixed Yoneda products between O_C and O_(C^(2)) can cancel the diagonal order-tau^2 Atiyah obstruction of O_C direct sum O_(C^(2)) for a product coefficient in V_RM outside V_D.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact K3/Dickson/rotation Yoneda targets, quadratic sheaf obstructions, simultaneous deformations of pairs and stronger formality results; read the primary statements and reused the sufficient nearby assessments identified below.
SOURCE_EVIDENCE: Iacono--Manetti, On Deformations of Pairs (Manifold, Coherent Sheaf), Canad. J. Math. 71 (2019), Theorem 7.11, p. 1235, equations (5.2) and (7.1), pp. 1224 and 1234, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B017822BED1B8D6202816C2E10C0A30D/S0008414X18000561a.pdf/on_deformations_of_pairs_manifold_coherent_sheaf.pdf#page=27; Huybrechts--Thomas, arXiv:0805.3527v2, Corollary 3.4, p. 14, https://arxiv.org/pdf/0805.3527v2#page=14; further statements, versions and scope comparisons below.
COMPARISON: Known theory controls fixed-ambient sheaf motions and simultaneous deformations of variety and sheaf. It does not evaluate these rotation sheaves' global products or their cancellation against the prescribed RM coefficient; the surface formality theorem has different hypotheses.
GAP: Identify the mixed-motion obstruction in the prescribed moving product with compatible signs and global descent, then test simultaneous cancellation in both diagonal Ext^2 groups, retaining the three infinity points. No product or cancellation is computed here.
REASON: Import the general obstruction and pair-deformation results; specialize their geometric data and compatibility with this small extension. The exact saved target remains a concrete different mechanism after the union exclusion and is retained for a separate research turn.

## Hypotheses

Use the very general cubic-RM K3 surface S and reduced rotation
supports C and C^(2) of L014 in X=S x S. Set P=O_C and Q=O_(C^(2)).
Write A_1=C[tau]/(tau^2) and A_2=C[tau]/(tau^3). The ambient product
comes from the same marked NS-fixed deformation in both factors,
with identified constant reduction over A_1 and order-tau^2
coefficient kappa in V_RM.

The saved test permits first-order motion of P direct sum Q from
both mixed Ext^1 directions, after forgetting the central splitting.
No first-order self component is added to this restricted test.
Retain the full support schemes, four finite intersection curves
and three infinity points. No filtration, quotient algebra, stability,
simplicity or Fourier--Mukai equivalence is assumed. No product,
reverse mixed Ext calculation, cancellation or lift is established here.

Reread Deligne's [Hodge formulation, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2).
It agrees with the [target audit](../../foundations/01-target-and-scope.md):
rational cycle-class surjectivity for every smooth projective complex
variety and every codimension. The intermediate sheaf question
does not replace that universal target.

## Conclusion

SPECIALIZE. The source comparison is complete and leaves no essential
access gap for the selected framework. General deformation theory
should be imported by citation. The justified work is its explicit
application to these singular supports and this ambient coefficient;
none of the inspected statements decides that application.

The plausible downstream use is a coherent representative of the
non-scalar rotation action that survives a transverse ramified test.
The central action is already covered by L014's cycle calculation.
Earlier representative tests allow three RM directions against four
required. This review leaves that bound and the attained 21-dimensional
span on the known family unchanged. The present existence problem is
quadratic in earlier motion; its solution set must not be called a
linear lifting kernel without proof.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, using one
exploration turn after L023's informative exclusion. The result is
a completed assessment and an actionable test, not a mathematical
advance, reproduction or result beyond the checked literature.
A bounded search without an exact match does not certify originality.

## Proof

The evidence is a comparison of primary statements and their scope.
No new obstruction identity or local/global product is derived here.

### Simultaneous deformations: the additional applicable source

Read Iacono--Manetti, *On Deformations of Pairs (Manifold, Coherent
Sheaf)*, published version, Canad. J. Math. 71 (2019), 1209--1241:
[Theorem 7.11, p. 1235](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B017822BED1B8D6202816C2E10C0A30D/S0008414X18000561a.pdf/on_deformations_of_pairs_manifold_coherent_sheaf.pdf#page=27),
equation (5.2), p. 1224, section 6, pp. 1226--1227, equation (7.1),
p. 1234, and Theorem 1.2, p. 1211. A finite locally free resolution
of a coherent sheaf on a smooth projective variety in characteristic
zero gives a dg Lie model for simultaneous deformations. Its anchor
projects to ambient deformations; its kernel is the endomorphism
complex. Section 6 specifies Maurer--Cartan deformations and gauge.

These hypotheses permit our nonsimple sheaf with singular support.
Application must fix the projection to the prescribed product.
Theorem 1.2's stronger smoothness conclusion needs degree-one trace
surjectivity and degree-two trace injectivity, neither established
here. No inspected statement evaluates our global products.

### The obstruction of the actual first-order sheaf

Reread Huybrechts--Thomas, *Deformation-obstruction theory for
complexes via Atiyah and Kodaira--Spencer classes*,
[arXiv:0805.3527v2 (15 September 2013), introductory hypotheses and Corollary 3.4, pp. 2 and 14](https://arxiv.org/pdf/0805.3527v2#page=14).
For a perfect complex on a separated noetherian scheme and a
square-zero thickening admitting a smooth ambient embedding, the
product of truncated Atiyah and Kodaira--Spencer classes vanishes
exactly when a perfect lift exists. Here the input must be the
chosen sheaf on X_(A_1), including its earlier motion, for the
extension X_(A_1) inside X_(A_2). A central direct-sum calculation
does not evaluate that input. Perfectness and the embedding
hypothesis must accompany its application.

Reread the [2014 erratum, pp. 561--562](https://link.springer.com/content/pdf/10.1007/s00208-013-0999-x.pdf#page=1).
It confirms the absolute criterion over a field and corrects omitted
flatness assumptions in the original relative formulation. Use
the corrected absolute-over-C construction on the nonreduced
smaller scheme. Its smooth central fibre's differentials do not
replace that datum.

### Fixed-ambient motions and stronger formality results

Reread Fiorenza--Iacono--Martinengo, *Differential graded Lie algebras
controlling infinitesimal deformations of coherent sheaves*,
[arXiv:0904.1301v3 (19 November 2009), Theorem 7.6 and section 8, pp. 19--21](https://arxiv.org/pdf/0904.1301v3#page=19).
The endomorphism dg Lie algebra of a locally free resolution, with
global descent, controls flat sheaf deformations on fixed X.
Coherent sheaves meet Theorem 7.6's negative-cohomology condition.
Section 8 identifies the global Ext^1 and Ext^2 spaces and gives
the Dolbeault model over C. This covers the allowed A_1 motion
without preserving a splitting. It does not select the later
ambient coefficient.

Read Bandiera--Manetti--Meazzini, *Formality conjecture for minimal
surfaces of Kodaira dimension 0*,
[arXiv:1907.10690v2 (2 August 2020), Theorem 1.1 and introduction, pp. 1--2](https://arxiv.org/pdf/1907.10690v2#page=1).
The introduction identifies the quadratic Kuranishi term with the
Yoneda pairing. Theorem 1.1 proves dg Lie formality for polystable
sheaves on smooth minimal projective surfaces of Kodaira dimension
zero. Our ambient variety is a fourfold; polystability is not given.
The support's dimension two does not make that theorem applicable.
It supplies neither our products nor an all-order quadratic model
for this moving-product problem.

The remaining compatibility is between the mixed-motion contribution
and the prescribed ambient term in one global model, with consistent
signs. This assessment does not assert an unproved formula for this
pair of supports. It also makes no formality assumption.

### Reused comparisons and redundancy

Reuse the [rotation-extension assessment](2026-09-27-three-rotation-sheaf-extensions.md)
for [Stacks 0BQP](https://stacks.math.columbia.edu/tag/0BQP), the
local-to-global Ext spectral sequence. A local composition or its
image in a sheaf Ext group need not determine a global Ext^2 class.
The same assessment's Pridham Corollaries 2.22 and 2.25,
[arXiv:1208.3111v4, pp. 18--20](https://arxiv.org/pdf/1208.3111v4#page=18),
control the semiregularity image and leave its kernel unresolved.
These sufficient comparisons are reused without new browsing.

Also reuse that assessment's theorem-level comparisons with Markman,
Theorem 5.1, and Toda, Theorem 1.1: their selected lifting statements
require Fourier--Mukai equivalence data absent from this target.
The [cubic-family audit](../../foundations/05-cubic-rm-family.md) and
previously inspected van Geemen--Schutt sections 4.8--4.9 and 5.3--5.4
cover the known construction and its scope.

Read L017's full proof, the [stopped extension attempt](../../ATTEMPTS/014-unfiltered-rotation-sheaf-extensions.md),
the [ramified-union assessment](2026-09-27-ramified-complete-intersection-union.md)
and [history 033](../../history/033-2026-09-27-ramified-complete-intersection-recovery.md).
L017 computes one directed Ext^1 space with four curve parameters
and three punctual parameters. Its fixed extension sheaves have
no transverse first-order lift. It does not evaluate the reverse
group or compositions for two-way motion of P direct sum Q.
L016 tests an ordinary-square algebra; L023 recovers an ideal
from an ideal-plus-line middle sheaf. Their stated conclusions
do not cover this central object and motion. The previous
representative exclusions remain in place.

### Bounded specialization and continuation test

Preserve the exact TARGET. One global cancellation test should:

1. Use compatible resolutions and descent data for P and Q.
   Reuse L017's established directed group, but justify the reverse
   direction and actual products. Retain all four curves and three
   infinity points; dimensions alone are insufficient.
2. Represent the permitted mixed motion in the pair-deformation
   model and impose the fixed common-factor ambient coefficient.
   Compare with the corrected obstruction of the actual A_1 sheaf
   before using a blockwise cancellation formula.
3. Test whether a single pair of permitted global mixed classes
   cancels both full diagonal ambient classes for one kappa outside
   V_D. A linear span of possible products, two independently
   chosen products, local cancellation or zero trace is insufficient.

Continue if a pair survives that global comparison, or a specific
cancellation remains with a bounded compatibility check. Stop this
restricted mechanism if the entire permitted product locus is
excluded. Failure of one selected class does not decide the
existential question; failure of the mixed-only test does not
exclude first-order self motion or other representatives.
Complete the continuation or stop decision within the shared
three-exploration-turn budget; this assessment uses the first turn.

Even diagonal cancellation requires checking all remaining
obstruction components and an actual flat coherent sheaf lift.
Higher orders, algebraization, a transverse family of algebraic
correspondences and recovery of the required RM classes on it
remain later steps. Arbitrary primitive fourfold classes and
higher-dimensional cases remain further gaps. No complete
Hodge candidate is produced.

### Search record and access boundary

Queries on 2026-09-27 included:

- "K3" "rotation" sheaf "Yoneda"
- "sheaf" "ambient" "quadratic" "Atiyah" obstruction Yoneda
- Fiorenza Iacono Martinengo "7.6" deformations sheaves
- Huybrechts Thomas deformation complexes embedding Corollary 3.4 square zero obstruction
- "Yoneda" "quadratic" "Kuranishi" sheaves K3 formality
- "deformations of pairs" "coherent sheaf" Manetti
- "rotation" "real multiplication" "sheaves"
- "Fiorenza" "Iacono" "Martinengo" coherent sheaves 7.6
- "Formality conjecture for minimal surfaces" arxiv
- "K3" "Dickson" "Yoneda"
- "real multiplication" "Kuranishi"

Exact-geometry searches produced no inspected theorem deciding
this target. Broader searches located the pair and formality
comparisons above. The stated numbers identify the published or
versioned copies actually read, not search snippets.

The BMM institutional PDF did not support reliable text navigation;
the accessible arXiv v2 resolved that issue. Si Li's
[*On the deformation theory of pair (X, E)*, arXiv:0809.0344v1](https://arxiv.org/pdf/0809.0344v1)
was opened and Corollary 3.2 and Theorem 4.4 inspected as an adjacent
lead, not an input to this assessment. The newer published pair
theorem supplies the selected coherent-sheaf model directly.

The 2025 joint-section preprint and original Kaledin--Lehn,
Budur--Zhang, Illusie and Lieblich sources were not read at theorem
level here and are not additional premises. No essential source
gap remains for the chosen test. The search is bounded and does
not assert that no exact theorem exists elsewhere.

The pending record from step 033 is completed with its target and
restricted motion unchanged. No derivation is combined with clearing
the literature gate. See [history 034](../../history/034-2026-09-27-two-way-yoneda-literature.md).

## Mathlib

Coverage: **not checked** for the full statement, mixed Yoneda
products or the moving-ambient specialization. The named theorems
and direct links above are supporting mathematical references;
none is a full match for this cancellation question or a claimed
Mathlib match. No library absence or certified originality is asserted.
