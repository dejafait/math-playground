# L182 — Resum the cubic probe's gradient terms before estimating flow

## Hypotheses

Use the SU(2) relative box, admitted even meshes a=8/N, straight
lower-rooted forest, complete displacement, and both actual L010
probes at tau=1/16 as in L181. All Taylor expansions are at fixed mesh
before refinement. Work in dimensionless full-link coordinates with
ordinary Euclidean adjoints, and keep all physical faces and normal
end edges. Vertex potentials vanish on every boundary vertex.

To distinguish the two covariances, write

\[
 D=D_0,\quad L=D_1^T D_1,\quad
 \Sigma_H=(L+DD^T)^{-1},\quad
 P=1-D(D^TD)^{-1}D^T,\quad S=P\Sigma_H P.
 \tag{1}
\]

Thus P is the orthogonal co-closed projection. The pinned scalar
Laplacian D^TD is invertible. L018 and L026 fix the full forest
retraction R=1-D Phi, including the upper pinned jump; pi_F restricts
its output to the nonforest links. Let z have three independent colors
with the possibly singular covariance S, and set x=pi_F Rz,
phi=Phi z. This is a representation of the original forest Gaussian,
not a different nonlinear integration prescription.

Let F_(i,3)(y) be the cubic Taylor polynomial of the complete uncentered
flowed numerator, on arbitrary full-link initial coordinates y. Its
restriction is L011's f_(i,1). Its quadratic polynomial is
sum_c (y^c)^T B_i y^c, with precisely L018's
B_i=H_tau Q_i H_tau and H_t=exp[-t(L+DD^T)/a^2]. Centering is immaterial
for this cubic. Use L181's original forest polynomial

\[
 \rho(x)=r_1(x)-D S_3(x)[2\Sigma_F A_F x].                 \tag{2}
\]

For a vertex field phi put (q phi)_e=phi_tail+phi_head. Brackets are
edgewise SU(2) brackets with t_c=i sigma_c/2, hence minus the color
cross product. Full-link inner products sum links and colors.

## Conclusion

The complete cubic probe obeys the exact deterministic identity

\[
 F_{i,3}(Rz)=F_{i,3}(z)+J_{i,1}(z)-\tfrac12J_{i,2}(z),     \tag{3}
\]
\[
 J_{i,1}=\langle B_i z,[z,q\phi]\rangle,\qquad
 J_{i,2}=\langle B_i z,[D\phi,q\phi]\rangle.
 \tag{4}
\]

This combines the observable cubic and the complete quadratic-flow
integral before removing their gradient dependence. Neither is
transferred separately. There are mesh-independent constants with

\[
 \|J_{i,1}\|_{L^2(S)}\le C_i[\log(eN)]^{1/4},\qquad
 \|J_{i,2}\|_{L^2(S)}\le C_i N,\qquad i=3,6.              \tag{5}
\]

In particular the complete correction J_i=J_(i,1)-J_(i,2)/2 is
O(a^-1) in L^2 and a^3 J_i tends to zero in L^2. The two terms in
(4) are correlated cubic polynomials; no independence is claimed.

L181's selected joint response therefore has the exact representation

\[
 G_{i,a}=\mathbb E_S[F_{i,3}(z)\rho(\pi_F Rz)]
              +\mathbb E_S[J_i(z)\rho(\pi_F Rz)].          \tag{6}
\]

In the first term, the two short-time input lines of the probe's
Duhamel formula can use H_s z because E_s z=H_s z on the co-closed
space. The integral still reaches s=0. The second term contains only
final-time smoothed B_i and explicit pinned prefix brackets, with no
flow-time integral.

This is a uniform bound on the probe correction, not a cubic bound
or scaled limit for (6). In particular a^3 J_i -> 0 in L^2 cannot be
paired with a mesh-dependent rho without an estimate. The available
consequence is only

\[
 a^3|\mathbb E_S[J_i\rho(\pi_F Rz)]|
       \le C_i a^2\|\rho\|_{L^2(\Sigma_F)}.                \tag{7}
\]

An O(a^-2) residual norm would give boundedness of this part, and an
o(a^-2) residual norm would remove it; neither is asserted or imported.
Its signed contraction may allow sharper estimates than (7). The
co-closed contribution, the complete joint limit, the independent
f_(i,2),r_0 term, finer asymptotics, matching, the interacting reflected
error <=c_box/2 and continuum/infrared construction remain unresolved.
This is local reproduction of gauge-jet and Gaussian norm methods,
not a claim of progress beyond the sources checked.

## Proof

### 1. Preserve the law and apply the existing full gauge identity

The finite cochain identity D_1 D=0 makes P commute with Sigma_H.
Consequently S is positive semidefinite and 0<=S<=Sigma_H. The Hodge
Gaussian decomposes into independent co-closed and gradient fields.
Since R D=0, R annihilates its entire gradient component; L018's
linear quotient law therefore gives

\[
 \operatorname{Cov}(Rz)=R\Sigma_H R^T=I_F\Sigma_F I_F^T.
 \tag{8}
\]

