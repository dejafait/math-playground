# L183 — Effective cubic residual retraction and a quartic pairing

## Hypotheses

Use L181–L182's fixed-mesh SU(2) expansion, relative box (-4,4)^4,
admitted even N with a=8/N, straight direction-1 lower-rooted forest,
complete displacement and both actual L010 probes at tau=1/16.
All physical faces, normal end edges and constant axial modes remain.
The small-coupling expansion precedes refinement. Inner products and
adjoints are in ordinary dimensionless full-link coordinates, with
three colors and bracket [v,w]=-v cross w.

Use L182's notation D, L, P, S, R=1-D Phi. In particular
S=P(L+DD^T)^(-1)P, LS=SL=P, and z has three independent colors
with one-color covariance S. Vertex potentials, including Phi z,
are set to zero at every boundary vertex. Let I=I_F and pi=pi_F.
Use L018's full symmetric residual matrix A, which satisfies AD=0,
and its restricted A_F=I^T A I. All maps below act identically on
colors. Write script R_3 and script S_3 for L156's full cubic
residual and action; their quadratic polynomials are respectively
<z,Az> and <z,Lz>/2. Both residual insertion subtractions are included.
Their restrictions are r_1 and S_3 of L181.

Let F_(i,3) be L182's complete full-coordinate cubic flowed numerator,
including its observable jet and quadratic flow integral, and B_i its
full quadratic matrix. Thus B_i D=0. Define

\[
 t(z)=2SAz,\quad \phi=\Phi z,\quad \psi=\Phi t(z),\qquad
 b(z)=\tfrac12[z,q\phi]-\tfrac14[D\phi,q\phi],             \tag{1}
\]

where (q phi)_e=phi_tail+phi_head. The quadratic map b is defined on
all full-link fields. Write d b(z)[v] for its directional derivative,
distinct from the incidence matrix D, and set

\[
 \begin{split}
 \rho_H(z)&=\mathcal R_3(z)-\mathrm d\mathcal S_3(z)[t(z)],\\
 W(z)&=P\,\mathrm d b(z)[t(z)],\\
 J_i(z)&=2\langle B_i z,b(z)\rangle,\qquad
 \widehat F_i(z)=F_{i,3}(Rz)=F_{i,3}(z)+J_i(z).
 \end{split}                                                \tag{2}
\]

The subscript H in rho_H labels this explicitly defined polynomial;
it asserts neither a nonlinear Hodge-gauge measure nor forest invariance.

## Conclusion

L181's original effective forest residual obeys, for every z in im P,

\[
 \boxed{\rho(\pi Rz)=\rho_H(z)-\langle Lz,W(z)\rangle.}     \tag{3}
\]

The terms 2<Az,b(z)> from retracting the residual and from differentiating
the retracted action cancel exactly. The remaining vector field is

\[
 \begin{split}
 W(z)=P\{&\tfrac12([t,q\phi]+[z,q\psi])\\
         &-\tfrac14([D\psi,q\phi]+[D\phi,q\psi])\}\
      ={}&\tfrac12P\bigl([t,q\phi]+[Rz,q\psi]\bigr).
 \end{split}                                                \tag{4}
\]

In particular the variation psi=Phi t of the prefix is essential.
All prefixes in (4) are the actual pinned ones, not independent noise
or a bulk continuation across the upper face.

This quadratic vector field has zero divergence on the co-closed
three-color space. Consequently the joint group and its gradient-probe
part have the exact finite identities

\[
 \boxed{G_{i,a}=\mathbb E_S[\widehat F_i\rho_H]
                 -\mathbb E_S[\mathrm d\widehat F_i(z)[W(z)]],}
                                                               \tag{5}
\]
\[
 \boxed{\mathbb E_S[J_i\rho(\pi Rz)]
   =\mathbb E_S[J_i\rho_H]
    -2\mathbb E_S\{\langle B_i W,b\rangle
                   +\langle B_i z,\mathrm d b(z)[W]\rangle\}.}
                                                               \tag{6}
\]

The last expectation in (6) is a quartic polynomial involving only
final-time B_i, the actual pinned prefix Phi (including its compositions)
and t=2SAz. The contraction
with Lz has removed a covariance through LS=P, rather than estimating
it by a norm. It has no remaining flow-time integration. Formula (5)
also retains the full flow dependence in F_(i,3) and its derivative.

