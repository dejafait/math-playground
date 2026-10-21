# L187 — Project the third probe-quartic placement before the energy count

## Hypotheses

Use L184–L186's exact fixed-mesh SU(2) setting: relative box
(-4,4)^4, admitted even N, a=8/N, straight direction-1 lower-rooted
forest, complete displacement and both actual L010 probes i=3,6 at
tau=1/16. The bare expansion is taken before refinement. All matrices
use ordinary full variable-link coordinates. Vertex potentials vanish
on every physical face; all normal end edges remain.

Keep S, P, A=PAP, B=B_i=PBP, M=2SAS, V=q Phi,
H=1-D Phi/2 and Gamma exactly as in L184. In particular M is signed,
A contains both insertion subtractions, and Phi is the original pinned
prefix. Select Q_3 of L184(5), without commuting any covariance:

\[
 Q_3=12\sum_{e,g,a,b,u,v}(SB)_{ve}(\Gamma_e)_{ab}
                    P_{ag}(\Gamma_g)_{uv}M_{ub}.             \tag{1}
\]

Constants below may depend on the fixed data, but not sufficiently
fine admitted meshes. The index a in (1) is a link label.

## Conclusion

For a rank-one input SB=n y^T define

\[
 \mathcal J_y=-\tfrac12\{H^T\operatorname{diag}(y)V
                          -V^T\operatorname{diag}(y)H\},\qquad
 U_n=\operatorname{diag}(Vn)H-\operatorname{diag}(Hn)V.
                                                               \tag{2}
\]

Then its entire third-placement contraction is

\[
 \mathcal Q_3(n,y)=-6\operatorname{Tr}(P\mathcal J_y M U_n^T),
 \qquad
 PU_n=P\{\operatorname{diag}(Vn)
                   -\operatorname{diag}(Rn)V\},\quad R=1-D\Phi.
                                                               \tag{3}
\]

The second identity retains the pinned jump. At every upper axial
normal edge g it also holds, separately, that

\[
 (U_n)_{g\bullet}=(Vn)_g I_{g\bullet}-n_g V_{g\bullet}.     \tag{4}
\]

For the two actual probes the resulting all-mesh bound is

\[
 |Q_{3,i,N}|\le C_i N^{7/2},\qquad
 |Q_{i,N}|=|Q_1+Q_2+Q_3|\le C_i N^{7/2}.                 \tag{5}
\]

This improves the stopped global O(N^5) count but misses O(N^3) by
one half power. In particular its scaled upper bound is only
|a^3 Q_i|<=C_i sqrt(N); no boundedness, growth lower bound, limit,
sign or cubic coefficient is established. L185–L186 still remove
Q_1+Q_2 at cubic scale, so Q_3 is the remaining quartic obstacle.
The sextic partner, co-closed probe flow down to zero time, independent
f_(i,2),r_0, finer asymptotics, full compensation, matching, reflected
error <=c_box/2 and continuum/infrared construction remain open.
This is local progress with assessed finite-matrix and mode methods,
not discovery beyond the sources checked.

## Proof

### 1. The signed order and all four row terms

L184(3) gives Gamma_e=-[H_e^T V_e-V_e^T H_e]/2, where the subscript
denotes a row. Hence sum_e y_e Gamma_e=mathcal J_y and
sum_v (Gamma_g)_(uv) n_v=-(U_n)_(gu)/2. Substitute both identities
into (1):

\[
 \mathcal Q_3(n,y)
 =-6\sum_{g,b,u}(P\mathcal J_y)_{gb}M_{ub}(U_n)_{gu}
 =-6\operatorname{Tr}(P\mathcal J_y M U_n^T).
                                                               \tag{6}
\]

The last equality uses M=M^T, not positivity or a moved residual.
For reference put K_XY=XMY^T for X,Y in {H,V}. Expanding (6) is
exactly

\[
 \begin{split}
 \mathcal Q_3(n,y)=3\sum_{e,g}y_e\{&
 (HP)_{eg}(Vn)_g(K_{VH})_{eg}
 -(HP)_{eg}(Hn)_g(K_{VV})_{eg}\\
 &-(VP)_{eg}(Vn)_g(K_{HH})_{eg}
 +(VP)_{eg}(Hn)_g(K_{HV})_{eg}\}.
 \end{split}                                                  \tag{7}
\]

These are all four terms of the third placement. Neither the second
placement nor its smooth tilted leg has been substituted here.

### 2. Exact pinned product cancellation

Let psi=Phi n and let phi=Phi w for any full link vector w. Both
are zero at every boundary vertex. On each oriented edge, multiplying
its two endpoint values gives the scalar identity

\[
 (q\psi)D\phi+(D\psi)q\phi=2D(\psi\phi).                 \tag{8}
\]

