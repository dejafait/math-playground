# L290 — Quadratic limits of both mixed cubic insertion/action groups

## Hypotheses

Use L280's SU(2) relative cube D=[-4,4]^4, even N>=2 and a=8/N.
Pin all boundary-contained links, fix gauges at all boundary vertices,
and retain every other link, including both normal endpoint cases.
All matrices use Euclidean counting measure and all pinned slots are
zero. Keep all three colors. Use the exact nonnegative product bump
of L282, as retained in L289: h_+=f_* and h_-=theta f_*, supported in
[-1/4,1/4]^3 times [1,2] and [-2,-1], respectively. Source derivatives
are at zero in (|s|+|t|)||f_*||_infinity<eta<1.

All ambient all-link Wilson jets remain on L280's own slice. In the
notation and normalization of L286(4)–(5) and L287(1), put

\[
 V(x)=T[x^3]/6=\sum_p(Cx)_p\cdot\zeta_p(x),\qquad
 V_h(x)=T_h[x^3]/6=\sum_{p\parallel12}h(z_p)(Cx)_p\cdot\zeta_p(x).
                                                               \tag{1}
\]

Here C is the complete relative incidence and zeta uses the actual four
ordered signed link slots. In particular there is no extra a^4 in
either plaquette sum. Let G and G_pm be L280(18)'s extended transverse
covariance and its single-source derivatives. Retain I_1 and Z_0 from
L289, and J_f from L284(2). The separate audits of L286–L289 accept
those inputs under their stated hypotheses; this derivation alone did
not discharge that verification.

## Conclusion

Both ENTIRE mixed insertion/action groups of L280(20) have the limits

\[
 \boxed{\displaystyle
 \lim N^{-2}\left[-\tfrac12\mathcal B(T_-,T;G_+,G,G)\right]
 =\lim N^{-2}\left[-\tfrac12\mathcal B(T_+,T;G_-,G,G)\right]
 =-\frac{3I_1}{16}\mathcal J_f .}                            \tag{2}
\]

Each limit includes o(N^2) error for the complete finite-box quantity,
with every action anchor, color, edge offset and boundary row retained.
Write their sum as J_{3,N}. Including L286's insertion pair and L289's
mixed-covariance action group M_{3,N}, the resulting subtotal is

\[
 \lim N^{-2}\{I_{3,N}+J_{3,N}+M_{3,N}
                    +\mathcal K_4^H+\operatorname{Tr}(DG_{-+})\}
 =\frac{Z_0-24I_1}{64}\mathcal J_f
 =\frac{3-22Z_0}{128}\mathcal J_f.                           \tag{3}
\]

Consequently the sole unestimated cubic group is exactly

\[
 D_{3,N}:=\tfrac12\mathcal B(T,T;G_-,G_+,G),\qquad
 N^{-2}\kappa_a=N^{-2}D_{3,N}
                   +\frac{3-22Z_0}{128}\mathcal J_f+o(1).  \tag{4}
\]

No scale, limit or compensation is asserted for D_{3,N}. Subleading
control, a mesh-uniform higher remainder, physical trajectory/composite
mixing, continuum axioms/positivity, a nonzero sector and finite positive
mass remain open. This is partial local progress under the prior EXPLORE
assessment, not certified originality or a complete-solution candidate.
The separate audit in section 6 accepts these limits under the stated hypotheses.

## Proof

### 1. Two separated nuclear-norm estimates

Suppress color. Take h=h_- and bar h=h_+, and put
U=GC_+^*W_+, W_+=diag(sqrt(h_+)), so G_+=UU^*. Let chi be the
orthogonal edge restriction to all slots incident to 12-plaquettes
where h_->0. Only directions 1 and 2 occur. For all sufficiently
small a these edges lie in L284(9)'s compact set E_-, and the opposite
source lies in E_+. No mesh limit or boundary deletion defines chi:
it is just the exact support of the differentiated insertion.

L281(10) and L287(14) give

\[
 \|U\|\le C_fN,\qquad \|CU\|\le C_f.                       \tag{5}
\]

