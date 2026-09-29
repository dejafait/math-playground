# Stable lifts of degree-three support maps — literature assessment

TARGET: Review criteria for lifting degree-three support morphisms S -> S^{(3)} to stable sheaf maps S -> M_H(2,0,-1), including collision strata.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact Mukai vector, exceptional non-locally-free K3 moduli, spherical/reflection transforms, punctual Quot stability, Hilbert-Chow lifting and blowup ideals; followed Yoshioka's exceptional-vector classification and read the primary statements below. A global Hilbert-cube theorem replaces the previously recorded generic model; no inspected result supplies an independent non-scalar cubic-RM support map.
SOURCE_EVIDENCE: Yoshioka, arXiv:math/9907001v2 (7 February 2000), section 0.2 and Proposition 3.4 with proof, PDF pp. 2,16, https://arxiv.org/pdf/math/9907001v2#page=16; Ekedahl--Skjelnes, Annals of Mathematics 179 (2014), Definition 2.7, section 7.24, Theorem 7.25 and Corollary 7.28, printed pp. 811,834--837, https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=32; Stacks Lemmas 31.33.5 (0806), https://stacks.math.columbia.edu/tag/0806, and 27.16.11 (01O4), https://stacks.math.columbia.edu/tag/01O4; Fu--Namikawa, arXiv:math/0306091v2 (19 June 2003), Definition 1 and Corollary 2.3, PDF pp. 2,5, https://arxiv.org/pdf/math/0306091v2#page=5; O'Grady's previously inspected Proposition 4.2 and Remark 4.3 were reread for comparison.
COMPARISON: Yoshioka supplies a global moduli-space isomorphism M_H(2,0,-1) with S^[3], including nonreduced subschemes, and already covers the pointwise trivial hull used in L039. Ekedahl--Skjelnes and Stacks supply precise Hilbert-Chow and general lifting frameworks. The actual weighted-support compatibility and its correct boundary-inclusive specialization must be checked separately; generic birationality and the Cartier criterion alone do not settle every prescribed support map.
GAP: Identify L039's weighted support morphism under the cited global isomorphism, then specialize the canonical blowup/relative-Proj lifting data with collision and descent qualifications. An independent support map with non-scalar action on a transverse cubic-RM surface remains a separate unresolved input.
REASON: Import the global Hilbert-cube theorem and general lifting results without reproof. Continue in a separate research turn with the single support-preserving lifting-criterion test below; do not classify all punctual rank-two quotients or assume every symmetric-product map lifts. This assessment changes the available mechanism but produces no lift, action calculation or originality claim.

## Hypotheses and relevance

Keep S a smooth projective complex K3 surface and
M=M_H(2,0,-1) the moduli of Gieseker-stable torsion-free sheaves.
The saved context uses v-generic H. The imported theorem uses
H general in the sense of Yoshioka's section 0.2; retain that
hypothesis, and check it explicitly before claiming the result
for a weaker interpretation of v-generic. This does not alter
the support-map or cubic-RM target. The intended application
has rank-eighteen T(S) and full endomorphism field
E=Q(zeta_7+zeta_7^(-1)). No RM or Picard-rank-one condition
is imposed by the source theorem.

The main gap on this route is an independent non-scalar
algebraic action on a surface beyond the Dickson locus. The
intermediate target screens whether a degree-three support
morphism can furnish an everywhere stable family. Its plausible
downstream use is the universal-sheaf correspondence and L039's
action formula. A correct lifting criterion still leaves the
support-map construction, its non-scalar action, transverse
coverage and the universal primitive Hodge gap unresolved.

## Conclusion

The unchanged saved target now has a ready SPECIALIZE assessment.
The global model is a known theorem, recorded by precise citation
in [the source note](../../foundations/06-exceptional-hilbert-cube-model.md).
Its discovery removes the need to extend O'Grady's generic kernel
model by a new quotient classification. The identification with
the notebook's specified support morphism and the application of
general lifting criteria remain a bounded specialization, not an
established conclusion of this literature turn.

