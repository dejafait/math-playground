# L075 — Changed-sign rank-two transform duality excludes two survivors

## Hypotheses

Retain L071's marked smooth projective complex K3 surface S, the real
Kähler class h and the identical hyperkähler metrics on X=S x S. Put
Omega=p_1^*h+p_2^*h, e_1=eta tensor 1 and e_2=1 tensor eta, with
integral_S eta=1. Use the full integral mixed class tau_D of L071,
including its divisor and transcendental components, at this same metric.

Let b=-11 or b=-13, and suppose F is a locally free rank-two
holomorphic bundle on X, slope-polystable at Omega, with

\[
c_1(F)=0\ \text{in }H^2(X,\mathbf Z),\qquad
\operatorname{ch}_2(F)=-6e_1+(b+4)e_2-\tau_D.
\tag{1}
\]

Initial higher characters and the initial K-class are unrestricted.
Use the audited L073 and L074 conclusions for the actual bundle
G=R^1p_2*F. No F existence, opposite-fibre stability, transform
equivalence, reconstruction, gluing or transport is assumed. Both
integers satisfy L071's admitted a=-10 domain: b<=-9 and
-6(b+4)=42 or 54 is 6 modulo 12.

## Conclusion

No F satisfying these hypotheses exists. The actual rank-two G would
carry a perfect symmetric O_S-valued holomorphic pairing by determinant
wedge and relative Serre duality. L074 forces this G to be stable with
trivial determinant; simplicity then contradicts that pairing.

This is a REPRODUCTION/specialization of the previously assessed duality
and simplicity tools. It excludes only the specified conditional kernels
at b=-11,-13. The cases b=-9,-17, other charges or representatives,
transverse transport, and universal primitive rational Hodge-class
algebraicity are outside this conclusion. No cycle or bundle existence
is supplied. The separate critical audit of 2026-10-08 below preserves
this specialization without a substantive repair or stronger exclusion.

## Proof

**Obtain the actual bundle before duality.** Apply L073 to (1). For
pi=p_2 it gives an actual locally free rank-two G, compatible with
base change, slope-polystable of slope zero at the unchanged real h,
and Rpi_*F=G[-1]. On every closed fibre S x {y}, with E_y its
restriction of F, the identification is

\[
G_y=H^1(S,E_y),\qquad H^0(S,E_y)=H^2(S,E_y)=0.
\tag{2}
\]

These are the audited all-fibre conclusions, not deductions from a
virtual rank or generic-fibre vanishing. L074 gives integral c_1(G)=0,
det(G)=O_S and c_2(G)=(b+17)eta, hence charge six or four.
Its complete exact-h split alternative has charge 14r^2, r in Z;
neither six nor four is such a value. Therefore G is slope-stable
at this same h. No stability of the opposite-factor restrictions is
used, and the character filter is not recomputed.

**Trivialize the coefficient lines.** K3 coherent cohomology and
coherent Künneth give H^1(X,O_X)=0. The exponential exact sequence
makes Pic(X)->H^2(X,Z) injective; (1) therefore implies det(F)=O_X.
This uses the integral first class, not slope zero. Fix a holomorphic
trivialization det(F)->O_X. The determinant wedge gives a perfect
alternating holomorphic bilinear form

\[
A:F\otimes F\longrightarrow O_X,
\qquad A(u,v)=-A(v,u).
\tag{3}
\]

Choose a nonzero holomorphic two-form sigma_1 on the FIRST K3. It
is nowhere zero and trivializes omega_{X/S}=p_1^*K_S for pi=p_2.
Multiplication by p_1^*sigma_1 identifies O_X with omega_{X/S}.
Thus the canonical relative Serre trace defines the specific map

\[
t:R^2\pi_*O_X
 \xrightarrow{\ \sigma_1\ }R^2\pi_*\omega_{X/S}
 \xrightarrow{\ \operatorname{Tr}_\pi\ }O_S.
\tag{4}
\]

It is an isomorphism: on each fibre it is the nonzero Serre-trace
functional on the one-dimensional H^2(S,O_S), after the chosen
canonical trivialization. Changing either chosen trivialization
rescales the forthcoming pairing by a nonzero scalar and cannot
change its symmetry or perfection. The exponential sequence and
canonical/Serre facts here are named standard inputs, also used in
L059; for K3 Picard injection see Huybrechts, *Lectures on K3
Surfaces*, author-hosted prepublication draft, Chapter 1 Section 3.2,
[equation (3.1), printed p. 15](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=15).

