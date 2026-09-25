# L009 — A covariant link translation has vanishing flowed Gaussian Ward residual

## Hypotheses

Use the SU(2) Wilson action, relative cochains, inner products, and fixed box D = (-4,4)^4 of L003. Use exactly the compact displacement u, its central-difference version u_a, the strains, the two quadratic forms q_(3,a), q_(6,a), and the centered three-color insertions J_(i,a) and probes O_(i,a) of L008. In particular, the flow time is tau = 1/16, both the triplet and the transition-region shear are retained, and the triplet uses an average of plaquette squares. All meshes a = 8/N have even N and are sufficiently fine that every stencil with a nonzero displacement coefficient lies strictly inside the box.

For each vertex x in this interior and ordered plane rho nu, let Q_p^x be the holonomy around an incident elementary square, starting at x and oriented positively in the ordered plane. There are four such squares. Define an anti-Hermitian traceless clover matrix by

\[
\mathscr C_{\rho\nu,a}(x;U)
=\frac18\sum_{p\in\mathcal C_{\rho\nu}(x)}
\bigl(Q_p^x-(Q_p^x)^\dagger\bigr)_0,
\qquad \mathscr C_{\nu\rho,a}=-\mathscr C_{\rho\nu,a},
\qquad \mathscr C_{\nu\nu,a}=0. \tag{1}
\]

The subscript 0 subtracts half the trace times the identity; for SU(2) this subtraction is already zero. Reversing a plane reverses each loop. For a positive link e = (x,nu), put y = x + a e_nu and define

\[
X_{\nu,a}(x;U)=\frac1{2a}\sum_\rho
\left[u_{a,\rho}(x)\mathscr C_{\rho\nu,a}(x;U)
+u_{a,\rho}(y)U_\nu(x)\mathscr C_{\rho\nu,a}(y;U)U_\nu(x)^{-1}\right],
\]
\[
V_a[U_\nu(x)]=X_{\nu,a}(x;U)U_\nu(x). \tag{2}
\]

Terms with zero displacement coefficients are omitted. Set V_a to zero on the fixed boundary links. Compact support makes (2) well-defined without specifying clovers at the boundary.

Here is the corresponding real linear map on one-cochains, separately in each color. Write F = d_a A and let bar F be the four-plaquette vertex average of L008. At the link midpoint z = x + a e_nu/2 set

\[
(K_a A)_\nu(z)=\frac12\sum_\rho
\left[u_{a,\rho}(x)\overline F_{\rho\nu}(x)
+u_{a,\rho}(y)\overline F_{\rho\nu}(y)\right]. \tag{3}
\]

Let L_a = d_a^* d_a on one-cochains, let Delta_a be the positive relative one-form Hodge Laplacian, and take three independent Gaussian one-cochains with covariance Delta_a^(-1). Define

\[
q_{V,a}(A)=\langle d_a A,d_a K_a A\rangle_a,
\qquad
I^G_{V_a}=\sum_{c=1}^3 q_{V,a}(A^c)-3\operatorname{Tr}K_a,
\]
\[
R^G_a=I^G_{V_a}-J_{3,a}-J_{6,a},
\qquad r_{i,a}=\operatorname{Cov}_G(O_{i,a},R^G_a),
\]
\[
W^G_{i,a}=\mathbb E_G\left[D O_{i,a}(A)[(K_a A^c)_{c=1}^3]\right],
\qquad i\in\{3,6\}. \tag{4}
\]

These are finite-dimensional Gaussian quantities. I^G is identified below as the leading coefficient of the exact finite-link insertion V_a S - div_H V_a. No interacting definition or limit of the flowed probes is assumed.

## Conclusion

The vector field (2) is smooth and gauge covariant, preserves the fixed links, and has the continuum classical normalization delta_u A_nu = sum_rho u_rho F_rho nu. Its Gaussian linearization is exactly (3). The Gaussian insertion in (4) is invariant under the free gauge transformation A -> A + d_a phi, is centered, and obeys the exact identities

\[
W^G_{i,a}=\operatorname{Cov}_G(O_{i,a},I^G_{V_a}),
\qquad
W^G_a=C_a\binom11+r_a, \tag{5}
\]

where C_a is L008's response matrix in the order (3,6). For this particular clover stencil Tr K_a = 0. This assertion concerns the linearization, not the full nonlinear Haar divergence.

Both residual responses vanish with the ultraviolet cutoff at fixed box and flow time:

\[
\lim_{a\downarrow0}r_{3,a}=\lim_{a\downarrow0}r_{6,a}=0,
\qquad
W^G_a\longrightarrow C_\tau\binom11. \tag{6}
\]

Consequently the free coefficients determined by these two Ward equations satisfy, on sufficiently fine meshes,