This also holds on normal end edges: the boundary endpoint values
are zero on both sides. Expanding (2) on w, then using (8), yields

\[
 U_nw=(q\psi)w-(Rn)q\phi-D(\psi\phi).
\]

Since psi phi is again a pinned vertex potential, P kills its full
incidence, proving the second identity in (3). No row is omitted.
At an upper axial normal edge, Phi's head value is zero, so
(D Phi)_g=-V_g. Thus H_g=I_g+V_g/2 and
(Hn)_g=n_g+(Vn)_g/2. Substitution into (2) proves (4) by canceling
the two identical double-prefix terms. This is a row identity,
not permission to extend a prefix smoothly through the upper face.

### 3. Positive trace counts, with the upper layer retained

Let n_0=N-1, U_st=min(s,t), G=Delta_T^(-1), and
K=Phi S Phi^T. L182(10) and L186(4) give
0<=K<=U tensor G. All traces in this proof include the entire finite
spectrum. L186(9) gives Tr G=O(N^3), and Tr U=O(N^2), whence

\[
 \operatorname{Tr}K\le C N^5.                            \tag{9}
\]

L026(6)–(7)'s full four-dimensional relative spectrum gives
Tr S<=Tr Sigma_H<=C N^4: its dimensionless inverse eigenvalues
are at most N^2/(4|k|^2), a shell max k_j=r has at most C r^3
modes, and sum_(r<N) r=O(N^2). The allowed zero own-direction
cosine modes are included; there is no zero full one-form mode.

The actual pinned incidence satisfies L186(5), and its axial
identity UL_D=I+(Uj)j^T gives Tr(UL_D)=2n_0. Therefore

\[
 \operatorname{Tr}(DKD^T)
 \le\operatorname{Tr}(UL_D)\operatorname{Tr}G
                 +\operatorname{Tr}U\,n_0^3
 \le C N^5.                                             \tag{10}
\]

The upper rank-one correction is retained in 2n_0. Positivity and
HSH^T<=2S+DKD^T/2, as in L186, now imply

\[
 \|S^{1/2}\|_{HS}\le C N^2,\qquad
 \|HS^{1/2}\|_{HS}+\|VS^{1/2}\|_{HS}\le C N^{5/2}.
                                                               \tag{11}
\]

Let Pi_top be the diagonal orthogonal projection onto precisely the
upper axial normal edges. Their
V rows are the last interior vertex rows of Phi, so (9)'s positive
comparison restricted to that layer gives

\[
 \|\Pi_{top}VS^{1/2}\|_{HS}^2
 =\operatorname{Tr}(\Pi_{top}VSV^T\Pi_{top}^T)
 \le n_0\operatorname{Tr}G\le C N^4.                     \tag{12}
\]

There is no smallness assertion for that layer. Finally the prefix
matrix on each transverse fiber is lower triangular with entries
zero or one and at most N rows and columns. Its row/column sum
bound gives ||Phi||_op<=N. The bounded-degree endpoint map q and
||P||<=1 give ||VP||_op<=C N.

### 4. Only the external covariance leg is smooth

Use L185(3)–(4)'s exact full heat expansion

\[
 B_i=a^2\sum_{k,l}d_{i;kl}e_ke_l^T,\qquad
 SB_i=a^2\sum_{k,l}d_{i;kl}n_ke_l^T,\quad n_k=Se_k,
 \quad\sum_{k,l}|d_{i;kl}|p(k)p(l)\le C_{i,p}.            \tag{13}
\]

Here e_k=a^2 f_k are the ordinary orthonormal full Hodge product
modes, and p is any fixed polynomial. Their supremum norm is at
most C a^2. If lambda_k is their physical eigenvalue, commutation
of P with Sigma_H gives n_k=lambda_k^(-1)P f_k.

For clarity, smoothness of P f_k follows directly from the same
relative tensor spectrum, rather than from rough-input consistency.
For a multi-index with all entries positive, the component modes
span a block of at most four dimensions; D maps the corresponding
vertex sine product to that block with component coefficients
2 sin(k_mu pi/(2N)). On this block P is the orthogonal matrix
I-dd^T/|d|^2. If one index is zero, only its own link component
exists and is already divergence-free. Thus P f_k is a combination
of at most four product modes with bounded coefficients. The gap
and L028's mode amplitudes and derivative bounds imply, for some
fixed polynomial p,

\[
 \|n_k\|_\infty\le C p(k),\qquad
 |n_k(x+a e_j)-n_k(x)|\le C a p(k)                       \tag{14}
\]

on each staggered component grid, including its smooth sine/cosine
extension to boundary coordinates. This does not extend Phi across
a face or assert smoothness of M on any rough input.