**Apply coefficient duality to this projection and retain its shift.**
Import [Stacks Section 48.19, (2),(9), Tag 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
with the supporting [Lemma 48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q)
and [Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT).
The projection pi is smooth projective of relative dimension two
over the Noetherian complex variety S. GAGA algebraizes F, a finite
locally free coherent sheaf. For the coefficient O_S the imported
proper coherent duality is

\[
R\pi_*(F^\vee\otimes\omega_{X/S})[2]
 \simeq R\mathcal Hom(R\pi_*F,O_S).
\tag{5}
\]

All complexes here meet the bounded coherent hypotheses. The form
A and sigma_1 identify F with F^vee tensor omega_{X/S}. By (2),
the left side of (5) is G[1] and the right side is G^vee[1].
The shift is therefore consistent with an actual self-duality of G.
The associated pairing is explicitly the holomorphic cup/wedge/trace
morphism

\[
Q:G\otimes G
 \xrightarrow{\ \cup\ }R^2\pi_*(F\otimes F)
 \xrightarrow{\ A\ }R^2\pi_*O_X
 \xrightarrow{\ t\ }O_S.
\tag{6}
\]

Its fibre at every y is the Serre pairing on H^1(S,E_y) with
itself under the perfect coefficient identification (3) and sigma_1.
Serre duality makes this pairing nondegenerate, even though A is
alternating. L073's base change ensures these are the fibres of
(6), not just abstract pairings on unrelated vector spaces. Hence
the bundle map Q^flat:G->G^vee is invertible at every closed point.
Its determinant has no zero: a nonempty closed degeneracy locus
on finite-type S would contain a closed complex point. Thus Q is
perfect everywhere. This is the cited duality's actual-image
specialization; no new duality theorem is reproved.

**Check both interchange signs.** The degree-one cohomology swap
has sign (-1)^(1*1)=-1 by [Stacks Section 15.59, Tag 0GWN](https://stacks.math.columbia.edu/tag/0GWN).
Coefficient wedge A has a second minus sign. Consequently (6) is
symmetric. In local Dolbeault representatives alpha=a tensor u and
beta=c tensor v, with u,v of degree (0,1), its trace integrand is

\[
A(a,c)\,u\wedge v\wedge\sigma_1.
\]

Interchanging alpha,beta negates both A(a,c) and u wedge v, giving
the same integrand. Linearity gives the same identity for arbitrary
representatives. The chosen two-form and trace do not alter this
swap. Therefore Q(u,v)=Q(v,u). Self-duality alone would not
determine this sign; the negative mixed class in (1) enters neither
of the two interchange rules.

**Compare with rank-two determinant wedge using simplicity.** The
integral determinant conclusion from L074 permits a chosen
trivialization det(G)->O_S. Its rank-two wedge form W:G tensor
G->O_S is perfect and alternating. Put
W^flat(u)(v)=W(u,v) and Q^flat(u)(v)=Q(u,v). The composite

\[
T=(W^\flat)^{-1}Q^\flat\in H^0(S,\mathcal End(G))
\tag{7}
\]

is a holomorphic automorphism. Import stable simplicity from
Huybrechts, *Lectures on K3 Surfaces*, author-hosted draft,
Chapter 9 Section 3.1(iii), [printed pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
The passage explicitly allows a complex K3 with a real Kähler class.
Its hypotheses fit the stable G at the unchanged h; no rational
polarization replacement is needed. Simplicity over C gives
T=c id_G for a scalar c, nonzero because T is invertible. Thus

\[
Q^\flat=cW^\flat,\qquad Q(u,v)=cW(u,v).
\tag{8}
\]

The right side is alternating, whereas Q is symmetric. Over C,
both identities imply Q(u,v)=-Q(u,v), hence Q=0, contradicting
perfection. This contradiction proves the stated nonexistence.

Only holomorphic duality and simplicity are needed; no connection
parallelness, real orthogonal reduction, projective lifting problem
or transform inverse is asserted. L059's rank-two comparison is a
known local precedent, not a changed-sign conclusion imported
without checking its coefficients and actual image. The older
rank-seven and rank-three compatible branches remain untouched.
The achieved threshold is exclusion of these two conditional F
cases, not algebraic realization or nonalgebraicity of a Hodge class.

**Separate critical audit, 2026-10-08.** The approved actual-map,
sign and simplicity audit finds no substantive mathematical error.
It is REPRODUCTION with outcome EXPLORATION: verifying the existing
exclusion supplies neither an additional excluded pair nor a new
mathematical result beyond the assessed tools.

The precise input category agrees with L071 and audited L073/L074.
For b=-11,-13 the products -6(b+4) are respectively 42,54, both
6 modulo 12; b<=-9 holds. L073 supplies the actual locally free G
and every-fibre concentration independently of the character filter.
L074 gives charges six and four, each incompatible with its complete
split alternative 14r^2. Consequently stability is established at
the original real h, not inferred from a virtual character or from
the stability of a generic restriction. Its integral determinant
conclusion precedes use of the wedge form W.

The coefficient trivializations in (3)--(5) are actual global ones.
Coherent Kunneth expresses H^1(X,O_X) as the sum of the two terms
containing H^1(S,O_S), both zero. The kernel of the first-Chern-class
map in the exponential sequence is therefore zero, so integral
c_1(F)=0 trivializes det(F). No nontrivial flat coefficient line is
left over. For p_2 the relative canonical line is p_1^*K_S; the
nonvanishing first-factor sigma_1, rather than a base form, is the
required identification. The Serre trace on H^2(K_S) is an
isomorphism by its duality with H^0(O_S)=C. Multiplication by
sigma_1 thus makes (4) nonzero on every fibre. Since X and S are
connected and projective, a change of either trivialization is a
nonzero constant; it cannot affect the sign or nondegeneracy.

One need not assume a base-change isomorphism for the intermediate
sheaf R^2 pi_*(F tensor F). The cup morphism is induced by the
natural derived morphism

\[
(R\pi_*F)\otimes^{\mathbf L}(R\pi_*F)
 \longrightarrow R\pi_*(F\otimes F)
 \longrightarrow R\pi_*\omega_{X/S}
 \longrightarrow O_S[-2].
\]

The second arrow uses A and sigma_1, and the last is the relative
trace. With Rpi_*F=G[-1], its degree-two morphism is precisely (6).
Cup is natural under restriction, and the proper smooth Serre trace
specializes to the fibre trace. The base-change identifications
from L073 therefore identify this map on each closed fibre with
the Serre cup pairing on H^1(E_y). The coefficient isomorphism
E_y -> E_y^vee tensor K_S makes that pairing perfect. Equivalently,
(5) has both sides in degree -1, namely G[1] and G^vee[1]; there
is no shift discrepancy. Thus Q^flat has nonzero determinant at
every closed point. A degeneracy locus is closed on finite-type S,
so the fibrewise check establishes perfection everywhere. This
verifies the application of the cited duality, without reproving it
or imposing extra base-change hypotheses on the intermediate sheaf.

For the symmetry test, coefficient degree is zero and Dolbeault
degree is one. Swapping two representatives negates determinant
wedge and negates their (0,1)-form wedge. The product sign is +1;
the even-degree sigma_1 introduces no additional swap sign. Hence
Q is symmetric as an actual holomorphic pairing, regardless of the
minus sign in the mixed Chern tensor. Finally the adopted convention
W^flat(u)(v)=W(u,v) gives exactly Q(u,v)=W(Tu,v) from (7).
Exact-real-h simplicity makes T=c id with c nonzero. This proves
Q=cW, an alternating form, contradicting symmetry and perfection
over C. Changing the coefficient-identification convention could
multiply Q by -1 but could not change this contradiction.

No connection parallelness, inverse transform, opposite-fibre
stability or kernel existence enters this verification. Its direct
mathematical inputs remain L071, L073 and L074; L059 is only a
comparison precedent. The claims for b=-9,-17 and the universal
primitive Hodge gap remain outside the audit. The earlier compatible
branches in ATTEMPTS/043/045 and the exhausted character filter in
ATTEMPTS/051 are preserved.

## Mathlib

Full matching coverage of this actual-image duality specialization and
exact-real-h rank-two exclusion: **not checked**. Unknown availability
is not evidence of absence. The precise Stacks proper-smooth duality
and graded-symmetry results and Huybrechts simplicity statement above
are imported. The determinant trivializations, both signs, fibrewise
perfectness and application to this G are the necessary specialization,
not reproofs of those general results. L071, audited L073 and audited
L074 supply the retained mathematical inputs. No originality or
complete Hodge-conjecture resolution is claimed.
