# L011 — Fixed-mesh expansion of the combined Ward response

## Hypotheses

Keep exactly the SU(2) box, boundary links, displacement, endpoint-averaged generator V_a, bare coupling g, Wilson flow, and two probes of L010. In particular tau = 1/16. Fix an admissible mesh a before taking g to zero. This statement uses no continuum renormalization or boundary-counterterm theorem.

Use the forest gauge of L003, with one rooted forest edge per interior vertex. Let E'_a be the remaining variable links. On the forest slice put U_e = exp(theta_e^c t^c) for e in E'_a, and set the forest links to identity. Write theta = g x; thus x_e = a A_e in the earlier convention. These are coordinates in the Lie basis -2 Tr(t^c t^d) = delta_cd, with ordinary Euclidean coordinate volume.

The following smooth gauge-invariant functions have no coupling parameter:

\[
\mathfrak j_i(U)=g^2\mathcal J_{i,a,g}(U),\qquad
F_i(U)=\mathfrak j_i(W_\tau(U)),\qquad
B(U)=V_a\mathcal S(U)-\mathfrak j_3(U)-\mathfrak j_6(U).
\tag{1}
\]

Here \(\mathcal S=4\sum_p P_p\), and the equality defining \(\mathfrak j_i\) means the g-independent numerators in L010, not a differentiation in g. All three types of function vanish to at least second order at flat links. For a smooth function G on the forest slice define its homogeneous Taylor polynomial by

\[
G_{[m]}(x)=\frac1{m!}\left.\frac{d^m}{dh^m}G(\exp(hx))\right|_{h=0}.
\tag{2}
\]

Only derivatives at zero are meant; no global logarithm is needed. Put