\[
z^G_a:=C_a^{-1}W^G_a\longrightarrow\binom11,
\qquad
\left\|z^G_a-\binom11\right\|
\le\frac2{\eta_\tau}\|r_a\|,
\quad \eta_\tau=\lambda_{\min}(C_\tau)>0. \tag{7}
\]

This fixes the limiting tree-level joint normalization for a specified link variation. It is not an interacting generator-normalization theorem or a bound on the matched interacting reflection error, whose required threshold remains c_box/2. No uniformity as tau tends to zero or the box grows is claimed.

## Proof

### 1. Gauge covariance and the translation scale

A gauge transformation sends each based loop Q_p^x to G(x) Q_p^x G(x)^(-1). Thus the first clover in (2) transforms in the adjoint at x. Since U_nu(x) transforms to G(x) U_nu(x) G(y)^(-1), the transported second clover transforms in the same way. Hence X transforms in the adjoint at x and V_a U transforms as a tangent vector to the link. Products, inverses, and the anti-Hermitian projection are smooth on the finite product of groups. The coefficients vanish near the boundary, so this is a smooth vector field on precisely the variable links in L007's Haar identity.

To check the classical scale without presuming quantum regularity, sample any fixed smooth anti-Hermitian connection \(\mathcal A\) by its link holonomies. Taylor expansion of parallel transport around an elementary square gives

\[
Q_p^x=1+a^2\mathcal F_{\rho\nu}(x)+O(a^3),
\qquad
\mathscr C_{\rho\nu,a}(x)=a^2\mathcal F_{\rho\nu}(x)+O(a^3). \tag{8}
\]

The estimate is uniform on the fixed compact support. For example, the derivative terms in the product of four edge expansions give \(\partial_\rho\mathcal A_\nu-\partial_\nu\mathcal A_\rho\), and their quadratic products give the commutator; choosing another corner as base changes these terms only by O(a^3). The four-loop factor 1/8 compensates for the factor 2 in Q - Q^dagger. Also u_a converges uniformly to u, U = 1 + O(a), and y - x = a e_nu. Substitution into (2) gives

\[
\frac1a(V_a U_\nu(x))U_\nu(x)^{-1}
=\sum_\rho u_\rho(x)\mathcal F_{\rho\nu}(x)+O(a). \tag{9}
\]

This establishes the stated classical normalization. It is only a smooth-field consistency assertion at this point; the rough Gaussian limit needs the estimates below.

For the free linearization, use the fixed-mesh coordinates U_e = exp(i g a A_e^c T^c) of L003. The linear plaquette term is i g a^2 (d_a A)_p^c T^c. Thus

\[
\mathscr C_{\rho\nu,a}(x)
=i g a^2\overline F_{\rho\nu}^c(x)T^c+O(g^2).
\]

The transport in (2) changes this only at order g^2. Therefore X_nu = i g a (K_a A)_nu^c T^c + O(g^2), and the induced vector field in the A coordinates is K_a A + O(g), with the same assertion for its first derivatives on bounded sets at each fixed mesh. No g-uniform or mesh-uniform Taylor remainder is claimed.

### 2. Divergence and the gauge quotient

The Wilson action has leading term S_0 = sum_c ||d_a A^c||_a^2/2 by L003. The Haar density in exponential coordinates is smooth, positive, and constant to leading order under this rescaling. The coordinate formula for divergence therefore gives

\[
V_a S=\sum_c\langle d_a A^c,d_a K_a A^c\rangle_a+O(g),
\qquad
\operatorname{div}_H V_a=3\operatorname{Tr}K_a+O(g). \tag{10}
\]

Indeed the coordinate vector field is K_a A + O(g), its ordinary divergence is 3 Tr K_a + O(g), and differentiating the rescaled log Haar density supplies no constant term. This proves the claimed leading insertion. It does not discard the field-dependent nonlinear divergence.

For completeness, the trace in (10) vanishes for the chosen stencil. At a vertex x the part of bar F_(rho nu)(x) coming from A_nu, for rho != nu, is

\[
\frac1{4a}\sum_{\epsilon=\pm1}
\left[A_\nu(x+a e_\rho+\epsilon a e_\nu/2)
-A_\nu(x-a e_\rho+\epsilon a e_\nu/2)\right]. \tag{11}
\]

The terms without a rho displacement cancel between the two plaquettes on opposite sides of x. Applying (11) at both endpoints of a link shows that (K_a A)_nu at that link contains no copy of A_nu at the same link. Contributions from A_rho have a different component. Thus every diagonal matrix entry of K_a is zero. All nonzero coefficients have full interior stencils, so there is no boundary exception.

The following argument retains Tr K_a to verify the quotient identity independently of that cancellation. Write P_a for the orthogonal projection onto ker d_a^*, with d_a^* here from one-cochains to zero-cochains. L003 proves that the relative box has no harmonic one-cochains and that the Gaussian splits into independent transverse and gradient components. Consequently

