# L008 — Flowed triplet and shear probes have a nonsingular Gaussian response

## Hypotheses

Use the three independent colors of the relative-boundary Gaussian one-cochain law in the fixed box D = (-4,4)^4 from L003, with even N and a = 8/N. The covariance on the one-cochain Hilbert space, whose inner product has weight a^4, is Delta_(1,a)^(-1). Write the exterior differential as d_a and use the positive Hodge Laplacian Delta_(1,a) = d_a* d_a + d_a d_a*. These are Gaussian statements, with no positive-coupling Wilson limit assumed.

Fix the following particular cutoff and the divergence-free displacement constructed in L007:

\[
b(t)=\begin{cases}e^{-1/t}&t>0,\\0&t\le0,\end{cases}
\qquad
\rho(x)=\frac{b(9-x^2)}{b(9-x^2)+b(x^2-25/4)},
\qquad \chi(x)=\prod_{\mu=1}^4\rho(x_\mu),
\]
\[
\Psi_{13}=\chi x_1x_3,\quad \Psi_{24}=\chi x_2x_4,
\quad \Psi_{31}=-\Psi_{13},\quad\Psi_{42}=-\Psi_{24},
\qquad u_\mu=\sum_\nu\partial_\nu\Psi_{\mu\nu},
\]

with every other entry of Psi zero. The denominator defining rho never vanishes. Thus chi is smooth, supported in [-3,3]^4, and equals one on [-5/2,5/2]^4. Define

\[
w_\mu=\partial_\mu u_\mu,\qquad
s_{\mu\nu}=\partial_\mu u_\nu+\partial_\nu u_\mu\quad(\mu<\nu).
\]

The sum of the w_mu is zero, so these w_mu are precisely the diagonal traceless strain coefficients in L007. On the open core (-5/2,5/2)^4 they equal (1,1,-1,-1), and every s_mu nu vanishes there.

For the discrete coefficients, extend Psi by zero and use central differences throughout:

\[
u_{a,\mu}=\sum_\nu\nabla^c_\nu\Psi_{\mu\nu},\qquad
w_{a,\mu}=\nabla^c_\mu u_{a,\mu},\qquad
s_{a,\mu\nu}=\nabla^c_\mu u_{a,\nu}+\nabla^c_\nu u_{a,\mu}.
\]

Then sum_mu w_(a,mu) = 0 exactly. Restrict to sufficiently fine meshes that the supported stencils and their incident plaquettes lie in the box interior. All vertex sums below are over that interior.

Here are the two specified one-color quadratic forms. For a smooth real one-form A, put F = dA and set

\[
q_3(A)=\int_D\sum_{\mu<\nu}(w_\mu+w_\nu)F_{\mu\nu}^2,
\qquad
q_6(A)=\int_D\sum_{\mu<\nu}s_{\mu\nu}
\sum_\alpha F_{\mu\alpha}F_{\nu\alpha}. \tag{1}
\]

For a lattice one-cochain A put F = d_a A. Let C_(mu nu)(x) be the four plaquettes of that plane through the vertex x, each expressed in the same positive plane orientation, and define

\[
\overline F_{\mu\nu}(x)=\frac14\sum_{p\in\mathcal C_{\mu\nu}(x)}F_p,
\qquad \overline F_{\nu\mu}=-\overline F_{\mu\nu},
\quad \overline F_{\mu\mu}=0,
\]
\[
q_{3,a}(A)=\frac{a^4}{4}\sum_{x,\mu<\nu}
(w_{a,\mu}+w_{a,\nu})(x)
\sum_{p\in\mathcal C_{\mu\nu}(x)}F_p^2,
\]
\[
q_{6,a}(A)=a^4\sum_{x,\mu<\nu}s_{a,\mu\nu}(x)
\sum_\alpha\overline F_{\mu\alpha}(x)\overline F_{\nu\alpha}(x). \tag{2}
\]

The triplet in (2) is the Gaussian coefficient of L006's site-centered average of plaquette traces, contracted as in L007. Its average of squares has not been replaced by the square of an average. Equation (2) also specifies the free shear representative used in this test.

Fix the physical flow time tau = 1/16, and let H_(tau,a) = exp(-tau Delta_(1,a)). For i = 3,6 define the centered unflowed insertions and the two flowed probes by