## Inspected statements and applicability

Read Yoshioka, *Irreducibility of moduli spaces of vector bundles
on K3 surfaces*, arXiv:math/9907001v2, Proposition 3.4 and its
proof, equations (3.42)--(3.47), [PDF p. 16](https://arxiv.org/pdf/math/9907001v2#page=16),
with the polarization setup on PDF pp. 1--2 and Case B on p. 12.
Set v_0=v(O_S)=(1,0,1) and l=2 in its exceptional family
l v_0-(l+1)omega. This is the exact saved vector. Unlike the
general deformation/birational conclusion of Theorem 0.1,
Proposition 3.4 is an isomorphism of moduli spaces. Its proof
uses the contravariant reflection-and-dual functor with kernel
I_Delta and relative Ext^1; it also proves the actual trivial
hull. The source note imports the statement without reproof.

Reread O'Grady, *Moduli of sheaves and the Chow group of K3
surfaces*, arXiv:1205.4119v2 (22 May 2012), Proposition 4.2,
its proof and Remark 4.3, [pp. 11--12](https://arxiv.org/pdf/1205.4119v2#page=11).
Its distinct-point construction gives a birational map. This is
compatible with, and weaker than, the global theorem above.
The earlier assessment inspected Yoshioka's Theorem 0.1 but
did not inspect Proposition 3.4; no assertion that a global
theorem was absent from the literature is retained.

Read Ekedahl--Skjelnes, *Recovering the good component of the
Hilbert scheme*, **published version**, Annals of Mathematics
179 (2014), 805--841: Definition 2.7 and Lemma 2.9, p. 811;
Proposition 7.23, section 7.24 and Theorem 7.25 with proof,
pp. 834--835; Proposition 7.27 and Corollary 7.28 with proof,
[pp. 835--837](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=30).
Corollary 7.28 identifies the entire Hilbert scheme for a smooth
separated surface with the blowup in the specified ideal of norms.
Proposition 7.23(4) identifies the divided-power base with the
symmetric product in this characteristic-zero case. The centre
is the source's ideal sheaf from section 7.24; its scheme
structure must be retained rather than substituting an unnamed
reduced collision locus. This covers the Hilbert scheme's
nonreduced boundary as well as its distinct-point open.

Read [Stacks Lemma 31.33.5, Tag 0806](https://stacks.math.columbia.edu/tag/0806),
statement and proof, on 2026-10-03. The blowup is final among
maps whose inverse image of the centre is an effective Cartier
divisor. This is a useful criterion within its stated category.
It does not assert that every map to the base lies in that
category or treat every map entirely inside the centre.

Read [Stacks Lemma 27.16.11, Tag 01O4](https://stacks.math.columbia.edu/tag/01O4),
statement and proof, on 2026-10-03. For a graded algebra
generated in degree one, relative Proj represents invertible
sheaves L with a graded map into the algebra of tensor powers
of L and a surjective degree-one part, modulo the stated
equivalence. This supplies a framework retaining the graded
relations, including maps into exceptional fibres. A line
quotient of a pulled-back ideal without its graded relations
is not the statement of this theorem.

Read Fu--Namikawa, *Uniqueness of crepant resolutions and
symplectic singularities*, arXiv:math/0306091v2, the introductory
projectivity convention and Definition 1, PDF p. 2, and
Theorem 2.2 with Corollary 2.3, [PDF pp. 4--5](https://arxiv.org/pdf/math/0306091v2#page=5).
Corollary 2.3 says every projective crepant resolution of a
smooth surface's symmetric product is isomorphic to Hilbert--Chow.
Definition 1 uses an isomorphism over the same base, which is
stronger than equivalence after a base automorphism. This is
a supporting alternative if the actual moduli support morphism
is first shown to be such a resolution; no such verification
is made here. Yoshioka's direct theorem suffices for the
abstract global model, so no uniqueness reproof is justified.

## Remaining specialization and continuation test

Import the global isomorphism, rather than reproduce its
reflection-transform proof. The bounded test is whether its
composition with Hilbert--Chow equals L039's weighted support
morphism on all stable sheaves, and whether the canonical
blowup/relative-Proj data then give a precise stable-lift
criterion for the prescribed g:S -> S^{(3)}. Agreement only
on a particular S-parameterized dense open is insufficient
for an image wholly contained in a collision stratum.

For a map generically outside the centre, screen the exact
effective-Cartier inverse-image hypothesis and the uniqueness
claim that it permits. For an image contained in the centre,
retain the pulled-back Rees algebra and its graded relations;
do not turn the possibly zero image ideal in O_S into a
blanket no-lift assertion. Treat the fine universal sheaf and
base-line-bundle ambiguity using
[the already inspected assessment](2026-10-03-cubic-rm-universal-sheaf-map.md).
A morphism to the Hilbert cube, a degree-three cycle, and a
flat quotient are distinct data until their applicability
and support agreement are justified.

Continue if the imported model yields this boundary-inclusive
criterion without assuming the desired non-scalar correspondence.
If support compatibility or a claimed lifting condition fails,
record the precise exception and restrict that condition. Do
not restart the stopped one-moving-point family, assert an
arbitrary map lifts, or count an abstract isomorphism as a
non-scalar action. No part of this test is derived in this turn.

## Redundancy, previous failures and actual threshold

Inspected the complete overview, local DAG, L039, the saved
assessment, recent histories, and the one-moving-point stop.
L038's scalar action and unstable collision fibres remain
evidence about that presentation; a global moduli isomorphism
does not repair its quotient or create its non-scalar action.
L039 remains unchanged. Its pointwise trivial-hull input is
already covered by Yoshioka's proof; its relative family/action
specialization is not imported as a matching theorem.

The current step imports known mathematics and improves the
local route by replacing generic-model uncertainty with a
global model. It is not progress beyond the checked literature.
The attained span remains 21 on the Dickson family, with three
RM directions against four required. The stopped scalar recipe
still contributes one transcendental direction against three
required by E. No new cycle, transverse surface or complete
informal candidate is supplied.

## Search and access record

Queries actually used included:

- K3 "(2,0,-1)" "symmetric"
- K3 "Hilbert cube" "spherical" moduli sheaves
- K3 rank two c2 three stable sheaves support Uhlenbeck collision Quot
- "K3" "(2, 0, -1)" Hilbert
- "K3" "c_2=3" moduli Hilbert
- "symmetric product" "unique symplectic resolution" surface
- "punctual Quot" "stability" rank two
- Fu Namikawa Uniqueness of crepant resolutions symplectic singularities arxiv
- Hilbert scheme points surface blowup symmetric product diagonal Fogarty ideal universal property lift
- Haiman Hilbert scheme symmetric product blowup ideal alternating polynomials theorem
- "Yoshioka" "Proposition 3.4" "Hilbert" 9907001
- "Hilbert-Chow" "lifting" morphism collision surface
- site:stacks.math.columbia.edu morphisms relative Proj invertible sheaf surjection graded algebra generated degree one

The primary statements listed above were read, not inferred
from search snippets. Yoshioka's submission history confirms
the inspected v2 date. The Fu--Namikawa PDF identifies itself
as v2 (19 June 2003); its regenerated title-page date is not
treated as a new theorem version. Hilbert-scheme summaries,
Haiman's plane-specific blowup paper and Quot/enumerative hits
were discovery leads, not independently inspected theorems
used here. The published Ekedahl--Skjelnes surface statement
resolves the needed blowup source scope. No essential source
is inaccessible for this SPECIALIZE decision. An intermediate
source checkpoint was saved and is incorporated here.

## Mathlib

Coverage: **not checked** for the full stable-lifting target,
the global moduli isomorphism, Hilbert--Chow, the ideal of norms,
or its supporting relative-Proj and blowup inputs. Direct
primary references above are supporting theorem matches for
the identified parts, not Mathlib matches for the full target.
No absence from checked Mathlib sources or novelty is asserted.
