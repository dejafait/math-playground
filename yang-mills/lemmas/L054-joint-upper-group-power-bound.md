# L054 — A power bound for the joint upper-face action group

## Hypotheses

Keep L049–L053's actual SU(2) forest law, both probes i=3,6,
tau=1/16, a=8/N, and every upper transverse edge, including end
edges. Take the small-coupling coefficient at fixed mesh first.
Use L051's one-color forest matrices S,B,A,J and C,U,V,W. Constants
may depend on the specified displacement, probe, box and flow time,
but not on sufficiently fine admitted meshes.

Write T for the transverse pinned incidence, G=(T^T T)^(-1),
P=TGT^T, and T_d for the forest-coordinate map to the full upper
curvature d of L049. Thus T_d is different from T and from T_eta.
Define

\[
K_d=T_dST_d^T,\quad H_0=T_dSJ^T=TG,\quad
D_0=I-K_d=b_N(\Delta_T)(I-P).                    \tag{1}
\]

In particular 0<=D_0<=I and D_0 T=0. These are L049–L050's
identities on the complete edge space. Boundary vertex rows are zero.

## Conclusion

Let G_i be precisely L051's selected nonradial upper quartic plus
upper/upper cubic-pair group. Then

\[
 |G_i|\le C_i a^{-2}.                              \tag{2}
\]

Equivalently L053's four remaining signed sums satisfy

\[
 |-6\Phi_D(U,V)+E_B+E_A+E_\times|\le C_i a^{-2},
 \qquad D=I-K=D_0+P/N.                            \tag{3}
\]

This bounds a^2 times this whole selected group; it establishes
neither convergence nor its coefficient or sign. In particular it
does not settle compensation of L047's selected negative coefficient.
It excludes stronger powers only in this group. Other cubic pairs,
measure, insertion and flow jets, subleading powers, the full cutoff
logarithm, finite matching and the interacting reflected error
<=c_box/2 remain open. There is no continuum construction or mass-gap
claim.

## Proof

### 1. Retain the nonzero curvature–potential covariance