This establishes a finite signed reduction only. No O(a^-3) bound,
finite scaled limit, vanishing, actual-probe coefficient, or bound
||rho||_2=O(a^-2) follows here. In particular (6) retains both its
sextic expectation E[J_i rho_H] and its quartic expectation with their
signs; neither is shown negligible. The co-closed probe's zero-time
flow endpoint, independent f_(i,2),r_0 contribution, finer asymptotics,
finite matching, reflected error <=c_box/2 and continuum/infrared
requirements remain open. This is local reproduction of the existing
gauge identity and finite Gaussian integration by parts, not a claimed
advance beyond the sources checked.

## Proof

### 1. Lift the original tilt direction in its original order

L182(8) gives C=R S R^T=I Sigma_F I^T. Since AD=0 and A is symmetric,
AR=A and R^T A=A. For x=pi Rz, I x=Rz, and hence

\[
 \begin{split}
 I(2\Sigma_F A_F x)
 &=2 C A Rz
 =2 R S R^T A Rz
 =2 R S A z=R t(z).                                       \tag{7}
 \end{split}
\]

Every equality is an identity of full finite matrices including forest
rows and physical end edges. This is not a commutation of A with S
and does not replace the forest covariance by S. It identifies the
lifted vector of the *original* forest derivative. In particular

\[
 \rho(\pi Rz)
  =\mathcal R_3(Rz)
      -\mathrm d\mathcal S_3(Rz)[R t(z)].                  \tag{8}
\]

The derivative here holds t(z) fixed at its value at z. It is a
first directional derivative, not a derivative of t itself.

### 2. Retract both complete invariant cubics before subtracting

L156 proof section 1, equation (4), applies to any of its full
pinned-gauge-invariant cubic jets with quadratic matrix M satisfying
MD=0. Integrating that identity from z to z-D Phi z, with Phi z
held fixed during that integration, gives precisely

\[
 \mathcal F_3(Rz)=\mathcal F_3(z)+2\langle Mz,b(z)\rangle.
                                                               \tag{9}
\]

This is L182's integration argument with the same coefficients and
bracket convention. It holds as a polynomial identity for every full
z. Apply (9) to M=A and M=L/2:

\[
 \mathcal R_3(Rz)=\mathcal R_3(z)+2\langle Az,b(z)\rangle,
 \qquad
 \mathcal S_3(Rz)=\mathcal S_3(z)+\langle Lz,b(z)\rangle.
                                                               \tag{10}
\]

These are the complete residual and action, so no separate gauge
invariance of an individual force/clover summand is assumed.
Differentiate the second polynomial identity at z in a fixed direction
v. R is linear, while b varies with both z and Phi z, so

\[
 \mathrm d\mathcal S_3(Rz)[Rv]
 =\mathrm d\mathcal S_3(z)[v]
     +\langle Lv,b(z)\rangle+\langle Lz,\mathrm d b(z)[v]\rangle.
                                                               \tag{11}
\]

Now substitute v=t(z). Since PA=A and LS=P,
Lt=2LSAz=2Az. Subtracting (11) from the first identity of (10) proves
(3): the two 2<Az,b> terms cancel with their exact factors. Since
Lz is co-closed, inserting P on d b does not change the pairing.

Differentiating (1) explicitly yields the first formula of (4),
including both appearances of psi. To check its shorter second form,
for any two pinned vertex fields phi,psi expand the endpoints on each
edge. Antisymmetry of the bracket gives the exact product identity

\[
 [D\psi,q\phi]-[D\phi,q\psi]=2D[\psi,\phi].              \tag{12}
\]

The vertex bracket vanishes on the boundary, so P annihilates the
right side with all normal end edges retained. The two quarter terms
therefore combine under P to -[D phi,q psi]/2. Adding this to
[z,q psi]/2 gives [Rz,q psi]/2 as claimed. This is not a boundary
summation with an omitted endpoint.

### 3. Divergence and Gaussian integration by parts

Choose a real orthonormal basis of im P in link space, and tensor it
with the three color axes. In these coordinates every component of
W is a linear combination of terms

\[
 \epsilon_{cde}\,z_r^d z_s^e
\]

whose coefficients depend only on link indices: P, Phi, D, q and
2SA are all color diagonal. Differentiating its output-color-c
component with respect to an input of the same color sets either
d=c or e=c. Both coefficients vanish by antisymmetry. Thus every
diagonal color derivative is zero and div_(im P tensor R^3) W=0.
This argument remains valid for a nonlocal link matrix or singular
full-space covariance. It does not assume spatial locality of W.

The Gaussian with covariance S is nondegenerate on im P, where its
inverse is L. For any polynomial g, ordinary finite-dimensional
Gaussian integration by parts on that space gives

