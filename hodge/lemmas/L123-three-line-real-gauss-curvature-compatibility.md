# L123 — Real Gauss-Codazzi compatibility for three quaternionic lines

## Hypotheses

Let (V,g,I,J,K) be a positive quaternionic Hermitian vector space of
quaternionic dimension n>=2. Let P_1,P_2,P_3 be distinct quaternionic
lines whose quaternionic span W has dimension two. By a hyperkähler
algebraic curvature tensor we mean a real algebraic Riemannian curvature
tensor with the hyperkähler holonomy symmetries. No curvature derivative,
local metric realization, completeness or local symmetry is assumed.

For application retain L118's entire conditional setting: identical
marked projective K3 factors with common metric g_B and ordered triple,
real product polarization Omega, rank-two locally free Omega-polystable
F, integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D. Its opposite map
has quaternionic differential, is parametrically totally geodesic, and
pulls back the normalized moduli metric to c g_B, c=2lambda,
1<lambda<5/4. L121, using L120's normalization, makes tangent lines at
distinct coincident preimages distinct. Suppose three such points have
line span W of quaternionic dimension two. The actual ambient dimension
is n=39. The three actual source curvature tensors and the angles are
unknown inputs; their values are not freely assigned by this application.

## Conclusion

There is an exact real linear compatibility equation (4) below for the
three prescribed intrinsic curvature tensors, including every normal
component required by pointwise Gauss-Codazzi. It handles arbitrary
angles with the positive metric retained. In coordinates specified below,
write its metric as [[a,Q],[Q*,b]], where Q=s Id+V_0 is quaternionic,
V_0*=-V_0, V_0^2=-r^2 Id, a,b>0 and ab>s^2+r^2. Then:

| Configuration | Independent real equations on the three quartics | Allowable triples | Compatible tensors on W |
| --- | ---: | ---: | ---: |
| Not a=b=-2s | 5 | 10 | 11 |
| a=b=-2s and r>0 | 4 | 11 | 12 |
| a=b=-2s and r=0 | 0 | 15 | 16 |

For any allowable triple its extensions on W form a real affine line.
On V the same restriction range holds: orthogonal extension supplies
solutions, and the additional homogeneous kernel is given in (7).
For n=39 its real dimension is 1,662,817. This reduction does not assume
that W is invariant under an actual ambient curvature operator.

An explicit real compatible tensor has unit-frame restrictions
(A,A,A/2), all nonzero, with A(z_0,z_1)=z_0^2 z_1^2. Thus a universal
pointwise exclusion based only on all three source curvatures being
nonzero fails. The exact equation can still test the actual tensors if
those tensors and angles become available. Global K3 nonflatness gives
no pointwise input. Neither an actual collision, a metric germ, F, an
algebraic cycle nor transverse transport is constructed or excluded.

This is a bounded REPRODUCTION/specialization of the assessed curvature
and submanifold framework, with an explicit interpolation calculation;
no originality is claimed. The separate critical audit below preserves the
formula and the bounded route stop, without a stronger geometric conclusion.

## Proof

