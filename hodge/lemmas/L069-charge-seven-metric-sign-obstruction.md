# L069 — Fixed-metric sign obstruction to the conditional charge-seven family

## Hypotheses

Suppose F satisfies exactly L052/L060's conditional hypotheses on
X=B x Y. The two factors are the same marked projective K3 surface
with the same fixed hyperkahler metric g and ordered complex structures
I,J,K, with IJ=K. F is a locally free holomorphic rank-two bundle,
slope-polystable for p_B^*h+p_Y^*h, where h=[omega_I] is the fixed
real Kahler class, and

\[
 c_1(F)=0,\qquad ch_2(F)=-6e_1-7e_2+\tau_D.
\]

Retain L062's self-adjoint mixed operator and its eigenvalue
D(sigma)=2lambda sigma, 1<lambda<3/2. Normalize the same holomorphic
two-form on both factors by

\[
 \sigma=\omega_J+i\omega_K,\qquad
 \omega_L(u,w)=g(Lu,w).
\]

Scaling L062's original nonzero form to this normalization does not
change its coefficient, since both its ordered pairing and its
cohomological contraction are complex-linear in sigma. L052 supplies
the compatible hyperholomorphic connection, L060 supplies stability
of every charge-seven fibre, and L067 supplies the natural local
quaternionic classifying map f and its positive constant L2 scale.
The moduli metric is defined using g on Y, rather than the integral
polarization H used to place f algebraically.

All statements concern this hypothetical F. No universal sheaf,
moduli surface, isotropic Mukai vector, global embedding, completeness,
transform inverse or existence of F is assumed.

## Conclusion

For the explicit Li L2 normalization below, the local metric
holomorphic symplectic form satisfies

\[
 f^*(\omega_J^M+i\omega_K^M)=\beta_F=-2\lambda\sigma_B.
 \tag{1}
\]

Here beta_F is precisely L062's displayed ordered Dolbeault pairing,
including its prefactor (2pi i)^(-2). L067's quaternionic compatibility
and positive metric pullback instead require that the left side be
c sigma_B with c>0. Thus c=-2lambda<0 is impossible. No F with the
stated hypotheses exists, provided the retained input conclusions hold.

This is a bounded REPRODUCTION/specialization of known metric and
family-form tools, with a new local notebook exclusion, rather than
a claim of originality or a resolution of the Hodge conjecture.
The separate critical audit of 2026-10-08 preserves its real-to-complex
comparison and sign verdict. It constructs no cycle or transverse deformation and
makes no exclusion of other representatives or other Chern data.

## Proof

