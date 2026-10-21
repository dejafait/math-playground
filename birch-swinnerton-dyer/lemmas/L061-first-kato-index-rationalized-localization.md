# L061 — First Kato index and rationalized classical localization

## Hypotheses

Retain every hypothesis of L026: E/Q is non-CM; p>=5 is good ordinary;
E[p] has surjective residual representation; p divides neither #E(F_p),
the Manin constant nor any Tamagawa factor; E(Q_p)[p]=0; a residual
Kurihara number is nonzero in Sakamoto's N_(1,0), with compatible Neron
plus-period and discrete-logarithm conventions; L(E,1)=0; w(E)=+1; and
the quadratic coefficient a_2 of the fixed primitive ordinary cyclotomic
series is independently certified nonzero. No point, finite-Sha or
zero-finite-Selmer-quotient hypothesis is added.

Set A=E[p^infinity], T=T_p E, D=Sel(Q,A), and

\[
L_p=\operatorname{im}\bigl(E(\mathbf Q_p)\otimes\mathbf Q_p/\mathbf Z_p
                  \longrightarrow H^1(\mathbf Q_p,A)\bigr),\quad
f=\operatorname{loc}_p:D\longrightarrow L_p,\quad D_0=\ker f.
\]

These are classical Kummer conditions at every place; D_0 changes only
the condition at p to zero. Use L005's compact rationalized space S,
completed local space V_loc and map lambda_p. Fix Kim's complete Kato
Kolyvagin system kappa for (T,F_can,P), with his coefficient ideals I_n,
square-free indices N_1 and auxiliary generators. Define

\[
k=\min\{\nu(n):n\in N_1,\ \kappa_n\ne0\},
\]

where nu(n) counts prime factors and the minimum concerns the whole
system, not its singular localization or a residual scalar collection.
The proof below establishes that this minimum exists. The ready assessment
is [the first-index specialization assessment](../drafts/literature/2026-10-14-first-kato-index-localization-criterion.md).

## Conclusion

There are natural identifications

\[
S=(T_pD)\otimes\mathbf Q_p,\qquad
V_{\rm loc}=(T_pL_p)\otimes\mathbf Q_p,\qquad
\ker\lambda_p=(T_pD_0)\otimes\mathbf Q_p,
\tag{1}
\]

under which lambda_p is the rationalized Tate-module map of f. In
particular

\[
\dim S=2,\quad \dim\ker\lambda_p=k,\quad
\operatorname{rank}_{\mathbf Q_p}\lambda_p=2-k,\quad k\in\{1,2\}.
\tag{2}
\]

Write I=f(D). The complete alternatives are:

- k=1: I=L_p, lambda_p is nonzero and surjective, and its kernel is
  a one-dimensional strict Selmer space. The integral Tate-module map
  has finite cokernel; it need not be surjective.
- k=2: I is finite cyclic, possibly zero, and lambda_p=0. A nonzero
  finite image is retained and does not give rationalized nonvanishing.

Equivalently, nonzero rationalized localization is certified by a
nonzero whole-system component kappa_ell at a one-prime index ell in
Kim's P. This is an exact existence criterion, not a method producing
such a component or selecting the successful branch from TM=0.

Kim's ordinary/strict sequence identifies

\[
0\longrightarrow D_0\longrightarrow D\longrightarrow I\longrightarrow0,
\qquad
I\simeq\left(H^1_{/f}(\mathbf Q_p,T)\big/
                  \operatorname{loc}_p^s\operatorname{Sel}_{\rm rel}(\mathbf Q,T)
          \right)^\vee.
\tag{3}
\]

Here relaxed means unrestricted at p and classical elsewhere, and vee
is Pontryagin dual. Both finite and positive-corank quotients are retained.
No finite Sha, rational Kummer membership, positive rational rank,
auxiliary construction or comparison with complex order follows.

## Proof