We need the stronger separated estimate

\[
 \|\chi U\|_1\le C_fN,\qquad
 \|G_+\chi\|_1\le C_fN^2.                                 \tag{6}
\]

Here ||.||_1 is the finite-matrix nuclear norm. To prove the first
inequality, use the exact edge-to-12-plaquette series L284(7)–(8),
with R_N=GC_12^*=a^3R_a, and the exact time factor of L003 section 3.
For t<s that factor is

\[
 G_{a,\Omega}(t,s)=r_{k,a}\sinh(\gamma(t+4))
                                   \sinh(\gamma(4-s)),\qquad
 r_{k,a}=\frac{a}{\sinh(a\gamma)\sinh(8\gamma)}.             \tag{7}
\]

For each edge component mu=1,2 and each of its allowed spatial k,
its contribution to chi U is therefore rank one. Before the a^3
factor it has entries

\[
 \pm\omega_{k_j,a}r_{k,a}
 [\chi(e)\chi_{\mu,k}(x_{e,sp})\sinh(\gamma(t_e+4))]
 [\phi_k(z_{p,sp})\sinh(\gamma(4-s_p))\sqrt{h_+(z_p)}],
                                                               \tag{8}
\]

where j=2 for mu=1 and j=1 for mu=2; all mode sets and signs are
exactly L284(8)'s. A term with zero omega is zero. The estimates
L284(10)–(11) bound the supremum of the absolute product in (8)
on the rectangular separated supports by C_f exp(-|k|/8).
Because the product factors into an edge function and a source
function, the product of their suprema satisfies the same bound.
Each grid has O(N^4) points. The nuclear norm of this rank-one term,
including its a^3, is at most

\[
 C_f a^3N^4e^{-|k|/8}\le C_f'N e^{-|k|/8}.                 \tag{9}
\]

Summing over the two components and all allowed three-dimensional
indices proves (6). The exponential series converges and also bounds
the entire discarded spatial-mode tail divided by N, uniformly in N.
No unestimated truncation is used. The second inequality follows from
G_+chi=U(U^*chi), (5), and ||AB||_1<=||A||||B||_1. The finitely many
coarser even meshes are included by increasing C_f; empty sources give
zero matrices. Reflection proves the same estimates with signs reversed.

A second bound needed below is already supplied by L281's separated
curvature matrix, denoted here by mathsf T to distinguish it from the
cubic tensor:

\[
 \|\operatorname{diag}(h_-)C_-U\|_1
 =\|W_-\mathsf T\|_1\le\sqrt{F}\,\|\mathsf T\|_1\le C_f,
 \quad\mathsf T=W_-C_-GC_+^*W_+,\quad F=\|f_*\|_\infty.
                                                               \tag{10}
\]

Thus local external curls have a bounded nuclear norm, whereas local
external edge fields have nuclear norm O(N). These are different
estimates; a pointwise kernel bound alone would not establish (6).

### 2. Removing external curls with a fully summed error

Work in the real Hilbert space of centered quadratic Gaussian
polynomials for x of covariance G tensor I_3. Define linear maps
from external edge/color vectors to this space by

\[
 \begin{split}
 A_h(u)&=\sum_{p\parallel12}h_p(Cu)_p\cdot\zeta_p(x),\\
 B_h(u)&=\sum_{p\parallel12}h_p(Cx)_p\cdot D\zeta_p(x)[u],\\
 A(u)&=\sum_p(Cu)_p\cdot\zeta_p(x),\\
 B(u)&=\sum_p(Cx)_p\cdot D\zeta_p(x)[u].
 \end{split}                                                   \tag{11}
\]

All polynomials are centered: every monomial has two distinct field
colors. L287's monomial estimates apply with the weights h_p inserted
in the coefficient vector. More explicitly, its proof for the
external-curl map factors through Z: alpha -> sum_p alpha_p dot
zeta_p(x), with ||Z||<=C sqrt(ell_N), ell_N=log(eN), on all plaquettes
or any orientation restriction. Its internal-curl proof gives