**Imported framework and scope.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-18-opposite-collision-gauss-curvature.md`
and its exact COVERED_TARGET. The primary algebraic input is
Kramer--Semmelmann--Weingart, *Eigenvalue Estimates for the Dirac Operator
on Quaternionic Kaehler Manifolds*,
[dg-ga/9703021v1, Section 3, Lemma 3.5, equations (3.10)--(3.13), PDF
pp. 10--11](https://arxiv.org/pdf/dg-ga/9703021v1#page=10), with the
complete proof and Lemmas 3.3--3.4 covered by that assessment. For
hyperkähler curvature, including quaternionic dimension one, use the
direct formula in Rozansky--Witten,
[hep-th/9612216v1, Section 2.1, equation (2.4), PDF pp. 9--10](https://arxiv.org/pdf/hep-th/9612216v1#page=9).
Positive quaternionic reality and symplectic lowering are as in
Semmelmann--Weingart, *Vanishing Theorems for Quaternionic Kaehler
Manifolds*, [math/0001061v1, Section 2, Lemma 2.3, equations (13)--(15),
PDF pp. 5--9](https://arxiv.org/pdf/math/0001061v1#page=5).
These results are imported, not reproved. In particular no
quaternionic-Kähler n>=2 Einstein argument is applied to the source.

In their notation V_C=H tensor E, where H has complex dimension two and
E has complex dimension 2n, both with positive quaternionic structures.
Hyperkähler algebraic curvature corresponds to S in Sym^4 E*, fixed
by its quaternionic antilinear involution rho. Up to the same fixed
nonzero convention scalar on ambient and source, the lowered curvature
on decomposable vectors is epsilon_H(h_1,h_2) epsilon_H(h_3,h_4)
S(e_1,e_2,e_3,e_4). This is the curvature-module identification, not a
claim about the existence of a metric realizing an arbitrary S.

A quaternionic line P gives a quaternionic complex two-plane L in E.
Its normal complement is the corresponding Hermitian and symplectic
orthogonal complement L^perp. By the displayed tensor formula, the
complete vanishing R(P,P,P,P^perp)=0 is equivalent to

    S(L,L,L,L^perp)=0.                                      (1)

Indeed complexification allows independent h_j, and the two epsilon_H
factors can be chosen nonzero. Restriction to L gives the intrinsic
curvature under the same convention. Import the named Gauss and Codazzi
equations in Chen, *Riemannian Submanifolds*,
[Section 3.1, equations (3.1)--(3.7), especially the combined identity
(3.4), PDF pp. 14--15](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Chen_Riemann_Submanifolds.pdf#page=14).
For zero second fundamental form their full vector-valued identity is
exactly intrinsic matching and (1). Skew-adjointness also makes
R(P,P) preserve the normal space once it preserves P. No separate
prescribed normal connection or differential curvature data are part
of this pointwise question. The space-form existence theorem in that
source is not applied.

**Compression and extension.** Split E=E_W orthogonal-direct-sum E_U,
with complex dimensions four and 2n-4. Restricting S to E_W retains
all algebraic symmetries and reality. For each L_i subset E_W, (1)
implies its corresponding normal equation inside E_W. Conversely any
real symmetric quartic on E_W satisfying those equations extends by
orthogonal projection in every slot to E; the extension vanishes
whenever a slot is in E_U. It therefore satisfies the full (1) in E
and has the same intrinsic restrictions. This proves equality of the
restriction ranges. It uses algebraic orthogonal compression, not an
assumption that the actual ambient curvature preserves W.

**Coordinates retain the metric.** Set U=H as a quaternionic line,
with its standard positive metric. Choose quaternionic-linear
isomorphisms phi_1:U -> P_1 and phi_2:U -> P_2 so that P_3 consists
of phi_1(x)+phi_2(x). This is possible because projection of P_3 onto
either summand of W=P_1 direct-sum P_2 is an isomorphism: its kernel
would be an intersection of distinct quaternionic lines. In the
coordinates phi(x,y)=phi_1(x)+phi_2(y), the three lines are therefore
(x,0),(0,x),(x,x). This change is not asserted to be unitary.

The actual positive metric has quaternionic Hermitian matrix
[[a,Q],[Q*,b]], with a,b positive real scalars. Write
Q=s Id+V_0, Q*=s Id-V_0, V_0*=-V_0 and V_0^2=-r^2 Id. Positivity is
ab>s^2+r^2. Put

    t=a+b+2s>0,  C=Q/a,  D=Q*/b,
    H=(a Id+Q*)/t,  Id-H=(b Id+Q)/t.                      (2)

The squared scales of the three coordinate embeddings are a,b,t.
Projection onto P_1 sends (x,y) to (x+Cy,0); projection onto P_2
sends it to (0,Dx+y). Projection onto P_3 sends it to (z,z), where
z=Hx+(Id-H)y. These follow by pairing with all vectors in the respective
line. In particular the normal spaces are represented by
(-Cv,v), (u,-Du), and ((Id-H)u,-Hu). The last expression spans the
normal space: H and Id-H commute and sum to Id, and the parameter map
is injective. No pairwise angle has been discarded.

Fix I and write U_C's E-factor as C^2 with coordinates x=(x_0,x_1).
Its quaternionic structure can be written j(x_0,x_1)=(-bar x_1,bar x_0).
All maps in (2) commute with j. The real quartic space
V_4=(Sym^4(C^2)*)^rho has real dimension five, where
rho f(x)=overline{f(jx)}. The fourth power makes rho^2=1.
The same definition on (x,y) gives the real form of Sym^4 E_W*.

Use polynomial notation f(x)=S(x,x,x,x); derivatives below therefore
retain the factors of four. Denote the three restriction polynomials
by A(x), B(x), T(x), each in V_4. For a quaternionic-linear map L set
D_L f(x)=df_x[Lx]. This operator preserves V_4.

**Complete interpolation including normal components.** The first
normal equation says that the derivative of F(x,y) at (x,0) in
(-Cv,v) vanishes. Its (3,1) bihomogeneous part must therefore be
dA_x[Cy]. The second equation similarly fixes the (1,3) part as
dB_y[Dx]. Consequently every solution of the first two equations is
uniquely of the form

    F(x,y)=A(x)+dA_x[Cy]+K(x,y)+dB_y[Dx]+B(y),             (3)

where K is bihomogeneous of degree (2,2). There are nine complex
coefficients in K before reality. Conversely (3) satisfies both full
normal equations; the other bihomogeneous parts have too many vanishing
slots to contribute to these first derivatives.

On the diagonal, define
T_0=T-A-B-D_C A-D_D B. The required restriction is K(x,x)=T_0(x).
Normal vanishing for P_3, together with this restriction, says
that dF_(x,x)[u,v]=dT_x[Hu+(Id-H)v]. This is equivalent to

    d_1 K_(x,x)[u]=U(x;u),
    U(x;u)=dT_x[Hu]-dA_x[u]-d^2 A_x[u,Cx]-dB_x[Du],

and K(x,x)=T_0(x). Once these hold, the derivative in the second
argument follows by differentiating F(x,x)=T(x); hence no normal
component has been omitted.

The map K -> d_1 K_(x,x)[u] from the nine-dimensional (2,2) space
to Sym^3(C^2)* tensor (C^2)*, of dimension eight, is surjective and
has kernel C Delta^2, Delta=x_0 y_1-x_1 y_0. Here is an explicit
verification. Write K=sum_{i,j=0}^2 k_ij x_0^(2-i)x_1^i
 y_0^(2-j)y_1^j. For total k=i+j the u_0 coefficient is
sum_{i+j=k}(2-i)k_ij and the u_1 coefficient is sum_{i+j=k}i k_ij,
with their respective cubic monomials. Setting all coefficients zero
kills k_00,k_01,k_10,k_12,k_21,k_22 and leaves
k_02=k_20 and k_11=-2k_20. This is exactly Delta^2. Rank-nullity gives
surjectivity. All operations commute with rho, so averaging K with
rho K supplies a real solution for real U. Delta^2 is fixed by rho;
the real kernel has dimension one.

Euler homogeneity in the first variable gives U(x;x)=2K(x,x).
Thus both required conditions on K hold if and only if U(x;x)=2T_0.
Using dA_x[x]=4A and d^2A_x[x,Cx]=3dA_x[Cx], this is precisely

    (D_H-2 Id)T=(2 Id+D_C)A-(2 Id+D_D)B.                  (4)

This proves necessity and sufficiency over the real form, as well as
the one-real-dimensional extension fibre. In particular imposing only
four-tangent contractions would miss (4).

**Rank for every positive metric.** On V_4, scalar multiplication
alpha Id induces D_(alpha Id)=4alpha Id. The three operators in (4)
are therefore

    D_H-2 Id = [2(a-b)/t] Id - D_(V_0)/t,
    2 Id+D_C = [2(a+2s)/a] Id + D_(V_0)/a,
    2 Id+D_D = [2(b+2s)/b] Id - D_(V_0)/b.                (5)

The standard positive inner product on Sym^4 induced from C^2 is
invariant under Sp(1). On its real form D_(V_0) is skew-adjoint,
since V_0 generates that compact group. Thus a real nonzero scalar
multiple of Id plus any multiple of D_(V_0) is invertible: its
inner product with a vector in its kernel gives the scalar times
the squared norm. Unless a=b=-2s, at least one scalar coefficient
in (5) is nonzero. That corresponding block makes the compatibility
map V_4^3 -> V_4 surjective, with rank five.

If a=b=-2s, then t=a and (4) reduces to

    D_(V_0)(A+B+T)=0.                                   (6)

For r=0 it imposes no condition. For r>0, a unitary eigenbasis for
V_0 has eigenvalues ir,-ir. On binary quartics the eigenvalues of
D_(V_0) are 4ir,2ir,0,-2ir,-4ir. Its complex kernel has dimension
one; the real form is preserved, so its real kernel also has dimension
one and its real rank is four. The compatibility map has that rank
because A+B+T ranges over V_4. This proves every case of the table.
The space of allowable triples has dimension 15 minus that rank;
adding the one-dimensional K kernel gives 16 minus that rank.
These exceptional conditions are derived from the positive matrix,
not from an assumed real-angle normal form. A common quaternionic
coordinate change rotates V_0 and scales a,b,s,r together and does
not alter the cases.

**All remaining ambient components.** To describe the entire space,
let m=2n-4 and let J_3 be the cubics on E_W vanishing on all three
L_i. The additional kernel beyond extension from E_W is the real form
of

    (J_3 tensor E_U*)
    direct-sum (Sym^2 E_W* tensor Sym^2 E_U*)
    direct-sum (E_W* tensor Sym^3 E_U*)
    direct-sum Sym^4 E_U*.                               (7)

Indeed only the term with exactly one E_U slot can enter (1), and
its remaining cubic must vanish on every L_i; terms with at least
two E_U slots never enter (1) or intrinsic restriction. These are
all components of a quartic with zero restriction to E_W. To compute
J_3, restriction to the coordinate lines first kills the (3,0) and
(0,3) parts. The remaining (2,1),(1,2) parts have total dimension
twelve. Diagonal evaluation surjects onto the four-dimensional binary
cubics, since every cubic monomial occurs as a (2,1) monomial on the
diagonal. Its kernel therefore has complex dimension eight. Each
summand of (7) has the total even-degree quaternionic real structure,
whose fixed real dimension equals its complex dimension. Thus (7)
has real dimension

    8m+10 binom(m+1,2)+4 binom(m+2,3)+binom(m+3,4).

For m=74 this is 1,662,817. The full solution space for a fixed
allowable triple has dimension 1 plus this number. This description
retains possible couplings to E_U rather than declaring W invariant.

**Actual source scaling.** Let k_i in V_4 encode the original K3
metric's curvature at the three points, in unit quaternionic frames
matched to phi_i/sqrt(a_i), where a_1=a,a_2=b,a_3=t. These matching
frames use the actual quaternionic isometry df_i/sqrt(c), c=2lambda.
For a constant metric rescaling c g_B, the connection is unchanged,
the covariant four-tensor becomes c R_(g_B), and its coefficients in
unit frames become k_i/c. Since phi_i has length scale sqrt(a_i),
its four-slot restriction polynomial is therefore

    A=a^2 k_1/c,  B=b^2 k_2/c,  T=t^2 k_3/c.              (8)

For example df_i applied to an original unit frame equals
sqrt(c/a_i) phi_i; four-slot Gauss matching gives exactly (8).
The same universal curvature-module convention is used on each side.
The common factor 1/c cancels in (4), but the a_i^2 factors and the
actual frame identifications cannot be dropped. There is no equality
assumption on k_1,k_2,k_3 and no independently chosen metric at the
three image branches.

**Discriminating nonzero witness.** Choose a=b=1,Q=0, so t=2,H=Id/2
and C=D=0. Equation (4) becomes A=B. Take the nonzero rho-real
quartic A(x)=x_0^2 x_1^2 and

    F(x,y)=A(x)+A(y).

This tensor is rho-real and has zero normal derivatives on the two
coordinate lines. On the diagonal its derivative in (u,-u) is zero,
so all normal equations hold. Its coordinate restrictions are
(A,A,2A); the third unit embedding is (x,x)/sqrt(2), making the unit
restrictions (A,A,A/2). All are nonzero. Extension by zero in E_U
retains this example in quaternionic dimension 39. With the fixed
c of L118, source unit polynomials (cA,cA,cA/2) would meet the
pointwise equations; this is a formal compatibility example, not an
assignment to the actual K3 points. In fact the exceptional real
case in the table permits arbitrary triples, but this simpler witness
already meets the stopping test.

The universal nonzero-curvature exclusion is therefore parked.
The exact conditional test (4), (8) remains available; without actual
angles and tensors it gives no collision exclusion. Differential
Bianchi, extension along branches, metric realization, the global
family F, image gluing and transverse transport are not supplied by
an algebraic curvature tensor. L122 and ATTEMPTS/070 concern a different
flat gluing inference and are not used as premises here. ATTEMPTS/047's
compatible index mechanism is not reopened.

**Verification and qualifications.** The proof above is uniform in all
positive metric matrices. The independent exact rational script
`scripts/opposite-curvature/check_three_line_curvature.py` builds the
full 24-by-35 normal-condition matrix and 15-by-35 restriction matrix
in four configurations: orthogonal equal scales, generic nonorthogonal,
exceptional with r>0, and exceptional with r=0. Their normal ranks are
24,24,23,19; their restriction-range ranks are 10,10,11,15. In each
case the full first-jet rank is 34 and the proposed equation annihilates
the entire normal kernel. It also checks the mixed interpolation rank,
the determinant-square kernel and the real all-nonzero witness exactly.
Reproduce with `python3 scripts/opposite-curvature/check_three_line_curvature.py`.
The full matrices and results are saved in
`scripts/opposite-curvature/three_line_curvature_certificate.json`.
These finite checks support the proof; samples do not prove the uniform
rank classification. The initial SymPy implementation could not run
because that package was absent; the completed script uses only Python's
standard-library rational arithmetic and has no such dependency.

**Separate critical audit, 2026-10-18 (step 367).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-18-three-line-real-curvature-critical-audit.md`.
This is RESEARCH / EXPLORATION / REPRODUCTION, task type proof_audit.
It reuses the primary curvature-module and combined Gauss-Codazzi
coverage cited above, and retains L118 and L121 as conditional inputs
(L120 enters through L121). Their proofs are not re-audited here. No
substantive error or stronger exclusion was found. The checks below
verify the specialization rather than reprove the imported theorems.