\[
J_{i,a}=\sum_{c=1}^3\left(q_{i,a}(A^c)-\mathbb E_G q_{i,a}(A^c)\right),
\qquad
O_{i,a}=\sum_{c=1}^3\left(q_{i,a}(H_{\tau,a}A^c)
-\mathbb E_Gq_{i,a}(H_{\tau,a}A^c)\right).
\]

Set C_(ij,a) = Cov_G(O_(i,a),J_(j,a)), with row and column order (3,6). These are curvature-quadratic probes at positive flow time; their weights can have either sign. Products in the shear probe can equivalently be written as signed squares using XY = ((X+Y)^2-(X-Y)^2)/4. The probes include the transition region; they are not assumed supported only where u is affine. Heat flow here is the linear Gaussian flow with relative boundary conditions. This does not assert an interacting flow construction or its Ward identity.

## Conclusion

There is a finite real symmetric positive definite matrix C_tau such that

\[
\lim_{a\downarrow0}C_a=C_\tau,\qquad
\lim_{a\downarrow0}\det C_a=\det C_\tau>0. \tag{3}
\]

An exact convergent expression for its entries is

\[
(C_\tau)_{ij}=6\operatorname{Tr}(H_\tau B_iH_\tau B_j)
=6\langle K_i,K_j\rangle_{\mathrm{HS}},
\quad
K_i=H_{\tau/2}B_iH_{\tau/2}, \tag{4}
\]

where the relative continuum operators B_i and H_tau are specified below. In particular, writing eta_tau = lambda_min(C_tau) > 0, all sufficiently fine meshes obey

\[
\lambda_{\min}(C_a)\ge\eta_\tau/2,
\qquad \|C_a^{-1}\|_{\mathrm{op}}\le2/\eta_\tau. \tag{5}
\]

This proves free algebraic identifiability for these two normalization probes. It proves no value of the Ward right-hand side, no normalization of a translation generator, no interacting matching coefficient, and no small lattice residual. No estimate uniform in flow time or box size is asserted. The required matched interacting reflection error <= c_box/2 remains unbounded.

## Proof

### 1. Bounded curvature forms with the required lattice normalization

On the six-component real two-form space use the norm squared sum_(mu<nu) F_(mu nu)^2. Equation (1) defines bounded self-adjoint multiplication operators M_3 and M_6 through q_i(A) = <dA,M_i dA>. For M_3 the diagonal entries are w_mu+w_nu. For M_6 its symmetric bilinear form is

\[
\langle F,M_6G\rangle
=\frac12\int_D\sum_{\mu<\nu,\alpha}s_{\mu\nu}
\left(F_{\mu\alpha}G_{\nu\alpha}
+G_{\mu\alpha}F_{\nu\alpha}\right). \tag{6}
\]

Smooth compact strains are bounded. There are finitely many components, and 2|XY| <= X^2+Y^2 bounds (6), proving the operator bounds.

For the lattice, (2) similarly defines self-adjoint M_(i,a) on relative two-cochains, including the adjacent-plaquette averaging in M_(6,a). Jensen's inequality gives

\[
a^4\sum_x|\overline F_{\mu\nu}(x)|^2
\le\frac{a^4}{4}\sum_x\sum_{p\in\mathcal C_{\mu\nu}(x)}|F_p|^2
\le a^4\sum_{p\parallel\mu\nu}|F_p|^2. \tag{7}
\]

The last inequality uses the four vertices of a plaquette. The same counting bounds the averaged squares in q_(3,a). Central differences of this fixed smooth Psi converge uniformly to the corresponding derivatives and have uniformly bounded coefficients. Thus sup_a ||M_(i,a)|| is finite. This argument concerns the free forms, not interacting field regularity.

To check the triplet normalization explicitly, in one color L006's Gaussian site insertion is hhat_(mu nu) = (1/8) sum_(p in C_(mu nu)(x)) :F_p^2:. In the contraction of that lemma's t_mu with w_(a,mu), the trace term drops out since sum w_(a,mu) = 0. The remaining coefficient of hhat_(mu nu) is 2(w_(a,mu)+w_(a,nu)). This gives exactly the first formula of (2), after centering and summing colors. The shear form has the normalization sum_alpha F_(mu alpha)F_(nu alpha) of L007's canonical free stress tensor. No factor 1/2 is inserted in this off-diagonal component; s_mu nu already pairs the two ordered strain entries.

### 2. Relative modes and the exact Gaussian response formula

Use the real Hilbert space of L^2 one-forms on D. An orthonormal component-mu basis is

