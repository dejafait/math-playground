# L286 — Uniform bound for the separated cubic insertion pair

## Hypotheses

Use L280's SU(2) relative cube D=[-4,4]^4, even N>=2 and a=8/N.
All boundary-contained links are pinned; gauges are identity on boundary
vertices; every other link, including both normal endpoint cases, is
variable. Use L003's exact real bump h_+=f_* and h_-=theta f_*,
with supports in [-1/4,1/4]^3 times [1,2] and [-2,-1]. Retain all
three colors. Sources have (|s|+|t|)||f_*||_infinity<eta<1; all
covariances and derivatives in this statement are evaluated at zero.

Use the ambient all-link Wilson jets of L279(8)–(9) on L280's own
slice H=ker B*, with pinned slots zero and no forest-link deletion.
Let b_{pm,1}=T_pm[x^3]/6 be the cubic insertion polynomials and
G the extended transverse covariance of L280(18). Let mathcal B be
L279(24)'s contraction, with Euclidean counting measure. In particular
there is no additional a^4 in either plaquette sum.

## Conclusion

The entire first group of L280(20) obeys

\[
 I_{3,N}:=\frac16\mathcal B(T_-,T_+;G,G,G)
       =\mathbb E^H_0[b_{-,1}b_{+,1}],\qquad
 |I_{3,N}|\le C_f,\qquad N^{-2}I_{3,N}\longrightarrow0.       \tag{1}
\]

The constant is independent of even N; this is an analytic bound, not
a fit or an assertion about individual uncontracted tensor entries.
The proof retains the full transverse covariance and controls every
source vertex pair. No internal action vertex occurs in this group.

Write the other four groups, with their original signs, as

\[
\begin{split}
 R_{3,N}={}&-\tfrac12\mathcal B(T_-,T;G_+,G,G)
           -\tfrac12\mathcal B(T_+,T;G_-,G,G)\\
          &+\tfrac14\mathcal B(T,T;G_{-+},G,G)
           +\tfrac12\mathcal B(T,T;G_-,G_+,G).
\end{split}                                                   \tag{2}
\]

Thus mathcal K_3^H=R_{3,N}+O_f(1). In conjunction with L285(4),

\[
\begin{split}
 N^{-2}\kappa_a={}&N^{-2}R_{3,N}
 +\frac{10Z_0-1-16I_1}{128}\mathcal J_f\\
 &+\frac3{32}\left(\frac14-2Z_0-2I_1\right)\mathcal S_f
 +o(1).                                                       \tag{3}
\end{split}
\]

The constants and functionals in (3) are exactly those of L285.
Neither the scale nor convergence of R_{3,N} is established here.
In particular this does not determine the complete cubic N^2 limit,
its compensation, the subleading coefficient, or any mesh-uniform
higher remainder. Continuum existence, a nonzero physical sector and
finite positive mass remain open. This is a partial specialization
within the prior EXPLORE assessment, without a claim of certified
originality beyond its checked sources. The separate critical audit in
section 5 accepts the stated bound under these hypotheses.

## Proof

### 1. The exact cubic vertex contains a curl

For a plaquette p write its ordered signed matrices as X_j, j=1,...,4,
using L279's conventions on the current slice. Set

\[
 Y_p=\sum_jX_j=y_p^ct^c,\qquad
 Z_p=\frac12\sum_{j<k}[X_j,X_k]=\zeta_p^ct^c .                    \tag{4}
\]

Here y_p=(Cx)_p is exactly the unscaled oriented linear curvature.
The vector zeta_p is quadratic in the four signed edge vectors, with a
fixed finite list of coefficients independent of N and p.

The cubic coefficient of 4P_p is exactly

\[
 4p_3(p;x)=-2\operatorname{Tr}(Y_pZ_p)=y_p\mathbin{\cdot}\zeta_p.
                                                               \tag{5}
\]

