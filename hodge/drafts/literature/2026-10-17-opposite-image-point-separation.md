# Opposite image point separation — completed source comparison

TARGET: Determine whether L118's local total geodesy and L120's degree-one normalization force injectivity of the opposite classifying map.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared audited L118/L120, the opposite compactification and earlier equality two-branch assessments, and ATTEMPTS/046, 047, 066, 069; searched trianalytic normalization, hyperkahler immersion injectivity, self-intersections and simply connected totally geodesic immersions; inspected primary statements and branchwise proof cases listed below.
SOURCE_EVIDENCE: Verbitsky alg-geom/9703016v1, Propositions 3.9--3.10, Theorem 4.7, Proposition 6.1, Theorems 6.2--6.3 and complete normalization proof, PDF pp. 16--19, 26--28; Soldatenkov--Verbitsky 1409.1100v2, Theorem 1.2 and Section 1.3; Verbitsky alg-geom/9610010v1, Propositions 9.9--9.11 and Lemma 9.12 with proofs, PDF pp. 44--46; reuse audited local-geodesy and normalization sources.
COMPARISON: The later desingularization theorem removes the older local-homogeneity assumption but retains separate local components; its normalization conclusion is an immersion, not point separation. The deformation paper's isomorphism criterion additionally requires Zariski tangent isomorphisms, not L118's injections. No applicable global injectivity theorem or counterexample with the full F hypotheses was found.
GAP: Excluding distinct parameters with the same opposite fibre remains open; neither all actual branch tangent images being equal nor absence of isolated distinct-branch collisions is established.
REASON: Park automatic injectivity from normalization and individual-branch geodesy. A narrower coincidence-scheme test is separately proposed; no mathematical specialization or new lemma is proved in this literature turn.
SCOPE: Conditional F and marked metric/triples of L071/L118/L120; B=S_1, Y=S_2, ch_2(F)=-14e_1-21e_2-tau_D, integral c_1=0 and rank two. Only original-image point separation; no F existence, reconstruction, compactification or transport.
LITERATURE_REASON: The target changes from normalization degree to point separation, which all saved ready assessments explicitly leave unresolved.

## Completed comparison

The main gap is universal primitive rational Hodge realization. Point
separation is an intermediate prerequisite for possible reconstruction of
this conditional moduli image; even success would leave F existence and
transverse transport independent. The reviewed threshold was an applicable
global injectivity theorem under exactly L118/L120's hypotheses. It was
not reached. This is source-scope evidence, not a proof that those complete
hypotheses admit a self-intersection.

