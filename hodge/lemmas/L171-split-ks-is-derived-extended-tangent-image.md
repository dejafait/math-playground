# L171 — The actual split KS map is the derived extended tangent map

## Hypotheses

Retain the entire conditional family and actual maps of L164. Thus
p:S_1 x B -> B is the projection of the identical marked projective
K3 surfaces with the fixed common hyperkähler metric, real Kähler
class, ordered triple and holomorphic forms. The hypothetical locally
free rank-two product-polystable F has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2,
\]

with the full prescribed tensor and actual compatible connection.
Put V=End_0(F), C=Rp_*V, M=R^1p_*V and W=R^2p_*V. The split
support Z is finite and reduced. Use L111's M=M** locally free of
rank 50, L108's specific extended inclusion i:T_B -> M and splitting
M=i(T_B) direct sum N, and L116's actual truncation inclusion
j:M[-1] -> C. No new splitting of C or M is chosen.

For z in Z, write M(z) for the ordinary residue fibre, and use
L164's actual injection

\[
 e_z=H^1(L\iota_z^*j):M(z)\hookrightarrow
 E_z=H^1(S_1,V_z),
\]

where the target identification is derived base change. Let
kappa_z:T_zB -> E_z be L111's actual determinant-fixed family KS
map, with the first-order convention in its equation (7). No ordinary
middle-base-change isomorphism, genericity, endpoint s,t, integrability
of arbitrary sections, or existence of F or z is assumed.

## Conclusion

For every z in Z, the actual maps satisfy

\[
                  e_z\circ i(z)=\kappa_z.                 \tag{1}
\]

In particular the actual KS plane is e_z(i(T_zB)). The equality uses
the first-order convention specified below; using the opposite sign
for the universal Atiyah class changes its auxiliary representative,
not either actual map in (1). Both maps land in the full 52-dimensional
derived middle space E_z; the 50-dimensional ordinary fibre has not
been substituted for that space. Empty Z is vacuous.

This is a conditional specialization of known Atiyah/KS, extension
and derived-map tools. The separate step 571 critical audit below
preserves the identity, with EXPLORATION / REPRODUCTION and no substantive
error or stronger conclusion found. It fills
the map-comparison gap left in L170, but this step does not test the
section-image intersection or assert an improved section threshold.
It evaluates no section bracket or quadric and proves neither F's
existence nor a split-cardinality exclusion. Primitive realization,
transport and the independent global obstruction questions remain open.

## Proof

