# L095 — Actual harmonic nonzero derivative at the split equality fibre

## Hypotheses

Retain L071's identical marked projective K3 factors S_1,S_2, the
same hyperkähler metric g, ordered structures I,J,K, real Kähler
class h and forms omega_L(u,w)=g(Lu,w), sigma=omega_J+i omega_K.
Write e_1=eta tensor 1, e_2=1 tensor eta, with integral_S eta=1.
The full integral mixed tensor tau_D has cup-product-self-adjoint
operator D and D[sigma]=2lambda[sigma], where 1<lambda<5/4.

Suppose F is locally free of rank two, slope-polystable at
Omega=p_1^*h+p_2^*h, with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use its actual compatible unitary hyperholomorphic connection from
L071, with curvature R. Regard S_2 as base and S_1 as fibre. At
y_0 in S_2 suppose the holomorphic fibre is E=L direct sum L^{-1},
with c_1(L)=k, k^2=-14 and h.k=0. Identify its restricted connection
unitarily with the determinant-one direct-sum HE connection A of
L094. No nonzero derivative, smooth quotient, germ realization or
generic fibre stability is assumed.

For a real base direction u put r_u(t)=R(u,t) on the fibre and use
the normalized real inner product

\[
 G_y(a,b)=-\frac1{4\pi^2}\int_{S_1}
                 \sum_j\operatorname{Tr}(a(f_j)b(f_j))\,dVol,
\]

where f_0,...,f_3 is any orthonormal fibre frame. It is the positive
negative-unitary-trace inner product of L070.

## Conclusion

For every fibre y and every real u in T_yS_2, the actual mixed form
r_u is ASD-harmonic:

\[
                    d_{A_y}^+r_u=0,\qquad d_{A_y}^*r_u=0.
                                                        \tag{1}
\]

Its full raw pairing is

\[
                     G_y(r_u,r_w)=2\lambda g(u,w).       \tag{2}
\]

In particular, at the specified split fibre, r_u lies in L094's
determinant-fixed harmonic space V, and its actual slice derivative
a(u)=P_Vr_u equals r_u. It is quaternionic and injective, and

\[
       \|r_u\|_{G_{y_0}}^2=2\lambda\|u\|_g^2>0
                    \quad\text{for }u\ne0.              \tag{3}
\]

It still satisfies L094's necessary quadratic obstruction Q(a(u))=0.
Thus this test removes the actual zero-derivative alternative; it
does not contradict the compatible quaternionic line of L094.
Harmonicity in (1) is not the stronger assertion d_A r_u=0.

This is a conditional ADVANCE / REPRODUCTION of the assessed
coefficient and raw curvature tools. The separate critical audit
below preserves the conclusion. No F, integrated surface germ, smooth stabilizer quotient,
global mixed-action realization, algebraic cycle or transport is
constructed. The universal primitive Hodge gap is unchanged.

## Proof

