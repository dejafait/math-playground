# L013 — Mixed extensions by the diagonal retain the cubic obstruction

## Hypotheses

Let S, X=S x S, C, V_N, V_RM, and V_D satisfy L008 and the additional genericity conditions of L009. Thus C is the reduced cubic correspondence support, its only singularities are the three transverse surface double points p_1,p_2,p_3, and it meets Delta=Delta_S along the diagonal copies D_+,D_- of two distinct smooth elliptic fibres F_+,F_- and at the p_i. There are 21 distinct finite nodal fibres, disjoint from F_+ and F_-. The same first-order deformation S_A occurs in both factors of X_A=S_A x_A S_A, where A=C[epsilon]/(epsilon^2) and kappa belongs to V_N.

For an arbitrary extension class e, fix its middle sheaf in

\[
0\longrightarrow\mathcal O_\Delta\longrightarrow\mathcal F_e
\longrightarrow\mathcal O_C\longrightarrow0.
\tag{1}
\]

A lift of F_e means an A-flat coherent sheaf on X_A with identified special fibre F_e. The maps in (1), its filtration, and its support are not assumed to lift. The case e=0 is included.

## Conclusion

Writing i_+ and i_- for the inclusions of the two curves in X, one has

\[
\begin{aligned}
\mathcal Hom_X(\mathcal O_C,\mathcal O_\Delta)&=0,\\
\mathcal Ext^1_X(\mathcal O_C,\mathcal O_\Delta)
&\simeq (i_+)_*N_{D_+/\Delta}\oplus(i_-)_*N_{D_-/\Delta},\\
\operatorname{Ext}^1_X(\mathcal O_C,\mathcal O_\Delta)&\simeq\mathbb C^2.
\end{aligned}
\tag{2}
\]

The two normal line bundles are trivial; the last isomorphism depends on their trivializations. There is no additional punctual Ext-sheaf contribution at the p_i. An extension with coordinate e_+ or e_- nonzero is locally cyclic along the corresponding entire curve; with that coordinate zero it is locally the direct sum there.

For every e and kappa as above,

\[
\mathcal F_e\text{ lifts to }X_A
\quad\Longleftrightarrow\quad \kappa\in V_D.
\tag{3}
\]

In particular the linear Atiyah obstruction

\[
o_{\mathcal F_e}(\kappa)
=(\operatorname{id}_{\mathcal F_e}\otimes\kappa_X)
  \circ\operatorname{At}(\mathcal F_e)
\in\operatorname{Ext}^2_X(\mathcal F_e,\mathcal F_e)
\tag{4}
\]

has kernel V_D on V_N and rank one on the four-dimensional V_RM. Its kernel on V_RM has dimension three, for every e. Meanwhile

\[
\operatorname{ch}_2(\mathcal F_e)=[C]+[\Delta]
\tag{5}
\]

acts on T(S) as U+id. Thus no mixed extension in (1) supplies the missing transverse first-order lift. This statement concerns the specified sheaves, not arbitrary sheaves with the same Chern character or the algebraicity of the Hodge class.

## Proof

**The mixed Ext sheaf along a finite intersection curve.** L009 gives local coordinates

\[
R=\mathbb C\{r,s,z,w\},\qquad
I_C=(z,s),\qquad I_\Delta=(z,r),\qquad I_{C\cup\Delta}=(z,rs).
\tag{6}
\]

Convergent power series suffice for the local arguments; their completed versions give the same finite-module calculations. Put M=R/(z,s) and N=R/(z,r). Applying Hom_R(-,N) to the Koszul resolution of M gives the cochain complex

\[
N\xrightarrow{b\mapsto(0,sb)}N^2
 \xrightarrow{(a,b)\mapsto-sa}N.
\tag{7}
\]

Multiplication by s is injective on N. Thus its degree-zero cohomology is zero and its degree-one cohomology is N/sN.

To identify the line bundle rather than only its local rank, apply sheaf Hom(-,O_Delta) to the ideal sequence of C. Locally a map I_C -> O_Delta sends z to a and s to b, and the Koszul relation forces sa=0, hence a=0. It therefore factors uniquely through I_C O_Delta, which is the Cartier ideal O_Delta(-D) of the intersection curve in Delta. Consequently Hom(I_C,O_Delta) is O_Delta(D) near this curve. Its quotient by Hom(O_X,O_Delta)=O_Delta is O_D(D)=N_{D/Delta}. This description is intrinsic and glues the local calculations. Each D is a fibre of the smooth elliptic fibration at its base value, so its normal line in Delta is trivial.

**No mixed Ext class is hidden at infinity.** At p_i let P,Q be the two smooth branches of C. L008 and L009 say that P,Q,Delta have pairwise transverse tangent planes. In particular

