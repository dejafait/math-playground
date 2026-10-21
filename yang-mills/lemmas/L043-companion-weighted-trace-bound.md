# L043 — The complete signed companion is O(a^-2)

## Hypotheses

Keep L040–L042's exact fixed-box, SU(2), straight-forest hypotheses,
ordinary dimensionless matrices, original probes i=3,6, tau=1/16 and
admitted meshes a=8/N. Include every upper (1,mu) plaquette and every
transverse end edge. Take the small-coupling coefficient at fixed mesh
first. Constants may depend on these fixed smooth data, not on a.

Write Delta=Delta_3, G=Delta^(-1), A=bar A and
P_i=G h_3 bar Q_i h_3 G, R=G A G as in L040. Write
F_i(v)=N(P_i)_(vv), Z(v)=N R_(vv), with zero boundary values.
The smooth extension of F_i has uniformly bounded C^2 norm by L042.
The compact smooth coefficient extensions bar u_j and
w_j=T_j bar u_j/a have uniformly bounded derivatives of every fixed
order. Here T_j=(S_j-S_j^(-1))/2, Delta_j=2-S_j-S_j^(-1) and
j ranges over {2,3,4}. The **actual discrete** divergence satisfies
sum_j w_j=0: L040(12)'s two central derivatives commute. This is
separate from L042's continuum divergence statement.

## Conclusion

For L041's complete signed H,L trace and both original probes,

\[
 |T_{i,a}|\le C_i a^{-2},\qquad
 \left|\sum_p G^{(0)}_{i,p}\right|\le C'_i a^{-2}.       \tag{1}
\]

Thus all growth strictly stronger than a^-2 is excluded for this
selected companion, improving L042's qualitative o(a^-4) result.
No existence or value of lim a^2 T_(i,a), cancellation against L039,
full power/logarithmic coefficient or finite matching is asserted.
The complete response, interacting reflected error <=c_box/2,
continuum field axioms and finite positive mass remain unresolved.

## Proof

### 1. An exact sum identity with all pinned end edges