**Named source imports and applicability.** Import Kim, *The structure of
Selmer groups and the Iwasawa main conjecture for elliptic curves*,
publisher-hosted author text dated 2025-05-12: [Sections 2.1--2.3,
printed pp. 10--12](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=11)
for the conditions/system; [Definition 2.12 and Theorem 2.13(5),
pp. 14--15](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=15)
for k=corank_Z_p D_0; [Proposition 3.13, p. 20](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=21)
for equivalence of whole-collection nonvanishing; and [(5.1), p. 26,
and Sections 5.3.2--5.3.4, pp. 27--28](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=27)
for (3) and the two corank branches. These general theorems are imported,
not reproved.

L026's termwise coefficient/period matching makes the integral Kurihara
collection nonzero from its retained residual witness. Proposition 3.13
therefore makes the whole Kato system nontrivial. Its residual
surjectivity and prime-to-p Manin premises hold. The construction's
local divisibility premise holds since H^0(Q_p,A)=0 is divisible;
surjectivity supplies the residual working hypotheses. Thus Theorem
2.13(5) applies. This invokes no componentwise equivalence between
Kurihara and Kato values. Neither source branch is discarded.

**Global coefficient matching.** Surjectivity of the action on E[p]
implies E(Q)[p]=0: the standard two-dimensional representation of
GL_2(F_p) has no fixed nonzero vector. A nonzero invariant p-power
torsion point would yield one of order p by multiplication, so
H^0(Q,A)=0. The exact coefficient sequence

\[
0\longrightarrow E[p^n]\longrightarrow A
  \xrightarrow{p^n}A\longrightarrow0
\]

then gives a natural isomorphism
H^1(Q,E[p^n]) -> H^1(Q,A)[p^n]. Under the two coefficient inclusions
into E, the induced localization maps to H^1(Q_v,E) commute. The
infinite Kummer sequence identifies its kernel on H^1(Q_v,A) with
E(Q_v) tensor Q_p/Z_p; this is the direct limit of the finite Kummer
sequences, an exact direct limit. Hence the global isomorphism restricts
to

\[
\operatorname{Sel}_{p^n}(E/\mathbf Q)\simeq D[p^n].
\tag{4}
\]

This kernel argument keeps local torsion at places other than p; it
does not assume local H^0 vanishing there. The real place has no
positive-degree p-primary cohomology since p is odd.

The coefficient maps in (4) commute with downward multiplication by p:
both composites are multiplication by p after inclusion into A. On the
point quotients these are reduction, as in the finite Kummer diagram.
Thus their inverse limits identify L005's compact Selmer module with
T_pD=lim_n D[p^n]. This is an inverse limit of isomorphisms, not an
assertion that an inverse limit preserves an arbitrary surjection.

**Local and strict matching.** The premise E(Q_p)[p]=0 similarly gives
H^0(Q_p,A)=0. The local coefficient isomorphism restricts to

\[
E(\mathbf Q_p)/p^nE(\mathbf Q_p)\simeq L_p[p^n],
\tag{5}
\]

through their injective Kummer maps. This again follows by taking the
kernel of the maps to H^1(Q_p,E); no local completion is replaced by
an algebraic tensor with Q_p. The downward maps in (5) agree with
reduction on the left and multiplication by p on the right. Taking
inverse limits identifies the completed local group with T_pL_p, and
localization commutes with (4)--(5) at every depth. Local coefficient
injectivity also identifies the finite strict subgroup with D_0[p^n].

For any homomorphism of p-primary groups D -> L_p with kernel D_0,
the kernel of T_pD -> T_pL_p is T_pD_0: a compatible sequence is in
the kernel exactly when every coordinate lies in D_0. Tensoring this
left-exact sequence with the flat Z_p-module Q_p preserves its kernel.
This proves all of (1), without integral right exactness.

