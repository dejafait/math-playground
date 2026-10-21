# L070 — Actual mixed-curvature obstruction for all fixed-tensor survivors

## Hypotheses

Retain L052's identical marked projective K3 factors B,Y, their same
hyperkahler metric g and ordered complex structures I,J,K with IJ=K.
Write omega_L(u,w)=g(Lu,w), h=[omega_I], and
sigma=omega_J+i omega_K on both factors. Let e_1=eta tensor 1 and
e_2=1 tensor eta, with integral_S eta=1. Retain the full mixed class
tau_D and its cup-product-self-adjoint operator D, with
D([sigma])=2lambda[sigma], 1<lambda<3/2.

Suppose F is a rank-two locally free holomorphic bundle on B x Y,
slope-polystable at p_B^*h+p_Y^*h, with

\[
 c_1(F)=0,\qquad
 ch_2(F)=(a+4)e_1+(b+4)e_2+\tau_D,
 \quad a,b\leq-9,\quad (a+4)(b+4)\equiv6\pmod {12}.
 \tag{1}
\]

The compatible unitary hyperholomorphic Chern connection supplied
by L052 is retained. Factor restrictions may be reducible. No
harmonic tangent, classifying map, smooth moduli quotient, universal
connection, L060 stability, or L067 chart is assumed.

## Conclusion

There is no F satisfying these hypotheses. More precisely, write R
for its actual curvature, r_u(t)=R(u,t) for its mixed block, and set

\[
 G_x(a,b)=-\frac1{4\pi^2}\int_Y
        \sum_{j=0}^3\operatorname{Tr}(a(e_j)b(e_j))\,dVol_Y,
 \quad H_x(u,w)=G_x(r_u,r_w).
 \tag{2}
\]

Here e_j is any real orthonormal frame on Y, and a,b are arbitrary
real skew-Hermitian End(F|_{x x Y})-valued one-forms. The quantity H
is a nonnegative symmetric form and equals c(x)g_B for a smooth
real function c>=0. The actual Chern–Weil contraction satisfies

\[
 \gamma_R:=p_{B*}\left(
  \frac{\operatorname{Tr}(R\wedge R)}{2(2\pi i)^2}
                  \wedge p_Y^*\sigma\right)
       =-c(x)\sigma_B=2\lambda\sigma_B.
 \tag{3}
\]

Thus c=-2lambda lies in (-3,-2), against c>=0 required. The
contradiction is independent of both pure coefficients a,b and
allows reducible restrictions. It excludes every member of L052's
necessary non-exclusion set for this fixed tensor and metric.

This is an informative NEGATIVE, classified REPRODUCTION: a
specialization of the assessed curvature and affine-unitary tools,
not an originality claim. A separate critical audit on 2026-10-08
preserves the signed identity and exclusion below. It is an obstruction to this bundle recipe, not to
algebraicity of the Hodge class or to the Hodge conjecture. Other
representatives and transverse transport remain unresolved.

## Proof

