# Larger-charge changed-sign orthogonal image — completed source comparison

TARGET: Test whether the actual p_2 direct image and its orthogonal summands exclude the changed-sign pair (a,b)=(-13,-14).
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the saved exact-pair duplicate search and primary transform/duality assessments; inspected L071, L073/L075 passages, L059's complete summand/index cases and ATTEMPTS/043/045; seven bounded external queries found a standard stable-block decomposition and general K3 simple-index bound, but no inspected theorem deciding the exact pair.
SOURCE_EVIDENCE: Freshly inspected Bartocci--Bruzzo--Hernandez Ruiperez (1998), Definition 2, Lemmas 1--2 and Theorem 3, pp. 243--246; Huybrechts K3 author draft, Chapter 9 Sections 1.2--1.3, Remark 1.5, pp. 169--170 and Section 3.1, pp. 175--176; Serman author manuscript Section 2.2, (2.2.1), Remark 2.3 and Proposition 2.6, pp. 10--11; Stacks 0A1H, 0BDK, 02UO and 0AU3; Cadek--Vanzura (1993), Section 2, relation (3), p. 2. Reuse inspected Fulton, Stacks duality/sign/Leray and Perego morphism coverage identified below.
COMPARISON: Preservation and coefficient duality have no image-rank or mixed-sign restriction; K3 simplicity/RR and parallel-morphism tools cover arbitrary stable summands at real h. Serman supplies a Schur-block comparison, not a K3 moduli theorem. L075's rank-two contradiction and L059/L061's numerical conclusions do not transfer; real rank-five existence cannot decide smaller-rank summands.
GAP: Separately verify all-fibre concentration, actual preserved image, full signed GRR, coefficient-duality symmetry/perfectness and every stable-block alternative; no new rank, character, summand verdict or pair exclusion is established here.
REASON: Essential general coverage is ready for one bounded necessary-constraint specialization, classified REPRODUCTION; import cited theorems and justify applications. Exact-h image/kernel existence, lifting/reconstruction and transport remain outside this test.
SCOPE: L071's identical marked projective K3 factors and hyperkahler metrics, actual real h and Omega, full integral -tau_D and full q-self-adjoint D, locally free rank-two holomorphic product-polystable F, integral c_1=0, fixed pair (-13,-14), unrestricted initial higher characters and K-class; actual p_2 image, coefficient duality, all stable-block/cohomology/simple and adjoint-index alternatives and necessary orthogonal characteristic relations only.
LITERATURE_REASON: The new pair and higher-rank summand question were REVIEW_REQUIRED; compare changed charge/rank hypotheses and complete Schur-block cases while reusing ready general preservation, GRR and duality coverage.

## Main gap, use and stopping test

Universal primitive rational Hodge-class algebraicity remains the main
gap. This intermediate target tests one different conditional bundle
input; its downstream use is deciding whether that input merits
construction work. It supplies no cycle or route resolving arbitrary
fourfolds. The flat (-10,-17) source blocker stays parked, and exhausted
six- and seven-charge directional tests are not rerun.

Establish the actual image before testing its character, pairing and
summands. Allow reducibility and arbitrary individual first Chern classes.
Continue to exclusion only if every permitted branch violates a rigorous
necessary condition. If a complete compatible branch survives the
approved constraints, stop this exclusion test without claiming its
realization. Failure of essential applicability also stops the bridge.

Essential established input is L071; its inherited exact line lattice
comes from L052. L073/L077 and L075 are method/source comparisons,
not theorems about this new image. L059/L061 supply failure comparisons,
not their old numerical conclusions. F existence, stable image,
opposite-fibre stability, inverse, reconstruction and transverse transport
are not assumptions. Any use of the other projection must first prove
its all-fibre concentration from L071; the general sources permit this
cohomological comparison but do not supply it automatically.
No cross-notebook input is used. This approval concerns source scope,
not an exclusion or approval of newly derived mathematics.

## Actual direct image and compatible preservation