**Imported constructions and their scope.** Reuse the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-split-ks-extended-tangent-comparison.md`.
Import the all-family Atiyah/KS construction and its first-neighbourhood
interpretation from Huybrechts--Lehn, *The Geometry of Moduli Spaces
of Sheaves*, E31 (1997), 10.1.5, 10.1.7--8 and Example 10.1.9,
[pp. 218--221](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=230).
No simple or stable fibre is needed for that construction. Import
derived pullback naturality from Nikolas Kuhn, *The Atiyah class on
algebraic stacks*, Forum Math. Sigma **12** (2024), e100,
DOI [10.1017/fms.2024.109](https://doi.org/10.1017/fms.2024.109),
Lemma 4.4/Claim 4.5 and Corollaries 4.6--4.7, pp. 32--35, and the
deformation-extension comparison in Lemmas 6.11--6.12 with proof,
pp. 50--51. Here the spaces are schemes, F is a vector bundle in
degree zero, and its pullback to a trivial dual-number thickening is
flat; multiplication identifies the ideal tensor the reduced bundle
with the ideal times the thickened bundle. These are within the cited
scope, including at a nonsimple split fibre. The general constructions
are imported, not reproved.

Use [Stacks 31.13.12, 0EBJ](https://stacks.math.columbia.edu/tag/0EBJ)
for full faithfulness on reflexive sheaves across a finite subset of
the smooth surface B. Use
[36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91) for
perfect pushforward and derived base change: p is proper, flat and
finitely presented, and V is locally free. For local derived maps use
[13.19.8, 064B](https://stacks.math.columbia.edu/tag/064B), in the
module category over O_{B,z}, and use the canonical truncation triangle
as in [13.12.4, 08J5](https://stacks.math.columbia.edu/tag/08J5).
No projectivity of vector bundles as global sheaf objects is asserted.
The remaining proof checks these constructions against the actual maps.

**An auxiliary derived family KS morphism.** The product has the
canonical algebraic splitting
Omega^1_{S_1 x B}=p_1^*Omega^1_{S_1} direct sum p^*Omega^1_B.
Project the Atiyah class of F to its base component. Since F is
locally free, this is a class in
Ext^1_X(O_X,End(F) tensor p^*Omega^1_B). Project coefficients by

\[
 A\longmapsto A-\tfrac12\operatorname{Tr}(A)\operatorname{id}_F,
\]

contract with p^*T_B, and apply derived adjunction. The result is an
algebraic morphism

\[
                \alpha:T_B[-1]\longrightarrow C.          \tag{2}
\]

Normalize the sign of the universal extension class so that the
deformation bar-partial_F+epsilon a has class +[a]. This fixes one
global sign in (2); it is the first-order KS convention used in
L111, where the induced endomorphism differential is
bar-partial+epsilon[a,-]. If the principal-parts convention for the
Atiyah class has the opposite sign, negate that class before (2).
There is no point-dependent scalar or change to i or kappa_z.

Let f=H^1(alpha):T_B -> M. On U=B minus Z the imported construction
is the actual algebraic family KS morphism. L108 constructs its i
by extending precisely that morphism. Consequently f|_U=i|_U.
Both T_B and M are reflexive vector bundles, the latter by L111;
the depth condition at the removed points is two. Full faithfulness
of restriction therefore gives

\[
                           f=i.                           \tag{3}
\]

This compares sheaf maps only. To obtain (1), it remains to check
both the derived lift and its first-order fibre interpretation.

**The first-order interpretation retains the normal direction.**
For u in T_zB let b_u:Spec C[epsilon]/(epsilon^2) -> B represent u,
and pull F back along id_{S_1} x b_u. Denote the resulting bundle
by F_u. Forgetting the dual-number structure gives the extension
of O_{S_1}-modules

\[
 0\longrightarrow F_z\xrightarrow{\epsilon}F_u
      \longrightarrow F_z\longrightarrow0,               \tag{4}
\]

where flatness identifies epsilon F_u with F_z. The cited
first-neighbourhood interpretation and pullback naturality identify
the contraction by u of the derived fibre of (2) with the trace-free
part of the extension class (4). In making this comparison one keeps
the base cotangent factor restricted to z and pairs it with u.
One does not map it to the zero cotangent space of Spec C; doing so
would erase the first-order direction rather than compute KS.

In the first-order Dolbeault description of (4), its class is [a]
for the family bar-partial_F+epsilon a, with the sign fixed above.
Changing a horizontal trivialization adds a fibre Dolbeault
coboundary. This is exactly L111's actual family class kappa_z(u),
whose induced action on endomorphisms is [a,-]. The trace-free
projection leaves this fibre class unchanged: trace takes values in
H^1(S_1,O_{S_1})=0, and End(F_z)=O_{S_1} direct sum End_0(F_z).
In particular the projected class is its unique trace-free class.
Thus, using the actual derived base-change identification,

\[
 H^1(L\iota_z^*\alpha)(u)=\kappa_z(u).                    \tag{5}
\]

This argument uses the deformation of the actual F, rather than a
coarse stable-moduli tangent theorem at z. It therefore applies to
L direct sum L^{-1}. It assumes neither simplicity nor ordinary
R^1 base change.

**Comparison with the actual truncation lift.** Set R=O_{B,z},
k=R/m, and T=(T_B)_z. The module T is finite free. Let K be a
bounded finite free representative of the actual C_R. Morphisms
out of the one-term projective complex T[-1] can be computed by
chain maps, and exactness of Hom_R(T,-) gives

\[
 \operatorname{Hom}_{D(R)}(T[-1],C_R)
   =H^1\operatorname{Hom}_R(T,K)
   =\operatorname{Hom}_R(T,H^1(K))
   =\operatorname{Hom}_R(T,M_R).                           \tag{6}
\]

The isomorphism sends a derived morphism to its degree-one map.
The actual j_R induces the identity of M_R, by its truncation
definition. Hence alpha_R and j_R composed with i_R[-1] both
map under (6) to i_R, by (3). They are the same derived morphism:

\[
                   \alpha_R=j_R\circ i_R[-1].             \tag{7}
\]

This is a local argument and needs no choice of a global splitting
or homotopy. Applying derived tensor with k to (7) preserves equality
of derived morphisms. Since T and M_R are free, the source and the
middle term in this composite reduce to T_zB[-1] and M(z)[-1].
The degree-one map of the reduction of j_R is, by definition,
L164's e_z. Combining (5) and (7) gives (1).

For clarity, K derived-tensor k is the full fibre complex, not its
ordinary degree-one cohomology tensored with k. At a split point
L111's minimal representative has residual dimensions (1,52,1)
and zero differentials. L164's map e_z is the injection of the
50-dimensional ordinary middle fibre into that 52-dimensional middle
space. Equation (7) is an equality before taking any fibre, so it
compares the actual lifts without removing the two additional
middle directions or choosing them away. This completes only the
approved comparison.

**Separate critical audit (2026-10-26, step 571).** The invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-split-ks-extended-tangent-critical-audit.md`
approves exactly this audit. The primary constructions and precise
citations above are imported using step 568's inspected statements and
proof cases; this audit does not claim fresh source retrieval or reprove
those general results. The direct inputs remain L108, L111, L116 and
L164, including their conditional family hypotheses. L170 is downstream
motivation, not a premise. No substantive defect was found in (1).

