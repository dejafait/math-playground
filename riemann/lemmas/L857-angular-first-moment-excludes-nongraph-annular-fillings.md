# Lemma 857: the first angular observable excludes the prescribed non-graph fillings

## Hypotheses

Use the actual data and fixed chart of L855/L856. In particular,
G(z)=xi(1/2+sqrt(z)/2)/8 is defined by its entire power series,
R=R_1>0 and C=R^2/G(R)^2>0 have the inherited L775/L847 normalization,
zeta eta!=0, G(zeta)=0 has fixed finite multiplicity n>=1, and
G(eta)(zeta-eta)!=0. The full form is

\[
 \omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                  dz_1\wedge dz_2.
\]

Keep the original product of discs D times E about (0,eta) in L855,
its nonvanishing H, and the unchanged inverse chart B with

\[
 z_1=\zeta+w,\quad z_2=h(w,v),\quad
 \omega=w^n dw\wedge dv,\quad
 h_w(0,0)=0,\quad h_v=1/H(w,h),\quad H_0=H(0,\eta)\ne0.
                                                               \tag{1}
\]

The inverse image lies in that original product. Retain its fixed
logarithm branches normalized to zero at the base pair, and the original
angle lifts theta^0. Put

\[
 \begin{split}
 A&=-iH_0\eta/\zeta,\qquad d_n=1-2^{-2n-2},\qquad
 \beta=2d_n/(n+1),\qquad b_r=\beta r^{2n+3},\\
 v_0(w)&=Aw+\frac{i}{n+1}\bar w^{n+1},\qquad
 v_{\rm out}(w)=v_0(w)+i b_r w^{-n-2}.
 \end{split}                                                   \tag{2}
\]

Prescribe exactly L856's inner circle |w|=r/2 on v_0 and outer
circle |w|=r on v_out, with their inward collar portions: the surface
near the inner boundary agrees with v_0 for |w|>r/2, and near the
outer boundary with v_out for |w|<r. The circles have the original
angular orientation, giving outer counterclockwise and inner clockwise
induced boundary orientations in w. The collars themselves extend to
the open neighborhoods specified in L856.

Consider a smooth compact oriented embedded annulus Sigma in B with
exactly these boundary circles and collar agreement. Require
dTheta_1 wedge dTheta_2 to be strictly positive on its oriented tangent
planes and the pullback of omega to be real nonnegative everywhere.
Zeros of omega and of w are allowed. Do not require Sigma to be a graph
over w, impose a bound on its w image, or shrink its allowed chart B.

## Conclusion

For every sufficiently small r>0, no such Sigma exists. All constants
and the radius threshold may depend on the fixed pair, n and chart.
The single observable used is exactly

\[
 \ell=(1,0)T^{-1}(\Theta-\theta^0),\qquad
 T=\begin{pmatrix}t&p\\-p&t\end{pmatrix},\qquad
 1/\zeta=p+it.                                                \tag{3}
\]

Its necessary full-form-weighted value is 2r+O(r^2) after normalization
by L856's positive mass M_0. Its maximum on any hypothetical Sigma is
at most r+O(r^2). Below, the unnormalized violation is at least
r M_0/2 for all radii within an explicit fixed-constant threshold.

This strengthens the graph-only obstruction for these prescribed local
collars. It neither identifies them with actual exterior contour data
nor excludes other collars, a surface leaving B, or a surface without
strictly positive original angular projection. It proves no Xi minor
sign, global matching/homology/exchange statement, other-order positivity
or RH conclusion. This known-tool specialization is REPRODUCTION under
the prior SPECIALIZE assessment. Its first independent conceptual audit
on 6 November 2026 accepts precisely this fixed-chart obstruction.
No novelty beyond the inspected sources is claimed.

## Proof

### Imported tools and the scope of the calculation

Use the unchanged invocation-start assessment
`drafts/literature/2026-11-06-nongraph-angular-observable-test.md`
and the completed source comparison it cites. The precise standard
inputs, already inspected there, are:

- Jiří Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
  31 May 2026, [Theorem C.6 and its proof, p224](https://www.jirka.org/scv/scv.pdf#page=224):
  Stokes for a compact smooth oriented manifold with boundary, with
  induced boundary orientation. Apply it componentwise to complex
  smooth one-forms. Projection injectivity is not a hypothesis.
- The same book, [Theorem 1.2.1 and proof, pp20–21](https://www.jirka.org/scv/scv.pdf#page=20):
  joint holomorphic power series on polydiscs, absolute uniform
  convergence on compact subpolydiscs, and the converse. This justifies
  the parameter-dependent segment primitives as in L855.
- Lebl, *Basic Analysis I*, v6.3,
  [Theorem 7.5.6, p290](https://www.jirka.org/ra/realanal.pdf#page=290)
  and [Lemma 4.2.2 and proof, pp162–163](https://www.jirka.org/ra/realanal.pdf#page=162):
  attainment of extrema on a nonempty compact metric space and Fermat's
  derivative test at an interior extremum. Apply Fermat in each local
  real coordinate. *Basic Analysis II*, v6.3,
  [Theorem 8.3.7, p38](https://www.jirka.org/ra/realanal2.pdf#page=38)
  supplies the chain rule.
- Philipp J. di Dio and Konrad Schmüdgen, *The multidimensional
  truncated Moment Problem: The Moment Cone*,
  [arXiv:1809.00584v1, positivity (5), pp4–5, Definition 5, p5,
  and Proposition 24(i), p12](https://arxiv.org/pdf/1809.00584v1#page=12):
  positive integration is nonnegative on a nonnegative test function.
  Here the measure is a smooth nonnegative two-form on compact Sigma,
  and the only tests needed are 1 and the bounded function ell.

L855 supplies the joint chart and its original tangent, and L856 supplies
the exact admissible collars and their periods. These standard theorems
are imported, not reproved. The difference requiring calculation is the
fixed angular observable, its primitive on the whole B, and its boundary
error relative to a vanishing M_0. No general filling theorem or new
maximum-principle theorem is assumed.

### An ambient primitive throughout the unchanged chart

Write D_0=p^2+t^2>0 and a=(a_1,a_2)=(t,-p)/D_0. On the original
product use the normalized holomorphic logarithms

\[
 L_1(w)=\log((\zeta+w)/\zeta),\qquad L_2(z)=\log(z/\eta),
 \quad \psi(w,z)=a_1 L_1(w)+a_2 L_2(z).
\]

These logarithms exist on the original discs: each disc avoids the
relevant zero, and the primitives of 1/(zeta+w) and 1/z along segments
give the normalized branches. Equivalently these are the branches
used in L855, continued over their discs. The derivative and value at
the base point identify each exponential with its stated ratio, so
the normalization agrees with the fixed angle lifts. This uses the
star-like primitive theorem already imported in L855: Lebl,
*Guide to Cultivating Complex Analysis*, v1.10,
[Corollary 3.2.12 and proof, pp67–68](https://www.jirka.org/ca/ca.pdf#page=67).
No change of branches or restriction of the hypothetical Sigma is made.

Define on the entire original product, and then on all B,

\[
 K(w,z)=\int_\eta^z H(w,t)\psi(w,t)\,dt,\qquad
 Q(w,v)=K(w,h(w,v)),\qquad f(w,v)=\psi(w,h(w,v)).              \tag{4}
\]

The segment remains in E. Joint holomorphicity and K_z=H psi follow
by the compactly convergent power-series argument of L855, now applied
to the holomorphic product H psi. For a point anywhere in D times E,
choose smaller concentric discs containing it and the segment, with
closures inside the original product; termwise integration on these
discs proves the identity locally at that point. Thus it holds on the
whole product, not just near the base pair. Composition with the fixed
inverse h proves that Q is holomorphic throughout B and, by (1),
Q_v=K_z h_v=f. Consequently

\[
 \alpha=-w^n Q\,dw,\quad d\alpha=f\omega,
 \qquad \alpha_0=-w^n v\,dw,\quad d\alpha_0=\omega.          \tag{5}
\]

The sign is positive because -dv wedge dw=dw wedge dv. These smooth
ambient one-forms are defined even at w=0; no division by w or omega
occurs. Their construction does not require B to be vertically convex
or contractible: the integration is performed in the original product.

The angle definitions give ell=Im(f). Let iota denote the inclusion of
a hypothetical Sigma and put mu=iota^*omega. By hypothesis mu is real
nonnegative. Hence

\[
 \ell\,\mu=\operatorname{Im}\bigl(\iota^*(f\omega)\bigr),
 \quad \int_\Sigma\ell\,\mu
       =\operatorname{Im}\int_{\partial\Sigma}\alpha,
 \quad \int_\Sigma\mu=\int_{\partial\Sigma}\alpha_0=M_0.
                                                               \tag{6}
\]

Stokes applies because Sigma is compact smooth with boundary and the
ambient forms are smooth on a neighborhood of it. Formula (6) uses the
reality of the restricted form. It does not assert that ell omega is
closed as an ambient form, or that a logarithm restricted to Sigma is
holomorphic in a real surface parameter.

### The angular maximum is attained on the boundary

Strict positivity of dTheta_1 wedge dTheta_2 means that dTheta is an
invertible map from every tangent plane of Sigma to R^2. Since a is
nonzero, d ell=a dTheta is nonzero on each such plane. By the coordinate
Fermat test, ell cannot have an interior local maximum or minimum.
Compactness gives extrema, so in particular

\[
                   \max_\Sigma\ell=\max_{\partial\Sigma}\ell.
                                                               \tag{7}
\]

This argument applies at zeros of mu and w and at folds of the w
projection. It requires only the angular projection to have full rank.

### A fixed compact neighborhood for boundary estimates only

Choose rho>0 such that (w,Aw+u) lies in B for |w|,|u|<=2rho;
its image is a compact subset of B. This is possible by openness at
(0,0). We use this smaller set only to estimate the prescribed circles,
not to constrain the rest of Sigma. Define

\[
 \widetilde f(w,u)=f(w,Aw+u),\quad f_0(w)=\widetilde f(w,0),
 \quad Q_0(w)=Q(w,Aw).
\]

The functions f_0 and Q_0 are holomorphic for |w|<2rho. The normalized
logs give f_0(0)=0. Using h_w(0,0)=0 and h_v(0,0)=1/H_0,

\[
 f_0'(0)=\frac{a_1}{\zeta}+\frac{a_2 A}{\eta H_0}
        =\frac{(t+ip)(p+it)}{D_0}=i.                         \tag{8}
\]

Thus there are finite nonnegative fixed constants C_2,C_1 with

\[
 |f_0(w)-iw|\leq C_2|w|^2,\qquad
 |\partial_u\widetilde f(w,u)|\leq C_1
       \quad(|w|,|u|\leq\rho).                              \tag{9}
\]

For the first inequality extend (f_0-iw)/w^2 holomorphically at zero
and take its maximum modulus on the compact disc; the second is the
maximum of a continuous derivative on a compact polydisc. Since Q_v=f,
integration along the u segment within this compact set gives

\[
 Q(w,Aw+u)=Q_0(w)+f_0(w)u+\mathcal R(w,u),
       \qquad |\mathcal R(w,u)|\leq\tfrac12 C_1|u|^2.        \tag{10}
\]

Indeed subtract f_0 from the integrand f(w,Aw+tau u), and use (9)
to bound the difference by C_1 tau |u|, then integrate 0<=tau<=1.

Put K_n=(1+2d_n)/(n+1). On each prescribed circle write v=Aw+u.
The exact traces (2) give

\[
 |u|\leq K_n r^{n+1},\qquad |w|\leq r.                     \tag{11}
\]

For the inner circle this follows from |u|=(r/2)^(n+1)/(n+1).
For the outer circle the two summands have moduli r^(n+1)/(n+1)
and beta r^(n+1). Take r<1, r<rho and K_n r^(n+1)<rho, in addition
to L856's collar-admissibility threshold. All estimates (9)–(10)
then apply. From (9) and (11), and n>=1,

\[
 |\ell-\operatorname{Re}w|
 \leq C_2r^2+C_1K_n r^{n+1}\leq C_\theta r^2,
 \quad C_\theta=C_2+C_1K_n.
\]

Equations (7) and (11) therefore imply

\[
                 \max_\Sigma\ell\leq r+C_\theta r^2.       \tag{12}
\]

### Boundary periods and the error at the required scale

Write the boundary integral as the outer counterclockwise integral
minus the inner counterclockwise integral. Collar agreement fixes these
signs: the inward side is |w|<r at the outer boundary and |w|>r/2 at
the inner one, and strict angular positivity agrees with L856's dx wedge
dy orientation there. No global w-graph assumption enters.

The contribution of -w^n Q_0(w) dw on either circle is zero by its
holomorphic power series (every power has exponent at least n>=1).
The leading term from (8)–(10) is -i w^(n+1)u dw. Replacing u by v
adds the holomorphic term i A w^(n+2) dw, whose integral is also zero.
Consequently, using the exact L856 periods,

\[
 \int_{\partial\Sigma}\alpha=iM_1+\mathcal E_r,\qquad
 M_0=c_n r^{2n+2},\quad c_n=\frac{2\pi d_n}{n+1}>0,\quad
 M_1=2rM_0.                                                  \tag{13}
\]

In particular the Laurent term has been included: in M_1 it contributes
-i b_r times the counterclockwise integral of w^-1 dw, namely
2pi b_r. Its M_0 contribution integrates w^-2 and is zero. The
antiholomorphic term contributes 2pi s^(2n+2)/(n+1) to the constant
period of a radius-s circle and zero to the first period. These are
exact identities from L856; no Laurent term is extended across zero.

For completeness, bound every remaining term of (10) on a circle
|w|=s with s=r or r/2. The absolute integral is at most

\[
 2\pi s^{n+1}\left(C_2 s^2 K_n r^{n+1}
                         +\tfrac12 C_1K_n^2 r^{2n+2}\right).
\]

Adding the two circles and using s<=r gives

\[
 \begin{split}
 |\mathcal E_r|&\leq4\pi C_2K_n r^{2n+4}
                      +2\pi C_1K_n^2 r^{3n+3}
                 \leq E_n r^{2n+4},\\
 E_n&=4\pi C_2K_n+2\pi C_1K_n^2,\qquad C_I=E_n/c_n.
 \end{split}                                                   \tag{14}
\]

The last inequality uses r<=1 and 3n+3>=2n+4 for n>=1, including
equality at n=1. Thus the error is O(r^2 M_0), smaller than the
needed separation scale r M_0. Taking imaginary parts in (6),(13)
and using (14) gives

\[
              \int_\Sigma\ell\,\mu
                       \geq M_0(2r-C_I r^2).                \tag{15}
\]

On the other hand mu is a finite positive measure of mass M_0>0.
Applying positive integration to (max_Sigma ell)-ell and then (12)
requires

\[
              \int_\Sigma\ell\,\mu
                       \leq M_0(r+C_\theta r^2).            \tag{16}
\]

For all the previous smallness conditions and
r<1/[2(1+C_I+C_theta)], the lower bound in (15) exceeds the upper
bound in (16) by at least r M_0/2>0. This is impossible.
All constants were fixed before r, and no estimate depended on a
choice or size of Sigma inside B. This proves the conclusion.

The calculation uses only the approved first angular observable.
It closes this specified change of projection class; it does not turn
the arbitrary collar data into actual global Xi data or address the
independent all-degree mixed-positivity gap.

### First independent conceptual audit — 6 November 2026

Under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-nongraph-angular-observable-audit.md`,
the audit accepts the complete proof (1)–(16), without a mathematical
repair or stronger conclusion. L855 supplies the original product,
joint chart and tangent; L856 supplies the prescribed collars and
periods. The actual G and full-form normalization agree with the stated
L775/L847 inputs. No additional direct mathematical dependency is used.
The standard results cited above are reused with their recorded
hypotheses, not asserted as new general theorems.

For the whole-chart issue, the disc D avoids w=-zeta and the disc E
avoids z=0. Their segment primitives define the normalized logarithms
uniquely; near the base point they agree with the fixed angle lifts.
For any point of D times E there are smaller concentric polydiscs,
with closures in D times E, containing that point and its integration
segment. The power series for H psi converge absolutely uniformly on
these compact sets. Termwise integration produces K and K_z=H psi
there; these local identities belong to the single segment integral
(4), so they agree on overlaps and hold on the entire product.
Composition with h therefore gives Q_v=f everywhere on the original B.
This argument uses neither h(w,0)=eta globally nor segments inside B.
In (5) the Q_w term wedges with dw to zero, and the Q_v term has the
positive sign from -dv wedge dw. Both primitives are smooth at w=0.

The coefficients a_1,a_2 are real and not both zero, so the normalized
logs give ell=Im f on all B. For mu=iota^*omega real, multiplying by
f and taking imaginary parts gives ell mu even at a zero of mu.
This establishes (6) without ambient closedness of ell omega.
Compactness of Sigma and smoothness of the ambient primitives justify
Stokes. At every interior point, positivity of the angular two-form
implies that dTheta is an isomorphism of real tangent planes; its
composition with the nonzero row a cannot vanish. Fermat and compact
extrema therefore give (7), even where w=0 or its projection folds.

For the boundary signs, the collar w-parametrizations have positive
angular determinant and hence give the orientation of Sigma. In polar
w-coordinates the outer outward normal is +partial_s and the inner
outward normal is -partial_s. The induced tangents are respectively
+partial_phi and -partial_phi. Thus Stokes gives outer CCW minus inner
CCW independently of the w projection away from the collars.
The boundary traces, with conjugate(w)^(n+1)=s^(2n+2)w^(-n-1), give
P_0(s;v_0)=2 pi s^(2n+2)/(n+1) and P_1(s;v_0)=0. The Laurent
increment contributes zero to P_0 and +2 pi b_r to P_1. This follows
from the circle powers -2 and -1 respectively. For alpha's leading
term -i w^(n+1)v dw the latter increment is +2 pi i b_r, so its
imaginary part is +M_1, not -M_1. No pole is extended across zero.

The boundary estimates use only one fixed compact sheared polydisc
inside B. Since a=(t,-p)/(p^2+t^2) and A/(eta H_0)=-i/zeta,
the derivative in (8) is (t+ip)(p+it)/(p^2+t^2)=i, also when
p=0 or t=0. All holomorphic Q_0 terms have zero circle integral.
The remaining integrand errors are bounded by
C_2 |w|^(n+2)|u| and (C_1/2)|w|^n|u|^2; multiplying by each
circle's length and adding gives exactly the upper bounds (14).
Division by M_0=c_n r^(2n+2)>0 therefore loses only that known
power: the normalized error is at most C_I r^2. The bound for ell
is at most r+C_theta r^2 because |u|<=K_n r^(n+1) and n>=1.
None of these estimates bounds the interior location or size of Sigma.

The limiting multiplicity check is explicit: for n=1,
d_1=15/16, beta=15/16, K_1=23/16 and c_1=15 pi/16. Thus
M_0=(15 pi/16)r^4, M_1=(15 pi/8)r^5, and each error in (14)
has order r^6. The required separation r M_0 has order r^5.
For every n>=1, 3n+3>=2n+4 gives the same strict relative saving.
With all prior radius restrictions and r<1/[2(1+C_I+C_theta)],
the lower-minus-upper bound is
M_0 r[1-(C_I+C_theta)r]>r M_0/2>0. All constants are fixed
before r and independent of the hypothetical filling.

This verifies the local conditional obstruction and closes this
specified non-graph escape. It does not show that actual exterior
contour data have these traces, impose an effective threshold uniform
in the pair or n, exclude fillings outside B or without strict angular
rank, or establish any all-degree sign. No higher observable, numerical
evidence, global filling theorem or RH assumption enters the audit.

## Mathlib

Full matching coverage of this annular obstruction is not checked.
The source assessment inspected the supporting theorem
[`IsLocalMax.hasFDerivAt_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Basic.html#IsLocalMax.hasFDerivAt_eq_zero),
which supplies the coordinate Fermat input under differentiability on
a real normed space. It does not supply this surface theorem. Coverage
of the remaining manifold Stokes, parameter-dependent primitive and
positive-integration specialization is unchecked; no absence or formal
verification claim is made.
