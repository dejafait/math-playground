# Equality-family normalization and generic degree — source coverage ready

TARGET: Assess whether L098's finite map has generic degree one via normalization and the actual Mukai two-form, retaining the finite split fibre.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L065 and its ready degree/form assessments with L095 and L098; checked ATTEMPTS/061 and narrowly searched finite K3 symplectic quotients, finite-etale Galois refinements, purity across finite sets, unique cover extensions and finite-symplectic Picard bounds; primary evidence and exact queries are below.
SOURCE_EVIDENCE: Inspected Stacks 0GS9, 03SF, 0H2W, 0EY6, 0EY7, 0BMB, 0BQL and 035Q statements and relevant proofs; Huybrechts's 449-page author draft 1.2.3 p. 11 and 15.1.5/15.1.8 with following table pp. 309--310; Xiao (1996) section 1 p. 74; reuse Huybrechts--Lehn 10.3.3--10.3.5/10.4.1--10.4.3 and Kuznetsov--Markushevich 2.2/(13)--(14) through the inspected older assessments.
COMPARISON: L065's global finite-etale Euler argument exceeds the current hypotheses; known punctured-cover extension and finite-symplectic automorphism constraints support a different specialization of the same degree target, using the retained rank-four K3 and actual stable family form. No full matching equality-family theorem was identified.
GAP: Establish the actual normalization factor, etale restriction, Galois refinement collapse and extended deck action, then compare the actual stable Mukai pullback with L095's nonzero raw form and test the known automorphism bound; no degree verdict is proved in this literature turn.
REASON: Essential source coverage is now supplied for one mathematical attempt on the saved target; import the general theorems and justify only the identified actual-family applications, retaining the entire finite split fibre.
SCOPE: The same hypothetical locally free rank-two Omega-polystable F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D at identical marked K3 metrics; audited L095/L096/L097/L098, H, possibly empty finite Z and reduced image W; retain the very general marked rank-four NS scope inherited through L025/L044/L071. No extension of the coarse form at m_0 is assumed.
LITERATURE_REASON: New essential scope is the normalization and degree of a finite map that may ramify over strictly semistable image points; the ready whole-map-finiteness assessment does not cover extension of the Mukai form or a singular-target finite-cover degree argument.

## Target, use and discriminating test

The main gap remains algebraic realization of arbitrary primitive
rational Hodge classes. A controlled normalization and degree could
help test reconstruction for this conditional equality-family route.
It would not construct F, separate all points of the original image,
integrate the split tangent, or supply a transverse algebraic cycle.

The intermediate threshold remains generic degree one, not merely
finiteness. For the proposed attempt write N for the normalization of
W, avoiding L065's different W notation. Continue only if the finite
factor h:B -> N has an etale restriction over the complement of the
full preimage of m_0, its covering automorphisms extend to B, and the
actual stable Mukai pullback forces those automorphisms to preserve
the fixed two-form. Test them against the retained Picard rank using
the imported bounds. A failure of any bridge stops this mechanism;
neither smoothness of N nor an Euler formula for a ramified cover
may be substituted. Z may be empty. No degree proof is performed here.

## Reused coverage and exact differences

Read L065's hypotheses and normalization/cover/form/Euler proof,
its degree assessment, the relevant audit record, and the family-form
assessment. These supply the general inputs already inspected there:
Stacks 0359/035S (finite normalization over C), 035D (finite separated
factor), 01UX/02G5 (relative differentials and unramifiedness), and
0BQ3 (normal implies geometrically unibranch). Reuse those statements
through drafts/literature/2026-10-07-charge-seven-generic-degree-one.md;
their family-specific application must be checked again. L065 is a
methodological comparison, not a direct input to the new conclusion.