\[
0\longrightarrow R/I_C\longrightarrow R/I_P\oplus R/I_Q
\longrightarrow k\longrightarrow0
\tag{8}
\]

is exact, where k is the residue field and the last map is the difference of evaluations. Set N=R/I_Delta. The two equations of each of P,Q restrict to a regular system of parameters on the smooth surface Delta. Their Koszul resolutions therefore give

\[
\operatorname{Ext}^1_R(R/I_P,N)
=\operatorname{Ext}^1_R(R/I_Q,N)=0.
\]

The relevant part of the long exact sequence of (8) is

\[
0\longrightarrow\operatorname{Ext}^1_R(R/I_C,N)
\longrightarrow\operatorname{Ext}^2_R(k,N)
\longrightarrow\operatorname{Ext}^2_R(R/I_P\oplus R/I_Q,N).
\tag{9}
\]

The last map is injective, as can be checked using P alone. Choose coordinates with I_Delta=(x_1,x_2) and I_P=(y_1,y_2), possible because these two surfaces are transverse. On N=C{y_1,y_2}, the x-part of the residue-field Koszul cochain complex has zero differential and the y-part has cohomology k only in degree two. Hence Ext^2_R(k,N)=k, represented by the top y-Koszul class. Also Ext^2_R(R/I_P,N)=k. A chain map lifting R/I_P -> k includes the y-Koszul resolution into the full (x,y)-Koszul resolution. On degree-two Ext it takes the displayed class to itself. Thus the P component of the map in (9) is an isomorphism, proving Ext^1_R(R/I_C,N)=0. No assumption that the full scheme C intersect Delta is a reduced point is used.

Everywhere, the Hom sheaf in (2) is zero: the restriction of I_C contains a nonzero local function on the integral Delta, and O_Delta has no such torsion. Off the intersection all mixed Ext sheaves are zero. The preceding computations therefore describe the entire Ext sheaf. The local-to-global Ext spectral sequence in total degree one has only H^0 of this sheaf, since every cohomology group of the Hom sheaf is zero. Its only possible outgoing differential lands in H^2 of that zero sheaf. This proves the global assertion in (2), because each connected elliptic curve has H^0(O_D)=C.

**The local middle modules.** In (6), choose a generator a of the submodule N and a lift b of the generator of M. Relations for a representative of the extension are

\[
za=ra=0,\qquad zb=0,\qquad sb=c\,a,
\tag{10}
\]

where c modulo s is its local class in (7). To obtain these relations, the compatibility of zb and sb first forces zb=0, as in (7); changing b by a multiple of a changes c by a multiple of s. If the extension class vanishes, choose c=0 and (10) is the split module M direct sum N. If its value on D is nonzero, c is a unit locally, so eliminate a=c^(-1)sb. The module is then R/(z,rs). The normal line in (2) is trivial and its global sections are constants, so along each entire D either the class is zero or it is nowhere zero. These are all the local cases along the finite curves.

The split case here is essential: F_e need not be a line bundle on the whole reduced union, even though it is cyclic near every curve with nonzero coordinate.

**Two facts about an arbitrary lifted sheaf.** First, if an A-flat coherent sheaf has central module R/I generated by one element, lift that element on a local ambient chart. Nakayama gives a surjection O_XA -> F_A. Its quotient is A-flat by hypothesis and its kernel reduces to I, because Tor^A_1(F_A,C)=0. Thus its annihilator defines a flat embedded lift of that local support. This ideal is independent of the chosen generator.

Second, suppose the central module on a chart is M direct sum N. Trivialize the smooth ambient deformation on that chart, so its ring is R tensor A. Any A-flat lift determines the Yoneda extension

\[
0\longrightarrow M\oplus N\xrightarrow{\epsilon}F_A
\longrightarrow M\oplus N\longrightarrow0
\tag{11}
\]

as R-modules. Here the first arrow identifies the central module with epsilon F_A. Its class has four blocks in Ext^1_R(M direct sum N,M direct sum N). The M,M block is itself a self-extension of M, and similarly for N,N. Such a self-extension defines an A-flat module by making epsilon the composite of the quotient and submodule maps: its epsilon kernel equals its epsilon image. If M or N is a structure sheaf of a smooth local branch, the first fact turns its block into a flat embedded lift of that branch.

On the complement of the other branch, the restriction of (11) is exactly the corresponding diagonal block: all blocks involving the vanished module restrict to zero. Therefore the branch support obtained from that block agrees there with the support of F_A. This does not claim that F_A splits, or that either original map in (1) extends. In particular new mixed blocks are allowed in (11).

**The diagonal displacement has no new poles.** Suppose F_e lifts. On

\[
S^\circ=S\setminus(F_+\cup F_-\cup\{q_1,q_2,q_3\}),
\qquad p_i=(q_i,q_i),
\]

