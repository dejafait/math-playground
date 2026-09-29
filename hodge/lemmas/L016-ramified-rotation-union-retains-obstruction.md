# L016 — The ordinary-square union also obstructs the prescribed ramified lift

## Hypotheses

Use the very-general cubic Dickson surface, rotations and open conditions of L014 and L015. In particular the Dickson parameter map has rank three in the marked deformation space, as required in L008. Put

\[
X=S\times S,\qquad
I_Y=I_{C^{(1)}}\cap I_{C^{(2)}}^2\cap I_{C^{(3)}},
\qquad C^{(1)}=C.
\]

The middle square is the ordinary square of the whole ideal, including at infinity. Set A_1=C[tau]/(tau^2) and A_2=C[tau]/(tau^3). Let S_(A_2) be an NS-fixed deformation with a specified identification S_(A_1)=S x Spec A_1. Denote its order-tau^2 Kodaira--Spencer class by kappa in V_N. Both factors of X_(A_2) have this same deformation. In the target application kappa belongs to V_RM outside V_D.

An allowed lift is any A_2-flat closed subscheme of X_(A_2) with special fibre Y. Its first-order motion in the fixed X is arbitrary. Neither its components nor its reduction nor a filtration of its nilpotents is required to lift.

## Conclusion

An allowed lift exists if and only if kappa belongs to V_D. Thus there is **no** such lift for a transverse RM coefficient at order tau^2, even after allowing every first-order motion of Y. The permitted coefficient space has dimension three, against the four-dimensional V_RM.

The extra input beyond L015 is global: on a general complete elliptic fibre the first-order multiplication on the squared sheet is forced to have only a vertical cubic term. Its quadratic trace defect therefore vanishes. This is not a multiplicativity theorem for trace on arbitrary cubic algebras.

This excludes the specified order-two ramified test for this representative. It does not exclude other representatives, other sheaves, or families whose first nonzero ambient term occurs at a higher order. L015's non-scalar cycle and the known 21-dimensional span on the Dickson family are unchanged. The rational Hodge conjecture remains unresolved.

## Proof

**Known deformation input and scope of the specialization.** Use the small-extension embedded deformation framework of [Buchweitz--Flenner, Lemmas 7.6--7.7, pp. 190--191](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56). In particular, once a local lift through A_2 -> A_1 exists, differences of lifts with that fixed reduction are parametrized by

\[
\operatorname{Hom}(I_Y,O_Y)\otimes(\tau^2).
\tag{1}
\]

Here tau annihilates the kernel, so only the special fibre occurs on the right. In generators this says that differences are tau^2 times their images in O_Y; flatness makes those images respect the central relations. Conversely the relations and flatness criterion give the corresponding ideal. This is the relative version of the ideal calculation in L007, not a replacement of the full obstruction theory by H^1 of a normal bundle.

