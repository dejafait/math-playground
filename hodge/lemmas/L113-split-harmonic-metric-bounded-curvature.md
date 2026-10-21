# L113 — Bounded curvature of the actual split harmonic metric

## Hypotheses

Retain audited L112 and L111, including the actual derived and harmonic
identifications, and L094/L095's coefficient quaternionic structures
and actual harmonic Kodaira--Spencer map. In particular F remains the
hypothetical locally free rank-two bundle with integral c_1=0,
ch_2=-14e_1-21e_2-tau_D and the given smooth compatible connection
at the identical marked hyperkähler metrics. The full negative tensor
and 1<lambda<5/4 are retained. Put M=R^1p_*End_0(F)=E. Its split
locus Z is finite and may be empty.

On U=B minus Z give M its actual fibrewise harmonic L2 metric G,
using the specified coefficient and fibre metrics. Near z in Z use
L111's convergent Koszul-plane splitting and L112's natural smooth
spectral comparison. No central Hermitian orthogonality, curvature
estimate, smooth metric extension, connection extension, semistability,
bound on |Z| or existence of F is assumed.

## Conclusion

For each z in Z, on some full coordinate ball D about z, the Chern
curvature Theta_G of (M|_U,G) has uniformly bounded pointwise norm,
using G on endomorphisms and the fixed smooth base metric on forms.
In particular there is K<infinity such that, for all sufficiently
small epsilon>0,

\[
 \int_{0<|b-z|<\epsilon}|\Theta_G|^2\,dVol_B
                  \le K\epsilon^4<\infty.                 \tag{1}
\]

This is a conditional local ADVANCE / REPRODUCTION under the prior
SPECIALIZE assessment. The separate critical audit below preserves the
conclusion (EXPLORATION / REPRODUCTION), with no substantive error or
stronger result found. No smooth
metric or connection extension, semistability, cardinality bound,
F, algebraic cycle or transport is supplied. The universal primitive
rational Hodge gap remains unresolved. For Z empty the local assertion
is vacuous.

## Proof

