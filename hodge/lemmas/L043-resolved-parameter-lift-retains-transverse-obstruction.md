# L043 — Resolving the parameter does not remove the fourth-direction obstruction

## Hypotheses

Retain the very-general cubic-RM surface S, operator U, elliptic
fibration, three points q_i, and spaces V_N, V_RM and V_D of
L006, L008 and L009. In particular retain L009's 21 distinct
finite nodal fibres and smooth finite diagonal-intersection fibres.
Let g:S -> S^{(3)} and K=J O_S be L042's actual norm-cycle map
and image ideal, with J having its full scheme structure.

Let p:B -> S be a finite composition of point blowups with B
smooth projective and K O_B invertible. Such a p is constructed
below with nine point blowups. Further point blowups are allowed.
Let rho:S^[3] -> S^{(3)} and let f:B -> S^[3] be the unique
lift with rho f=g p. Put A=C[epsilon]/(epsilon^2).

In the deformation test, let S_A have class kappa in V_RM and
restrict the target to S_A^[3]. Allow an arbitrary smooth
first-order deformation B_A of B and an arbitrary map
f_A:B_A -> S_A^[3] reducing to f. Do not assume that p, an
exceptional configuration, g, or an embedded image has already
deformed. Analytic compact-manifold deformations are allowed;
this includes the algebraic projective ones.

## Conclusion

The stated central lift exists after three point blowups over
each q_i. It is a lift from a smooth projective resolution of
Bl_K(S), not a lift on the original S ruled out by L042.

Even with all source motions allowed, every such f_A forces

\[
\kappa\in V_D.
\tag{1}
\]

For the nine-blowup construction, every direction of V_D does
occur. Thus the attainable induced RM target directions are
exactly V_D, of dimension three against four required. The
necessary containment (1) also holds after further point
blowups of the parameter surface.

This stops this resolved-lift recipe at first order. It supplies
no fourth-direction representative, new algebraic class or
general Hodge resolution. It does not exclude other central
support cycles, ramified families with zero first-order target
motion, or unrelated higher-dimensional cycle sources.

## Proof

**The central family away from the three triple collisions.**
Write Y=C union Delta_S with its reduced union scheme. By
L008, the normalization W of C maps finite flat of degree two
to S and is an embedding in S x S except at the three image
double points. Outside q_1,q_2,q_3 in the first factor, C is
therefore finite flat of degree two. Away from the two finite
diagonal-intersection fibres, it is disjoint from the diagonal.

At either finite intersection curve, L009 gives coordinates
u_1,w_1,u_2,w_2 and the ideal

\[
(w_2-w_1,(u_2-u_1)(u_2+u_1)).
\]

Over the first factor this part of the family has algebra
O_S[u_2]/(u_2^2-u_1^2), free of rank two. The remaining
C point is a disjoint rank-one summand. At a branch point
of W -> S disjoint from the diagonal, C itself supplies
the rank-two finite flat algebra; no reduced-fibre argument
replaces it. Hence Y over

\[
S^0=S\setminus\{q_1,q_2,q_3\}
\]

is a closed finite flat degree-three subscheme of S^0 x S.
It defines a Hilbert-cube map whose Hilbert--Chow cycle is
g on the dense distinct-support open, and therefore everywhere
on S^0 by separatedness and reducedness. L040's correctly
scoped necessity criterion implies K is invertible on S^0.

**Explicit principalization at infinity.** At q_i use L042's
formal coordinates and put D=(uv,u^3,v^3), so K=D^2.
On the first point-blowup chart u=x, v=xy,

\[
D O=x^2(y,x),\qquad K O=x^4(y,x)^2.
\tag{2}
\]

The other chart gives the symmetric formula. Thus precisely
two points on this exceptional P^1 remain nonprincipal,
the two tangent-axis points. Blow up each of them once.
On the two charts at either point, the ideal (x,y) becomes
(x) or (y), so (2) becomes principal. Elsewhere it already
was principal. These are actual points specified by tangent
lines; formal coordinates are only used to check their ideals.
Invertibility descends from the faithfully flat completed
local rings. This proves principalization by three blowups
per q_i and no blowup away from them.