The arbitrary-base cubic-algebra tables are known: [Poonen, Proposition 5.1 and its proof, corrected author version, PDF pp. 5--6](https://math.mit.edu/~poonen/papers/moduli.pdf#page=5), or [Wood, Theorem 2.1 and equation (1), pp. 1073--1074](https://msp.org/ant/2011/5-8/ant-v5-n8-p05-p.pdf#page=6). Their scalar terms can be quadratic in first-order parameters. The proof below specializes them to the multiplication permitted by this embedding and its complete fibres. Abstract algebra smoothness alone would not justify the conclusion.

**Each reduced rotation support is infinitesimally rigid in the fixed product.** We first extract a consequence of the proof of L008:

\[
H^0(C^{(j)},N_{C^{(j)}})=0\qquad (j=1,2,3).
\tag{2}
\]

Here is why the coefficient calculation proves rigidity, rather than only a constraint on ambient directions. Any embedded first-order lift of one support has the simultaneous normalization and two finite flat double-cover projections constructed there. For the j-th rotation the two deck involutions multiply to v -> zeta^(2j)v. Since 2j is invertible modulo seven, the same argument recovers the full dihedral action. The argument uses H^0(W,T_W)=0, proved in L008, so its group relations hold in every such lift.

After conjugating the base action and fixing its line-bundle linearization, all the lifted coefficients are exactly

\[
A_v=\alpha(v^{15}+v)+\beta v^8,
\qquad B_v=\gamma(v^{19}+v^5)+\delta v^{12}.
\tag{3}
\]

The quotient has the Dickson equation in the proof of L008; NS-fixedness retains the exceptional curve and its equisingular resolution. There are four coefficient tangents before the one-dimensional Weierstrass scaling. By the rank-three hypothesis their map to marked surface deformations has kernel exactly that scaling direction. If S itself is fixed, therefore, the coefficient motion can be removed by this scaling. The normalized cover and its dihedral action then become constant.

The identifications of its two quotients with the fixed S cannot introduce another infinitesimal motion. Any two such identifications reducing to the same central map differ by an infinitesimal automorphism of S. But H^0(S,T_S)=0: contraction with its nonvanishing holomorphic two-form identifies T_S with Omega^1_S, whose global sections vanish for a K3 surface. The corresponding statement for W was already used above. Thus the two projection maps, and hence the embedded image, are constant. L007's tangent-space description now gives (2). This uses the full lift classification in L008, not merely its equality of obstruction kernels.

**All three first-order centres are constant.** Suppose Y_(A_2) is a lift and restrict it to A_1. Its ambient deformation is constant. L015's mixed-residue argument applies to this arbitrary first-order motion. It kills every mixed residue and every reduced--reduced smoothing residue, and recovers lifts of both reduced components C^(1) and C^(3). The proof is symmetric in those two multiplicity-one components. By (2) these recovered lifts are constant.

We also require the centre of the squared component, including where the first projection ramifies. On the separated smooth part of C^(2), take any local tangential coordinates and two normal coordinates q,z. An arbitrary first-order lift of its ordinary ideal square has a free algebra with basis 1,q,z over the chosen tangential coordinates. Its products have no scalar first-order term, by L015's associativity calculation. If the six linear coefficients of q^2,qz,z^2 are a,b,c,d,e,f, its normalized traces are

\[
\frac{\operatorname{Tr}(q)}3=\tau(a+d)/3,
\qquad
\frac{\operatorname{Tr}(z)}3=\tau(c+f)/3.
\tag{4}
\]

They define a first-order normal displacement of the smooth reduced surface. This displacement is independent of the choice of tangential retraction. To check this, expand a coordinate change in the two normal variables. Its linear part acts by the normal transition matrix. The normalized trace of every quadratic normal product is zero over A_1, so all the higher normal terms contribute zero. If a tangential coordinate is changed by a normal term, Taylor expansion of a coefficient introduces another normal factor; in a first-order product its contribution is again zero. These calculations also allow a change of normal frame. Thus (4) transforms as a section of the normal bundle, and its local graph ideals glue. No global finite projection at its ramification fibres is being assumed here.

At each mixed crossing L015's notation gives the thickened centre displacements

\[
\delta q=\tfrac13(M(r)/r+E(r)),\qquad
\delta z=\tfrac13(C(r)+B_0(r)).
\tag{5}
\]

The residue M(0) vanishes by that lemma, so both displacements extend regularly across the curve. At infinity the normal sheaf of C^(2) has the same description as that of C in L008: it is the pushforward of the immersion normal bundle on W. Indeed the graph branches are f^2 and f^(-2); their tangent matrices still have invertible difference, and the same local normal-module computation applies. Hartogs therefore extends the displacement over the finitely many missing points. It gives a global first-order embedded lift of C^(2), so (2) makes it constant as well.

This constructs only the first-order centre from Y_(A_1). It does not claim that an arbitrary square thickening has a centre at higher order, or that the central nilpotent filtration has lifted.

**Complete fibres restrict the remaining first-order multiplication.** Work now over a small disk in a dense open of the first elliptic base, avoiding branch values, singular fibres, component intersections and infinity. The first projection of Y_(A_2) is finite: it is proper and its special fibre is finite. Its central idempotents lift, separating rank-one sheets of the reduced components and rank-three sheets of the squared component. Flatness and the local flatness criterion make these summands locally free of the stated ranks over the source S_(A_2). This is the argument in L015, valid over A_2 as well.

Fix a rank-three sheet and first restrict to A_1. Its centre is the constant graph, by the preceding paragraph. In local normal coordinates its most general first-order multiplication is consequently

\[
\begin{aligned}
q^2&=\tau(aq+bz),\\
qz&=\tau(cq-az),\\
z^2&=\tau(eq-cz).
\end{aligned}
\tag{6}
\]

The two trace-zero equations account for the minus signs. Let M be the conormal bundle of this graph, and N=M^vee. The multiplication in (6) gives a tensor

\[
\eta\in H^0(\operatorname{Sym}^3N\otimes\det(N)^{-1}).
\tag{7}
\]

For clarity this identification can be checked without an algebra classification. If m denotes the coefficient of tau in the multiplication, send a conormal vector u to u wedge m(u,u). For u=xq+yz this is

\[
\bigl(bx^3-3ax^2y-3cxy^2-ey^3\bigr)q\wedge z.
\tag{8}
\]

This is an isomorphism from trace-free symmetric multiplication tensors to Sym^3(M^vee) tensor det(M). The construction is invariant under linear changes of conormal coordinates. Nonlinear normal changes, or changes of tangential coordinates, only produce central products of two normals inside a tau correction, so do not change this first-order tensor. Hence it is defined over the whole source above the chosen disk, not just over individual fibre charts.

The central graph map is a local isomorphism of the elliptic surfaces, so N is the pullback of T_S from the target. On a general complete smooth fibre E it fits in

\[
0\longrightarrow T_E\simeq O_E
\longrightarrow N|_E
\longrightarrow O_E\longrightarrow0.
\tag{9}
\]

The extension is non-split. Its class is the Kodaira--Spencer class of that fibre in the elliptic fibration. A split sequence would make the first-order fibre deformation trivial, forcing the derivative of its j-invariant to vanish. We have chosen a general base value where that derivative is nonzero. Such values form a dense open because the given J_0=R composed with P_a is nonconstant. Also det(N)|_E is trivial; it is the restriction of the determinant of the tangent bundle of a K3 surface.

For this non-split extension, the global sections of Sym^3(N|_E) are precisely the cubes of the vertical subline. Here is the needed elementary check. Choose a global generator v of that subline and local lifts h_i of a generator of the quotient. Their transitions have h_j=h_i+c_ij v, with a nonzero class [c_ij] in H^1(E,O_E). Write a putative section as a polynomial of degree three in v,h_i. If its largest nonzero horizontal exponent is k>0, its leading coefficients glue to a nonzero constant because E is complete. Comparing the coefficient with exponent k-1 would express k times that constant times c_ij as a coboundary of functions. This is impossible in characteristic zero. Only the vertical cube remains. Tensoring with the trivial determinant line does not alter the conclusion.

In (8), q is the horizontal conormal coordinate and z the vertical one. The cube of the vertical tangent is the y^3 term. Thus a=b=c=0 on every such fibre. The coefficients are holomorphic on the separated sheet, so density gives

\[
q^2=qz=0,\qquad z^2=\tau\beta q
\quad\pmod{\tau^2}
\tag{10}
\]

on every separated chart under discussion. The scalar beta need not vanish. This step uses complete fibres and non-isotriviality. Pointwise algebra alone permits all four coefficients in (6).

**Trace is multiplicative for every continuation of (10) to A_2.** Over a source coordinate chart, write its actual rank-three algebra as

\[
\begin{aligned}
q^2&=\tau^2(A_0+A_1q+A_2z),\\
qz&=\tau^2(B_0+B_1q+B_2z),\\
z^2&=\tau\beta q+\tau^2(D_0+D_1q+D_2z).
\end{aligned}
\tag{11}
\]

Here the subscripts on the coefficients are unrelated to the Artinian rings. Coefficients are functions on the central source chart, lifted to its deformation. Any order-tau^2 change of beta is absorbed into D_1. This is the specialization of the known cubic-algebra tables that is needed here.

Associativity (q^2)z=q(qz), compared at order tau^2 in the free basis 1,q,z, gives A_0=B_0=0. Next (qz)z=q(z^2) gives D_0=0: the term tau*beta*q^2 is already zero modulo tau^3. Thus

\[
\operatorname{Tr}(q)=\tau^2(A_1+B_2),\qquad
\operatorname{Tr}(z)=\tau^2(B_1+D_2),
\tag{12}
\]

and the traces of q^2,qz,z^2 all vanish. The last assertion uses tau*beta*Tr(q)=0. Products of the two normalized traces also vanish. Multiplicativity follows on the basis pairs and hence on the whole algebra. Its unit has trace three, so Tr/3 is a unital algebra homomorphism.

Since trace is intrinsic for a finite locally free algebra over the fixed first projection, these local homomorphisms glue on the entire separated sheet over the base disk. They give actual graph sections whose first-order reductions are the constant graph. This conclusion was proved using (10); it is false for unrestricted first-order cubic multiplication parameters.

**The graph sections preserve the fibre j-invariant through order two.** The NS-fixed elliptic pencil and zero section extend to S_(A_2). One can either repeat L008's line-bundle argument or base change its first-order construction by epsilon -> tau^2: a smooth deformation trivialized modulo tau^2 has local gluing maps with only an order-tau^2 term. Choose its base trivialization compatibly and write

\[
J_{A_2}(t)=J_0(t)+\tau^2 dJ(t),\qquad
a_{e,k}=dJ(p_{e,k}).
\tag{13}
\]

Every rank-one sheet, and every trace section just constructed, is a map defined on the whole source elliptic surface above a disk. Its second base coordinate is constant on complete fibres. Over A_2 this follows inductively from the corresponding assertion on S: subtract a lifted base function at each power of tau. Its fibre map is an isomorphism, since it reduces to an isomorphism between smooth proper elliptic curves; finiteness and the rank-one unit-map argument prove this over the Artinian base. The usual short-Weierstrass change of coordinates then preserves j, just as in L014 and L015. Therefore each of these graph maps satisfies

\[
J_{A_2}(t)=J_{A_2}(s).
\tag{14}
\]

The graph maps have zero first-order displacement. Equation (14) is not being asserted on the entire nonreduced Y_(A_2).

**The mixed crossings have a flat reference lift retaining both centres.** Use L015's full local normal-module parametrization at a mixed crossing, with central ideal

\[
I=(z^2,zq,rq^2),\qquad r=Q_i(t,s),\quad q=Q_2(t,s).
\tag{15}
\]

Let w be a local coordinate on the common elliptic fibre, taken from the first factor. In the notation of that parametrization, constancy of the reduced first-order centre forces M(0)=0, N(q)=0, C(0)=0 and D(q)=0. Constancy of the thickened centre forces M=-rE and B_0=-C. Away from r=0, the products on the thickened sheet are therefore

\[
q^2=\tau(-Eq+(P/r)z),\quad
qz=\tau(Cq+Ez),\quad
z^2=\tau(rAq-Cz).
\]

Condition (10), first valid on a dense open, gives E=P=C=0. These functions are regular in r,w, so the equalities hold across r=0 as well. Thus the actual first-order ideal at the crossing is

\[
(z^2-\tau rq A(r,w),\ zq,\ rq^2)\pmod{\tau^2}.
\tag{16}
\]

Use exactly the same generators as a reference ideal over A_2. It is flat. Indeed set

\[
J_T=(q^2,qz,z^2-\tau rq A),\qquad J_R=(r,z).
\]

The quotient by J_T is free with basis 1,q,z over C[[r,w]] tensor A_2, with products q^2=qz=0 and z^2=tau*r*A*q. Its multiplication is associative and the displayed presentation has that basis. The quotient by J_R is flat. Their sum is (r,z,q^2), whose quotient is also flat and independent of tau. Finally J_T intersect J_R is exactly (16), because reducing a multiple of q^2 modulo (r,z) forces its coefficient into (r,z); the zq^2 term is already generated by zq. The exact sequence for this intersection, with flat component and intersection quotients, proves flatness of the union quotient.

This reference contains the constant reduced branch and has a constant trace section on the thickened branch. Over the first projection r is a function of t,q; replacing rA(r,w) by its value at q=0 changes its product with q by a multiple of q^2, which is zero in the reference. Thus the same statement holds using the required first projection, rather than an auxiliary projection to r,w.

By (1), any actual A_2 lift with reduction (16) differs from this reference by tau^2 times an arbitrary homomorphism in L015's parametrization. Denote its coefficients again by A,B_0,C,D,E,M,N,P. The old first-order nilpotent parameter in (16) is held fixed and is not one of these differences. Products of that tau term with these tau^2 differences vanish. Consequently the order-two displacements of the isolated reduced sheet and thickened trace section are exactly

\[
\begin{array}{ll}
\text{reduced sheet:}&
\delta r=M(0)/q+N(q),\quad \delta z=C(0)+qD(q),\\[2mm]
\text{trace section:}&
\delta q=\tfrac13(M(r)/r+E(r)),\quad
\delta z=\tfrac13(C(r)+B_0(r)).
\end{array}
\tag{17}
\]

In particular the two possible base-normal residues are mu=M(0) and mu/3. This computes the difference for every lift, rather than setting its remaining nilpotent parameters to zero.

**The order-two residues vanish.** Near any mixed ordered critical pair the same central factorization as in L015 gives

\[
J_0(t)-J_0(s)=H(t,s)rq,\qquad H_D\ne0.
\tag{18}
\]

Use (14) on each graph away from the crossing, substitute (17), and take its order-tau^2 coefficient. There are no quadratic terms from a first-order graph displacement, since those displacements are zero. After restricting to the double curve the two equations are

\[
d+H_D\mu=0,\qquad d+H_D\mu/3=0,
\quad d=a_{e,k}-a_{e,l}.
\tag{19}
\]

The pole bounds in (17) make these restrictions legitimate: multiplying by q or r removes the only possible pole. Hence mu=d=0 at every mixed curve. These curves represent the pairs {1,3} and {2,3} for each sign e, and therefore

\[
a_{e,1}=a_{e,2}=a_{e,3}.
\tag{20}
\]

At a reduced--reduced crossing the first-order ideal is constant. To see this directly, its central ideal is (z,rq). The two recovered component motions are zero, so the images of both generators in its first-order ideal homomorphism vanish on the dense open of each component. The central union is reduced, hence both images are zero. Differences of order-two lifts are consequently just tau^2 times the familiar normal-module calculation for (z,rq). Equation (14) holds on the isolated sheets. Its difference vanishes modulo tau^2 and its remaining coefficient is a function on this reduced central union, so it vanishes throughout. Equation (20) then kills its smoothing residue at the crossing, exactly as in L014. No restriction to the reduction of the squared component is used in this argument.

**Recover C and retain all points at infinity.** Away from the other components Y_(A_2) already supplies the reduced C sheet. At a mixed crossing on C, mu=0 makes both reduced displacements in (17) regular. Together with the constant first-order branch they give a smooth flat C lift there. At a reduced--reduced crossing, the zero smoothing residue factors its two branch equations to order tau^2, again recovering C. These local lifts agree on their dense smooth overlaps. Their differences lie in tau^2 times the ordinary normal bundle and are zero on a dense open, so they glue.

We have obtained an embedded lift of C off the three infinity points, constant modulo tau^2. Choose local trivializations of the ambient deformation compatible with its specified first-order trivialization. Near an omitted point the punctured C lift is then tau^2 times a section of N_C. The identification N_C=nu_*N_j in L008 and Hartogs on the smooth surface W extend that section uniquely. L007's ideal description, applied to the square-zero coefficient tau^2, gives a flat local lift of C. Uniqueness makes all these extensions glue. Analytic constructions can be algebraized by proper GAGA over A_2.

This extension uses the normal sheaf of the recovered **reduced** C. It imposes no flatness on a residual ideal of Y and does not replace its full ideal at infinity

\[
(J_1\cap J_{-1})\cap(J_2\cap J_{-2})^2
\cap(J_3\cap J_{-3})
\]

by separate branch squares. Any extra local first-order motions of that ideal cannot avoid the necessary recovery just proved on the punctured neighbourhood.

Since the recovered C lift and the ambient deformation are both constant modulo tau^2, their ideal gluing equations at order tau^2 are precisely the first-order gluing equations of L007 with epsilon substituted by tau^2. Thus ob_C(kappa)=0. Equivalently their local equations descend to the first-order deformation with class kappa. L008 gives kappa in V_D, proving necessity for every allowed first-order motion.

**Sufficiency and threshold.** If kappa belongs to V_D, L015 supplies the flat family of the whole ordinary-square union, including its complete ideal at infinity. Pull its first-order deformation back along epsilon -> tau^2. Flatness is preserved by base change, and the resulting lift has the required ambient coefficient and is constant modulo tau^2. This proves sufficiency. The dimensions three and four are those of L008. No claim about higher ramification orders follows from this calculation.

The supporting exact-arithmetic command

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/cubic-deformation/check_ramified_trace.py

checks the order-two associativity constraints, multiplicativity of trace in (11), the trace-free cubic tensor in (8), and the mixed-residue constraint rank. It also exhibits a general cubic-algebra trace defect, confirming why the fibre restriction is essential. These algebra checks do not verify global rigidity, coordinate gluing, complete-fibre arguments or Hartogs extension; their informal proofs are given above.

## Mathlib

Coverage of the full statement: **not checked**. No Mathlib match or absence is asserted. The [prior SPECIALIZE assessment](../drafts/literature/2026-09-27-ramified-three-rotation-lift.md) covers this exact target. The directly linked Buchweitz--Flenner result supports the relative embedded deformation framework, and Poonen and Wood support cubic algebras over nilpotent bases; none is a match for the full global obstruction statement.

The supporting theory is imported. The fixed-product rigidity consequence, complete-fibre restriction and mixed-crossing calculation specialize it to this representative. Their combined statement was not matched in the checked literature, so POTENTIALLY_NEW means only potentially beyond those checked sources, not certified originality. This is an informative negative result for the prescribed lifting mechanism, not a resolution or disproof of the Hodge conjecture.
