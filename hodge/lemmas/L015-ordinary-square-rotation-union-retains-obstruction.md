# L015 — An ordinary-square rotation union retains the cubic obstruction

## Hypotheses

Use the very-general cubic Dickson surface S, the finite cover W, the three reduced rotation images C^(j), and the open conditions on the critical fibres and j-map in L014. In particular C^(1)=C. Write X=S x S, A=C[epsilon]/(epsilon^2), and

\[
I_Y=I_{C^{(1)}}\cap I_{C^{(2)}}^2\cap I_{C^{(3)}}.
\]

This is the ordinary square of the entire ideal sheaf of C^(2), including at its three singular points. It is not a symbolic square or an intersection of squares of its analytic branch ideals. An allowed lift is any A-flat closed subscheme Y_A of X_A=S_A x_A S_A with this special fibre; no component, reduction or nilpotent filtration is required to lift. The ambient tangent direction kappa lies in V_N, with V_D and V_RM as in L008.

Use L007's first-order ideal-gluing obstruction ob_Y. Its proof applies to this arbitrary ideal: local lifts in a trivialized smooth ambient deformation are parametrized by Hom(I_Y,O_Y), and the normal-sheaf Cech class vanishes precisely when they glue. This is a first-order statement, not an identification of the full higher obstruction theory with H^1 of a normal sheaf.

## Conclusion

The fundamental cycle and its action on T(S) are

\[
[Y]=[C^{(1)}]+3[C^{(2)}]+[C^{(3)}],
\qquad T_{[Y]}|_{T(S)}=2U^2-5\operatorname{id}.
\tag{1}
\]

This action is non-scalar. Nevertheless every allowed lift of Y yields an embedded lift of C, and

\[
\ker(\operatorname{ob}_Y|_{V_N})=V_D,\qquad
\dim\ker(\operatorname{ob}_Y|_{V_{\rm RM}})=3,\qquad
\operatorname{rank}(\operatorname{ob}_Y|_{V_{\rm RM}})=1.
\tag{2}
\]

The distinguishing compatibility condition occurs at a reduced--thickened intersection. In local coordinates its ideal is (z^2,zq,rq^2). If mu is the possible pole residue of the reduced branch's r-displacement, the normalized trace section of the thickened branch has q-displacement residue mu/3. Equality of the two fibre j-invariants on each section forces both residues to vanish. Nilpotent deformation parameters other than this residue need not vanish.

Thus the useful cycle passes the relevance check but fails the required four-dimensional first-order kernel. This stops the specified representative at first order. It does not exclude other representatives, ramified deformations with a later nonzero ambient term, or all algebraic cycles on the transverse surfaces. No new surface attains the known 21-dimensional span by this argument.

## Proof

**Cycle multiplicity and action.** The three supports are distinct, irreducible surfaces, generically smooth of codimension two. Their generic multiplicity-one normalization maps and finite intersections are established in L014. At the generic point of C^(2), the ambient local ring is regular of dimension two and its ideal is the maximal ideal m. The residue field is K, and m/m^2 has dimension two over K. The exact sequence

\[
0\longrightarrow m/m^2\longrightarrow R/m^2\longrightarrow K
\longrightarrow0
\]