First, the tensor formula tests the full normal condition. Upon
complexification, each quaternionic tangent line is H tensor L_i and
its real orthogonal complement complexifies to H tensor L_i-perp.
Choosing the H slots with both alternating factors nonzero recovers
every coefficient S(e_1,e_2,e_3,n). Conversely their vanishing kills
every three-tangent/one-normal curvature component. Symmetry in the
E slots and polarization over C make the diagonal cubic test
S(x,x,x,n)=0 equivalent to all three independent tangent slots. Thus
polynomial first derivatives lose no normal equation. Positive
orthogonal projection onto E_W commutes with its quaternionic structure;
restriction and extension preserve the real curvature module. Necessity
inside W and sufficiency by extension are separate arguments, so no
curvature-invariance of the actual W has entered.

The graph metric and all three projections also survive direct pairing.
For example pairing (u,u) with (x-z,y-z) gives the operator
(a+Q*)x+(Q+b)y-tz, hence the stated H. Its normal parameter
((1-H)u,-Hu) lies in the kernel because H commutes with 1-H;
if both entries vanish their difference is u, proving injectivity.
The first two normal tests fix exactly the (3,1) and (1,3) coefficients
in (3). At the diagonal their first-variable derivatives are respectively
d^2 A_x[u,Cx] and dB_x[Du], with no extra dA_x[Cu]: Cy is independent
of x until after this differentiation. This order of operations is
essential to the coefficients in (4).

