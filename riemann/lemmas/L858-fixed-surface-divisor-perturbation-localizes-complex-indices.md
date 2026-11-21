# Lemma 858: divisor perturbation localizes the complex indices of a fixed radial torus

## Hypotheses

Use L847's actual entire G, positive R,C, and full form on X=(C*)^2:

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
                                                               \tag{1}
\]

Let u:T^2 -> R^2 be real C2 and periodic, with
u_2(t,s)=u_1(s,t). Give T^2 the orientation dt wedge ds, and set

\[
 z_j(\theta)=R e^{u_j(\theta)+i\theta_j},\quad
 \Phi_u=(z_1,z_2),\quad A=Du,\quad
 J=\det(I-iA)=1-\det A-i\operatorname{tr}A,\quad f=F\circ\Phi_u.
                                                               \tag{2}
\]

Assume the exact full density q=fJ is real and nonnegative everywhere.
Assume also that u agrees with L849's exact analytic graph on a smaller
open diagonal collar |delta|<delta_c, where t=m+delta, s=m-delta,
and 0<delta_c<epsilon_849. L849's positive off-diagonal density,
prescribed h,b and inherited L848 analytic/trusted-software
qualifications are retained. The choice is strictly inside the width
on which L849 proves its collar estimates.

No isolation of J zeros, simple zeros of G, forced divisor contact,
nonzero contact census, RH, or positivity-preserving surface
perturbation is assumed. In particular u need not be analytic away
from its prescribed collar. All factors and all their zeros in (1)
are retained.

## Conclusion

There are epsilon_0>0, a smooth exchange-invariant cutoff chi in [0,1],
and real C1 matrix fields A_epsilon, 0<=epsilon<=epsilon_0, such that
A_0=A, chi=1 near K={J=0}, and both chi and A_epsilon-A vanish
near the closure of the prescribed smaller collar. Their oriented
plane fields, in the actual ambient coordinates, are

\[
 g_\epsilon(\theta)
 =\operatorname{span}_{\mathbb R}^{\rm or}
    \left[H(\theta)(I-iA_\epsilon(\theta))\right],
 \qquad H=\operatorname{diag}(iz_1,iz_2).                    \tag{3}
\]

The columns give the orientation. These maps form a homotopy of the
original oriented Gauss map g_0, with u and Phi_u fixed, and satisfy

\[
 J_\epsilon:=\det(I-iA_\epsilon)=J+\epsilon\chi\bar f.
                                                               \tag{4}
\]

For every positive epsilon in this range, its complex-plane contacts
are exactly Z={f=J=0}. This set is finite, even if K was nonisolated.
At a point p in Z, let n_j(p) be the multiplicity of G at z_j(p),
with n_j=0 when G(z_j(p)) is nonzero. Put N_p=n_1(p)+n_2(p)>=1.
In either Lai orientation class its local contribution is

\[
                            I_p=-N_p<0.                    \tag{5}
\]

Both class totals are zero. Consequently **Z is empty** under these
hypotheses. Thus a globally nonnegative radial torus with this collar
cannot have a complex tangent on the zero divisor of the full form.
For positive epsilon the constructed plane field is totally real.

This is a conditional necessary constraint, first proved here within
the construction turn's invocation-start EXPLORE scope. The independent
conceptual audit of 6 November 2026 accepts the stated conclusion,
including nonisolated original contacts and both orientation classes.
The localization and fixed-surface lift are the local progress beyond
the source statements checked; POTENTIALLY_NEW does not certify
originality. The sources' index identities are imported known results.
The audit is REPRODUCTION under its prior SPECIALIZE assessment, not
an additional mathematical discovery or an audit of L848's software.
No original surface is changed, and A_epsilon is not asserted to be
the derivative of another u. No contact is forced, no positive torus
is constructed or excluded in general, and no new Xi minor sign or
all-degree conclusion follows.

## Proof

### Source boundary and the two orientation classes

The pre-invocation assessment is
`drafts/literature/2026-11-06-gauss-map-divisor-localization-test.md`.
Its completed global-index comparison supplies the following inputs:

