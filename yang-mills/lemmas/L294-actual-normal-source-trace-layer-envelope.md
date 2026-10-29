# L294 — Summable trace and layer envelopes for the actual normal sources

## Hypotheses

Retain L280's SU(2) relative cube, even N>=2, a=8/N, all
boundary-contained links pinned, boundary-fixed gauges and every
variable normal link at both endpoints. Sources are differentiated
at zero in (|s|+|t|)||f_*||_infinity<eta_src<1, with eta_src>0.
Use exactly L282(1)'s
product bump and L003's separated spatial indices K_N, spatial
modes phi_k, positive weights b_(k,a) and gamma_(k,a). All matrices
C,B,L=C*C+BB* use unscaled incidence and counting measure. As in
L282(20), define the actual source fields

\[
 \sigma_{+,k,a}=f_*\psi_{k,a}\,dx_1\wedge dx_2,
 \quad \sigma_{-,k,a}=\theta\sigma_{+,k,a},\qquad
 X_{\epsilon,k,a}=(L/a^2)^{-1}(C^*/a)\sigma_{\epsilon,k,a}.
 \tag{1}
\]

The displayed fields are scalar fields for one fixed color; the same
estimate applies to each of the three colors. Only their component 1
is considered. This is the normal component
on the face x_1=-4; the component projection is not a replacement
of the full Wilson coefficient. The physical inner product used
to normalize modes is a^4 times the counting sum.

Put y=(x_2,x_3,t), d=x_1+4. Fix real smooth cutoffs chi(y), eta(d)
as in the approved one-face test: their product w is supported in
a collar disjoint from the other faces and away from all edges,
and eta=1 on [0,d_0] for some d_0>0. They do not depend on N or k.
For normal edge indices n>=0, the center has d=(n+1/2)a.

## Conclusion

Let mathfrak X_(epsilon,k,a) be the tensor trigonometric interpolant
of (X_(epsilon,k,a))_1: cosine modes in x_1, including zero, and
positive sine modes in each of x_2,x_3,t, with exactly L003's
normalizations and finite index ranges. This choice, not an
arbitrary interpolation of boundary data, defines its face trace

\[
 T_{\epsilon,k,a}(y)=\mathfrak X_{\epsilon,k,a}(-4,y).
 \tag{2}
\]

There is C_f independent of every even N and k in K_N such that,
with r=|k| and gamma=gamma_(k,a), the envelope

\[
 A_{k,a}=C_f(1+r)^7e^{3\gamma}
 \tag{3}
\]

has all of the following properties for both epsilon=+,-:

\[
 \|\mathfrak X_{\epsilon,k,a}\|_{C^3([-4,4]^4)}\le A_{k,a},
 \qquad
 \partial_1\mathfrak X_{\epsilon,k,a}(-4,y)=0,
 \tag{4}
\]
\[
 \big|\mathfrak X_{\epsilon,k,a}(-4+d,y)-T_{\epsilon,k,a}(y)\big|
       \le \tfrac12 A_{k,a}d^2\quad(0\le d\le8),
 \tag{5}
\]
\[
 b_{k,a}A_{k,a}^2
       \le C_f'(1+r)^{15}e^{-r/4},\qquad
 \lim_{R\to\infty}\sup_{N\ {m even}}
       \sum_{\substack{k\in K_N\\|k|>R}}b_{k,a}A_{k,a}^2=0.
 \tag{6}
\]

For each fixed k in the infinite separated mode set,
mathfrak X_(epsilon,k,a) converges in C^2 on the closed cube to
the component 1 of L282(3)'s continuum field X_(epsilon,k).
In particular (2) converges to its actual normal trace. No a priori
continuum boundary regularity theorem is needed to define that
trace: the uniformly differentiated mode series below constructs it.

The interpolated localized amplitude w mathfrak X has physical
Lipschitz and supremum norms at most C_w A_(k,a). If M>=0 is a
fixed integer, then on meshes with (M+1/2)a<=d_0, its sampled
values u from the approved test satisfy