Here is an independent coefficient check of the interpolation. In the
map K -> d_1K_(x,x)[u], the total-index-zero and total-index-four groups
force k_00=k_22=0 in the kernel. The two equations at index one are
2k_01+k_10=0 and k_10=0; those at index three are k_12=0 and
k_12+2k_21=0. At index two they are 2k_02+k_11=0 and
k_11+2k_20=0. The sole remaining polynomial is a multiple of
(x_0y_1-x_1y_0)^2. Thus the nine-to-eight map is onto. The induced
antilinear involution on its target acts on all four argument slots;
it squares to one and intertwines the map. Averaging any complex
preimage therefore proves real surjectivity, rather than merely
assuming that a complex solution is real. The determinant square is
itself fixed. Euler in the first variable gives 2K(x,x)=U(x;x).
Substitution gives the two sides

    U(x;x)=D_H T-4A-3D_C A-D_D B,
    2T_0=2T-2A-2B-2D_C A-2D_D B.

Their equality is exactly (4), including the negative B block. Once
it holds, Euler recovers the prescribed diagonal value; differentiating
that value then recovers the second-variable derivative. This proves
both directions of the full real compatibility claim.

For the rank test, a block alpha Id+beta D_(V_0) with alpha nonzero
is invertible on the real five-space, by taking its inner product with
a kernel vector. The three alpha coefficients in (5) vanish together
if and only if a=b=-2s. In this exceptional case t=a and the signs in
(4) give D_(V_0)(T+A+B)=0. For r>0 the complex eigenweights are
4ir,2ir,0,-2ir,-4ir; invariance of the real form makes the real kernel
one-dimensional and rank four. For r=0 the equation is zero. Positivity
still requires r^2<3a^2/4 in the exceptional case; both r=0 and permitted
r>0 occur, so neither exceptional row is vacuous. The restriction
ranges are consequently 10,11,15 and the corresponding tensor spaces
on W have dimensions 11,12,16. The argument covers every positive
metric, not merely the rational sample matrices.