- Hon-Fei Lai, *Characteristic classes of real manifolds immersed in
  complex manifolds*, Trans. AMS 172 (1972), 1–33,
  DOI 10.1090/S0002-9947-1972-0314066-8,
  [Theorem 4.8, Definition 4.9 and Theorem 4.10, pp16–17;
  Theorem 5.10 and its plane-subbundle interpretation, pp24–25](https://scispace.com/pdf/characteristic-classes-of-real-manifolds-immersed-in-complex-2lh0zj0xb1.pdf).
  The two complex-plane loci in the oriented Grassmannian carry
  Poincare-dual classes. Isolated intersections are evaluated by local
  degree; Lai gives the negative locus the opposite orientation to
  the image of the positive locus under plane-orientation reversal.
  The bundle formulation does not require a new surface immersion.
- Franc Forstneric, *Analytic disks with boundaries in a maximal real
  submanifold of C2*, Ann. Inst. Fourier 37(1) (1987), 1–44,
  DOI 10.5802/aif.1076,
  [Section 2, determinant map (2.1), Definition 2 and Lemma 8 with
  its proof, pp11–15](https://www.numdam.org/item/10.5802/aif.1076.pdf).
  This gives the orthonormal-frame determinant, its winding
  interpretation, and the local index with the enclosing loop oriented
  by the tangent complex line. Frame changes by positive real
  determinants do not change that winding.

The named homotopy invariance of singular homology, already used in
L847, applies to the pairing with these fixed classes. These are
imports, not reproved class formulas. The exact lift, isolation and
sign calculations below are necessary because those general theorems
do not supply them for (1). Primary determinant and orientation cases
were rechecked in this attempt; no additional literature assessment
or changed source scope is used.

Taylor factorization at a finite zero of the nonzero entire G is the
standard isolated-zero theorem: Jiří Lebl, *Guide to Cultivating
Complex Analysis*, v1.10, [Theorem 2.4.7, pp49–50](https://www.jirka.org/ca/ca.pdf).
Its source scope was already inspected for L847 and L855. Below only
local factorization and the first-order expansion of C1 maps are
needed, not an analytic inverse theorem for the C2 surface.

### A contact-free collar and a normal coordinate for the determinant

Along the diagonal, exchange symmetry makes A commute with the
coordinate-exchange matrix. Its eigenvalues in the symmetric and
antisymmetric directions are the real numbers h'(m), b(m) prescribed
by L849. Therefore

\[
                    J(m,m)=(1-ih'(m))(1-ib(m))\ne0.        \tag{6}
\]

Off the diagonal in the exact collar, L849 gives q>0, so neither f
nor J vanishes there. Since delta_c<epsilon_849, continuity of u and
Du extends the matching to the collar boundary, where the same strict
off-diagonal estimate applies. Thus J has no zero on the closure of
the smaller collar, and compactness gives a neighborhood of that
closure disjoint from K. This concerns J; the diagonal density zero
has not been removed or identified with a complex point.

Write s=tr A, B=A-(s/2)I, and d=det B. Then

\[
                 J=1-s^2/4-d-is.                          \tag{7}
\]

On K, s=0 and d=1. If K is empty there is nothing to localize:
take chi=0 and A_epsilon=A. Otherwise choose an exchange-invariant
open neighborhood V of K, with closure away from the smaller collar
and with d>1/2 throughout its closure. Choose a smooth cutoff chi
equal to 1 on a neighborhood W of K and supported compactly in V.
It may be made exchange-invariant by averaging with its exchanged
copy. Both K and the chosen neighborhoods can be invariant because
s,d,J and f are invariant under exchange. This is an ordinary finite
smooth-cutoff construction on the torus; it changes no surface data.

Put f=P+iQ. On V, for t>=0 define

\[
 \begin{split}
 s_t&=s+t\chi Q,\\
 D_t&=d+(s^2-s_t^2)/4-t\chi P,\\
 \lambda_t&=\sqrt{D_t/d},\qquad
 A_t=(s_t/2)I+\lambda_t B.                                \tag{8}
 \end{split}
\]

Take

\[
 E=\sup_{\bar V}\left(|P|+|sQ|/2+Q^2/4\right),\qquad
 \epsilon_0=\min\{1,[4(1+E)]^{-1}\}>0.
\]

For 0<=t<=epsilon_0 the numerator obeys

\[
 D_t=d-t\chi(P+sQ/2)-t^2\chi^2Q^2/4
       \geq\tfrac12-tE>\tfrac14.                          \tag{9}
\]

Thus (8) defines real C1 fields and a continuous homotopy. Where
chi=0 it gives s_t=s, lambda_t=1 and A_t=A. Define A_t=A outside
V; compact support of chi makes the definitions agree on an open
overlap. There is no division by d outside V. Taking trace and
determinant in (8) gives

\[
 \operatorname{tr}A_t=s_t,\quad
 \det A_t=s_t^2/4+D_t=s^2/4+d-t\chi P,
\]

which proves (4) exactly. All expressions commute with coordinate
exchange, so A_t(t_2,t_1)=S A_t(t_1,t_2) S, where S swaps the two
coordinates.

### The ambient lift and its normalization

For every real A_t, the columns of I-iA_t are independent over R:
their real parts are the standard real basis. Multiplication by the
fixed invertible complex matrix H preserves this property. Thus (3)
is an actual oriented plane field, and at t=0 its columns are exactly
the two derivatives of Phi_u. It is a homotopy of its Gauss map, not
a scalar prescription without a geometric lift. It is stationary
near the closed smaller collar. Only planes are changed anywhere.

Let M_t=H(I-iA_t) and let E_t be its real Gram matrix,
(E_t)_{ab}=Re sum_j conjugate((M_t)_{ja})(M_t)_{jb}. It is positive
definite. Orthonormalizing by the positive real matrix E_t^(-1/2)
preserves orientation, so the source's determinant map pi satisfies

\[
 \pi(g_t)=\frac{\det_{\mathbb C}M_t}{\sqrt{\det E_t}}
         =\frac{-z_1z_2}{\sqrt{\det E_t}}\,J_t.             \tag{10}
\]

Consequently the complex-plane contacts of g_t are precisely the
zeros of J_t. The multiplier in (10) is nonzero on the whole torus.
Its winding is zero on a loop bounding a small disc, since it extends
nonvanishingly over that disc. No claim of zero winding on arbitrary
noncontractible torus loops is needed or made. In particular (4)
does not assert an additive perturbation of the normalized pi.

### The zero set after perturbation, including originally nonisolated contacts

Multiplying (4) by the original, fixed f gives

\[
                         fJ_t=q+t\chi|f|^2.               \tag{11}
\]

Both terms on the right are real nonnegative. For t>0, if J_t=0
and chi>0, (11) forces f=0 and then J=0. If chi=0 and J_t=0,
then J=0, contradicting chi=1 on K. Conversely f=J=0 implies
J_t=0. Hence for every such t the contact set is exactly Z. At its
points P=Q=0, so (8) also gives A_t=A and g_t=g_0 there.

This identity removes every original complex point off the form's
divisor, including nonisolated sets of such points. To analyze the
remaining set, first observe that z_1=z_2 forces theta_1=theta_2
modulo 2pi. Those points lie on the prescribed diagonal, which is
contact-free by (6). Thus the diagonal factor in F is nonzero at
every point of Z.

At any p in K, write

\[
 A(p)=\begin{pmatrix}a&b\c&-a\end{pmatrix},\qquad
                     bc=-(1+a^2)<0.                       \tag{12}
\]

The real Jacobian determinants of the two coordinate maps, relative
to the original angular orientation and the usual complex-plane
orientation, are

\[
 \det_{\mathbb R}Dz_1(p)=-|z_1(p)|^2b,\qquad
 \det_{\mathbb R}Dz_2(p)= |z_2(p)|^2c.                     \tag{13}
\]

They are nonzero with a common sign sigma_p=sign(-b)=sign(c).
The tangent plane at p is complex, and its z_1 projection is a
nonzero complex-linear map, so sigma_p is precisely whether its
complex orientation agrees with the original surface orientation.

Here is the full local isolation check, without assuming analyticity
of u. Write L_j=Dz_j(p), an invertible real-linear map. For a small
real increment h,

\[
 z_j(p+h)-z_j(p)=L_j h+r_j(h),\qquad r_j(h)=o(|h|).
\]

With c_j=min_{|v|=1}|L_jv|>0, shrink a disc about p until
|r_j(h)|<c_j|h|/2 for both j. Then z_j(p+h) != z_j(p) for
every h!=0 in this disc. Shrink further so the only possible zero
of G in each coordinate image is its center z_j(p), if that is a
zero, and so z_1-z_2 stays nonzero. These restrictions follow from
the isolated zeros of the nonzero entire G and continuity. For
p in Z at least one n_j is positive, and the exact local factorization
is

\[
 f(\theta)=U(\theta)
       \prod_{j:n_j>0}(z_j(\theta)-z_j(p))^{n_j},           \tag{14}
\]

where U is continuous and nonzero on the full disc. The factors with
n_j=0 are included in U, along with both coordinate denominators and
the retained, locally nonzero diagonal factor. Thus f has exactly
one zero on this disc, namely p. In particular p is isolated in Z.
As Z is closed in the compact torus, it is finite: an infinite closed
subset would have an accumulation point in Z, contradicting the
local isolation just proved. No finite census of the original K was
assumed.

### Both local signs, without nondegeneracy

Orient a small circle about p by the original angular orientation.
The first-order bound above homotopes z_j(p+h)-z_j(p) on that circle
to L_jh without a zero. The oriented ellipse L_j(circle) winds
sigma_p times about zero. Since U extends nonvanishingly over the
disc, (14) yields

\[
                      \operatorname{wind}_\theta f
                         =\sigma_p N_p.                   \tag{15}
\]

Take the disc also inside W. For t>0, (11) is strictly positive
on its punctured part, because chi=1 and f!=0 there. Therefore

\[
 \operatorname{wind}_\theta J_t
   =-\operatorname{wind}_\theta f=-\sigma_p N_p.           \tag{16}
\]

The conversion from this determinant winding to the relevant Lai
local degree is

\[
                 I_p=\sigma_p\operatorname{wind}_\theta
                                \pi(g_t).                 \tag{17}
\]

For clarity, this is not an identification of the two orientation
classes. Near a complex plane, choose fixed complex-linear coordinates
(W,V) making that plane V=0. Nearby planes are real graphs
V=alpha W+beta conjugate(W), with their orientation either agreeing
or disagreeing with complex W. In the agreeing orientation, their
frame determinant is -2i beta; normalization multiplies it by a
positive scalar. The complex-plane locus is beta=0. The source's
local-index convention uses the complex orientation on the parameter
disc, giving the extra sigma_p in (17) when that differs from the
original one. Reversing the plane orientation changes the frame
determinant only by -1, but Lai reverses the orientation on the
negative complex-plane locus; hence the same formula (17) applies
in that class, not the uncorrected winding in (16).

One can check the normal orientation directly in Lai's real graph
coordinates (the orientation calculation preceding Theorem 4.8,
pp15–16). Write alpha=a+ib and beta=c+id. The normal components
of the two complex-W-oriented frame vectors are
(a+c,b+d) and (-b+d,a-c). The real-linear change from (a,b,c,d)
to (a+c,b+d,-b+d,a-c) has determinant +4. The complex orientation
on the positive complex-plane locus is the (a,b) orientation, so
its normal orientation is (c,d), the beta orientation. Plane
orientation reversal preserves the four-dimensional Grassmannian
orientation: reversing the W-basis from (1,i) to (1,-i) and the
V-normal basis from (1,i) to (1,-i) preserves the ambient real
orientation. In the four graph entries this changes
(x_1,x_2,y_1,y_2) to (x_1,-x_2,-y_1,y_2), with determinant +1.
Lai's prescribed reversal of the negative locus therefore reverses
its normal orientation. The degree is accordingly +wind(beta) at
the positive locus and -wind(beta) at the negative one. This proves
(17) for the plane maps used here, with no integrability assumption
on the perturbed planes.

To check that this coordinate calculation applies to the actual
frame M_t, shrink the contact disc so its W-projection is a real
isomorphism on every plane g_t(theta). Its ordered projected frame
has real determinant of constant sign sigma_p. In the fixed complex
coordinates its determinant is therefore -2i beta times that
nonvanishing real determinant. The fixed complex coordinate change
adds a nonzero constant, and Gram normalization adds a positive
factor. All these factors extend nonvanishingly over the disc, so
none changes the boundary winding. This verifies the use of pi(g_t)
in (17), including the negative class, without applying a graph-of-a-
surface theorem to an arbitrary plane field.

For an isolated degenerate zero the local intersection degree means
the winding on this small boundary circle. Normal-coordinate degree
and the cited Poincare-dual pairing give the same contribution; no
generic perturbation or simple zero is needed. Equations (10),
(16) and (17) now prove I_p=-N_p in both classes. Every possible
contact of g_t was included in the finite set Z.

### The two zero totals at C2 regularity

The original C2 surface has a C1 Gauss map, and all maps (3) are
C1. Their continuous class pullbacks and the preceding local degrees
are defined at this regularity. We can compute the two totals without
invoking a sign-preserving smoothing, or applying a smooth embedding
theorem directly to the C2 surface.

For a fixed positive t, consider the explicit plane homotopy

\[
 h_r(\theta)=\operatorname{span}_{\mathbb R}^{\rm or}
            [H(\theta)(I-irA_t(\theta))],\quad 0\leq r\leq1.
                                                               \tag{18}
\]

Its columns are real independent for the same reason as in (3).
At r=1 it equals g_t. At r=0 its columns are complex independent,
so its image avoids both complex-plane loci. A Poincare-dual class
of either locus restricts to zero on that complement. Homotopy
invariance of the pairing therefore makes both totals for g_t zero.
This auxiliary homotopy computes the class pairing only; it is not
asserted to be a collar-relative surface deformation. The actual
lift (3)–(4) is collar-relative and fixes the surface everywhere.

Here the local-degree summation is the topological interpretation
of the cited class, not a transversality assumption. Write
\(\mathcal G\) for the oriented Grassmannian and \(\mathcal C_+\) and
\(\mathcal C_-\) for its two complex-plane loci. For either sign the
Poincare-dual class is the image of its normal orientation class in
\(H^2(\mathcal G,\mathcal G\setminus\mathcal C_\pm;\mathbb Z)\).
Pull it back by g_t to \(H^2(T^2,T^2\setminus Z_\pm;\mathbb Z)\),
where \(Z_\pm=\{p\in Z:\sigma_p=\pm1\}\). Excision identifies the latter
group with the sum of the local disc groups. In the coordinates
above each integer is the boundary degree with the chosen normal
orientation, exactly (17). The image in H^2(T^2; Z), evaluated
on the oriented torus, is their sum. This also covers an empty
\(Z_\pm\). Only continuous maps of pairs and their homotopy invariance
enter; C1 is more than sufficient. Degenerate contacts need neither
smoothing nor a regular-value perturbation.

Equivalently these are the zero totals supplied by Lai for a smooth
embedded torus, but (18) justifies their use here for continuous
plane maps and the original C2 regularity. Locality of the class
pairing over the finitely many disjoint contact discs gives

\[
 0=I_+(g_t)=-\sum_{p\in Z:\,\sigma_p=+1}N_p,\qquad
 0=I_-(g_t)=-\sum_{p\in Z:\,\sigma_p=-1}N_p.               \tag{19}
\]

Every summand is a positive integer before its displayed minus sign.
Both sets are empty. This proves Z empty and completes the exact
prescription's localization test, including originally nonisolated
J zeros.

### Consistency checks and remaining obligations

L855 is a consistency example, not a premise. At its conditional
finite-n germ, the central matrix is [[0,-1],[1,0]], sigma=+1,
and its full J is a nonzero factor times conjugate(w)^n. Formula
(17) gives -n, agreeing with (5). This local germ has no global
torus class budget, so its existence is not contradicted. Extending
that germ to a torus under all present hypotheses would fail (19).

For coordinate exchange tau, J_t and f are invariant. The map tau
reverses the parameter orientation, while exchanging the two ambient
complex coordinates preserves complex orientation on a complex line.
More explicitly A_t(tau theta)=S A_t(theta)S; at a complex point b
and c interchange, so sigma changes sign. The winding in (16) also
changes sign and their product (17) stays -N_p. Thus exchange moves
a contact to the other class with the same negative index. There
are no fixed diagonal contacts. A mere reversal of the surface
orientation likewise reverses sigma and boundary winding together;
it does not make a positive compensating term.

The argument does not show that Z must be nonempty for any proposed
global extension of the given collar. It also does not rule out
nonisolated original J zeros at f!=0, establish a positive extension,
or settle any other order or shift. A forced common contact, actual
global matching and all-degree transfer remain separate gaps.
L853 and L854, fixed-cutoff crossings and all annular stop results
are not used. No numerical test, cross-notebook input or mathematical
script enters this proof.

The independent conceptual audit used
`drafts/literature/2026-11-06-l858-gauss-map-localization-audit.md`,
unchanged and SPECIALIZE at invocation start. It checked (8)–(11)
algebraically, the complete contact census (12)–(16), both signs
against Lai's graph-coordinate orientation on pp15–16 and negative
locus convention on pp16–17, and the continuous class pairing
(18)–(19). The expanded normal-coordinate and relative-class
paragraphs above make the last two checks explicit; no hypothesis,
conclusion or mathematical input has been strengthened. L855's
finite-n germ and coordinate exchange give the stated consistency
checks. This accepts the conditional exclusion only; a forced
common contact remains entirely unproved.

## Mathlib

Full matching coverage of this fixed-surface localization is not
checked. Coverage of the supporting Grassmannian class, local-degree,
homotopy-invariance and isolated-zero results is also not checked in
this step. The cited primary results are the standard inputs; there
is no claim of formal verification or absence from Mathlib.