\[
 \mathbb E_S[g(z)\langle Lz,W(z)\rangle]
   =\mathbb E_S[\mathrm d g(z)[W(z)]
                      +g(z)\operatorname{div}W(z)]
   =\mathbb E_S[\mathrm d g(z)[W(z)]].                    \tag{13}
\]

For clarity, the first equality follows by integrating each derivative
of g W_j exp(-<z,Lz>/2) over the co-closed coordinate space. Every
boundary term at infinity vanishes because g W_j is polynomial and
L is positive definite there. All Gaussian moments are finite at each
fixed mesh. No mesh-uniform assertion is needed for (13), and no
unweighted full-space inverse of L is used.

By L181 and L182, G=E_S[widehat F_i rho(pi Rz)]. Apply (13) to
(3) with g=widehat F_i to obtain (5). Apply it with g=J_i instead.
Differentiating J_i=2<B_i z,b(z)> in the fixed direction W(z) gives

\[
 \mathrm d J_i(z)[W(z)]
 =2\langle B_i W(z),b(z)\rangle
      +2\langle B_i z,\mathrm d b(z)[W(z)]\rangle,
                                                               \tag{14}
\]

which proves (6). This derivative does not differentiate W; its
separate divergence has already been accounted for in (13).
In particular the last term of (14) retains the further composed prefix:

\[
 \mathrm d b(z)[W]
 =\tfrac12([W,q\phi]+[z,q(\Phi W)])
   -\tfrac14([D(\Phi W),q\phi]+[D\phi,q(\Phi W)]).          \tag{15}
\]

Phi W is a quadratic vertex field with the same pinned endpoint rule;
it is not replaced by psi, zero or an independent field. The reduction
to degree four does not assert that these composed prefixes are bounded.
The first factor in each inner product of (14) and its second factor
have total degree four. No pairing or sign is dropped in passing
from the original sextic expectation to this quartic one.

### 4. Scope of the improvement and the unsuccessful norm test

The attempted L182(7) norm route requires an O(a^-2) bound on the
full forest residual for cubic boundedness of the gradient-probe part.
The identities above neither prove that norm bound nor replace it by
a uniform bound on rho_H or W. Their specific gain is cancellation
of the explicit quadratic-residual retraction terms and the exact
Gaussian removal of the Lz line in the remaining retraction correction.
The new expression still contains t=2SAz on rough inputs and its
pinned prefix psi. L028's smooth-mode consistency is applicable only
when a smoothed leg actually reaches A in the required order; it
cannot be assigned to t(z) for a rough Gaussian z. In particular
B_i cannot be commuted through W's multipliers, prefixes or A.

To use (6) for the cubic-scale test one must control its complete
signed expectations, retaining their contractions and all prefix
endpoints, or prove the missing residual norm by a separate valid
estimate. There is no such estimate in this lemma. The flow integral
in the first part of L182(6) also remains, with its zero-time endpoint.
A finite algebraic identity alone permits neither limit interchange
nor removal of any term in this response.

Verification is analytic: (7) checks the noncommuting lift order,
(11) differentiates both prefix slots, (12) checks the pinned product
identity edge by edge, and (13) retains the full Gaussian divergence.
No numerical or truncated-spectrum test is used to certify an exponent,
limit or actual-probe value.

### 5. Global Gaussian energy test: the available count misses cubic scale

The following bounded attempt concerns the entire quartic expectation
in (6), not either of its two summands separately. Put

\[
 Q_{i,N}=\mathbb E_S[\mathrm dJ_i(z)[W(z)]].                 \tag{16}
\]

L182 proves that J_i is pure third Gaussian chaos and
||J_i||_2<=C_i N. On im P, S has inverse L. Cauchy--Schwarz with
these two inverse metrics, first pointwise and then in probability,
therefore gives

\[
 |Q_{i,N}|\le
 (\mathbb E_S\langle\nabla_P J_i,S\nabla_P J_i\rangle)^{1/2}
 (\mathbb E_S\langle W,LW\rangle)^{1/2}
 =\sqrt3\,\|J_i\|_2
 (\mathbb E_S\langle W,LW\rangle)^{1/2}.                  \tag{17}
\]