\[
 \begin{split}
 &\sum_{k\in K_N} b_{k,a}
 \max_{\epsilon\in\{+,-\}}
 \max_{0\le n\le M}
 \sup_{y\ {m on\ the\ tangential\ grid}}
 \left|u_{\epsilon,k,a}(n,y)-\chi(y)T_{\epsilon,k,a}(y)\right|^2
 \\
 &\hspace{20mm}\le
 C_{f,w}a^4(M+1/2)^4\longrightarrow0.                       \tag{7}
 \end{split}
\]

Thus the source trace/layer and source-envelope summability
obligations hold for the complete external-mode sum. They do not
bound the complete signed kernel defect F_(N,k) in the approved
transfer. In particular (6) is not an N-scale tail estimate for that
defect. The finite-cube-to-half-space comparison, deep-layer and
tangential localization errors, missing bulk second vertices and
the bound mathcal F_N=o(N) remain unproved. No Wilson external curl
has been dropped and no auxiliary slab limit is taken here. There
is no interacting comparison, continuum construction or mass claim.

## Proof

### 1. The exact normal forcing and a smooth reflected extension

Write s_(+,k,a)(x,t)=f_*(x,t)phi_k(x)sinh(gamma(4-t)) as a smooth
function on R^4, and s_-=s_+ composed with time reflection. The
bump makes both compactly supported. For the oriented 12 curl,
(dA)_12=partial_1 A_2-partial_2 A_1, so its adjoint component 1
is +partial_2. Directly collecting the two incident plaquettes
on any variable component-1 edge gives

\[
 q_{\epsilon,k,a}(z)=
 \frac{s_{\epsilon,k,a}(z+(a/2)e_2)
              -s_{\epsilon,k,a}(z-(a/2)e_2)}a.
 \tag{8}
\]

This is exactly ((C*/a)sigma)_1 on that edge grid, including
normal end edges. Boundary-contained 12-plaquettes have zero
source. Coordinates 3 and 4 are interior vertex coordinates,
coordinate 2 in (8) moves from a vertex to its two neighboring
plaquette midpoints, and coordinate 1 stays at its edge midpoint.
Time reflection does not reverse the spatial 12 orientation.

Regard the right side of (8) as a smooth function throughout R^4.
It equals the integral of partial_2 s(z+ta e_2) for
-1/2<=t<=1/2. L003 gives gamma<=Omega_(k,a)<=pi r/8. Every spatial
trigonometric derivative has size at most a constant times the
corresponding power of (1+r); on the support of any derivative of
f_*, time lies in [1,2], so every time derivative of the hyperbolic
factor is bounded by gamma^j e^(3 gamma). The same bound holds
after reflection. The product rule and this integral therefore give

\[
 \max_{|\beta|\le6}\|\partial^\beta q_{\epsilon,k,a}\|_\infty
       \le C_0(1+r)^7e^{3\gamma}=:B_{k,a}.                  \tag{9}
\]

Here C_0 depends only on the finite collection of bump derivatives
through order 7 and the fixed mode normalizations. It does not
depend on the number of modes or on a. The supports in coordinates
1 and 3 stay in [-1/4,1/4]; in coordinate 2 they stay in
[-1/4-a/2,1/4+a/2]; time stays in [1,2] or [-2,-1]. Since a<=4,
these supports remain strictly inside the cube even on the coarsest
meshes. In particular the coordinate-2 support is inside [-9/4,9/4].

Extend q from the cube evenly across both x_1 faces and oddly
across both faces in each other coordinate, periodically with
period 16 in each coordinate. Call this smooth function Q. All
derivatives match across reflection seams because q vanishes in
a neighborhood of every face. The extension preserves the sup
bounds (9), since reflections only change derivative signs.
This is a reflected extension of the forcing for an estimate;
it does not assume that the physical vector inverse is scalar
Dirichlet, or that its boundary values vanish.

