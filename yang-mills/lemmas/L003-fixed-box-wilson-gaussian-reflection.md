# L003 — Fixed-box Wilson Gaussian reflection coefficient

## Hypotheses

Let N be even, a = 8/N, and let the cubical lattice fill D = [-4,4]^4, with time the fourth coordinate. Fix every link **contained in the geometric boundary** to the identity of SU(2); normal links touching the boundary remain variables. Use all elementary plaquettes, counted once with orientation mu < nu. Boundary plaquettes have identity holonomy and contribute zero. Gauge transformations equal the identity at boundary vertices. Reflection is theta(x,t) = (x,-t).

Use the ordinary two-dimensional trace and Hermitian generators T^c with Tr(T^c T^d) = delta_cd/2, for c,d = 1,2,3. Set

\[
P_p(U)=1-\tfrac12\operatorname{Tr}U_p,\qquad
d\mu_{a,g}=Z_{a,g}^{-1}
\exp\!\left[-\frac4{g^2}\sum_pP_p(U)\right]\prod_e dU_e ,
\quad g>0,
\]

where Haar measure runs over the variable links. This is the Wilson convention beta = 4/g^2. All expectations with subscript (a,g) use this finite probability measure.

Let f = f_* be the bump of L002. The mathematical properties imported from that lemma are

\[
f\in C_c^\infty(\mathbb R^4;\mathbb R),\quad
f\ge0,\quad \int f=1,\quad
\operatorname{supp}f\subset K=[-1/4,1/4]^3\times[1,2].
\]

Its infinite-volume covariance bound is not an input here. For a 12-plaquette, z_p is its center, with midpoint coordinates in directions 1 and 2 and vertex coordinates in directions 3 and 4. Define the centered gauge-invariant observable and its reflected correlation by

\[
F_{a,g}(f)=\frac4{g^2}\sum_{p\parallel12}
f(z_p)\bigl(P_p-\mathbb E_{a,g}P_p\bigr),\qquad
Q_{a,g}(f)=
\mathbb E_{a,g}\!\left[\overline{F_{a,g}(\theta f)}F_{a,g}(f)\right].
\]

The sum has no extra a^4: that factor appears in the quadratic expansion of P_p. This is a specified bare normalization; no interacting composite renormalization is assumed.

Relative p-cochains are real p-cell components that vanish on cells contained in the boundary. Give each degree the inner product a^4 times the sum of component products. The differential d is oriented incidence divided by a, and d* is its adjoint. For each color, let A be the centered Gaussian one-cochain with action

\[
\tfrac12\bigl(\|dA\|^2+\|d^*A\|^2\bigr).
\]

The proof shows this Gaussian is nondegenerate and that its curvature law is the gauge-quotient quadratic Wilson law. Colors are independent. Put B^c = (dA^c)_{12} and

\[
O_a(f)=\frac{a^4}{2}\sum_{p\parallel12}f(z_p)
\sum_{c=1}^3\left((B_p^c)^2-\mathbb E_G(B_p^c)^2\right),
\qquad
q_a(f)=\mathbb E_G[\overline{O_a(\theta f)}O_a(f)].
\]

## Conclusion

At each fixed mesh,

\[
\lim_{g\downarrow0}Q_{a,g}(f)=q_a(f).
\]

Moreover, the Gaussian coefficients have a finite positive limit:

\[
q_{\rm box}(f):=\lim_{\substack{N\to\infty\\N\ {\rm even}}}q_{8/N}(f)
\quad\hbox{exists},\qquad
q_{\rm box}(f)\ge\tfrac32 d_{\rm box}^2>0,
\]

where the following constants are independent of the mesh:

\[
\Omega=\frac{\pi\sqrt5}{8},\quad
\alpha=\frac{\pi^2}{16},\quad
m_\phi=\frac{\cos^2(\pi/16)\cos^2(\pi/32)}{128},
\quad
d_{\rm box}=
\frac{m_\phi\alpha\,\sinh^2(2\Omega)}
{\Omega\sinh(8\Omega)}.
\]

Consequently, for all sufficiently fine even meshes,

\[
q_a(f)\ge c_{\rm box}:=\tfrac34d_{\rm box}^2>0.
\]