\[
f_{\mu,k}(x)=\mathbf e_\mu e_{k_\mu}(x_\mu)
\prod_{\nu\ne\mu}v_{k_\nu}(x_\nu),
\quad k_\mu\ge0,\quad k_\nu\ge1\ (\nu\ne\mu),
\]
\[
e_0=8^{-1/2},\quad e_k(x)=\tfrac12\cos(k\pi(x+4)/8),
\quad v_k(x)=\tfrac12\sin(k\pi(x+4)/8)\quad(k\ge1).
\]

Define Delta_1 on this basis by lambda_k = (pi/8)^2 |k|^2. These are exactly the continuum limits of the relative modes derived in L003. Define the two-form modes with edge/cosine coordinates in their two component directions and vertex/sine coordinates in the other directions. Differentiation maps these modes by the incidence signs and frequencies pi k_mu/8. The identity Delta_1 = d* d + d d* follows by cancellation of mixed terms, as in the lattice tensor-product calculation. In particular,

\[
R=d\Delta_1^{-1/2},\quad \|R\|\le1,
\qquad B_i=R^*M_iR,\qquad H_\tau=e^{-\tau\Delta_1}. \tag{8}
\]

The strict positivity of Delta_1 follows from the three positive vertex indices in every one-form component. The B_i are bounded and self-adjoint. Also sum_(mu,k) exp(-tau lambda_k) is finite for every tau > 0, by the product of four convergent Gaussian series. Thus H_(tau/2) is Hilbert–Schmidt and K_i in (4) is Hilbert–Schmidt. The covariance Delta_1^(-1) is interpreted as a Gaussian generalized field, or equivalently by independent real standard normal coefficients in this basis, rather than as an L^2-valued random variable.

The flowed quadratic kernel H_tau B_i H_tau is trace class and Hilbert–Schmidt: its trace norm is at most ||B_i|| Tr(H_tau^2). Finite-mode centered quadratic sums consequently converge in L^2 by the Gaussian moment formula below, so the continuum flowed probes are well-defined. Gauge invariance here means invariance under the free transformation A -> A + d phi. The product-complex identity d H_tau = exp(-tau Delta_2) d shows that the flowed curvature remains unchanged under this transformation, just as on the lattice. No nonlinear gauge transformation or interacting observable limit is inferred.

At finite lattice spacing put R_a = d_a Delta_(1,a)^(-1/2) and B_(i,a) = R_a* M_(i,a) R_a. Again ||R_a|| <= 1 and the B_(i,a) have uniformly bounded norms. In orthonormal coordinates write A = Delta_(1,a)^(-1/2) xi, where xi has independent standard normal entries. Then

\[
q_{j,a}(A)=\xi^{\mathsf T}B_{j,a}\xi,
\qquad
q_{i,a}(H_{\tau,a}A)
=\xi^{\mathsf T}H_{\tau,a}B_{i,a}H_{\tau,a}\xi. \tag{9}
\]

Here heat flow and the covariance square root commute since both are functions of the same Laplacian. For symmetric finite matrices U,V, expanding the four Gaussian coordinates gives

\[
\operatorname{Cov}(\xi^{\mathsf T}U\xi,\xi^{\mathsf T}V\xi)
=2\operatorname{Tr}(UV).
\]

Indeed E[xi_r xi_s xi_t xi_v] is delta_rs delta_tv + delta_rt delta_sv + delta_rv delta_st; centering cancels the first pairing and symmetry makes the other two equal. Summing three independent colors therefore gives the *exact* finite-lattice identity

\[
C_{ij,a}=6\operatorname{Tr}(H_{\tau,a}B_{i,a}H_{\tau,a}B_{j,a})
=6\operatorname{Tr}(K_{i,a}K_{j,a}),
\quad K_{i,a}=H_{\tau/2,a}B_{i,a}H_{\tau/2,a}. \tag{10}
\]

The second equality follows by multiplying the K matrices and cycling the outer heat factors in the finite trace. It makes the response symmetric even though only the row probe in its original definition is flowed. The continuum expression (4) is well-defined by the same heat-sandwiched formula. In the displayed mode basis it is explicitly

\[
(C_\tau)_{ij}
=6\sum_{m,n}e^{-\tau(\lambda_m+\lambda_n)}
(B_i)_{mn}(B_j)_{mn},\qquad
(B_i)_{mn}=\frac{\langle df_m,M_i df_n\rangle}
{\sqrt{\lambda_m\lambda_n}}. \tag{11}
\]

