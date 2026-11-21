# Lemma 868: the one-sided dual class reduces to a nonnegative correction and a closure system

## Hypotheses

Use L847's actual entire G, positive R,C, and the forms on X=(C*)^2

\[
 F=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\qquad
 \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
 \tag{1}
\]

In particular G(0)=a_0>0. The torus T has both radii R and the
ordered angular orientation dtheta_1 wedge dtheta_2. For every real
matrix A put (E_j)_k=z_k(A_kj+i delta_kj), with this fixed order.
The proposed certificate alpha is a real C1 two-form on all X,
closed there, satisfying the **upper-only** inequality

\[
       \alpha_z(E_1,E_2)\leq |\omega_z(E_1,E_2)|
       \quad(z\in X,\ A\in\mathbb R^{2\times2}).          \tag{2}
\]

No reverse orientation, left-hand modulus, nonnegativity of alpha,
jet bound, zero exclusion, holomorphic coefficient assumption, growth
condition at an end of X, RH, or graph-existence hypothesis is added.

## Conclusion

Put x_j=log(|z_j|/R), and use local angles y_j with global closed
one-forms dy_j=Im(dz_j/z_j). Define

\[
 \eta=(dx_1+i\,dy_1)\wedge(dx_2+i\,dy_2),\qquad
 \beta=dy_1\wedge dy_2,\qquad \omega=-F\eta.
\]

The entire class (2), with closedness, consists **exactly** of

\[
 \alpha=\operatorname{Re}((q-ir)\eta)-h\beta,
 \qquad h\geq0,\qquad q^2+r^2\leq |F|^2,                 \tag{3}
\]

where q,r,h are real C1 functions on X and, in logarithmic coordinates,

\[
 r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}
                       \quad(j=1,2).                    \tag{4}
\]

These are global periodic equations on R^2 times T^2; no global
single-valued angle is required. At F=0 they force q=r=0, but the
pointwise domination does not force h=0. At J=det(I-iA)=0 the
evaluation of alpha is -h, not necessarily zero.

The real number

\[
 K=(2\pi)^{-2}\int_{[0,2\pi]^2}(q+h)(x,y)\,dy_1dy_2
 \tag{5}
\]

is independent of x. Set M=(2pi)^(-2) integral_T omega. Then

\[
 \int_T\alpha=-(2\pi)^2K,\qquad
 \int_T\alpha>\left|\int_T\omega\right|
                  \ \Longleftrightarrow\ K<-|M|.        \tag{6}
\]

If h is independent of both radial coordinates, there is no strict
gain: integral_T alpha <= |integral_T omega|. However (3)-(4) admit
globally defined, radially dependent h and nonholomorphic q-ir,
including the zero-period example constructed below. Thus the
holomorphic reduction used for L867 cannot simply be applied to
this enlarged class.

Whether any solution of (3)-(4) has K<-|M| remains unresolved.
This is an exact intermediate reduction and a scoped subclass stop,
not a full-class no-gain theorem, a strict-gain certificate, a graph
construction, or an RH result. The independent conceptual audit of
6 November 2026 below accepts this exact statement. The prior EXPLORE search did not locate
a matching full classification; that is not certified originality.

## Proof

### Assessed scope and imported inputs

The invocation-start assessment is
`drafts/literature/2026-11-06-oriented-one-sided-dual-period-test.md`.
It covers the full six-coefficient test, closedness and period question
with exactly (2), including an informative remaining case. L847
supplies (1), the actual-function properties, graph differential and
compact homotopy. L867 supplies its six-coefficient evaluation and,
only in the radial-independent-h subclass below, its audited
absolute-domination theorem. No stronger conclusion from its source
comparison is imported for (2).