The finite-mesh small-coupling limit and the mesh limit are **iterated limits**. No estimate uniform in a is asserted for Q_(a,g) - q_a, and no prescribed running coupling, positive renormalized coupling, interacting continuum field, or physical mass is constructed.

## Proof

### 1. Wilson normalization and the fixed-mesh Gaussian limit

Near the identity, write U_e = exp(i g a A_e^c T^c), with the sign reversed on reversed links. For the four signed edge matrices X_j = +/- a A_e^c T^c in a plaquette, expansion to second order and cyclicity of trace give

\[
\operatorname{Tr}\prod_{j=1}^4e^{igX_j}
=2-\frac{g^2}{2}\operatorname{Tr}\Big(\sum_jX_j\Big)^2+O(g^3).
\]

The linear term vanishes because the generators are traceless. Indeed the quadratic trace terms are -sum_j Tr(X_j^2)/2 - sum_(i<j) Tr(X_i X_j), which equal the displayed square. Since sum_j X_j = a^2 (dA)_p^c T^c,

\[
P_p=\frac{g^2a^4}{8}\sum_c(dA)_p,c^2+O(g^3).
\]

At fixed mesh these Taylor statements hold uniformly for A in each bounded set. Thus the action has quadratic part (a^4/2) sum_(p,c) (dA)_p,c^2, and (4/g^2) sum_p f(z_p)P_p has quadratic part (a^4/2) sum_(p,c) f(z_p)(dA)_p,c^2.

Here is why the corresponding fixed-mesh limit of expectations is valid despite gauge zero modes. Choose a forest connecting every interior vertex to a boundary vertex, with one boundary root per component. For example, at fixed interior coordinates 2,3,4, take the edges in direction 1 from the lower face up to the last interior vertex. There is one forest edge per interior vertex. Recursively gauging each forest link to the identity determines a unique gauge transformation equal to identity on the boundary. Left and right Haar invariance, integrated successively along the forest, identifies integrals of gauge-invariant functions with integrals against product Haar measure on the remaining links with forest links set to identity. The integrated gauge volume is one.

On this reduced compact product of groups, the action has a unique absolute minimum, at the identity configuration. Each P_p is nonnegative and vanishes exactly when U_p is identity. If all plaquette holonomies are identity, products along paths depend only on their endpoints: elementary plaquette moves and cancellation of an edge with its reverse relate paths in a cubical box. A potential obtained by parallel transport from a boundary vertex is identity at all boundary vertices, since the boundary graph is connected and its links are identity. Thus the flat configuration is a gauge transform of identity by an allowed transformation. Identity forest links force that transformation to be identity at every interior vertex as well.

The same path argument for real cochains says that dA = 0 implies A = d phi with phi zero on the boundary. With A zero on forest edges, phi is constant along each forest component and hence zero. Therefore the quadratic form ||dA||^2 is positive definite on the forest slice.