**Imported tools and applicability.** L071 establishes stability of
the hypothetical product bundle before using Verbitsky,
*Hyperholomorphic connections on coherent sheaves and stability*,
[math/0107182v10, Definition 3.2, Proposition 3.7, Lemma 3.8 and
Theorem 3.9, pp. 11--14](https://arxiv.org/pdf/math/0107182v10#page=11).
Its actual curvature is invariant under simultaneous I,J,K rotation;
its fibre restrictions are ASD with zero Kähler contraction. This
does not require irreducible restricted connections.

Import coefficient Bianchi and Kähler adjoint identities for an
integrable Hermitian connection from Buchdahl--Schumacher,
*Polystable bundles and representations of their automorphisms*,
Complex Manifolds **9** (2022), 78--113,
[Section 1, p. 81, DOI 10.1515/coma-2021-0131](https://d-nb.info/1262812674/34#page=4).
The actual Chern connection is Hermitian and integrable, and both
Kähler metrics are fixed. These identities require no simplicity.
L094's separate audit gives their real contraction and harmonic
comparison in precisely the present skew-adjoint convention.

Biswas--Schumacher's stable-family harmonicity theorem,
[*Geometry of moduli spaces of Higgs bundles*, math/0605589v1,
Section 3, Lemmas 3.2--3.3 and Proposition 3.4, pp. 7--8](https://arxiv.org/pdf/math/0605589v1#page=7),
is not directly applied at the reducible fibre: its stability
hypothesis fails there. The coefficient argument below handles the
already supplied smooth connection instead of constructing family
metrics or reproving a general moduli theorem. In particular Li's
irreducible universal-connection Laplacian inverse is not used.

The raw normalization and exterior identities are L070's audited
equations (2), (4)--(13), which specialize Yang Li,
[*Mukai duality on K3 surfaces from the differential geometric
perspective*, 1908.05017v1, Section 2.2, pp. 5--6](https://arxiv.org/pdf/1908.05017v1#page=5),
before quotienting. Only those actual-curvature identities are
reused; L070's positive-tensor exclusion is outside these hypotheses.
Chern--Weil is Bismut, *Index Theorem and the Heat Equation*, ICM
Berkeley proceedings (1987),
[p. 492, (0.2)](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1987c.pdf#page=2).
Thus ch_2 is represented by Tr(R wedge R)/(2(2pi i)^2).

**Keep the actual horizontal connection in Bianchi.** Locally choose
a smooth unitary trivialization over a base ball, write A_y for the
vertical connection and H_u for the horizontal coefficient. At a
fixed base point choose u independent of the fibre coordinates.
The product Levi-Civita connection has no mixed connection terms.
The mixed curvature and coefficient Bianchi identity give

\[
 r_u=\dot A_u-d_{A_y}H_u,\qquad
 d_{A_y}r_u=\dot R_{Y,u}+[H_u,R_Y]
                       =\nabla_u^{\operatorname{End}F}R_Y.    \tag{4}
\]

For clarity, on fibre vectors t,s the cyclic Bianchi sum is
nabla_u R(t,s)+nabla_t R(s,u)+nabla_s R(u,t)=0; its last two
terms are -(d_{A_y}r_u)(t,s). Equivalently differentiate the
vertical curvature and use d_{A_y}^2H_u=[R_Y,H_u] in the first
identity of (4). Both checks retain the horizontal commutator.
They do not replace the connection by an uncorrected derivative.

The fibre self-dual projection is fixed as y varies. R_Y^+=0 at
every y by L071. Differentiation in u commutes with this projection,
and the commutator in (4) is also ASD because it changes only the
endomorphism coefficient. Therefore d_{A_y}^+r_u=0. This establishes
the linearized ASD equation at every fibre, including reducible ones.
The right side of (4) need not vanish, so full covariant closedness
of r_u is neither required nor claimed.

**Quaternionic symmetry forces the Coulomb equation.** Product
hyperholomorphicity says R(Lv,Lw)=R(v,w) for L=I,J,K. On one base
and one fibre vector this gives

\[
                      r_{Lu}=L_c r_u,
                  (L_c a)(t)=-a(Lt).                         \tag{5}
\]

At a normal orthonormal fibre frame set
C_0(a)=sum_j(nabla_{f_j}a)(f_j) and
C_L(a)=sum_j(nabla_{f_j}a)(Lf_j). The structures are parallel;
L094's audited real coefficient identities give

\[
 d_{A_y}^*a=-C_0(a),\quad
 \langle d_{A_y}a,\omega_L\rangle=C_L(a),\quad
                    C_I(I_c a)=C_0(a).                       \tag{6}
\]

These are endomorphism-valued contractions in the form legs.
In the last identity, the definition of I_c and I^2=-1 directly
give sum_j -(nabla_{f_j}a)(I I f_j)=C_0(a). Hence no derivative
of I or scalar-Laplacian inversion occurs.

Apply the already established ASD equation to the real direction
Iu. Since omega_I is self-dual, it implies
0=C_I(r_{Iu})=C_I(I_c r_u)=C_0(r_u). Equation (6) yields
d_{A_y}^*r_u=0, proving (1). Together, all three self-dual
contractions and the Coulomb contraction vanish. L094's coefficient
Kähler comparison therefore also identifies r_u^{0,1} as a
Dolbeault-harmonic form. This is a statement about the raw form,
before a stabilizer quotient, not just its projected class.

**Determinant-fixed comparison at the split point.** Integral c_1=0
and Pic^0(S_1 x S_2)=0 trivialize det F holomorphically. The induced
determinant Chern connection is HE with constant zero. In a global
nonvanishing holomorphic determinant frame its log metric has zero
Laplacian, hence is constant on the compact product. Its curvature
is zero, so Tr R=0 and r_u is skew-adjoint trace-free. This is the
same determinant argument checked in L094's audit, rather than
inferring trace-flatness merely from a rational first class.

Polystable HE uniqueness identifies the restricted connection at
y_0 with A by an isometry of the chosen HE metrics, as in L094.
Equations (1) place r_u in its V. L094's actual-family slice bridge
then gives a(u)=P_Vr_u=r_u. Equation (5) makes this map quaternionic;
the actual smooth family, not an arbitrary compatible tangent,
supplies Q(a(u))=0. Injectivity will follow from the norm below.

**Specialize the raw pairing with the negative tensor.** Put
H_y(u,w)=G_y(r_u,r_w). L070's raw argument applies with base S_2
and fibre S_1: both have the same ordered quaternionic structures,
the connection has invariant curvature, and its fibre curvature is
coefficientwise orthogonal to each omega_L. No tensor-sign,
harmonicity or irreducibility assumption enters these identities.
The negative trace pairing is positive and (5) makes H_y symmetric
and quaternionic-invariant. Since the base tangent is a quaternionic
line, H_y=c(y)g for a smooth real c(y)>=0.

To retain the relevant sign and factorial explicitly, write
R=R_B+R_m+R_Y and R_m=sum_i dx_i wedge r_i, with base forms first.
The only terms of Tr(R wedge R) that contribute after wedging with
omega_L and fibre integration are R_B R_Y+R_Y R_B+R_m^2. Their
evaluation on u,w is

\[
 2\operatorname{Tr}(R_B(u,w)R_Y)
                         -2\operatorname{Tr}(r_u\wedge r_w).
\]

R_Y wedge omega_L=0 coefficientwise, so the first term vanishes
even for a fibre-dependent noncentral R_B. The two ordered mixed
terms and (2pi i)^2=-4pi^2 give the actual real integral

\[
 C_L(u,w):=p_{2*}\left(
    \frac{\operatorname{Tr}(R\wedge R)}{2(2\pi i)^2}
                                \wedge p_1^*\omega_L\right)(u,w)
  =\frac1{4\pi^2}\int_{S_1}
                 \operatorname{Tr}(r_u\wedge r_w)\wedge\omega_L
  =-G_y(L_c r_u,r_w)=-c(y)\omega_L(u,w).                \tag{7}
\]

The last equality uses the ordered frame identity
-Tr(a wedge b) wedge omega_L=<L_c a,b>dVol from L070.
All operations use the complex fibre orientation. Thus

\[
 \gamma_R:=p_{2*}\left(
     \frac{\operatorname{Tr}(R\wedge R)}{2(2\pi i)^2}
                                     \wedge p_1^*\sigma\right)
                      =-c(y)\sigma_{S_2}.                     \tag{8}
\]

This also shows that the full raw unitary pairing is the relevant
one; here its central part is zero by the determinant argument.
There is no replacement of the raw norm by a projected norm.

**Actual-form evaluation, including the exchanged factors.** The
integrand in (8) is closed of type (4,2). Integration along the
complex surface S_1 gives a closed form of type (2,0), hence a
holomorphic two-form on S_2. For tau_D=sum_i alpha_i tensor beta_i,
our operator convention is D(z)=sum_i q(z,alpha_i)beta_i.
Consequently integration on the first factor gives
p_{2*}(tau_D p_1^*[sigma])=D[sigma], whereas L070's integration
on the second gives D^*[sigma]. The common metric and the retained
self-adjointness ensure either computation has the same eigenvalue;
in this orientation it is D directly. Exchanging the degree-two
factors incurs sign +1.

The two pure point terms have fibre degrees six and two,
respectively, after multiplying by p_1^*[sigma]; neither survives
integration. Therefore the full *negative* tensor gives

\[
                         [\gamma_R]=-2\lambda[\sigma_{S_2}].  \tag{9}
\]

Holomorphic two-forms on the compact Kähler base inject into de Rham
cohomology. Equations (8)--(9) thus give equality of actual forms,
not just classes, and the nowhere-vanishing sigma forces
c(y)=2lambda at every y. This proves (2)--(3). The achieved scale
lies in (2,5/2), which meets the strict threshold c>0, rather than
only the nonnegative threshold of the raw pairing. In the
unnormalized L094 inner product this is
integral -Tr(r_u wedge *r_u)=8pi^2 lambda g(u,u).

The zero harmonic derivative is therefore impossible for this
hypothetical F. Its image is a nonzero quaternionic line satisfying
Q=0, entirely consistent with L094's exhibited compatible line.
No identification with that particular line, integration theorem,
higher-order vanishing or coarse-quotient immersion follows. The
equality/positive-Euler realization and universal Hodge gaps remain.

**Separate critical audit, 2026-10-12 (step 244).** The exact approved
audit finds no substantive error, stronger exclusion or existence
conclusion. Its outcome is EXPLORATION / REPRODUCTION: independent
verification of this conditional specialization, without a new
mathematical advance or an originality claim. All three direct inputs
remain L070, L071 and L094; no new mathematical dependency is introduced.

The saved source comparison additionally identifies a close published
analogue: Yang Li, *Mukai duality on K3 surfaces from the differential
geometric perspective*,
[1908.05017v1, Section 3.2, Lemmas 3.5 and 3.6, printed pp. 10--12](https://arxiv.org/pdf/1908.05017v1#page=12).
These give raw ASD/Coulomb harmonicity and quaternionic variation for
opposite fibres of his universal connection, without assuming those
fibres irreducible. His original isotropic irreducible moduli K3 and
universal-connection construction are additional hypotheses, unavailable
here. Thus this is a known partial overlap, not direct certification of
the arbitrary conditional F in this lemma. Checking its coefficient
specialization and signed norm remains necessary. No universal-family
existence statement or printed global period sign is used.

First, the connection premise really is supplied by L071. A polystable
rank-two product bundle that is not stable is a sum of two lines. With
trivial determinant its mixed character is a product of divisor classes
and annihilates sigma; it cannot equal the present tensor acting by
-2lambda on sigma. L071 therefore applies the stable hyperholomorphic
connection theorem legitimately. Invariance is for the full Chern
class at the identical product metric. Restriction preserves invariant
curvature coefficientwise, so every vertical curvature is ASD even
when its connection is reducible.

Independently differentiate R_Y=d_Y A_y+A_y wedge A_y. This gives
dot R_Y=d_A dot A_u. Substituting r_u=dot A_u-d_A H_u gives

\[
 d_A r_u=d_A\dot A_u-[R_Y,H_u]
        =\dot R_Y+[H_u,R_Y].
\]

Both equalities have the sign in (4). The product metric fixes the
fibre Hodge star; hence the self-dual part is
dot(R_Y^+)+[H_u,R_Y^+]=0. The connection on the coefficient bundle
is retained, and there is no assumption that dot R_Y or d_A r_u
vanishes. Base and fibre vector fields can be chosen independently
at the point, so there is no mixed Levi-Civita correction.

For the Coulomb check, choose a normal orthonormal fibre frame with
omega_I=theta_0 wedge theta_1+theta_2 wedge theta_3. Direct
antisymmetrization gives

\[
 \langle d_Aa,\omega_I\rangle
 =\tfrac12\sum_j(d_Aa)(f_j,If_j)
 =\sum_j(\nabla_{f_j}a)(If_j)=C_I(a).
\]

In the second half of the antisymmetrization, replace f_j by If_j;
I^2=-1 changes its sign. This computation is coefficient-valued
and uses only the parallelness of I. Thus C_I(I_c a)=C_0(a)
has no missing factor or adjoint term. Invariance of curvature gives
r_(Iu)=-r_u composed with I with exactly the sign in (5). The
already proved ASD equation for Iu implies C_0(r_u)=0 and hence
d_A^*r_u=0. Neither irreducibility nor removal of the parallel
diagonal zero-form is needed for this implication.

The determinant/slice passage is also valid for the actual connection.
Integral c_1=0 and Pic^0(X)=0 imply det F is holomorphically trivial.
The induced determinant HE constant is zero, and in a global
holomorphic frame its log metric is harmonic on compact X, hence
constant. This proves Tr R=0 as an actual form. HE uniqueness on
the split fibre then gives the stated unitary identification with A.
In L094's imported unitary slice, an actual smoothly gauge-fixed
derivative b_u differs from dot A_u by an exact d_A-term; the
horizontal term shows the same for b_u-r_u. Both b_u and r_u are
now in ker d_A^* intersect ker d_A^+. If b_u-r_u=d_A s, then
its squared L2 norm equals <d_A^*(b_u-r_u),s>=0. Hence b_u=r_u.
Parallel gauge generators remain harmless; they are not inverted.
This checks the same actual derivative, rather than substituting
a coarse-moduli tangent at a singular point. L094's necessary
quadratic condition still follows from the actual family curve.

Finally enumerate the ordered curvature square by fibre degree.
Before wedging with omega_L the nine products have degrees
0,1,2,1,2,3,2,3,4 in the order
R_B^2, R_B R_m, R_B R_Y, R_m R_B, R_m^2, R_m R_Y,
R_Y R_B, R_Y R_m, R_Y^2. Only the three degree-two terms survive.
The pure pair is 2 Tr(R_B(u,w)R_Y); multiplying the coefficientwise
identity R_Y wedge omega_L=0 kills it even for noncentral,
fibre-dependent R_B. The ordered mixed terms are
-Tr(r_u wedge r_w)+Tr(r_w wedge r_u)=-2 Tr(r_u wedge r_w).
Division by 2(2pi i)^2 gives the prefactor +1/(4pi^2) in (7).
For an independent sign check take r_u=T theta_0 and
r_(Iu)=T theta_1, with -Tr(T^2)=t>0. Their contribution to C_I(u,Iu)
is -t/(4pi^2) per fibre volume, while G(I_c r_u,r_(Iu)) is
+t/(4pi^2). Bilinearity and the quaternionic frame identity in L070
give the same sign for arbitrary coefficient one-forms. This is an
exterior-algebra check, not a constructed curvature example.

Quaternionic invariance of the positive raw pairing gives H_y=c(y)g.
The actual integral is closed and of type (2,0), because its integrand
is closed of type (4,2) and the first-factor fibre has complex dimension
two. The operator convention integrates tau_D to D sigma on this
factor, with no interchange sign in even degree. The pure terms have
fibre degrees six and two and contribute zero. Thus its class is
-2lambda[sigma], and injectivity of holomorphic two-forms into de Rham
cohomology gives the actual equality -c(y)sigma=-2lambda sigma.
The nowhere-zero sigma forces c(y)=2lambda in (2,5/2), strictly
above zero. The unnormalized squared norm is consequently
8pi^2 lambda g(u,u), agreeing with (3).

The audit therefore retains the nonzero quaternionic harmonic
derivative, but adds no conclusion about the reducible-fibre locus,
an integrated germ, a smooth quotient or a common kernel. L094's
compatible-line stop is unchanged. Equality/positive-Euler realization,
prescribed global mixed action and universal Hodge realization remain
unresolved.

## Mathlib

Full matching coverage of this raw reducible-family harmonicity and
changed-sign strict norm specialization: **not checked**. Unknown
coverage is not absence. The precise primary coefficient, invariant
curvature, affine normalization and Chern--Weil citations are above;
the audited local identities are applied with their hypotheses and
factor conventions explicitly checked. This is local conditional
progress using known tools, with no originality claim or progress
beyond the checked literature asserted. The separate audit above
preserves this conditional proof and its limitations.