For clarity, if E_0' is the strict transform of the first
exceptional curve and E_1,E_2 are the two new exceptional
curves, the local divisor of K is

\[
4E_0'+6E_1+6E_2.
\]

All multiplicities belong to the full norm ideal D^2.
Replacing K by its radical would give a different calculation.
The global blowup universal property, [Stacks Lemma 31.33.5,
Tag 0806](https://stacks.math.columbia.edu/tag/0806), factors
p through Bl_K(S). It also gives the unique lift f to the
norm-ideal blowup S^[3] identified in L040. B is smooth
projective and its map to Bl_K(S) is proper birational, so
it is a smooth resolution of that blowup.

**All source motions admit some blowdown-map deformation.**
Use the already inspected simultaneous-map criterion of
[Iacono, arXiv:0705.4532v2, Theorem 5.5 and Remark 5.12,
equation (7), pp. 9,14--15](https://arxiv.org/pdf/0705.4532v2#page=14).
For a central map r:D' -> D, a pair of first-order classes
(eta,xi) is attained by a deformation of r exactly when

\[
dr(eta)=r^*(xi)\quad\hbox{in }H^1(D',r^*T_D).
\tag{3}
\]

This imports the map framework; it is not reproved here.
To apply it to every motion of a point blowup, check the
particular differential and pullback, rather than impose
persistence of its exceptional curves as an extra premise.

For r the blowup of a smooth point, its two local charts
give Rr_*O_{D'}=O_D. The degree-zero assertion is extension
of functions on a normal surface across the omitted point.
The degree-one assertion can be checked on the ordinary
blowup of A^2: the charts have rings C[x,t] and C[s,y],
with y=xt and s=t^{-1}; their intersection has ring
C[x,t,t^{-1}]. A monomial x^a t^b, a>=0, lies in the first
chart if b>=0, and if b<0 equals y^a s^{a-b} in the second.
Thus its Cech H^1 is zero. The same computation applies
after the local flat coordinate change for a smooth surface;
away from the centre r is an isomorphism. Higher direct
images vanish as well since the fibres have dimension one.
The projection formula and Leray consequently give

\[
r^*:H^1(D,T_D)\xrightarrow{\sim}H^1(D',r^*T_D).
\tag{4}
\]

The local Jacobian of (x,t) -> (x,xt) also checks

\[
0\longrightarrow T_{D'}\xrightarrow{dr}r^*T_D
\longrightarrow i_*O_E(1)\longrightarrow0.
\tag{5}
\]

Indeed the derivative is injective and its quotient is
supported on x=0; along E its image in the constant
two-dimensional tangent space at the centre is the
tautological O_E(-1), leaving quotient O_E(1).
In particular H^1(O_E(1))=0, so every target class can
also be attained. More essentially for the present test,
for *any* eta, (4) defines a unique xi satisfying (3).
Iacono therefore supplies a deformation of r with that
source class. Its source may be identified with the given
first-order D'_A, since these classes classify the
deformations up to isomorphism.

Apply this consecutively to the given sequence of point
blowups, starting with arbitrary B_A. It constructs some
smooth deformation S'_A of S and a morphism

\[
p_A:B_A\longrightarrow S'_A
\tag{6}
\]

reducing to p. This is a consequence for all source
motions, not a restriction to deformations chosen in
advance to preserve the resolution diagram. Off the
finite set of images of the blowup centres, (6) is an
isomorphism: it is proper with isomorphic special fibre
there, hence finite there, and the unit map is an
isomorphism by flatness and Nakayama. These arguments
also apply analytically using coherent proper pushforward.

**The map's periods identify S'_A with S_A.** Let Z be the
universal length-three subscheme on S^[3] x S. Use its
degree-two incidence correspondence

\[
\mu(t)=\operatorname{pr}_{S^{[3]}*}
             ([Z]\smile\operatorname{pr}_S^*t).
\]

Pulling Z back by f gives a finite flat family on B x S.
Over the complement of the blowup-centre images it is the
family Y just identified. Thus, on that open, f^*mu(t)
is the pullback to the *first* factor of Y's correspondence.
The transpose convention must be checked: on the dense
cover chart, v -> a zeta^{-1}/v exchanges
t=v+a/v and s=zeta v+zeta^{-1}a/v, with x,y unchanged.
The reduced closure C is therefore invariant under
transposition. L009's action U+id is consequently also
the action needed for this first-factor pullback.

The point-blowup cohomology decomposition is
H^2(B,Q)=p^*H^2(S,Q) plus its rational exceptional
divisor space. This follows successively by excision
for one blowup; equivalently, restriction off a point
retains H^2(S,Q) and adds one exceptional class upstairs.
All the added classes are of type (1,1). The difference
between f^*mu|_T and p^*(1+U) is thus a rational Hodge
map from T to that exceptional divisor space. It vanishes:
a rational Hodge functional T -> Q(-1), represented via
the nondegenerate cup pairing, would give a rational
(1,1)-vector in T, and L006's Lefschetz-(1,1) argument
excludes such a vector. We have proved the full central
identity, not just an identity on holomorphic forms:

\[
f^*\mu(t)=p^*(1+U)t\qquad(t\in T).
\tag{7}
\]

The same conclusion about exceptional corrections can
also be checked on every exceptional curve: its weighted
target support is the fixed finite cycle g(p(E)), and
the incidence class of a degree-two target class restricts
to zero there. There is no extra transcendental term
from the punctual Hilbert-cube fibre.

**Retain the map-motion homotopy explicitly.** Import the
full tangent cocycle from [Iacono, 0705.4532v2, Theorem 5.5
and Remark 5.6, PDF pp. 9--10](https://arxiv.org/pdf/0705.4532v2#page=9).
For any central holomorphic map r:D -> M with simultaneous
first-order deformation, choose Dolbeault representatives
eta_D, chi_M and a smooth section z of r^*T_M such that

\[
\bar\partial z=dr(\eta_D)-r^*(\chi_M).
\tag{7a}
\]

There is no assumption that the right side is zero as a
vector-valued form. If alpha is a holomorphic two-form on M,
define the smooth (1,0)-form on D

\[
c_\alpha(z)(v)=\alpha(z,dr(v)).
\]

The holomorphic bundle map c_alpha commutes with bar-partial.
Contraction of (7a), with the same slot convention on both
sides, therefore gives the exact correction

\[
\eta_D\mathbin{\lrcorner}r^*\alpha
 -r^*(\chi_M\mathbin{\lrcorner}\alpha)
 =\bar\partial c_\alpha(z).
\tag{7b}
\]

For example, in holomorphic coordinates its one-form is
alpha_ab(r) z^a (partial_i r^b) dx^i. Its bar-partial is
alpha_ab(r) (bar-partial_j z^a) (partial_i r^b)
dbar-x^j tensor dx^i, exactly the difference in (7b).
Holomorphicity of r and alpha eliminates the other terms.
Thus the homotopy is retained and is bar-partial-exact in
H^1(D,Omega_D^1). This is the needed extension of the
strict-representative contraction identity of
[Iacono, 0707.2454v2, Lemma 4.7, PDF p. 9](https://arxiv.org/pdf/0707.2454v2#page=9).
It applies separately to f_A and p_A, with their own z.

Use [Fiorenza--Manetti, published Proposition 4.5 and
Theorem 5.1, pp. 593,595--596](https://ems.press/content/serial-article-files/30459?nt=1#page=15)
for the formal Hodge filtration and its contraction derivative
over A. Its Artin-base naturality is not the incidence
comparison: that comparison is checked next.

**Check the relative incidence in the same markings.** Put
M_A=S_A^[3]. The actual relative universal subscheme
Z_A in M_A x_A S_A is finite flat of length three over M_A.
Its structure sheaf is a relative perfect complex on that
smooth relative product. Locally this follows by lifting a
finite free resolution of its central sheaf, using A-flatness
and Nakayama for each kernel. Equivalently, in surface
coordinate charts a length-three finite free algebra has
the length-two Koszul resolution for the two commuting
coordinate multiplication operators. This does not require
the support to be reduced or the punctual algebra to be
Gorenstein.

Use its relative degree-four Chern character

\[
\gamma_A=\operatorname{ch}_2(O_{Z_A})
 \in F^2H^4_{\rm dR}(M_A\times_A S_A/A).
\]

On the central smooth product, the leading-character formula
identifies gamma_0 with the full fundamental class [Z],
including generic lengths. This is the known input of
[Fulton, Intersection Theory, second edition, Theorem
18.3(3),(5) and Example 18.3.11, pp. 353--354,363](https://djvu.online/file/87GFN2nbfbdF7),
already inspected in the notebook's global-support assessment.
The relative holomorphic Chern character belongs to F^2:
it is the degree-two trace of the Atiyah class, or the
Chern--Weil character of compatible connections whose
curvature has no (0,2) part. This statement applies to
perfect complexes by locally free resolutions and descent;
no global holomorphic resolution on the analytic deformation
is assumed.

Here is the marking check, also over the nonreduced base.
Choose differentiable nilpotent trivializations of M_A and
S_A. A smooth vector-bundle lift has the same underlying
bundle over A as its reduction: the changes of local
trivializations are an additive cocycle of smooth
endomorphisms, killed by a partition of unity. This gives
the same topological K-class for the relative perfect
complex, using local resolutions and their descent. For
a connection deformation nabla_epsilon=nabla_0+epsilon a
with curvature R_0, the Chern--Weil transgression is

\[
\operatorname{ch}_2(\nabla_\epsilon)
 -\operatorname{ch}_2(\nabla_0)
 =\epsilon\,d\!\left((2\pi i)^{-2}
                       \operatorname{Tr}(a\wedge R_0)\right).
\tag{7c}
\]

It follows by differentiating Tr(R^2)/(2(2 pi i)^2),
using the Bianchi identity and the trace of a commutator
being zero. Signed sums, or the corresponding descended
perfect-complex character, obey the same transgression.
Consequently gamma_A is [Z] tensor 1 in marked de Rham
cohomology. This uses the universal sheaf on the entire
relative product, including collisions; an identity only
on the distinct-support open is not used to determine it.

Define mu_A by cup product with gamma_A and fibre
integration along the surface factor. These operations
are the central operations under the product marking.
Moreover mu_A takes F^2 in degree two to F^2 in degree
two: gamma_A contributes filtration degree two, and
integration over S_A lowers it by two. Thus

\[
\mu_A=\mu\otimes 1
\quad\text{as marked maps,}\qquad
\mu_A(F^2H^2(S_A))\subset F^2H^2(M_A).
\tag{7d}
\]

An arbitrary motion of f does not change its marked
pullback either. In differentiable trivializations its
first-order variation on a closed form beta is
d c_beta(z)+c_{d beta}(z)=d c_beta(z), the Cartan homotopy
formula along r. Changes of trivialization are themselves
infinitesimal diffeomorphisms and induce the identity on
de Rham cohomology by the same formula. The marked maps
of f_A and p_A are therefore their central pullbacks.
Unlike (7b), this last assertion is in de Rham cohomology;
both are needed to compare the varying filtrations.

Write omega_A for the marked target period. Since kappa
preserves both NS and U, omega_A lies in T tensor A and
in the same U-eigenspace as omega. Its eigenvalue is
theta, and theta+1 is nonzero: L006's cubic has value
1 at -1. Consequently (7) and Hodge functoriality give

\[
f_A^*\mu_A(\omega_A)=(1+\theta)p^*\omega_A
     \quad\hbox{in }F^2H^2(B_A).
\tag{8}
\]

The pullback by (6) identifies the one-dimensional F^2
line of S'_A with that of B_A. Its reduction is the
usual isomorphism on holomorphic two-forms for a point
blowup, so it remains an isomorphism over A by Nakayama
and Hodge base change. In cohomology its marked map is
the same p^*. Equation (8), its nonzero scalar and the
injectivity of p^* therefore force the period lines of
S'_A and S_A to agree, including the epsilon coefficient.

Infinitesimal K3 Torelli now gives xi=kappa, where xi is
the class of S'_A. Its needed form is elementary here:
contraction with the nowhere-vanishing omega is the
sheaf isomorphism T_S -> Omega_S^1, and the derivative
of the period line is the induced map on H^1. It is
injective. The same comparison can be checked directly
without choosing normalized generators for the period lines.
If eta is the class of B_A, let chi denote the induced
class of M_A and alpha the holomorphic representative of
mu(omega). Equations (7d) and the formal period derivative
give chi contracted with alpha = mu(kappa contracted with
omega) in H^1(M,Omega_M^1). A change of the chosen period
generator contributes only its F^2 component, so it does
not alter this (1,1) equality. Central identity (7) also
gives f^*alpha=(1+theta)p^*omega as holomorphic forms:
their cohomology classes agree, and the holomorphic-form
map to de Rham cohomology is injective on projective B.
Applying (7b) to the two maps, rather than assuming strict
compatibility of representatives, now gives

\[
\begin{aligned}
(1+\theta)p^*(\xi\mathbin{\lrcorner}\omega)
 &=\eta\mathbin{\lrcorner}f^*\mu(\omega)\\
 &=f^*\mu(\kappa\mathbin{\lrcorner}\omega)\\
 &=(1+\theta)p^*(\kappa\mathbin{\lrcorner}\omega)
 \quad\hbox{in }H^1(B,\Omega_B^1).
\end{aligned}
\]

Both map-motion corrections in this displayed chain are
bar-partial-exact by (7b). The last equality uses that
NS-fixed RM motion puts kappa contracted with omega in
the same T-eigenspace. This condition is imposed only
on kappa; xi is arbitrary until equality is proved.
Injectivity of p^* and contraction with omega gives
xi=kappa again. Equality of marked first-order deformation
classes permits an isomorphism S'_A -> S_A reducing to
id_S. Compose (6) with it. This identifies the two
factors; it was not assumed at the start.

**Recover only the punctured embedded family, then C.**
The separate critical audit of this passage on 2026-10-15 uses the
unchanged hypotheses above and the supporting sources below. It finds
no substantive error or stronger conclusion. The following details
make explicit the application at arbitrary extra blowup centres;
they do not assert an extension theorem for arbitrary subschemes.

Let Q contain q_1,q_2,q_3 and the finite images in S of all extra
blowup centres, including infinitely near centres. Write U=S\Q.
The open U_A of S_A is defined by its underlying topological open U;
no choice of moving sections through Q is needed. The preceding
blowdown and period arguments identify p_A^{-1}(U_A) with U_A.

First check the actual central subscheme. The opening local models
make Y_U a closed finite flat family of degree three, including the
nonreduced length-two fibres of C's branched projection and the
length-two diagonal crossings. Its Hilbert map h:U -> S^[3] agrees
with f p^{-1} on the dense distinct-support open: there a cycle of
three distinct points has a unique length-three subscheme. Both maps
are defined on reduced U and the Hilbert scheme is separated, so
they agree on all of U. More explicitly, the ideal of their equalizer
vanishes on a dense open and hence vanishes on the reduced source.
Thus central agreement is agreement of universal families, not merely
agreement of support cycles at collision points.

Pull back the actual relative universal family by f_A and restrict
to this open. By the defining points functor, [Stacks Section 44.2,
Tag 0B94](https://stacks.math.columbia.edu/tag/0B94), it is a closed
subscheme Z_U of U_A x_A S_A finite locally free of degree three over
U_A. Pullback preserves flatness ([Stacks Lemma 10.39.7, Tag
00HI](https://stacks.math.columbia.edu/tag/00HI)); since U_A is A-flat,
transitivity ([Lemma 10.39.4, Tag
00HC](https://stacks.math.columbia.edu/tag/00HC)) makes Z_U A-flat.
Its reduction is the actual Y_U just checked. The analytic statement
uses the proper flat universal family in the Hilbert/Douady functor,
as stated in Buchweitz--Flenner, *A Semiregularity Map for Modules and
Applications to Deformations*, arXiv:math/9912245v1 (31 December 1999),
[printed p. 49](https://arxiv.org/pdf/math/9912245v1#page=49), together
with the relative Hilbert framework above. There is no flat-image
claim over Q or on the image of f_A.

**The diagonal component and all extra punctures.** On
U\(F_+ union F_-), the central diagonal is an open-and-closed
component of the finite family. Idempotents lift uniquely through
the square-zero reduction ideal ([Stacks Lemma 10.32.6, Tag
00J9](https://stacks.math.columbia.edu/tag/00J9)). Its lifted summand
is a direct summand of the finite locally free algebra, hence locally
free; its central rank is one. Its unit map from O_{U_A} is an
isomorphism, since locally it is a map of free rank-one modules whose
reduction is an isomorphism. This proves that the component is the
graph of a map reducing to id. Because both factors are the same
S_A, subtracting id and dividing by epsilon gives an intrinsic
section v of T_S on this open. No sheet separation at an intersection
is inferred from idempotents.

At each point of (F_+ union F_-)\Q, use L009's same-factor coordinates
r=u_2-u_1, s=u_2+u_1, z=w_2-w_1. The two meeting sheets have central
ideal (z,rs); the third sheet is disjoint locally. A flat embedded
first-order lift has generators

\[
 z-\epsilon\alpha,\qquad rs-\epsilon\beta,
 \qquad \alpha,\beta\in O/(z,rs).
\]

This is L007's ideal parametrization, equivalently the non-lci-valid
Hom description of [Buchweitz--Flenner, Lemma 7.6, printed
p. 50](https://arxiv.org/pdf/math/9912245v1#page=50); no properness
assumption is needed for that description. On the diagonal away
from u=0 it gives

\[
 v={\beta_\Delta\over 2u}\partial_u
          +\alpha_\Delta\partial_w.
\]

Consequently v is a section of the *existing* bundle
T_S(F_++F_-) over S\Q, with possible simple poles only in the
base direction. Extend this section through each point of Q by
coefficientwise Hartogs in a local bundle frame. Algebraically use
[Stacks Lemma 15.24.18, Tag
0AVB](https://stacks.math.columbia.edu/tag/0AVB); analytically use
Lebl, *Tasty Bits of Several Complex Variables*, version 4.4
(31 May 2026), [Theorem 2.1.4 and Corollary 2.1.5, printed
pp. 49--50](https://www.jirka.org/scv/scv.pdf#page=49).
The smooth surface has complex dimension two and Q is finite, so
these are precisely isolated-point coefficient extensions. In
particular a point of Q on F_+ or F_- creates no additional pole:
the extension is first made in the twisted bundle, not in T_S.

Connected fibres and the projection formula make dpi(v) a section
xi of T_{P^1}(t_++t_-)=O_{P^1}(4). At all 21 finite nodal values,
including when the node belongs to Q, the extended v is regular:
these fibres are disjoint from the twisting fibres. In smooth surface
coordinates pi-t_0=xy at the node, dpi is zero there. Hence xi
vanishes at each of those distinct values and is zero. On each
intersection chart outside Q the displayed formula now gives
beta_Delta=0 and no polar part. Thus v is regular on S\Q and a
second Hartogs application, this time to T_S, makes it a global
holomorphic vector field. Contraction with the K3 two-form and
H^0(S,Omega_S^1)=0 imply v=0. This also treats extra centres at
ordinary smooth points and at the nodal fibres without losing any
of the zero-count constraints.

The actual relative diagonal is therefore contained in Z_U
scheme-theoretically, not just on its reduction. Indeed the image
of any local section of I_{Z_U} in O_{Delta_{U_A}} has zero reduction,
so belongs to epsilon O_{Delta_{U_A}}, naturally identified with
O_{Delta_U} by A-flatness. Its coefficient vanishes on the dense
open where the graph was selected. The smooth reduced surface U
has no nonzero regular (or holomorphic) function with that property.
Thus the image is zero everywhere on Delta_{U_A}. This argument
uses no family or containment over the omitted Q.

**Residual equations and flatness only where defined.** At the two
intersection curves outside Q, this containment forces the central
classes alpha and beta to be multiples of r in O/(z,rs). Changing
generators puts the actual ideal into L009's form

\[
 J_A=(z-\epsilon r a,\ r(s-\epsilon b)).
\]

Its colon by the actual diagonal ideal (z,r) is

\[
 J_A:(z,r)=(z-\epsilon r a,\ s-\epsilon b).
\]

To check the colon, first quotient by z-epsilon r a. The resulting
ring is A\{r,s,w\} (or its formal completion), the image of (z,r)
is (r), and that of J_A is (r(s-epsilon b)). Multiplication by r
is injective in this power-series ring over A. Cancelling r proves
the displayed equality. The residual equations have independent
central differentials dz and ds, so the relative coordinate change
(z,s) -> (z-epsilon r a,s-epsilon b) identifies the quotient locally
with A\{r,w\}; it is A-flat. This verifies the actual quotient,
not an assertion of flatness for arbitrary colons.

Away from the diagonal, its ideal is the unit ideal and the residual
is Z_U. Near points of the diagonal away from C the lifted component
is exactly the diagonal, so its colon is the unit ideal and the
residual is empty. These cases cover the whole punctured support:
C is smooth away from its three singular points over q_i. Colon is
intrinsic, so these local residuals glue to an A-flat embedded lift
C_{U,A} of C restricted to U x S. All q_i are omitted; no colon is
taken at a three-branch point for the flatness argument.

**Extend ideal parameters, then check their transitions.** Put
P=C intersect (Q x S). It is finite because g_0:W -> S is finite
and nu:W -> C is surjective; its preimage in W is finite as well.
The open restriction of C is C\P, even though the removed ambient
set Q x S has positive dimension. L008 identifies

\[
 N_C=\mathcal Hom(I_C,O_C)=\nu_*N_j,
\]

where W is smooth and N_j is already a rank-two vector bundle.
Consequently restriction of sections of N_C across P is an
isomorphism locally: pull to nu^{-1} of the neighbourhood, extend
bundle coefficients through its finitely many omitted points, and
push forward. Use the same Hartogs citations as above on W, not
normality or smoothness of C. This covers both ordinary points of
C over extra centres and its three non-lci double points.

Choose small smooth ambient charts V_i trivializing X_A=S_A x_A S_A
and reducing to the given charts of X=S x S. In each chart the
constant ideal I_C provides a reference flat lift. L007's formula
then identifies C_{U,A} on the puncture with a section phi_i of
N_C there. Extend it uniquely to phi_i on all of C intersect V_i.
For completeness, the reconstructed ideal consists locally of
f+epsilon g with f in I_C and g modulo I_C equal to phi_i(f).
Linearity makes it an ideal; its intersection with epsilon O_X is
epsilon I_C. Thus its quotient satisfies ker(epsilon)=epsilon M
and is A-flat by the square-zero case of [Stacks Lemma 10.101.6,
Tag 051K](https://stacks.math.columbia.edu/tag/051K). This uses the
full Hom module and imposes no lci condition.

On an overlap two ambient trivializations differ by
1+epsilon D_ij, with D_ij a regular ambient derivation. The
corresponding parameter difference is delta(D_ij), the everywhere
defined normal section obtained by restriction to I_C modulo I_C,
with the same sign convention as L007. This equality holds on the
puncture because the original ideals glue. Uniqueness of extension
in nu_*N_j forces the equality also at P. Hence the reconstructed
ideals glue in the actual X_A, independently of trivializations.
This is the transition check needed to extend a torsor of local
lift parameters; no global ambient trivialization is assumed.
The analytic construction is a coherent ideal on the compact
ambient deformation, and suffices directly for the allowed analytic
scope (with proper GAGA in the algebraic case).

We have recovered a flat embedded lift of C in the same
S_A x_A S_A. L008 therefore forces kappa in V_D, proving (1).
The central lift, all-source blowdown and marked period comparison
remain the earlier inputs; this audit verifies only the subsequent
punctured recovery. It finds no new exclusion or independent
construction and does not reopen the stopped resolved-lift recipe.

**The three permitted directions occur.** In the actual
Dickson family, the finite normalization maps and g
vary as in L008 and L042. The three fixed points at
infinity vary as sections, and L009's finite-order
averaging coordinates linearize their order-seven
action with constant weights. The norm determinants
therefore give the same relative ideal
(uv,u^3,v^3)^2 at each section. Blow up those sections
and the two tangent-axis sections on each first
exceptional divisor. Formula (2) principalizes the
relative norm ideal in the same charts.

Away from these sections the relative Y is finite flat
of degree three: its central family is S-flat there,
its Dickson-family embedded lift is flat by L009, and
the local flatness criterion gives flatness over the
deformed parameter surface. Thus the relative image
ideal is invertible there as well. The imported
blowup property gives f_A on the deformed nine-blowup
surface. Restriction to any tangent of that family
supplies every kappa in V_D. Together with (1) and
L008's dimensions this proves the exact threshold.

The [prior SPECIALIZE assessment](../drafts/literature/2026-10-03-resolved-parameter-hilbert-cube-deformation.md)
covers the unchanged target and the inspected map,
relative Hilbert-cube and blowup framework. The explicit
principalization, all-source application, period comparison
and punctured recovery are the geometry-specific difference.
No inspected theorem was a match for this full exclusion.
Classification is POTENTIALLY_NEW only in that limited
literature sense, with no certified originality claim.
The known framework is imported, not rediscovered.

## Mathlib

Coverage: **not checked** for the full resolved-parameter
exclusion, point-blowup deformation maps, incidence
period comparison or their combination. Iacono's
Theorem 5.5 and Remark 5.12 equation (7) and Stacks
Tag 0806, directly linked above, match the imported
framework portions. Ekedahl--Skjelnes' [Corollary 7.28,
Annals 179 (2014), pp. 836--837](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=32)
supports the relative Hilbert-cube/blowup identification.
None is a Mathlib theorem or a match for (1).
Iacono's Theorem 5.5/Remark 5.6 supplies the general
map-motion cocycle; Lemma 4.7 supplies its strict-contraction
counterpart, not a complete match for (7b). The linked
Fiorenza--Manetti statements supply the Artinian Hodge
filtration and derivative, not the marked incidence (7d).
The linked Fulton statement supplies the central leading
character. Cartan homotopy, the Atiyah-class definition of
the holomorphic Chern character and Chern--Weil transgression
are supporting standard inputs; (7b)--(7d) give their
specific application including collisions and dual numbers.
This critical calculation reproduces the known framework
with its previously implicit correction made explicit;
it is no certified new discovery. Excision for point-blowup
cohomology, the local flatness criterion and Nakayama remain
supporting inputs. No library absence or general Hodge
resolution is asserted.

The 2026-10-15 residual audit specializes the cited Hilbert/Douady,
idempotent, embedded-Hom, flatness and Hartogs inputs. Full matching
Mathlib coverage remains **not checked**. The explicit application above
is classified REPRODUCTION; no stronger result or certified originality
is claimed.
