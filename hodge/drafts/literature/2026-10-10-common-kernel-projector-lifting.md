# Common-kernel projector lifting — completed source comparison

TARGET: Test whether L079's parallel trivial direct-image summands lift to nontrivial parallel projectors on its common rank-two kernel.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact projector/fullness and Nahm inversion searches located BJ and Bridgeland; scoped duplication search recovered the 2026-10-05 flat-transform assessment, which already covers general inversion failures. Fresh inspection isolates the different kernel-endomorphism map required here.
SOURCE_EVIDENCE: BBHR (1998), Definition 2, Section 3.3, Lemmas 1--2, Theorem 3 and Section 4.1/Theorem 4, pp. 244--247; Bartocci--Jardim math/0312045v1, Section 3, Theorems 2--3 and following remark, pp. 4--5, Section 4/Theorem 5, pp. 6--7; Bridgeland math/9809114v2, Theorem 1.1/Corollary 1.2, pp. 1--2, Theorems 5.1/5.4 and essential adjunction proof, pp. 8--11. Reuse inspected Perego Propositions 3.9--3.12/3.15, pp. 36--38, for actual parallel morphisms.
COMPARISON: General preservation permits reducible images; special inversion requires an identified universal/moduli kernel absent here. Fullness of Phi_F concerns input morphisms, whereas this target needs endomorphisms of F as kernel. Covered stability/parallel-morphism tools permit a terminal direct-map obstruction test, not a reconstruction theorem or exclusion of F.
GAP: Apply the existing stability of F to its parallel endomorphisms, check the natural maps induced by both R^1 projections, and test the actual trivial-summand projectors against their images; no map image or nonlifting result is derived in this literature turn.
REASON: Park automatic inversion/fullness as a source of projectors. One bounded specialization of known parallel-morphism and direct-image functoriality tools can decide the narrower natural-lifting question under the unchanged saved target; it requires separate approval and a mathematical turn.
LITERATURE_REASON: The kernel-morphism requirement was outside ready preservation/index coverage; this turn read exact inversion/fullness hypotheses and reused the earlier general comparison rather than reopening the parked Itoh curvature source.
SCOPE: L079's exact marked S x S, full negative mixed tensor, pair (-13,-14), rank-two locally free slope-polystable F, unchanged identical metric and both actual compatible direct images; all t=1 and t=2 branches retained. Only natural parallel kernel-endomorphism maps and their idempotents are approved; no inverse, fullness, new reconstruction assertion, F existence or transport.

## Gap, intermediate target and decision

The universal gap remains algebraic realization of every primitive
rational Hodge class; the local gap is one common holomorphic F with
L079's prescribed mixed action. The saved intermediate target asks
whether the actual parallel projectors onto its trivial image summands
can come from parallel projectors of that same rank-two F. A valid
lifting mechanism could interact with L071's product-splitting exclusion.
Individual E_4 and J_5, and the audited real-index results L084/L085,
do not supply it.

The source comparison rejects automatic invocation of the inspected
inversion/fullness theorems. It does not reject the existence of F and
does not prove a counterexample with L079's full hypotheses. The
remaining bounded test uses known morphism tools directly rather than
asserting an inverse. No projector-lifting theorem for this exact F was
located in the inspected material; that observation is not novelty.

## Primary hypotheses and essential proof cases