Thus x has the original forest law and I_F x=Rz. This holds also at
the upper normal edges, since R and Phi retain their pinned definitions.
It transfers any polynomial only by the explicitly displayed map R.

The complete uncentered numerator is invariant under pinned gauge
transformations: L010's flow is equivariant and its two final probes
are invariant. Its constant and linear jets vanish. Apply L156 proof
section 1, equation (4), with its temporary quadratic matrix replaced
by B_i. This previously proved general identity gives

\[
 D F_{i,3}(y)[D\phi]
        =-\langle B_i y,[y,q\phi]\rangle.                  \tag{9}
\]

The hypothesis B_i D=0 follows from Q_i D=0 and commutation of the
Hodge heat with the gradient projection. Integrate (9) along
z+tD phi for -1<=t<=0, holding phi fixed. Since
B_i(z+tD phi)=B_i z, the integrand is affine in t. In full,

\[
 F_{i,3}(z-D\phi)-F_{i,3}(z)
   =\int_0^{-1}-\langle B_i z,[z+tD\phi,q\phi]\rangle\,dt
   =J_{i,1}-\tfrac12J_{i,2}.
\]

This proves (3) for every z and every pinned phi, before setting
phi=Phi z. The sign and half come from the actual interval of this
integral. No invariance of a truncated probe or of rho was used.
L019's general observable-jet compensation and L022's pure-gradient
test are consistent with this specialization; they are not cutoff
estimates being transferred to this group.

### 2. Bounds for the full spectrum and the actual prefix

Let K=Phi S Phi^T. By positivity and L156(6)--(7),

\[
 0\le K\le \Phi\Sigma_H\Phi^T\le M\otimes G_T,
 \qquad \|K\|_{\rm HS}\le C N^4,                         \tag{10}
\]

where M_st=min(s,t) on interior axial levels and G_T is the inverse
three-dimensional transverse Dirichlet Laplacian. The last domination
and its N^4 Hilbert--Schmidt bound are precisely the full-prefix
estimate proved there, including both axial ends and the constant
axial edge mode. For positive matrices the Hilbert--Schmidt norm is
monotone in this order: Tr(Y^2-X^2)=Tr((Y-X)(Y+X))>=0 for 0<=X<=Y.
This justifies its use for K, even though P is nonlocal.

Also

\[
 \|S\|_{\rm HS}\le\|\Sigma_H\|_{\rm HS}
       \le C N^2\sqrt{\log(eN)}.                          \tag{11}
\]

To see the last estimate without omitting modes, use L026(6)--(7).
A component has one edge-cosine index 0,...,N-1 and three vertex-sine
indices 1,...,N-1. Its dimensionless eigenvalue is at least
4|k|^2/N^2. Squaring its inverse contributes at most
N^4/(16|k|^4). The shell max k_j=m contains at most C m^3 indices,
including all four components. Summation over 1<=m<N gives
C N^4 log(eN) for Tr Sigma_H^2. There is no zero full one-form mode;
the allowed zero in the cosine direction is included in the shell count.

We also need the smoothing strength on the *external* B_i leg. Choose
a real orthonormal eigenbasis e_k of the full Hodge Laplacian and put
v_(i,k)=B_i Sigma_H^(1/2) e_k. Then

\[
 B_i S B_i=B_i\Sigma_H B_i
       =\sum_k v_{i,k}v_{i,k}^T,
 \qquad \sum_k\|v_{i,k}\|_\infty^2\le C_i a^6.            \tag{12}
\]

Here is the coordinate normalization and uniform estimate. Write
lambda_k for the physical eigenvalue and f_(k,a) for the L2_a-normalized
product mode, so e_k=a^2 f_(k,a) and
Sigma_H^(1/2)e_k=a lambda_k^(-1/2) f_(k,a). L028's actual quadratic
forms have Q_i=a^2 Q_(i,a) in these coordinates; their bounded strain,
clover and incidence stencils give
||Q_(i,a) f_(k,a)||_infinity<=C_i p(k) for a fixed polynomial p,
with physical end rows retained. The coefficients are compactly
supported inside the box, so differentiating them in the adjoint
stencils has the same bound. The physical eigenvalues obey
lambda_k>=c|k|^2, and the normalized modes are uniformly bounded.
Consequently

\[
 v_{i,k}=a^3\lambda_k^{-1/2}e^{-\tau\lambda_k}
                     H_\tau Q_{i,a} f_{k,a},\qquad
 \|v_{i,k}\|_\infty\le C_i a^3 p_1(k)e^{-\tau\lambda_k}.
\]

The componentwise relative Hodge heat is a contraction in the supremum
norm: each scalar mixed Dirichlet/edge-Neumann discrete Laplacian has
nonpositive off-diagonal entries and nonnegative row sums, so its heat
matrix is nonnegative with row sums at most one. This includes the
normal end edges. Summing the last squared estimate over the entire
finite spectrum, dominated by the full infinite heat-weighted sum,
proves (12). No infrared or internal-loop damping is inferred from it.
The first equality in (12) uses B_i P=B_i exactly.