### 2. Three discrete Laplacians and coefficient decay

Let H_a be the component-1 block of L/a^2 and define on functions
on R^4 the centered difference operator

\[
 (h_a Q)(z)=\sum_{j=1}^4
       \frac{2Q(z)-Q(z+ae_j)-Q(z-ae_j)}{a^2}.
 \tag{10}
\]

L003's exact interval complex says H_a is DD* in its midpoint
coordinate 1 and D*D in its other, vertex coordinates. On the
first normal edge DD* has the row (q_0-q_1)/a^2: its outside
ghost value is q_0. Even reflection at x_1=-4 gives precisely
that ghost value. The upper endpoint works identically. In the
other coordinates the boundary vertex values are zero, exactly
the odd-reflection convention. Hence restriction of h_a Q to
the component-1 grid is H_a q.

The operator h_a commutes with each of these reflections and
with period-16 translations. Its iterates retain the required
parities and zero values on the odd faces. Applying the same
boundary-row argument repeatedly proves, for every even N,
that H_a^3 q is the restriction of h_a^3 Q. This includes stencils
that cross several reflected faces on a coarse mesh.

The exact identity

\[
 \frac{2Q(z)-Q(z+ae_j)-Q(z-ae_j)}{a^2}
   =-\int_{-1}^1(1-|t|)\partial_j^2Q(z+tae_j)\,dt
 \tag{11}
\]

follows twice from the fundamental theorem of calculus. Each
integration weight has integral one. Expanding the third power
of the sum in (10) and using (9) bounds ||h_a^3 Q||_infinity by
4^3 B_(k,a). The grid volume a^4 N(N-1)^3 is at most 8^4, so

\[
                 \|H_a^3 q\|_a\le8^2 4^3 B_{k,a}.        \tag{12}
\]

For clarity use ell for an internal four-dimensional tensor
index, distinct from the external spatial index k. Its ranges are
0<=ell_1<=N-1 and 1<=ell_j<=N-1 for j=2,3,4. Set

\[
 E_\ell(z)=e_{\ell_1}(x_1)v_{\ell_2}(x_2)
                   v_{\ell_3}(x_3)v_{\ell_4}(t),\qquad
 \Lambda_{\ell,a}=\sum_{j=1}^4
               \left[\frac2a\sin\frac{\pi\ell_j}{2N}\right]^2.
 \tag{13}
\]

These are exactly orthonormal for the physical grid measure;
H_a E_ell=Lambda_(ell,a)E_ell. The sine bound in L003/L280 gives
Lambda_(ell,a)>=|ell|^2/16. There is no all-zero index because
the three tangential indices are positive. Self-adjointness in
this finite physical inner product gives

\[
 \begin{split}
 \widehat q_{\ell,a}
    &=\Lambda_{\ell,a}^{-3}
                  \langle H_a^3q,E_\ell\rangle_a,\\
 \widehat X_{\ell,a}
    &=\Lambda_{\ell,a}^{-1}\widehat q_{\ell,a},\qquad
 |\widehat X_{\ell,a}|
       \le C B_{k,a}|\ell|^{-8}.                          \tag{14}
 \end{split}
\]

The second line is the component-1 field in (1): L has no
component mixing, and L282(20) identifies this quadratic inverse
with the actual transverse source field. No nonlinear jet is
transported by this identity.

Define mathfrak X by the finite sum of these coefficients times
the continuous trigonometric functions E_ell. It agrees exactly
with every sampled component-1 field value. For |beta|<=3,
||partial^beta E_ell||_infinity<=C_beta |ell|^|beta|. The number
of nonnegative four-indices with max ell_j=m is at most 15m^3;
|ell| and max ell_j differ by at most a factor two. Consequently

\[
 \sum_{|\ell|>R}|\ell|^{j-8}\le C_j R^{j-4}
       \quad(R\ge1,\ 0\le j\le3).                         \tag{15}
\]