gives length three. The other two ideals become units there. At the generic points of C^(1) and C^(3) the coefficient is one. The associated-cycle definition uses these generic lengths; lower-dimensional or embedded structure at the intersections does not change them. The supporting references already screened are [Stacks Project, Definition 42.10.2, Tag 02QX](https://stacks.math.columbia.edu/tag/02QX) and the conormal description for regular immersions in [Section 31.22, Tag 0638](https://stacks.math.columbia.edu/tag/0638). This proves the cycle formula for the specified ordinary square.

Put theta_j=zeta^j+zeta^(-j). The trace computation in L006 works for j=1,2,3: the deck involution v -> a*zeta^(-2j)/v gives

\[
(g_0\sigma^j)^*((g_0\sigma^j)_*g_0^*\omega)
=g_0^*\omega+\kappa_j^*g_0^*\omega
=\theta_j(g_0\sigma^j)^*\omega.
\]

Generic multiplicity one identifies this pushforward with [C^(j)]. The full endomorphism field acts injectively on the holomorphic line, so theta_2=theta_1^2-2 and theta_1+theta_2+theta_3=-1 give respectively the actions U^2-2 id and -U^2-U+id for j=2,3. Their weighted sum is (1). The irreducible cubic for U in L006 excludes a rational quadratic relation, so 2U^2-5 id is non-scalar. These are action identities on T, not Chow identities or identifications with composition supports.

**The finite strata and the exact ideal at infinity.** Retain L014's notation

\[
Q_j(t,s)=t^2+s^2-\theta_jts-a(4-\theta_j^2),\quad
p_{e,k}=ec\theta_k,\quad c^2=a,\quad e=\pm1.
\]

For each e, the unordered critical pairs {1,2}, {1,3}, {2,3} lie respectively on conic pairs {Q_1,Q_3}, {Q_2,Q_3}, {Q_1,Q_2}. Each occurs in both orders. L014 proves that these twelve finite intersection curves are smooth complete elliptic curves, that the conic pairs are transverse and unramified over both bases there, and that there are no finite triple intersections. Four curves are reduced--reduced; eight meet the squared component.

At a mixed curve choose r=Q_i for its reduced component, q=Q_2, a fibre difference coordinate z, and a coordinate w along the common fibre. The central ideals of the two smooth surfaces are (z,r) and (z,q), giving exactly

\[
(z,r)\cap(z,q)^2=(z^2,zq,rq^2).
\tag{3}
\]

Indeed reduce an element of (z^2,zq,q^2) modulo (z,r); its q^2 coefficient must belong to (z,r), and zq^2 is already in (zq). At a reduced--reduced curve the ideal is (z,rq), as in L014. On the remaining finite locus the scheme is one smooth surface or its ordinary first infinitesimal neighbourhood.

At infinity there are precisely the three points from L008. In its equivariant local coordinates, let

\[
J_k=(w_1-\zeta^{kd_1}u_1,\ w_2-\zeta^{kd_2}u_2),
\quad
(d_1,d_2)=(6,2),(3,5),(6,2).
\]

The full completed ideal is

\[
(J_1\cap J_{-1})\ \cap\ (J_2\cap J_{-2})^2\
\cap\ (J_3\cap J_{-3}).
\tag{4}
\]

The six graph planes have pairwise invertible differences of their tangent matrices. Formula (4), rather than an intersection of six independently thickened planes, retains the specified nilpotent and possible punctual structure. We will determine the kernel without classifying all local deformation parameters of (4): necessity uses extension of the recovered C across its punctures, while sufficiency makes this entire ideal constant in a family.

**A trace section for a deformed square-zero rank-three algebra.** We first give the algebra needed on the dense open where a thickened sheet is a neighbourhood of a graph. Let R_A be a flat A-algebra and B_A a free commutative R_A-algebra of rank three with basis 1,x,y, reducing to R_0[x,y]/(x,y)^2. All multiplication corrections are first order, so write

\[
x^2=\epsilon(a_0+a_1x+a_2y),\quad
xy=\epsilon(b_0+b_1x+b_2y),\quad
y^2=\epsilon(c_0+c_1x+c_2y)
\tag{5}
\]

with coefficients in R_0, lifted arbitrarily to R_A. Associativity (x^2)y=x(xy) gives a_0*y=b_0*x after identifying epsilon B_A with B_0. Independence of x,y gives a_0=b_0=0. The relation (xy)y=x(y^2) similarly gives c_0=0. Therefore

\[
\operatorname{Tr}(x)=\epsilon(a_1+b_2),\qquad
\operatorname{Tr}(y)=\epsilon(b_1+c_2),\qquad
\operatorname{Tr}(x^2)=\operatorname{Tr}(xy)
=\operatorname{Tr}(y^2)=0.
\]

Consequently tau=Tr/3 is a unital R_A-algebra homomorphism B_A -> R_A: multiplicativity holds on the basis pairs and hence everywhere by bilinearity. This uses first order and the rank-three square-zero special fibre. It is not a statement about arbitrary finite flat algebras or higher-order deformations. Trace is intrinsic, so these local maps glue.

For a neighbourhood of a graph of a morphism between smooth surfaces, its ordinary ideal-square quotient has just this special fibre over the first projection. Lifts of two relative coordinates and 1 remain a basis by Nakayama's lemma; the argument applies locally. The resulting section Spec R_A -> Spec B_A, followed by the second projection, is an actual graph map. It reduces to the original graph. Calling it the trace section imposes no requirement that a chosen central reduction or filtration persist.

**Fibre j-invariants on the separated sheets.** Suppose Y_A is an allowed lift. The NS-fixed argument in L008, which is independent of a support lift, gives an elliptic pencil and zero section on S_A. Trivialize its base P^1_A and write

\[
J_A(t)=J_0(t)+\epsilon\,dJ(t),\qquad J_0=R\circ P_a
\]

with R as in L014. Set a_{e,k}=dJ(p_{e,k}); these are well-defined under an infinitesimal base change because J_0' vanishes at all six critical points. They are regular there by the smooth-fibre hypotheses.

The first projection Y_A -> S_A is finite: it is proper and its special fibre is finite, so all its fibres have dimension zero even over the nilpotent base. On a small disk in a dense open of the first elliptic base, avoid intersections, branch values, singular fibres and infinity. The central finite algebra separates into four rank-one reduced graph sheets and two rank-three squared graph sheets. Its idempotents lift uniquely. Each lifted summand is A-flat; since its central module is locally free over S, the local flatness criterion makes it locally free of the same rank over S_A.

The rank-one sheets are graphs by their unit maps. The rank-three sheets have the trace sections just proved. All these graph maps are defined on the whole S_A over the chosen base disk, including the complete elliptic fibres. Their second base coordinate comes from the first base: a central function on this elliptic surface comes from the base because its proper connected fibres have only constant functions. Subtracting a lift of that base function reduces the assertion over A to the same assertion for the epsilon coefficient. Thus each graph sends complete fibres to fibres. Its fibre map reduces to an isomorphism, and is itself an isomorphism: properness and the rank-one finite-algebra argument apply to a morphism of smooth curves with isomorphic special fibre.

Each graph therefore satisfies J_A(t)=J_A(s). The j-invariance used here is the supporting result in [Schuett--Shioda, Elliptic Surfaces, Section 2.6 and Theorem 2.4, p. 5](https://arxiv.org/pdf/0907.0298#page=5), already checked in the prior assessment's L014 comparison. Over A, translate the image of the origin and use the short-Weierstrass scaling x -> u^2x, y -> u^3y; numerator and denominator of j have the same weight. No converse from equal j to an isomorphism is needed.

This proves equality on the reduced sheets and the trace sections on the dense complete-fibre locus. It does not assert that J_A(t)-J_A(s) vanishes on the whole nonreduced Y_A. In fact its central reduction generally does not vanish there. The separate identities extend as identities of meromorphic normal displacements on each central smooth branch. This is enough for the residue calculation.

**All first-order displacements at a mixed curve.** Work in (3), with coefficients in K=C[[w]], and put

\[
B=K[[r,q,z]]/(z^2,zq,rq^2),\quad f=z^2,\quad g=zq,\quad h=rq^2.
\]

The syzygy module of these three monomials is generated by q*f-z*g and rq*g-z*h. One can check this without a resolution theorem: pairwise monomial syzygies generate by cancellation of monomials; the remaining pair syzygy rq^2*f-z^2*h is rq times the first plus z times the second. The same coefficientwise argument works for power series.

Every element of B has a unique expression A(r)+q*B_1(r)+q^2*C(q)+z*D(r). Write a general such expression for each image of phi:I -> B. The equation q*phi(f)-z*phi(g)=0 forces the constant-in-q,z parts of both images to be zero, the q coefficient of phi(f) to be divisible by r, and its q^2 tail to be zero. Then rq*phi(g)=0, and the other syzygy forces the constant-in-q,z part of phi(h) to vanish. Hence exactly all homomorphisms are

\[
\begin{aligned}
\phi(f)&=rq\,A(r)+z\,B_0(r),\\
\phi(g)&=q\,C(r)+q^2D(q)+z\,E(r),\\
\phi(h)&=q\,M(r)+q^2N(q)+z\,P(r).
\end{aligned}
\tag{6}
\]

The eight series have coefficients in K and are arbitrary. Conversely these expressions satisfy both generating syzygies. By L007 they parametrize every flat first-order ideal lift in a trivialized ambient chart. Choose the sign convention that a lift has equations f-epsilon*phi(f), and similarly for g,h; changing the parametrization sign changes all displacements together.

On the reduced branch r=z=0, away from q=0, the actual isolated reduced sheet has normal displacement

\[
\delta r=\frac{M(0)}q+N(q),\qquad
\delta z=C(0)+qD(q).
\tag{7}
\]

In particular it has at most a simple r-pole and no z-pole. On the thickened branch q=z=0, away from r=0, equations (6) give the products in the free basis 1,q,z over the first projection:

\[
\begin{aligned}
q^2&=\epsilon\left(\frac{M(r)}r q+\frac{P(r)}r z\right),\\
qz&=\epsilon(C(r)q+E(r)z),\\
z^2&=\epsilon(rA(r)q+B_0(r)z).
\end{aligned}
\tag{8}
\]

Their normalized traces give the normal displacement of its trace section:

\[
\delta q=\frac13\left(\frac{M(r)}r+E(r)\right),\qquad
\delta z=\frac13(C(r)+B_0(r)).
\tag{9}
\]

In (8)--(9), coefficients mean their restrictions to the central thick branch. This remains correct when r,w are not exactly the chosen first-projection coordinates: on that branch the first projection is etale, so express r,w in those coordinates and q,z. The terms linear in q,z in any coefficient multiply a central quadratic normal monomial and disappear in an epsilon correction. Thus the calculation gives the intrinsic normal displacement; tangential reparametrization does not change it.

Equations (7) and (9) exhibit the residues mu=M(0) and mu/3. They retain all the nilpotent parameters A,B_0,C,D,E,M,N,P. In particular P(0), another possible local parameter, was not discarded or assumed zero. The pole coefficient mu glues in the fixed base-coordinate trivializations; the argument below is also valid separately on every chart of the elliptic curve.

**The residue incompatibility.** Choose one mixed ordered critical pair (p_{e,k},p_{e,l}). The Dickson factorization in L014 and the assumption R'(2ec^7) nonzero give near the corresponding whole elliptic curve

\[
F_0(t,s):=J_0(t)-J_0(s)=H(t,s)\,r q,\qquad H|_D=H_D\ne0.
\tag{10}
\]

The other conic and t-s are units there. The finite base coordinates t,s lift in the smooth ambient family and can be used in its local trivializations. Thus the extra first-order term of F_A is dJ(t)-dJ(s). Its value on the curve is d=a_{e,k}-a_{e,l}.

Restrict the meromorphic graph identities proved above to the two central branches. On the reduced branch the differential of (10) is H*q*delta r. Substituting (7) and restricting to D gives

\[
d+H_D\mu=0.
\tag{11}
\]

On the trace section of the thick branch the differential is H*r*delta q. Equation (9) gives

\[
d+\frac{H_D\mu}{3}=0.
\tag{12}
\]

The regular parts of (7) and (9) are multiplied by q or r and vanish on D. Changes by tangential displacements do not alter either equation because F_0 vanishes identically on each central branch. These are restrictions of identities known on dense open subsets; the displayed pole bounds make their products regular at D, justifying the restriction. Subtracting (12) from (11) gives 2*H_D*mu/3=0, hence mu=d=0.

The mixed curves are the ordered pairs {1,3} and {2,3} for each sign e. They therefore force

\[
a_{e,1}=a_{e,3},\qquad a_{e,2}=a_{e,3}.
\tag{13}
\]

At the remaining, reduced--reduced, curves with pair {1,2}, the central ideal is (z,rq). On this neighbourhood F_A vanishes on the entire lifted union: its reduction vanishes, and its epsilon coefficient vanishes on the dense open of each reduced central branch, hence on their reduced union. Write its arbitrary lifted equations as z-epsilon*alpha and rq-epsilon*beta. Formula (10) now gives H_D*beta|_D+a_{e,1}-a_{e,2}=0. Equation (13) forces beta|_D=0. This is L014's local double-crossing argument with the corresponding pair of conics; its former single-branch test is replaced here by (11)--(12).

**Recovering C and the necessary kernel inclusion.** Off the other components and infinity, Y_A itself restricts to a smooth lift of C. At a mixed crossing on C, mu=0 makes both normal displacements (7) regular. They define a smooth embedded lift across the whole curve by the ideal parametrization for (z,r). It agrees with the given isolated sheet off that curve. In fact it is contained in Y_A: the restrictions of (6) to this branch coincide with the variations of f,g,h obtained from (7), with M(0)=0.

At a reduced--reduced crossing, beta|_D=0 means beta=r*b+q*a in the central quotient. The product equation factors to first order as (r-epsilon*a)(q-epsilon*b), after absorbing terms in the central ideal into its generators. Together with z-epsilon*alpha this gives the two smooth component lifts. Take the one reducing to C.

These local lifts glue. Their restrictions on the dense open of each smooth central branch agree, and their difference is a regular normal-bundle section, which must then be zero. This produces an embedded C lift off the three infinity points.

L008 proves N_C=nu_*N_j with W smooth and N_j locally free. Removing those points removes only finitely many points on W. Hartogs extends a section of N_j uniquely across them, hence does the same for N_C. Trivialize the ambient first-order deformation near an infinity point. L007 identifies the punctured lift with a section of N_C there; extend it and use its ideal parametrization to obtain a flat lift on the full neighbourhood. Uniqueness makes these ideals glue. Proper GAGA over A applies if these constructions are made analytically.

This extension concerns the recovered reduced C, whose normal sheaf has the stated property. No flatness of a residual ideal of (4), reduction of Y_A, or prescribed lift of its nilpotent structure at infinity is assumed. Any actual Y_A would imply C_A, so L008 yields kappa in V_D.

**Sufficiency, including the entire ordinary square.** Vary the Dickson parameters in a small neighbourhood retaining the generic hypotheses, and use the scheme-theoretic intersection of the two reduced image ideals with the square of the second image ideal. At a smooth component point there are relative regular coordinates making the ideal a coordinate ideal or its square. At finite intersection curves the same transverse base coordinates and fibre difference give the constant ideals (z,rq) or (3). Their quotients are flat over the parameter base.

At infinity, L008's order-seven local automorphism f and its three fixed points vary with the parameters. Since df-id is invertible, those fixed points persist as sections. Finite-group averaging, as in L014, provides relative analytic coordinates with f equal to the constant diagonal matrix with the appropriate weights. Use the same coordinates in both factors. All six graphs become the constant J_k, and the full ideal, with the ordinary square taken after its two-branch intersection, is precisely the constant expression (4). Its quotient is a product with the parameter base and is flat, including any embedded structure. This verifies flatness for the specified ideal rather than for a substituted thickening.

Every tangent vector in V_D therefore lifts Y. Combined with necessity and L008's dimensions dim V_D=3 and dim V_RM=4, this proves (2). The calculation is for unramified first-order embedded deformations. It supplies no statement that a family with zero first derivative and a later transverse term must obey the same linear trace identities.

The supporting command

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/cubic-deformation/check_three_rotation_thickening.py

checks the monomial ideal, graded normal-module dimensions and spanning formulas, rank-three associativity and trace identities, and the numerical residue and critical-pair constraint ranks using exact rational arithmetic. It also checks the cycle-action identity and all six distinct infinity weights. These finite calculations do not verify the global graph construction, Hartogs extension or family flatness; their informal proofs are above.

## Mathlib

Coverage of the full statement: **not checked**. No matching or supporting Mathlib theorem, or absence from checked Mathlib sources, is asserted. The [saved SPECIALIZE assessment](../drafts/literature/2026-09-26-three-rotation-thickening.md) covers the exact target. [Buchweitz--Flenner, Lemmas 7.6--7.7, Theorem 7.8 and Remark 7.11(1), pp. 190--192](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56) support general embedded deformation theory; the Stacks and elliptic-surface references above support cycle multiplicities and j-invariance. They do not state this union's kernel.

The family construction and rotation actions are imported or reproduced. The rank-three trace argument, its mixed-crossing specialization and the resulting kernel were not matched by the sources in the saved bounded review. The step is classified POTENTIALLY_NEW only in that limited sense, with no certified originality claim. It is an informative negative result for this representative, not a resolution of the rational Hodge conjecture.