**Imported inputs and why the specialization is necessary.** Import
hyperholomorphicity as invariance of the actual End(F)-valued curvature
under simultaneous quaternionic rotations from Verbitsky,
*Hyperholomorphic connections on coherent sheaves and stability*,
[arXiv:math/0107182v10, Definition 3.2, Proposition 3.7,
Lemma 3.8 and Theorem 3.9, PDF pp. 11–14](https://arxiv.org/pdf/math/0107182v10#page=11).
L052 has already checked the stable-product and invariant-Chern
hypotheses that supply this connection; they do not require stable
factor restrictions. Import the invariant surface two-form
orthogonality to the Kahler triple from the same Proposition 3.7
and Lemma 3.8, also proved in Verbitsky, *Hyperholomorphic bundles*,
[alg-geom/9307008v1, Proposition 1.2, Definition 2.1 and the proof
of Theorem 2.3/Lemma 2.1, PDF pp. 4–7](https://arxiv.org/pdf/alg-geom/9307008v1#page=4).
These are statements about curvature and invariant forms, not
about a quotient's regularity.

Use the affine normalization in Yang Li, *Mukai duality on K3
surfaces from the differential geometric perspective*,
[arXiv:1908.05017v1, Section 2.2, equations (1)–(2) and the
construction preceding Theorem 2.10, PDF pp. 5–6](https://arxiv.org/pdf/1908.05017v1#page=5).
Its negative unitary trace, wedge forms and negative precomposition
are used before reduction. Its irreducible quotient, Section 2.3
universal connection and global period sign are not inputs. The
extension of the trace-free affine formulas to the central unitary
part is checked explicitly below. The required raw identity is not
an assertion that raw mixed curvature is a harmonic variation.

Import ordinary Chern–Weil from Bismut, *Index Theorem and the
Heat Equation*, ICM Berkeley 1986 proceedings (1987),
[p. 492, equation (0.2)](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1987c.pdf#page=2):
ch(F)=Tr exp(-R/(2pi i)), so ch_2 is represented by
Tr(R wedge R)/(2(2pi i)^2). The square eliminates the possible
choice of sign in the first-character convention.

The sources do not state this fixed-tensor exclusion. We therefore
compute the actual pure and mixed blocks and their signed pairing.
We reuse the pointwise frame identity from L069 and the transpose
and Chern–Weil conventions from L062 only in the scope explicitly
justified below; neither narrower lemma's stable-fibre or moduli
conclusion is extended by assumption. No general existence or
moduli theorem is reproved.

**All curvature blocks and their symmetry.** The product tangent
splitting gives a global decomposition

\[
 R=R_B+R_m+R_Y
\]

by real base/fibre degrees (2,0),(1,1),(0,2). Hyperholomorphicity
says, for L=I,J,K and any real tangent vectors v,w on the product,

\[
                       R(Lv,Lw)=R(v,w).                 \tag{4}
\]

On two fibre directions this makes R_Y an invariant surface two-form
with values in the skew-Hermitian endomorphisms. The imported
orthogonality applies coefficientwise at every (x,y). Hence

\[
                  R_Y\wedge\omega_L^Y=0,
                  \qquad L=I,J,K.                      \tag{5}
\]

The same holds for the base block in base directions, although only
(5) will be needed to remove the pure-product contribution. This
is an End(F)-valued equality, before trace and before integration.
It does not require irreducibility, a chosen splitting into stable
factor bundles, or vanishing of R_B itself.

Applying (4) to a base direction u and a fibre direction t, and
then replacing t by -Lt, gives

\[
                  r_{Lu}(t)=-r_u(Lt)=:(L_c r_u)(t).
 \tag{6}
\]

The metric on End(F) is fixed by the given unitary connection;
precomposition acts on the one-form leg alone. Thus each L_c is
orthogonal and skew-adjoint for G_x, with L_c^2=-1 and I_cJ_c=K_c.
The last equality follows directly from composition on covectors:
I_cJ_c a=a composed with JI=-a composed with K=K_c a.
No gauge correction or harmonic projection enters (6).

**Full unitary trace, including its centre.** The coefficient
pairing -Tr(AB) for skew-Hermitian matrices is real symmetric
and positive definite: -Tr(A^2)=Tr(A^*A). In rank two decompose
A=A_0+(t/2)Id and B=B_0+(s/2)Id, where t=Tr A and s=Tr B
are purely imaginary. Then

\[
                 -\operatorname{Tr}(AB)
                  =-\operatorname{Tr}(A_0B_0)-ts/2.       \tag{7}
\]

For a square the central term -t^2/2 is nonnegative. Cross terms
vanish because the trace-free part has zero trace. Apply this to
every one-form coefficient in (2). It proves positivity for all
unitary variations, including their central part. Taking trace and
subtracting the centre commute with (4)–(6), so the central curvature
also obeys (5) and (6). Thus its pure-product contribution vanishes
by the same reason, and its mixed contribution adds a nonnegative
summand to H. No determinant-flat assertion is needed: the entire
central block is retained and checked. In particular c_1(F)=0
has not been used as an unsupported pointwise trace-vanishing claim.

For arbitrary such real one-forms a,b, L069's proof (2a)–(2b)
is the purely pointwise identity

\[
 -\operatorname{Tr}(a\wedge b)\wedge\omega_L^Y
        =\langle L_c a,b\rangle\,dVol_Y.                \tag{8}
\]

Its scope includes the present forms: in an oriented orthonormal
coframe theta_0,...,theta_3 with e_1=Ie_0,e_2=Je_0,e_3=Ke_0,
the forms are theta_01+theta_23, theta_02-theta_13,
theta_03+theta_12 for I,J,K. The coefficient equality is
(theta_r wedge theta_s wedge omega_L)/vol
=<L_c theta_r,theta_s>. Multiplying by -Tr(AB) gives (8) for
each pair of coefficients and hence by bilinearity for a,b.
This computation does not use trace-freeness, harmonicity or the
charge-seven assumptions of L069. Equation (7) verifies its central
part explicitly. This is the needed applicability check of that
previously audited frame identity.

**Expand before discarding any term.** For a fixed L define the
actual real base two-form

\[
 C_L=p_{B*}\left(
       \frac{\operatorname{Tr}(R\wedge R)}{2(2\pi i)^2}
                       \wedge p_Y^*\omega_L^Y\right).
 \tag{9}
\]

Fibre integration needs degree four in Y. The terms R_B^2 and
R_BR_m+R_mR_B have fibre degrees zero and one before wedging with
omega_L, and cannot contribute. The terms R_mR_Y+R_YR_m and R_Y^2
have fibre degrees three and four before that wedge, so exceed
four afterwards and vanish. Exactly

\[
          R_B R_Y+R_Y R_B+R_m^2                          \tag{10}
\]

remain in base/fibre degree (2,2). Products denote the exterior
product and the displayed order of matrix multiplication.

In real base coordinates write R_m=sum_i dx_i wedge r_i. For
real base vectors u,w, graded trace cyclicity and reordering a
fibre one-form past a base one-form give the fibre two-form

\[
 \bigl[\operatorname{Tr}(R\wedge R)\bigr]_{(2,2)}(u,w)
    =2\operatorname{Tr}\bigl(R_B(u,w)R_Y\bigr)
                    -2\operatorname{Tr}(r_u\wedge r_w).
 \tag{11}
\]

Indeed the two ordered mixed terms have coefficients
-Tr(r_u wedge r_w) and +Tr(r_w wedge r_u); the latter equals
-Tr(r_u wedge r_w). This retains noncommuting matrices under
trace. For the pure-product terms the two even degrees commute
and trace cyclicity gives the factor two displayed in (11).
By (5) the first term of (11), wedged with omega_L^Y, is zero
pointwise, even when R_B(u,w) is noncentral and y-dependent.
It is not removed merely from the cohomological pure coefficients.

Since (2pi i)^2=-4pi^2, the remaining term and the factorial give

\[
 C_L(u,w)=\frac1{4\pi^2}\int_Y
                \operatorname{Tr}(r_u\wedge r_w)\wedge\omega_L^Y
          =-G_x(L_c r_u,r_w)=-H_x(Lu,w).                \tag{12}
\]

We use the complex orientation of Y and the order base forms
followed by fibre forms. Moving the fibre two-form past an even
degree incurs no further sign. Formula (12) applies to the actual
curvature, without a quotient or integration by parts.

**Nonnegative quaternionic scale.** By (6) and orthogonality of
L_c, H_x(Lu,Lw)=H_x(u,w). It is symmetric and nonnegative by (2)
and (7). On the four-dimensional real space T_xB these facts imply
H_x=c(x)g_B, c(x)>=0, including the possibility of a zero form.
Explicitly choose a g_B-unit u and use the orthonormal basis
u,Iu,Ju,Ku. Its four H-diagonal entries all equal H(u,u).
For distinct entries symmetry and the skew-adjoint quaternionic
operators give zero: H(u,Lu)=0, and H(Lu,Mu) reduces to
plus or minus H(u,Nu)=0 when L and M are distinct. Thus the full
matrix is c times the identity. The expression as the metric
trace of H divided by four shows that c is globally smooth;
fibre integration is smooth because Y is compact and R is smooth.
This proves from (12)

\[
                  C_L=-c(x)\omega_L^B,
       \qquad \gamma_R=C_J+iC_K=-c(x)\sigma_B.          \tag{13}
\]

Strict positivity or injectivity is not required for a contradiction.

**Real/complex and ordered-pairing check.** This also checks the
raw version of L062's ordered convention. Let u,w be real base
vectors, v=(u-iIu)/2, z=(w-iIw)/2, and a=r_u,b=r_w. By (6),

\[
          r_v=(a-iI_c a)/2=a^{0,1},
          \qquad r_z=b^{0,1}.                           \tag{14}
\]

Here the right sides are type projections on Y with complexified
End coefficients; I_c=-precomposition with I_Y acts by +i on
(0,1) covectors and -i on (1,0) covectors. Thus (14) introduces
no scalar beyond those already in the type projections, and no
coefficient conjugation. The real structure on coefficients is
A -> -A^* combined with conjugation on differential forms. It
is not substituted for the natural complexification in (14).

With the ordered raw expression

\[
 \beta_R(v,z)=\frac1{(2\pi i)^2}\int_Y\sigma_Y\wedge
                         \operatorname{Tr}(r_v\wedge r_z),
 \tag{15}
\]

only the target (0,2) wedge component survives. Summing (8) for
J and iK and using (14) gives beta_R=c(x)sigma_B on holomorphic
vectors. Equivalently, in holomorphic base coordinates the
base-(2,0), fibre-(0,2) part of the traced curvature square is
-2 dz_j wedge dz_k wedge Tr(r_j wedge r_k). Dividing by 2!
therefore gives gamma_R=-beta_R, exactly the sign in (12)–(13).
The pure blocks contribute nothing to this complex component
because R has total type (1,1); they were independently retained
and removed in the full real calculation (10)–(12). This proves
the raw real/complex comparison without declaring r harmonic,
using a Kodaira–Spencer injection, or requiring a smooth quotient.

**Evaluate the fixed tensor as an actual form.** Chern–Weil,
Bianchi and d sigma=0 show that gamma_R is closed and represents
p_B*(ch_2(F)p_Y^*[sigma]). Because R is Chern curvature of total
type (1,1), gamma_R has pure type (2,0) after integration over
the complex surface Y. It is therefore a holomorphic two-form.
This argument retains the actual connection; it does not replace
a closed form by its class pointwise without justification.

For (1), the e_1 contribution has fibre degree two and the e_2
contribution has fibre degree six, so neither survives the
pushforward. Write tau_D=sum_i alpha_i tensor beta_i. With
q the surface cup product, its action is
z -> sum_i q(z,alpha_i)beta_i, whereas the pushforward is
sum_i q(beta_i,[sigma])alpha_i=D^*([sigma]). This is the same
transpose computation as L062, unchanged when the pure point
coefficients vary. The retained self-adjointness gives

\[
                      [\gamma_R]=2\lambda[\sigma_B].    \tag{16}
\]

On the compact Kahler surface B, holomorphic two-forms inject into
de Rham cohomology by Hodge decomposition. Hence (16) implies
gamma_R=2lambda sigma_B as actual forms. Since sigma_B is
nowhere zero, (13) yields c(x)=-2lambda everywhere, contradicting
c>=0. The achieved forced interval (-3,-2) is disjoint even from
the weaker required interval [0,infinity). No approximation or
uncalculated pure-curvature remainder enters this threshold.

The integer survivor inequalities and congruence identify the
approved scope but never enter the signed identity; all those
pairs are excluded at once. This does not revoke their actual
topological SU(2) realization or individual factor constructions.
It stops using pure point corrections to rescue this fixed mixed
tensor at this same common metric. A different mixed tensor,
metric arrangement, bundle recipe or algebraic correspondence is
outside the conclusion. No Hodge class has been proved nonalgebraic,
no new cycle or transverse surface has been constructed, and the
universal primitive Hodge-class realization gap is unchanged.

**Separate critical audit, 2026-10-08.** The audit checks the actual
connection, rather than promoting the narrower moduli conclusions of
L062 or L069. In L052 the polystable rank-two product bundle is first
shown stable by exclusion of a sum of two line bundles; the full
rotation-invariant first two Chern classes then supply the compatible
connection. No stability of its factor restrictions is used here.
The imported invariant-form orthogonality is coefficientwise: for
every skew-Hermitian coefficient of R_Y it gives wedge zero with
each omega_L. Multiplying that zero by the arbitrary coefficient
R_B(u,w) still gives zero, so dependence on y or noncommutativity
cannot restore the discarded pure-product term.

Independently enumerating the nine ordered square terms gives fibre
degrees 0,1,2,1,2,3,2,3,4 for
R_B^2, R_B R_m, R_B R_Y, R_m R_B, R_m^2, R_m R_Y,
R_Y R_B, R_Y R_m, R_Y^2 respectively. Adding the degree-two
omega_L leaves exactly the three terms of (10). Their ordered
evaluation is (11), with both mixed products present. As a direct
sign check, take quaternionic orthonormal frames on the two tangent
spaces and any skew-Hermitian coefficient T with
t=-Tr(T^2)>0. The pointwise mixed assignment
r_(e_j)=T theta_j obeys (6). On (e_0,Ie_0) its traced mixed square
is 2t theta_01; after division by 2(2pi i)^2 and wedging with
omega_I, its contribution is -t dVol_Y/(4pi^2). The corresponding
G(I_c r_(e_0),r_(Ie_0)) is +t/(4pi^2) per unit volume. This is
a check of exterior algebra, not an assertion that this assignment
extends to a global curvature or a bundle. It verifies the minus
sign and factorial of (12) without reference to a moduli form.
The trace-free/central decomposition (7) is orthogonal and positive
on each summand; the same check works for central T. No hidden
determinant-flat or trace-free hypothesis is needed.

The three operators L_c act only on covectors, preserve the full
unitary coefficient metric, and satisfy the same quaternionic
relations as the base. Consequently (6) makes H invariant under
I,J,K. Its symmetric matrix in u,Iu,Ju,Ku has equal diagonal
entries and zero off-diagonal entries by skew-adjointness, proving
H=cg with c>=0 even if r has a kernel. On complexified covectors
I_c has eigenvalue +i on (0,1) and -i on (1,0), so
(1-iI_c)/2 is precisely the (0,1) projection in (14). The ordered
complex square still has coefficient -2; the trace pairing is
complex-bilinearly extended, without conjugating a coefficient.
Thus (15) agrees with the real calculation and introduces neither
an additional factor two nor a reversed Yoneda order.

Finally the integrand defining gamma_R is closed of type (4,2),
and integration along the complex surface gives a closed (2,0)
form. Compact Kahler Hodge injection therefore validates the
actual-form comparison. For the same ordered Kunneth tensor the
pushforward is D^*, not D by convention; retained self-adjointness
is exactly what identifies it with D here. Pure factor-point terms
have the wrong fibre degree and do not affect this computation.
The audit preserves c=-2lambda in (-3,-2) versus c>=0, and finds
no substantive error or stronger conclusion. This is verification
of the existing scoped obstruction, not a new mathematical result.

## Mathlib

The full actual-curvature, raw affine pairing and fixed-tensor
exclusion have **not been checked** in Mathlib. No absence or
matching declaration is asserted. The precise primary references
above supply invariant curvature, surface orthogonality, affine
unitary normalization and Chern–Weil. L052 supplies the conditional
connection and fixed data; the explicitly identified computations
in L062 and L069 supply the unchanged transpose/conventions and
pointwise frame identity. This is local progress by specialization
of assessed known tools, with no claim of progress beyond the
checked literature. The separate audit above preserves the proof;
it does not supply Mathlib coverage or an existence theorem.
