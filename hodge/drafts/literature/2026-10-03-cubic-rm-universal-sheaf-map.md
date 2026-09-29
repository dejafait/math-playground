# Universal-sheaf surface-map supply — literature assessment

TARGET: Review whether an algebraic map S -> M_H(2,0,-1) for a cubic-RM K3 surface S can realize a non-scalar endomorphism of T(S) via a pulled-back universal sheaf.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact Mukai vector, K3 maps to sheaf moduli and Hilbert cubes, universal-family criteria, non-scalar correspondence actions and stronger Hilbert-scheme exclusions; followed primary references and read the statements listed below. No inspected theorem supplies or excludes the required map with non-scalar action on the transverse cubic-RM surface.
SOURCE_EVIDENCE: O'Grady, arXiv:1205.4119v2, Proposition 4.2 and Remark 4.3, pp. 11--12, https://arxiv.org/pdf/1205.4119v2#page=11; Yoshioka, arXiv:math/9907001v2, Theorem 0.1, p. 2, https://arxiv.org/pdf/math/9907001v2#page=2; Huybrechts--Lehn, The Geometry of Moduli Spaces of Sheaves, online 281-page text, Theorem 4.6.5 and Corollary 4.6.7, printed pp. 107--108, https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=119; Markman, arXiv:math/0305042v3, equations (32)--(33), p. 23, https://arxiv.org/pdf/math/0305042v3#page=23; scope comparisons and direct links below.
COMPARISON: Known results cover nonemptiness, the six-dimensional moduli space, an untwisted universal family and a generic three-point kernel model, together with the normalized Mukai action. They do not cover an algebraic S-parameterized family with non-scalar action; birationality to S^[3], pointwise Chern-class realization and isotropic-vector derived equivalences do not supply that family.
GAP: On the unchanged rank-eighteen cubic-RM locus, independently construct or obstruct f:S -> M_H(2,0,-1) and evaluate its pulled-back universal correspondence on T(S). Generic kernel presentations require separate treatment of descent, collisions and images contained in the boundary; the existing support and Kuga-Satake exclusions do not settle these questions.
REASON: Import the inspected moduli, universal-family and action theorems without reproof. Their exact-vector kernel model justifies one bounded specialization testing an independent family and its action; stop a tested recipe if it yields only scalars or assumes the missing non-scalar correspondence. No full-statement match or novelty conclusion is claimed.

## Hypotheses

Retain T=T(S) of rational rank eighteen, full endomorphism
field E=Q(zeta_7+zeta_7^(-1)), and the four-dimensional
NS-fixed RM locus beyond the three-dimensional Dickson locus.
The [cubic-family audit](../../foundations/05-cubic-rm-family.md)
fixes the starting example; no theorem for that special family
is silently extended to every surface in its RM locus.
Reuse the unchanged rational target and primary-source comparison
in the [scope audit](../../foundations/01-target-and-scope.md).

M_H(2,0,-1) means Gieseker-stable **torsion-free sheaves**
with this Mukai vector, for a v-generic ample H. It is not
an asserted moduli space of locally free slope-stable bundles.
The prospective f is an algebraic morphism defined on all of S;
a rational map from a blowup is not a match for this target.
No f, non-scalar action or transverse cycle is supplied here.

The gap is algebraic realization of a non-scalar element of E
on a transverse cubic-RM surface. The intermediate target is
the stated map and its pulled-back universal family. Its plausible
use is an algebraic correspondence on S times S independent of
the modified Kuga--Satake cycle. Covering arbitrary primitive
fourfold classes and higher-dimensional cases remains a later,
separate gap even if this intermediate target succeeds.

## Conclusion

The exact saved action has a ready SPECIALIZE assessment.
Known results remove the moduli-existence and universal-family
questions and give an explicit generic model and action convention.
They leave the map-construction and non-scalar-action questions open.
No new result is derived in this literature-only turn. The supporting
mathematics is imported by citation; any subsequent specialization
must distinguish it from the remaining map/action test.

## Inspected statements and applicability