To verify this specialization directly from L279(8), each X_j^2 is
scalar, so Tr(X_j^3)=Tr(X_j^2 X_k)=0. The only surviving degree-three
terms in the ordered product are Tr(X_i X_j X_k), i<j<k, each with
coefficient one. The trace of three su(2) matrices is alternating.
In Tr(Y_p Z_p), the terms with a repeated index vanish. For a fixed
ordered triple i<j<k, its three remaining terms are

\[
 \tfrac12\operatorname{Tr}\{X_i[X_j,X_k]
                    +X_j[X_i,X_k]+X_k[X_i,X_j]\}
       =\operatorname{Tr}(X_iX_jX_k).
\]

This proves (5) with the Wilson factor 4 and
-2 Tr(t^c t^d)=delta_cd. No nonlinear jet has been transported from
a forest slice. Consequently
b_{pm,1}=sum_{p parallel12} h_pm(z_p) y_p dot zeta_p, where z_p
in the weight is the plaquette center as in L279, and zeta_p is the
quadratic color vector in (4).

### 2. Uniform transverse edge bound on opposite supports

Suppress color. Work first with a<=1/2. Every edge of a weighted
12-plaquette lies in one of L284(9)'s fixed neighborhoods E_- or E_+.
All its directions are 1 or 2 and its time is a vertex coordinate.
The two neighborhoods have time separation at least 3/2. Constants
below are uniform on both E_- times E_+ and its reversed order.

We need the full edge covariance, in addition to the curl kernels.
L280(23) gives the exact relative decomposition

\[
 G=L^{-1}-B\Delta^{-2}B^*,\qquad L=C^*C+BB^*,\quad\Delta=B^*B.
                                                               \tag{6}
\]

Use L003's physically normalized spatial bases. For the component mu
in {1,2} define
chi_{mu,k}(x)=e_{k_mu}(x_mu) product_{j!=mu, j<=3} v_{k_j}(x_j).
The component indices have 0<=k_mu<N and 1<=k_j<N for j!=mu.
Write Omega^2=sum_{j=1}^3 omega_{k_j,a}^2 and

\[
 g_{a,\Omega}(t,s)=
 \frac{a\sinh(\gamma(t+4))\sinh(\gamma(4-s))}
      {\sinh(a\gamma)\sinh(8\gamma)},\quad
 \gamma=\frac2a\operatorname{arsinh}(a\Omega/2),\quad t<s.
                                                               \tag{7}
\]

L003's tensor modes give, for edges e parallel mu and f parallel nu,

\[
\begin{split}
 a^{-2}(L^{-1})_{ef}
 &=\delta_{\mu\nu}\sum_{k\text{ in component }\mu}
       \chi_{\mu,k}(x_e)\chi_{\mu,k}(x_f)g_{a,\Omega}(t_e,t_f),\\
 a^{-2}(B\Delta^{-2}B^*)_{ef}
 &=\sum_{k\in\{1,\ldots,N-1\}^3}
    \omega_{k_\mu,a}\omega_{k_\nu,a}
    \chi_{\mu,k}(x_e)\chi_{\nu,k}(x_f)H_{a,\Omega}(t_e,t_f),\\
 H_{a,\Omega}(t,s)&=-\partial_{\Omega^2}g_{a,\Omega}(t,s).
\end{split}                                                   \tag{8}
\]

Spatial arguments in chi are the actual edge midpoints/vertices.
For the last identity differentiate L003's finite time-mode sum:
H=sum_{j=1}^{N-1} v_j(t)v_j(s)/(omega_{j,a}^2+Omega^2)^2.
The two B factors are spatial differences of vertex sine modes, so
supply a omega each, with their two minus signs cancelling. For a
normalization check, Delta/a^2 is the physical scalar Laplacian;
B=-a d_0. Thus B Delta^-2 B*=a^-2 d_0(Delta/a^2)^-2 d_0^*.
Converting its point kernel with measure a^4 sum to a counting-matrix
entry gives precisely a^2 in (8). The same conversion for L^-1 also
gives a^2. The all-positive indices in the longitudinal term and the
zero cosine indices in the component inverse are both retained.

Here are uniform estimates for both finite sums. As in L284(10),