\[
L_a\Delta_a^{-1}=\Delta_a^{-1}L_a=P_a.
\]

Since (3) depends only on d_a A, K_a annihilates gradients and K_a P_a = K_a. Finite-dimensional Gaussian integration and cyclicity of trace give, for one color,

\[
\mathbb E_G q_{V,a}(A)
=\operatorname{Tr}(L_a K_a\Delta_a^{-1})
=\operatorname{Tr}(P_a K_a)=\operatorname{Tr}K_a. \tag{12}
\]

Both q_(V,a) and I^G are unchanged by A -> A + d_a phi, because d_a A and K_a A are unchanged. Equation (12) proves their required centering.

There is a gauge-fixing term to check when using the full Hodge Gaussian for the Ward response. Its ordinary Gaussian integration-by-parts formula, summed over colors, is

\[
\mathbb E_G[D O(A)[K_a A]]
=\operatorname{Cov}_G\left(O,
\sum_c\langle A^c,\Delta_a K_a A^c\rangle_a
-3\operatorname{Tr}K_a\right). \tag{13}
\]

Here O can be either flowed probe, which depends only on the curvatures by L008. Decompose A = A_T + A_L into the independent transverse and gradient Gaussians. Since K_a A = K_a A_T, the difference between the quadratic form in (13) and q_(V,a) is

\[
\langle A_L,\Delta_a(1-P_a)K_a A_T\rangle_a
=\langle d_a^* A,d_a^* K_a A\rangle_a.
\]

Its conditional expectation given A_T is zero, and O is a function of A_T. Its mixed covariance with O is therefore exactly zero. This proves the first identity in (5). The second follows by adding and subtracting J_3 + J_6 in (4). Thus the full Hodge gauge-fixing term has been checked rather than identified with the physical insertion.

### 3. The limiting classical quadratic form

For a smooth real one-form A in the box let K A be the one-form with components sum_rho u_rho F_rho nu, F = dA. The compact support of u removes all boundary terms, even when A is a relative mode rather than a compactly supported form. Commuting partial derivatives in dF = 0 gives

\[
(dK A)_{\mu\nu}
=(\partial_\mu u_\rho)F_{\rho\nu}
-(\partial_\nu u_\rho)F_{\rho\mu}
+u_\rho\partial_\rho F_{\mu\nu}. \tag{14}
\]

Contract with F and sum over mu < nu. The transport term integrates to minus one half the integral of div u times sum_(mu<nu) F_mu nu^2, which is zero. The remaining terms give

\[
\langle dA,dK A\rangle
=\int_D\sum_{\mu,\rho,\alpha}
(\partial_\mu u_\rho)F_{\mu\alpha}F_{\rho\alpha}
=q_3(A)+q_6(A). \tag{15}
\]

For the last equality the diagonal terms yield (w_mu + w_nu) F_mu nu^2, and the two off-diagonal orders yield s_mu nu sum_alpha F_mu alpha F_nu alpha. This is precisely L007's compact classical translation calculation with L008's normalization. There is no singlet because div u = 0, but the shear has not been deleted. Polarization proves (15) for the associated symmetric bilinear forms as well.

### 4. A uniform polynomial mode bound

The clover and endpoint averages are bounded maps in the weighted cochain norms. More explicitly, set G_nu(x) = sum_rho u_a,rho(x) bar F_rho nu(x). Jensen's inequality for the two endpoint values and counting each vertex twice in each direction give

\[
\|K_a A\|_a^2\le a^4\sum_{x,\nu}|G_\nu(x)|^2
\le 2\|u_a\|_\infty^2\|d_a A\|_a^2. \tag{16}
\]

The final estimate uses the vector Euclidean norm for u_a, Cauchy–Schwarz in rho, and L008's four-plaquette averaging bound; each unordered curvature component occurs in two ordered pairs. The smooth fixed Psi gives a uniform bound on ||u_a||_infty. Thus a constant C_u independent of sufficiently fine a satisfies ||K_a A||_a <= C_u ||d_a A||_a.

Use the normalized relative modes f_(m,a) of L008, with positive eigenvalues lambda_(m,a). Labels include the one-form component. Define the symmetric, covariance-normalized action-variation matrix

\[
(B_{V,a})_{mn}
=\frac{\langle d_a f_{m,a},d_a K_a f_{n,a}\rangle_a
+\langle d_a f_{n,a},d_a K_a f_{m,a}\rangle_a}
{2\sqrt{\lambda_{m,a}\lambda_{n,a}}}. \tag{17}
\]