The indices m,n include the one-form component as well as its four mode indices. Absolute convergence follows from the Hilbert–Schmidt Cauchy–Schwarz inequality, or the bounds below. Formulas (6), (8), and the fixed bump make every entry in (11) specified.

### 3. The triplet and shear forms are independent on exact curvatures

Suppose alpha B_3 + beta B_6 = 0. Every smooth compactly supported A lies in the domain of Delta_1^(1/2); this follows from its finite derivative L^2 norms and the sine/cosine expansion. Evaluating the operator equality on Delta_1^(1/2) A gives

\[
\alpha q_3(A)+\beta q_6(A)=0 \tag{12}
\]

for all such A. This tests exact curvatures dA, rather than arbitrary independent two-form values.

First choose A = phi dx_2 with real nonzero smooth phi supported in the open affine core and with partial_1 phi nonzero. There s is zero. The only possible curvatures are in planes 12, 23, 24, whose q_3 coefficients are respectively 2, 0, 0. Consequently

\[
q_6(A)=0,\qquad q_3(A)=2\int_D(\partial_1\phi)^2>0.
\]

Equation (12) forces alpha = 0.

L007 proves that a nonzero compactly supported displacement cannot have every off-diagonal strain zero. Our u is nonzero in the core, so some s_jk is nonzero. Choose a small open patch where that coefficient has fixed strict sign, and a nonzero real smooth phi compactly supported in the patch. Choose an index i distinct from j and k, and set

\[
A_n=\phi(x)\sin(nx_i)(dx_j+dx_k),\qquad n=1,2,\ldots.
\]

The leading curvatures are F_ij = F_ik = n phi cos(nx_i); every omitted term is bounded independently of n on a fixed compact support. Among off-diagonal stress components, only the jk component has a term of order n^2: it is F_ji F_ki = n^2 phi^2 cos^2(nx_i). All other contributions to q_6 are O(n) after integration. Hence

\[
\frac{q_6(A_n)}{n^2}
=\int_D s_{jk}\phi^2\cos^2(nx_i)+O(1/n)
\longrightarrow\frac12\int_D s_{jk}\phi^2\ne0. \tag{13}
\]

For the limit, use cos^2 t = (1+cos(2t))/2 and integrate the compactly supported smooth oscillatory coefficient once by parts in x_i. Thus q_6 is not zero on all compact one-forms, forcing beta = 0 in (12). The B_i are linearly independent.

Every heat eigenvalue is strictly positive, so H_(tau/2) has dense range: its range contains every finite linear combination of the mode basis. If alpha K_3 + beta K_6 = 0, the bounded bilinear form of alpha B_3 + beta B_6 vanishes on this dense range in both arguments. By continuity it vanishes everywhere, and the preceding independence forces alpha = beta = 0. The K_i are therefore independent in the real Hilbert space of self-adjoint Hilbert–Schmidt operators. Its Gram matrix (4) is strictly positive definite: for every nonzero real pair z,

\[
z^{\mathsf T}C_\tau z=6\|z_3K_3+z_6K_6\|_{\mathrm{HS}}^2>0. \tag{14}
\]

In particular both diagonal entries are positive and their Cauchy–Schwarz inequality is strict, proving det C_tau > 0. No numerical rank assumption enters this argument.

### 4. Heat bounds control the full mesh limit

Embed each finite one-cochain Hilbert space isometrically into the continuum one-form space by sending its normalized product modes to the identically labeled continuum modes. L003 proves their discrete normalization and differential formulas. The allowed indices satisfy the same lower constraints as above and are bounded by N-1. Extend lattice operators by zero on the omitted modes. For each retained label,

\[
\lambda_{k,a}=\sum_\mu\omega_{k_\mu,a}^2,
\quad \omega_{r,a}=\frac2a\sin\frac{r\pi}{2N},
\qquad
\frac{|k|^2}{16}\le\lambda_{k,a}\le\frac{\pi^2|k|^2}{64},
\quad \lambda_{k,a}\longrightarrow\lambda_k. \tag{15}
\]

The inequalities follow from 2x/pi <= sin x <= x for 0 <= x <= pi/2 and a = 8/N. Missing modes contribute zero to the heat operator. For every fixed pair of modes m,n,

\[
(B_{i,a})_{mn}\longrightarrow(B_i)_{mn}. \tag{16}
\]

