# L215 — A uniform scalar-prefix plateau replacement below cubic scale

## Hypotheses

Keep L025, L213 and L214's pinned relative SU(2) cube, admitted even
meshes a=8/N, straight lower-rooted direction-1 forest, and both actual
L010 probes i=3,6 at tau=1/16. The bare expansion precedes refinement.
All matrices and transposes below use ordinary stored dimensionless
link coordinates. Retain all colors, transverse planes, normal end
edges, upper-adjacent levels, both residual subtractions and heat modes.

Use L026's full Hodge covariance and L065's scalar block:

\[
 H=\Delta_3,\quad G=H^{-1},\quad L_E=D_vD_v^T,\quad
 \Sigma_1=(L_E\otimes I+I_N\otimes H)^{-1},\quad
 H_T=I_N\otimes H,\quad A_{11}=I_1^T A I_1.
 \tag{1}
\]

Here H is the three-dimensional pinned vertex Laplacian, D_v maps
the N-1 pinned axial vertex values to all N axial edges, and L_E has
its normalized constant mode. In particular the last axial edge is
present in (1). L065 gives a constant C_A independent of N such that

\[
 A_{11}=H_T^{1/2}F_NH_T^{1/2},\qquad F_N=F_N^T,
 \quad\|F_N\|\le C_A.
 \tag{2}
\]

For a positive variable transverse edge e of direction mu=2,3,4 at
axial vertex level 1<=j_e<N, define q_e on the transverse interior
vertices to be delta_(v+e_mu)-delta_v, omitting a delta at a pinned
endpoint. Let b_j on the N axial edge levels be the indicator of
0,...,j-1. The forest row in L214(5) is the direct transverse row
minus w_e^T I_1^T, where

\[
 w_e=b_{j_e}\otimes q_e,\qquad
 f_e=\Sigma_1 w_e,\qquad
 g_e=b_{j_e}\otimes Gq_e.
 \tag{3}
\]

The replacement g_e is a sharp lower-prefix plateau with its actual
moving cut; it is not a smooth extension through an axial pin.

## Conclusion

Uniformly over these edges, including normal transverse end edges,

\[
 \|H_T^{1/2}(f_e-g_e)\|^2\le6,\qquad
 \|H_T^{1/2}f_e\|^2\le j_e,\quad
 \|H_T^{1/2}g_e\|^2\le j_e.
 \tag{4}
\]

Consequently, for every such e,f, the actual two-prefix scalar block
of L214(9) admits the uniform signed comparison

\[
 \left|w_e^T\Sigma_1 A_{11}\Sigma_1w_f-g_e^TA_{11}g_f\right|
 \le \sqrt6 C_A(\sqrt{j_e}+\sqrt{j_f})\le2\sqrt6 C_A\sqrt N.
 \tag{5}
\]

Define \(\widetilde T_i^{(0)}\) from L213(2)'s entire transverse
24-pair class by replacing only this two-prefix block in each local
V_p by g_e^T A_11 g_f. Keep the direct/direct and both mixed blocks
exactly as in L214(4)–(9), with their original minus signs, and keep
the original tensor K, U_(i,p), colors and traversal signs. Then

\[
 |T_i^{(0)}-\widetilde T_i^{(0)}|
 +|G_i^{\rm nr}-\widetilde T_i^{(0)}|
 \le C_i a^{-5/2},\qquad i=3,6.
 \tag{6}
\]

Thus their differences vanish after multiplication by a^3. The
complete nonradial action response has a finite a^3-scaled limit
exactly when this partially replaced, still complete transverse
contraction does, with the same value. No limit for that contraction
or its individual blocks is established. This is a specialization
of spectral-energy methods within the approved complete-response
target, with no certified originality claim. Full compensation, finer
asymptotics, finite matching, reflected error <=c_box/2, continuum
axioms and infrared finite positive mass remain unresolved.

## Proof

### 1. Keep the endpoints in the transverse dipole estimate

For 1<=k_r<N the normalized transverse sine waves are