Read Yoshioka, *Irreducibility of moduli spaces of vector bundles
on K3 surfaces*, [arXiv:math/9907001v2, 7 February 2000,
Theorem 0.1 and its setup, pp. 1--2](https://arxiv.org/pdf/math/9907001v2#page=2).
For primitive positive-rank v and general H, this gives nonemptiness
when v^2>=-2, the irreducible symplectic deformation type, and,
for v^2>=2, the Hodge isometry theta_v:v^perp -> H^2(M_H(v),Z).
In the saved vector's convention v^2=4, c_2=3 and the dimension
is six: the target is of K3^[3] type, not a K3 surface.
These are theorem-applicability checks, not a new construction.
No map f or its pullback is specified by the theorem.

Read O'Grady, *Moduli of sheaves and the Chow group of K3 surfaces*,
[arXiv:1205.4119v2, 22 May 2012, Proposition 4.2, its proof,
and Remark 4.3, pp. 11--12](https://arxiv.org/pdf/1205.4119v2#page=11);
also Theorem 0.6 and the convention equations (0.0.7)--(0.0.8),
[pp. 2--3](https://arxiv.org/pdf/1205.4119v2#page=2).
The exact vector is the exceptional generic non-locally-free
case. Its generic sheaf fits into
0 -> F -> O_S^2 -> direct sum of k(p_i), i=1,2,3 -> 0,
with distinct support points and distinct kernel lines. Remark 4.3
gives a birational map S^[3] to M_H(v). The Chern-class theorem
is an equality of sets of classes in CH_0(S); it does not choose
a flat family over S. The reduced open model is not a classification
of families meeting, or contained in, the boundary.

Read Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
[online 281-page text, Proposition 4.6.2, Theorem 4.6.5,
Corollary 4.6.7 and their proofs, printed pp. 106--108,
PDF pp. 118--120](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=119).
The determinant-of-cohomology criterion gives a universal family
on the stable moduli space when the Euler-pairing gcd is one.
Here chi(F)=r+s=1, so the O_S test already satisfies it; equivalently
the surface criterion has gcd(2,0,-3)=1. Thus an untwisted
universal **sheaf** is available for this vector. This does not
assert local freeness, a chosen normalization or a surface map.
The [author-hosted K3 draft, Chapter 10, section 2.2,
printed p. 196](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=196)
was also read as a cross-check of the numerical Mukai-pairing
criterion. Its [errata](https://www.math.uni-bonn.de/people/huybrech/ErratumK3.html)
and draft warning were inspected; the cited general criterion
and proof above are the source used here.

Read Markman, *On the monodromy of moduli spaces of sheaves
on K3 surfaces*, [arXiv:math/0305042v3, 6 October 2005,
sections 3.1--3.2, pp. 19--23](https://arxiv.org/pdf/math/0305042v3#page=19).
Equations (32)--(33) define theta_v by pushforward of the
universal Chern character times sqrt(td_S), using x^vee and
division by the quasi-universal similitude. The extension outside
v^perp can depend on the family, and the normalized class of
equation (27) handles its line-bundle ambiguity. This supplies
the action convention to use for the pullback. It does not
control f^* or make it an isometry. The geometric Chern class,
the chosen theta_v convention and the direction of the desired
self-correspondence must be tracked, rather than identifying
H^2(M) with T(S) as if this determined an action on S.

Read Caldararu, *Non-Fine Moduli Spaces of Sheaves on K3 Surfaces*,
[arXiv:math/0108180v1, 27 August 2001, Theorems 3.1--3.4
and their preceding setup, pp. 12--14](https://arxiv.org/pdf/math/0108180v1#page=12).
The quoted K3-surface identification and equivalence require
a primitive **isotropic** vector and a compact nonempty moduli
space. Their v^2=0 hypothesis fails here. They cannot replace
the missing surface map by a Fourier--Mukai equivalence.

Read Verbitsky, *Trianalytic subvarieties of the Hilbert scheme
of points on a K3 surface*, [arXiv:alg-geom/9705004v2,
11 November 1997, Theorem 1.1, p. 4, and Definition 2.10,
p. 10](https://arxiv.org/pdf/alg-geom/9705004v2#page=4).
The exclusion requires an automorphism-free K3, a Mumford--Tate
generic induced complex structure in the stated hyperkahler sense,
and a trianalytic subvariety. None of these extra hypotheses is
established for the proposed image on this projective RM locus.
The generic nonprojective no-subvariety conclusion is not a
no-map theorem for the saved target.

## Comparison with earlier routes and bounded test

The local DAG and existing assessments were checked for overlap.
The terminal-syzygy and mixed-presentation stops concern their
specific representatives, and L037 concerns automatic cycle
supply from a square-form comparison. None treats this sheaf
moduli source. Reuse those stops without reproducing their proofs.
The already checked isometry limitation in L004 remains a useful
comparison if a proposed construction only produces isometries;
it is not an exclusion of arbitrary f or arbitrary correspondences.

One separate research turn may use the known generic kernel model
to test an independently specified S-parameterized family and
evaluate its normalized universal-correspondence action. Start
with the reduced three-point locus if appropriate, keeping the
collision and boundary qualifications explicit. In particular,
moving one point while fixing two is only a test recipe; neither
its extension over collisions nor its action is asserted here.
Check whether a quotient family exists before assuming its kernel
defines the required global map. Do not assume that ordered
support points or a relative double dual descend automatically.

Continue upon a concrete flat stable family with controlled
non-scalar action on an intended transverse surface, or an
informative obstruction that changes the selected construction.
Stop a recipe if its action is scalar or its input already requires
the missing non-scalar correspondence. A scalar calculation for
one recipe does not exclude maps whose images lie in other strata.
Merely observing that a known universal family can be pulled back
after assuming f exists would not justify an ADVANCE.

The achieved span remains 21 on the explicit Dickson family,
and three RM directions remain covered against four required.
The six-dimensional moduli space is an auxiliary target dimension,
not an increased cycle span or an additional RM direction.
Map existence, controlled action, transverse coverage and the
universal Hodge gap remain unresolved. This is the first consecutive
EXPLORATION after L037; the assessment does not reset that count.

## Search record and access qualifications

Representative exact and broader queries actually used:

- `K3 "M_H(2,0,-1)" universal sheaf map`
- `K3 surface morphism moduli "2, 0, -1"`
- `"K3" "moduli" "(2,0,-1)"`
- `"K3" "M(2,0,-1)"`
- `K3 surface embedding moduli stable sheaves transcendental endomorphism real multiplication`
- `Markman Hodge conjecture K3 surface universal sheaf non isometric endomorphism`
- `"K3" "moduli" "c_2=3" "rank"`
- `"K3" "surface" "map" "Hilbert cube"`
- `"K3" "universal sheaf" "non-scalar"`
- `"K3" "surface" "Hilbert scheme" "trianalytic" Verbitsky`
- `Mukai "On the moduli space of bundles on K3" pdf "A.6"`
- `Huybrechts Lehn "Theorem 4.6.5" "universal"`
- `"K3" "real multiplication" "Hodge conjecture" "2026" Markman`

The [author-hosted O'Grady PDF](https://www1.mat.uniroma1.it/people/ogrady/zero-cycles-on-k3s.pdf)
timed out; access was resolved through the complete arXiv v2 PDF.
Mukai's [author-hosted original paper](https://www.kurims.kyoto-u.ac.jp/~mukai/paper/Tata.pdf)
was located, but its scanned appendix yielded no readable text
or usable screenshot in this tool session. Theorem A.6 was not
read and is not cited as inspected evidence. Its access is not an
essential gap here: the complete general criterion and proof
were read in Huybrechts--Lehn. Search hits for general surveys,
other Hilbert-cube geometries and claimed broad Hodge resolutions
were not used as theorem-level evidence. No novelty follows from
failure to find a full-statement match.

An intermediate REVIEW_REQUIRED source checkpoint was saved
before the final scope comparison and is incorporated above.
No new map, action formula, obstruction, lemma, mathematical
script or complete informal candidate was produced.

## Mathlib

Coverage: **not checked** for the full map/action statement or
the supporting moduli, universal-family and Mukai-map theorems.
No matching Mathlib theorem or absence from checked sources is
asserted. The named results and direct links above are supporting
mathematical sources; none is a match for the full target.