\[
 0\le g_{a,\Omega}(t,s)
 \le \frac{e^{-\Omega(s-t)/2}}{\Omega(1-e^{-2})},\qquad
 |k|/4\le\Omega\le\pi|k|/8,\quad \Omega/2\le\gamma\le\Omega.
                                                               \tag{9}
\]

To control H, differentiate (7) before using a bound. Set A=t+4,
D=4-s; then 0<A,D<8 and A+D<=8. We have

\[
 \partial_{\Omega^2}\gamma
   =\frac1{2\Omega\sqrt{1+(a\Omega/2)^2}}\le\frac1{2\Omega}.
\]

For r>0, coth r<=1+1/r (from e^{2r}-1>=2r). Hence, with a<=1/2,

\[
 \left|\partial_\gamma\log g_{a,\Omega}\right|
 \le A\coth(\gamma A)+D\coth(\gamma D)
       +a\coth(a\gamma)+8\coth(8\gamma)
 \le 17+4/\gamma.
\]

Combining this inequality with (9) proves

\[
 |H_{a,\Omega}(t,s)|
 \le C e^{-\Omega(s-t)/2}(\Omega^{-2}+\Omega^{-3}).          \tag{10}
\]

Every spatial basis factor is uniformly bounded, and each omega is
at most Omega. Since |k|>=1 and s-t>=3/2, the terms of both sums
in (8) are bounded by C exp(-3|k|/16), after enlarging C. This is
summable over all nonnegative spatial triples: grouping by maximum
index m leaves at most (m+1)^3 terms and exponential decay. Thus
both complete sums, not just any fixed modes, are uniformly bounded.
Their difference in (6) gives

\[
 |G_{ef}|\le C a^2
 \quad(e\text{ in a negative weighted plaquette},
       f\text{ in a positive weighted plaquette}).            \tag{11}
\]

This derivation used the exact relative modes, including the boundary
conditions of the longitudinal subtraction. No full-space scalar
replacement, boundary limit, or unproved inverse-square kernel theorem
is used. All normal links remain in the covariance even though the
insertion supports themselves are in the interior.

### 3. Curl lines and the full Gaussian contraction

For p,q weighted opposite 12-plaquettes and their edges e,f, L284(7)–(11)
and symmetry give

\[
 |(C_{12}G)_{pf}|+|(GC_{12}^*)_{eq}|\le C a^3.              \tag{12}
\]

L003's exact separated curvature formula and uniform mode majorant,
with the normalization justified below, give

\[
 |(C_{12}G C_{12}^*)_{pq}|\le C a^4.                       \tag{13}
\]

The normalization in (13) also follows without a further input:
x=aA, Cx=a^2dA, and CB=0 removes the longitudinal term in (6).
Thus its point covariance is a^4 times L003's bounded physical
separated curvature kernel. Reflection pairs every negative support
point with a positive one; the bound in L003 section 4 is uniform for
all such pairs, not just on the reflected diagonal. These estimates
and (11) are color-scalar and hold on the entire two-source grids.

By L280's color argument, every pairing with an internal contraction
at a cubic vertex is zero. One can also see this directly in (5):
zeta_p is a sum of brackets, so its three color indices with y_p are
alternating, whereas every covariance contracts two colors with a
Kronecker delta. The two cubic insertions have zero means. Of the
six fully crossing pairings between y_p dot zeta_p and y_q dot zeta_q,
each is of one of two types:

- The two linear curvatures pair together. The three factors have
  bounds C a^4, C a^2, C a^2 by (13) and (11).
- Each linear curvature pairs with an edge factor at the other vertex.
  The factors have bounds C a^3, C a^3, C a^2 by (12) and (11).

Both products are O(a^8). The finite color sum and the fixed local
quadratic coefficients in (4) multiply this bound by a constant
independent of N,p,q. This preserves the curl until after contraction;
expanding it into separately bounded edge terms would lose its powers
of a. Therefore

\[
 |\mathbb E^H_0[(4p_3(p;x))(4p_3(q;x))]|\le C a^8.         \tag{14}
\]

