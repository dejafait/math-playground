# L013 — Auxiliary-first relative-cochain covariance

## Hypotheses

Use L003's finite relative cubical complex in [-4,4]^4, with even N >= 2 and a = 8/N. For a single colour, let C^p be the real p-cochain space, with inner product a^4 times the cell sum. Components on cells contained in the geometric boundary vanish. Write

\[
D=d:C^0\longrightarrow C^1,\qquad
E=d:C^1\longrightarrow C^2,\qquad
\delta=D^*,\quad
L_0=D^*D,\quad L_1=E^*E+DD^*.
\tag{1}
\]

Thus C^0 consists of interior vertex values; C^1 retains normal links touching a boundary face and omits links contained in the boundary. Put m = dim C^0 = (N-1)^4 and n = dim C^1 = 4N(N-1)^3. L003 establishes ED = 0, ker E = im D, and positive definiteness of L_0 and L_1 for these spaces.

For each of the three SU(2) colours, take A in C^1, an independent real Fourier auxiliary variable b in C^0, and independent Grassmann variables c and bar c with coefficient space C^0. All integrations use orthonormal coordinates for the stated inner products. In point components, the orthonormal coordinates are a^2 times those components in every degree. Extend the inner products bilinearly to Grassmann coefficients.

Let

\[
d\gamma(b)=(2\pi)^{-m/2}e^{-\|b\|^2/2}\,db,
\qquad
\mathcal B[e^{-(\bar c,L_0c)}]=\det L_0.
\tag{2}
\]

Here \(\mathcal B\) is Berezin integration, with orientation fixed by \(\mathcal B[\prod_{j=1}^m(-\bar c_jc_j)]=1\). Expanding the exponential in its top Grassmann degree gives the determinant in (2).

For F a bounded measurable function or a polynomial of the three connection fields, define an **iterated** functional

\[
\begin{aligned}
\mathcal I(F)=\int_{(C^1)^3}\! &F(A^1,A^2,A^3)
\prod_{r=1}^3\left\{
e^{-\|EA^r\|^2/2}
\left[\int_{C^0}e^{i(b^r,\delta A^r)}d\gamma(b^r)\right]
\mathcal B_r[e^{-(\bar c^r,L_0c^r)}]
\right\}
\prod_{r=1}^3dA^r.
\end{aligned}
\tag{3}
\]

The b and Grassmann integrations are performed before the A integrations. Equation (3), rather than an interchange of a joint oscillatory integral, is the prescription. No strong normal derivative condition is imposed on A, and no auxiliary field equation is imposed on integration variables.

