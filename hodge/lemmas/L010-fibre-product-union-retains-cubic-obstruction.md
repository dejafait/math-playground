# L010 — Adding a smooth fibre product retains the cubic support's obstruction

## Hypotheses

Let S, C, X = S x S, V_N, V_RM, and V_D satisfy L008. Use the elliptic fibration pi:S -> P^1 and the smooth fibre E = F_+ from L009. Explicitly, choose v_+ with v_+^2 = a/zeta and put t_+ = (1+zeta)v_+, so E = pi^{-1}(t_+). Retain the very-general hypotheses of those lemmas. Set

\[
B=E\times E,\qquad D=\Delta_E\subset B,\qquad Y=C\cup B,
\]

where Y is the reduced scheme-theoretic union. Work over A = C[epsilon]/(epsilon^2), in X_A = S_A x_A S_A for an NS-fixed first-order deformation S_A. Let

\[
N_Y=\mathcal Hom(I_Y/I_Y^2,O_Y),\qquad
\operatorname{ob}_Y(\kappa)=H^1(\delta_Y)(\kappa_X|_Y),
\quad \delta_Y(v)(f)=v(f)\bmod I_Y.
\]

The ideal-gluing criterion proved in L007 applies to Y: this class vanishes exactly when Y has a flat embedded first-order lift in X_A. No lci hypothesis on all of Y is imposed.

## Conclusion

Every flat embedded lift Y_A contains a flat embedded deformation B_A' of B. The residual ideal I_{Y_A}:I_{B_A'} defines a flat embedded lift of C. Consequently

\[
\ker(\operatorname{ob}_Y|_{V_N})=V_D,\qquad
\dim\ker(\operatorname{ob}_Y|_{V_{\rm RM}})=3,\qquad
\operatorname{rank}(\operatorname{ob}_Y|_{V_{\rm RM}})=1.
\]

Thus this added fibre product does not remove the fourth RM direction's obstruction. Its cycle class acts as zero on T(S), so [Y] still acts as the cubic generator U. The result concerns this particular reduced representative, not every cycle with that action or nonreduced replacements. No additional surface is shown to attain the required 21-dimensional rational Hodge span, and the universal target remains unresolved.

## Proof

**The intersection and the local smoothing.** The finite-chart parametrization of C is

\[
t=v+a/v,\qquad t'=\zeta v+\zeta^{-1}a/v,
\]

with identical elliptic coordinates in both factors. Requiring t=t'=t_+ selects exactly v=v_+. Both derivatives there are nonzero, with dt'/dt=-1. As checked in L009, the local branch of C is the graph of an involution fixing E pointwise. The entire intersection C intersect B is the reduced diagonal D, including the zero-section point; B is disjoint from the three singularities of C over infinity.

Near any point of D use the local involution coordinates of L009: f(u,w)=(-u,w), where E is u=0. In the product put

\[
r=u_2-u_1,\qquad s=u_2+u_1,\qquad z=w_2-w_1,\qquad w=w_1.
\]

Then

\[
I_C=(s,z),\quad I_B=(s,r),\quad I_D=(s,r,z),\quad
I_Y=(s,rz).
\tag{1}
\]

The intersection-ideal equality follows by reducing modulo s: (r) intersect (z) = (rz) in the regular ring with coordinates r,z,w. In particular Y is lci along D and has a local smoothing rz=epsilon. Local existence of this smoothing does not establish its global compatibility.

**A reference lift of B exists in every NS-fixed direction.** The fibre line bundle O_S(F) extends to S_A because its first-order obstruction is contraction of kappa with c_1(F), which vanishes for kappa in V_N. Its extension is unique since H^1(S,O_S)=0. The fibre pencil has h^0(O_S(F))=2, h^2(O_S(F))=0, and chi(O_S(F))=2 by K3 Riemann–Roch, so h^1(O_S(F))=0. Hence its two sections lift and still generate the line bundle, by Nakayama. They define pi_A:S_A -> P^1_A. This is also the pencil-lifting argument used in L008.

Choose a section t_{+,A} of the base reducing to t_+. The fibre E_A = pi_A^{-1}(t_{+,A}) is smooth over A, since the central fibration is smooth along E. Thus

\[
B_A^0=E_A\times_A E_A\subset X_A
\]

is a flat embedded reference lift. Existence here is explicit; no vanishing of H^1(B,N_{B/X}) is assumed.

**Any lifted B branch has at most a simple normal pole.** Suppose Y_A is a flat embedded lift. On the open complement of C, it is a lift of B minus D. Compare this lift with B_A^0 on that open set. The difference of two embedded first-order lifts in the same ambient deformation is intrinsically a section of the central normal sheaf, by the ideal parametrization in L007. We obtain

\[
\sigma\in H^0(B\setminus D,N_{B/X}).
\]

Lift the central coordinates (1) locally so that the reference B_A^0 has equations s=r=0. A flat lift of the lci ideal (s,rz) has generators

\[
s-\epsilon\alpha,\qquad rz-\epsilon\beta,
\tag{2}
\]

where alpha and beta are central functions modulo I_Y, with arbitrary local lifts to the ambient ring. On B minus D the coordinate z is invertible. Restricting their central values to B gives the two normal components of sigma, in the s,r frame, as

\[
\alpha_B,\qquad \beta_B/z.
\tag{3}
\]

Since z cuts out D on B with multiplicity one, these components have at most simple poles along D. Changes of normal frame are regular, so this is the invariant statement

\[
\sigma\in H^0(B,N_{B/X}(D)).
\tag{4}
\]

There is no need to select or normalize a B branch along D to obtain (4): the branch is selected only on B minus D, and (2) controls the extension of its normal displacement.

**An elliptic product has no such nonzero principal parts.** The normal bundle of a smooth fibre in S is trivial. Therefore

