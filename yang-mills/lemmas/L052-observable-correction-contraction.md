# L052 — Observable correction contraction and one bounded noise term

## Hypotheses

Keep L049–L051's actual three-color SU(2) forest Gaussian, both probes
f=f_(i,0), i=3,6, residual r=r_0, a=8/N, tau=1/16 and all upper
edges, including transverse end edges. Take the small-coupling
coefficient at each fixed mesh first. Use one-color forest matrices
S=Sigma_F, B=B_(i,F), A=A_F from L018. Let J be L051's map to the
upper potential u, and let T_eta be the linear map to L049's
eta=d-L/N. In particular T_eta S J^T=0. T_eta is held fixed when
the covariance is tilted. It is not the transverse incidence.

Use L051's C=JSJ^T=NG3, U=JSBSJ^T and V=JSASJ^T. Define

\[
\begin{split}
K_B&=T_\eta SBS T_\eta^T,& K_A&=T_\eta SAS T_\eta^T,\\
K_{BA}&=T_\eta(SBSAS+SASBS)T_\eta^T,\\
H_B&=T_\eta SBSJ^T,& H_A&=T_\eta SASJ^T.             \tag{1}
\end{split}
\]

K_B,K_A,K_BA are symmetric edge matrices; H_B,H_A have an edge
index followed by a vertex index. Vertex rows and columns at a pinned
boundary vertex mean zero. For ordered edges e=(v,v'), h=(w,w'), put

\[
\begin{split}
\delta_{eh}(C)&=C_{vw}C_{v'w'}-C_{vw'}C_{v'w},\\
\delta_{eh}(C,M)&=C_{vw}M_{v'w'}+M_{vw}C_{v'w'}
                   -C_{vw'}M_{v'w}-M_{vw'}C_{v'w},\\
p_{eh}(x,y)&=(H_B)_{ex}(H_A)_{hy}+(H_A)_{ex}(H_B)_{hy},\\
\Xi_{eh}&=-p_{eh}(w,v)C_{v'w'}+p_{eh}(w,v')C_{vw'}
             +p_{eh}(w',v)C_{v'w}-p_{eh}(w',v')C_{vw}.
                                                               \tag{2}
\end{split}
\]

All sums below are over the full ordered edge-pair set.

## Conclusion

L049's complete observable derivative correction has the exact formula

\[
\begin{split}
\mathcal E(f,r)&=E_{BA}+E_B+E_A+E_\times,\\
E_{BA}&=3\sum_{e,h}(K_{BA})_{eh}\delta_{eh}(C),\\
E_B&=3\sum_{e,h}(K_B)_{eh}\delta_{eh}(C,V),\\
E_A&=3\sum_{e,h}(K_A)_{eh}\delta_{eh}(C,U),\\
E_\times&=3\sum_{e,h}\Xi_{eh}.                     \tag{3}
\end{split}
\]

The term with the mixed second derivative of the noise covariance obeys

\[
 |E_{BA}|\le C_i,\qquad a^2 E_{BA}\longrightarrow0. \tag{4}
\]

Thus L051's complete selected nonradial upper quartic plus top/top
cubic-pair group can be written

\[
G_i=-6\Phi_D(C,W+W^T)-6\Phi_D(U,V)
        +E_B+E_A+E_\times+O_i(a^{-1}).              \tag{5}
\]

Here D, W and Phi_D are precisely L051's fixed original objects.
No scaled bound, limit or cancellation is claimed for the three
remaining E terms or the two Phi terms. The estimate (4) excludes an
unsuppressed logarithm only in E_BA; L051's R bound still does not
exclude one in R. Other cubic pairs, action/measure/insertion/flow
jets, full response logarithm, matching, the interacting reflected
error <=c_box/2, continuum field construction, full reflection
positivity and finite positive mass remain unresolved.

## Proof

### 1. Keep the full covariance under the quadratic tilt

Use the standard finite-dimensional Gaussian quadratic-tilt identity
in L018(8) and L051(6). On a neighborhood of s=t=0 the normalized
tilt by exp(sf+tr) has three independent identical covariance blocks

\[
S(s,t)=(S^{-1}-2sB-2tA)^{-1}.                       \tag{6}
\]

Positive definiteness at each fixed mesh supplies an integrable
Gaussian majorant for polynomial expectations and their derivatives.
Additive constants in f,r disappear from normalization. Define