\[
 \|B\|\le C,\quad \|B_h\|\le C_f,\quad B_h=B_h\chi,
 \quad A=ZC,\quad A_h=Z_{12}\operatorname{diag}(h)C_- .     \tag{12}
\]

The bound for Z follows from L287(7), (9): each product of two
undifferentiated selected covariance rows has absolute row sum
O(ell_N), with bounded slot multiplicity. The bound for B_h follows
from L287(10)–(12)'s positive Schur-product estimate, applied to
h_p u_{e(p)}. This keeps all cross terms between its finitely many
types and every plaquette pair. No derivative of h is involved.

Extend U diagonally over the three colors. Equations (5), (6),
(10) and (12) give

\[
 \begin{array}{ll}
 \|AU\|\le C_f\sqrt{\ell_N},&\|BU\|\le C_fN,\\
 \|A_hU\|_1\le C_f\sqrt{\ell_N},&\|B_hU\|_1\le C_fN.
 \end{array}                                                   \tag{13}
\]

The nuclear norm of a map into this Gaussian Hilbert space is defined
on its finite-dimensional range. All trace inequalities here are
ordinary finite-rank singular-value inequalities.

Define matrices E_h and E_h^int by

\[
 u^*E_hv=2\mathbb E[DV_h(x)[u]DV(x)[v]],\qquad
 u^*E_h^{\rm int}v=2\mathbb E[B_h(u)B(v)].                  \tag{14}
\]

They need not be symmetric. Color rotations make each a scalar edge
matrix tensored with I_3, as in L287 section 3. Since DV_h=A_h+B_h,
DV=A+B, the three discarded terms are exactly AA, AB and BA.
For maps P,Q from the source space, |Tr(P^*Q)|<=||P||_1||Q||.
Apply this to (13), with the source-local map always in nuclear norm.
It follows that

\[
 |\operatorname{Tr}((E_h-E_h^{\rm int})G_+)|
       \le C_f(\ell_N+N\sqrt{\ell_N})=o(N^2).              \tag{15}
\]

Both quadratic derivatives have the factor 1/2 in T_h[u,x,x] and
T[v,x,x]. Their two crossing Gaussian pairings therefore give
(E_h)_{il}=sum T_{h,ijk}T_{lmn}G_{jm}G_{kn}; the internal pairing
vanishes by color. Thus the exact original mixed term is
-Tr(E_hG_+)/2. Equation (15) controls its complete external-curl
error without replacing either vertex by a scalar model.

### 3. Uniform approximation of the weighted internal operator

Use exactly L288(2)'s positive transverse polynomial covariance
widehat G_{N,m}=C^*C h_m(L)^2 and R=G-widehat G. Define E_{h,m}^int
by (14) with x of covariance widehat G tensor I_3. Then

\[
 \|E_h^{\rm int}-E_{h,m}^{\rm int}\|\le C_f/(m+1),\qquad
 \|E_{h,m}^{\rm int}\|\le C_f.                            \tag{16}
\]

Here is the weighted specialization, since the unweighted positive
operator inequality alone is not (16). Couple x=y+z with independent
covariances widehat G and R. As in L288(11), write
B_h(u;y+z)=B_h(u;y)+Z_h(u), and B(v;y+z)=B(v;y)+Z(v).
In each of the three residual polynomials, multiply the coefficient
of the type at its first vertex by h_p. The same estimates using
sup R_ee<=960/(m+1), sup(CRC*)_pp<=122880/(m+1)^2 and
||widehat G||<=(m+1)/16 give

\[
 \mathbb E|Z_h(u)|^2\le C_f(m+1)^{-1}\|u\|^2,
 \qquad \mathbb E|Z(v)|^2\le C(m+1)^{-1}\|v\|^2.          \tag{17}
\]