\[
S_m=\mathcal S_{[m]},\quad
f_{i,k}=(F_i)_{[k+2]},\quad r_k=B_{[k+2]}\quad(k=0,1,2),
\qquad M_2(x)=\frac1{12}\sum_{e\in E'_a}|x_e|^2.
\tag{3}
\]

Let \(\langle\cdot\rangle_0\) be the normalized, nondegenerate Gaussian density proportional to \(e^{-S_2(x)}dx\) on this forest slice. All cumulants below use this Gaussian. For scalar polynomial random variables define

\[
\kappa_0(X_1,\ldots,X_n)=
\sum_{\pi\in\mathcal P_n}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{A\in\pi}\left\langle\prod_{j\in A}X_j\right\rangle_0.
\tag{4}
\]

This finite partition formula also defines cumulants when a moment generating function has no neighborhood of convergence. In particular \(\kappa_0(X,Y)=\operatorname{Cov}_0(X,Y)\). Neither the higher Taylor polynomials nor their separate cumulants are identified with gauge-invariant polynomials of a Hodge Gaussian.

## Conclusion

The remaining response in the saved target has the fixed-mesh expansion

\[
\begin{split}
\mathcal R_{i,a}(g)
&=\operatorname{Cov}_{a,g}
 (\mathcal O_{i,a,g},V_aS_g-\mathcal J_{3,a,g}-\mathcal J_{6,a,g})\\
&=r_{i,a}^{G}+g^2\Gamma_{i,a}+o_a(g^2),\qquad
r_{i,a}^{G}=\kappa_0(f_{i,0},r_0),
\end{split}\tag{5}
\]

where \(r_{i,a}^{G}\) is L009's Gaussian residual response, and the coefficient is the following finite Gaussian expression:

\[
\begin{split}
\Gamma_{i,a}={}&
 \kappa_0(f_{i,2},r_0)+\kappa_0(f_{i,1},r_1)
 +\kappa_0(f_{i,0},r_2)\\
&-\kappa_0(f_{i,1},r_0,S_3)
 -\kappa_0(f_{i,0},r_1,S_3)\\
&-\kappa_0(f_{i,0},r_0,S_4+M_2)
 +\tfrac12\kappa_0(f_{i,0},r_0,S_3,S_3).
\end{split}\tag{6}
\]

The flow Taylor coefficients and the generator coefficients needed in (6) are specified by the recursions below, including all terms through homogeneous degree four. Thus (6) retains insertion, action, coordinate-density, and nonlinear-flow corrections. It is a formula for the coefficient, not an evaluated set of lattice Wick contractions or a bound uniform in a.

For comparison with the full Ward identity, define

\[
\mathcal D_{i,a}(g)=\mathbb E_{a,g}[V_a\mathcal O_{i,a,g}]
-\operatorname{Cov}_{a,g}
 (\mathcal O_{i,a,g},\mathcal J_{3,a,g}+\mathcal J_{6,a,g}).
\]

Its order-g^2 coefficient is \(\Gamma_{i,a}+\gamma^H_{i,a}\), with the plus sign and \(\gamma^H\) of L010. The Haar coordinate term M_2 in (6) is not that divergence insertion; retaining one does not replace the other.

No value is proved for a coefficient of \(\log(\sqrt\tau/a)\) in \(\Gamma_{i,a}\). In particular, the existence of such a logarithmic asymptotic, the absence of faster cutoff dependence, and a bounded remainder are not conclusions. There is no interacting reflected-error estimate against c_box/2.

## Proof

### 1. Exact quotient measure and its first correction

L003's rooted forest gauge is an exact reduction of gauge-invariant Haar integrals to product Haar on E'_a. It has a unique flat minimum, and S_2 is positive definite. Gauge covariance of V_a implies gauge invariance of V_a\mathcal S. The flow is equivariant by L010, so all functions in (1), and their products, are eligible for this reduction. Flow the full link configuration after starting on the slice; no claim is made that Wilson flow preserves forest gauge.

For t^c = i sigma^c/2 the eigenvalues of theta^c t^c are +/- i|theta|/2. The SU(2) exponential-coordinate Haar density, up to a constant, is

\[
j(\theta)=\left(\frac{\sin(|\theta|/2)}{|\theta|/2}\right)^2.
\tag{7}
\]

Indeed SU(2) is the unit three-sphere, parameterized by (cos(r/2), sin(r/2) theta/r). Its radial Haar volume is a constant times sin^2(r/2) dr dOmega, while Cartesian volume is r^2 dr dOmega; the ratio normalized to one at zero gives (7). Expanding sine and then the logarithm yields log j(gx_e) = -g^2|x_e|^2/12 + O(g^4|x_e|^4). The factor g raised to the dimension of the slice cancels in normalized expectations. Consequently the rescaled density relative to the Gaussian, before normalization, is

\[
\begin{split}
&\exp[-g S_3-g^2(S_4+M_2)+O_a(g^3)]\\
&\hspace{1cm}=1-gS_3+g^2\bigl(\tfrac12 S_3^2-S_4-M_2\bigr)+O_a(g^3).
\end{split}\tag{8}
\]

These Taylor assertions initially hold on fixed bounded coordinate sets. They are not cutoff-uniform estimates. The density is the exact reduced Haar density: no determinant for a second, nonlinear gauge choice is to be appended to it.

### 2. Laplace expansion and connected subtraction

Here the finite-dimensional Taylor expansion may be integrated to second order. To give the needed remainder justification, choose a sufficiently small fixed coordinate neighborhood of the unique minimum as in L003. Its action is bounded below by a mesh-dependent positive constant times |theta|^2, and the complement has action bounded below by a positive constant. Localize further to |x| <= g^(-epsilon), with a fixed sufficiently small epsilon > 0. Taylor remainders of the smooth action, densities, and numerators are bounded by a power of g times a polynomial in x; taking additional finite Taylor orders if necessary makes the remainders o(g^2) after division by the observable factors g^2. On this region the cubic and higher terms of the exponent are small relative to its quadratic lower bound. Taylor's formula for the exponential is then dominated by a fixed Gaussian times a polynomial.

In the rest of the local chart, the Gaussian lower bound gives a polynomial prefactor times exp(-c_a g^(-2epsilon)); outside the chart the original bound gives a polynomial prefactor times exp(-c'_a/g^2). Both are smaller than every required power of g. Thus one may integrate (8) and the observable expansions, normalize, and form the covariance through order g^2. Constants depend on a. This is an ordinary fixed-dimensional Laplace argument and does not justify passing to the mesh limit.

The expansions of the two uncentered observables are

\[
g^{-2}F_i(\exp(gx))=f_{i,0}+g f_{i,1}+g^2 f_{i,2}+O_a(g^3),
\quad
g^{-2}B(\exp(gx))=r_0+g r_1+g^2 r_2+O_a(g^3).
\tag{9}
\]

Centering the first observable in L010 changes no covariance. Expanding the normalized covariance with density (8) gives (6). One algebraic way to verify every connected subtraction is to take the coefficient of two source variables in the formal logarithm of the moment series for exp(source_1 F + source_2 B - gS_3 - g^2(S_4+M_2)); only finitely many polynomial moments are involved. The term with two copies of -gS_3 carries 1/2, and a single copy of -g^2(S_4+M_2) carries a minus sign. This produces exactly the last four terms of (6) in addition to the three observable terms. Formula (4) supplies a definition independent of convergence of the formal exponential.

Every order-g term has odd total polynomial degree: f_(i,1) and r_1 have degree three, S_3 has degree three, and the leading observables have degree two. The centered Gaussian is invariant under x -> -x, so these terms vanish. The leading covariance is the forest-slice quadratic Wilson covariance of L009. Only at this quadratic level does L003's linear quotient argument identify it with the Hodge-Gaussian curvature calculation. This gives (5) with its stated r^G.

### 3. Actual nonlinear flow and insertion Taylor coefficients

For explicit evaluation of (6), use logarithm coordinates on **all** variable links near identity, with fixed boundary links omitted. Let I insert the forest-slice vector x into this full space, setting forest entries to zero. Write the coordinate Wilson-flow vector field of L010 as

\[
Q(\theta)=Q_1\theta+Q_2(\theta)+Q_3(\theta)+O(|\theta|^4),
\tag{10}
\]

where Q_m is homogeneous of degree m. This is the coordinate vector field obtained by differentiating the exponential map; replacing it by the Lie-algebra left-frame coefficients at nonlinear orders is not valid. Smoothness of the exponential chart and L010's specified flow uniquely determine these derivatives. Its linear part is Q_1 = -a^(-2)D^*D, where D is unscaled edge-to-plaquette incidence. This is -d_a^*d_a in the cochain convention.

If theta_t(g)=g z_1(t)+g^2 z_2(t)+g^3 z_3(t)+O_a(g^4) starts at gIx, differentiation of the finite ODE and variation of constants give

\[
\begin{split}
z_1(t)&=e^{tQ_1}Ix,\\
z_2(t)&=\int_0^t e^{(t-s)Q_1}Q_2(z_1(s))\,ds,\\
z_3(t)&=\int_0^t e^{(t-s)Q_1}
 [D Q_2(z_1(s))z_2(s)+Q_3(z_1(s))]\,ds.
\end{split}\tag{11}
\]

Let j_(i,m) be the homogeneous degree-m polynomial of \(\mathfrak j_i\) in the full coordinates. Evaluating all z's at tau, ordinary polynomial composition gives

\[
\begin{split}
f_{i,0}&=j_{i,2}(z_1),\\
f_{i,1}&=D j_{i,2}(z_1)z_2+j_{i,3}(z_1),\\
f_{i,2}&=D j_{i,2}(z_1)z_3+j_{i,2}(z_2)
 +D j_{i,3}(z_1)z_2+j_{i,4}(z_1).
\end{split}\tag{12}
\]

In particular, flowing only the quadratic probe omits terms in both f_(i,1) and f_(i,2).

The corresponding residual coefficients are also determined without an interacting gauge-fixing ansatz. Let v_m be the homogeneous degree-m term of the full coordinate vector field V_a, and let s_m be the full-coordinate Taylor polynomial of \(\mathcal S\). V_a vanishes at identity. Apply the chain rule before restricting to the forest slice:

\[
\begin{split}
r_0&=(D s_2\,v_1-j_{3,2}-j_{6,2})\circ I,\\
r_1&=(D s_2\,v_2+D s_3\,v_1-j_{3,3}-j_{6,3})\circ I,\\
r_2&=(D s_2\,v_3+D s_3\,v_2+D s_4\,v_1-j_{3,4}-j_{6,4})\circ I.
\end{split}\tag{13}
\]

Here each derivative is evaluated at the argument of its accompanying vector polynomial. Equations (10)–(13), finite products of the specified link matrices, and Gaussian moments define a finite computation at every fixed mesh. They leave substantial contractions and their ultraviolet estimates to be performed.

### 4. Ward sign and limitation of external heat suppression

L007 gives E[V O] = Cov(O,V S_g - div_H V). Subtracting Cov(O,J_3+J_6) gives the exact identity

\[
\mathcal D_{i,a}(g)=\mathcal R_{i,a}(g)
 +\operatorname{Cov}_{a,g}(\mathcal O_{i,a,g},-\operatorname{div}_H V_a).
\tag{14}
\]

L010 evaluates the coefficient of the last term as \(\gamma^H_{i,a}\). It is added in the full Ward response and is absent from the requested remaining covariance. In contrast, M_2 is part of the measure used to compute that remaining covariance itself. These terms have different origins and different algebraic positions.

The tree proof in L009 bounds a trace with heat factors on two quadratic-mode indices. Formula (6) involves, for example, a connected four-cumulant with two cubic action vertices. Internal contractions of those vertices do not each carry a positive-tau heat factor. Similarly, the integrals in (11) extend to s=0; fixed final flow time does not give a uniform positive lower bound on every internal heat time. Therefore L008–L010's external heat-trace bounds, as stated, do not dominate the terms in (6). This identifies a missing estimate, not a divergence or an obstruction to a cancellation in their sum.

The source assessment supplies general bulk renormalization context, but no imported theorem here identifies the all-face boundary and actual insertion matching needed to bound (6). No value, including zero, is assigned to the requested logarithm. Finite matching and the reflected-error threshold c_box/2 remain uncontrolled.

The check `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check.py` compares the cumulant formula with independent normalized Gaussian moment-series arithmetic. A separate radial SU(2) case checks the Haar-density coefficient, a nonlinear flow contribution, and the Ward-divergence sign. These are algebraic checks of the expansion; they do not evaluate (6) for the four-dimensional box or establish a cutoff limit.

## Mathlib

Coverage of the full fixed-mesh specialization: **not checked**. Coverage of the supporting Laplace expansion, polynomial cumulants, SU(2) exponential volume, and smooth ODE differentiation: **not checked**. No Mathlib theorem is asserted to match the statement. The [prior literature assessment](../drafts/literature/2026-09-26-current-target.md) records the primary renormalization statements and direct links; they are supporting context, not premises that settle this covariance. This is a reproduction of finite-dimensional perturbation identities specialized to the existing definitions, with no claim of a result beyond the checked literature.
