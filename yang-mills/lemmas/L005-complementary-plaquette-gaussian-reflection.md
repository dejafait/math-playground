# L005 — Complementary plaquettes retain a positive Gaussian reflection norm

## Hypotheses

Use the SU(2) Wilson measure, the box [-4,4]^4, even N, mesh a = 8/N, relative cochain boundary conditions, three-color Gaussian curvature law, reflection theta, and nonnegative test f = f_* of L003. In particular, f has integral one and support in

\[
K=[-1/4,1/4]^3\times[1,2].
\]

For mu nu = 12 or 34 let Z_(mu nu,a) be the centers of the plaquettes in that plane. A 34 center has vertex coordinates in directions 1,2 and midpoint coordinates in directions 3,4. Define

\[
F_{\mu\nu,a,g}(f)=\frac4{g^2}
\sum_{p\parallel\mu\nu}f(z_p)
\bigl(P_p-\mathbb E_{a,g}P_p\bigr),
\qquad P_p=1-\tfrac12\operatorname{Tr}U_p,
\]
\[
F^D_{a,g}(f)=F_{12,a,g}(f)-F_{34,a,g}(f),
\qquad
Q^D_{a,g}(f)=\mathbb E_{a,g}
\bigl[F^D_{a,g}(\theta f)F^D_{a,g}(f)\bigr].
\]

Here theta f = f composed with theta. Both plaquette traces are reflection-even: reflection may reverse their oriented holonomy, but the SU(2) trace of the inverse is the same trace. The linear 34 curvature itself is reflection-odd. These are compatible statements because the quadratic observable contains its square.

For B_(mu nu)^c = (dA^c)_(mu nu), put

\[
O_{\mu\nu,a}(f)=\frac{a^4}{2}
\sum_{z\in Z_{\mu\nu,a}} f(z)\sum_{c=1}^3
\left((B_{\mu\nu}^c(z))^2-\mathbb E_G[(B_{\mu\nu}^c(z))^2]\right),
\]
\[
O_a^D=O_{12,a}-O_{34,a},\qquad
q^D_a(f)=\mathbb E_G[O_a^D(\theta f)O_a^D(f)],\qquad
q_{\mu\nu,a}(f)=\mathbb E_G[O_{\mu\nu,a}(\theta f)O_{\mu\nu,a}(f)].
\]

Thus q_(12,a) is precisely q_a of L003. No interacting independence, renormalized operator matching, or running coupling is assumed.

## Conclusion

At each fixed mesh,

\[
\lim_{g\downarrow0}Q^D_{a,g}(f)=q^D_a(f),
\qquad
q^D_a(f)=q_{12,a}(f)+q_{34,a}(f),
\qquad q_{34,a}(f)\ge0.
\]

The separated Gaussian mesh limit exists and is finite, with

\[
q^D_{\rm box}(f):=\lim_{\substack{N\to\infty\\N\ {\rm even}}}q^D_{8/N}(f)
\ge q_{\rm box}(f)\ge\tfrac32d_{\rm box}^2>0.
\]

Here the constants are the same as in L003:

\[
\Omega_* =\frac{\pi\sqrt5}{8},\qquad
m_\phi=\frac{\cos^2(\pi/16)\cos^2(\pi/32)}{128},\qquad
d_{\rm box}=
\frac{m_\phi(\pi^2/16)\sinh^2(2\Omega_*)}
{\Omega_*\sinh(8\Omega_*)}.
\]

Consequently, at every sufficiently small even mesh,

\[
q^D_a(f)\ge c_{\rm box}:=\tfrac34d_{\rm box}^2>0.
\]

The result is an iterated free limit in a fixed box. It neither bounds an interacting remainder uniformly in a nor constructs an interacting continuum theory or a mass gap.

## Proof

### 1. Fixed-mesh Wilson matching and the mixed terms