**Known inputs and the specialization.** Reuse the unchanged assessment
`drafts/literature/2026-10-16-split-harmonic-metric-curvature-energy.md`.
The Chern formula imported here is Demailly, *Complex Analytic and
Differential Geometry*, version 21 June 2012, Chapter V, section 12,
(12.2)--(12.3) and Theorem 12.4, pp. 268--269,
[primary text, university mirror](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf#page=269).
In a holomorphic frame it gives connection matrix G^{-1} partial G
and curvature bar-partial(G^{-1} partial G). It is used only on the
puncture, where G is smooth positive definite. The smooth quotient
construction has the scope of Chapter V, section 14, Theorems
14.3/14.5 and (14.6)--(14.7), pp. 273--275; below we differentiate
L112's exact quotient matrix, rather than apply a constant-rank
extension theorem at z.

Coefficient harmonic quaternionic invariance is Verbitsky,
*Hyperholomorphic bundles*, alg-geom/9307008v1, section 4,
[Theorem 4.1 and Corollary 4.3, pp. 12--15](https://arxiv.org/pdf/alg-geom/9307008v1#page=12),
with the real-form and operator identification already justified in
L094. It applies to End_0 of the split connection without simplicity.
L112 supplies the actual spectral quotient, not a substitute metric.
The work remaining beyond these imports is to identify its central
mixed block and estimate its full derivatives. The finite frame check
below is necessary at the reducible fibre; no irreducible moduli metric
or coarse-space comparison is used there.

**The actual central plane is quaternionic.** Fix z. Write V_R for
L094's real space of skew-adjoint ASD-harmonic one-forms and
phi(a)=a^{0,1} for its real-linear isomorphism to the Dolbeault
harmonic H^1(End_0(F_z)). Let I_c,J_c,K_c act on real forms by
R_c a=-a composed with R. The map phi identifies I_c with multiplication
by i; transport the other two operators to Dolbeault cohomology by
this same map. Use L094's positive real inner product

\[
 g_0(a,b)=-\int_{S_1}\sum_\nu\operatorname{Tr}
                         (a(f_\nu)b(f_\nu))\,dVol.
                                                               \tag{2}
\]

These operators are orthogonal and satisfy the quaternionic relations.
L095's actual mixed curvature gives a quaternionic injective map
T_zB -> V_R. Denote its real image by W. Thus W is a real
four-dimensional quaternionic line. Its image under phi is exactly
the complex KS plane, with the tangent convention fixed in L111.

Put h_0=diag(1,-1), xi=i h_0, T=ad(xi) and A=ad(h_0) on the
Dolbeault space. Conjugation by the compact stabilizer is unitary and
commutes with I_c,J_c,K_c. Differentiating gives a real operator T
commuting with all three. There is no diagonal degree-one sector;
on the two complex weight spaces A has eigenvalues +2,-2. Since
T=iA on Dolbeault forms, under phi the operator A is -I_c T.
It is invertible. L111 identifies the two incoming coefficients as
-A times the two KS classes. Hence the residue of its plane P has
underlying real space

\[
                   P_{\mathbb R}=A W=-I_c T W=T W.        \tag{3}
\]

The last equality is an equality of subspaces: T W is quaternionic,
so it is invariant under I_c. It is also invariant under J_c,K_c.
This argument uses the real compact generator xi before converting
to h_0; it does not incorrectly assert that A commutes with J_c.

**Serre orthogonality is actual Hermitian orthogonality here.** We
check the relevant pairing identity on forms, prior to any quotient.
In an oriented orthonormal frame e_0,Ie_0,Je_0,Ke_0, with dual
theta_0,...,theta_3, the three forms are

\[
 \omega_I=\theta_{01}+\theta_{23},\quad
 \omega_J=\theta_{02}-\theta_{13},\quad
 \omega_K=\theta_{03}+\theta_{12}.
\]

For r<s in the order 01,02,03,12,13,23, both
(theta_r wedge theta_s wedge omega_R)/dVol and
the inner product of R_c theta_r with theta_s have the following
six coefficients:

\[
 I:(1,0,0,0,0,1),\qquad
 J:(0,1,0,0,-1,0),\qquad
 K:(0,0,1,1,0,0).
\]

Both expressions vanish on diagonal pairs and change sign on reversing
the pair. Multiplying by -Tr(XY) for arbitrary skew-adjoint coefficient
matrices and summing therefore proves, for every real coefficient
one-form pair a,b, the pointwise identity

\[
 -\operatorname{Tr}(a\wedge b)\wedge\omega_R
           =\langle R_c a,b\rangle\,dVol.                 \tag{4}
\]

Here the right inner product includes negative trace. Set
sigma=omega_J+i omega_K, as in L095. Since sigma has type (2,0),
only the (0,2) part of a wedge b survives after wedging with sigma.
Thus (4), complex-linearity and (2pi i)^{-2}=-1/(4pi^2) give the
actual normalized Serre identity

\[
 \begin{split}
 \Omega_z(\phi(a),\phi(b))
 &=(2\pi i)^{-2}\int\sigma\wedge
                   \operatorname{Tr}(\phi(a)\wedge\phi(b))\\
 &=\frac1{4\pi^2}\bigl(g_0(J_c a,b)+i g_0(K_c a,b)\bigr).
 \end{split}                                             \tag{5}
\]

There is no commutation of coefficient matrices assumed in (4)--(5);
trace makes their bilinear product symmetric. The orientation and
normalization agree with the forms fixed in L094/L095.

The ordinary Dolbeault L2 Hermitian product h_D satisfies
Re h_D(phi(a),phi(b))=g_0(a,b)/2. This follows from
a=phi(a)-phi(a)^* and the orthogonality of types (1,0),(0,1);
polarizing the norm gives the displayed real-part identity.
For a complex subspace P invariant under J_c, equation (5) implies

\[
                 P^{\perp_{\Omega_z}}=P^{\perp_{h_D}}.    \tag{6}
\]

Indeed vanishing of (5) for all b in the real space of P gives
g_0(J_c a,b)=0. Skew-adjointness of J_c and J_c P=P make this
equivalent to g_0(a,P)=0. Conversely that orthogonality and invariance
under J_c,K_c make both terms in (5) zero. Real orthogonality to an
I_c-invariant subspace is equivalent to Hermitian orthogonality,
by also testing I_c b. This proves both directions of (6).

L111 chooses J=P^{perp_omega} over the local ring, where omega reduces
to this very Omega_z under natural derived base change. Hence its
central J_z is P_z^{perp_{Omega_z}}. In L112 the central comparison
T_z^1 maps to the harmonic space and is the natural derived-fibre
identification. It therefore pulls back both the actual h_D and the
same Serre form used above. Combining (3)--(6), P_z and J_z are
orthogonal for the actual pulled-back metric H_K at z. Arbitrary
choices of chain representative away from z do not alter this
central comparison: the residual differentials are zero and the
specified cohomological identification fixes T_z^1.

**Exact quotient and complete derivative estimates.** Use L112's
extending holomorphic frame on K^1=P direct sum J and coordinates
x,y with z=0. Put w=(x,y)^t and r=(|x|^2+|y|^2)^{1/2}. The incoming
column is v=(w,0). Write the smooth positive Hermitian matrix as

\[
                 H_K=\begin{pmatrix} A_0&B_0\\B_0^*&C_0\end{pmatrix},
                 \qquad B_0(0)=0.                       \tag{7}
\]

Here A_0 is two by two, C_0 is fifty by fifty, and the star is
conjugate transpose. We use the anti-linear first-slot convention.
L112's exact least-norm formula, minimized in the one complex variable
t representing the boundary t v, gives, for r>0,

\[
 G=C_0-Q,\qquad
 Q=\frac{(B_0^*w)(w^*B_0)}{w^*A_0w}.                    \tag{8}
\]

This is the actual G, including every smooth cross term, not its
leading approximation. Choose one smaller closed ball on which H_K
is positive and smooth, and all its derivatives through order two
are bounded. Positivity gives constants c,C>0 with

\[
 cr^2\le d:=w^*A_0w\le Cr^2.                            \tag{9}
\]

All derivatives below are real coordinate derivatives, measured in
fixed finite matrix norms. The estimates hold for every partial
derivative of the indicated order, uniformly on the full puncture.
The mean-value estimate and B_0(0)=0 give
|B_0|<=C r, |D B_0|<=C, |D^2 B_0|<=C. Since w is linear,
for u=B_0^*w and N=u u^* the product rule gives

\[
 |D^k u|\le C_k r^{2-k},\qquad
 |D^k N|\le C_k r^{4-k},\quad 0\le k\le2.               \tag{10}
\]

In particular the second derivative of u includes D^2 B_0 times w
and both first-derivative products; none is omitted. Similarly
|Dd|<=C r and |D^2d|<=C. Differentiating the full inverse denominator,

\[
 D(d^{-1})=-d^{-2}Dd,\qquad
 D_iD_j(d^{-1})=2d^{-3}D_i d D_j d-d^{-2}D_iD_j d,
\]

and (9) imply |D^k(d^{-1})|<=C_k r^{-2-k} for k=0,1,2.
Every term in the product rule for Q=N d^{-1} is therefore bounded
by a constant times r^{2-k} at order k. Thus

\[
        |Q|\le C r^2,\qquad |DQ|\le C r,\qquad
                         |D^2Q|\le C.                  \tag{11}
\]

All constants apply simultaneously on one ball; no coordinate ratio
or selected direction is used. Both axes and all approach directions
are included. Smoothness of C_0 and (8)--(11) show that G and its first
two derivatives are bounded on the puncture. L112's positive lower
bound also gives a uniform bound on G^{-1} there.

**Curvature and energy.** In the extending holomorphic J-frame the
imported Chern formula expands as

\[
 \Theta_G=\bar\partial(G^{-1}\partial G)
 =-G^{-1}(\bar\partial G)G^{-1}\wedge\partial G
                         +G^{-1}\bar\partial\partial G. \tag{12}
\]

The complete bounds just proved give a uniform bound on every matrix
coefficient of (12). L112's two-sided norm equivalence converts this
to a bound in the actual G-endomorphism norm. The base metric is
smooth positive through z and uniformly equivalent to the coordinate
metric on the smaller closed ball. Its volume on a radius-epsilon
ball is at most a constant times epsilon^4. This proves (1) and the
stated stronger pointwise bound.

The cancellation B_0(0)=0 is essential to this derivation and has
been proved for the actual central comparison, rather than inferred
from boundedness of G alone. The estimates do not assert a smooth
second-derivative limit, a smooth metric/connection extension or a
semistability theorem. They do not bound |Z| or change L111's
conditional budget c_2(N)=(800-|Z|)eta. ATTEMPTS/063/066/067 retain
their scopes: no automatic extension, singular coarse-metric bridge
or duality-only numerical bound has been invoked. No global kernel
or Hodge-class realization follows from this local conditional test.

**Separate critical audit, 2026-10-16 (step 324).** Use the unchanged
prior SPECIALIZE assessment
`drafts/literature/2026-10-16-split-harmonic-curvature-critical-audit.md`.
The audited assertion is the uniform pointwise curvature bound and
(1), for this actual metric. The following checks use L094, L095,
L111 and L112 in their stated conditional scopes; their direct uses
and hence the DAG row are unchanged. Demailly's Chern formula and
Verbitsky's coefficient input retain the versions, theorem numbers
and hypotheses cited above. No general extension theorem is imported
or reproved.

First fix the real and complex identifications at the actual split
connection. L094's real/Dolbeault comparison is a=b-b^*, b=a^{0,1},
with I_c acting as i, and with the given coefficient adjoint. It
preserves the harmonic spaces by the coefficient Kähler identities.
For a real base tangent t, its complex tangent is u=(t-iIt)/2.
L095 gives r_{It}^{0,1}=i r_t^{0,1}, so r_u^{0,1}=r_t^{0,1}.
Thus the real image W and the complex KS plane agree under phi,
without a factor two or conjugation. It is L095's actual image W,
not the optional compatible line constructed in L094.

The parallel compact stabilizer generator xi=i diag(1,-1) is
skew-adjoint for the actual direct-sum metric. Its infinitesimal
conjugation T preserves harmonic forms and commutes with each R_c:
conjugation changes coefficient legs, whereas R_c changes form legs.
On Dolbeault forms T=iA, hence A=-I_c T on the underlying real space.
The lack of a diagonal H^1 sector and the two weights imply A^2=4,
so its image of W has real dimension four. For every R_c and w in W,
R_c Tw=T R_c w belongs to TW; therefore TW is quaternionic and
-I_c TW=TW. This proves (3). In particular one need not, and must
not, commute A itself with J_c. L111's degree-zero connecting map
is exactly -A times KS; its incoming residual plane is precisely
this subspace, regardless of the higher-order choices of a,b_0.

Second check the pairing before transporting the metric. The frame
used in (4) is positively oriented for I: omega_I^2/2=dVol. For any
basis covectors theta_r,theta_s, the wedge coefficient is the inner
product <R_c theta_r,theta_s>; the six upper-triangular coefficients
listed above, their negatives below the diagonal and their zero
diagonal account for all sixteen ordered pairs. Expanding
a=sum X_r theta_r and b=sum Y_s theta_s multiplies each coefficient
by -Tr(X_r Y_s). Trace symmetry makes this real symmetric coefficient
pairing positive on skew-adjoint matrices. Matrix commutativity is
not used. This verifies (4) for arbitrary coefficient one-forms.
In wedging with sigma of type (2,0), only a^{0,1} wedge b^{0,1}
survives; commuting sigma past their degree-two product has sign +1.
Equation (4) and the negative scalar (2pi i)^{-2} consequently give
the positive scalar 1/(4pi^2) in (5). Orthogonality of types in
a=b-b^* gives ||a||^2=2||b||^2, and real polarization gives the
claimed real part of h_D. If (5) vanishes against P, its real part
g_0(J_c a,P)=0 and J_c P=P imply g_0(a,P)=0. Conversely this last
condition kills both real and imaginary parts because J_c P=K_c P=P.
Testing also I_c P=P gives the full Hermitian orthogonality. Thus (6)
is an equality for the actual products, not just two nondegenerate forms.

L111 represents the actual derived cup/trace class, whose residual
pairing is exactly (5). Since both residual differentials are zero,
homotopic representatives have identical residual degreewise maps.
L112's natural comparison T_z^1 has this same prescribed derived-fibre
identification and lands in the central harmonic space. Pulling back
its actual L2 metric therefore makes J_z=P_z^{perp_omega} orthogonal
to P_z. The smooth cutoff has middle rank fifty-two at the center;
the fifty-dimensional ordinary fibre of M is not used in its place.
This proves B_0(0)=0 for the H_K used in (7), without requiring the
comparison to preserve a chain pairing away from the center.

Third check every singular quotient term. L112 gives the class of j
as j+t v, with t arbitrary and v=(w,0). In the anti-linear first-slot
convention, its squared norm is

\[
 j^*C_0j+\bar t\,w^*B_0j+t\,j^*B_0^*w+|t|^2d,
 \qquad d=w^*A_0w.
\]

Completing the square gives t=-d^{-1}w^*B_0j and exactly (8).
For real coordinate indices i,j put u=B_0^*w, N=uu^*.
Linearity of w gives
u_i=(B_0^*)_i w+B_0^*w_i and
u_{ij}=(B_0^*)_{ij}w+(B_0^*)_i w_j+(B_0^*)_j w_i.
Thus u,u_i,u_{ij} have orders r^2,r,1 on r<=1. In particular
N_{ij}=u_{ij}u^*+u_i u_j^*+u_j u_i^*+u u_{ij}^*
has order r^2; N and N_i have orders r^4 and r^3. All terms in
d_i and d_{ij}, including derivatives of A_0 and of both copies of
w, have orders r and 1 respectively. The positive lower bound in
(9) follows from the positive principal block A_0 on one closed ball.
In particular no directional lower bound is substituted for it.

Writing subscripts for these real derivatives, the full second
derivative is

\[
 Q_{ij}=\frac{N_{ij}}d
 -\frac{N_i d_j+N_j d_i+N d_{ij}}{d^2}
 +\frac{2N d_i d_j}{d^3}.                              \tag{13}
\]

The three groups have bounds Cr^2/r^2, Cr^4/r^4 and Cr^6/r^6.
Each is uniformly bounded, including when i=j. The zeroth and first
derivatives similarly have bounds Cr^2 and Cr. These estimates use
only full-ball smooth bounds and r, so apply on both axes and all
approach directions. They verify (10)--(11) for the complete quotient,
not a truncated Taylor term. They do not give a second-derivative limit.

Finally all real second-derivative bounds control the complex mixed
derivatives in (12), since partial and bar-partial are fixed linear
combinations of real coordinate derivatives. Differentiating G^{-1}
gives -G^{-1}(bar-partial G)G^{-1}, so both terms of (12) are bounded
by L112's inverse bound and the estimates just checked. If cI<=G<=CI,
the squared G-Hilbert--Schmidt norm of any endomorphism matrix X is
at most (C/c)||X||_{HS}^2: conjugate X by G^{1/2} and G^{-1/2}.
The fixed smooth base metric gives an additional uniform conversion
for the two-form legs. Its volume density is bounded on the same
closed coordinate ball, whose real dimension is four. Integrating
the squared pointwise bound yields exactly K epsilon^4 in (1), with
K depending on the conditional family and chosen neighborhood.

The audit preserves the required stronger bounded-curvature threshold,
and hence finite energy. It finds no substantive repair, stronger
obstruction or existence conclusion, so its outcome is EXPLORATION /
REPRODUCTION, not another mathematical advance. If Z is empty there
are no split-point assertions. Smooth extension, semistability,
|Z|, existence of F, transport and universal primitive Hodge realization
remain unproved. ATTEMPTS/063/066/067 retain their precise scopes;
this estimate does not erase their independent missing hypotheses.

## Mathlib

Full matching coverage of this actual-family harmonic-metric
specialization, including its central Serre/Hermitian comparison and
finite energy at the jump, has not been checked. Supporting analytic
inputs are the precise Demailly and Verbitsky results cited above,
together with the stated canonical actual-family inputs. No absence
claim or formal verification is made. This is an informal specialization
of known tools preserved by the separate audit above, not a candidate Hodge
resolution.