All types still have bounded edge-slot multiplicity; h only changes
their coefficient norm by ||h||_infinity. Each residual has conditional
mean zero given y, including B_h(u;z) by its distinct field colors.
The exact cross-covariance difference is consequently
2 E[Z_h(u)Z(v)]. Cauchy–Schwarz proves (16), and the original
weighted/unweighted B bounds give its second inequality. No positivity
or symmetry of this cross matrix is claimed.

Both E_h^int and E_{h,m}^int have rows supported in chi. Thus the
difference D satisfies D=chi D. Trace cyclicity, (6) and (16) imply

\[
 N^{-2}|\operatorname{Tr}((E_h^{\rm int}-E_{h,m}^{\rm int})G_+)|
       \le C_f/(m+1).                                      \tag{18}
\]

This estimate includes the full, possibly distant action vertex and
every relative boundary row. It is the required uniform error before
any finite-range or mesh limit, not an entrywise approximation followed
by an uncontrolled sum.

### 4. The weighted bulk row sum with the exact Wilson vertex

For fixed m, the operator in (16) has finite range and exact bulk
agreement by the same path construction as L288 section 3. First
compute its bulk row sum with h=1 on all 12-plaquettes. Only this
auxiliary computation uses odd periodic tori; the relative-box
covariances in (15)–(18) are unchanged.

For a constant external color field u, L289(4)–(5)'s raw-slot
differentiation gives on one 12-plaquette

\[
 (Cx)_{12}\cdot([u_1,\operatorname{av}_1x_2]
                       -[u_2,\operatorname{av}_2x_1]).     \tag{19}
\]

Use midpoint Fourier coordinates d_mu=2 sin(q_mu/2),
c_mu=cos(q_mu/2), lambda=|d|^2, P=I-dd^T/lambda and
gamma_m=lambda h_m(lambda)^2. For one fixed external unit color A,
the symmetrized quadratic matrix of (19) is -i H_{12,u} tensor J_A,
where Tr J_A^2=-2 and

\[
 \begin{split}
 H_{12,u}&=u_1c_1 A_{1,12}+u_2c_2 A_{2,12},\\
 A_{1,12}&=d_1e_2e_2^T-\tfrac{d_2}{2}(e_1e_2^T+e_2e_1^T),\\
 A_{2,12}&=d_2e_1e_1^T-\tfrac{d_1}{2}(e_2e_1^T+e_1e_2^T).
 \end{split}                                                   \tag{20}
\]

This follows by symmetrizing each of the two terms in (19), just as
L289(6) symmetrizes their sum over orientations. The cosine factors
are the actual endpoint averages, so no raw-edge phase is omitted.
For the complete action and constant v, its matrix H_v from L289
satisfies PH_vP=s_vP, s_v=sum_mu v_mu sin q_mu. Direct calculation
also gives

\[
 \operatorname{Tr}(A_{1,12}P)=d_1P_{22}-d_2P_{12}=d_1,
 \quad \operatorname{Tr}(A_{2,12}P)=d_2,
 \quad \operatorname{Tr}(H_{12,u}P)=u_1\sin q_1+u_2\sin q_2.
                                                               \tag{21}
\]

The real Gaussian cross-covariance formula is 2 Tr(K_1 Gamma K_2
Gamma), and (14) multiplies it by a further two. With Gamma=gamma_m P
tensor I_3 and (-i)^2 Tr J_A^2=2, the complete row-sum bilinear form is

\[
 8\int\gamma_m(q)^2
       (u_1\sin q_1+u_2\sin q_2)
       \left(\sum_\mu v_\mu\sin q_\mu\right)\frac{dq}{(2\pi)^4}.
                                                               \tag{22}
\]

Finite range identifies this torus expression per unit volume with
the full infinite-lattice row sum once the torus exceeds its path
range; then Fourier sums converge to the displayed integral. Oddness
eliminates cross directions, and coordinate interchange equates the
two diagonal entries. The scalar color-block row sum is therefore

\[
 R_{12,m}=\beta_m\Pi_{12},\qquad
 \beta_m=8\int\sin^2q_1\,\lambda(q)^2h_m(\lambda(q))^4
                    \frac{dq}{(2\pi)^4}\longrightarrow8I_1. \tag{23}
\]

