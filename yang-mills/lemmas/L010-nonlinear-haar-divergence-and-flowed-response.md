# L010 — Exact nonlinear Haar divergence and its flowed two-probe coefficient

## Hypotheses

Use the finite SU(2) Wilson measure and relative cochains of L003 in D = (-4,4)^4, with a = 8/N and even N. Use the displacement u_a, central strains w_(a,mu), s_(a,mu nu), quadratic forms, Gaussian probes O_(i,a), and free response matrix C_a of L008, with i = 3,6 and tau = 1/16. Use exactly the clover matrices and endpoint-averaged link vector field V_a of L009. All supported stencils lie strictly inside D. Extend displacement coefficients by zero outside their compact support.

Write t^c = i sigma^c/2, with -2 Tr(t^c t^d) = delta_cd. The link derivative L_e^c acts along U_e -> exp(s t^c) U_e. Thus if V_a U_e = X_e U_e and X_e = sum_c v_e^c t^c, its product-Haar divergence is sum_(e,c) L_e^c v_e^c. Let

\[
P_p(U)=1-\tfrac12\operatorname{Tr}U_p,\qquad
\mathcal S(U)=4\sum_p P_p(U),\qquad S_g=\mathcal S/g^2.
\]

For a plaquette p in plane mu nu, mu < nu, with lower corner x, abbreviate x_mu = x + a e_mu, x_nu = x + a e_nu, and x_mu nu = x + a e_mu + a e_nu. Define its planar strain and vertex-averaged central strain by

\[
b_p=\frac{1}{2a}\bigl[
u_{a,\mu}(x_\mu)+u_{a,\mu}(x_{\mu\nu})
-u_{a,\mu}(x)-u_{a,\mu}(x_\nu)
+u_{a,\nu}(x_\nu)+u_{a,\nu}(x_{\mu\nu})
-u_{a,\nu}(x)-u_{a,\nu}(x_\mu)\bigr],
\]
\[
\widetilde b_p=\frac14\sum_{v\text{ vertex of }p}
(w_{a,\mu}+w_{a,\nu})(v). \tag{1}
\]

The nonlinear probe representatives are specified here, rather than inferred from their free coefficients. For g > 0 set

\[
\mathcal J_{3,a,g}(U)=\frac8{g^2}\sum_p\widetilde b_p P_p(U),
\qquad
\mathcal J_{b,a,g}(U)=\frac8{g^2}\sum_p b_p P_p(U),
\]
\[
\mathcal J_{6,a,g}(U)
=-\frac2{g^2}\sum_{x,\mu<\nu}s_{a,\mu\nu}(x)
\sum_\alpha\operatorname{Tr}
\bigl(\mathscr C_{\mu\alpha,a}(x;U)
\mathscr C_{\nu\alpha,a}(x;U)\bigr). \tag{2}
\]

These expressions are uncentered. Only their centered versions or covariances will be used. The triplet is an average of plaquette traces, while the shear uses products of clover matrices at the same vertex.

Define Wilson flow W_t(U) on the variable links by

\[
\frac{d}{dt}W_{t,e}
=-\frac1{a^2}\sum_c(L_e^c\mathcal S)(W_t)\,t^c W_{t,e},
\qquad W_0=U, \tag{3}
\]

with every fixed boundary link held fixed. The physical time normalization in (3) is part of this definition. Put

\[
\mathcal O_{i,a,g}(U)
=\mathcal J_{i,a,g}(W_\tau(U))
-\mathbb E_{a,g}\mathcal J_{i,a,g}(W_\tau(U)),\qquad i=3,6. \tag{4}
\]

For one real Gaussian color set q_(b,a)(A) = a^4 sum_p b_p (d_a A)_p^2, and let J_(b,a) be the sum of its three centered color copies. Define the isolated Haar contribution to the Ward response and its small-coupling coefficient by

\[
h_{i,a}(g)=\operatorname{Cov}_{a,g}
\bigl(\mathcal O_{i,a,g},-\operatorname{div}_H V_a\bigr),
\qquad
\gamma^H_{i,a}=\lim_{g\downarrow0}g^{-2}h_{i,a}(g). \tag{5}
\]

No full interacting Ward-residual expansion is assumed in these definitions.

## Conclusion

For every link configuration, the exact nonlinear identity is

\[
\operatorname{div}_H V_a
=\frac38\sum_p b_p\operatorname{Tr}U_p
=-\frac34\sum_p b_p P_p(U)
=-\frac{3g^2}{32}\mathcal J_{b,a,g}(U). \tag{6}
\]

The constant term vanishes by compact-support telescoping. The identity is not a nonlinear zero-divergence assertion. Its fixed-mesh expansion in U_e = exp(g a A_e^c t^c) starts with