For the ambient kernel, decompose by degree in E_U. Degree zero is
already the W problem. Degree one contributes a cubic on E_W for each
external covector. Normal testing requires that cubic to vanish on each
L_i; no additional mixed external equation arises because three slots
are tangent to L_i. The coordinate restrictions remove eight of the
twenty cubic coefficients; diagonal evaluation on the remaining twelve
has rank four. Thus J_3 has dimension eight. Although J_3 alone has an
antilinear quaternionic structure squaring to minus one, its tensor
with E_U* has square plus one. All other summands in (7) likewise have
even total degree and fixed real dimension equal to complex dimension.
For m=74 their dimensions are 592,27750,281200,1353275, respectively,
with total 1662817. The additional one-dimensional W kernel gives
1662818 for each nonempty full ambient restriction fibre. This neither
sets actual external curvature components to zero nor assumes that
those components vanish geometrically.

Finally let e be an original source unit quaternionic frame and choose
it so df_i(e)/sqrt(c)=phi_i/sqrt(a_i). Constant rescaling to c g_B
leaves the connection unchanged and multiplies the covariant curvature
by c. Four-slot Gauss then gives

    (c/a_i)^2 S|_(phi_i) = c k_i,

in the common curvature-module convention. Hence S|_(phi_i)=a_i^2 k_i/c,
exactly (8). The frame identification is part of this statement; it does
not equate tensors at different source points. For the proposed witness,
j sends each binary monomial x_0^2 x_1^2 to itself after conjugation.
The product sum A(x)+A(y) has no axis normal derivatives, and its
entire diagonal normal derivative is dA_x[u]-dA_x[u]=0. The diagonal
unit parametrization contributes (1/sqrt(2))^4, giving A/2. The three
nonzero unit restrictions are therefore real and obey all normal
conditions, not merely the four-tangent Gauss contractions.

