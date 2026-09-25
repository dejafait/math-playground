# L011 — The length-two fibre thickening retains the cubic obstruction

## Hypotheses

Let S, C, X=S x S, V_N, V_RM, and V_D satisfy L008, and retain the smooth fibre E=F_+ and local conic coordinates used in L010. Put B=E x E and D=Delta_E. With theta=zeta+zeta^(-1), let R_theta be the base correspondence whose finite equation is

\[
t_1^2+t_2^2-\theta t_1t_2=a(4-\theta^2).
\]

At b=(t_+,t_+) this is smooth. Let xi be its length-two subscheme supported at b, defined by the square of the maximal ideal in O_{R_theta,b}. For p=pi x pi:X -> P^1 x P^1 set

\[
B_2=p^{-1}(\xi),\qquad Y_2=C\cup B_2,
\]

where the union is scheme-theoretic, with ideal I_C intersect I_{B_2}. The scheme B_2 is nonreduced. Work over A=C[epsilon]/(epsilon^2) in X_A=S_A x_A S_A, where S_A is an NS-fixed first-order deformation. Define N_{Y_2}=Hom(I_{Y_2}/I_{Y_2}^2,O_{Y_2}) and the ideal-gluing obstruction ob_{Y_2} as in L007. Its vanishing is equivalent to a flat embedded lift; no lci hypothesis on all of Y_2 is imposed.

## Conclusion

Every flat embedded lift Y_{2,A} contains a flat embedded lift B'_{2,A} of B_2. The residual ideal I_{Y_{2,A}}:I_{B'_{2,A}} defines a flat embedded lift of C. Consequently

\[
\ker(\operatorname{ob}_{Y_2}|_{V_N})=V_D,\qquad
\dim\ker(\operatorname{ob}_{Y_2}|_{V_{\rm RM}})=3,\qquad
\operatorname{rank}(\operatorname{ob}_{Y_2}|_{V_{\rm RM}})=1.
\]

The fundamental cycle is [C]+2[B], with the same transcendental action U as C. The required four-dimensional lifting kernel is not attained. This rejects the specified length-two addition; it does not obstruct all nonreduced representatives, all algebraic extensions of U, or the Hodge conjecture.

## Proof

**The Cartier intersection on the thickening.** Work analytically near the compact fibre product B, applying proper GAGA over A at the end. Choose base coordinates s,r near b such that R_theta is s=0 and xi has ideal (s,r^2). They can be taken to be the involution coordinates from L010. The map p is smooth near B. Near any point of D, including its zero-section point, the remaining coordinates z,w from L010 give

\[
I_C=(s,z),\quad I_{B_2}=(s,r^2),\quad
I_{Y_2}=(s,r^2z).
\tag{1}
\]

The last equality follows in the regular ring modulo s from (z) intersect (r^2)=(r^2z). Set D_2=C intersect B_2. Its ideal in O_{B_2} is locally (z). Here z is a non-zero-divisor in C[[r,z,w]]/(r^2), and away from D this ideal is the unit ideal. Thus D_2 is a globally defined effective Cartier divisor of B_2, reducing to D on B. The three singular points of C over infinity are disjoint from B_2.

The equations s,r^2, defined on a neighbourhood of all of B, trivialize the conormal of B_2. Therefore

\[
N_{B_2/X}\simeq O_{B_2}^{\oplus2}.
\tag{2}
\]

As p is smooth near B, B_2 is flat over T=Spec C[r]/(r^2). Multiplication by r identifies its nilpotent ideal with O_B. In particular

\[
0\longrightarrow O_B\xrightarrow{\ r\ }O_{B_2}
\longrightarrow O_B\longrightarrow0.
\tag{3}
\]

The first arrow sends a function on B to r times any lift; it is independent of the lift. This does not assume that B_2 is a product deformation of B.

**Simple poles still supply no extra global sections.** The elliptic calculation in L010 gives

\[
H^0(B,O_B(D))=H^0(B,O_B)=\mathbb C
\tag{4}
\]