\[
N_{B/X}=\operatorname{pr}_1^*N_{E/S}\oplus
\operatorname{pr}_2^*N_{E/S}\simeq O_B^{\oplus2}.
\]

Give E its elliptic group law using the zero section, and let d:B -> E send (p,q) to q-p. The automorphism (p,q) -> (p,q-p) identifies d with the second projection and D with E x {0}. It follows that

\[
H^0(B,O_B(D))=H^0(E,O_E(0)).
\]

On a smooth genus-one curve, Riemann–Roch and Serre duality give h^0(O_E(0))=1: the canonical bundle is trivial and O_E(-0) has negative degree, hence no nonzero section. A supporting precise reference is [Stacks Project, Lemma 53.5.2, Riemann–Roch, tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6). The inclusion O_B into O_B(D) is consequently an isomorphism on global sections. Interpreting these sections as meromorphic functions, only constants occur; the one-dimensional space does not supply a function with a genuine simple pole.

Thus the natural inclusion gives

\[
H^0(B,N_{B/X})=H^0(B,N_{B/X}(D))\simeq\mathbb C^2.
\tag{5}
\]

By (4)–(5), sigma is regular on all of B. In (3), beta_B is therefore divisible by z, so its restriction to D vanishes. This is precisely the vanishing of the local node-smoothing residue. The argument concerns simple poles only; it does not assert the same conclusion for higher allowed pole orders or for a nonreduced central component.

**The extended branch is contained in Y_A.** Use the global normal section sigma to modify B_A^0. The ideal parametrization from L007 glues these local modifications and produces a flat embedded lift B_A' of B, agreeing with the selected branch on B minus D. More concretely, the two constant sections in (5) move the two fibres independently in the lifted pencil; B_A' can be taken as pi_A^{-1}(t_{1,A}) x_A pi_A^{-1}(t_{2,A}) for suitable first-order base sections. This does not assert that both factors use the same moving fibre.

The restriction of any local function in I_{Y_A} to O_{B_A'} has zero reduction, because B is contained in Y. By A-flatness, such a restriction is epsilon times a regular function on B. It vanishes on B minus D, where the two lifts agree, and hence vanishes everywhere because B is integral and this open set is dense. We have proved the scheme-theoretic containment

\[
B_A'\subset Y_A.
\tag{6}
\]

**The residual ideal is flat everywhere.** Near D choose ambient coordinates flattening B_A', so its ideal is (s,r) and the central ideals are still (1). Containment (6) says that the central correction terms alpha and beta in (2) vanish on B. In O_Y their classes are thus multiples of r. After absorbing multiples of s into the generators, the ideal takes the form

\[
J_A=(s-\epsilon r a_0,\ r(z-\epsilon b_0)).
\]

Its colon by I_{B_A'} is

\[
J_A:(s,r)=(s-\epsilon r a_0,\ z-\epsilon b_0).
\tag{7}
\]

Indeed, quotient by s-epsilon r a_0. The resulting ring is A[[r,z,w]], the image of (s,r) is (r), and multiplication by r is injective. The colon of (r(z-epsilon b_0)) by (r) is therefore (z-epsilon b_0). Taking its inverse image proves (7). The residual equations have independent central differentials ds,dz, so they define an A-flat deformation of the smooth C branch. This formal calculation also proves the assertion for the analytic local rings by faithful flatness of completion.

Away from B, the colon is I_{Y_A}, already a flat lift of C. Away from C, the ideals of Y_A and B_A' agree and the residual is empty. Along D, (7) gives flatness. These cases cover X, including all three singular points of C, since B avoids them. Thus the global colon ideal defines a flat embedded C_A. No simultaneous normalization of Y_A or unproved flatness of a residual at a singular intersection is used. Proper GAGA over A transfers the coherent ideals constructed with local analytic coordinates to algebraic ones.

L008 now implies kappa in V_D for every NS-fixed kappa admitting Y_A. This proves the kernel containment in V_D.

**The reverse inclusion and the threshold comparison.** Vary the Dickson parameters in the small neighbourhood from L008. Choose the root v_+ and the corresponding smooth fibre E holomorphically there. The family C is flat by L008, B is a smooth family of fibre products, and their intersection is exactly the smooth family D of diagonal elliptic curves. The coordinates (1) work relatively along D; there are no additional intersections over infinity. The exact sequence for the relative scheme-theoretic union,

\[
0\longrightarrow O_Y\longrightarrow O_C\oplus O_B
\longrightarrow O_D\longrightarrow0,
\]

shows O_Y is flat over the parameters because both the middle and right terms are flat. It also remains exact after base change, identifying every fibre with the specified union. Therefore every direction of V_D supplies a flat Y lift. Combined with the previous containment, this proves the kernel equality. L008 supplies dim V_D=3 and dim V_RM=4, giving rank one on V_RM.

Finally [B]=[F] tensor [F] lies in the divisor-product span. Its correspondence action on w in T(S) is q(w,F)[F]=0. L006 and L007 identify the reduced support C's action with U, so Y has the same action. An extension of Y could therefore have supplied the missing generator, but this representative's kernel is only three-dimensional against the required four. The calculation stops this reduced fibre-product addition; it does not obstruct all algebraic representatives of the Hodge class.

## Mathlib

Coverage of the full statement: **not checked**. No Mathlib match or absence is claimed. The directly linked [Stacks Project Riemann–Roch theorem, tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6), supports the one-dimensional section calculation on E; it is not a match for this union's obstruction statement or a Mathlib reference. K3 Riemann–Roch, the line-bundle obstruction, the first-order ideal parametrization, and proper GAGA are supporting standard inputs. The normal-pole bound, forced component, flat residual, and both kernel inclusions are proved above.