The standard-library verification script was read and rerun. It builds
the full polynomial normal and restriction matrices, computes exact
rational ranks, and tests the compatibility relation on the entire
normal kernel by row-span inclusion. Its normal ranks 24,24,23,19 and
restriction ranks 10,10,11,15 meet the required values; interpolation,
real witness and normal-component checks all pass, with an empty failure
list. The regenerated certificate is
`scripts/opposite-curvature/three_line_curvature_certificate.json`.
The exact arithmetic is supporting evidence; the preceding uniform
argument is what verifies arbitrary angles and the real exceptional
cases. No selected matrix preview is used as a proof.

ATTEMPTS/071's stop is retained solely for universal exclusion based on
nonzero pointwise source curvature. Actual source tensors, their matched
frames and collision angles remain unknown. No differential Bianchi
specialization, extension along branches, metric realization, F existence,
image gluing, collision emptiness or transverse transport follows. The
universal primitive Hodge gap is unchanged. This successful scoped audit
is not an additional mathematical advance or an originality claim.

## Mathlib

Full matching coverage for the real hyperkähler curvature module,
three-line normal-condition interpolation, or this specialization has
not been checked. No absence claim is made. The named curvature and
Gauss-Codazzi inputs above are imported from the precisely cited primary
sources; the elementary interpolation and rank proof are written here.