Use all transverse edges e=(v,v'), with a boundary evaluation of any
matrix or diagonal interpreted as zero. For symmetric P=P_i and R,
expanding eta_H=(delta_v+delta_v')/2 and eta_L=delta_v-delta_v'
from L040 gives

\[
 u_hv_l+u_lv_h-2u_bv_b
 =N^2\{P_{vv}R_{v'v'}+P_{v'v'}R_{vv}-2P_{vv'}R_{vv'}\}.
                                                               \tag{2}
\]

Put p(v)=P_(vv), r(v)=R_(vv). The exact graph identity is

\[
\begin{split}
\sum_e\{p(v)r(v')+p(v')r(v)-2P_{vv'}R_{vv'}\}
={}&\operatorname{Tr}(M_p\Delta R)
       -\sum_v(\Delta p)(v)r(v)\\
 &+\sum_e\{p(v)+p(v')-2P_{vv'}\}R_{vv'}.             \tag{3}
\end{split}
\]

To check it, the trace term contributes on each edge
p(v)(r(v)-R_(vv'))+p(v')(r(v')-R_(vv')). The second term is
minus (p(v)-p(v'))(r(v)-r(v')). Adding the last term yields
exactly the left side, edge by edge. The Dirichlet Laplacian includes
end edges, so this derivation also holds at pinned endpoints; no
boundary flux has been omitted.

Since Delta R=A G, p=F_i/N, r=Z/N and
N R_(vv')=v_h-v_l/4, (2)–(3) imply

\[
\begin{split}
S_{i,a}:=\sum_e(u_hv_l+u_lv_h-2u_bv_b)
={}&N\operatorname{Tr}(M_{F_i}A G)
 -\sum_v(\Delta F_i)(v)Z(v)\\
 &+\sum_e u_l(v_h-v_l/4).                            \tag{4}
\end{split}
\]

L041–L042 give |Z|+|v_h|+|v_l|<=C/a, |u_l|<=C_i a^2 and
|Delta F_i|<=C_i a^2, including vertices adjacent to pinned faces.
There are O(a^-3) vertices/edges. The last two sums in (4) are
therefore O(a^-2). It remains to bound its weighted trace.

### 2. Exact infinite-lattice diagonal cancellation

On Z^3 define the dimensionless Green kernel

\[
 g(n)=\int_{[-\pi,\pi]^3}\frac{e^{i n\cdot\theta}}
        {\lambda(\theta)}\frac{d\theta}{(2\pi)^3},
 \quad \lambda=\sum_j(2-2\cos\theta_j).               \tag{5}
\]

The integral is absolutely convergent: near zero its integrand is
O(|theta|^-2), integrable in three dimensions. It is real, invariant
under coordinate reflections/permutations, and Delta g=delta_0 by
multiplying the integrable Fourier integrand by lambda. Let
b_0=g(0), b_1=g(e_j), b_2=g(2e_j). At zero,
6(b_0-b_1)=1. The full kernel is positive semidefinite on any finite
set because its quadratic forms are the integrals of
|sum_v c_v e^(i v dot theta)|^2/lambda. In particular b_0 is finite
and positive. We use no unproved pointwise Green asymptotic.

Extend the coefficient stencils by zero outside their fixed compact
support. At a row v, apply L040(10)–(11) to the column g(y-v).
For the transport, (K^T Delta g)_(v)=0, since Delta g is supported
at v and K has zero diagonal. Also T_k g(v-v)=0 and
T_k g(+-e_j)=0 for k different from j by reflection symmetry.
Consequently

\[
 \big((\Delta K+K^T\Delta)g/2\big)(v)
       =\frac{b_0-b_2}{2}\sum_j w_j(v).               \tag{6}
\]

For the triplet the two incident edge weights in direction j are
(w_j(v)+w_j(v+-e_j))/2. Thus

\[
 (Q_3g)(v)=(b_0-b_1)\sum_j
       \left\{2w_j(v)-\frac12(\Delta_j w_j)(v)\right\}. \tag{7}
\]

For every shear pair j different from k, the factors T_k g(+-e_j)
and T_j g(+-e_k) vanish. Hence (Q_6g)(v)=0 even for variable shear
coefficients. Equations (6)–(7) give, before imposing divergence zero,

\[
 (A G_\infty)_{vv}
 =\left(\frac{b_0-b_2}{2}-2(b_0-b_1)\right)\sum_jw_j(v)
   +\frac{b_0-b_1}{2}\sum_j(\Delta_j w_j)(v).
\]

Using the exact central divergence and b_0-b_1=1/6 gives

\[
 (A G_\infty)_{vv}=\frac1{12}\sum_j(\Delta_j w_j)(v).
                                                               \tag{8}
\]

Every physical second derivative of w_j is uniformly bounded, so
|Delta_j w_j|<=C a^2 by the central Taylor formula. All nonzero rows
are compactly interior. Since F_i is bounded and their number is
O(a^-3),

\[
 |\operatorname{Tr}(M_{F_i}A G_\infty)|\le C_i a^{-1}.
                                                               \tag{9}
\]

Here G_infinity means its kernel restricted to the finite cube.
Restriction does not change (8) on a nonzero row, because that row's
entire stencil is interior. Formula (8) does not say A=0 or that
individual Green dipoles vanish.

### 3. Control the physical-boundary correction by harmonic energy

Set D=G_infinity-G on the interior vertices. We prove D>=0,
D_(vv)<=b_0 and harmonicity on compact interior rows, rather than
assuming a convergence rate to an infinite-volume kernel.

For a real source c supported on the cube, finite-dimensional energy
completion gives

\[
 c^T Gc=\sup_{h\text{ supported on cube interiors}}
       \{2\langle c,h\rangle-\langle h,\Delta h\rangle\}.
\]

Zero extension of h has exactly this Dirichlet energy on Z^3.
Fourier completion of the square, or weighted Cauchy–Schwarz, bounds
each expression by integral |hat c|^2/lambda=c^T G_infinity c.
The latter is finite by (5), since hat c is bounded. Thus D is
positive semidefinite. Since G is positive definite,
0<=D_(vv)<=b_0. This argument needs no bounded infinite inverse on
l^2 or monopole l^2 approximation.

For a vertex v whose full nearest-neighbor row is interior, Delta
applied to G_infinity in its first variable is the identity row by
(5); the same holds for G. Hence (Delta D)_(v,y)=0 for every interior
y. Realize D as the covariance of a finite, possibly degenerate,
centered Gaussian vector f. Then Delta f(v)=0 almost surely at each
such vertex: its variance is (Delta D Delta^T)_(vv)=0. There are
finitely many vertices, so these statements hold simultaneously.
Extend f by zero to boundary vertices for the edge identities below.

Choose a fixed smooth compact cutoff chi in (-4,4)^3 equal to one
on all nonzero coefficient rows and columns of A and their neighbors,
for every sufficiently fine mesh. Its support stays away from faces,
and |chi(v')-chi(v)|<=C a on edges. Put h=chi f. Exact summation by
parts on the full pinned graph gives

\[
 \|h\|_E^2=\langle\chi^2 f,\Delta f\rangle
             +\sum_{(v,v')}(\chi(v)-\chi(v'))^2 f(v)f(v'),
 \quad \|h\|_E^2=\langle h,\Delta h\rangle.           \tag{10}
\]

Indeed, on each edge, (chi_v f_v-chi_w f_w)^2 minus
(chi_v^2 f_v-chi_w^2 f_w)(f_v-f_w) is
(chi_v-chi_w)^2 f_v f_w. This also verifies every end edge.
The first term of (10) vanishes because chi is supported on harmonic
rows. Since |E f(v)f(v')|<=b_0 by covariance Cauchy–Schwarz,

\[
 E\|h\|_E^2\le C a^2\,O(a^{-3})\le C a^{-1},
 \qquad E\|h\|_2^2\le C a^{-3}.                     \tag{11}
\]

No positivity of the pointwise off-diagonal covariance is needed.
For the bounded smooth F_i, the elementary edge product rule gives

\[
 \|F_i h\|_E^2\le C_i\{\|h\|_E^2+a^2\|h\|_2^2\}.
                                                               \tag{12}
\]

This follows by writing the edge difference of F_i h as
F_i(v)(h(v)-h(v'))+(F_i(v)-F_i(v'))h(v') and using its bounded
first physical derivative. It holds at endpoints as well.

L041(13) implies the bilinear energy estimate
|<x,A y>|<=C ||x||_E ||y||_E. For example conjugating by the positive
Dirichlet Delta^(1/2) gives a symmetric matrix of norm <=C.
Since chi=1 on all rows and columns of A,

\[
\begin{split}
 |\operatorname{Tr}(M_{F_i}A D)|
 &=|E\langle F_i f,A f\rangle|
  =|E\langle F_i h,A h\rangle|\\
 &\le C(E\|F_i h\|_E^2)^{1/2}(E\|h\|_E^2)^{1/2}
  \le C_i a^{-1}.                                   \tag{13}
\end{split}
\]

Thus the physical-boundary correction is bounded with its full kernel
retained. The bound is deliberately sufficient for the power threshold;
it gives no scaled limit and does not claim pointwise O(a^2) for the
finite-box diagonal.

### 4. Assemble the estimate and delimit its use

Since G=G_infinity-D, (9) and (13) give
|Tr(M_(F_i) A G)|<=C_i a^-1. Multiplying by N=8/a and using (4)
proves S_(i,a)=O(a^-2). L041's color factor T_(i,a)=-3 S_(i,a)
proves the first assertion of (1). Its d-containing remainder is
O(a^-1), so the second assertion follows as well. All physical
boundary strips were included throughout; no unflowed heat factor
was added, and the original probe weights were preserved.

The finite identity checks are reproduced by
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_companion_weighted_trace.py`.
The full certificate is
`scripts/combined-ward-response/companion-weighted-trace-certificate.json`.
All 1,385 checks have exactly zero defect: all 75 coefficient basis
values in the complete radius-two row for (6)–(8), one divergence-free
stream polynomial with nonzero second-order diagonal, the complete
symmetric P,R basis pairs on the pinned N=2,3 cubes, and 12 dense
rational P,R checks at N=4. The local kernel values obey the exact
Green equations at zero and its neighbors, and all required reflection
and permutation symmetries; they test the algebra, not an approximation
to the actual kernel. The analytic argument above supplies the
all-mesh bound. A finite preview or numerical extrapolation is not
used as evidence for that bound.

Reuse `drafts/literature/2026-09-26-current-target.md`, SPECIALIZE.
The inspected bulk input remains Luescher–Weisz, *Perturbative analysis
of the gradient flow in non-abelian gauge theories*,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7.1–7.4,
(7.1)–(7.8), and section 8.2, with ordinary bulk renormalization and
its stated R^4 scope. It supplies neither the present unflowed
fixed-box trace bound nor physical-boundary compensation. It is not
reproved. Here elementary Fourier positivity, finite energy completion,
a cutoff energy identity and the exact compressed stencils provide
the required specialization. Classify this local standard-method
progress as REPRODUCTION; no originality claim is made.

An O(a^-2) upper bound clears the stronger-power test but is neither a
limit nor a sign. Comparison with L030/L039 requires a justified value
for a^2 T_(i,a), specifically +48 I_i to cancel their selected
negative coefficient. That value is not assumed here. Even cancellation
would leave subleading powers/logarithms, other plaquettes and nonlinear
jets, L019's inter-group compensation, finite matching, the interacting
reflected-error threshold c_box/2 and the continuum/infrared problem.

## Mathlib

Coverage of the full signed fixed-box companion bound: **not checked**.
Coverage of supporting lattice Fourier kernels, covariance ordering,
finite Gaussian representations, energy completion and discrete cutoff
identities: **not checked**. No matching Mathlib theorem is asserted;
unknown coverage is not evidence of absence.