\[
C(s,t)=JS(s,t)J^T,\quad
K(s,t)=T_\eta S(s,t)T_\eta^T,\quad
H(s,t)=T_\eta S(s,t)J^T.
\]

At zero H=0 by L049's global regression. It is not zero throughout
the tilt. Differentiating the inverse without commuting its factors
gives

\[
\begin{gathered}
C_s=2U,\quad C_t=2V,\qquad
K_s=2K_B,\quad K_t=2K_A,\quad K_{st}=4K_{BA},\\
H_s=2H_B,\qquad H_t=2H_A.                          \tag{7}
\end{gathered}
\]

The original noise K=K(0,0) and maps J,T_eta remain fixed in
F(u)=Q^T mathcal K Q/8 from L049. Regressing eta anew under the tilt
would change this polynomial and would not compute its cumulant.

### 2. Contract the two cubic vertices

L049 gives S_(3,top)=sum_e eta_e dot (u(v) cross u(v'))/2.
Import Isserlis' theorem for centered finite Gaussian moments. Within
one epsilon tensor, contracting any two legs forces two colors equal
and yields zero. All nonzero pairings of two cubic vertices therefore
join each of the first vertex's three legs to a leg of the second.
The six permutations have their determinant signs, and the color
contraction for each is six times that sign. Consequently

\[
E_{s,t}[S_{3,\mathrm{top}}^2/2]
=\frac34\sum_{e,h}\det
\begin{pmatrix}
K_{eh}&H_{ew}&H_{ew'}\\
H_{hv}&C_{vw}&C_{vw'}\\
H_{hv'}&C_{v'w}&C_{v'w'}
\end{pmatrix}(s,t).                               \tag{8}
\]

This includes e=h, edges sharing vertices and pinned endpoints;
singular joint row covariances are allowed because they are linear
images of the nondegenerate forest vector. The same argument with
two cross products gives

\[
E_{s,t}F=\frac34\sum_{e,h}K(0,0)_{eh}
                          \delta_{eh}(C(s,t)).     \tag{9}
\]

The normalized mixed derivative of a fixed polynomial expectation
is its third cumulant against f,r, with all five connected
subtractions. L049(7) and (15) therefore identify E(f,r) with the
mixed derivative of (8) minus (9).

Expand the determinant in (8) along its first row. The difference
of its first term and (9) is
(K(s,t)-K(0,0))_eh delta_eh(C(s,t)). Its mixed derivative at zero is

\[
4\big[(K_{BA})_{eh}\delta_{eh}(C)
      +(K_B)_{eh}\delta_{eh}(C,V)
      +(K_A)_{eh}\delta_{eh}(C,U)\big].
\]

Each other determinant term has two H factors. Since H(0,0)=0,
its mixed derivative contains precisely H_s H_t+H_t H_s, times
the remaining base C entry. No derivative of C or second derivative
of H survives in these terms. Their signed sum is 4 Xi_eh by (2).
Multiplication by 3/4 proves (3). In particular it retains the
mixed noise/potential attachments that noise/potential independence
at s=t=0 alone would miss.

### 3. Bound the mixed second noise derivative uniformly over edge pairs

Use L028's full exterior expansion (11)–(13) as extended to the
upper rows in L029's proof of (13). In that expansion the ordinary
covariance-square-root column v_k has upper H,L,d sizes bounded by
(1,a,a^2) P(k), and its residual column z_k has sizes bounded by
(a^2,a^3,a^4) P(k). These uniform bounds include every transverse
end edge and all mode indices; their constants are independent of
the chosen edge. Since 1/N=a/8, the actual noise row satisfies

\[
 |(v_k)_{\eta_e}|\le C a^2 P(k),\qquad
 |(z_k)_{\eta_e}|\le C a^4 P(k).                    \tag{10}
\]

Indeed eta=d-L/N as a linear row on the forest slice; no nonlinear
vertex has been transferred to the Hodge law unchanged. L018's
explicit linear lift and the free-gauge invariance of the two
quadratic forms give the same exterior expansion for these rows.
Its noise/noise entry at possibly distinct e,h is

\[
(T_\eta SBSAS T_\eta^T)_{eh}
=\sum_{k,l}e^{-\tau(\lambda_k+\lambda_l)}
     (B_{i,a})_{kl}(v_k)_{\eta_e}(z_l)_{\eta_h}.    \tag{11}
\]

Here B_(i,a) is L028's uniformly bounded relative probe form, not
the forest matrix B in (1). L028 gives lambda_k>=c|k|^2 and a
fixed polynomial P; hence the double heat-weighted polynomial sum
in (11) is uniformly finite. Equation (10) yields O(a^6) uniformly
in both edges. The other matrix in K_BA is the transpose of this
one, so

\[
\sup_{e,h}|(K_{BA})_{eh}|\le C_i a^6.              \tag{12}
\]

Using different edges does not require a new regularity assertion:
the two uniform column bounds in (10) apply separately before the
absolutely convergent heat sums are taken.

### 4. Sum the rough potential covariance with its full spectrum

An entrywise bound on C alone loses two powers of a here. Instead
use C=NG3 and its complete Hilbert–Schmidt norm. L029's transverse
Dirichlet eigenvalues obey lambda_k>=4|k|^2/N^2, with all three
indices positive. Therefore

\[
\|C\|_{\mathrm{HS}}^2
=N^2\sum_{k\in\{1,\ldots,N-1\}^3}\lambda_k^{-2}
\le\frac{N^6}{16}\sum_{k\in\mathbb N_{>0}^3}|k|^{-4}
\le C N^6.                                       \tag{13}
\]

For the last convergence, the shell max k_j=m has at most 3m^2
points and |k|>=m, so its contribution is at most 3/m^2. Thus
(13) includes rough modes without any low-frequency substitution.

Every interior vertex belongs to at most six retained edges. Zero
rows at boundary vertices contribute nothing. For example
sum_(e,h) C_vw^2 <=36 ||C||_HS^2, and the same bound holds for
each choice of first/second endpoints. Cauchy–Schwarz on the ordered
edge-pair set gives

\[
\sum_{e,h}|\delta_{eh}(C)|\le72\|C\|_{\mathrm{HS}}^2.
                                                               \tag{14}
\]

Combining (12)–(14) and N=8/a yields
|E_BA|<=216 C_i a^6 ||C||_HS^2=O_i(1), proving (4).
No sign, limiting finite value or cutoff-independent numerical
constant suitable for the interacting error is asserted. Equation
(5) now follows directly from L051(5) and (3)–(4).

### 5. Verification and scope of the reproduction

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_observable_correction.py`.
The full inputs and exact results are retained in
`scripts/combined-ward-response/observable-correction-certificate.json`.
Six exact rational checks pass, including two direct Gaussian
cumulants of the cubic square minus the conditional quartic and their
invariance under additive probe constants. The corrections are 423/16
and -16209/64. In the latter case E_BA, E_B and E_cross are respectively
-7587/64, -4059/16 and 3807/32, while E_A=0; the first case exercises
the remaining E_A term. A pinned product and the base conditional
expectation are checked as well. These surrogate checks test signs,
factors and connected subtractions, not the actual box asymptotics.
The arbitrary-mesh bound (4) is the analytic argument above.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. This is a local
reproduction of Gaussian tilting, Isserlis contraction and existing
relative spectral estimates for the actual physical-boundary rows.
General flow-renormalizability and stress-matching results are not
reproved or given extra boundary hypotheses. L048's general two-cubic
contraction remains valid; (3) specializes the previously unexpanded
observable correction and (4) removes one of its terms at a^2 scale.
This is no claim of progress beyond the sources' general methods.

The remaining comparison must retain E_B,E_A,E_cross jointly with
L051's two signed Phi terms. Bounds for C alone do not bound V,K_A
or H_A, which contain the unflowed residual. In particular (4) cannot
be promoted to a bound on E. ATTEMPTS/017's uniform-smallness stop
is unchanged; no low-mode substitution, omitted end edge or discarded
observable derivative is used.

## Mathlib

Coverage of the full specialized correction identity and uniform
E_BA bound: **not checked**. Supporting finite Gaussian tilting,
Isserlis' theorem, Hilbert–Schmidt estimates and relative spectral
calculus: **not checked**. No matching Mathlib theorem is asserted.
The named finite Gaussian identities are used in the conventions
of L018 and L051; L028–L029 supply the full exterior estimates and
the relative spectrum. Unknown coverage is not evidence of absence.