the central diagonal is disjoint from C. The first fact just proved gives a flat embedded lift of that branch, by its annihilator on this open set. Its first projection is locally an isomorphism: its reduction is the identity and the equations of a lifted smooth diagonal can be solved for the second coordinates over A. The local inverses glue. Its second projection consequently differs from the identity by epsilon times a vector field

\[
v\in H^0(S^\circ,T_S).
\]

Both ambient factors are the same S_A, so comparison with the actual relative diagonal makes v a global section, with no difference of Kodaira–Spencer classes.

Near either finite curve, L009 chooses local surface coordinates (u,w) in which the central correspondence branch is the graph of (u,w) -> (-u,w). Use the same lifted coordinates on both ambient factors and put r=u_2-u_1, s=u_2+u_1, z=w_2-w_1. If e is nonzero there, F_e is cyclic by (10), and its lift has a flat local support with equations

\[
z=\epsilon\alpha,\qquad rs=\epsilon\beta.
\]

Here alpha and beta are regular modulo (z,rs). On the punctured diagonal s=2u, giving

\[
v=\frac{\beta_\Delta}{2u}\frac{\partial}{\partial u}
  +\alpha_\Delta\frac{\partial}{\partial w}.
\tag{12}
\]

Thus its only possible pole is simple and in the base direction. If e is zero along this curve, the N,N block of (11) instead extends the diagonal branch regularly across the curve, so v has no pole there. This addresses the locally split case without assuming any flatness for the annihilator of the entire split sheaf.

At q_i a puncture in the smooth surface cannot create a pole of a vector-bundle section. Hartogs therefore gives

\[
v\in H^0\bigl(S,T_S(F_++F_-)\bigr).
\tag{13}
\]

Apply dpi and the projection formula for pi:S -> P^1 with connected fibres. The result is a section of T_P1(t_++t_-)=O_P1(4). At the node of each of the 21 finite singular fibres, v is regular and dpi vanishes on the tangent space of S. Hence this section vanishes at all 21 distinct nodal values and must be zero. In (12), this kills the possible base-direction polar part; the other coefficient is regular. Thus v extends to H^0(S,T_S)=0. The last equality follows by contracting with the K3 holomorphic symplectic form and using H^0(S,Omega_S^1)=0. The branch support is the actual diagonal wherever the two components are separated.

**Recovering C from the sheaf lift.** At a cyclic finite crossing let J_A be the annihilator of F_A on that chart. Its restriction to O_DeltaA is zero off the intersection by v=0, hence zero everywhere: multiplication by u is injective on the locally trivial A-flat O_DeltaA. Thus J_A is contained in I_DeltaA. Exactly as in L009's residual calculation, its equations can be written

\[
J_A=(z-\epsilon r a_0,\ r(s-\epsilon b_0)),\qquad
J_A:(z,r)=(z-\epsilon r a_0,\ s-\epsilon b_0).
\tag{14}
\]

The second quotient is A-flat, since the two central equations z,s have independent differentials. One can also verify the colon directly: after eliminating z, multiplication by r in A{r,s,w} is injective, so cancellation leaves s-epsilon b_0. This is a flat lift of the smooth C branch and agrees with F_A's support away from Delta.

At a locally split finite crossing take the M,M self-extension block of (11). It defines a flat lift of C on that chart, and it too agrees with F_A's support off Delta. Away from Delta, use the cyclic-support construction directly. These local lifts glue on C minus {p_i}. Indeed on any overlap they agree away from the intersection curves. The difference of two embedded first-order lifts of the smooth C is a regular section of its normal bundle; a section zero on a dense open set is zero. This also proves independence of the chosen local splitting and trivialization.

To fill a p_i, trivialize the smooth ambient deformation locally. The punctured embedded lift is a section of N_C on that puncture, by L007's ideal-deformation parametrization. L008 proves N_C=nu_*N_j, with nu:W -> C finite, W smooth, and N_j locally free. Removing p_i removes only two points from W. Hartogs on this vector bundle therefore extends the normal section uniquely. L007's parametrization turns it into a flat embedded lift on the whole neighbourhood. Uniqueness glues these extensions to a flat embedded C_A in X_A. Proper GAGA over A makes the analytic local construction algebraic.

This proves that every sheaf lift of F_e forces a support lift of C. L008 now gives kappa in V_D. No global Fitting support, lifted filtration, or flat colon at a three-branch point was assumed.

**Every extension class lifts along V_D.** Conversely, realize a direction in V_D by the Dickson family, giving C_A and Delta_A. Along the moving smooth curves D_+,A and D_-,A, the relative local equations are still (6) over A. At infinity, L009's finite-order linearization puts the three graphs in a constant plane arrangement over A. Thus (7)--(9) work over A as well: the relevant parameter multiplications remain injective and the map on the top y-Koszul class remains an isomorphism. They give