The Gaussian Fourier transform is a supporting known input: NIST DLMF, [equation 1.14.1](https://dlmf.nist.gov/1.14.E1) and the Gaussian row of [Table 1.14.1](https://dlmf.nist.gov/1.14.T1). The prior SPECIALIZE assessment in drafts/literature/2026-10-03-auxiliary-boundary-gaussian-matching.md approves exactly this finite-cochain applicability test. It does not import a continuum auxiliary measure or boundary Ward theorem.

## Conclusion

The prescription is well defined on the stated F, with finite positive normalization

\[
Z_{\rm aux}:=\mathcal I(1)
=\left[\det L_0\,(2\pi)^{n/2}(\det L_1)^{-1/2}\right]^3>0.
\tag{4}
\]

The normalized connection law \(\mathbb E_{\rm aux}F=\mathcal I(F)/Z_{\rm aux}\) is exactly the three independent Hodge Gaussians of L003. In particular, for arbitrary J^r in C^2,

\[
\mathbb E_{\rm aux}
\exp\left(i\sum_{r=1}^3(J^r,EA^r)\right)
=\exp\left[-\frac12\sum_{r=1}^3
(J^r,E L_1^{-1}E^*J^r)\right].
\tag{5}
\]

For curvature components at relative two-cells p,q, this gives the raw point covariance

\[
\mathbb E_{\rm aux}[(EA^r)_p(EA^s)_q]
=\delta_{rs}\,a^{-4}(E L_1^{-1}E^*)_{pq}.
\tag{6}
\]

Consequently, L003's centered curvature-square coefficient q_a(f), its separated mesh limit and its eventual lower bound c_box are unchanged by this prescription. This is a reproduction and regulator specialization of known Gaussian integration, not a result beyond the checked literature or a new reflected-error bound.

The underlying bosonic A,b integrand is not jointly absolutely integrable. No ordinary joint probability law, arbitrary integration order, smooth continuum b trace, boundary Ward identity or nonlinear measure replacement follows from (3).

## Proof

### Auxiliary integration and normalization

For fixed A, the b integral is absolutely convergent: its oscillatory factor has modulus one and d gamma is a probability measure. Apply the cited one-dimensional Gaussian Fourier identity in orthonormal coordinates, and take the finite product over m coordinates:

\[
\int_{C^0}e^{i(b,\delta A)}d\gamma(b)
=e^{-\|\delta A\|^2/2}.
\tag{7}
\]

This is an integral at fixed A, so no A,b interchange is used. The finite Berezin integral gives det L_0, independent of A. It is nonzero and positive because L_0 is positive definite by L003; there is no unremoved constant ghost mode on interior vertices with boundary values zero.

Insert (7) and (2) into (3). Since \(\|EA\|^2+\|\delta A\|^2=(A,L_1A)\), the resulting expression is

\[
\mathcal I(F)=(\det L_0)^3
\int_{(C^1)^3}F(A^1,A^2,A^3)
\exp\left[-\frac12\sum_{r=1}^3(A^r,L_1A^r)\right]
\prod_{r=1}^3dA^r.
\tag{8}
\]

Positive definiteness of L_1 gives Gaussian decay in every connection direction. Therefore (8) is absolutely convergent for bounded F and all polynomials, and its normalization is (4). The ghost determinant cancels in the normalized law. No mesh-dependent measure factors are suppressed: (4) uses orthonormal-coordinate Lebesgue measures, and the same convention is used in every inner integral.

### Curvature law and the boundary regulator

Equation (8) has exactly L003's quadratic action and exactly its integration space. Its independent colour Gaussians have covariance operator L_1^{-1}. Diagonalizing the positive real operator L_1 and applying the Gaussian Fourier identity to each connection mode gives (5), since \((J,EA)=(E^*J,A)\). Alternatively, its second derivatives at zero give the same covariance. This establishes equality of the entire centered Gaussian curvature law, including every mixed two-cell covariance.

To convert the operator covariance to point components, write \(\widehat A=a^2A\) in the cell basis. In these orthonormal coordinates the incidence matrices still have entries +/- 1/a, since the scale a^2 is the same in every degree. The covariance of \(E\widehat A\) is the matrix \(E L_1^{-1}E^*\); that of \(EA=a^{-2}E\widehat A\) is a^{-4} times this matrix. This proves (6) with the same kernel normalization as L003.

No boundary cells are added or removed in the integration. In particular, b, c and bar c have only interior vertex coordinates, while A keeps all relative one-cell coordinates, including the normal links touching a face. The adjoint delta in (7) is the finite relative incidence adjoint, not a divergence supplied with an extra face equation. Consequently, (8) is the same relative Hodge realization on the complete cubical complex, including face intersections. Its tangential sine and normal cosine modes and their operator interpretation are those already established in L003; no second proof of those modes is needed. A normal Neumann operator condition cannot be imposed as an additional strong constraint on the integration variables on the basis of (7).

L003 also identifies this Hodge curvature law with the quadratic Wilson gauge-quotient law. Thus the specified centered curvature-square insertion has exactly the same moments and reflected coefficient at each fixed mesh. Its separated mesh limit and c_box lower bound follow by that existing result. This conclusion is about the regulated Gaussian law, not about identifying nonlinear forest-gauge coordinate polynomials with (3).

### Why the order and later gaps remain essential

For one colour and F = 1, the modulus of the bosonic integrand before b integration is

\[
(2\pi)^{-m/2}
e^{-\|EA\|^2/2-\|b\|^2/2}.
\tag{9}
\]

The space im D has dimension m > 0, ED = 0, and A may be decomposed orthogonally into im D and its complement. The modulus is independent of the im D coordinate. Its integral over that coordinate is infinite, even after integrating b. Thus Fubini's theorem for absolute integrals is unavailable for the original joint expression. Equations (7)–(8) prove the well-defined iterated prescription; they do not repair the lack of absolute convergence of (9). The imaginary linear coupling is also not a positive joint density.

In particular, completing the square in b must not be interpreted as imposing b = i delta A pointwise, or as transferring b's absent boundary-vertex values into a smooth normal derivative constraint on A. This finite calculation avoids the strong-domain premise rejected in L012; that result is a contrast, not a mathematical input to the covariance equality.

This step establishes no BRST Ward identity for auxiliary or ghost insertions, no continuum trace theorem, and no interacting boundary subtraction. It supplies no bound on L011's one-loop physical-boundary remainder or on the difference of the matched interacting reflection form and the free coefficient. The required error <= c_box/2 on a specified coupling trajectory, finite matching, field construction, limiting reflection positivity, infrared control and finite positive mass remain missing.

An independent exact rational check on the even N=2 complex compares all 576 two-cell covariance entries with a forest-gauge calculation, retaining the a^-4 point normalization and all relative links before selecting the forest. The reproduction command is `PYTHONDONTWRITEBYTECODE=1 python3 scripts/auxiliary-cochains/check.py`. This finite check supports the applicability and normalization; the proof for all meshes is (7)–(8) using L003, not the calculation.

## Mathlib

Coverage of the full auxiliary-first cube covariance statement: **not checked**. Coverage of supporting Gaussian Fourier integration, finite Berezin determinants, positive finite-dimensional Gaussian covariance and relative Hodge decomposition: **not checked**. No Mathlib theorem name or direct library match is asserted. The direct NIST links above support the Gaussian transform, while L003 supplies the established cochain Gaussian and boundary realization. Neither is asserted to be a full source match for a continuum auxiliary formulation or physical-boundary Ward theorem.