Freshly read Bartocci, Bruzzo and Hernandez Ruiperez,
*A hyperkahler Fourier transform*, Differential Geometry and its
Applications **8** (1998), 239--249,
[Sections 3.1--3.3, Definition 2, Lemmas 1--2 and Theorem 3,
pp. 243--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
Compact hyperkahler source, compatible product rotations, a hermitian
quaternionic-instanton kernel, source instanton and IT are required.
Odd IT demands all even fibre cohomology vanish at every parameter.
Lemma 1 handles twistor IT; Lemma 2 identifies actual holomorphic
hermitian restrictions including the nonflat twistor embedding, and
descent supplies Theorem 3's compatible connection. No image-rank,
irreducibility or mixed-operator positivity hypothesis occurs.
Section 4.1's inverse results require additional special K3 hypotheses.

L071's full connection/factor proof was read, including stable/split
alternatives and the exact zero-slope line lattice. Reuse the
[seven-charge assessment](2026-10-09-sign-reversed-seven-charge-bogomolov.md)
for arbitrary-rank preservation at this changed sign. Use the actual
conditional connection on F and flat source O_S; new every-fibre
vanishing and constant dimension remain obligations. No twistor reproof
is warranted.

Freshly read [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
and [Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK),
including the Noetherian and fixed-rank open-locus proof cases.
Finite presentation, perfect input, bounded finitely presented
base-flat complex and proper support give perfect pushforward with
arbitrary base change. Single-degree constant-rank derived fibres
then identify the locally free image on the specified open locus.
GAGA and smooth projective p_2 fit this setting; all fibres and the
empty complementary locus still require proof. Older 0BDH references
name the containing section; 0BDK is this lemma's tag.

## Full character, cohomology and coefficient duality

Reuse the inspected Fulton, *Intersection Theory*, second edition
(1998), Theorem 15.2, pp. 286--287, and Example 15.2.8,
pp. 291--292, from the
[six-charge character assessment](2026-10-05-six-charge-surface-character-filter.md),
retaining its scan-host qualification. Freshly read
[Stacks 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO):
its displayed relative case assumes proper smooth projection, finite
locally free input and locally free higher images, and uses the
alternating sum. Fulton remains the proof citation. Retain L071's
forced full character, full mixed square and relative Todd; the
positive holomorphic image differs from its alternating class.
Check integral c_1 before determinant or simplified index arguments.

Reuse [Stacks Lemma 20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2)
and its spectral-sequence proof as inspected in the
[opposite-projection assessment](2026-10-06-nonflat-opposite-projection-review.md).
The ringed-space morphisms and bounded-below F[0] fit its hypotheses.
Concentration must precede any single-row global cohomology comparison.
L058/L060's evaluated cohomology is not imported.

Freshly read [Stacks 48.19(2),(9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3):
proper coherent duality and smooth relative dimension two retain the
canonical coefficient and shift, with no image-rank condition.
Reuse the proofs of [48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q),
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT) and the
commutativity differential check in [15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN),
recorded in the
[rank-two duality assessment](2026-10-08-sign-reversed-rank-two-duality.md).
The rank-two kernel determinant, relative K3 two-form, cup,
coefficient wedge and trace must construct the actual pairing.
Retain both interchange signs and every-fibre perfectness.
Self-duality alone does not determine symmetry.

Reuse Perego, *Kobayashi--Hitchin corrispondence for twisted vector
bundles*, Complex Manifolds **8** (2021), 1--95,
[Propositions 3.9--3.12 and 3.15 with proof, pp. 36--38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36),
as inspected in the
[orthogonal assessment](2026-10-05-flat-transform-orthogonal-residual.md).
On a compact Hermitian manifold the dual/tensor rules determine
Einstein functions, and the stated weak Hermite--Einstein morphisms
are parallel when the target function is at most the source function.
Use trivial twisting and zero B-field; verify actual zero functions,
including on summand projections. A fresh opening returned an internal
error; no fresh extraction is claimed. Prior complete inspected
coverage remains reusable, so this is not an essential source blocker.

## Exhaustive summand scope and stronger indices

Freshly read Huybrechts, *Lectures on K3 Surfaces*, author-hosted
prepublication draft,
[Chapter 9 Sections 1.2--1.3 and Remark 1.5, pp. 169--170](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=169),
and [Section 3.1(ii)--(iv), pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
These cover arbitrary-rank RR, simple self-Ext indices, slope
simplicity and dual stability, explicitly allowing real Kähler classes.
Simple E satisfies chi(E,E)<=2, equivalently Mukai square at least -2;
this is stronger than the semistable discriminant test.
Reuse inspected Theorem 4.9, p. 182, for compact-Kähler
Hermite--Einstein/polystability. These statements do not make a
polystable higher-rank image simple.

Freshly read Olivier Serman, *Orthogonal and symplectic bundles on
curves and quiver representations*, undated author-hosted manuscript,
[Section 2.2, (2.2.1), Remark 2.3 and Proposition 2.6 with proof,
pp. 10--11](https://math.univ-lille1.fr/~serman/grenoble.pdf).
The three cases are orthogonal stable types with quadratic multiplicity
spaces, symplectic stable types with symplectic multiplicity spaces,
and paired non-self-dual types with hyperbolic forms. The proof uses
scalar endomorphisms, vanishing between distinct stable types and
multiplicity-space bilinear algebra. Its base is a curve:
unitary-flat correspondence and moduli/existence conclusions are not
K3 inputs. Only this Schur-block pattern is a comparison.

For the K3 specialization, justify the Hom properties using the covered
zero-Einstein stable summands and parallel-morphism theorem, then
retain all three cases. This finite application is the identified
difference, not a reproof of curve moduli theory. L059's completed
partition enumeration is data-specific. Keep arbitrary individual c_1
until a rigorous constraint removes it, including trivial lines,
line dual pairs and repeated symplectic blocks. Simple self-Ext,
surface cohomology and exterior-square/adjoint RR tests are covered
applications of the cited RR and Chern-character tools; they are
not existence criteria.

## Topological rank qualifications and prior failures

Freshly inspected Cadek--Vanzura, *On the classification of oriented
vector bundles over 5-complexes*, Czechoslovak Math. J. **43** (1993),
753--764,
[author manuscript Section 2, relation (3), p. 2](https://www.math.muni.cz/~cadek/papers/so5.pdf#page=2).
The general necessary relation retains p_1, the Pontryagin square
of w_2 and the coefficient image of w_4. Reuse previously inspected
Theorem 1(i), p. 5, with its real-rank-five existence hypothesis.
It cannot realize smaller-rank blocks by deleting trivial directions;
only the covered necessary relations are approved for those blocks.
Compatibility is not full topological or holomorphic existence.
A spin base does not fix an orthogonal bundle's w_2.

L059's parallel real-reduction reasoning is dimension-independent
supporting material, but its rank-seven character and existence
witness do not transfer. Balaji, math/0407079v1, was freshly read
at its rank-three quadratic/Clifford statements (Theorems 1.1/1.5)
and the Theorem 1.5 proof passage. Its scope does not classify a
higher-rank K3 image or supply an unrestricted projective/spin lift.
Such reconstruction is outside this bounded test.

Read ATTEMPTS/043 and /045: the former preserves a compatible
orthogonal rank-seven branch, the latter nonspin ordinary and twisted
lifts at different data. L059's full stable-block/adjoint cases and
L061's lifting qualifications were read. No old numerical exclusion,
spin condition or compatible-index existence assertion transfers.
This new pair is independently testable; no previous stop is erased.

## Searches and precise continuation

Reuse the supplied notebook-local exact-pair/rank/charge search rather
than rerun it against the newly written working note. New reads remain
notebook-local. External queries on CHECKED were:

- "hyperkahler Fourier transform" Bartocci Bruzzo Theorem 3 quaternionic instanton
- K3 orthogonal bundle rank five polystable second Chern number existence spin symplectic
- "K3" "orthogonal bundles" stable second Chern
- "orthogonal" "polystable" "symplectic" "multiplicity" bundles decomposition
- "autodual" "Nahm" transform symmetric symplectic
- "K3" "orthogonal" "(-13,-14)"
- "K3" "orthogonal bundle" "rank 4" stability Chern

The decomposition query led to inspected Serman. Exact-coefficient
searches gave no useful inspected theorem; failed searches establish
no novelty. Curve Higgs/parabolic transform and real-structure leads
do not settle this ordinary K3-product input and remain unread.
Reuse the earlier orthogonal assessment's inspected Bhosle double-plane
and Abuaf--Boralevi P^2 hypothesis mismatches; neither supplies this
exact metric or kernel. No unfollowed lead is a mathematical input.

The exact TARGET is ready for one separate RESEARCH turn, classified
REPRODUCTION. Import the general results with applicability arguments.
L071 retains full integral -tau_D, actual h/Omega, local freeness,
rank two, product-polystability, integral c_1=0 and unrestricted initial
higher characters/K-class. All-fibre concentration, compatible actual
image, pairing and every summand constraint remain proof obligations.
If a complete compatible branch remains after these bounded constraints,
record it and abandon this exclusion mechanism, without claiming
image/kernel existence or requiring new literature to complete this test.

Full matching and supporting Mathlib coverage: **not checked**; no
absence claim is made. This LITERATURE turn derives no new result for
(-13,-14), creates no lemma and modifies no mathematical script.