\[
 \varphi_k(v)=(2/N)^{3/2}\prod_{r=2}^4
          \sin(\pi k_r v_r/N),\qquad
 \lambda_k=\sum_{r=2}^4\alpha_{k_r},\quad
 \alpha_m=4\sin^2(\pi m/(2N)).
 \tag{7}
\]

Extend these waves by their exact zero values to the pinned
endpoints. Taking their difference across e in direction mu gives

\[
 |q_e^T\varphi_k|^2\le (8/N^3)\alpha_{k_\mu}
                       \le(8/N^3)\lambda_k.
 \tag{8}
\]

Indeed the mu sine difference is
2 sin(pi k_mu/(2N)) cos(pi k_mu(v_mu+1/2)/N); the other sine
factors have magnitude at most one. This identity also holds for
v_mu=0 and v_mu=N-1, where one endpoint value is zero. No interior
dipole estimate has been extended to a boundary delta by assumption.

Since lambda_k>=4|k|^2/N^2, (8) yields

\[
 \begin{split}
 \|Gq_e\|^2
 &=\sum_k |q_e^T\varphi_k|^2/\lambda_k^2
 \le {8\over N^3}\sum_k\lambda_k^{-1}
 \le {2\over N}\sum_{k\in\{1,\ldots,N-1\}^3}|k|^{-2}
 \le6{N-1\over N}\le6.
 \end{split}
 \tag{9}
\]

For the last inequality, the shell max(k_r)=m contains
m^3-(m-1)^3<=3m^2 indices, each with |k|^2>=m^2. This proves
the bound using every transverse mode, including the smallest ones.
Also, with D_mu the pinned transverse vertex-to-edge difference,
q_e=D_mu^T delta_e and D_mu^T D_mu<=H. Hence

\[
 q_e^TGq_e\le1.
 \tag{10}
\]

This is the norm bound for D_mu H^(-1/2), and includes the normal
end edges in D_mu. It is a positive statement about H, not A_11.

### 2. Compare the full axial resolvent with the sharp plateau

The pinned axial incidence gives exactly

\[
 \|b_j\|^2=j,\qquad
 b_j^T L_E b_j=\|D_v^Tb_j\|^2=1,
                    \quad 1\le j<N.
 \tag{11}
\]

In fact (D_v^T b_j)_s=b_j(s-1)-b_j(s) is one at the single
interior vertex s=j and zero at all other interior vertices. This
keeps both axial end edges. There is no artificial lower jump term,
because the lower endpoint is pinned in the vertex domain; at j=N-1
the moving cut is still the interior vertex N-1.

Diagonalize L_E and H in their full orthonormal bases, writing
alpha>=0 and lambda>0 for the two eigenvalues. In a joint mode,
f_e and g_e have respective multipliers 1/(alpha+lambda) and
1/lambda on b_j tensor q_e. Therefore the squared H_T error is

\[
 \sum_{\alpha,k}|\widehat b_j(\alpha)|^2
 |q_e^T\varphi_k|^2
 {\alpha^2\over\lambda_k(\alpha+\lambda_k)^2}
 \le
 \left(\sum_\alpha\alpha|\widehat b_j(\alpha)|^2\right)
 \left(\sum_k {|q_e^T\varphi_k|^2\over\lambda_k^2}\right)
 \le6.
 \tag{12}
\]

The scalar inequality used here is
alpha^2/(alpha+lambda)^2<=alpha/lambda for alpha>=0,
lambda>0, which follows from alpha lambda<=(alpha+lambda)^2.
Equations (9) and (11) then give the last bound. The constant axial
mode has alpha=0 and contributes zero to the error, rather than
being omitted from f_e or g_e. This estimate is uniform also for
j near either end, without a physical-frequency cutoff or mass.

Finally Sigma_1 H_T Sigma_1<=Sigma_1<=I_N tensor G by the same
commuting positive spectral calculus. Thus

\[
 \|H_T^{1/2}f_e\|^2
 \le w_e^T\Sigma_1w_e
 \le j_e q_e^TGq_e\le j_e,
 \quad
 \|H_T^{1/2}g_e\|^2=j_e q_e^TGq_e\le j_e.
 \tag{13}
\]

This proves (4). Neither an unweighted norm bound on f_e-g_e nor
smoothness of either long prefix is needed or asserted.