under the natural inclusion. Namely the difference map E x E -> E identifies O_B(D) with the pullback of O_E(0), and genus-one Riemann–Roch gives h^0(O_E(0))=1. The supporting precise source is [Stacks Project, Lemma 53.5.2, Riemann–Roch, tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6). Equality (4) says there is no genuine meromorphic simple pole, not that the line bundle has no sections.

Let L=O_{B_2}(D_2). Tensor (3) with this invertible sheaf. Since L|_B=O_B(D), the resulting exact sequence has outer terms O_B(D). If h is a global section of L, its reduction on B is a constant by (4). Subtract that constant, viewed as a regular section through O_{B_2} -> L. The remainder lies in the kernel, which is H^0(B,O_B(D)) under the left-hand injection. It is therefore r times another constant, again a regular function on B_2. Conversely every regular function gives such a section. The same reduction argument in (3) shows that the regular functions are exactly c_0+c_1r. Thus

\[
H^0(B_2,O_{B_2}(D_2))=H^0(B_2,O_{B_2})
=\mathbb C\oplus\mathbb C r,
\tag{5}
\]

and (2) gives

\[
H^0(B_2,N_{B_2/X}(D_2))=H^0(B_2,N_{B_2/X})
\simeq\mathbb C^4.
\tag{6}
\]

This calculation explicitly treats both nilpotent layers. It uses neither reducedness nor a vanishing assertion for H^1 of the normal sheaf.

**A reference thickening and the pole bound for an arbitrary lift.** L010 proves that the elliptic pencil extends to pi_A:S_A -> P^1_A in every NS-fixed direction. Use the same base coordinates s,r over A and pull back the constant length-two base scheme (s,r^2). This gives a reference lift B^0_{2,A}. It is A-flat because the base scheme is free of rank two over A and p_A is smooth along its inverse image.

Suppose Y_{2,A} is an A-flat embedded lift. On the open complement of C its central fibre is B_2 minus D, so it is a lift of this open part of B_2. Comparing it with B^0_{2,A} gives an intrinsic section

\[
\sigma\in H^0(B_2\setminus D,N_{B_2/X}).
\]

Here D denotes the closed support of D_2; the open subscheme retains its nilpotents. The usual difference of first-order ideals is a homomorphism I/I^2 -> O, as proved in L007. It applies to this nonreduced lci scheme.

Lift coordinates near D so B^0_{2,A} has equations s=r^2=0. Since (1) is a regular-sequence ideal and the lifted quotient is A-flat, its generators lift to generators of I_{Y_{2,A}}. They have the form

\[
s-\epsilon\alpha,\qquad r^2z-\epsilon\beta.
\tag{7}
\]

On the open set where z is invertible, divide the second generator by z. Relative to the normal frame dual to s,r^2, the difference section has components

\[
\alpha|_{B_2},\qquad (\beta|_{B_2})/z.
\tag{8}
\]

They have at most a simple pole along the Cartier divisor D_2. This is invariant under changes of regular normal frame and local equation of D_2, so sigma lies in H^0(B_2,N_{B_2/X}(D_2)). By (6) it is regular everywhere. The exponent two on r has not produced a second-order pole along z=0; these are different coordinates and different divisors.

Write its components in the global frame (2) as a_0+a_1r and b_0+b_1r. The deformed base scheme

\[
s=\epsilon(a_0+a_1r),\qquad
r^2=\epsilon(b_0+b_1r)
\tag{9}
\]

is finite flat of length two over A: eliminate s, and the remaining monic quadratic has basis 1,r. Its inverse image B'_{2,A} under p_A is a flat embedded lift with exactly the difference section sigma. It agrees with Y_{2,A} on the complement of C. Equivalently, it is the modification of the reference lift by that global normal section. Crucially, (9) allows a deformation r^2=epsilon b_0; it does not insist that the double structure remain fixed.