There are at most (N+1)^4 possible plaquette anchors in each source
sum, and the weights have absolute value at most F. Since a=8/N,

\[
 |\mathbb E^H_0[b_{-,1}b_{+,1}]|
 \le C F^2 a^8(N+1)^8\le C_f.                              \tag{15}
\]

This estimates the whole double sum, including all allowed edge
placements and colors. For the finitely many even N with a>1/2,
Gaussian nondegeneracy from L003 makes every term finite; increase
C_f to their finite maximum. Empty source grids contribute zero.
Finally b_pm,1=T_pm[x^3]/6; six crossing pairings give 6/36=1/6.
This proves (1) with exactly L280(20)'s first-group multiplicity.
Equations (2)–(3) follow by subtraction and L285(4).

### 4. Scope of the localization test

For any fixed lattice-distance cutoff R, the source vertices in (1)
are farther apart than R for all sufficiently large N. Hence (15)
controls the entire discarded tail of this subfamily, after N^-2
normalization, by C_f/N^2. It does not rely on a local bulk fit.

In the mixed groups of (2), an action vertex may approach the insertion
vertex or the opposite source. In the action/action groups both vertices
range over the box. Their differentiated covariance lines are not the
three separated lines used in (11)–(13). L285(7)'s uniform local-entry
approximation by itself supplies no summable error over these pairs.
No tail or boundary error for those four groups is claimed. The
remaining task needs a signed or derivative-weighted full vertex-pair
estimate; repeating an unweighted uniform-entry replacement will not
establish it. This proof controls one complete subfamily only.

### 5. Separate critical audit (2026-10-26)

This audit accepts (1)–(3), conditional on the stated relative quadratic
law, separated curvature kernels and L285's comparison. It does not use
L291's later conditional cancellation to verify any input.

In the cubic jet, the three surviving contributions to Tr(YZ) for
i<j<k have signs +,-,+, and therefore sum to Tr(X_i X_j X_k).
Terms with a repeated slot have zero trace. Since 4P=4-2 Tr of the
ordered product, (5) has the required factor -2 and hence y dot zeta.
This check applies with pinned slots zero and to the ambient jet on
the present slice. Each nonzero monomial has three distinct colors,
so internal Gaussian contractions really vanish; this is not an
assumption about spatial independence.

For the transverse kernel, the longitudinal term in (8) has positive
spatial vertex indices and the component inverse includes its own
cosine zero index. Both have the counting-matrix factor a^2. The
identity for H is differentiation of a finite time-mode sum at fixed
mesh, so it requires no infinite-sum interchange. On the separated
rectangles, differentiating the exact hyperbolic expression gives
the displayed bound (10): A+D<=8, a<=1/2, and
r coth(gamma r)<=r+1/gamma bound the four logarithmic derivatives
by 17+4/gamma. Multiplication by partial_(Omega^2) gamma and (9)
gives an exponentially summable majorant even after both spatial
frequency factors. This verifies the complete edge bound (11), not
merely its fixed-mode version.

The curl-edge and curl-curl factors have counting normalizations a^3
and a^4. The two possible fully crossing pairing types therefore both
cost a^8. The number of weighted pairs is at most (N+1)^8, so (15)
is uniform when a=8/N. All finite color and slot multiplicities are
mesh independent. The finitely many remaining coarse even meshes
are nondegenerate finite Gaussians, including the empty-grid case.
Finally six pairings divided by 6^2 give exactly the coefficient 1/6.
The residual four groups and (3) are algebraic subtraction using the
same coefficients, without any further estimate on them. No stronger
rate, uniform higher remainder or interacting conclusion is accepted.

## Mathlib

The full finite relative-box cubic insertion bound and its supporting
relative spectral kernels have not been checked in Mathlib. No absence
claim is made. Finite Gaussian pairing and the exact scalar time Green
function are reused from L279/L280 and L003, with the needed quadratic
law and normalizations justified above. The additional work is the
Wilson-specific curl factor and the complete separated pair estimate;
no external continuum existence or lattice-renormalization theorem is
asserted or reproved.