**Ranks and finite images.** The finite generation in L026's proof
gives D^vee finitely generated over Z_p, of rank two. The structure
theorem and Pontryagin duality give, noncanonically,
D=(Q_p/Z_p)^2 direct-sum F for a finite p-group F. Likewise D_0 is
cofinitely generated: its dual is a quotient of D^vee. For any such
group G=(Q_p/Z_p)^d direct-sum F_G, T_pG has rank d. Indeed the
Tate module of Q_p/Z_p is Z_p, and a compatible sequence in finite
F_G of exponent p^e has coordinate x_n=p^e x_(n+e)=0. Thus finite
parts contribute zero, without being assumed absent.

L005's local structure identifies E(Q_p)'s open formal subgroup with
p Z_p, of finite index. The non-anomalous hypothesis makes its reduction
quotient prime to p. On tensoring with Q_p/Z_p the finite prime-to-p
kernel/cokernel vanish, so L_p is isomorphic to Q_p/Z_p. Alternatively
the same conclusion follows from (5) and that local structure. Therefore
T_pL_p has rank one. Kim gives rank_Z_p T_pD_0=k. Rank-nullity in
(1) now yields (2), including k>=1 and k<=2.

In the exact sequence 0 -> D_0 -> D -> I -> 0, Pontryagin duality
and flat rationalization give corank I=2-k. A subgroup of Q_p/Z_p
is either finite cyclic or the whole group: if its orders are
unbounded, it contains the unique subgroup of order p^n for every n.
Consequently k=1 gives I=L_p, whereas k=2 gives finite I. This also
proves that the two alternatives are exhaustive. In the first case
T_p f is a rank-one map from a finitely generated module to Z_p;
its nonzero image is p^e Z_p for some e>=0, so its cokernel is finite.
We do not infer its integral surjectivity from f's discrete surjectivity.
In the second case T_p I=0 even if I is nonzero. Equation (3) is the
unchanged source identification of this image with the relaxed
singular-localization cokernel dual.

Finally, k is defined as the minimum prime count of a nonzero whole
component. Since k cannot be zero under these hypotheses, k=1 is
equivalent to existence of kappa_ell!=0 at a one-prime index. This
does not assert nonzero singular localization of that component, and
does not replace the whole-system index by a residual Kurihara index.
In particular L026's ordinary augmentation semisimplicity has not
selected k=1. The strict line in that branch remains a Selmer line;
L005 still requires rational Kummer membership for its rank threshold.