The decisive scope difference is that L098 has unramifiedness only
on U=B minus Z. Its actual equality (4) retains the full exceptional
support and all points in it have image m_0. Reinspected
[Stacks Lemma 37.37.2, 0GS9](https://stacks.math.columbia.edu/tag/0GS9):
integral geometrically unibranch target, connected source, a dominating
component, and unramifiedness are all required. Its proof propagates
the etale locus along the dominating component. This can be tested
on an open normalization factor; it cannot establish whole-map
etaleness at the split parameters. The old smoothness descent and
Euler multiplicativity are consequently not an approved shortcut.

## Covering and extension inputs

[Stacks Section 58.7, 03SF](https://stacks.math.columbia.edu/tag/03SF)
gives a connected finite-etale Galois refinement of any connected
finite-etale cover. A connected Galois cover has automorphism group
of order equal to its degree, acting simply transitively on geometric
fibres. Read the statements and their Galois-category justification.
The proposed use is to refine the punctured normalization cover and
test its further finite-etale cover of U, before assigning a deck
group to h. A finite cover is not assumed Galois at the outset.

[Stacks Lemma 58.31.2, 0H2W](https://stacks.math.columbia.edu/tag/0H2W)
extends a finite-etale cover of a dense open in a locally Noetherian
scheme when it is unramified in codimension one and the omitted
local rings are regular. Read its entire proof: first extend at the
codimension-one generic points, then apply local purity and 0EY7.
For the intended source application the complement in smooth B is
finite. Verify the absence of omitted codimension-one points and
the hypotheses for this actual open before using the theorem.
[Lemma 58.21.6, 0EY7](https://stacks.math.columbia.edu/tag/0EY7)
states essential surjectivity of cover restriction under local purity;
its proof spreads the local extension by Noetherian induction.

[Stacks Lemma 58.21.5, 0EY6](https://stacks.math.columbia.edu/tag/0EY6)
gives the unique finite depth-at-least-two extension across a
depth-at-least-two complement. Read its full relevant proof: the
extension algebra is j_* of the finite-etale algebra, and reflexive
uniqueness identifies every such finite extension. This supplies
coverage for extending deck automorphisms via that same algebra,
provided the actual finite h and the finite complements meet the
depth hypotheses. It does not say the extension is etale without
flatness. This is the needed extension input, avoiding an unproved
Hartogs claim for arbitrary maps. [Lemma 58.11.2, 0BQL](https://stacks.math.columbia.edu/tag/0BQL)
identifies a connected finite-etale cover of a normal integral scheme
with normalization in its function field; its short proof was read
as supporting comparison.

[Stacks purity, Lemma 58.21.4, 0BMB](https://stacks.math.columbia.edu/tag/0BMB)
requires normal source local ring, regular target local ring,
quasi-finiteness, equal positive local dimensions and codimension-one
unramifiedness. Read its dimension-one and higher-dimensional
reduction cases. This permits source-side puncture tests; it is not
applicable across singular points of N merely because their support
is finite. No target singularity classification is assumed.

## Two-form comparison and automorphism constraints

Reuse the precise coarse-form coverage in the two older assessments:
Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves* (1997),
10.3.3--10.3.5, pp. 224--225, and 10.4.1--10.4.3, pp. 227--228,
[primary text](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=235);
Kuznetsov--Markushevich, math/0703264v2, Theorem 2.2 and equations
(13)--(14), pp. 8--10,
[primary text](https://arxiv.org/pdf/math/0703264v2#page=9).
Their stable/simple-sheaf family formulas and quasi-universal
similitude cancellation do not depend on the old charge-seven vector.
Their use here is restricted to M^s and the actual family on U.

L098 already identifies its actual stable differential with the same
dual-number Ext class and mixed-curvature representative. L095's
actual raw fibre integral gamma_R equals -2lambda sigma_B, including
the first-factor orientation, the full negative tensor and the pure
point terms. The future proof must compare the ordered coarse family
form with this gamma_R up to one fixed nonzero scalar on U. A
charge-seven value is not imported. Do not claim a coarse form at
m_0 or extension to N; the cover automorphisms need only be tested
against the actual nonzero form on the open source and its existing
global extension on B. This is an application still to be proved.

[Huybrechts, *Lectures on K3 surfaces*, 449-page author-hosted draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf),
Remark 1.2.3, printed p. 11, states triviality of the algebraic
fundamental group over a separably closed field; its finite-cover
Serre-duality/Riemann--Roch proof was read. Section 15.1.2,
Corollaries 1.5 and 1.8 and the following table, pp. 309--310,
give the finite-symplectic order/fixed-point and Picard bounds;
the invariant-cohomology proof passage was read. Every nonidentity
finite symplectic automorphism in the projective complex case requires
Picard rank at least nine. Import these results; no reproof is needed.
The present marked rank-four scope is recorded in
foundations/05-cubic-rm-family.md and L025, retained through L044/L071.
Check this scope explicitly; the proposed test is not approved for
arbitrary higher-Picard specializations. Whether the actual cover
produces such automorphisms remains the mathematical application.

## Known obstruction and search limits

[Xiao, *Galois covers between K3 surfaces*, Ann. Inst. Fourier 46
(1996), 73--88, section 1, p. 74](https://www.numdam.org/article/AIF_1996__46_1_73_0.pdf#page=3)
states that a finite symplectic quotient has rational double points
and its projection is unramified outside those points. Its introductory
equivalence with preservation of the two-form was also read. This
records a known higher-degree mechanism under general finite-exceptional
cover/form inputs. It is not a counterexample to the actual equality
family: neither its Picard rank nor the sole exceptional coarse-image
value is matched here. The full Xiao classification tables and the
2026 *Singular symplectic surfaces* lead were not assessed or used.
No claim of complete classification is based on these previews.

Queries included `Xiao Galois covers between K3 surfaces quotient
singularities table symplectic finite groups`, `K3 finite symplectic
automorphism Picard number at least eight Nikulin`, `finite quasi
etale cover simply connected smooth source Galois quotient normal
variety theorem`, and Stacks-specific searches for Galois refinements,
integral-closure actions and regular codimension-two cover extension.
Nonprimary hits were discovery aids only. The narrow older local
degree/form assessments and ATTEMPTS/061 contain no duplicate proof
for this finite-split-fibre target. The compatible split quadratic
line stop is preserved; a deck-group degree test has a different,
independently testable threshold. No essential source is blocked.

Essential continuation inputs are audited L095/L096/L097/L098 and
the retained marked rank-four scope of L025/L044/L071. F existence,
integrated germs, separation in the original possibly singular W,
reconstruction and transport remain unresolved. This source import
changes the approved mechanism, not the degree or the attained Hodge
cycle span. The next step is a REPRODUCTION specialization of known
tools, not certified originality. Full matching Mathlib coverage:
not checked. No lemma, mathematical script or degree computation
was written in this literature-only turn.