To justify (16), apply d_a to their product mode formulas: the incidence signs are unchanged and every frequency omega_(r,a) tends to pi r/8. The strains converge uniformly to w and s. In q_(3,a) the four adjacent squared/bilinear mode values converge uniformly on the strain support to the same value at the vertex. In q_(6,a) each averaged curvature does so. Polarize these expressions for the pair of modes. Their weighted vertex sums converge by the Riemann-sum theorem to (1) and (6). Finally divide by sqrt(lambda_(m,a) lambda_(n,a)), whose limit is strictly positive. Compact support ensures that all these fixed stencils stay away from the boundary; the boundary mode functions themselves have not been replaced by different ones.

It remains to control all modes, not only each fixed pair. Let P_M project onto all one-form modes with |k| <= M, and write E_a = H_(tau/2,a), E = H_(tau/2). Equation (15) gives the uniform tail bound

\[
\|(1-P_M)E_a\|_{\mathrm{HS}}^2
\le\sum_{\substack{\mu,k\ \mathrm{allowed}\\|k|>M}}
e^{-\tau|k|^2/16}\longrightarrow0\quad(M\to\infty). \tag{17}
\]

The same bound holds for E. Convergence of the sum follows, for example, by grouping integer vectors in shells and bounding their number by 4(2r+3)^4, a polynomial dominated by the Gaussian decay. Also ||E_a||_op <= 1. For K_(i,a) = E_a B_(i,a) E_a, splitting off the two tails yields

\[
\|K_{i,a}-P_MK_{i,a}P_M\|_{\mathrm{HS}}
\le2\|B_{i,a}\|_{\mathrm{op}}\|(1-P_M)E_a\|_{\mathrm{HS}}. \tag{18}
\]

Indeed use (1-P_M)K_(i,a) + P_M K_(i,a)(1-P_M), commute P_M with E_a, and apply ||XYZ||_HS <= ||X||_HS ||Y||_op ||Z||_op, or its version with the Hilbert–Schmidt factor on the right. The B norms are uniformly bounded by step 1 and ||R_a|| <= 1. The identical estimate applies to K_i.

For a fixed M, (15)–(16) show that the finite matrices P_M K_(i,a) P_M converge entrywise, hence in Hilbert–Schmidt norm, to P_M K_i P_M. Choose M large in (17)–(18) and then a small for these finite matrices. This proves

\[
\|K_{i,a}-K_i\|_{\mathrm{HS}}\longrightarrow0.
\]

The Hilbert–Schmidt inner products in (10) therefore converge to (4), proving (3). Finite-dimensional matrix convergence also implies operator-norm convergence. For small enough a its error is at most eta_tau/2, and the Rayleigh quotient gives (5).

### 5. Interpretation and remaining threshold

The result concerns the coefficient matrix on the right of L007's proposed two-probe equation W = C z + r. It gives a bounded inverse for the free coefficient matrix at the specified fixed flow time. It does not compute W or r or establish that their interacting analogues converge. Nor does it show that the interacting response is close to the free one along a prescribed coupling trajectory. Those are substantive additional estimates, even though the free algebraic system now has full rank.

Positive flow time makes these mixed Gaussian contractions finite. A Wick-centered, unflowed curvature quadratic in four dimensions need not be an ordinary L^2 random variable. Only the flowed probes and the limiting mixed response (4) are used; no existence of an unflowed continuum J_i is inferred from (3). In particular the Gram positivity here is an ordinary Gaussian response calculation, not a reflection-norm lower bound. Heat flow is nonlocal in Euclidean time, so these normalization probes are not asserted to belong to the original positive-time local reflection algebra.

L006's original complementary-plane observable still requires the matched interacting reflected error <= c_box/2. This lemma supplies no numerical margin for that error and no bound on it. Nonlinear probe and generator matching, full field construction, reflection positivity of the limiting algebra, infrared control, other compact simple groups, and finite positive physical mass remain unresolved. The [recorded flow-Ward literature](../foundations/05-lattice-stress-tensor-matching.md#local-translation-identities) is supporting context; no interacting result from it is imported into this Gaussian proof.

## Mathlib

Coverage of the full flowed-response and relative-lattice convergence statement: **not checked**. Coverage of supporting Gaussian quadratic moments, Hilbert–Schmidt Gram matrices, heat operators, trigonometric mode expansions, compact-support oscillatory tests, and Riemann sums: **not checked**. No inspected Mathlib theorem name or direct library link is asserted. The proof gives the specialized normalization, independence, and uniform tail argument explicitly; the linked flow-Ward source is supporting literature, not a match for this full statement.