For completeness, ordinary finite-dimensional Laplace scaling now applies with moment control. In exponential coordinates theta_e near the unique minimum, the reduced Haar density is smooth and strictly positive, and 4 sum_p P_p has positive Hessian. In a fixed sufficiently small coordinate neighborhood it is bounded below by c_a |theta|^2. Outside that neighborhood, compactness and uniqueness of the minimum give a strictly positive lower bound. Substitute theta_e = g a A_e. The common Jacobian power of g cancels in normalized expectations. On the rescaled neighborhood, the integrands converge to those of the nondegenerate Gaussian quadratic action and are dominated by a Gaussian with a mesh-dependent positive constant. The observable P_p/g^2 is bounded there by a mesh-dependent constant times |A|^2, so its first and second products are covered by polynomial times Gaussian domination. Outside the neighborhood, any powers of g^-1 in these moments are dominated by exp(-c'_a/g^2), even after dividing by the normalization, which is asymptotic to a positive constant times the appropriate power of g. This proves joint first and second moment convergence of the rescaled plaquette sums, including the reflected sum. Centering therefore converges as well. The constants in this paragraph need not be uniform as the number of links grows.

To identify the limiting curvature law, decompose the space of relative one-cochains orthogonally as im(d on zero-cochains) plus ker(d*). The zero-cochain Laplacian is positive, since a function vanishing on the boundary with zero differential is zero. Thus every gauge class has a unique representative in ker(d*). The forest slice maps linearly and bijectively onto this orthogonal slice; the Jacobian is constant and curvature is unchanged. On the orthogonal slice ||dA||^2 is positive definite by the closed-cochain argument just given.

In the Gaussian with action (||dA||^2 + ||d* A||^2)/2, the orthogonal and gradient components decouple. The first term depends only on the orthogonal component, the second only on the gradient component, and the latter has a nondegenerate Gaussian integral. Integrating it out leaves precisely the normalized curvature law on the orthogonal slice, hence on the forest slice. This proves the first limit in the conclusion and justifies using the Hodge gauge-fixed Gaussian for the coefficient. It does not gauge-fix the interacting measure by a formal insertion.

### 2. Relative boundary modes

The one-dimensional interval has vertices x_j = -4 + ja for j = 0,...,N and edge midpoints x_(j+1/2). Zero-cochains vanish at endpoints and use the interior vertices; one-cochains use all N edges. Both inner products use weight a. Write Dv_j = (v_(j+1)-v_j)/a.

An orthonormal basis of vertex modes and edge modes is

\[
v_k(x)=\sqrt{\frac28}\sin\frac{k\pi(x+4)}8
\quad(1\le k\le N-1),
\]
\[
e_0(x)=8^{-1/2},\qquad
e_k(x)=\sqrt{\frac28}\cos\frac{k\pi(x+4)}8
\quad(1\le k\le N-1),
\qquad
\omega_{k,a}=\frac2a\sin\frac{k\pi}{2N},\quad\omega_{0,a}=0.
\]

The modes are evaluated on their respective vertex or midpoint grids. Their orthogonality and norms follow by expanding sine and cosine products into sums of exponentials and summing finite geometric series; each nonconstant squared norm before multiplication by a is N/2. Direct subtraction gives Dv_k = omega_(k,a) e_k, D*e_k = omega_(k,a) v_k, and D*e_0 = 0.

The relative cubical complex is the tensor product of these interval complexes. A component in directions I uses edge spaces in I and interior vertex spaces in the other directions. This is exactly the convention of vanishing on boundary cells. The differential is the sum of the one-dimensional D operators with the usual alternating orientation signs. Operators in distinct coordinates commute before those signs; in dd* + d*d the mixed terms cancel. The Hodge Laplacian on each component is therefore the sum of DD* in its edge coordinates and D*D in its vertex coordinates. There is no mixing of components. For one-cochains, three vertex coordinates give strict positivity. This proves the Gaussian nondegeneracy and the stated sine/cosine boundary conditions without imposing a different scalar Dirichlet condition on all components.

For the 12-curvature, define spatial indices

\[
\mathcal K_N=
\{(k_1,k_2,k_3):0\le k_1,k_2\le N-1,\quad
1\le k_3\le N-1,\ (k_1,k_2)\ne(0,0)\},
\]
\[
\phi_k(x)=e_{k_1}(x_1)e_{k_2}(x_2)v_{k_3}(x_3),\quad
\alpha_{k,a}=\omega_{k_1,a}^2+\omega_{k_2,a}^2,\quad
\Omega_{k,a}^2=\alpha_{k,a}+\omega_{k_3,a}^2.
\]

The component A_2 contributes omega_(k_1,a)^2 to the curvature covariance and A_1 contributes omega_(k_2,a)^2. Their cross covariance is zero. Their mode denominators are identical, and the time coordinate is a vertex coordinate for both. Consequently the one-color point covariance is

\[
C_a((x,t),(y,s))
=\sum_{k\in\mathcal K_N}
\alpha_{k,a}\phi_k(x)\phi_k(y)G_{a,\Omega_{k,a}}(t,s),
\]

where G_(a,Omega) is the kernel of (D*D + Omega^2)^-1 relative to the measure a sum over interior time vertices. In particular,

\[
G_{a,\Omega}(t,s)=
\sum_{j=1}^{N-1}\frac{v_j(t)v_j(s)}{\omega_{j,a}^2+\Omega^2}.
\]

The factors of a in this kernel agree with the original a^4 cochain inner product.

### 3. The reflected time Green function and positive mode contributions

Put gamma = (2/a) asinh(a Omega/2). For t <= s in (-4,4), the discrete Dirichlet Green function is

\[
G_{a,\Omega}(t,s)=
\frac{a\,\sinh(\gamma(t+4))\sinh(\gamma(4-s))}
{\sinh(a\gamma)\sinh(8\gamma)}.
\]

One can verify the normalization directly. In integer coordinates its expression is a sinh(i eta) sinh((N-j)eta) / [sinh eta sinh(N eta)] for i <= j, with eta = a gamma and 2 cosh eta = 2 + a^2 Omega^2. It solves the homogeneous three-term recurrence off i = j, vanishes at the endpoints, and applying D*D + Omega^2 at i = j gives 1/a. Thus it is the kernel for measure a sum, rather than the unweighted inverse matrix. Uniqueness follows from positivity of the operator.

For positive t,s the reflected kernel consequently factors:

\[
G_{a,\Omega}(-t,s)=r_{a,\Omega}h_{a,\Omega}(t)h_{a,\Omega}(s),
\quad
r_{a,\Omega}=\frac a{\sinh(a\gamma)\sinh(8\gamma)}>0,\quad
h_{a,\Omega}(t)=\sinh(\gamma(4-t)).
\]

The spatial magnetic component is even under time reflection. Set

\[
b_{k,a}=\alpha_{k,a}r_{a,\Omega_{k,a}}>0,\qquad
\psi_{k,a}(x,t)=\phi_k(x)h_{a,\Omega_{k,a}}(t).
\]

Then C_a(theta z,w) = sum_k b_(k,a) psi_(k,a)(z) psi_(k,a)(w).

For centered real Gaussian X,Y, differentiating their moment generating function gives E[(X^2 - E X^2)(Y^2 - E Y^2)] = 2(E XY)^2. Applying this identity to three independent colors and including the factor 1/2 from each insertion yields

\[
q_a(f)=\frac32a^8\sum_{z,w}f(z)f(w)C_a(\theta z,w)^2
=\frac32\sum_{k,l\in\mathcal K_N}b_{k,a}b_{l,a}
\left(a^4\sum_z f(z)\psi_{k,a}(z)\psi_{l,a}(z)\right)^2.
\]

Here z,w run over centers of the retained 12-plaquettes. All sums are finite. Every ordered pair of modes contributes a nonnegative term, although an individual spatial mode changes sign. In particular, retaining any single diagonal term k = l is a valid lower bound. The centering removes the within-insertion contractions; it is not replaced by an assertion about ordinary variance.

### 4. A finite separated continuum limit in this box

For a fixed index k, as a tends to zero,

\[
\omega_{k_j,a}\longrightarrow\pi k_j/8,\qquad
\Omega_{k,a}\longrightarrow\Omega_k=\pi|k|/8,\qquad
\gamma_{k,a}\longrightarrow\Omega_k,\qquad
\frac a{\sinh(a\gamma_{k,a})}\longrightarrow\Omega_k^{-1}.
\]

The spatial sine and cosine formulas are already the restrictions of mesh-independent functions. We justify convergence of the full covariance, including its growing set of indices.

For indices in K_N, elementary sine bounds give

\[
\frac{|k|}{4}\le\Omega_{k,a}\le\frac{\pi|k|}{8}.
\]

Also u = a Omega_(k,a)/2 lies in (0,sqrt(3)], and asinh u >= u/sqrt(1+u^2) >= u/2. Hence gamma_(k,a) >= Omega_(k,a)/2 >= |k|/8. Since |k| >= 1, for t,s in [1,2] the factored Green function obeys

\[
0<G_{a,\Omega_{k,a}}(-t,s)
\le
\frac{\exp[-\Omega_{k,a}(t+s)/2]}
{\Omega_{k,a}(1-e^{-2})}.
\]

Indeed a/sinh(a gamma) <= 1/gamma, each numerator sinh is at most half its positive exponential, and sinh(8 gamma) = e^(8 gamma)(1-e^(-16 gamma))/2 with 1-e^(-16 gamma) >= 1-e^-2. All spatial products satisfy |phi_k(x)phi_k(y)| <= (2/8)^3, and alpha_(k,a) <= Omega_(k,a)^2. Thus the absolute value of each term of C_a(theta z,w), uniformly on K times K, is bounded by

\[
\frac{1}{64(1-e^{-2})}\frac{\pi|k|}{8}
\exp(-|k|/4).
\]

This is summable over nonnegative k_1,k_2 and positive k_3: the number of lattice points in a shell of radius n grows at most polynomially, whereas the exponential decays. Extend the finite sums by zero for missing indices. The summable bound and convergence of every fixed mode give uniform convergence on K times K to the series

\[
C_{\rm box}^{\theta}(z,w)=
\sum_{\substack{k_1,k_2\ge0,\ k_3\ge1\\(k_1,k_2)\ne(0,0)}}
\frac{\alpha_k}{\Omega_k\sinh(8\Omega_k)}
\phi_k(x)\phi_k(y)
\sinh(\Omega_k(4-t))\sinh(\Omega_k(4-s)),
\quad
\alpha_k=(\pi/8)^2(k_1^2+k_2^2).
\]

For this uniform-convergence argument the finite expressions may be evaluated by their trigonometric formulas at all points of K; on the grid they are the covariance already derived. The limit is continuous and bounded there.

The staggered plaquette-center grids are product Riemann grids, and a^4 sum_z f(z) tends to integral f = 1. Uniform convergence and boundedness of the reflected kernel, followed by the ordinary Riemann-sum theorem applied to its continuous limit, now give

\[
q_a(f)\longrightarrow
\frac32\int_K\!\int_K f(z)f(w)
\bigl(C_{\rm box}^{\theta}(z,w)\bigr)^2\,dz\,dw
<\infty.
\]

This is a separated limit. The argument never takes the covariance through coincident insertions and proves no ordinary all-moment limit for the composites.

### 5. An explicit surviving mode

Take k_* = (0,2,1), available for N >= 4. On the spatial support of f its squared spatial wave is

\[
\phi_{k_*}(x)^2
=\frac1{128}\cos^2(\pi x_2/4)\cos^2(\pi x_3/8)
\ge m_\phi>0.
\]

Its limiting alpha and Omega are exactly the constants in the conclusion. The limiting time factor obeys sinh^2(Omega(4-t)) >= sinh^2(2 Omega) for 1 <= t <= 2.

Keep the diagonal (k_*,k_*) term in the finite sum for q_a and take the limit, using the already proved convergence of q_a and ordinary Riemann sums for this fixed mode. Nonnegativity of f and its integral one imply

\[
\begin{aligned}
q_{\rm box}(f)
&\ge \frac32
\left[
\frac{\alpha}{\Omega\sinh(8\Omega)}
\int_K f(x,t)\phi_{k_*}(x)^2
\sinh^2(\Omega(4-t))\,dx\,dt
\right]^2\\
&\ge \frac32 d_{\rm box}^2>0.
\end{aligned}
\]

The finite convergence of q_a to this positive number gives q_a >= q_box/2 >= 3 d_box^2/4 for all sufficiently fine even meshes. This completes the claimed Gaussian bound and its regulator matching.

### 6. Comparison with the bound still required

For a proposed interacting continuum trajectory g(a), write the exact difference R_a = Q_(a,g(a))(f) - q_a(f). The proved lower bound would give Q_(a,g(a))(f) >= c_box/2 if one also established |R_a| <= c_box/2 uniformly at sufficiently small a. That estimate is not supplied by the fixed-mesh Laplace limit. Its smallness thresholds can depend on a; no rate or relation to a coupling at a fixed physical scale has been proved.

One can choose a successively smaller bare coupling separately at each mesh to make the finite-mesh difference small. Such a diagonal choice is not control of a prescribed Yang–Mills renormalization trajectory or proof of nonzero renormalized interaction. Composite normalization may itself require further renormalization. Convergence of the needed interacting observables, positivity on the entire limiting algebra, all remaining field axioms and gauge groups, removal of the box, and a finite positive physical mass remain open.

The boundary mode energies are regulator scales. A positive coefficient in this finite box, or the positive spatial frequencies used to bound it, is not a physical Yang–Mills mass gap.

## Mathlib

Coverage of the full statement: **not checked**. Coverage of supporting finite-dimensional Gaussian, Haar integration, orthogonal-decomposition, trigonometric, Laplace-asymptotic, dominated-convergence, and Riemann-sum results: **not checked**. No inspected Mathlib theorem or direct library link is asserted. The specific gauge reduction, Hessian matching, mode expansion, Green-function normalization, domination, and lower bound are proved above; no continuum Yang–Mills existence theorem is used as an input.