These convergent sums and (14) prove the C^3 bound in (4), after
enlarging C_f in (3) by fixed constants. Every cosine has zero
first derivative at both x_1 endpoints, proving the second part
of (4). Twice integrating the normal derivative, using that zero
value and the uniform second derivative bound, proves (5).

### 3. The trace is the continuum trace, not a guessed vertex value

Fix external k. L003 gives gamma_(k,a)->Omega_k and the same
continuous spatial trigonometric functions on every mesh. On
the compact support, s_(epsilon,k,a) and each of its derivatives
converge uniformly to s_(epsilon,k). Equation (8) therefore
converges uniformly, with every fixed derivative, to
q_(epsilon,k)=partial_2 s_(epsilon,k).

For each fixed internal ell, product Riemann sums give
widehat q_(ell,a)->integral q_(epsilon,k)E_ell, and
Lambda_(ell,a)->(pi/8)^2|ell|^2. Thus each fixed inverse
coefficient in (14) converges to that of the continuum inverse
defined in L282(3). That continuum source is compactly supported
away from every face. Three integrations by parts for its mixed
scalar Laplacian have no boundary terms and give the same
C B_k |ell|^-8 bound for its inverse coefficients. Alternatively
the bound follows for each ell from (14) and the fixed-mode limit.
Here B_(k,a) is bounded along the fixed-k sequence.

The tails (15) for j=0,1,2 tend to zero uniformly for both the
discrete interpolants and the continuum series. First fixing a
finite internal cutoff, passing to the coefficient limits, and
then removing that cutoff proves C^2 convergence on the closed
cube. The limiting series is the specified relative spectral
inverse, not another boundary problem. Its restriction at x_1=-4
is the asserted continuum normal trace. On the actual first
normal edge, the difference from this interpolant's face value
is at most A_(k,a)a^2/8 by (5); a normal endpoint was not replaced
by a zero boundary vertex.

### 4. Complete external-mode summability and the layer test

L003 gives, uniformly on K_N,
gamma>=r/8, alpha_(k,a)<=pi^2 r^2/64 and

\[
 b_{k,a}=\frac{\alpha_{k,a}a}
                 {\sinh(a\gamma)\sinh(8\gamma)}.
 \tag{16}
\]

Since r>=1, sinh(a gamma)>=a gamma and
sinh(8 gamma)=e^(8 gamma)(1-e^(-16 gamma))/2 yield

\[
 b_{k,a}\le\frac{\pi^2}{4(1-e^{-2})}\,r e^{-8\gamma}.
 \tag{17}
\]

Multiplying by (3) squared leaves e^(-2 gamma)<=e^(-r/4),
which proves the first assertion of (6). The sum of its right
side over nonnegative k_1,k_2 and positive k_3 converges: shell
counts grow polynomially and the exponential decays. Extending
the finite mode sets by zero proves both a uniform bound on
sum_k b A^2 and the uniform tail assertion. The same constants
bound both reflected sources. Thus no growing external cutoff
is hidden in this argument.

The product rule gives the stated C^1 bounds for w mathfrak X.
For n<=M and (M+1/2)a<=d_0, eta((n+1/2)a)=1; (5) gives

\[
 |u_{\epsilon,k,a}(n,y)-\chi(y)T_{\epsilon,k,a}(y)|
       \le\tfrac12\|\chi\|_\infty A_{k,a}
                           a^2(M+1/2)^2.                  \tag{18}
\]

Square, take the displayed suprema and maximum, multiply by b,
and sum using (6). This proves (7) without discarding any
external modes. Its square-root form is O(a^2(M+1/2)^2) in the
b-weighted source norm; it is not a bound after contraction
with S_N or S_infinity. Three colors and the two source orders
do not change a source-envelope bound, but their exact factor
3a^2 and both ordered defect pairings must still be retained in
the unproved transfer.