L049 proves the polynomial identity
S3_top=sum_e d_e dot (u(v) cross u(v'))/2: replacing d by eta is
optional, since (T u)_e dot (u(v) cross u(v'))=0 separately on each
edge. We use d. Under the normalized quadratic tilt by exp(sf+tr),
put

\[
S(s,t)=(S^{-1}-2sB-2tA)^{-1},\quad
C(s,t)=JS(s,t)J^T,\quad K(s,t)=T_dS(s,t)T_d^T,
\quad H(s,t)=T_dS(s,t)J^T.                         \tag{4}
\]

The finite Gaussian tilt and Isserlis' theorem are used in exactly
L051–L052's conventions. Positive definiteness near zero justifies
all polynomial differentiations at each fixed mesh. Importing those
identities does not require a new continuum or boundary theorem.
Here H(0,0)=H_0 is NONZERO and must be retained.

For symmetric vertex matrices M, define the trilinear expression

\[
\begin{split}
\Omega(H,L;M)=\sum_{e=(v,v'),h=(w,w')}[&
-H_{ew}L_{hv}M_{v'w'}+H_{ew}L_{hv'}M_{vw'}\\
&+H_{ew'}L_{hv}M_{v'w}-H_{ew'}L_{hv'}M_{vw}].       \tag{5}
\end{split}
\]

Interchanging the ordered edges shows Omega(H,L;M)=Omega(L,H;M).
Use delta(C) and delta(C,M) from L052. The same six cross-vertex
Isserlis pairings used in L052(8), now without setting H(0,0)=0,
give the exact identity

\[
\begin{split}
F(s,t)&=E_{s,t}[S3_{\rm top}^2/2-q_A]\\
&=\tfrac34\left[-\Phi_{D_0}(C(s,t),C(s,t))
 +\sum_{e,h}(K(s,t)-K_d)_{eh}\delta_{eh}(C(s,t))
 +\Omega(H(s,t),H(s,t);C(s,t))\right].             \tag{6}
\end{split}
\]

Indeed the determinant's first term is K_eh delta_eh(C), and its
other four terms are (5). The expectation of q_A is
3 sum_e delta_ee(C)/4. Thus (6) has the correct quartic subtraction,
including its color factor. No conditional-independence assertion
under the tilt is used.

Define the d versions of the derivative blocks

\[
\begin{gathered}
K_B^d=T_dSBST_d^T,\quad K_A^d=T_dSAST_d^T,\\
K_{BA}^d=T_d(SBSAS+SASBS)T_d^T,\\
H_B^d=T_dSBSJ^T,\quad H_A^d=T_dSASJ^T,
\quad Y=T_d(SBSAS+SASBS)J^T,\quad W_+=W+W^T.
\end{gathered}                                    \tag{7}
\]

Their factors in derivatives are C_s=2U, C_t=2V, C_st=4W_+,
K_s=2K_B^d, K_t=2K_A^d, K_st=4K_BA^d,
H_s=2H_B^d, H_t=2H_A^d and H_st=4Y. Differentiating (6) therefore
gives exactly

\[
\begin{split}
F_{st}(0,0)={}&-6\Phi_{D_0}(C,W_+)-6\Phi_{D_0}(U,V)\\
&+3\sum_{e,h}[ (K_{BA}^d)_{eh}\delta_{eh}(C)
 +(K_B^d)_{eh}\delta_{eh}(C,V)
 +(K_A^d)_{eh}\delta_{eh}(C,U)]\\
&+3[2\Omega(Y,H_0;C)+2\Omega(H_B^d,H_A^d;C)
 +2\Omega(H_B^d,H_0;V)\\
&\hspace{14mm}+2\Omega(H_A^d,H_0;U)
 +\Omega(H_0,H_0;W_+)].                           \tag{8}
\end{split}
\]

This formula displays every derivative of the nonzero base H_0.
By Gaussian parity and L049(15), the desired group is

\[
G_i=F_{st}(0,0)-\kappa(f,r,R).                    \tag{9}
\]

L051 bounds the last term by O(a^-1). We bound (8) without assigning
a small smooth-column estimate to the entire block V.

### 2. Full-spectrum bounds for the rough blocks

L040's axial-zero compression and L041(13) give, as full vertex
matrices,

\[
C=NG,\qquad V=NG\bar A G,\qquad
-cG^{-1}\le\bar A\le cG^{-1},\qquad -cC\le V\le cC.
                                                               \tag{10}
\]

The compression applies to every pair of vertex evaluation rows:
their lifted covariance columns are sqrt(N) E_0 G delta_v. It is
therefore not merely a same-edge identity. Put
R=G^(1/2) bar A G^(1/2); then R is symmetric and ||R||<=c.
The diagonal bound and complete spectrum in L029/L052 yield

\[
\operatorname{Tr}G=O(N^3),\quad
\operatorname{Tr}G^2=O(N^4),\quad
\|C\|_{HS}+\|V\|_{HS}=O(N^3).                    \tag{11}
\]

For the V estimate, in a G eigenbasis with eigenvalues g_j>0,
sum_jk g_j g_k |R_jk|^2 <= sum_j g_j^2 sum_k |R_jk|^2
<=c^2 sum_j g_j^2; the first inequality uses 2g_jg_k<=g_j^2+g_k^2
and symmetry. Multiplication by N^2 proves the squared bound.
The exact identities T^T T=G^-1 and P=TGT^T imply further

\[
\begin{gathered}
\|H_0\|_{HS}=O(N^{3/2}),\quad
\|H_0T^T\|_{HS}=\|P\|_{HS}=O(N^{3/2}),\\
\|TV\|_{HS}+\|VT^T\|_{HS}=O(N^{5/2}),\quad
\|TVT^T\|_{HS}=O(N^{5/2}).                        \tag{12}
\end{gathered}
\]

For example ||TV||_HS^2=N^2 Tr(G R^2)<=c^2 N^2 Tr G.
Also TG^(1/2) is an isometry on the m=(N-1)^3 vertex space, so
||TVT^T||_HS=N||R||_HS<=c N sqrt(m). The H_0 assertions follow
from ||TG||_HS^2=Tr G and rank(P)=m. No mode cutoff is used.

L028–L029's heat-expanded ordinary upper potential columns h_k obey
||h_k||_infinity<=p(k) and ||T h_k||_infinity<=a p(k).
Their residual columns j_k obey the corresponding bounds
a^2p(k), a^3p(k). The full double heat sum with coefficients
(B_i,a)_kl is uniformly absolutely summable with these polynomial
weights. In particular

\[
\|U\|_{HS}=O(N^3),\qquad \|W_+\|_{\max}=O(a^2).
                                                               \tag{13}
\]

Here U=sum_kl exp(-tau(lambda_k+lambda_l)) (B_i,a)_kl h_k h_l^T;
this is the ordinary exterior expansion obtained from L028(13)
with its residual factor omitted. It follows directly from the
same lifted covariance/probe product JSBSJ^T. W has the expansion
with h_k j_l^T from L053. Each assertion retains all modes.

### 3. Bound the two D_0 contractions

For a pinned deterministic vertex field h and a mean-zero field xi
of covariance C, keep L053's B_h xi and endpoint average M xi.
The exact identity B_h xi=-T(h xi)+2(T h)M xi, together with
D_0 T=0 and 0<=D_0<=I, gives

\[
Q_0(h):=E\|D_0^{1/2}B_h\xi\|^2
 \le4\|Th\|_\infty^2 E\|M\xi\|^2
 \le C N^4\|Th\|_\infty^2.                       \tag{14}
\]

The last step is L053's complete covariance trace estimate, including
end edges. Consequently Q_0(h_k)<=C N^4 a^2 p(k)^2 and
Q_0(j_l)<=C N^4 a^6 p(l)^2. The rank-two contraction identity in
L053 and Cauchy–Schwarz, followed by the full heat sums, give

\[
 |\Phi_{D_0}(C,W_+)|=O(N^4 a^4)=O(1).             \tag{15}
\]

For the other term use (10), not a smooth residual column. The same
rank-two identity is linear in its covariance argument. Writing
V=C^(1/2) R C^(1/2) with ||R||<=c gives

\[
|\Phi_{D_0}(V,hk^T+kh^T)|
 \le c\sqrt{Q_0(h)Q_0(k)}.                       \tag{16}
\]

One direct justification is Hilbert–Schmidt Cauchy–Schwarz applied
to D_0^(1/2) B_h C^(1/2), R, and the transpose of the corresponding
k matrix. This uses no positivity of V. Expand the symmetric U in
its absolutely heat-weighted rank-two terms using (13). Equations
(14) and (16) imply

\[
 |\Phi_{D_0}(U,V)|=O(N^4 a^2)=O(a^{-2}).           \tag{17}
\]

### 4. Control the d derivative blocks uniformly over distinct rows

L029's ordinary exterior columns have d entries O(a^2 p(k));
residual columns have d entries O(a^4 p(k)). Its upper potential
entries and differences are those used in (13). Thus, by the same
full heat sums,

\[
\|K_B^d\|_{\max}=O(a^4),\quad
\|K_{BA}^d\|_{\max}=O(a^6),\quad
\|H_B^d\|_{\max}=O(a^2),\quad \|Y\|_{\max}=O(a^4),
\quad \|H_B^d T^T\|_{\max}=O(a^3).                \tag{18}
\]

For the two blocks without external heat factors use L041's separated
source proof. In full Hodge coordinates x_d=Sigma r_d obeys
||A_0 x_d||_2<=C a^5, uniformly over all top edges. It also gives
||x_d||_2<=C/a. A potential column x_v=sqrt(N)E_0G delta_v has
||x_v||_2<=C/a by its complete transverse spectrum. Gauge invariance
of the quadratic forms, with the explicit linear forest lift in
L018, therefore yields for arbitrary edges e,h and vertices v

\[
|(K_A^d)_{eh}|=|x_{d,e}^T A_0 x_{d,h}|\le C a^4,
\qquad |(H_A^d)_{ev}|=|x_{d,e}^T A_0 x_v|\le C a^4.
                                                               \tag{19}
\]

The original proof of ||A_0 x_d||_2 is uniform in source location;
it only uses separation from the fixed interior coefficient support.
Using a different second row does not alter that hypothesis. This
does not assert a small norm for A_0 on rough arbitrary inputs.

Each vertex occurs in at most six retained edges. Hence every
endpoint pullback of a vertex or edge–vertex matrix to an edge-pair
array has HS norm bounded by a fixed multiple of its original norm.
Applying Cauchy–Schwarz to the four endpoint products in delta(C,M)
gives

\[
\sum_{e,h}|\delta_{eh}(C,M)|\le C\|C\|_{HS}\|M\|_{HS}.
                                                               \tag{20}
\]

The analogous assertion holds for delta(C) with ||C||_HS^2.
By (11), (13), (18) and (19), the three K sums in (8) have bounds
O(1), O(a^-2), O(a^-2), respectively.

### 5. Retain the mixed terms with H_0

For four of the five Omega types in (8), direct HS estimates suffice.
For example sum_eh |(H_0)_hv C_v'w'|<=C||H_0||_HS||C||_HS,
while sum_eh |(H_0)_ew(H_0)_hv|<=C||H_0||_HS^2.
For an endpoint pullback of C alone, its l1 norm is at most
C N^3||C||_HS. Apply these observations to the four terms of (5):

| Type | Bound |
| --- | --- |
| Omega(Y,H_0;C) | O(a^4 N^(9/2)) = O(N^(1/2)) |
| Omega(H_B^d,H_A^d;C) | O(a^6 N^6) = O(1) |
| Omega(H_A^d,H_0;U) | O(a^4 N^(9/2)) = O(N^(1/2)) |
| Omega(H_0,H_0;W_+) | O(a^2 N^3) = O(N) |

The remaining term Omega(H_B^d,H_0;V) cannot use the crude
entrywise estimate: that would give O(N^(5/2)). Keep its alternating
endpoint structure instead. For each ordered pair e=(v,v'),h=(w,w'),
write b=(H_B^d)_ew, db=(H_B^d)_ew'-(H_B^d)_ew,
l=(H_0)_hv, dl=(H_0)_hv'-(H_0)_hv. Its summand is exactly

\[
\begin{split}
&-b l\,[V_{v'w'}-V_{vw'}-V_{v'w}+V_{vw}]\\
&\quad+b\,dl\,[V_{vw'}-V_{vw}]
       +db\,l\,[V_{v'w}-V_{vw}]-db\,dl\,V_{vw}.   \tag{21}
\end{split}
\]

Expanding (21) recovers all four terms of (5), with their signs.
The mixed difference is the edge-pair matrix TVT^T, the single
differences are endpoint pullbacks of VT^T and TV, and dl is
-(H_0T^T)_he=-P_he. By (18), |b|<=C a^2 and |db|<=C a^3.
Using (11)–(12) and the bounded endpoint multiplicities gives the
following bounds for the four complete sums in (21):

\[
 C a^2 N^{3/2}N^{5/2},\quad
 C a^2 N^{3/2}N^{5/2},\quad
 C a^3 N^{3/2}N^{5/2},\quad
 C a^3 N^{3/2}N^3.                                \tag{22}
\]

They are respectively O(N^2), O(N^2), O(N), O(N^(3/2)); all are
O(a^-2). This is the only additional difference estimate needed.
The rough V is controlled by its full relative-form bound throughout.
The endpoint identities apply unchanged when a vertex is pinned;
T and P retain every end edge.

### 6. Assembly, verification and scope

Equations (15), (17), (20) and (22) bound every term in the exact
identity (8) by O(a^-2). Combining with (9) and L051 proves (2).
L053(3), including its O(a^-1) remainder, then proves (3). The new
argument does not assert separate bounds for the four eta-based
sums: the curvature regrouping is essential to the proof given.

The determinant expansion (6), the nine product-rule contributions
in (8), the complete spectral traces (11)–(12), and the four-term
identity (21) are analytic checks for arbitrary admitted meshes.
No numerical approximation or finite-mesh diagnostic is used as
evidence for the asymptotic bound. In particular no diagnostic sign
has been converted into a limit. This is a local reproduction of
finite Gaussian contraction and matrix estimates, with applicability
to the actual boundary rows justified above. The unchanged SPECIALIZE
assessment `drafts/literature/2026-09-26-current-target.md` covers the
same probes, regulator and response. General renormalization theorems
are not reproved or assigned additional physical-boundary hypotheses.

The next scale question remains the signed a^2 limit of this group.
The present O(a^-2) bound permits a nonzero coefficient and therefore
does not prove cancellation or reduce the group to logarithmic order.
All O(a^-1) terms in L051–L053 must be restored for a logarithm.

## Mathlib

Coverage of this complete specialized bound: **not checked**.
Supporting finite Gaussian tilting, Isserlis' theorem, matrix
Cauchy–Schwarz and finite spectral calculus: **not checked**.
No matching Mathlib theorem is asserted. The local mathematical
inputs are L018, L028–L029, L040–L041 and L049–L053, with the
specific uses proved above. Unknown coverage is not evidence of
absence; no new external source premise is required.