### 3. Use only the actual scalar residual form

Write the difference in (5) as

\[
 (f_e-g_e)^T A_{11}f_f+g_e^T A_{11}(f_f-g_f).
 \tag{14}
\]

Apply (2) and Cauchy–Schwarz separately to these two terms. The
three bounds in (4) give exactly (5). Both generator orientations
and the two insertion subtractions enter through the unchanged
actual A_11 in (2). It need not be positive. No scalar bound is
assigned to a mixed component block. In particular this comparison
does not remove or approximate L214's two direct/prefix terms.

### 4. Sum the actual transverse action contraction

The exact row expansion of the lifted residual in L214 is

\[
 \begin{split}
 (R\Sigma A\Sigma R^T)_{ef}
 ={}&d_e^T\mathscr Vd_f-d_e^T\mathscr V I_1w_f
       -w_e^TI_1^T\mathscr Vd_f
       +f_e^TA_{11}f_f,\\
 &\mathscr V=\Sigma A\Sigma.
 \end{split}
 \tag{15}
\]

Only its last term changes in the defined replacement. This term
has a plus sign because both forest rows have a minus prefix. V
contains no Gaussian-tilt factor 2. The other three terms in (15)
and the local quartic tensor remain exactly those of L025.

L213(11)–(13) and L214(13) give |(U_(i,p))_(alpha beta)|<=C_i a^2
uniformly on all transverse plaquettes. Their full double heat sum
already bounds all mode polynomials uniformly. Equation (5) bounds
every changed one-color V entry by C sqrt(N). Colors are diagonal,
traversal signs have magnitude one, and fixed traversal entries
have zero rows. K is a fixed finite-dimensional tensor. Therefore

\[
 \sum_{p\in P_T}
 |24K:U_{i,p}:(V_p-\widetilde V_p)|
 \le C_i N^4 a^2\sqrt N
 =O_i(a^{-5/2}).
 \tag{16}
\]

This is a uniform summed error, including all planes 23,24,34 and
every transverse boundary strip, not just a pointwise plateau
preview. The factor 24 is retained once. Apply L213(3)'s complete
O(a^-5/2) comparison between G_i^nr and T_i^(0) and the triangle
inequality to obtain (6). Multiplication by a^3 proves the claimed
equivalence of limit questions; it does not prove either limit.

### 5. Scope, overlap and meaningful checks

The unchanged ready EXPLORE assessment
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`
covers the exact complete L025 target and its intermediate reductions.
Its inspected primary results do not supply this bare forest limit.
The proof above specializes the existing full relative spectrum and
L065's scalar energy form; no general source theorem is reproved.

The duplicate comparison inspected L177 proof section 1's rectangular
prefix resolvent identity and L097 proof section 3's full-curvature
static comparison. The former retains the constant mode and bounds
a different matrix energy square; the latter uses a low-spectrum
split for a different curvature/prefix sandwich. Neither supplies
(5) or (16) for this actual local action contraction. The present
endpoint-dipole calculation supplies the needed uniform row estimate
directly. These comparisons motivate the standard method and are
not additional premises of (4)–(16).

The analytic checks are the complete endpoint sine difference (8),
the three-dimensional shell bound (9), the exact one-cut axial
energy (11), inclusion of alpha=0 in (12), the original residual
order and signs in (14)–(15), and the complete plaquette/heat count
(16). No numerical extrapolation, mathematical script or IEEE sign
premise is required. Upstream analytic lemmas remain imported.

The earlier failures of bounded raw forest covariance and smooth
extension across the upper pin are preserved: g_e still has O(sqrt N)
energy and a sharp moving cut. A scalar plateau replacement is not
a limit for its quadratic form, and says nothing about cancellation
with the direct and mixed terms. Those signed asymptotics remain
part of the same unresolved complete-response question.

## Mathlib

Full coverage of this specialized forest-action replacement: **not
checked**. Supporting finite spectral calculus, tensor-product modes,
incidence energy, Cauchy–Schwarz and finite Riemann-sum prerequisites:
**not checked**. Unknown availability does not mean absence. No
matching Mathlib theorem or claim of mathematical novelty is made.