L003 proves that the relative one-cochain Hodge Laplacian d*d + dd* is a direct sum over potential components. Each component is a tensor sum of the interval vertex Dirichlet and edge Neumann Laplacians, with no coupling to other components. Thus the centered Gaussian potential families A_1,A_2,A_3,A_4 are independent, as are the colors. The Gaussian curvature law is the gauge-quotient quadratic Wilson law established there; component independence of this chosen Gaussian is used only to calculate that curvature law.

The entire 12 curvature family depends only on A_1,A_2, and the entire 34 curvature family only on A_3,A_4. Hence these two curvature families are independent, including at reflected arguments. In particular,

\[
\mathbb E_G[B_{12}^c(z)B_{34}^d(w)]=0,
\qquad
\mathbb E_G[O_{12,a}(\theta f)O_{34,a}(f)]
=\mathbb E_G[O_{34,a}(\theta f)O_{12,a}(f)]=0.
\]

The second equality uses centering as well as independence. Expanding the difference gives exactly q^D_a = q_(12,a) + q_(34,a). This is a calculation of the mixed terms, not an inference from separate positive bounds.

The expansion used in L003 applies to every plaquette orientation:

\[
P_p=\frac{g^2a^4}{8}\sum_c(B_p^c)^2+O(g^3).
\]

Its fixed-mesh forest gauge reduction has the same unique nondegenerate minimum regardless of which finite list of plaquette sums is inserted. In its small coordinate neighborhood, each rescaled sum is bounded by a mesh-dependent constant times |A|^2; products of two sums by a constant times |A|^4. The Gaussian domination and exponentially suppressed complement in that proof therefore apply simultaneously to the 12 and 34 sums and their reflections. Joint first and second moment convergence, followed by centering, gives the claimed fixed-mesh limit for Q^D. There is no estimate uniform in the mesh in this argument.

### 2. The electric time covariance and its contact term

Use L003's interval modes v_k on interior vertices and e_k on edge midpoints, with e_0 = 8^(-1/2), and

\[
Dv_k=\omega_{k,a}e_k,\qquad
D^*e_k=\omega_{k,a}v_k,\qquad
\omega_{k,a}=\frac2a\sin\frac{k\pi}{2N},\quad \omega_{0,a}=0.
\]

For the 34 curvature the spatial indices, waves, and frequencies are

\[
\mathcal J_N=\{(k_1,k_2,k_3):1\le k_1,k_2\le N-1,
\quad 0\le k_3\le N-1\},
\]
\[
\chi_k(x)=v_{k_1}(x_1)v_{k_2}(x_2)e_{k_3}(x_3),\qquad
\beta_{k,a}=\omega_{k_1,a}^2+\omega_{k_2,a}^2>0,\qquad
\Omega_{k,a}^2=\beta_{k,a}+\omega_{k_3,a}^2.
\]

For each k, the term D_3 A_4 contributes omega_(k3,a)^2 times the temporal edge resolvent (DD* + Omega^2)^(-1). It is absent when k3 = 0, as the zero coefficient correctly records. The term -D_4 A_3 contributes D(D*D + Omega^2)^(-1)D*. These potential components are independent. The elementary intertwining identity gives

\[
D(D^*D+\Omega^2)^{-1}D^*
=DD^*(DD^*+\Omega^2)^{-1}
=I-\Omega^2(DD^*+\Omega^2)^{-1}.
\]

Indeed (DD* + Omega^2)D = D(D*D + Omega^2), and both shifted operators are invertible. This identity includes the constant edge mode; it does not invert DD* without its positive shift. The electric covariance for that spatial mode is therefore

\[
I-\beta_{k,a}(DD^*+\Omega_{k,a}^2)^{-1}.
\]

Relative to the time measure a times counting measure, the identity operator has kernel delta_(ij)/a. Its contribution vanishes between a negative reflected temporal edge and a positive temporal edge, since those edges are distinct. This contact term is discarded only for the separated reflection calculation.

### 3. The Neumann edge Green function

Write temporal edge centers as t_i = -4 + (i+1/2)a, for 0 <= i < N. For Omega > 0 define gamma = (2/a) asinh(a Omega/2). The kernel of (DD* + Omega^2)^(-1), relative to the measure a times counting measure, is