**Preservation and special inversion.** Bartocci--Bruzzo--Hernandez
Ruiperez, *A hyperkahler Fourier transform*, Differential Geometry and
its Applications **8** (1998), 239--249,
[Definition 2, Section 3.3 and Theorems 3--4, pp. 244--247](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
Theorem 3 starts with a hermitian quaternionic-instanton product kernel
and an IT input bundle. Its proof identifies twistor higher images with
the index bundle and descends a compatible connection; it does not
reconstruct kernel morphisms. This matches the preservation use in
L079, with input O_S and kernel F in either direction.

Section 4.1's inversion uses a reflexive K3: integral H with H^2=2,
a degree-zero determinant line with square -12, and nodal curves of
H-degree greater than two. The kernel is the normalized universal
rank-two bundle on the specified instanton-moduli K3, whose fibre
second Chern number is -1; the reverse universal kernel is its dual.
L079 instead has determinant-trivial charge-nine and charge-ten fibres
at the fixed real metric, and neither factor is identified with that
whole moduli space. These numerical/universal hypotheses do not match.
Theorem 4 cites the algebraic inversion proof rather than proving a
new arbitrary-kernel inversion statement.

The essential convolution proof is already inspected and reusable in
[the flat-transform assessment](2026-10-05-six-charge-flat-transform-rigidity.md):
BBHR, *A Fourier-Mukai transform for stable bundles on K3 surfaces*,
J. reine angew. Math. **486** (1997), 1--16; inspected
[alg-geom/9405006v2, Sections 4.1 and 4.3, Proposition 10 and Theorem 2](https://arxiv.org/pdf/alg-geom/9405006v2).
That proof uses universal-family Ext and the reverse-moduli
identification to obtain diagonal-supported convolution. It cannot be
substituted with flatness of an image or existence of individual blocks.
The earlier normalized trivial-image example has different determinant
and image rank; it is not an L079 counterexample. No reproof is needed.

**General transform caveat.** Bartocci--Jardim, *Hyperkahler Nahm
transforms*, inspected [math/0312045v1, 2 December 2003](https://arxiv.org/pdf/math/0312045v1#page=5),
Section 3, Theorems 2 and Theorem-Definition 3, pp. 4--5: the projected
Dirac-kernel connection agrees with the odd-IT higher image. The
following remark explicitly permits failure of inversion and
irreducibility preservation. Section 4, pp. 6--7, discusses mutual
whole-moduli interpretations; its Theorem 5 specializes to reflexive
K3s. These are additional assumptions, not consequences of compatible
preservation. Retain the already recorded target-manifold typo in
Theorem-Definition 3; use BBHR for the preservation input. No example
in this passage is asserted to satisfy L079.

**Fullness and the relevant category.** Bridgeland, *Equivalences of
triangulated categories and Fourier-Mukai transforms*, Bull. London
Math. Soc. **31** (1999), 25--34; inspected
[math/9809114v2, 12 March 2019](https://arxiv.org/pdf/math/9809114v2).
Theorem 1.1 assumes smooth projective varieties of equal dimension
and a vector-bundle kernel. Strong simplicity requires simple fibres
and vanishing of every cross-fibre Ext at distinct parameter points;
canonical-bundle invariance then gives equivalence. Corollary 1.2 uses
a fine compact two-dimensional stable-bundle moduli space. Stable
fibres alone do not verify these hypotheses.

Theorem 5.1's proof, pp. 8--10, reconstructs point objects through
adjunction, convolution support and the Kodaira--Spencer map;
Theorem 5.4, pp. 10--11, compares adjoints after fullness is established.
These cases were inspected; no all-degree cross-fibre orthogonality,
whole-moduli identification or adjunction isomorphism is supplied here.
The v2 flatness correction to Lemma 4.3 is retained; that lemma is not
used as a reconstruction shortcut.

In the notation Phi_F(A)=Rp_2*(p_1^*A tensor F), the morphism map in
fullness varies A while fixing F. The proposed lift instead varies
endomorphisms of the product kernel F and applies Rp_2*. These are
different maps. Faithfulness only gives injectivity; fullness would
concern surjectivity on the specified morphism spaces; preservation
only provides the image's connection. None is interchangeable with
lifting the chosen kernel idempotents.

## Ready tools for the same target's terminal test

L071's stable-or-split argument proves that any conditional L079 F is
stable; the nonzero mixed holomorphic-form action excludes the product
line-splitting branch. Its compatible connection is already established.
L079 supplies both actual base-changing images, their parallel summand
projections and every trivial multiplicity t=1 or t=2. These local
proof passages were read; no existence premise was added.

Reuse Perego, *Kobayashi--Hitchin corrispondence for twisted vector
bundles*, Complex Manifolds **8** (2021), 1--95,
[Propositions 3.9--3.12 and 3.15, pp. 36--38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36),
with complete statement/proof coverage recorded in the
[orthogonal assessment](2026-10-05-flat-transform-orthogonal-residual.md)
and reused in the larger-charge assessment. Compact Hermitian scope
covers the product and each factor. Apply trivial twisting, zero
B-field and equal zero Einstein functions. The parallel-morphism
statement and the usual stable scalar-endomorphism argument are
ready tools, not a new source hypothesis. A holomorphic stable image
is not assumed: every polystable branch remains in scope.

The next mathematical turn should explicitly identify the two natural
maps from parallel endomorphisms of F to endomorphisms of G and H,
verify their preservation of identities/composition and compatibility
with the actual image connections, and compare the specified
trivial-summand projections with their ranges. Import known theorems;
justify only these applicability/naturality steps. Do not reprove
Nahm preservation or assert any kernel reconstruction theorem.

Continue only if this comparison supplies a discriminating conclusion
about the natural lifts. Stop the natural-projector mechanism if the
projectors are not in those ranges; such nonlifting concerns morphisms,
not nonexistence of F. If the comparison remains undetermined, save
the exact missing bridge rather than promote fullness to an assumption.
Independent block existence, actual block identification, common F,
transport and universal Hodge algebraicity remain unresolved.

## Search, duplicates and qualifications

Queries: `Bartocci Bruzzo Hernandez Ruiperez hyperkahler Nahm transform
invertibility morphisms Fourier Mukai`; `Nahm transform K3 trivial
kernel direct image fully faithful idempotent`; `Bridgeland equivalences
triangulated categories Theorem 5.1 strongly simple Fourier Mukai 1999
pdf`; `Nahm transform projectors K3`; `Nahm transform fully faithful`.
Search hits on elliptic/relative transforms, ALE spaces and unrelated
torus projectors were not inspected as exact lifting theorems and are
not inputs. No source blocker remains essential to the selected test.

The narrow local duplicate search recovered the 2026-10-05 inversion
comparison and the charge-seven off-diagonal-Hom assessment. Their
cross-fibre and inverse hypotheses are reused rather than reproved.
ATTEMPTS/042,/043,/045,/053,/054 remain stopped with their original
evidence. The distinct question here is the natural kernel-endomorphism
map, not another image-character, index or curvature-positivity test.
The parked Itoh assessment remains SOURCE_BLOCKED and unopened.

Full Mathlib coverage of the lifting implication and selected natural
map test is not checked; this is not evidence of absence. No
cross-notebook input, new lemma, mathematical script or derivation was
made. SPECIALIZE approves a known-tool obstruction test only. The
newly completed ready assessment receives separate supervisor approval
before its mathematical application.