Here grad_P differentiates only on im P. To justify the last equality
without a nonsingular full-space covariance assumption, integrate
the divergence of J_i S grad_P J_i against the Gaussian on im P.
It yields the expectation of
J_i(z dot grad_P J_i-Tr(S Hess_P J_i)). The first term is 3J_i^2
by cubic homogeneity. The Hessian contraction vanishes: every internal
pair in J_i sets two colors equal in its alternating color tensor,
as proved in L182. Polynomial Gaussian integration by parts is valid
on this finite-dimensional space. Thus (17) is the usual third-chaos
energy identity specialized to the actual correlated prefix polynomial.

For this particular count only, import L020(11)'s full residual form
bound. Its whitening is exactly Sigma_H^(1/2) A Sigma_H^(1/2):
the factors A=a^2 N_a and Sigma_H=a^-2 Delta_phys^-1 cancel.
Since A=PAP and P commutes with Sigma_H, restriction to im P gives
||S^(1/2) A S^(1/2)||<=C N. Consequently the actual tilt t=2SAz obeys

\[
 \operatorname{Cov}(t)=4SASA S\le C N^2 S.                \tag{18}
\]

Indeed the left side is S^(1/2)(2S^(1/2)AS^(1/2))^2 S^(1/2).
This is a positive covariance comparison, not a commutation of A and S
or a smooth-input estimate on t. Applying the actual Phi on both sides
also gives Cov(psi)<=C N^2 K, where K=Phi S Phi^T.

L026(11) gives (Sigma_H)_ee<=8 for every variable link, hence
S_ee<=8. L182(10), using L156's pinned-prefix domination, gives
K<=M tensor G_T. Its diagonal is at most C N: to check the only
additional scalar estimate, the normalized three-dimensional Dirichlet
waves have squared amplitude at most 8/N^3, and their dimensionless
eigenvalues are at least 4|k|^2/N^2. The shell max k_j=m has at most
3m^2 members, so

\[
 (G_T)_{yy}\le {2\over N}
       \sum_{k\in\{1,\ldots,N-1\}^3}|k|^{-2}
       \le {6(N-1)\over N}\le6.
\]

Since M_ss=s<=N, K_vv<=6N. Pinned vertex values remain zero.
For each color, these comparisons imply the following uniform variance
bounds on every available row, including normal end edges:

\[
\begin{array}{c|cccc}
\text{field}&z_e&t_e&(q\phi)_e,(D\phi)_e
 &(q\psi)_e,(D\psi)_e\cr
\text{variance bound}&C&CN^2&CN&CN^3.
\end{array}                                                \tag{19}
\]

The displayed endpoint bounds follow from
Var(X+Y),Var(X-Y)<=2Var(X)+2Var(Y); no independence is used.
For any jointly centered scalar Gaussian X,Y, Isserlis' theorem gives
E[X^2Y^2]=Var(X)Var(Y)+2Cov(X,Y)^2<=3Var(X)Var(Y).
Applying this to each color component of the four brackets in the
first formula of (4) bounds their squared norms per edge by, respectively,
CN^3, CN^3, CN^4 and CN^4. The squared norm of their sum is at most
four times the sum of their squared norms, with their fixed coefficients
included. There are at most 4N^4 variable links. Projection P is a
contraction, and ||L||<=16 from the full relative one-form spectrum.
Thus this global count supplies only

\[
 \mathbb E_S\langle W,LW\rangle\le C N^8,
 \qquad |Q_{i,N}|\le C_i N^5.                              \tag{20}
\]

All fields here are functions of the same z. In particular (18)--(20)
retain the moving prefix psi. Equation (17) estimates dJ_i[W] itself,
so the Phi W contribution in (15) is still present; it has not been
deleted by estimating only the first summand of (14). No flow-time
interchange or additional heat damping is used.

The required upper bound for this part is C_i N^3. With the imported
||J_i||_2=O(N), (17) would reach that threshold from an energy norm
(E<W,LW>)^(1/2)=O(N^2); (20) gives only O(N^4). Equivalently its
cubic-scaled upper bound is C_i N^2, not a uniform bound. Neither
inequality is a lower bound or asserts optimality. This unsuccessful
absolute count establishes no signed growth, nonconvergence or
obstruction to a sharper joint contraction. Repeating it without
additional cancellation is not a justified cubic-scale route. The
sextic expectation in (6) and the co-closed zero-time flow contribution
also remain untreated. This test changes no conclusion of the lemma.

### 6. Complete third-chaos norm test: retain the cancellation before counting

This test concerns the O(N^3) residual norm sufficient for L189's
co-closed initial interval. It does not change section 4's O(N^2)
threshold for the prefix-probe correction. It gives only

    ||rho(pi Rz)||_2 <= C N^4.                              (21)