The convergence is precisely the dominated-convergence step in
L289(9)–(10), with factor 8 instead of 24. Summing (23) over all
six orientations gives three such contributions per direction,
recovering L289's 24I_1 normalization. This is a consistency check,
not a substitute for (20)–(22) or a separate critical audit.

### 5. Fixed-range source limit and assembly

Fix m. Every active first vertex is in the compact insertion support;
all paths in the finite-range operator then stay away from all boundary
faces for sufficiently large N. Its second vertex is within a fixed
lattice distance. Thus every nonzero coefficient is exactly a bulk
coefficient with its actual first-vertex weight h_p. All other rows
are zero, not silently removed. This use of compact support applies
only after the whole-box estimate (18).

Write V_a(x,y)=(R_{a,mu}(x,y))_mu from L284(7)–(12), with components
3 and 4 zero. On E_- times the opposite support this field and its
first derivatives are uniformly bounded, and V_a converges uniformly
to the continuum kernel V. For fixed m the row range, number of
entries and absolute row sums of E_{h,m}^int are bounded independently
of N. Freeze h_p at the external row center x_i and the neighboring
components of V_a at that same point. Their errors are O_{m,f}(a),
uniformly in i and opposite-source y. Smoothness of h also controls
rows adjacent to the edge of its support. Equation (23) yields

\[
 (E_{h,m}^{\rm int}V_a(\cdot,y))_i
       =\beta_m h(x_i)(\Pi_{12}V_a(x_i,y))_{\mu_i}
                         +O_{m,f}(a)                       \tag{24}
\]

on a fixed compact neighborhood containing every active row. Both
sides vanish outside that neighborhood for large N. The matrix in
(24) is its scalar color block; the internal color sums are already
included in beta_m.

The exact all-color trace normalization, with R_N=a^3R_a, is

\[
 \begin{split}
 N^{-2}\operatorname{Tr}(E_{h,m}^{\rm int}G_+)
 =\frac3{64}a^8\sum_{i,p}h_+(z_p)R_{a,\mu_i}(x_i,z_p)
                         (E_{h,m}^{\rm int}V_a(\cdot,z_p))_i.
 \end{split}                                                   \tag{25}
\]

The factor three counts only external colors. The factor 1/64 is
1/(a^2N^2); the original trace has no extra a^4 plaquette weight.
Physical row and source volumes are uniformly bounded. Therefore
the summed O_m(a) error in (24) tends to zero in (25). Uniform
kernel convergence and product Riemann sums on the actual edge and
plaquette grids give, for every fixed m,

\[
 \lim N^{-2}\operatorname{Tr}(E_{-,m}^{\rm int}G_+)
                         =\frac{3\beta_m}{64}\mathcal J_f. \tag{26}
\]

First take N to infinity at fixed m, using (15) and (18), and then
let m increase using (23). This gives the complete limit
N^-2 Tr(E_-G_+) -> (3/64)(8I_1)J_f. Its original -1/2 prefactor
proves the first equality of (2). Reversing the source supports gives
the same estimates. Time reflection preserves directions 1,2 and
12 orientation, and the kernel identity in L284 section 3 identifies
the reversed integral with the same J_f. This proves the second
equality without presuming termwise nonlinear gauge independence.

Finally L286(1) makes I_{3,N}/N^2 tend to zero. L289(3) gives the
subtotal of M_{3,N}, the complete quartic and the complete density
as Z_0 J_f/64. Adding the two limits (2) gives
(Z_0-24I_1)J_f/64. The already justified identity L289(16),
I_1=Z_0/2-1/16, gives (3). L280(20) has exactly one further cubic
group, D_{3,N}, proving (4) without estimating or cancelling it.

### 6. Separate critical audit (2026-10-26)

This audit accepts (2)–(4), conditional on the exact imported relative
kernels, source hypotheses and preceding audited estimates. In
particular it checks the nonsymmetric weighted operator and its
entire action domain; an unweighted positive bound would not suffice.