\[
G^N_{a,\Omega}(t,s)=
\frac{a\cosh(\gamma(t+4))\cosh(\gamma(4-s))}
{\sinh(a\gamma)\sinh(8\gamma)},\qquad t\le s,
\]

and is symmetric in t,s. The superscript N denotes Neumann boundary conditions here.

To verify it, set eta = a gamma, u_i = cosh((i+1/2)eta), and w_i = cosh((N-i-1/2)eta). The interior recurrence has diagonal 2 cosh eta = 2 + a^2 Omega^2 and off-diagonals -1. The endpoint rows have diagonal 1 + a^2 Omega^2, equivalently ghost conditions u_(-1) = u_0 and w_N = w_(N-1). Both displayed functions obey their respective endpoint condition and the interior recurrence. Their discrete Wronskian is

\[
u_{j+1}w_j-u_jw_{j+1}=\sinh\eta\sinh(N\eta).
\]

It follows by applying the recurrence at the join that a u_(min(i,j)) w_(max(i,j)) divided by this Wronskian has image delta_(ij)/a under DD* + Omega^2. This proves the kernel formula and its normalization, including the endpoint rows. Positivity of the shifted operator gives uniqueness.

For positive temporal edge centers t,s it factors as

\[
G^N_{a,\Omega}(-t,s)=r_{a,\Omega}h^N_{a,\Omega}(t)h^N_{a,\Omega}(s),
\qquad
r_{a,\Omega}=\frac a{\sinh(a\gamma)\sinh(8\gamma)}>0,
\quad h^N_{a,\Omega}(t)=\cosh(\gamma(4-t)).
\]

The one-color, untransformed electric curvature covariance at reflected arguments is consequently

\[
C^\theta_{34,a}(z,w)
:=\mathbb E_G[B_{34}^c(\theta z)B_{34}^c(w)]
=-\sum_{k\in\mathcal J_N}\beta_{k,a}r_{a,\Omega_{k,a}}
\chi_k(x)\chi_k(y)h^N_{a,\Omega_{k,a}}(t)h^N_{a,\Omega_{k,a}}(s).
\]

The overall minus sign is consistent with the electric curvature's odd reflection parity. The square observable is even, so its reflected Wick contraction is the square of this covariance, with no additional minus sign.

For clarity, set b^E_(k,a) = beta_(k,a) r_(a,Omega_(k,a)) > 0 and psi^E_(k,a)(x,t) = chi_k(x) h^N_(a,Omega_(k,a))(t). The centered Gaussian square identity, three colors, and the factor 1/2 in each insertion give

\[
\begin{aligned}
q_{34,a}(f)
&=\frac32 a^8\sum_{z,w\in Z_{34,a}}
f(z)f(w)\bigl(C^\theta_{34,a}(z,w)\bigr)^2\\
&=\frac32\sum_{k,l\in\mathcal J_N}b^E_{k,a}b^E_{l,a}
\left(a^4\sum_{z\in Z_{34,a}}
f(z)\psi^E_{k,a}(z)\psi^E_{l,a}(z)\right)^2\ge0.
\end{aligned}
\]

All finite sums involve only support in positive time. This also proves nonnegativity for any real test with that support; only the quantitative lower bound imported for the magnetic part uses this particular nonnegative f.

### 4. Separated mesh convergence

For fixed k, omega_(kj,a) tends to pi k_j/8, Omega_(k,a) tends to Omega_k = pi |k|/8, gamma_(k,a) tends to Omega_k, and a/sinh(a gamma_(k,a)) tends to 1/Omega_k. The spatial waves are restrictions of fixed trigonometric functions. The limiting reflected electric kernel is thus the series

\[
C^\theta_{34,\rm box}(z,w)=
-\sum_{\substack{k_1,k_2\ge1\\k_3\ge0}}
\frac{\beta_k\chi_k(x)\chi_k(y)}{\Omega_k\sinh(8\Omega_k)}
\cosh(\Omega_k(4-t))\cosh(\Omega_k(4-s)),
\quad \beta_k=(\pi/8)^2(k_1^2+k_2^2).
\]