The estimate is above both thresholds. It supplies no growth lower
bound, response limit or removal of an initial flow interval. Its
purpose is to test whether complete antisymmetrization alone repairs
the absolute norm method of section 5; the calculation below does not
obtain that repair.

Let E=im P in one-color link space, m=dim E, and choose a linear
isomorphism Z:R^m -> E with ZZ^T=S. The inverse covariance identity
gives Z^T L Z=I. Write z^c=Z xi^c for three independent standard
m-dimensional Gaussians. Set

    M=2 Z^T A Z,       t^c=Z M xi^c.

The second equality follows from ZZ^T=S, so the original order 2SA
is retained. Choose the same orthogonal eigenbasis of the real
symmetric M in all three colors. Absorb this basis change into Z;
then M=diag(mu_1,...,mu_m). This is an exact finite coordinate change,
not a localization of Z, Phi Z or A, and M need not be positive.
Section 5's whitened form bound gives max_a |mu_a|<=C N.

For any of the invariant homogeneous cubics F in this section define
its spatial coefficient array f by the polynomial identity

    F(Z xi)=sum_(a,b,c) f_abc xi_a^1 xi_b^2 xi_c^3.         (22)

The alternating color argument of L155, proof section 2, makes f
alternating in its three spatial indices. Equivalently, take the
coefficient of xi_a^1 xi_b^2 xi_c^3 after substituting the complete
polynomial. No ordered summand is omitted in this definition. Since
the three colors are independent standard Gaussians, direct second
moments give

    E[F(Z xi) G(Z xi)]=sum_(a,b,c) f_abc g_abc,
    ||F(Z xi)||_2^2=sum_(a,b,c) f_abc^2.                   (23)

There is no factorial in (23): all ordered a,b,c occur in (22).
It is also the Isserlis third-chaos identity, since every internal
color contraction vanishes. In the symmetric combined-index tensor
convention T_(ad,be,cf)=f_abc epsilon_def/6, one obtains
6||T||_HS^2=||f||_HS^2, which checks the normalization.

Let alpha_H and beta_H be the arrays (22) of script R_3(z) and
script S_3(z), respectively, and alpha_F,beta_F those of their
compositions with R. Differentiation in the FIXED direction t(z)
acts on (22) as

    (D_M f)_abc=(mu_a+mu_b+mu_c) f_abc.                    (24)

Consequently the exact complete norm is

    ||rho(pi Rz)||_2^2
       =sum_(a,b,c) |(alpha_F)_abc
                    -(mu_a+mu_b+mu_c)(beta_F)_abc|^2.     (25)

This is a squared norm of the joint polynomial, not a difference of
norms. All residual/action cross terms remain. In particular the
symmetry of M and spatial antisymmetry yield eigenvalue SUMS, not
differences. Neither property alone deletes D_M beta_F.

One can also see precisely what L183's cancellation removes in this
same norm. Write the actual quadratic b from (1) as

    b_j^r(Z xi)=sum_(b,c,d,e) B_(j,bc) epsilon_rde
                                 xi_b^d xi_c^e,
    B_(j,bc)=-B_(j,cb),
    V_abc=sum_j (LZ)_(ja) B_(j,bc).

Here r,d,e are color indices, j is a full variable link, and a,b,c
are whitened spatial indices. The actual bracket sign and the factors
1/2 and -1/4 of (1) are included in B. Such a B exists by expanding
(1) and antisymmetrizing its two spatial input slots; for example it
is half the coefficient of xi_b^2 xi_c^3 in b_j^1. Define
Alt V=(1/6) sum_(permutations pi) sgn(pi) V_(pi(a,b,c)).
The array of <Lz,b> is exactly 6 Alt V, by collecting its six color
orders. The array of 2<Az,b> is 6 Alt(mu_a V_abc), since
2AZ=LZ M. Applying (24) to the former and subtracting the latter
therefore gives the exact complete coefficient

    h_abc=(alpha_H)_abc
          -(mu_a+mu_b+mu_c)(beta_H)_abc
          -6 Alt[(mu_b+mu_c)V_abc],
    ||rho(pi Rz)||_2^2=sum_(a,b,c) |h_abc|^2.              (26)

The last term retains both derivatives of b, hence both moving
prefixes. In particular the D phi,q phi term in b is differentiated
in both slots. Equation (26) is another form of (3), obtained before
any norm inequality. The canceled weight is the mu_a attached to
Lz. The two other weights are not replaced by a commutator or set to
zero. The basis change may mix every physical row and frequency;
no mode, end edge or prefix endpoint has been removed.