\[
\operatorname{div}_H V_a
=-\frac{3g^2}{32}\sum_{c=1}^3q_{b,a}(A^c)+O_a(g^3), \tag{7}
\]

uniformly for A in a fixed bounded set. In particular there is no term of order g or order one.

The flow and probes in (3)–(4) are smooth and gauge covariant/invariant as appropriate at every fixed mesh. The limits in (5) exist and satisfy

\[
\gamma^H_{i,a}
=\frac3{32}\operatorname{Cov}_G(O_{i,a},J_{b,a}),
\qquad
\gamma^H_a=\frac3{32}C_a\binom10+O(a^2). \tag{8}
\]

The O(a^2) constant is independent of sufficiently fine meshes at this fixed box, displacement, and flow time. Consequently

\[
\gamma^H_a\longrightarrow\frac3{32}C_\tau\binom10\ne0,
\qquad
C_a^{-1}\gamma^H_a=\binom{3/32}{0}+O(a^2). \tag{9}
\]

Here C_tau is L008's positive definite matrix. Thus this isolated order-g^2 contribution has a finite nonzero limit and no ultraviolet logarithmic growth. Equation (9) expresses only that contribution in the free response basis. It does not compute the full order-g^2 correction to either Ward coefficient or the complete logarithmic residual. The small-coupling limit is taken first at each fixed mesh; no assertion about a joint limit g = g(a) is made. No matched interacting reflection-error estimate against c_box/2 is obtained.

## Proof

### 1. Differentiate the actual clover loops

The normalized Pauli matrices give

\[
\sum_c(t^c)^2=-\tfrac34 I,\qquad
v_e^c=-2\operatorname{Tr}(t^c X_e). \tag{10}
\]

Consider a based loop Q through its base link. If the link is traversed positively, its derivative is t^c Q or Q t^c, according to which end of the word contains the link. The derivative of Q dagger has the corresponding negative sign. Cyclicity of trace and (10) give the following contribution of (Q - Q dagger)/8 to the divergence of its Lie-algebra coefficients:

\[
-\frac14\sum_c\operatorname{Tr}
\bigl((t^c)^2(Q+Q^\dagger)\bigr)
=\frac3{16}\operatorname{Tr}(Q+Q^\dagger)
=\frac38\operatorname{Tr}Q. \tag{11}
\]

SU(2) traces are real. A negative traversal gives the negative of (11). A loop not containing the varied link contributes zero. The traceless projection in the clover introduces no additional term: contraction with t^c kills its scalar part, and for SU(2) Q - Q dagger is already traceless.

For the upper-endpoint term, put y = x + a e_nu and Y = U_e C(y) U_e^(-1). Differentiating the transport itself gives [t^c,Y]. Its contraction in the divergence is zero, since Tr(t^c[t^c,Y]) = 0 for each c. In the derivative of C(y), the Lie generator at y is U_e^(-1)t^c U_e. This rotated basis has the same quadratic Casimir (10). Therefore (11), with the same traversal sign, also applies to the transported clover. This accounts for all dependencies on the varied link; the transport has not been frozen when differentiating.

Fix a positive link e = (x,nu). In the clover for the ordered plane rho nu at either endpoint, exactly two incident squares contain e. The square on its negative-rho side traverses e positively; the square on its positive-rho side traverses e negatively. Let p_(rho nu)(z) denote the square with lower corner z in that plane. Including the generator's factor 1/(2a), its linkwise divergence is therefore

\[
\sum_cL_e^c v_e^c
=\frac{3}{16a}\sum_{\rho\ne\nu}
\bigl(u_{a,\rho}(x)+u_{a,\rho}(y)\bigr)
\left[\operatorname{Tr}U_{p_{\rho\nu}(x-ae_\rho)}
-\operatorname{Tr}U_{p_{\rho\nu}(x)}\right]. \tag{12}
\]

Reversing the ordered plane leaves its plaquette trace unchanged. Formula (12) applies to all ordered rho != nu. Its signs can equivalently be checked by the positively oriented word (+rho,+nu,-rho,-nu): the left nu-edge is negative and the right nu-edge is positive.

### 2. Assemble all edges of each plaquette

For p in plane mu nu, the two nu-edges in (12) contribute its forward difference of u_(a,mu), averaged over the two nu-endpoints. The two mu-edges contribute its forward difference of u_(a,nu), averaged over the two mu-endpoints. Their sum is exactly (3/8)b_p Tr U_p, with b_p as in (1). The support is away from the fixed boundary, so every edge with a nonzero coefficient is variable and no edge is missing. Summing (12) proves the first equality of (6).

For each plane separately, sum (1) over all lower corners using the zero extension. Every positive translate of a compactly supported displacement sum equals its untranslated sum. Hence

\[
\sum_{p\parallel\mu\nu}b_p=0. \tag{13}
\]

