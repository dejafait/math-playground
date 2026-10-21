# L050 — Exact upper-face noise defect and a nonsmall realizable quartic

## Hypotheses

Keep exactly L049's SU(2) forest Gaussian, upper-face edge set E_top,
u, d, eta, K, P and Q, including all transverse end edges and three
transverse directions. Work in ordinary dimensionless stored coordinates,
a=8/N, with N admitted and even. The identities below in fact hold for
every integer N>=2; the explicit potential test uses N>=4. No change of
probe, forest, boundary condition, bare coupling or flow is made.

Regard E_top as the relative one-cochains of the three-dimensional
transverse cube: a component uses N edges in its own direction and
N-1 interior vertices in each other direction. Edges contained in a
transverse boundary face are absent, while edges meeting such a face
remain. Let T=T3 be the incidence with (T phi)_e=phi(v)-phi(v'), and set

\[
 \Delta_0=T^T T,\qquad G3=\Delta_0^{-1},\qquad
 P=T G3 T^T,\qquad
 \Delta_T=T T^T+D_{1,T}^T D_{1,T}.                    \tag{1}
\]

D_(1,T) is the transverse edge-to-plaquette incidence. Its orientation
has no effect on Delta_T. The finite relative tensor-product spectrum
of L003/L026 makes Delta_0 and Delta_T positive definite. Write
Q_parallel^c=P Q^c and Q_perp^c=(I-P) Q^c for each color c. Fractional
powers below are the ordinary positive finite-matrix spectral calculus.

## Conclusion

For lambda>0 define

\[
\begin{split}
 b_N(\lambda)&=\frac1N+\frac2N\sum_{n=1}^{N-1}
 \frac{\lambda\cos^2(n\pi/(2N))}
      {\lambda+4\sin^2(n\pi/(2N))},\\
 \gamma(\lambda)&=2\operatorname{arsinh}(\sqrt\lambda/2),\\
 b_N(\lambda)&=\frac{\sqrt{\lambda(\lambda+4)}}2
          \coth(N\gamma(\lambda))-\frac\lambda2.
\end{split}                                                        \tag{2}
\]

The full upper-face noise and its defect obey exactly

\[
 K_d=I-b_N(\Delta_T)(I-P),\qquad
 I-K=\frac PN+b_N(\Delta_T)(I-P).                    \tag{3}
\]

All these operators commute with P. In particular the gradient defect
is exactly 1/N, while the zero-divergence defect has symbol b_N.
For every lambda>0,

\[
 \frac\lambda{\lambda+4}\le b_N(\lambda)
 \le\min\{1,\ 1/N+\sqrt\lambda\}.                  \tag{4}
\]

Thus L049's actual quartic defect has the energy representation and bound

\[
\begin{split}
 Z(u)&=\frac1{8N}\sum_c\|Q_\parallel^c\|^2
   +\frac18\sum_c\langle Q_\perp^c,
                       b_N(\Delta_T)Q_\perp^c\rangle,\\
 0\le Z(u)&\le\frac1{8N}\sum_c\|Q^c\|^2
   +\frac18\sum_c\|\Delta_T^{1/4}Q_\perp^c\|^2.
\end{split}                                                        \tag{5}
\]

On a spectral subspace lambda<=a^2 M the defect norm is at most
a(1/8+sqrt(M)). If lambda_N/a^2 tends to Lambda>0, then

\[
 \frac{b_N(\lambda_N)}a\longrightarrow
 \sqrt\Lambda\coth(8\sqrt\Lambda),\qquad
 \frac{1/N}a=\frac18.                              \tag{6}
\]

These are low-frequency statements only. For every even N>=2 a
zero-divergence mode of eigenvalue 4 has defect b_N(4)>=1/2, so
||I-K||>=1/2. There is also a test in the actual nonlinear product
range, not just an arbitrary edge mode. For every N>=4 one can choose
u supported on four interior vertices such that

\[
 P Q^c=0\quad\hbox{for all }c,\qquad
 q_A=\frac12,\qquad Z\ge\frac7{32},\qquad
 \frac{Z}{q_A}\ge\frac7{16}.                       \tag{7}
\]

Consequently no uniform pointwise estimate Z<=epsilon_N q_A with
epsilon_N tending to zero holds for all upper potential fields. This
stops that proposed action-only shortcut. It does not establish a
nonzero signed cumulant, growth for either actual probe, or failure of
compensation by R and E in L049. The bound on the fractional product
energy in (5), its signed contraction with f_(i,0),r_0, the derivative
correction E, other cubic pairs and all remaining jets are unresolved.
There is no full a^2-scaled response, logarithmic coefficient, finite
matching, interacting reflected error <=c_box/2, continuum construction
or finite positive mass claim.

## Proof

### 1. Identify the complete boundary covariance

Use only L026's exact linear lift of the forest Gaussian to the Hodge
field z; no nonlinear vertex is replaced by an unmodified Hodge
polynomial. L049's actual upper circulation is

\[
 d_e=z_1(N-1,v)-z_1(N-1,v')-z_\mu(N-1,v).           \tag{8}
\]

Different components of z are independent. L003, proof section 2, and
L026(6) give the complete relative sine/cosine basis. Put
mu_n=4 sin^2(n*pi/(2N)). The squared last axial **edge** mode is 1/N
for n=0 and (2/N)cos^2(n*pi/(2N)) for n>0. The squared last axial
**vertex** mode is (2/N)sin^2(n*pi/N), n=1,...,N-1. Thus define

\[
\begin{split}
 R_N(\lambda)&=\frac1{N\lambda}
  +\frac2N\sum_{n=1}^{N-1}
       \frac{\cos^2(n\pi/(2N))}{\lambda+\mu_n},\\
 W_N(\lambda)&=\frac2N\sum_{n=1}^{N-1}
       \frac{\sin^2(n\pi/N)}{\lambda+\mu_n}.
\end{split}                                                        \tag{9}
\]

The covariance of z_1(N-1,.) is R_N(Delta_0). The block diagonal
covariance of the three z_mu(N-1,.) fields is W_N(Delta_T): each
transverse component has its own edge cosine and two vertex sine
coordinates, precisely including the transverse end edges.

Completeness of the N axial edge modes gives
1/N+(2/N)sum_(n=1)^(N-1)cos^2(n*pi/(2N))=1. Also
sin^2(n*pi/N)=mu_n cos^2(n*pi/(2N)). Hence exactly

\[
 b_N(\lambda)=\lambda R_N(\lambda),\qquad
 W_N(\lambda)=1-b_N(\lambda).                       \tag{10}
\]

The cochain identity D_(1,T) T=0 proves Delta_T T=T Delta_0.
Moreover P is an orthogonal projection, since T^T T=Delta_0.
It follows that P commutes with Delta_T and

\[
 T R_N(\Delta_0)T^T=b_N(\Delta_T)P.                 \tag{11}
\]

For example, apply (11) to a gradient T phi and to its orthogonal
complement separately; on the former it is the intertwining identity
and on the latter T^T vanishes. Combining independent component
covariances in (8) now gives

\[
 K_d=T R_N(\Delta_0)T^T+W_N(\Delta_T)
     =I-b_N(\Delta_T)(I-P).
\]

L049 gives K=K_d-P/N, proving (3). This computes the actual block
without discarding pinned end rows or presuming transverse directions
independent after taking the curvature.

### 2. Resolve the scalar symbol and its bounds

Let D be the unscaled interval difference on N edges and N-1 interior
vertices. The Neumann edge Laplacian A_N=D D^T is tridiagonal, with
endpoint diagonal entries 1, interior diagonal entries 2 and adjacent
entries -1. The cosine decomposition in (9) says
R_N(lambda)=((A_N+lambda I)^(-1))_(N-1,N-1).

Put gamma=2 asinh(sqrt(lambda)/2), so lambda+2=2 cosh(gamma).
For j=0,...,N-1 the vector c_j=cosh((j+1/2)gamma) obeys the interior
homogeneous recurrence and the left endpoint equation
(1+lambda)c_0-c_1=0. At the right endpoint,

\[
 (1+\lambda)c_{N-1}-c_{N-2}
 =\cosh((N+1/2)\gamma)-\cosh((N-1/2)\gamma)
 =2\sinh(N\gamma)\sinh(\gamma/2).
\]

Dividing c by this last positive quantity solves
(A_N+lambda I)r=e_(N-1), including both endpoints. Therefore

\[
 b_N(\lambda)=
 \frac{2\sinh(\gamma/2)\cosh((N-1/2)\gamma)}
      {\sinh(N\gamma)}
 =\sinh\gamma\coth(N\gamma)-\frac\lambda2,
\]

which is (2), since sinh(gamma)=sqrt(lambda(lambda+4))/2.

The cosine weights in (9) are nonnegative and sum to one. All axial
eigenvalues lie in [0,4], so averaging lambda/(lambda+mu_n) proves
lambda/(lambda+4)<=b_N(lambda)<=1. For the stronger upper estimate,
the function
f(theta)=lambda cos^2(theta/2)/(lambda+4 sin^2(theta/2)) decreases on
[0,pi]. The right Riemann sum with spacing pi/N is no larger than its
integral; its last value is zero. Thus

\[
 b_N(\lambda)\le\frac1N+\frac2\pi\int_0^\pi f(\theta)d\theta
 =\frac1N+\frac{\sqrt{\lambda(\lambda+4)}-\lambda}{2}
 \le\frac1N+\sqrt\lambda.                          \tag{12}
\]

For the displayed integral substitute t=tan(theta/2); the integrand
times dtheta becomes
2lambda dt/[(1+t^2)(lambda+(lambda+4)t^2)]. Partial fractions and
the integral of 1/(1+t^2) give its stated value. The last inequality
follows by squaring sqrt(lambda(lambda+4))<=lambda+2sqrt(lambda),
whose two sides are positive. This proves (4) without a mode cutoff.

### 3. The quartic energy and low-frequency limit

Apply (3) to L049's Z=(1/8)sum_c (Q^c)^T(I-K)Q^c.
Orthogonality of P and I-P, and their commutation with Delta_T, give
the equality in (5); (12) gives its upper bound by spectral calculus.
On eigenvalues at most a^2 M, both the gradient eigenvalue 1/N=a/8
and the complementary symbol are at most a(1/8+sqrt(M)). This proves
the asserted subspace norm estimate. It is not an estimate on arbitrary
products Q of the random potentials.

If lambda_N/a^2 tends to Lambda>0, then gamma(lambda_N)/a tends to
sqrt(Lambda), N gamma tends to 8sqrt(Lambda),
sinh(gamma)/a tends to sqrt(Lambda), and lambda_N/a tends to zero.
Substitute these limits in the exact formula (2). The argument of coth
has a positive limit, so continuity proves (6). In particular, fixed
transverse mode indices have Lambda=(pi/8)^2 sum_j k_j^2, with the
own-direction index permitted to be zero. No sum of rough products or
infinite contraction has been interchanged with this fixed-mode limit.

### 4. High modes and an actual potential-product obstruction

Take one transverse component with its constant own-direction edge
mode e_0 and vertex indices N/2 in the other two directions. This is
an admissible relative mode for every even N>=2. Its divergence is
zero because D^T e_0=0, so P annihilates it. Its transverse eigenvalue
is 0+4sin^2(pi/4)+4sin^2(pi/4)=4. Equation (3) and (4) give a defect
b_N(4)>=1/2. Consequently ||I-K||>=1/2. Equation (2) also gives
b_N(4) tending to 2sqrt(2)-2, but no probe contraction follows.

To avoid relying only on an arbitrary edge mode, choose a square of
four interior vertices in the first two transverse directions. With
1<=m<=N-2 let them be
v_0=(m,m,m), v_1=(m+1,m,m), v_2=(m+1,m+1,m),
v_3=(m,m+1,m). Set their color-vector potentials successively to
e_1,e_2,-e_1,-e_2, and set u=0 at all other vertices. These are
allowed upper potentials: L049's covariance N G3 is positive definite
on the whole interior vertex space, and no additional linear constraint
is imposed. Values on transverse boundary vertices are still zero.

The only nonzero Q=u(v) cross u(v') are the four square edges. Their
third-color entries form an oriented unit circulation, and their other
colors vanish. There is one incoming and one outgoing unit value at
each square vertex, hence T^T Q^3=0 and P Q^3=0. Its norm squared
is 4. In the componentwise transverse Hodge Laplacian each of these
edges has diagonal 6. The two parallel edges of each of the two
components are neighbors in one transverse vertex direction, with
opposite signs; their off-diagonal Laplacian entries are -1.
No Hodge cross-component terms occur. Therefore

\[
 (Q^3)^T\Delta_T Q^3=4\cdot6+2+2=28.               \tag{13}
\]

All transverse Laplacian eigenvalues are at most 12 by L003's tensor
product spectrum. Thus (4) implies
b_N(lambda)>=lambda/(lambda+4)>=lambda/16 on this spectrum. From
P Q^3=0, (5) and (13) give Z>=28/(8*16)=7/32, while
q_A=||Q^3||^2/8=1/2. This proves (7) at every mesh N>=4, with a
translated square if desired. Hence the uniform relative-smallness
estimate fails even on realizable Q. The test is mesh dependent and
not a fixed smooth continuum field or an expectation under the Gaussian.
It proves no signed response growth or noncompensation of L047.

### 5. Verification, scope and downstream use

Run `OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_upper_noise_spectrum.py`.
The full certificate is
`scripts/combined-ward-response/upper-noise-spectrum-certificate.json`.
Seven exact rational N=2 checks pass, including an independently
inverted actual four-dimensional Hodge boundary covariance and the full
defect matrix. N=2 is an algebra check rather than an admitted probe
evaluation. Five N=4 binary64 diagnostics pass; the complete 108-row
boundary identity residual is below 8.89e-16, versus tolerance 1e-11.
Three exact integer checks of the actual four-vertex Q give divergence
zero, norm squared 4 and Laplacian energy 28. All fifteen check records
and the empty failures field were inspected. Numerical diagnostics are
not an outward enclosure or proof of the general spectral identity.
The arbitrary-mesh identities and bounds are the analytic proof above.

This is a specialization/reproduction of the existing finite relative
spectral decomposition, Gaussian covariance and real symmetric spectral
theorem. Recomputing their general theory would be redundant; computing
this particular physical-boundary block is needed because the approved
flow-renormalization and bulk-matching sources do not supply it. No
originality or progress beyond those general source methods is claimed.

Equation (5) supplies an explicit fractional-energy target for a signed
Z contraction, replacing the unavailable uniform-smallness shortcut.
It does not bound the energy of the full random product, and estimates
on smooth external columns alone cannot be assigned to every internal
mode. L049's R and observable derivative correction E must still be
retained, as must top/non-top pairs and the other L011 jets. Comparing
the completed group with L047 at a^2 scale remains the continuation
test; a fixed-mode defect tending to zero is not that comparison.

## Mathlib

Coverage of the full specialized upper-face covariance and actual-product
counterexample: **not checked**. Coverage of supporting finite real
symmetric spectral calculus, discrete relative cochains and fractional
matrix powers: **not checked**. No matching Mathlib theorem is asserted.
The imported local input is L003, proof section 2, reproduced with
ordinary-coordinate scaling in L026, and L049's Gaussian regression;
the particular boundary evaluation and qualifications are proved here.