Here is the full available absolute count from (26). L149's ordered
word formulas, applied to L155(2), give bounded stencil size and
at most C N for the absolute coefficient sum of each local cubic
residual summand. There are O(N^4) placements, and each link occurs
in only boundedly many stencils. The generator contributes 1/a;
both insertion subtractions have bounded coefficients. The action
cubic has bounded coefficients and the same bounded incidence
property on ALL plaquettes, including physical faces.

For either local cubic sum, the internal pairings vanish. Each cross
pairing between two stencils is a product of three entries of S.
Section 5 gives |S_ef|<=8. Bound one of the three entries by 8,
then sum the absolute product of the other two by Cauchy--Schwarz
over both stencil placements. The bounded incidence multiplicities
bound each squared sum by C||S||_HS^2. The fixed number of stencil
and color choices contributes only a constant. L182(11) consequently
gives

    ||alpha_H||_HS <= C N ||S||_HS
                   <= C N^3 sqrt(log(eN)),
    ||beta_H||_HS <= C ||S||_HS
                  <= C N^2 sqrt(log(eN)).                (27)

No smooth-input residual estimate is used here. By (24),
||D_M beta_H||_HS<=3||M||_op||beta_H||_HS.

For the prefix coefficient, Wick pairing with the above antisymmetric
B gives, with all three output colors summed,

    E<b,Lb>=12 sum_(a,b,c) |V_abc|^2.                    (28)

To check the factor, for a fixed output color r the two cross pairings
give 4 sum_(b,c) B_(j,bc)B_(k,bc); the three values of r give 12.
The remaining contraction is (LZ)(LZ)^T=LSL=L. No internal pairing
survives. This proves (28) also when the full-space S is singular.
For b itself, section 5's endpoint variance bounds give
E|[z,q phi]_e|^2<=C N and
E|[D phi,q phi]_e|^2<=C N^2 by Gaussian fourth moments.
Thus E||b||^2<=C N^6 after summing all O(N^4) links. Since
||L||<=16, (28) implies ||V||_HS<=C N^3.

Alt is an orthogonal projection for the ordinary tensor norm. Only
NOW take norms in the complete expression (26). The bound is

    ||h||_HS
      <= ||alpha_H||_HS+3||M||_op||beta_H||_HS
                              +12||M||_op||V||_HS
      <= C [N^3 sqrt(log(eN))+N^4] <= C N^4.              (29)

This proves (21), while explaining its failure to reach O(N^3).
The complete norm retains possible cross cancellation in (26); (29)
does not establish that it occurs or that it fails. In particular the
available bound inserted in L189(4) gives only C_i N eta(delta),
which is not uniform as N tends to infinity at fixed delta.
Choosing delta depending on N would not justify the missing fixed-
interval limit or its uniform removal. For the prefix-probe part,
L182(7) is weaker still with this norm bound.

The spectral-symmetrization/absolute-norm attempt stops here. It is
not evidence of a divergent actual response or of an optimal residual
exponent. Further use of (26) needs a specific controlled cancellation,
rather than repeating (29). An independent test within the same joint
target is the signed initial-time pairing from (5), retaining both
E[I rho_H] and E[dI[W]]; derivative heat factors might give a bound
that the unweighted residual norm cannot provide. No such signed
bound is proved in this section.

## Mathlib

Full matching result and supporting gauge-jet, cochain and Gaussian
integration-by-parts statements: **not checked**. Unknown coverage
is not evidence of absence. The named standard input is finite-dimensional
Gaussian integration by parts, whose precise possibly singular-covariance
specialization is justified in (13). L156's proved full gauge-jet identity
is reused through (9); no general flow or renormalization theorem is
reproved. The unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
records the primary sources and why they do not cover this selected
bare group. This reduction does not import their full-correlation
conclusions as a bound for either expectation in (6).
Section 5 uses the named Isserlis theorem and finite Gaussian integration
by parts with their specializations written out above. Its additional
supporting third-chaos energy and matrix-inequality coverage is likewise
not checked; its insufficient upper bound is not a new matching theorem
or a source-level discovery.
Section 6 uses the same finite Gaussian pairing input and elementary
orthogonal diagonalization. The complete three-form norm and its
insufficient O(N^4) estimate have not been checked in Mathlib. The
local word tensors are imported from L149/L155, not replaced by
generic synthetic fixtures. This is an inconclusive bounded research
test, not a new source-level result or a claimed cubic estimate.