The same sum is obtained inside the box because all its nonzero terms are interior. Substitute Tr U_p = 2(1 - P_p) into the first equality of (6) and use (13). This gives its remaining equalities. This step needs compact support; it does not require a pointwise discrete divergence cancellation of b_p.

At fixed mesh the elementary plaquette expansion in L003 is

\[
P_p\bigl(\exp(g a A^c t^c)\bigr)
=\frac{g^2a^4}{8}\sum_c(d_a A^c)_p^2+O_a(g^3). \tag{14}
\]

It follows either by multiplying the four exponentials and taking their trace, or from the displayed quadratic trace calculation there. Analyticity of the finite products makes the remainder uniform on bounded coordinate sets. Applying (14) to (6) proves (7). There is no claim that this Taylor remainder is uniform as the mesh is refined.

### 3. The nonlinear probes have the required fixed-mesh Gaussian limit

The vector field in (3) is smooth on a finite product of compact groups, so its flow exists for all finite times and depends smoothly on its initial value. The product metric defined by -2 Tr is invariant under allowed gauge transformations, and the action is gauge invariant. Its gradient and flow are therefore equivariant. The plaquette traces and the same-vertex clover traces in (2) are gauge invariant, so (4) defines real smooth gauge-invariant observables for each g > 0. Reality of the clover product trace also follows from cyclicity and anti-Hermiticity.

To fix the linearization and time scale, temporarily use unscaled small link coordinates U_e = exp(theta_e^c t^c) and let D be the incidence matrix taking edge circulations around plaquettes. Formula (14) gives

\[
\mathcal S(\exp\theta)
=\tfrac12\sum_{p,c}(D\theta^c)_p^2+O(\|\theta\|^3).
\]

The group metric agrees with the Euclidean theta metric at the identity. Since d_a = D/a and the edge and plaquette inner products both have weight a^4, D*D = a^2 d_a* d_a. Thus (3) linearizes to

\[
\dot A=-L_a A,\qquad L_a=d_a^*d_a,\qquad
A(t)=e^{-tL_a}A. \tag{15}
\]

The relative Hodge decomposition in L003 has no harmonic one-forms. On its transverse space L_a = Delta_(1,a); on gradients L_a = 0. Therefore e^(-t L_a) A and H_(t,a) A differ by a gradient. Both q_(3,a) and q_(6,a) depend only on d_a A, so their values on these two evolved fields agree. No extra gauge-damping term is required for this assertion about the free curvatures.

Regrouping L008's vertex sums gives

\[
q_{3,a}(A)=a^4\sum_p\widetilde b_p(d_a A)_p^2. \tag{16}
\]

Also the clover expansion from L009 is C_(mu nu,a) = g a^2 t^c bar F_(mu nu)^c + O_a(g^2). Using -2 Tr(t^c t^d) = delta_cd in (2), its shear coefficient is precisely sum_c q_(6,a)(A^c). Combining (14)–(16) proves that the leading coefficients of the unflowed J_b and the flowed representatives J_i(W_tau) are respectively sum_c q_(b,a)(A^c) and sum_c q_(i,a)(H_(tau,a)A^c).

This coefficient calculation also yields convergence of the relevant expectations and products. L003's fixed-mesh gauge-quotient Laplace argument has a nondegenerate quadratic action at the unique flat minimum modulo gauge. The numerators of every representative in (2), including after the smooth flow, vanish to second order at that minimum. In a fixed local gauge chart they are bounded by C_a ||theta||^2; after theta = g a A, division by g^2 leaves polynomially bounded Gaussian integrands. Products are bounded by higher fixed polynomials. Outside that chart their numerators are bounded on the compact configuration space, and any powers of g^(-1) are dominated by the exponentially small action weight. These are the same local domination and exterior suppression used in L003; their constants may depend on a and tau. Hence the joint first and second moments converge to the stated Gaussian ones, and centering converges as well.

The exact equality -div_H V_a = (3g^2/32) J_(b,a,g) now gives

\[
g^{-2}h_{i,a}(g)
=\frac3{32}\operatorname{Cov}_{a,g}
\bigl(\mathcal O_{i,a,g},\mathcal J_{b,a,g}\bigr)
\longrightarrow\frac3{32}\operatorname{Cov}_G(O_{i,a},J_{b,a}). \tag{17}
\]

This proves the first part of (8) as an actual fixed-mesh small-coupling limit, not an interchange with the ultraviolet limit.

### 4. A uniform O(a^2) comparison controls every flowed mode

View u_a as a smooth function on R^4 by applying L008's central-difference formula to its fixed smooth compactly supported Psi before sampling. For every fixed derivative order its derivatives are uniformly bounded: each difference quotient is an average of a derivative of Psi over a segment. In particular there is a bound on its first three derivatives independent of small a.