First check the type of the auxiliary morphism. Because F is locally
free, the base component of its Atiyah class lies in
Ext^1_X(O_X,V tensor p^*Omega_B^1) after trace-free projection. The
locally free duality between p^*Omega_B^1 and p^*T_B identifies this
with Hom_D(X)(p^*T_B,V[1]). Derived adjunction, followed by the same
shift on source and target, gives (2). Thus its degree-one sheaf map
has source T_B, with no dual tangent space or degree-zero shift.
The product splitting is essential: it selects the base component
while retaining its cotangent factor on restriction. Pulling the
Atiyah class all the way to the cotangent of a closed point instead
would not be this construction.

For the sign check, smoothly split (4) and write its underlying bundle
as pairs (v,w), meaning epsilon v+w, with the first entry the subobject.
For bar-partial_{F_u}=bar-partial_{F_z}+epsilon a, its differential is

\[
 (v,w)\longmapsto
       (\bar\partial v+a\wedge w,\bar\partial w).
\]

The off-diagonal term therefore represents the extension by +[a].
Changing the smooth splitting changes a by a Dolbeault coboundary.
The induced operator on End(F_z) is
bar-partial+epsilon[a,-], exactly the convention used in L111 (7).
The one universal Atiyah sign chosen in (2) consequently works both
on U and at every split point; no actual i or kappa_z is rescaled.
Trace of [a] lies in H^1(S_1,O)=0. The split trace decomposition
End(F_z)=O direct sum V_z, valid in characteristic zero for rank two,
then identifies [a] with its unique class in H^1(V_z). This checks
trace-free projection at nonsimple fibres without invoking stability.

The cited first-neighbourhood interpretation applies because F_u is
locally free on the dual-number product: multiplication by epsilon
identifies its ideal submodule with F_z, as required in (4).
Pullback naturality and perfect proper base change identify the
contraction of (2) with that extension. They apply to the morphism
and not just the cohomology dimensions. In this comparison the
restricted factor Omega_B^1|_z is paired with u before forgetting
the first-order direction. Thus (5) is valid in the full E_z even
when the fibre is L direct sum L^{-1}.

Next check the specific extension. L108 defines i|_U as the actual
family KS map, with the same first-order Dolbeault convention, and
extends that map into M**. L111 identifies the canonical M -> M**
with an isomorphism. Both H^1(alpha) and i are therefore maps into
this same M. The reflexive restriction theorem applies on the smooth
integral surface B across finite Z (depth two). Their equality on U
gives (3). It would not justify global equality of derived maps; the
proof does not use it for that purpose.

Finally check (6) at the stalk. A chain map T[-1] -> K is a map
T -> Z^1(K); two such maps are homotopic precisely when their
difference comes from Hom_R(T,K^0) through d^0. Since T is finite
free, Hom_R(T,-) preserves the surjections K^0 -> im(d^0) and
Z^1(K) -> H^1(K). The quotient of chain maps by homotopies is
therefore exactly Hom_R(T,H^1(K)). This verifies the displayed
derived Hom calculation using the cited projective-complex theorem.
The canonical j_R induces id_M, so alpha_R and j_R i_R[-1] have the
same class, giving (7). Global projectivity or global uniqueness of
a lift is neither asserted nor needed.

Derived tensor with k preserves that equality. Since T and M_R are
free, their reductions have no additional Tor terms; K tensor k,
however, remains the full derived fibre. L164's actual e_z is the
degree-one map of this same reduced j_R. At a split point the
minimal complex has zero residual differentials and dimensions
(1,52,1); neither of the two middle directions outside the ordinary
50-dimensional image is deleted. Equations (5) and (7) thus give
the equality of maps (1), not merely equality of images or a scalar
multiple. For empty Z the assertion is vacuous.

The audit preserves only this identity. It assumes the previously
audited conditional inputs; it is not a fresh audit of their entire
ancestry. It proves no section-intersection claim, no bracket
vanishing and no improved threshold. In particular ATTEMPTS/092–094
remain unaffected: additive splitting and actual base integrability
do not imply arbitrary section integrability, and the complementary
global operation is still unevaluated. Existence of F, actual section
quadrics, square length, transport and primitive realization remain open.

## Mathlib

Full matching coverage for the all-family Atiyah/KS and actual derived
truncation comparison has not been checked; no absence is claimed.
The cited primary sources supply the general constructions, and the
proof above is their informal conditional specialization to the actual
family. It is not a formal verification or a resolution of the Hodge
conjecture.
