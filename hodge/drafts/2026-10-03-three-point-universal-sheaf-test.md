# Three-point universal-sheaf test — preliminary reasoning and decision

The saved target and prior SPECIALIZE assessment in
`drafts/literature/2026-10-03-cubic-rm-universal-sheaf-map.md`
are unchanged for this research step. The gap is a non-scalar
algebraic action on a transverse cubic-RM surface; arbitrary
primitive fourfold classes and higher dimensions remain separate.

Test the explicit quotient of O_(S x S)^2 by the sum of the
diagonal and two constant point sections, with three distinct
constant quotient lines. This is the one-moving-point recipe
named in the prior assessment, not an assumed global stable map.
The sought threshold is a non-scalar action and a global stable
family. A scalar action or collision instability stops this recipe.

Reasoning to check: the quotient should remain surjective at a
two-point collision because the two quotient lines are independent;
its kernel should therefore be flat. The distinct-point fibres
should be Gieseker stable because a constant rank-one direction
must vanish at at least two points. At a collision, the direction
killed by the remaining quotient should instead contain I_p,
whose Euler characteristic exceeds the rank-normalized kernel's.
The K-theory class suggests ch_2=-[Delta]-[S x p]-[S x q],
hence scalar action. Markman's x^vee convention must be retained.

These were the initial checkpoint questions. They are resolved in
the full proof [L038](../lemmas/L038-one-moving-point-sheaf-map-is-scalar.md):
the family is flat, stable off the two collisions and unstable at
both collisions; its ch_2 action is -id and its normalized Mukai
action is +id. A hypothetical stable repair over those two base
points cannot change that scalar action, by Chow localization and
the extension of base line bundles across codimension two.

Decision: stop this recipe. It supplies one transcendental
dimension against three required by E and no additional RM
direction. Other support families, unordered descent and boundary
images remain open. Moduli prerequisites and the action convention
are imported; this explicit calculation is a reproduction and
application of known tools, with no claim of originality.

Re-read Markman, arXiv:math/0305042v3, equations (32)--(33),
printed p. 23, solely to check the sign in the reused convention.
The positive pushforward with x^vee agrees with the +id result.
No change to the prior approved assessment was needed.