Let z be the center of p. The mu part of b_p is the centered mu-difference with step a/2, divided by a, averaged at z +/- a e_nu/2. Taylor's formula with bounded third derivatives consequently gives

\[
b_p=\partial_\mu u_{a,\mu}(z)+\partial_\nu u_{a,\nu}(z)+O(a^2).
\]

The corresponding terms of tilde b_p average the central derivative with step a at the four vertices. The central derivative approximates the ordinary derivative with error O(a^2); averaging its derivative values about z cancels the first-order terms. The same uniform third-derivative bound gives

\[
\sup_p|b_p-\widetilde b_p|\le K_u a^2. \tag{18}
\]

All stencils in this argument use the smooth zero extension, so there is no boundary exception. This is a deterministic coefficient comparison, not a statement that interacting plaquette fields have uniform moments.

Use L008's R_a = d_a Delta_(1,a)^(-1/2), with ||R_a|| <= 1. Let B_(b,a) be the covariance-normalized matrix of q_(b,a), and B_(3,a), B_(i,a) those of L008. Equation (16) and the diagonal multiplication operators with entries b_p, tilde b_p imply

\[
\|B_{b,a}-B_{3,a}\|_{\mathrm{op}}\le K_u a^2. \tag{19}
\]

There are three independent colors and two connected Gaussian pairings. Consequently, with H_a = exp(-tau Delta_(1,a)),

\[
\operatorname{Cov}_G(O_{i,a},J_{b,a})-C_{i3,a}
=6\operatorname{Tr}
\bigl(H_a B_{i,a}H_a(B_{b,a}-B_{3,a})\bigr). \tag{20}
\]

L008 proves uniform bounds ||B_(i,a)|| <= M_i and a uniform heat trace Tr(H_a^2) <= T_tau < infinity. Explicitly its eigenvalue estimate lambda_(k,a) >= |k|^2/16 bounds that trace by the convergent sum over relative one-form labels of exp(-tau |k|^2/8). The trace-norm inequality

\[
\|H_a B_{i,a}H_a\|_1
\le\|B_{i,a}\|_{\mathrm{op}}\|H_a\|_{\mathrm{HS}}^2
\]

and (19) give the full, uniform bound

\[
\left|\operatorname{Cov}_G(O_{i,a},J_{b,a})-C_{i3,a}\right|
\le6M_iT_\tau K_u a^2. \tag{21}
\]

This controls all modes at once, including those at the cutoff. Combining (17) and (21) proves (8). L008 gives C_a -> C_tau and ||C_a^(-1)|| <= 2/eta_tau eventually. These imply (9). Its limiting vector is nonzero because (C_tau)_(33) > 0. In particular the exact nonlinear divergence cannot vanish identically for all configurations on all sufficiently fine meshes: otherwise (17) would be zero, contradicting (9).

### 5. Scope of the correction

L007's finite-link identity inserts VS - div_H V, which fixes the minus sign used in (5). The computation isolates that measure-divergence contribution. The action variation VS, the positive-coupling action and measure corrections, the nonlinear flowed probes, and the generator's quantum normalization still enter the rest of the Ward residual. They can cancel or alter the finite term (9) or produce logarithms in the full response. Neither their combined order-g^2 coefficient nor an ultraviolet-uniform interacting remainder is computed here.

The planar-strain representative J_b is not exactly the site-averaged triplet J_3 at finite mesh. Bound (21) concerns their leading Gaussian mixed responses only; it does not grant an O(a^2) interacting comparison. There is no claimed uniformity as tau goes to zero or the box grows. Wilson flow is nonlocal in Euclidean time, so these normalization probes are not assigned to the original positive-time reflection algebra. The matched reflected-error threshold remains c_box/2, with no new bound on that error. This is an interacting-insertion input, not a continuum field construction or mass-gap argument.

The rational quaternion check `PYTHONDONTWRITEBYTECODE=1 python3 scripts/haar-divergence/check.py` differentiates the based group words and endpoint transports directly. It checks (12) on 45 link rows at three rational mesh sizes, verifies both regroupings in (6), and exhibits a nonzero nonlinear divergence. It does not establish an interacting or a mesh limit; those limits and their order are justified above.

## Mathlib

Coverage of the full nonlinear-divergence identity, specified Wilson-flow probes, and iterated response limit: **not checked**. Coverage of supporting SU(2) matrix identities, smooth flows on compact manifolds, fixed-dimensional Laplace asymptotics, Gaussian quadratic covariances, and trace-norm estimates: **not checked**. No inspected Mathlib theorem name or direct library link is asserted. The specialized normalization, loop differentiation, time scale, and uniform response comparison are proved here. The [recorded flow-Ward source](../foundations/05-lattice-stress-tensor-matching.md#local-translation-identities) is supporting context, not a match for this fixed-boundary statement.