### Scope and verification

This proof supplies the stronger source estimate explicitly sought
by the prior EXPLORE assessment, beyond L282's physical L2
convergence. It uses only the stated relative spectral identities,
elementary finite-dimensional self-adjointness, the fundamental
theorem of calculus and summable mode estimates. No scalar
boundary-regularity theorem is imported or reproved. Originality
beyond the sources checked is not asserted. The proof checks the
normal midpoint and tangential vertex stencils, both normal
endpoints, both source signs, coarse meshes and the complete
external tail analytically; it needs no numerical certificate.
The separate critical audit below accepts these source estimates under
the stated inputs; it does not itself supply a kernel-contracted bound.

### 5. Separate conceptual audit (2026-10-27)

This audit accepts (4)--(7) and the stated C^2 convergence, with exactly
L003's grids and L280/L282's quadratic source identity. It imports no
new regularity theorem and makes no originality claim. The full matching
Mathlib result remains unchecked.

**Forcing, reflections and all meshes.** In the oriented 12 incidence,
the component-1 edge occurs with plus sign in the plaquette above it
in direction 2 and minus sign below in the curl itself; transposing
the incidence collects the two plaquette sources as (8). Equivalently
the formal adjoint of the term -partial_2 A_1 is +partial_2. The
plaquette centers differ from that edge center only by +/-a e_2/2.
No normal endpoint is removed. The compact product bump leaves a
positive margin at every face even for a=4: the only enlarged support
coordinate is 2, contained in [-9/4,9/4]. Consequently the odd/even
extension of the forcing, not of an arbitrary source row, is smooth
through every seam. Its derivatives through order six have (9)'s
bound for both reflected sources. The coordinate-1 even ghost is the
first edge value itself, whereas each tangential odd ghost has zero
value on the boundary vertex. These are exactly DD* and D*D. Centered
differences preserve those parities, so the identification with H_a
continues through all three iterations, including coarse-grid stencils.

**Coefficient decay and the trace.** Each application of h_a is an
average of second derivatives with a weight of integral one, with
four coordinate choices. Thus three applications cost at most 4^3
times the sixth derivative bound; multiplying the supremum by the
square root of physical grid volume costs at most 8^2. In the
physically orthonormal tensor basis, Cauchy--Schwarz and
Lambda >= |ell|^2/16 give
|Xhat_ell| <= Lambda^-4 ||H_a^3 q||_a <= C B |ell|^-8.
The three strictly positive tangential indices exclude a zero
eigenvalue even when the normal cosine index is zero. Four-dimensional
shell counting then gives a differentiated tail bounded by
C B R^(j-4) for 0<=j<=3, as in (15). In particular the C^3 bound
is uniform, not a finite-mode estimate with a growing constant.
Every normal cosine has derivative zero at the face. Integrating
twice proves (5), including the actual first midpoint displacement a/2.
For fixed external k, the Riemann sums and eigenvalues converge in
each internal mode. The uniform j<=2 tails identify their limit with
L282's specified continuum relative inverse in C^2, including its trace.
No scalar Dirichlet replacement or nonlinear jet transfer occurs.

**Complete external sum.** The exact weight (16), gamma>=r/8 and
alpha<=pi^2 r^2/64 give (17) with the stated constant. Its product
with A^2 is bounded by C(1+r)^15 exp(-2 gamma), hence by
C(1+r)^15 exp(-r/4). Three-dimensional external shell counts are
polynomial, so this is a common summable majorant over all K_N and
has a uniformly vanishing tail. Squaring the midpoint Taylor error
before summing yields precisely a^4(M+1/2)^4 in (7). This accepts
the source estimate for both orders and all colors; it does not
replace a bound on a signed operator pairing by an ordinary source norm.

## Mathlib

Full matching and supporting Mathlib coverage for these staggered
relative-mode trace/layer estimates has not been checked. No
absence claim or formal verification is made.