The first component vanishes on each transverse face. Summing at
most N such entries gives ||Phi n_k||_infinity<=C N p(k).
Its transverse neighboring differences, including normal transverse
end edges, are at most C N a p(k)<=C' p(k); the zero boundary
value equals the sine extension there. Its axial differences are
one entry of n_k except at the upper pinned edge. Consequently

\[
 \|Vn_k\|_\infty\le C N p(k),\qquad
 \|(1-\Pi_{top})Rn_k\|_\infty\le C p(k),\qquad
 \|\Pi_{top}Rn_k\|_\infty\le C N p(k).                   \tag{15}
\]

The upper jump remains of order N in the safe bound. Apply (3),
(11)–(12), and (15), using ||P||<=1, to obtain

\[
 \begin{split}
 \|PU_{n_k}S^{1/2}\|_{HS}
 &\le\|Vn_k\|_\infty\|S^{1/2}\|_{HS}
 +\|(1-\Pi_{top})Rn_k\|_\infty\|VS^{1/2}\|_{HS}\\
 &\quad+\|\Pi_{top}Rn_k\|_\infty
                              \|\Pi_{top}VS^{1/2}\|_{HS}
 \le C N^3 p(k).                                        \tag{16}
 \end{split}
\]

### 5. Signed residual and the attained threshold

Here PD=0 gives PH=P and H^T P=P; it does **not** give
PH^T=P. The earlier version of this paragraph incorrectly used that
last identity. Keep H^T in its original order instead. For y=e_l,
equation (2) gives exactly

\[
 P\mathcal J_yS^{1/2}
 =-\tfrac12\{PH^T\operatorname{diag}(y)VS^{1/2}
           -PV^T\operatorname{diag}(y)HS^{1/2}\}.
\]

The bounded incidence degree and ||Phi||_op<=N give
||PH^T||_op<=1+||Phi||_op ||D||_op/2<=C N.
The operator/trace bounds above and ||y||_infinity<=C a^2 imply

\[
 \|P\mathcal J_{e_l}S^{1/2}\|_{HS}
 \le C a^2(N\,N^{5/2}+N\,N^{5/2})\le C' N^{3/2}.       \tag{17}
\]

Thus the stated bound survives with no changed power of N, and all
later estimates here retain their conclusions. No commutation of P
and H^T is needed. This repairs a matrix-order error rather than
assuming the erroneous cancellation as an input.

Let E=S^(1/2)AS^(1/2). L186(12) imports the complete residual
form bound ||E||_op<=C N. Since M=2S^(1/2)E S^(1/2), finite trace
Cauchy–Schwarz and ||X E||_HS<=||X||_HS ||E||_op give

\[
 |\mathcal Q_3(n_k,e_l)|
 \le12\|E\|_{op}\,
       \|P\mathcal J_{e_l}S^{1/2}\|_{HS}
       \|PU_{n_k}S^{1/2}\|_{HS}
 \le C N^{11/2}p(k).                                    \tag{18}
\]

The extra P on the last factor is exact: the first factor already
has output in im P, so its Hilbert–Schmidt inner product kills the
orthogonal output of U_n S^(1/2). No positivity of E or M is used.
Multiply (18) by the exterior a^2 in (13) and sum its complete
heat spectrum. This proves Q_3=O(N^(7/2)). L185–L186 prove the
second bound in (5). The remaining half-power loss in this absolute
count must be removed, or the signed trace treated differently,
before cubic boundedness can be claimed. Even a cubic bound would
still require a controlled limit argument.

### 6. Exact checks and their limited scope

Run from the notebook:

    python3 scripts/combined-ward-response/check_probe_quartic_third_placement.py

The full certificate is
`scripts/combined-ward-response/probe-quartic-third-placement-certificate.json`.
Its rational row and trace formulas match L184's direct polynomial
fourth-moment calculation in both full and singular supported fixtures:
Q_3=-81360 and -882. The four signed terms are retained separately.
A pinned two-interior-vertex incidence fixture verifies (3), PD=0
and the upper-row cancellation (4) exactly. All selected records were
inspected in full. These are algebra checks; they are not actual box
probe values or evidence of signed growth. The all-mesh bound is
the analytic argument (9)–(18), conditional on its cited inputs.

## Mathlib

Full matching bound and supporting pinned-prefix, relative-mode and
finite matrix coverage: **not checked**. Unknown availability is not
absence. L184 imports Isserlis' named fourth-moment theorem; its
contraction is reused without reproof. The particular projected trace,
pinned product rule and layer count are necessary specializations
because Q_3 keeps the residual on a rough slot. No general flow or
renormalization theorem is reproved. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this attempt; full renormalized correlations do not import this
selected bare-group limit.