**Imported metric and natural tangent, with qualifications.** Import
Yang Li, *Mukai duality on K3 surfaces from the differential geometric
perspective*, [arXiv:1908.05017v1, Section 2.2, Theorem 2.10 and
equations (1)–(2), PDF pp. 5–6](https://arxiv.org/pdf/1908.05017v1#page=5),
14 August 2019. On the real harmonic tangent of trace-free skew-Hermitian
connection variations a,b, its local hyperkahler quotient uses

\[
 G(a,b)=\frac1{4\pi^2}\int_Y\langle a,b\rangle\,dVol_Y,
 \qquad
 \omega_L^M(a,b)=-\frac1{4\pi^2}
             \int_Y Tr(a\wedge b)\wedge\omega_L^Y,
 \qquad L_Ma=-a\circ L_Y.
 \tag{2}
\]

The coefficient inner product is the negative unitary trace pairing;
in particular G is positive. The source's conventions give
omega_L^M(a,b)=G(L_Ma,b). These formulas are restricted to
 d_A^*a=0, d_A^+a=0, and gauge directions are d_A phi. This is the
local quotient construction on a K3, not Li's subsequent global
isotropic-vector duality or his suspect signed equation (6).
No global period formula is imported. The source's positive metric,
negative trace and negative precomposition in (2) are kept together.

**Independent frame check of the imported convention.** Fix a unit
vector e_0 and put e_1=Ie_0, e_2=Je_0, e_3=Ke_0. This frame has
the complex orientation: I pairs e_0 with e_1 and e_2 with e_3.
For its dual coframe theta_r write theta_rs=theta_r wedge theta_s
and vol=theta_0 wedge theta_1 wedge theta_2 wedge theta_3. Then

\[
 \omega_I=\theta_{01}+\theta_{23},\qquad
 \omega_J=\theta_{02}-\theta_{13},\qquad
 \omega_K=\theta_{03}+\theta_{12}.
 \tag{2a}
\]

For L=I,J,K let L_c alpha=-alpha circ L. Directly applying these
operators to the four covectors gives respectively
(theta_1,-theta_0,theta_3,-theta_2),
(theta_2,-theta_3,-theta_0,theta_1), and
(theta_3,theta_2,-theta_1,-theta_0). The complete alternating
coefficient check is therefore

| L | 01 | 02 | 03 | 12 | 13 | 23 |
| --- | --- | --- | --- | --- | --- | --- |
| I | 1 | 0 | 0 | 0 | 0 | 1 |
| J | 0 | 1 | 0 | 0 | -1 | 0 |
| K | 0 | 0 | 1 | 1 | 0 | 0 |

Each entry is both (theta_r wedge theta_s wedge omega_L)/vol
and the covector inner product <L_c theta_r,theta_s>. The diagonal
entries vanish and reversed entries change sign, so this verifies
every pair, not just one positive test vector. Multiplying by
-Tr(AB) for arbitrary skew-Hermitian coefficient matrices A,B and
summing proves pointwise, for all such a,b,

\[
 -\operatorname{Tr}(a\wedge b)\wedge\omega_L
       =\langle L_c a,b\rangle\,dVol_Y.
 \tag{2b}
\]

Here the inner product on the right includes the negative trace;
the coefficient norm is -Tr(A^2)=Tr(A^*A)>0 for A nonzero.
Thus (2) is internally consistent with the notebook's slot convention;
no opposite-slot convention or reversed orientation has been imported.
The same operators satisfy I_c J_c=K_c. This is the finite
convention check needed for this specialization, not a reproof of
the hyperkahler quotient theorem. Its restriction to the harmonic
tangent preserves the identity.

The fibres here are irreducible by L060's stability and L052's
compatible connection. Their trace-free obstruction vanishes as
checked in L067; H^1(O_Y)=0 removes a determinant tangent. Thus (2)
applies on the local smooth charts used by L067. Use its audited
natural connection/coarse-germ comparison to identify the same df
with the family Kodaira--Spencer map after the harmonic quotient.
Li's Lemma 2.12, equation (4), PDF p. 7, also fixes the local mixed
curvature convention R_univ(a,t)=a(t). The natural Dolbeault comparison
is obtained by differentiating the connection's (0,1) operator; it is
not a conjugation or a rescaling of the family differential.

For the audit one can check the sign of this quaternionic identification
directly on the actual F. In a differentiable unitary identification
over a small parameter open, write A_x for the vertical connection
and H_u for the horizontal connection component in a real parameter
direction u. Its mixed curvature is

\[
 r_u(t):=R(u,t)=\dot A_u(t)-(d_{A_x}H_u)(t).
 \tag{2c}
\]

Thus its quotient class is the derivative of x -> [A_x]. Let P be
orthogonal projection to the harmonic tangent in (2). It kills the
displayed gauge term, so a=P r_u is exactly df(u). The tangent is a
quaternionic invariant subspace by Li's equation (1); its orthogonal
complement is invariant too, since L_c is orthogonal. Hence P
commutes with every L_c. Hyperholomorphicity on the simultaneous
product gives R(Lu,Lt)=R(u,t), and replacing t by -Lt gives
r_{Lu}=-r_u circ L. Consequently

\[
                P r_{Lu}=L_c P r_u.                  \tag{2d}
\]

This checks the actual family's J,K, not just its I-holomorphicity
or an abstract Ext-space identification. The central determinant
tangent is absent because H^1(Y,O_Y)=0; the projection is to the
trace-free tangent. The calculation uses the actual connection and
requires no universal U(2) family. In particular, the extra global
isotropy assumptions in Li's Section 2.3 are not being specialized
away: only its local mixed-curvature convention is compared with
(2c), and (2d) follows from the retained hyperholomorphic F itself.

The general metric and moduli constructions are imported. The only
calculation needed here is their signed comparison with the explicit
ordered pairing in L062. This calculation is necessary because the
saved source assessment does not license reading a signed coefficient
from Li's global period statement or from an abstract Serre trace.

**Real unitary and holomorphic tangent conversion.** Let u,w be real
tangent vectors of B at x. Let a,b be the real harmonic representatives
of df(u),df(w) in (2). The derivative of the relative holomorphic
structure in the real direction u represents the Dolbeault class
[a^(0,1)]; passing to a horizontal slice changes it by a Dolbeault
coboundary. This is the same natural deformation map used in L067
and L062's mixed-curvature formula (4a).

To verify the complex tangent factor, complexify the real one-form
space. Since I_Y has eigenvalue -i on antiholomorphic covectors,
I_M=-precomposition with I_Y has eigenvalue +i on (0,1)-forms and
-i on (1,0)-forms. Consequently

\[
 \frac{a-iI_Ma}{2}=a^{0,1}.
 \tag{3}
\]

For v=(u-iI_Bu)/2 in T_x^(1,0)B, L067 gives

\[
 df_{\mathbb C}(v)
     =\frac{df(u)-iI_Mdf(u)}2,
 \qquad \kappa_x(v)=[a^{0,1}].
 \tag{4}
\]

The same applies to z=(w-iI_Bw)/2 and b. Equations (3)–(4) show
explicitly why the factors 1/2 in the tangent projections introduce
no factor 1/2 or 1/4 in the ordered Dolbeault pairing. Equivalently,
the real derivative of the (0,1) operator in the I_Bu direction has
class i[a^(0,1)], so its derivative in v is exactly [a^(0,1)].

An explicit factor check uses the frame (2a). Put a=T theta_0,
b=T theta_2 with T skew-Hermitian and t=-Tr(T^2)>0. Then
a^(0,1)=T(theta_0-i theta_1)/2 and
b^(0,1)=T(theta_2-i theta_3)/2, while
sigma=(theta_0+i theta_1) wedge (theta_2+i theta_3).
Their ordered wedge gives
sigma wedge Tr(a^(0,1) wedge b^(0,1))=-t vol:
the wedge of the unscaled four complex covectors is 4 vol,
cancelling the two projection halves. Both sides of (6) therefore
have density t vol/(4pi^2) on this pair. This exact check agrees
with the general type-projection argument and fixes its normalization;
it is not used to infer a global family from pointwise test forms.

A real skew-Hermitian variation is real for the coefficient operation
T -> -T^*, combined with conjugation of differential-form type.
Its two type parts are related by that operation, rather than by
scalar complex conjugation of matrices. The decomposition (3) uses
this real tangent and its ordinary complexification; it does not
replace the conjugate (1,0) coordinates in Verbitsky's presentation
by an unrelated KS map. The trace in (2) and in L062 is the same
matrix trace, extended complex-linearly, with the displayed order.

**Signed form equality.** Summing (2) for J and iK gives, on real
harmonic a,b,

\[
 \Omega_M(a,b):=(\omega_J^M+i\omega_K^M)(a,b)
     =-\frac1{4\pi^2}\int_Y Tr(a\wedge b)\wedge\sigma_Y.
 \tag{5}
\]

Since sigma_Y is of type (2,0) on the complex surface Y, the only
nonzero contribution to this integral is
Tr(a^(0,1) wedge b^(0,1)). Moving sigma_Y past this degree-two
product has sign +1. Complex-bilinearly extending (5) and evaluating
on the holomorphic tangents (4) therefore gives

\[
 (f^*\Omega_M)(v,z)
   =-\frac1{4\pi^2}\int_Y\sigma_Y\wedge
                         Tr(a^{0,1}\wedge b^{0,1})
   =\frac1{(2\pi i)^2}\int_Y\sigma_Y\wedge
                         Tr(\kappa_x(v)\wedge\kappa_x(z)).
 \tag{6}
\]

The last identity uses (2pi i)^2=-4pi^2. Representative independence
is L062's explicit Dolbeault coboundary/Stokes calculation. Thus it
also covers the horizontal gauge corrections and replacement of raw
mixed curvature by harmonic representatives. No harmonicity of raw
mixed curvature has been assumed. There is no exchange of Yoneda
order, coefficient conjugation, or reversal of fibre orientation in
(6); both use the complex orientation of Y. This proves exactly
f^*Omega_M=beta_F, rather than equality up to an unspecified scalar.
L062's equation (3), as an actual holomorphic form, now proves (1).

**Positive-scale test.** With the same normalization (2), L067 gives
f^*G=cg_B, c>0, and df commutes with J,K. For real u,w, hence also
by complex extension,

\[
 (f^*\omega_J^M)(u,w)
     =G(J_Mdf(u),df(w))
     =c\,g_B(J_Bu,w)=c\,\omega_J^B(u,w).
\]

The identical calculation for K gives f^*Omega_M=c sigma_B.
Comparison with (1) and sigma_B nonzero forces c=-2lambda. Since
lambda>0, this contradicts positivity. A different positive L2
normalization multiplying (2) by t>0 multiplies both the metric and
Omega_M; its forced scale is -2t lambda, still negative. A phase
change of sigma applied on both marked factors also cannot change
the coefficient. Changing J,K independently would change the
hypotheses and is not this test.

The achieved bound c=-2lambda lies in (-3,-2), whereas the required
bound is c>0; no numerical approximation is involved. This excludes
the exact conditional F, independently of the older compatible
index tests in ATTEMPTS/047. It does not refute the Hodge conjecture:
a failed bundle representative supplies no nonalgebraic Hodge class.
The unresolved universal primitive Hodge gap, other representatives
and transverse cycle transport remain untouched.

**Separate critical audit, 2026-10-08.** The scoped exclusion survives.
The full frame table (2a)--(2b) checks the three printed conventions
independently; their combination has no sign inconsistency. Equations
(2c)--(2d) verify the same negative-precomposition action directly on
the actual family's mixed curvature before harmonic projection. The
natural (0,1) derivative and (3)--(4) therefore use this action,
including its J,K, without substituting coefficient conjugation for
the KS map. Gauge corrections are exactly the Dolbeault coboundaries
covered in L062, whose ordered trace integral is representative
independent on the compact fibre.

The audit also rechecks L062's relevant exterior coefficient: the two
mixed curvature products contribute -2 Tr(a_j wedge a_k) after
moving target one-forms past parameter one-forms. Division by 2!
leaves -(2pi i)^(-2) times that ordered trace for the ch_2
contraction, whereas beta uses +(2pi i)^(-2). No other curvature
component contributes to parameter type (2,0), target type (0,2)
for a Chern curvature of total type (1,1). The closed pure-type
integral and Hodge injection in L062 establish this equality of
actual forms. Its raw contraction uses D's adjoint, equal to D by
the retained self-adjointness. Thus C_F=-beta_F=2lambda sigma and
Omega_M=beta_F have consistent, opposite signs, with the same
complex fibre orientation. Equation (2b) then makes the metric test
literal: the forced c=-2lambda is negative, not an unspecified
choice of phase for a Serre pairing.

No substantive error, stronger exclusion or existence result was
found. This audit is EXPLORATION and REPRODUCTION of the covered
tools; it adds explicit verification, not a new mathematical result
or originality claim. All input hypotheses and the earlier necessary
index calculations remain in force. Only this exact charge-seven F
has been audited; no all-charge consequence is asserted.

## Mathlib

Coverage of the full unitary L2/ordered-Yoneda comparison and this
conditional sign obstruction: **not checked**. No matching theorem
or absence is asserted. The gauge metric is imported by the precise
primary citation above; the natural family and quaternionic inputs
are L062 and L067 with the conditional L052/L060 data. This step
reproduces and specializes the assessed known tools and does not
claim progress beyond the literature checked.