[Verbitsky, *Hypercomplex varieties*, alg-geom/9703016v1,
12 March 1997](https://arxiv.org/pdf/alg-geom/9703016v1#page=18),
Theorem 4.7, describes quaternionic linear tangent-cone components.
Proposition 6.1 and Theorem 6.2, PDF pp. 26--27, establish smooth
normalization for a hypercomplex variety and an integrable induced
structure. Unlike the older Theorem 6.1 in alg-geom/9611015v1, local
homogeneity is established earlier, not an additional hypothesis. Read
the full proof: it normalizes a neighborhood by the disjoint union of its
smooth local components, then glues their hypercomplex structures.
Theorem 6.3's proof, p. 28, explicitly retains identifications of
trianalytic subsets. These statements do not identify separate branches
or assert that normalization has singleton fibres. They are comparisons;
this turn does not verify an intrinsic hypercomplex structure on the
actual algebraic image or apply the theorem to it.

[Soldatenkov--Verbitsky, *k-symplectic structures and absolutely
trianalytic subvarieties in hyperkahler manifolds*,
1409.1100v2](https://arxiv.org/pdf/1409.1100v2#page=3), Theorem 1.2,
PDF p. 3, states that normalization of a trianalytic subvariety in a
hyperkahler manifold is smooth and its map to the ambient manifold is
an immersion. Section 1.3, p. 6, specifies generic bijectivity. This
confirms the precise scope; it adds no injectivity conclusion. Its
Theorem 1.16 concerns absolutely trianalytic cycles in a compact IHS
ambient manifold. Neither that ambient hypothesis nor absolute
trianalyticity is supplied here. The requested v2 PDF has an internal
footer reading version 1.0, September 3, 2014; no other version is used.

[Verbitsky, *Deformations of trianalytic subvarieties*,
alg-geom/9610010v1](https://arxiv.org/pdf/alg-geom/9610010v1#page=44),
Proposition 9.9 starts with a morphism isometric on nonsingular loci.
Propositions 9.10--9.11 require a finite dominant map, isomorphic
normalizations, and an isomorphism on every Zariski tangent space.
Read the graph argument and subsequent flatness argument, pp. 44--46.
L118 supplies an ambient tangent injection, not the last hypothesis for
the normalization-to-image map. The existing compact-Douady assessment
already excludes using global transport without the stated ambient
hypotheses. No new application of Proposition 9.11 or its Lemma 9.12
is made; their printed argument is not a substitute for the missing
tangent-surjectivity check. Generic degree one alone does not meet it.

## Duplicates, failures and bounded continuation

The [earlier equality two-branch comparison](2026-10-13-equality-stable-double-point-tangent-lines.md)
already found that the older tangent-cone theorem does not force equal
tangent lines. That is retained evidence, not a new result of this step.
The new comparison checks the later theorem without the additional
local-homogeneity hypothesis and the superficially stronger isomorphism
criterion. Neither repairs point separation. ATTEMPTS/046's Hom
linearization, ATTEMPTS/047's compatible index, ATTEMPTS/066's metric
warning and ATTEMPTS/069's unknown cup entry remain stopped in their
recorded scopes. No compactification search is reopened.

Queries included `Verbitsky hyperkahler immersion trianalytic normalization
self intersections embedding totally geodesic`, `compact simply connected
hyperkahler totally geodesic immersion injective trianalytic subvariety`,
`trianalytic self-intersections`, `hyperkahler immersion K3 injective`,
and `trianalytic double points`. Search-only leads on symmetric spaces,
generic Hilbert schemes and unrelated flat immersions were not imported.
No essential access blocker remains for this comparison. No novelty is
inferred from these bounded searches. Full matching Mathlib coverage is
not checked.

The materially narrower proposed test is to determine whether the actual
off-diagonal coincidence scheme is finite and reduced, without asserting
its emptiness. That would delimit the residual separation gap and might
support a later family-specific collision invariant. Its separate
[assessment](2026-10-17-opposite-coincidence-scheme-finiteness.md) proposes
one bounded local-branch/scheme argument. It is newly written and requires
separate approval before mathematics; this review proves none of it.
Continue only if actual local charts, geodesic uniqueness and scheme
tangents control the complete coincidence scheme. Abandon that test if
they require image normality, unavailable global isometries or an ambient
completion. Finitely many possible collisions would still not prove
injectivity.

## Initial proposal retained (superseded as routing)

The main gap remains universal primitive rational Hodge realization.
The intermediate target is whether f^-(x)=f^-(x') can occur for x!=x'.
A justified separation result could support later image reconstruction;
a verified obstruction to this inference would delimit what normalization
and local metric rigidity actually provide. Neither outcome constructs F
or an algebraic class. No separation implication is derived here.

Use L071's actual compatible connection and full negative tensor,
L118's actual same-extension map and local geodesy with scale 2lambda,
and L120's audited finite unramified degree-one normalization. Do not
assume normality of the reduced image, completeness of its ambient L2
metric, a compact hyperkahler metric extending it, or global separation.
L119 may be consulted only if its actual normal bundle becomes relevant;
its index is not a substitute for an image argument.

Review primary statements and relevant proof cases about globally
parametrized totally geodesic quaternionic immersions and trianalytic
image normalization. Check their embedding, completeness and compactness
hypotheses before using any conclusions about branch coincidence or
intersection. These are proposed search directions, not inspected leads.
Continue only with an applicable theorem or a concrete, separately
assessable branch test. If sources control normalization alone or require
an unavailable ambient completion, record that difference and park this
inference rather than repeat the earlier compactification search.

ATTEMPTS/046 already shows that relative-Hom Euler data and its first
linearization do not decide separation for the earlier family; do not
repeat that test under a new charge. ATTEMPTS/047's index stop,
ATTEMPTS/066's automatic metric-extension warning, ATTEMPTS/069's unknown
global cup entry and the opposite L2 boundary assessment remain intact.
This proposal is not a new ready assessment and establishes no lemma.
Mathlib coverage for the proposed global assertion is not checked.