\[
\mathcal Hom_{X_A}(\mathcal O_{C_A},\mathcal O_{\Delta_A})=0,
\qquad
\mathcal Ext^1_{X_A}(\mathcal O_{C_A},\mathcal O_{\Delta_A})
\simeq\bigoplus_{\pm}(i_{\pm,A})_*N_{D_{\pm,A}/\Delta_A}.
\tag{15}
\]

Each D_+,A and D_-,A is a smooth elliptic fibre over a lifted base value. Its normal line in Delta_A is the pullback of the tangent line at that base value, hence trivial after choosing a basis over A. Its global functions are A. One direct check of the latter is to reduce a global function to its constant value on the central elliptic curve, subtract the same lifted constant, and identify the remaining epsilon multiple with a central global function. Local A-flatness makes this identification exact. Therefore the local-to-global spectral sequence again gives

\[
\operatorname{Ext}^1_{X_A}(\mathcal O_{C_A},\mathcal O_{\Delta_A})
\simeq A^2,
\tag{16}
\]

whose reduction onto the C^2 in (2) is surjective. This assertion uses the explicit relative computations, not an automatic base-change theorem for Ext. Choose a class reducing to e. Its extension has A-flat submodule and quotient, hence A-flat middle sheaf, and its special fibre is (1). All e thus lift along V_D, proving (3).

**The obstruction and the represented class.** The coherent sheaf F_e is perfect on the smooth projective X. The Atiyah--Kodaira--Spencer criterion for perfect complexes identifies its obstruction with (4); a precise supporting source is Huybrechts--Thomas, [*Deformation-obstruction theory for complexes via Atiyah and Kodaira--Spencer classes*, Corollary 3.4, p. 14](https://arxiv.org/pdf/0805.3527#page=14). The NS-fixed ample class makes X_A projective, so it embeds into a smooth ambient complex scheme, as required there. On the smooth central fibre the classical Atiyah class suffices.

Here perfect-complex lifting is equivalent to the sheaf lifting used in (3). To check the potentially nontrivial direction, tensor a perfect lift K_A with the triangle coming from 0 -> epsilon A -> A -> C -> 0. Both end terms are its derived central restriction F_e, so the cohomology sequence makes K_A a single sheaf fitting into 0 -> F_e -> K_A -> F_e -> 0. Multiplication by epsilon is the composite of the quotient and inclusion; its kernel equals its image, proving A-flatness. Conversely an A-flat coherent lift is locally perfect: successively choose finite free surjections, whose kernels stay A-flat; after the central finite free resolution reaches a locally free syzygy, its A-flat lift is locally free by Nakayama and the flatness criterion. Thus the obstruction criterion detects exactly (3). Since (4) is linear in kappa, dim V_D=3 and dim V_RM=4 give the stated kernel and rank.

Additivity of the Chern character in (1) gives (5). For the leading term of O_C, the normalization exact sequence (8) globalizes to O_C -> nu_*O_W with cokernel the three residue fields. Grothendieck--Riemann--Roch for W -> X starts in degree four with [C], since the normalization has generic degree one by L007; the residue fields contribute only in degree eight. The same theorem for the smooth diagonal gives ch_2(O_Delta)=[Delta]. L006 and L007 identify [C]'s action with U, and the diagonal acts as id.

The achieved first-order kernel is three-dimensional for all of the two-dimensional extension space, against four dimensions required to pass this RM tangent test. The existing 21-dimensional algebraic span is still confined to the known family. Higher-order lifting and algebraization would remain necessary after a successful first-order test of some other representative; neither follows just from (5) remaining a Hodge class. No arbitrary fourfold or higher-dimensional case is resolved here.

## Mathlib

Coverage of the full statement: **not checked**. No full matching Mathlib theorem, supporting Mathlib name, or absence from Mathlib is asserted. Huybrechts--Thomas Corollary 3.4 is a supporting obstruction criterion, not a statement about these extensions or their kernel. [Stacks Project, Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB) supports the Hartogs step through the height-one-localization characterization of reflexive modules over a normal domain; it is not a Mathlib match or the full extension-sheaf result. The Koszul resolution, local-to-global Ext spectral sequence, Yoneda classification of extensions, Nakayama's lemma, the flatness criterion over dual numbers, proper GAGA, and Grothendieck--Riemann--Roch are named supporting inputs. The mixed Ext calculation including the isolated-point map, treatment of both local module types without preserving a filtration, recovery of C, and lifting of every class along V_D are proved above. L006 and L007 supply the cycle action and multiplicity, L007 and L008 the support obstruction and normal-sheaf extension property, and L009 the intersection geometry, local coordinates, and relative linearization at infinity.