**Containment without an appeal to reduced density.** Restrict any local section of I_{Y_{2,A}} to O_{B'_{2,A}}. Its reduction is zero, so A-flatness writes it as epsilon times a unique central function h on B_2. On B_2 minus D the two lifts agree, and hence h vanishes there. Locally multiplication by z is injective on O_{B_2}; thus the localization O_{B_2} -> O_{B_2}[1/z] is injective. It follows that h=0. This proves

\[
B'_{2,A}\subset Y_{2,A}
\tag{10}
\]

scheme-theoretically. The argument excludes functions supported on D even in the nilpotent layer; density of an open set in the reduced support alone would not have sufficed.

**The residual is flat even when the thickening changes.** Near D let K=(S,R) be the ideal of B'_{2,A}, with reductions s,r^2 as in (9), and write J=I_{Y_{2,A}}. By (10), J is contained in K. Choose generators of J reducing to s,r^2z. The regular sequence s,r^2 has only its Koszul syzygies, so their coefficients in S,R may be chosen with reductions (1,0) and (0,z), respectively. Explicitly, if a s+b r^2=s, then (a-1,b)=h(r^2,-s); subtracting the lifted Koszul syzygy adjusts the coefficients to those reductions. The second row is handled identically. Hence for some local coefficients p,q,u,v,

\[
J=\bigl((1+\epsilon p)S+\epsilon qR,
          \epsilon uS+(z+\epsilon v)R\bigr).
\]

Divide the first generator by its unit coefficient, put S'=S+epsilon qR, and subtract epsilon u times it from the second generator. This gives

\[
K=(S',R),\qquad J=(S',RZ),\qquad Z=z+\epsilon v.
\tag{11}
\]

In the ambient ring modulo S', the element R is a non-zero-divisor. Indeed that quotient is smooth and flat over A with central coordinates r,z,w, and the reduction of R is the non-zero-divisor r^2. If Rx=0, reducing first forces x=epsilon x_1; flatness and reduction again force x_1 to vanish modulo epsilon, giving x=0. Cancellation of R in this quotient now proves

\[
J:K=(S',Z).
\tag{12}
\]

The central equations are s,z with independent differentials, so (12) defines a smooth, hence flat, lift of the C branch near D. This proof never changes R into r^2 by a coordinate transformation; such a transformation need not exist for (9).

Away from B, the residual is Y_{2,A}, already a lift of C. Away from C, the ideals of the two lifts agree and their colon is the unit ideal. These cases and (12) cover all of X, including the three singular points at infinity, which lie away from B. Therefore the global colon ideal defines a flat embedded C_A. Proper GAGA over the Artin base turns the analytic coherent constructions into algebraic ones. L008 now forces every admissible kappa in V_N to belong to V_D.

**The reverse inclusion.** Along the small Dickson-family neighbourhood from L008, choose b and its length-two subscheme on the varying conic holomorphically. The central smoothness conditions persist. The resulting B_2 family is flat: locally its base is the family of length-two points with algebra O_parameters[r]/(r^2), and the elliptic product is smooth over it. The intersection D_2 is the corresponding length-two restriction of the smooth elliptic C branch, and is flat over the parameters as well. L008 supplies a flat family C, including its three transverse double points. The relative union exact sequence

\[
0\longrightarrow O_{Y_2}\longrightarrow O_C\oplus O_{B_2}
\longrightarrow O_{D_2}\longrightarrow0
\]

then proves flatness of Y_2. Since the right term is flat, the sequence stays exact after base change, so its fibres are the required scheme-theoretic unions. Thus all directions in V_D admit lifts. Combined with the preceding containment this gives the kernel equality; the dimensions three and four, and hence rank one on V_RM, follow from L008.

Finally the generic multiplicities of Y_2 along C and B are one and two. Its fundamental cycle is [C]+2[B]. L010 identifies [B]=[F] tensor [F] and its zero action on T(S), while C acts as U. The thickening therefore preserved the intended cohomological action but failed the required first-order threshold. The 21-dimensional Hodge span remains established only for the already known cubic family, not for any new transverse member or for the universal target.

## Mathlib

Coverage of the full statement: **not checked**. No Mathlib match or absence is claimed. The directly linked [Stacks Project Riemann–Roch theorem, tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6), supports only the elliptic section count; it is not a match for this obstruction theorem. The first-order ideal parametrization, lifting of the elliptic pencil, and prior support kernel are used in their stated scopes. The nilpotent-layer pole calculation, containment, and residual flatness are proved here, with proper GAGA as a standard supporting theorem. No numerical evidence is used to infer the global obstruction.