### 3. Correlated cubic polynomials via independent-copy norm bounds

Both J_(i,1) and J_(i,2) have one invariant alternating color bracket.
Every linear map in their definitions acts only on link or vertex
indices. For the color-diagonal Gaussian z, an internal contraction
of any two of their three slots sets two colors equal, hence vanishes.
They are therefore pure third chaos even though phi and z are
correlated.

Here is the needed finite Gaussian estimate, including why independent
copies may be used for a bound. Represent z=C xi with independent
standard real Gaussian coordinates, allowing C to be rectangular.
An ordered trilinear expression has a coefficient tensor T and its
value on xi,xi,xi depends only on sym T. If every internal contraction
vanishes, the Isserlis pairing theorem gives

\[
 \mathbb E|T(\xi,\xi,\xi)|^2
       =6\|\operatorname{sym}T\|_{\rm HS}^2
       \le6\|T\|_{\rm HS}^2
       =6\mathbb E|T(\xi_1,\xi_2,\xi_3)|^2,              \tag{13}
\]

where the three copies on the right are independent. Symmetrization
is an orthogonal projection, proving the inequality. This does not
assert equality with an independent-noise model or remove any term
from the original expectation.

For fixed colored link vector v, the forms

\[
 \langle v,[w,q\psi]\rangle=w^T M_v\psi,
 \qquad
 \langle v,[D\chi,q\psi]\rangle=\chi^T N_v\psi
\]

have ||M_v||_op+||N_v||_op<=C||v||_infinity. Indeed expand the bracket
in its structure constants, all bounded by one. Each edge has only
two endpoints and each vertex bounded degree, so every row and column
has boundedly many coefficients of magnitude at most C||v||_infinity.
The row/column-sum operator estimate proves the claim, including
pinned endpoints with their zero values. Color factors are fixed.

For independent w with covariance S and psi with covariance K,

\[
 \mathbb E|w^T M_v\psi|^2
   =\operatorname{Tr}(S M_v K M_v^T)
   \le\|M_v\|_{\rm op}^2\|S\|_{\rm HS}\|K\|_{\rm HS}.
 \tag{14}
\]

This is Hilbert--Schmidt Cauchy--Schwarz followed by the two-sided
operator ideal bound. For independent chi,psi both of covariance K,
the corresponding estimate is

\[
 \mathbb E|\chi^T N_v\psi|^2
       \le\|N_v\|_{\rm op}^2\|K\|_{\rm HS}^2.            \tag{15}
\]

Use (13) on each J, assigning its external B_i z to the first copy
and its two bracket arguments to the other copies. Expand the
covariance of the external copy by (12), summing also its three
colors. Applying (14)--(15) to each deterministic v_(i,k) gives

\[
 \|J_{i,1}\|_2^2
    \le C\sum_k\|v_{i,k}\|_\infty^2
                      \|S\|_{\rm HS}\|K\|_{\rm HS}
    \le C_i a^6 N^6\sqrt{\log(eN)},
\]
\[
 \|J_{i,2}\|_2^2
    \le C\sum_k\|v_{i,k}\|_\infty^2\|K\|_{\rm HS}^2
    \le C_i a^6 N^8.
\]

Since aN=8 these are exactly (5). In particular this argument avoids
an expectation of a spatial maximum, which would introduce a needless
extra logarithm. It uses all correlated contractions via (13), rather
than assuming that the exterior field is independent of its prefix.

### 4. Return to the approved joint group and retain its missing bound

L181(5), the law (8), and (3) give (6) without changing rho, either
insertion subtraction, or the order 2 Sigma_F A_F. On im P,
L agrees with L+DD^T, so E_s z=H_s z for every s>=0. Apply this only
inside the complete full-coordinate F_(i,3)(z) formula of L181(10).
The cubic observable remains present, as does the entire interval
[0,tau]; s=0 is not suppressed by this identity.

Cauchy--Schwarz, (8), and (5) prove (7). There is no estimate here
for ||rho||_2: its action derivative is nonlocal and not a standalone
gauge-invariant cubic. Thus this proof does not supply a bound on
(6), a limit interchange, or a compensation coefficient. Its concrete
use is to isolate all gradient dependence of the probe in a controlled
final-time correction before attempting the remaining signed pairing.

No numerical check is used to infer any limit or exponent. The finite
identities are applications of L156's proved gauge identity and the
named Isserlis theorem; the bounds above are analytic full-spectrum
bounds. No new general gauge or flow-renormalization theorem is needed.

## Mathlib

Full matching result and supporting cubic-chaos, cochain heat, and
matrix norm statements: **not checked**. Unknown availability is not
absence. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers the exact response target and records the primary literature
and its limitations. L156's local gauge identity and Isserlis' pairing
theorem are reused with the explicit specialization above; no source
about full renormalized correlations is imported as a selected-group
cutoff bound.