**Scope and review.** The bounded continuation test succeeds as a
known-source specialization: coefficient matching, both branches and
finite images are preserved. The separate critical audit below passes on the unchanged
hypotheses and conclusions. It is neither a BSD candidate nor progress beyond the
checked source package. General fine-Selmer integral comparisons, such
as [Wuthrich, Lemma 3.1, author p. 6](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/fine.selmer.pdf#page=6),
permit finite errors; no general integral equality is claimed here.
The stronger global/local torsion hypotheses above are exactly what
justify the explicit coefficient equalities used for this application.
Fine control and height theorems are not used to choose a branch.


**Critical audit (2026-10-14).** No failed implication or additional
arithmetic premise was found. The following checks make the coefficient
naturality and the identification with the source's strict group explicit.
They verify the existing specialization, rather than strengthening it.

Write i_n:E[p^n] -> A for inclusion, u_n:E[p^n] -> E[p^(n+1)]
for upward inclusion, and d_n:E[p^(n+1)] -> E[p^n] for multiplication
by p. Then

\[
i_{n+1}u_n=i_n,\qquad i_n d_n=p i_{n+1}.
\tag{6}
\]

Thus (4) carries upward maps to inclusions D[p^n] -> D[p^(n+1)],
and downward maps to multiplication by p. To check the point maps
independently, for a field K of characteristic zero and P in E(K),
choose Q with p^n Q=P. The cocycle sigma -> sigma(Q)-Q represents
its finite Kummer image. The same Q is a p^(n+1)-division point of
pP, so u_n carries the Kummer image of P to that of pP. Conversely,
if p^(n+1)Q=P, then pQ is a p^n-division point of P, and d_n sends
the Kummer cocycle at depth n+1 to the one at depth n. Hence the
upward point map is [P] -> [pP], while the downward point map is
[P] -> [P]. Both statements hold at every completion and globally.
In particular, downward coefficient multiplication is not multiplication
by p on the point quotient.

For clarity, at any place v let h_n and h_infinity be the maps from
H^1(Q_v,E[p^n]) and H^1(Q_v,A) respectively to H^1(Q_v,E).
They satisfy h_n=h_infinity composed with H^1(i_n). Their kernels
are exactly the finite and infinite Kummer images, respectively.
Consequently the preimage of the infinite Kummer image under H^1(i_n)
is the finite Kummer image, even when H^1(i_n) is not injective locally.
This proves both directions of the local-condition assertion used in
(4), including at bad primes. At infinity, restriction/corestriction
kills positive-degree cohomology by two, while these coefficient groups
are p-primary with p odd, so the condition contributes nothing.
Global H^0(Q,A)=0 supplies the global injectivity needed in (4).

At p, the additional H^0(Q_p,A)=0 makes H^1(i_n) an isomorphism
onto H^1(Q_p,A)[p^n]. Restricting its inverse to L_p[p^n] is legitimate
by the preceding preimage argument and proves (5). It also proves the
stronger zero-condition matching: a finite localization maps to zero
in H^1(Q_p,A) if and only if it was already zero. Therefore the
finite p-strict subgroup corresponds exactly to D_0[p^n]. Equation
(6) shows that the direct limit of these subgroups is D_0, since every
element of D_0 has finite p-power order. This identifies the discrete
strict group in Kim's theorem with the D_0 used here, as well as
identifying the inverse-limit kernel. Away from p, the condition remains
classical; it has not been changed to the all-place zero condition.

The source applicability check uses Sections 2.1.5--2.1.6 for the
self-dual classical and dual canonical conditions; Theorem 2.1 and
Section 2.4.1 for the construction and residual hypotheses; Definition
2.12/Theorem 2.13(5) for the whole-system index; and Proposition 3.13
for collection nonvanishing. Equation (5.1) and both complete positive-
corank cases in Sections 5.3.2--5.3.4 agree with (3). No primitivity
or componentwise scalar equivalence is added. The primary version and
precise citations are those already given above. These source statements
are imported, not independently reproved.

There is no hidden tensor exactness in the local dimension computation.
For U=E_1(Q_p), the finite quotient E(Q_p)/U has order d=#E(F_p),
prime to p. Inclusion U -> E(Q_p) and [d]:E(Q_p) -> U have both
composites [d]. After tensoring with Q_p/Z_p, multiplication by d is
invertible, so inclusion becomes an isomorphism. Since U is isomorphic
to p Z_p, its tensor is Q_p/Z_p. The infinite Kummer map is injective,
which proves the asserted structure of L_p.

Finally the strict Tate-module kernel is obtained coordinatewise, before
flat rationalization. The structure theorem then gives ranks two and k,
so the map has rank 2-k independently of any right-exactness claim.
Discrete image corank is computed separately by exact Pontryagin duality.
Thus a corank-one image must equal L_p, whereas a corank-zero image is
finite cyclic and can be nonzero. In the latter case its Tate module
vanishes because bounded exponent kills every compatible coordinate.
In the former, the rationalized map is onto and the integral cokernel
is finite; integral surjectivity has not been proved or used. No step
kills F or the possible divisible Sha contribution. The one-prime
existence criterion follows from the already established k in {1,2};
it supplies no witness and uses no assumption that lambda_p is nonzero.

## Mathlib

The full specialization and the imported Kim structure and reciprocity
theorems: not checked. Supporting long-exact-cohomology, filtered-colimit,
Pontryagin-duality, Tate-module and rank-nullity coverage: not checked.
The elementary matching is proved above; unknown library coverage is
not evidence of absence.
