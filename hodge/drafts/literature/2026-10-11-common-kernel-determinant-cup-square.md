# Common-kernel determinant cup-square — source comparison

TARGET: Assess the rank-two determinant cup-square test on H^1(S x S,F) for L079's t=1 and t=2 branches, retaining both relative Serre pairings.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact rank-two coefficient cup/square, determinant/Plucker and hyperholomorphic H^1 queries plus scoped L079/L086, ATTEMPTS/055/056 and saved duality coverage; no full matching theorem was identified in inspected sources. Demailly's archived coefficient-resolution proof and primary Stacks cup-product/duality statements were read; search snippets are not theorem evidence.
SOURCE_EVIDENCE: Demailly, alg-geom/9410022v3 (28 February 1995), Section 1.A, (1.1)--(1.3), printed pp. 4--5, and Section 4.A, (4.3)--(4.4'), printed pp. 27--28; Stacks live 2026-10-11, 20.31.3/5/6/7/8 (0FP3, 0FKU, 0FP6, 0H99), 15.59 (0GWN), 20.13.4 (01F2), 36.23.1 (0FLN), 48.19(2),(9) (0AU3), 48.15.7 (0BRT); reused the inspected 2026-10-08 changed-sign duality assessment for 48.3.6 (0A9Q).
COMPARISON: Known coefficient Dolbeault resolutions, Koszul signs, multiplicative pushforward/base-change and smooth-proper duality cover the machinery. None of the inspected statements gives this prescribed common-kernel verdict. The remaining specialization is a local rank-two exterior-algebra check followed by comparison of the same global cup class with both actual relative forms; no reproof of Dolbeault or duality is warranted.
GAP: Establish or refute the proposed self-cup-square identity for degree-one F-cohomology and prove the two restriction comparisons before deciding compatibility in either t branch. Neither an identity nor an exclusion is established in this literature turn.
REASON: Essential machinery is now accessible and its hypotheses match the saved conditional target; approve only one separate bounded specialization attempt, with both branches and scalar qualifications retained. This is source-coverage exploration, not a new mathematical input or Hodge algebraicity.
LITERATURE_REASON: The new global coefficient-cup target lay outside ready individual-holonomy and natural-projector coverage; the essential unread input was the multiplicative coefficient-resolution/restriction comparison.
SCOPE: Exactly L071/L079 on the identical marked K3 product, rank-two locally free F, integral c_1=0, full negative tensor, (-13,-14), both actual odd images and perfect symmetric forms, t=1 or 2. Only the determinant cup-square/restriction test is covered; no inverse, projector lifting, image identification, F existence or transport.
COVERED_TARGET: Test the rank-two determinant cup-square identity and its compatibility with both L079 relative Serre forms in the t=1 and t=2 branches.

## Exact proposed scope

Use the conditional F of L079 on X=S x S: locally free rank two,
Omega-polystable, integral c_1=0 and full ch_2=-9e_1-10e_2-tau_D,
at L071's identical fixed metrics. L079 supplies both actual odd
direct images G and H, their perfect symmetric parallel Serre forms,
and common trivial multiplicity t=1 or t=2. No F is constructed.

Assess the determinant-valued cup pairing on H^1(X,F), its product
in H^4(X,O_X), and its restrictions to the two K3 factors. Verify
the actual determinant trivialization, exterior and cohomological
signs, the edge/base-change identifications, and the relation to
the actual relative forms before any compatibility verdict. The
possible cup-square identity and simultaneous nonvanishing needed
for an obstruction are questions, not established inputs. A choice
of scalar normalization must not be mistaken for a vanishing result.

The universal primitive Hodge gap remains. A rigorous incompatibility
could stop this exact common-kernel recipe even though individual
image blocks now exist. A compatible answer would stop this bounded
test without asserting common-kernel existence. Neither outcome
would settle algebraicity or transverse transport.

## Completed primary-source comparison

**Coefficient model.** Read Demailly, *L2 vanishing theorems for positive
line bundles and adjunction theory*, [archived v3](https://arxiv.org/pdf/alg-geom/9410022v3),
Section 1.A, printed pp. 4--5 (PDF pages 4--5). For a complex
manifold and any holomorphic vector bundle, he defines the coefficient
Dolbeault operator componentwise in a holomorphic frame, checks frame
independence, and uses the locally exact, acyclic smooth resolution
to prove (1.3). The comparison with algebraic cohomology is GAGA
in the projective case. Section 4.A, printed pp. 27--28 (PDF pages
27--28), gives (4.3) and the coefficient wedge/integral Serre pairing
(4.4), with its Hodge-star proof. Compactness and a Hermitian metric
are the stated scope. Our smooth projective X and its K3 fibres
meet it. This licenses smooth representatives; it does not state
the proposed rank-two quartic identity. Neither flatness of F's
full connection nor multiplicativity of harmonic representatives
is required or to be assumed.

**Cup conventions and actual models.** Read [Stacks 20.31.3,
0FP3](https://stacks.math.columbia.edu/tag/0FP3), its adjunction proof
and the following global comparison in [20.31,
0FKU](https://stacks.math.columbia.edu/tag/0FKU). For complexes on a
ringed space, the naive product maps to the derived cup product.
Read 20.31.5--6 there: associativity and commutativity use the
derived tensor constraints; the associativity proof compares the
adjoint counit maps, whereas the commutativity proof is omitted.
Read [15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN), including
the differential check for the interchange sign (-1)^(pq).
These are general product theorems, not a rank-two vanishing theorem.
A later application must also retain the coefficient wedge's
interchange and must verify that its smooth product represents the
coherent cup product through the coefficient resolution. Ordinary
ungraded Plucker signs cannot simply be copied into degree one.

**Composition and restriction.** Read [20.31.7,
0FP6](https://stacks.math.columbia.edu/tag/0FP6), statement and proof:
relative cup is compatible with composition of morphisms of ringed
spaces, because the composed counits give the same adjoint map.
Read [20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99): the
relative cup commutes with the base-change maps for a commutative
square and arbitrary derived coefficients; its proof is omitted.
Compatibility alone does not assert that base change is an
isomorphism. L079 already supplies the all-fibre coefficient
base-change isomorphisms for both projections. A fibre inclusion
has locally free coefficient pullback here. These results therefore
cover the needed restriction comparison, but it remains to be
written for the same global class and both actual image sections.

Read [20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2), including
its composition-of-functors proof: bounded-below coefficient complexes
give Leray on ringed spaces. L079's single surviving row is the
existing input for H^1(X,F) versus H^0(S,G) and H^0(S,H); additive
Leray alone would not justify a product comparison.
Read [36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN), both
the projection/base-change proof and the affine-complex proof case.
It gives the cup-defined Kunneth isomorphism for quasicoherent
coefficients, quasi-compact quasi-separated factors tor-independent
over the base, and the global version over an affine base. Our
base is Spec(C), with smooth projective factors and O coefficients.
This covers the scalar-cohomology product needed to interpret a
degree-four class. Its specialization and the proposed compatibility
verdict are still future mathematics.

**Relative trace.** Freshly read [48.19(2),(9),
0AU3](https://stacks.math.columbia.edu/tag/0AU3) and [48.15.7,
0BRT](https://stacks.math.columbia.edu/tag/0BRT), including the smooth
diagonal/conormal proof of the latter. The former specifies proper
duality for bounded-above coherent and bounded-below quasicoherent
coefficients over a Noetherian base; smooth proper dimension d
identifies the dualizing coefficient with Omega^d[d]. Here d=2,
the base is the projective K3 and F is locally free. Reuse 48.3.6
and the already inspected pairing coverage in
[the changed-sign duality assessment](2026-10-08-sign-reversed-rank-two-duality.md).
L079 has already checked integral determinant triviality, canonical
two-forms, both symmetry signs, perfection, and the nondegenerate
restriction to each trivial isotypic part. No reproof is justified.
The later global comparison must use these actual forms and allow
each chosen canonical trace normalization its nonzero scalar.

## Search record and strongest inspected conclusions

Queries on 2026-10-11 included `"rank two" bundle "cup product"
"H^1" square`, `"determinant" "cup" "Plucker" cohomology vector
bundle`, `"rank two" "cup square" bundle cohomology`, `"rank two"
"H^1" "det" "cup" K3 product`, `"rank two" bundle cohomology
"cup" "square" vanishing`, `"cohomology" "Plucker relations"
vector bundles`, and `"rank two" "hyperholomorphic" "H^1" product`.
Source-location searches used Demailly/Dolbeault and Stacks
cup-product/pullback terminology. These bounded searches found
supporting machinery, not a full matching common-kernel theorem;
this is not evidence of novelty.

Ordinary Grassmannian Plucker relations and Mukai's curve-coefficient
cup-product lead appeared in search results; their theorem/proof
passages were not inspected and are not imported. A new odd-Plucker
lead was traced to Bhatia--Ganguly--Jiang--Rabin--Sam,
[*Cohomology of Complex Supertori*, 2606.02903v1](https://arxiv.org/html/2606.02903v1).
Its introduction and Theorem 1.1 hypotheses concern translation
quotients of affine superspace over a Grassmann algebra, with
structure-sheaf cohomology, rather than rank-two coefficients on
ordinary K3 products. The relevant Section 4.2 formula/proof could
not be fetched; it is an unread algebraic lead, not a matching
theorem or an essential input to the elementary specialization.
No superspace cohomology is imported into this notebook.

The author-hosted Demailly book and shorter notes repeatedly failed
web retrieval; shell curl failed DNS. The successful archived v3
above resolves essential access for the stated coefficient model.
No failure or search snippet is treated as theorem evidence.

Scoped reads of L079's pairing/Leray/audit passages and L086's
natural-map proof, together with ATTEMPTS/055/056 and the saved
duality assessment, found no prior global cup-square test. Keep
all those results and stops: no projector lifting is proposed.
The ready L089 assessment continues to cover individual tensors
only and is neither refreshed nor used as a mathematical premise.

## Separate bounded specialization and decision test

For the one covered target, form beta(u,v) in H^2(X,O_X) by the
determinant-valued degree-one cup after L079's actual determinant
trivialization. Test whether beta(u,u) cup beta(u,u)=0 in
H^4(X,O_X) is valid, using a holomorphic rank-two frame in the
smooth resolution. This equation is a proposed test, not a proved
identity. If a polarized version is used, determine its signs
explicitly instead of importing an ungraded relation.

Then compare restrictions of that same beta with Q_G and Q_H via
the two actual Leray edge maps and canonical-form/trace choices.
Check nonzero comparison scalars, not a preferred phase. Evaluate
whether the two quadratic self-pairings can be simultaneously
nonzero on the same H^1(X,F), separately for t=1 and t=2; a
nondegenerate complex symmetric form need not be anisotropic.
Use scalar Kunneth to compare the resulting degree-four product.
Do not calculate or decide any of these questions in this source
turn. The sources cover their tools; their local application is
the identified difference requiring the separate research turn.

Continue only if both the rank-two identity and the relative
comparisons hold with the retained assumptions. A proved
incompatibility excludes precisely L079's conditional recipe;
compatibility, failure of the identity, or failure of a load-bearing
comparison ends this bounded test with the exact reason recorded.
Neither verdict establishes a kernel, image identification, a
cycle, transverse transport or the universal Hodge target.

The mechanism uses global degree-one coefficient classes. It does
not ask a direct-image projector to lift through End(F); that
mechanism remains stopped by L086 and ATTEMPTS/055. It does not
repeat L079's individual character/index filters, ATTEMPTS/053,
or ATTEMPTS/056's half-adjoint indices. The first source review
must still check relevant known obstructions and possible duplicates;
this local search makes no novelty claim.

Essential continuation inputs: L071 and L079; L086 bounds what the
projector comparison supplies. L089 is motivation through individual
block existence, not a premise for the proposed global identity.
No cross-notebook input. Full matching and supporting Mathlib coverage
is not checked; unknown coverage is not absence. This file records
source approval for the single covered specialization, subject to the
supervisor's separate next-turn approval. It proves no cup-square
identity or common-kernel exclusion and writes no new lemma.