For the compact-chain comparison import the C1 Stokes theorem as in
Jiří Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
31 May 2026, [Appendix C, Theorem C.6 and the following regularity
remark, p224](https://www.jirka.org/scv/scv.pdf#page=224), already
checked for L847. Its application is verified below. Cauchy-Schwarz,
compact integration of C1 functions, and the coefficient algebra are
elementary specializations; no general null-Lagrangian classification,
calibration existence, strong duality or new analytic import is used.

### The upper inequality at every matrix

Use L867's global coframe and its unique six real coefficients:

\[
 \alpha=p\,dx_1\wedge dy_1+q\,dx_1\wedge dx_2
 +r\,dx_1\wedge dy_2+s\,dy_1\wedge dx_2
 +t\,dy_1\wedge dy_2+v\,dx_2\wedge dy_2.
\]

Fix z and write A=[[a,b],[c,d]]; here c is a matrix entry. Direct
evaluation, with the same orientation as L867, gives

\[
 P(A):=\alpha(E_1,E_2)=-pb+q(ad-bc)+ra+sd+t+vc,
 \qquad J=1-\det A-i\operatorname{tr}A.                 \tag{7}
\]

For every a in R and b!=0 take d=-a, c=-(1+a^2)/b. These matrices
all have J=0 and remain within the prescribed ordered family. Hence

\[
 -pb-v(1+a^2)/b+(r-s)a+q+t\leq0.                         \tag{8}
\]

Fix a=0. Let b tend to both signed infinities: if p were nonzero,
one sign would make -pb tend to positive infinity, while the other
terms stay bounded. Thus p=0. Now let b tend to zero from both
sides; the same reasoning forces v=0. With these coefficients zero,
(8) for every real a forces r=s and q+t<=0. Set h=-(q+t)>=0.
This argument uses both signs of a permitted matrix entry, never a
reversal of E_1,E_2.

Put U=det A-1, V=tr A, and f=|F(z)|. Every real (U,V) occurs, since
A=[[0,-(U+1)],[1,V]] has these determinant and trace. The whole
remaining inequality is therefore

\[
                  qU+rV-h\leq f\sqrt{U^2+V^2}.          \tag{9}
\]

If ell=sqrt(q^2+r^2)>0, choose (U,V)=lambda(q,r), lambda>0,
divide (9) by lambda, and let lambda tend to infinity. This gives
ell^2<=f ell, hence ell<=f. If ell=0 the same conclusion is
immediate. Conversely ell<=f and h>=0 imply (9) by Cauchy-Schwarz.
All transformations were pointwise on X, with C1 coefficient
functions and no division by F or J. They establish (3) as a
necessary and sufficient pointwise condition, including f=0.

In particular the discarded equality at J=0 is not recovered:
(7) is q(det A-1)+r tr A-h, and equals -h there.

### Exact closedness and the period

Expand (3) as

\[
 \alpha=q\,dx_1\wedge dx_2+r\,dx_1\wedge dy_2
         +r\,dy_1\wedge dx_2-(q+h)\,dy_1\wedge dy_2.
 \tag{10}
\]

All four coframe elements are closed. In d alpha the coefficients
of dx_1 wedge dx_2 wedge dy_j are q_yj-r_xj, and those of
dx_j wedge dy_1 wedge dy_2 are -(q+h)_xj-r_yj, for j=1,2.
These four three-forms form a real basis. Thus d alpha=0 is
equivalent to all four equations (4). This proves necessity and
sufficiency at C1 regularity; no second derivatives are taken.

For x fixed, restriction to the angular torus sets dx_1=dx_2=0.
Its integral is therefore -(2pi)^2 times the mean in (5).
Differentiate that mean in x_j. Differentiation under the integral
is valid because q+h and its first derivatives are continuous on
each compact radial neighborhood times the angular torus. Equation
(4) gives K_xj=-(2pi)^(-2) integral r_yj=0, by periodicity.
The domain R^2 of x is connected, so K is constant. This proves
(5)-(6), with no estimate at a noncompact end and no sign assumption
on M.

For comparison, (3) gives the valid but generally insufficient bound

\[
 K\geq-\inf_{x\in\mathbb R^2}(2\pi)^{-2}
              \int_{[0,2\pi]^2}|F(Re^{x_1+iy_1},Re^{x_2+iy_2})|\,dy.
 \tag{11}
\]

Indeed K>=-mean|F| for each x. Each such compact coordinate torus
is connected to T by L847's compact homotopy, so its mean of F is
M. Triangle inequality gives mean|F|>=|M|. Consequently (11) alone
does not give the needed K>=-|M|. No equality of those thresholds
is asserted.

### The radial-independent correction is stopped

Suppose h_x1=h_x2=0. Then d(h beta)=0: the remaining derivatives
of h are angular and repeat one of the dy factors. The real C1
form alpha+h beta=Re((q-ir) eta) is globally closed and satisfies

\[
 |(\alpha+h\beta)(E_1,E_2)|
       \leq |q-ir|\,|\eta(E_1,E_2)|\leq|\omega(E_1,E_2)|.
\]

All hypotheses of L867 now apply to this form, including all zeros
and all matrices. Import its conclusion: alpha+h beta=Re(c omega)
for one constant |c|<=1. Hence

\[
 \int_T\alpha=\operatorname{Re}\left(c\int_T\omega\right)
                         -\int_T h\,\beta
                 \leq\left|\int_T\omega\right|,
\]

because h>=0 and beta is the positive angular area form on T.
This is an applicability argument for the audited local theorem,
not a reproof of its removal or Liouville inputs. Conversely, the
constant forms Re(c omega) remain admissible in the enlarged class
and attain the threshold |integral_T omega| by choosing c with the
appropriate phase (or c=0 when that period is zero). Nothing here
rules out a larger value when h has radial dependence.

### A global nonholomorphic, zero-period example

Choose delta>0 so that |G(z)|>=a_0/2 for |z|<=delta; continuity at
zero with G(0)=a_0>0 supplies such a delta. Consider the compact
annular product

\[
 \delta/8\leq |z_1|\leq\delta/4,\qquad
 \delta/2\leq |z_2|\leq3\delta/4.                        \tag{12}
\]

The two radii ranges are disjoint, and both G factors are nonzero.
Thus F is continuous and nowhere zero on (12). Its minimum modulus
m there is strictly positive by compactness. This is an existence
construction, not a numerical estimate of m or a claimed strict gain.

Let [l_j,u_j] be the logarithms, relative to R, of the two radial
intervals in (12), with centers mu_j and half-lengths ell_j>0.
Define b(s)=(1-s^2)^2 for |s|<1 and b(s)=0 otherwise. This function
is C1 because both its value and first derivative vanish at +/-1;
it lies in [0,1]. Put

\[
 \varphi(x)=b((x_1-\mu_1)/\ell_1)b((x_2-\mu_2)/\ell_2),
 \quad q=-\tfrac m2\varphi,\quad r=0,\quad h=\tfrac m2\varphi.
 \tag{13}
\]

These are global C1 functions on X. On their support, |q-ir|<=m/2
<=|F|; outside it q=r=h=0. Moreover h>=0, r_xj=q_yj=0 and
(q+h)_xj=-r_yj=0. Hence the already proved equivalence (3)-(4)
verifies every plane inequality and closedness on all X. Equivalently,
the resulting form is simply q(x) dx_1 wedge dx_2; its derivative
vanishes because q depends only on the two x coordinates.

Its angular restriction is zero, so K=0 and its period is zero.
The real coefficient q is nonconstant and has a nonzero radial
derivative at an interior point of the support; since it is
angle-independent, its antiholomorphic derivative in that coordinate
is nonzero. Thus q-ir is not holomorphic. Also h_xj is not identically
zero. This is a rigorous witness that the remaining radial dependence
cannot be eliminated just by closedness, all-X control and (2).
It is not evidence for a positive period gap.

### Downstream meaning and remaining obstruction

For any C2 periodic L847 graph, the tangent pair is exactly E_1,E_2
with A=Du and the positive angular orientation. Integrating (2)
gives integral Phi_u^*alpha <= integral |q_u| dy. The homotopy
Phi_(tu) is C2 with compact image in X; pulling the C1 closed alpha
back to [0,1] times T^2 yields a C1 closed form. The cited C1 Stokes
theorem therefore gives integral Phi_u^*alpha=integral_T alpha.
There are just the two endpoint boundaries with L847's orientations;
F=0 and J=0 introduce no new boundary or singularity.

If the full pullback q_u is real nonnegative everywhere, then
integral |q_u|=|integral_T omega| by L847's same homotopy for omega.
Thus a solution of (3)-(4) with K<-|M| would obstruct every such graph.
This proves the required one-sided sufficient comparison directly;
it assumes neither domination on reversed planes nor strong duality.

The full remaining case is exactly the global periodic C1 system
(3)-(4) with radial dependence in h and K<-|M|. The example (13)
has K=0 and does not reach that threshold. Bound (11) leaves the
same gap. No further all-class inequality or construction has been
established. Other graph constructions, higher signs and actual-Xi
all-degree mixed positivity remain independent unresolved steps.

### Independent conceptual audit, 6 November 2026

The invocation-start EXPLORE assessment was
`drafts/literature/2026-11-06-one-sided-dual-reduction-audit.md`.
The complete proof above was checked using L847's actual form and
compact-cylinder interface and L867's already audited theorem. The
parent literature comparison was reused at its recorded source
versions; no new analytic input or full-class period theorem is
imported. This audit verifies the existing reduction and applications,
not a stronger result or a claim of originality.

For the six coframe wedges in their displayed order, the independent
evaluations on E_1,E_2 are

\[
             -b,\quad ad-bc,\quad a,\quad d,\quad1,\quad c.
\]

Also eta(E_1,E_2)=det A-1+i tr A=-J, so omega(E_1,E_2)=FJ.
Thus (7) and its orientation are correct. On the J=0 family,
with a=0 fixed, the term -v/b tends to zero as b tends to either
signed infinity, while q+t is fixed. This forces p=0. With p=0,
the two signed limits b->0 force v=0. The remaining inequality is
(r-s)a+q+t<=0 for every real a, giving r=s and h=-(q+t)>=0.
None of these tests reverses the ordered plane. The companion matrix
has determinant U+1 and trace V. Positive scaling in (9), with
q,r,h fixed at z, gives ell^2-h/lambda<=f ell and then ell<=f;
the ell=0 case and the converse Cauchy--Schwarz bound are included.
At F=0 this gives q=r=0, leaving alpha=-h beta; at every J=0,
alpha(E_1,E_2)=-h. Neither zero set has been discarded.

Writing S=q+h, direct exterior differentiation of (10) gives

\[
\begin{split}
d\alpha={}&(q_{y_1}-r_{x_1})\,dx_1\wedge dx_2\wedge dy_1
 +(q_{y_2}-r_{x_2})\,dx_1\wedge dx_2\wedge dy_2\\
 &-(S_{x_1}+r_{y_1})\,dx_1\wedge dy_1\wedge dy_2
  -(S_{x_2}+r_{y_2})\,dx_2\wedge dy_1\wedge dy_2.
\end{split}
\]

These are four independent three-form components. This checks every
sign and both directions of (4) without taking second derivatives.
The coframe and coefficients are global on X and periodic on the
angular cover, so this local calculation proves global closedness.

Restriction to a coordinate torus gives alpha=-S beta and
omega=F beta. Compact differentiation and angular periodicity give
partial_xj mean(S)=-mean(r_yj)=0, hence one constant K on all R^2.
For I=integral_T omega=(2pi)^2 M, the strict inequality is
-(2pi)^2 K>|I|, exactly K<-|M|. The infimum direction in (11) is
also correct: K>=-mean|F| for every x implies K>=-inf_x mean|F|.
Homotopy invariance gives mean F=M at every such torus, so
inf_x mean|F|>=|M|. Its negative is at most -|M|, which confirms
that the available lower bound cannot by itself supply the desired
one. This uses no limit at either end of X.

When h_x1=h_x2=0, the angular terms in dh wedge beta repeat a
dy factor and vanish. Therefore alpha+h beta is a real C1 closed
form on all X. Its absolute evaluation is bounded by
sqrt(q^2+r^2)|eta(E_1,E_2)|<=|FJ| everywhere, including all zeros.
These are exactly L867's hypotheses. Its conclusion and the positive
orientation of beta on T give the stated no-gain inequality. The
phase c=conjugate(I)/|I| when I!=0, and c=0 when I=0, verifies
attainment within the constant subclass. The original alpha has not
been asserted to satisfy absolute domination.

For (12), both coordinates lie in the closed disc of nonvanishing G,
neither is zero, and |z_1-z_2|>=|z_2|-|z_1|>=delta/4.
Consequently the continuous modulus of F has a positive minimum m
on the entire compact annular product, with all angular values
included. At either endpoint of the bump, its value and derivative
are zero; the extension in (13) is therefore C1 across every edge
and corner of the product support. On that support |q|<=m/2<=|F|,
and off it q=r=h=0. Its angle independence and S=0 verify (4)
on all X, including the support boundary and every F zero outside
the annuli. At x_1=mu_1+ell_1/2, x_2=mu_2 one has
q_x1=3m/(4ell_1)>0. In the local holomorphic coordinate
w_1=x_1+i y_1, partial_bar_w1(q-ir)=q_x1/2!=0.
Thus the example is actually nonholomorphic and radially dependent,
while S=0 gives K=0 exactly. It is no strict-gain witness.

Finally, for each C2 periodic graph the homotopy Psi(t,theta)=
Phi_(tu)(theta) is C2 on the compact parameter cylinder and stays
in a compact product of annuli in X. Pulling back C1 alpha gives
a C1 two-form with d(Psi^*alpha)=Psi^*(d alpha)=0. The cited
Lebl C1 Stokes theorem therefore applies, with positive t=1 and
negative t=0 angular orientation and no side boundaries. The same
argument for omega gives its common period I. Integration of the
upper-only inequality on the graph yields integral_T alpha<=
integral |q_u| dy; if q_u is real nonnegative, its right side is
|I|. Numerator zeros and J zeros are regular points of this pullback
argument and introduce no boundaries. This verifies precisely the
conditional obstruction stated above.

No mathematical defect was found, and no statement or hypothesis
needed repair. The coefficient equivalence, C1 closure, period sign,
global example, subclass theorem application and downstream Stokes
comparison are accepted. The full strict-period problem is still
open. This is an independently checked local input, with no new
mathematics beyond the submitted result, no numerical evidence,
no new DAG dependency and no RH conclusion.

## Mathlib

Full matching theorem and supporting formal coverage were not checked;
unknown coverage is not evidence of absence. This is an informal
coefficient/closedness reduction and explicit C1 example, with the
scoped import of L867 and the stated Stokes theorem. The independent
informal audit above is complete; no formal verification, mathematical
script or numerical evidence is claimed.