Each separated spatial mode in (8) is rank one on the rectangular
edge/source sets. The supremum of its product factors equals the
product of the two suprema. The exponential mode majorant therefore
bounds its nuclear norm by C_f a^3 N^4 exp(-|k|/8), which is
O_f(N exp(-|k|/8)). Summing all allowed modes proves the first
bound (6); multiplication by ||U||=O_f(N) proves the second.
The estimate for diag(h_-) C_- U is the different, O_f(1)
separated-curvature nuclear bound (10). Neither statement follows
by multiplying a pointwise bound by the rank of the matrix.

The maps B_h and B have bounded norms, and B_h=B_h chi. Combining
these with the two distinct nuclear estimates gives all four norms
in (13). Applying the finite-rank trace inequality with the local
factor in nuclear norm gives AA=O_f(ell_N) and AB,BA each
O_f(N sqrt(ell_N)). The derivative factors 1/2 and the two crossing
pairings identify E_h exactly, so the original coefficient remains
-Tr(E_h G_+)/2. No covariance or action vertex is omitted in this
removal of external curls.

In the independent splitting of section 3, insertion weights only
multiply each coefficient vector by a bounded h_p. The residual
conditional means remain zero, including the two-color z,z term.
Thus the cross-matrix difference is exactly 2 E[Z_h(u)Z(v)],
whose operator norm is O_f((m+1)^-1). Positivity or symmetry is
unnecessary. Its rows are supported in chi, so D=chi D and
Tr(D G_+)=Tr(D G_+ chi). The second estimate (6) consequently
proves (18) on the full box, before finite range is used.

The two restricted spatial matrices in (20) have traces
Tr(A_(1,12) P)=d_1 and Tr(A_(2,12) P)=d_2: the terms
d_1 d_2^2/lambda, respectively d_2 d_1^2/lambda, cancel.
Together with PH_vP=(sum v_mu sin q_mu)P, this yields (22).
The Gaussian and color factors are four times two, giving 8,
not the full-action value 24. Oddness removes cross directions,
and the same integrable majorant as in L289 gives beta_m -> 8 I_1.
Summing the six orientation restrictions returns three copies per
direction, in agreement with the independently checked full action.

For fixed m, every path from an active first vertex remains inside
the box for small enough a. Its second action vertex may be
arbitrary in the original expression; finite range, used only after
(18), now bounds its distance. Smooth weight freezing is valid also
at the edge of the insertion support because h is a globally smooth
bump. L284's uniform separated kernel and derivative bounds give
the O_(m,f)(a) error in (24) on every active row. In (25),
N^-2 a^6=a^8/64, and the remaining factor three counts external
colors only. The product grids have bounded physical volume, so
the complete summed error vanishes and the product Riemann sum is
J_f. Letting N increase at fixed m and then m increase uses the
uniform estimate (18), rather than interchanging unchecked limits.

Consequently each trace limit is (3/64)(8 I_1) J_f; its original
-1/2 gives -3 I_1 J_f/16. Reflection preserves 12 orientation
and gives the same second limit. Adding both to L289's subtotal
and L286's zero normalized insertion pair leaves
(Z_0-24 I_1)J_f/64=(3-22 Z_0)J_f/128. L280's exact five-group
decomposition then gives (4). This accepts no estimate for the
distinct-line term within this lemma and no subleading or higher
remainder. All continuum and mass-gap qualifications remain.

## Mathlib

Coverage of the full Wilson-specific relative-box result is not
checked; no matching theorem or absence claim is made. Exact relative
modes and their time factor are reused from L003/L284; the separated
curvature trace bound from L281; the cubic jet and Gaussian factors
from L286/L287; the positive covariance approximation and its residual
bounds from L288; and the full-action Fourier computation and scalar
integral comparison from L289. The additional work is the weighted
two-vertex specialization and its complete summation. Finite-rank
singular-value inequalities and Gaussian pairings are used explicitly
to verify that specialization. No new external kernel theorem,
renormalization input or nonlinear forest transport is invoked.
