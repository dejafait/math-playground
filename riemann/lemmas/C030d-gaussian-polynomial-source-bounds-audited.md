# Corollary C030d: audit of the Gaussian polynomial source bounds

## Hypotheses

Let N be an integer with N>=1, set d=2N-1, and let q be a real
polynomial of degree at most d (including q=0). Use the unnormalized norm

\[
 \|q\|_G^2=\int_{\mathbb R}e^{-x^2}|q(x)|^2\,dx.
\]

Complex evaluation means evaluation of this polynomial, not of its
modulus on the real axis. There is no parity or zeta hypothesis.

## Conclusion

All three bounds in Nicholas G. Polson, *On Hilbert's 8th Problem*,
[arXiv:1708.02653v24](https://arxiv.org/pdf/1708.02653v24),
11 September 2026, Lemma7.6, equations(23)-(25), printed p19, hold
under these hypotheses. Explicitly, for z=x+iy and 0<r<1,

\[
 e^{-\operatorname{Re}(z^2)}|q(z)|^2
 \le \frac{r^{-d}}{\sqrt\pi\sqrt{1-r^2}}
 \exp\!\left(-\frac{1-r}{1+r}x^2+\frac{1+r}{1-r}y^2\right)
 \|q\|_G^2.                                      \tag{23}
\]

With r_N=1-1/(2N),

\[
 C_N=\frac{r_N^{-d}}{\sqrt\pi\sqrt{1-r_N^2}}<2\sqrt N,
 \qquad e^{-x^2}|q(x)|^2\le C_N\|q\|_G^2
 \quad(x\in\mathbb R).                           \tag{24}
\]

For every real frequency y,

\[
 \left|\int_{\mathbb R}q(x)^2e^{-x^2}e^{-iyx}\,dx\right|
 \le 4^N e^{-y^2/12}\|q\|_G^2.                    \tag{25}
\]

These are coefficient-uniform reproductions of the cited source
claims. They audit one component used in Lemma7.7 and hence in the
finite source input of C030b. No conclusion about the full near-zero
assembly, far-time estimates, all-degree positivity or RH follows here.

## Proof

The independent audit is justified by the need to validate this
load-bearing source component; the estimates are not claimed as new.
We use the physicists' Hermite polynomials H_j throughout. Their
orthogonality for e^(-x^2) and squared norms 2^j j! sqrt(pi) are the
standard Hermite orthogonality theorem; see NIST DLMF
[18.39(i), equation18.39.14 and the paragraph after18.39.15](https://dlmf.nist.gov/18.39#i).
Mehler's identity is cited from
[DLMF18.18.28](https://dlmf.nist.gov/18.18.E28), with parameter of
modulus less than one. Both sources were inspected on16 November2026.
The complex use of the latter is justified explicitly below.

### Complex specialization and convergence

For |rho|<1 and u,v complex, define

\[
 K(\rho;u,v)=\frac1{\sqrt\pi\sqrt{1-\rho^2}}
 \exp\!\left(\frac{2\rho uv-\rho^2(u^2+v^2)}{1-\rho^2}\right),
\]

using the analytic square-root branch equal to1 at rho=0. This branch
exists throughout the disk since 1-rho^2 has no zero there. K is
holomorphic in rho and entire in each spatial variable. Let b_j(u,v)
be its jth Taylor coefficient in rho at0. These coefficients are entire
in u,v, either by differentiation of the displayed expression or by
Cauchy's coefficient formula on any circle |rho|=s<1.

For real u,v, DLMF18.18.28 and uniqueness of Taylor coefficients give

\[
 b_j(u,v)=\frac{H_j(u)H_j(v)}{2^j j!\sqrt\pi}.
\]

For each fixed real v, the one-variable identity theorem extends this
equality to all complex u. Then, for each fixed complex u, the same
theorem in v extends it to all complex v. This argument identifies the
coefficients before asserting convergence of the complex Hermite sum.

Indeed, for any compact set E of spatial pairs and 0<r<s<1, put
M=sup{|K(rho;u,v)|: |rho|=s, (u,v) in E}, which is finite.
Cauchy's estimate gives |b_j(u,v)|<=M s^(-j) on E. Consequently
the sum of |b_j(u,v)rho^j| is bounded by M/(1-r/s) for |rho|<=r.
Thus the Taylor/Hermite expansion is absolutely and locally uniformly
convergent on the entire required domain and equals K there.

Write h_j=H_j/(2^j j! sqrt(pi))^(1/2). Since H_j has real
coefficients, specializing to rho=r in(0,1), u=z and v=conj(z) yields

\[
 \sum_{j=0}^{\infty}r^j|h_j(z)|^2
 =\frac1{\sqrt\pi\sqrt{1-r^2}}
   \exp\!\left(\frac{2r|z|^2-r^2(z^2+\bar z^2)}{1-r^2}\right).
                                                               \tag{A}
\]

Every term on the left is nonnegative. This uses conjugation and real
Hermite coefficients, not a positivity assertion for arbitrary complex
spatial pairs.

### Finite expansion and the evaluation estimate

The polynomials h_0,...,h_d have successive degrees0,...,d and nonzero
leading coefficients, so they form a basis of this polynomial space.
Expand q=sum_(j=0)^d a_j h_j. Orthogonality gives
||q||_G^2=sum_(j=0)^d |a_j|^2. Finite-dimensional Cauchy-Schwarz and
r^j>=r^d for j<=d imply

\[
 |q(z)|^2\le\|q\|_G^2\sum_{j=0}^d|h_j(z)|^2
 \le r^{-d}\|q\|_G^2\sum_{j=0}^{\infty}r^j|h_j(z)|^2.
                                                               \tag{B}
\]

For z=x+iy, the exponent in(A) is
2r x^2/(1+r)+2r y^2/(1-r). Multiplying(B) by
exp(-Re(z^2))=exp(-x^2+y^2) therefore gives exactly(23).
All norm constants are those of the unnormalized Gaussian measure.

### The scalar constant, including N=1

Since d=2N-1>=1, r_N=d/(d+1). The elementary inequality
log(1+u)<u for u>0 gives

\[
 r_N^{-d}=(1+1/d)^d<e,\qquad
 1-r_N^2=\frac{4N-1}{4N^2}\ge\frac3{4N}.
\]

Hence C_N<2e sqrt(N)/sqrt(3pi)<2sqrt(N). The last strict comparison
uses e<3 and pi>3, and thus e^2<9<3pi. For example e<3 follows
directly from its series: for j>=2, j!>=2^(j-1), strictly for j>=3,
so sum_(j>=2)1/j!<1. No asymptotic estimate in N is used.
At N=1 the exact value is C_1=4/sqrt(3pi), consistent with the bound.
Set y=0 and r=r_N in(23); the remaining exponential in x is at most1.
This proves(24) on the full real axis.

### Fourier estimate and contour limits

Fix q and a frequency y>=0, and put a=y/6. The function
F(z)=q(z)^2 exp(-z^2-iyz) is entire. Choose a finite B with
|q(z)|<=B(1+|z|)^d for all z. Along each vertical side z=+/-R-is,
0<=s<=a, of the rectangle between the real axis and Im(z)=-a,

\[
 |F(z)|\le B^2(1+R+a)^{2d}\exp(-R^2+s^2-ys)
 \le B^2(1+R+a)^{2d}\exp(-R^2+a^2).
\]

The integral over each side is at most a times this bound and tends
to zero as R tends to infinity. On each horizontal line the integrand
is absolutely integrable, being a fixed polynomial times a Gaussian
in its real coordinate. Cauchy's contour theorem followed by these
limits therefore proves

\[
 \int_{\mathbb R}q(x)^2e^{-x^2-iyx}\,dx
 =\int_{\mathbb R}q(x-ia)^2e^{-(x-ia)^2-iy(x-ia)}\,dx.          \tag{C}
\]

When y=0 this is just the original integral, with a=0. There is no
assumption that the vertical-edge limit is uniform over q or y;
each is fixed for this exact identity.

Only now take absolute values. At z=x-ia,
|exp(-iyz)|=exp(-ya) and |exp(-z^2)|=exp(-Re(z^2)). By(23) at r=1/2,

\[
 |F(x-ia)|\le
 \frac{2^d}{\sqrt\pi\sqrt{3/4}}\|q\|_G^2
 \exp(-x^2/3+3a^2-ya).
\]

The exponent independent of x is 3(y/6)^2-y(y/6)=-y^2/12.
Integrating the nonnegative upper bound in(C), and using the Gaussian
integral integral_R exp(-x^2/3) dx=sqrt(3pi), gives

\[
 |\textstyle\int_{\mathbb R}q(x)^2e^{-x^2-iyx}\,dx|
 \le \frac{2^{2N-1}\sqrt{3\pi}}{\sqrt\pi\sqrt{3/4}}
        e^{-y^2/12}\|q\|_G^2
 =4^N e^{-y^2/12}\|q\|_G^2.
\]

For y<0, q(x)^2 exp(-x^2) is real and integrable, so its transforms
at y and -y are conjugate. Their absolute values agree, giving(25).
The zero polynomial satisfies all three inequalities directly. The
proof covers y=0, N=1, arbitrary coefficients and all real frequencies;
no finite numerical sampling is used.

The source bounds pass this audit. The local expansion of the complex
Mehler justification makes its analytic premise explicit; it identifies
no false source inequality. For the eventual parity-restricted use,
q(x)=x^epsilon p(x^2), epsilon in{0,1}, deg(p)<=N-1 indeed has degree
at most2N-1. That degree check alone does not audit Lemma7.7's other
inputs or assemble its lower bound.

## Mathlib

Full matching Mathlib coverage for(23)-(25), their exact constants and
the complex Mehler specialization has not been checked. Availability
is unknown, not asserted absent. The precise standard mathematical
inputs used here are Hermite orthogonality and DLMF18.18.28 above,
finite Cauchy-Schwarz, the holomorphic identity theorem and Cauchy
coefficient/contour theorems, and the ordinary Gaussian integral.
No formal verification or source-computation replay is claimed.