Here is a uniform summable bound that justifies this limit. The same elementary sine and asinh bounds as in L003 give

\[
\frac{|k|}{4}\le\Omega_{k,a}\le\frac{\pi|k|}{8},\qquad
\gamma_{k,a}\ge\frac{\Omega_{k,a}}2\ge\frac{|k|}{8}.
\]

For t,s in [1,2], using cosh u <= exp(u) for u >= 0 and a/sinh(a gamma) <= 1/gamma yields

\[
0<G^N_{a,\Omega_{k,a}}(-t,s)
\le\frac{4}{\Omega_{k,a}(1-e^{-2})}
\exp\!\left[-\frac{\Omega_{k,a}}2(t+s)\right].
\]

The denominator estimate uses 16 gamma_(k,a) >= 2|k| >= 2. Also |chi_k(x)chi_k(y)| <= 1/64 and beta_(k,a) <= Omega_(k,a)^2. Hence each summand in the reflected electric covariance is at most

\[
\frac{\pi|k|}{128(1-e^{-2})}\,e^{-|k|/4}
\]

in absolute value, uniformly on K times K and in the mesh. This is summable over the three spatial indices. Extend each finite series by zero on missing indices and evaluate its noncontact trigonometric formula throughout K times K. Convergence of fixed modes and this tail bound give uniform convergence to the displayed continuous, bounded kernel.

The 34 plaquette centers form a product Riemann grid, shifted by half a mesh in directions 3,4. Uniform kernel convergence and the ordinary Riemann-sum theorem therefore prove

\[
q_{34,a}(f)\longrightarrow q_{34,\rm box}(f)
=\frac32\int_K\!\int_K f(z)f(w)
\bigl(C^\theta_{34,\rm box}(z,w)\bigr)^2\,dz\,dw<\infty.
\]

This limit is nonnegative, either directly from the integral for f >= 0 or from the nonnegative finite forms. L003 supplies convergence and its explicit positive bound for q_(12,a). Adding the two limits proves finiteness and positivity of q^D_box. At every mesh where L003 gives q_(12,a) >= c_box, the exact sum identity gives q^D_a >= c_box as well. No new choice of the constant is needed.

### 5. Required interacting threshold and scope

For a specified and correctly matched interacting observable along a specified trajectory g(a), the remaining comparison would require

\[
\left|Q^{D,\mathrm{matched}}_{a,g(a)}(f)-q^D_a(f)\right|
\le c_{\rm box}/2
\]

uniformly for sufficiently small a. That would imply a positive lower bound c_box/2 for this one reflected insertion. This lemma establishes the Gaussian side of that threshold and supplies no interacting error estimate. In particular, the exact zero mixed covariance is a property of the free quadratic law, not of the Wilson measure at positive g.

The channel was motivated by L004's stress-tensor projection; no perturbative renormalization identity from that motivation is needed for the present proof. Finite lattice matching, possible boundary effects, a controlled coupling trajectory, construction and reflection positivity of the full limiting field algebra, removal of the infrared box, other gauge groups, and finite positive mass remain open. A separated composite correlation is not an ordinary all-moment composite-field limit, and the positive box frequencies are not a physical mass gap.

Finite computational checks are reproducible with `PYTHONDONTWRITEBYTECODE=1 python3 scripts/complementary-plaquette/check.py`. They compare independent matrix inverses with the edge Green formula and the electric resolvent identity, and compare a full relative-cochain curvature covariance with the spatial-mode formula. They also check the zero mixed covariance. These checks support normalization and sign bookkeeping; the mesh limit and uniform lower bound are proved above, not inferred numerically.

## Mathlib

Coverage of the full complementary-plaquette reflection statement: **not checked**. Coverage of supporting finite Gaussian independence, Wick moments, resolvent identities, finite difference equations, dominated convergence, and Riemann sums: **not checked**. No inspected Mathlib theorem names or direct library links are asserted. The existing L003 Gaussian and magnetic-bound inputs are used with their stated qualifications; the electric kernel, mixed-term calculation, and separated convergence are proved here.