This is the matrix of q_(V,a)(Delta_a^(-1/2) xi). Move the first differential onto its adjoint. Since L_a = Delta_a P_a and P_a commutes with Delta_a, ||L_a f_(m,a)||_a <= lambda_(m,a), while ||d_a f_(n,a)||_a <= sqrt(lambda_(n,a)). Applying (16) proves

\[
|(B_{V,a})_{mn}|
\le\frac{C_u}{2}
\left(\sqrt{\lambda_{m,a}}+\sqrt{\lambda_{n,a}}\right). \tag{18}
\]

No uniform unsmoothed operator norm for B_(V,a) is needed. L008 supplies uniformly bounded B_(3,a) and B_(6,a), where q_(i,a)(Delta_a^(-1/2) xi) = xi^T B_(i,a) xi. Therefore B_(R,a) = B_(V,a) - B_(3,a) - B_(6,a) has an entry bound of the same form with an additional constant.

For each fixed pair of labels m,n,

\[
(B_{R,a})_{mn}\longrightarrow0. \tag{19}
\]

To verify this without differentiating a mesh error, write each term in the numerator of (17) as <L_a f_(m,a), K_a f_(n,a)>_a. The product sine/cosine formulas in L003 show that L_a f_(m,a) converges uniformly on the support to d^*d f_m: every incidence frequency 2 sin(k pi/(2N))/a tends to k pi/8, with unchanged component signs. For a fixed mode n, its clover values, endpoint averages, and smooth displacement coefficients in (3) converge uniformly to K f_n. The sum is a Riemann sum on the link midpoint grid, with compact interior support. The numerator therefore converges to the polarization of <dA,dK A>. The eigenvalue denominators have positive limits. Equation (15), together with the corresponding convergence of B_(3,a) and B_(6,a) proved in L008, gives (19).

### 5. Heat suppression controls the entire residual response

The same three-color Gaussian contraction used in L008 now gives the exact finite-mesh formula

\[
r_{i,a}=6\sum_{m,n}
e^{-\tau(\lambda_{m,a}+\lambda_{n,a})}
(B_{i,a})_{mn}(B_{R,a})_{mn}. \tag{20}
\]

The centering in (4) removes the disconnected Gaussian pairing; the remaining two pairings and three colors give the factor 6. The heat flow acts only on the probe, producing one factor on each of its mode indices.

Embed all finite label sets in the continuum label set as in L008, setting summands for missing labels to zero. Its uniform spectral inequalities are

\[
|k|^2/16\le\lambda_{k,a}\le\pi^2|k|^2/64.
\]

By (18) and the uniform B_i bounds, the absolute value of each summand of (20), including its factor 6, is at most

\[
C\bigl(1+|k_m|+|k_n|\bigr)
\exp\left[-\frac{\tau}{16}
\bigl(|k_m|^2+|k_n|^2\bigr)\right], \tag{21}
\]

with C independent of a,m,n. The sum of (21) over both four-dimensional integer labels and their four possible components is finite: shell counts grow polynomially and the exponential is Gaussian. Every fixed summand tends to zero by (19). Dominated convergence of this absolutely summable series proves (6), including contributions from arbitrarily high lattice modes. This is the additional step that smooth-field consistency alone would not provide.

Finally L008 gives C_a -> C_tau and ||C_a^(-1)|| <= 2/eta_tau eventually. Apply this to the exact equation (5) to obtain (7).

The proof never asserts existence of an unflowed continuum random variable I^G or J_i; only their mixed responses with the flowed probes have been taken to the limit. The free coefficient z^G tends to (1,1) for the specified generator. Nonlinear flowed-probe matching, renormalization of that generator, the field-dependent Haar divergence at positive coupling, interacting response stability, and the interacting residual remain unestimated. In particular (6) is not the bound on the reflected interacting observable required to be <= c_box/2. Heat flow still need not preserve the original positive-time reflection algebra. No continuum interacting field or finite positive physical mass has been obtained.

The exact rational-arithmetic check `PYTHONDONTWRITEBYTECODE=1 python3 scripts/link-translation/check.py` constructs the oriented loop words independently and checks K_a d_a = 0, the zero diagonal of K_a, and the endpoint-averaged u F scale on constant-curvature affine potentials. These are finite stencil checks; the full mode limit is proved in steps 4–5.

## Mathlib

Coverage of the full covariant-link construction and flowed Gaussian residual limit: **not checked**. Coverage of supporting compact-group divergence, finite-dimensional Gaussian integration by parts, Hodge decompositions, matrix traces, and dominated convergence for mode sums: **not checked**. No inspected Mathlib theorem name or direct library link is asserted. The gauge covariance, normalization factors, quotient correction, and uniform mode estimate are proved explicitly here. The [recorded translation-Ward source](../foundations/05-lattice-stress-tensor-matching.md#local-translation-identities) is supporting context, not a match for this fixed-boundary statement.
