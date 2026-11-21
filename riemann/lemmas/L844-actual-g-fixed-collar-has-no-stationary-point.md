# Lemma 844: the actual-G angular density has no eventual fixed-collar saddle

## Hypotheses

Use the actual completion in L018 and the interface proved in L775:

\[
G(z)=\frac18\xi\left(\frac12+\frac{\sqrt z}{2}\right)
 =\sum_{n\ge0}\frac{M_{2n}}{8\,4^n(2n)!}z^n.
\]

Evenness makes this an entire function; no branch is needed in its
definition. For every integer r>=2 put k=r-1 and let R_k>0 be the unique
radius with R_k G'(R_k)/G(R_k)=k. L775 proves existence, uniqueness,
G(R_k)>0 and R_k tending to infinity. All coefficient factorials are
retained. Define the holomorphic function in the specified angular
coordinates by

\[
H_r(\boldsymbol\zeta)=
 \prod_{j=1}^{r}\left[e^{-ik\zeta_j}
             \frac{G(R_ke^{i\zeta_j})}{G(R_k)}\right]
 \prod_{1\le i<j\le r}4\sin^2\frac{\zeta_i-\zeta_j}{2},
\qquad
\mathcal C_r=\{\boldsymbol\zeta:
 |\Re\zeta_j|\le\tfrac12,\ |\Im\zeta_j|\le1\text{ for all }j\}.
\]

A nonzero stationary point means H_r!=0 and every complex partial
derivative of H_r vanishes. This is stationarity of this specified
function, not constrained stationarity of its modulus, and not
stationarity of a density after a change of integration measure.
No RH or minor-positivity assumption is made.

## Conclusion

There is an integer r_0 such that, for every r>=r_0, H_r has no nonzero
stationary point in the entire closed collar C_r. In particular, the
proposed eventual family with nonsingular logarithmic Hessian does not
exist in this collar. The threshold is existential, not numerically
certified. This includes both angular and radial boundary faces and all
their intersections.

The conclusion concerns this particular angular density and collar
only. It does not exclude other saddles or other contours, determine
any coefficient-minor sign, or resolve any RH-equivalent positivity
condition. No Hessian estimate is needed once stationarity is excluded.
The separate conceptual audit of 2026-11-06 below accepts this scoped
conclusion without changing its hypotheses or making the onset effective.

## Proof

### Exact stationary equations and a necessary zero sum

Set z_j=R_k exp(i zeta_j) and A(z)=zG'(z)/G(z). At a point where H_r!=0,
all G(z_j) and all sine factors are nonzero. Thus the z_j are nonzero
and pairwise distinct. There is a local analytic logarithm of H_r, and
direct differentiation gives

\[
\partial_{\zeta_j}\log H_r
 =i(A(z_j)-k)+\sum_{l\ne j}\cot\frac{\zeta_j-\zeta_l}{2}.
\tag{1}
\]

For a nonzero sine factor the exact complex identity

\[
\cot\frac{\zeta_j-\zeta_l}{2}
 =i\frac{z_j+z_l}{z_j-z_l}
\]

holds. Since H_r!=0, vanishing of its derivatives is equivalent to
vanishing of the logarithmic derivatives. Dividing (1) by i therefore
gives, at any such stationary point,

\[
A(z_j)-k+\sum_{l\ne j}\frac{z_j+z_l}{z_j-z_l}=0
\quad(1\le j\le r).                                      \tag{2}
\]

Multiply the jth equation by z_j and sum. Each unordered pair contributes

\[
z_i\frac{z_i+z_j}{z_i-z_j}
+z_j\frac{z_j+z_i}{z_j-z_i}=z_i+z_j.
\]

Every z_j occurs in r-1 pairs, so (2) implies the exact identity

\[
\sum_{j=1}^{r}z_jA(z_j)+(r-1-k)\sum_{j=1}^{r}z_j=0.
\]

The stipulated k=r-1 consequently forces

\[
\boxed{\ \sum_{j=1}^{r}z_j A(z_j)=0.\ }                    \tag{3}
\]

No integration or asymptotic approximation was used. As a check of the
coordinate convention, with m=r(r-1)/2 the same function is exactly

\[
H_r=(-1)^m\frac{R_k^{kr}}{G(R_k)^r}
       \prod_{i<j}(z_i-z_j)^2
       \prod_j G(z_j)z_j^{-(k+r-1)}.                       \tag{4}
\]

Here 4 sin^2((zeta_i-zeta_j)/2)=-(z_i-z_j)^2/(z_i z_j).
Since partial_(zeta_j)=i z_j partial_(z_j), (4) reproduces (2).
The Jacobian of an integration measure is not multiplied into (4):
doing so would change the function whose stationary points were asked
for. The argument makes no coordinate-invariant claim about saddles.

### Uniform actual-G logarithmic derivative in the closed sector

We prove a quantitative-sign estimate for |arg z|<=1/2 and sufficiently
large |z|. In this sector choose the principal square root q=sqrt(z),
write rho=|q| and theta=arg z, and put s=(1+q)/2. Then

\[
|\arg q|\le\tfrac14,\qquad
\sigma:=\Re s\ge\tfrac12+\tfrac\rho2\cos(\tfrac14).
\tag{5}
\]

In particular sigma>=2 eventually, uniformly in the closed sector.
Here G is nonzero: by L018 it is a nonzero constant times
s(s-1)pi^(-s/2)Gamma(s/2)zeta(s). The elementary factors are nonzero,
Gamma is nonzero on the right half-plane
([NIST DLMF 5.2(i)](https://dlmf.nist.gov/5.2#i)), and the following elementary
Dirichlet-series estimate also verifies that zeta(s) is nonzero here:

\[
|\zeta(s)-1|\le\sum_{n\ge2}n^{-2}
 \le\tfrac14+\int_2^\infty x^{-2}\,dx=\tfrac34,
\qquad |1/\zeta(s)|\le4.                                 \tag{6}
\]

The defining Dirichlet series ([NIST DLMF 25.2.1](https://dlmf.nist.gov/25.2.E1))
and its derivative converge locally
uniformly for Re(s)>1. For example, on Re(s)>=1+epsilon the derivative
terms are dominated by (log n)n^(-1-epsilon), a convergent series.
Let B=sum_(n>=2)(log n)/n^2<infinity. For sigma>=2, differentiating that
series and using (6) gives

\[
\left|\frac{\zeta'}{\zeta}(s)\right|
 \le4\sum_{n\ge2}(\log n)n^{-\sigma}
 \le4B\,2^{2-\sigma}.                                    \tag{7}
\]

Thus rho times this quantity tends uniformly to zero by (5).
The Dirichlet series and nonvanishing of Gamma are the standard inputs
already recorded in `foundations/notation-and-inputs.md`.

For Gamma, import the complex digamma expansion, rather than
differentiating an unqualified real-axis error term:

\[
\psi(w)=\operatorname{Log}w-\frac1{2w}+O(|w|^{-2})
\quad (|w|\longrightarrow\infty,\ |\arg w|\le\pi-\delta),
\tag{8}
\]

with any fixed delta>0. This is [NIST DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2),
with the sector condition in [Section 5.11(i)](https://dlmf.nist.gov/5.11#i)
and uniform complex remainder bounds in
[Section 5.11(ii)](https://dlmf.nist.gov/5.11#ii), inspected 2026-11-06.
These are supporting standard results, not a cited saddle-exclusion
theorem. For w=s/2=(1+q)/4, adding the positive real number 1 to q
decreases its absolute argument, so |arg w|<=1/4. Moreover
(rho-1)/4<=|w|<=(rho+1)/4. Thus (8) applies uniformly up to the sector
boundaries. Its complex remainder can also be obtained from the
analytic Stirling remainder already recorded in the foundations by
Cauchy estimates on disks inside a larger sector; no derivative bound
from Katkova's auxiliary generic-C estimates is used.

Taking the logarithmic derivative of L018's exact product and using
z ds/dz=q/4 yields

\[
A(z)=\frac q4\left[
 \frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s)\right].          \tag{9}
\]

For rho>=2, both |s| and |s-1| are at least (rho-1)/2.
Substitution of (8) into (9), together with (7), therefore gives

\[
A(z)=\frac q8\operatorname{Log}\frac{s}{2\pi}+O(1)
     =\frac q8\operatorname{Log}\frac{q}{4\pi}+O(1).       \tag{10}
\]

All O(1) constants are uniform on this fixed closed sector. For the
last equality, s=(q/2)(1+1/q), the principal logarithms are compatible
there, and |Log(1+1/q)|<=2/rho for rho>=2, by its absolutely convergent
power series. The rational terms in (9) times q are bounded; the
digamma remainder times q is O(1/rho); and the zeta term times q tends
uniformly to zero. This supplies each part of the asserted uniform
error. Consequently there exist constants C>=0 and rho_0 such that

\[
\left|A(z)-\frac q8\operatorname{Log}\frac{q}{4\pi}\right|
 \le C\quad(\rho\ge\rho_0,\ |\arg z|\le\tfrac12).       \tag{11}
\]

Let c_0=cos(3/4)>0, and also require rho>=4pi. Since
zq=rho^3 exp(3i theta/2), (11) implies

\[
\begin{split}
\Re(zA(z))
&\ge\frac{\rho^3}{8}
  \left[\log\frac\rho{4\pi}\cos\frac{3\theta}{2}
        -\frac\theta2\sin\frac{3\theta}{2}\right]-C\rho^2\\
&\ge\frac{\rho^3}{8}
  \left[c_0\log\frac\rho{4\pi}-\frac14-\frac{8C}{\rho}\right].
\end{split}                                               \tag{12}
\]

Here |theta|<=1/2, so cos(3theta/2)>=c_0 and
|(theta/2)sin(3theta/2)|<=1/4, including equality at either angular
boundary where relevant. Choose rho_*>=max(rho_0,4pi,1) so large that
for all rho>=rho_*,

\[
\frac{c_0}{2}\log\rho
 \ge c_0\log(4\pi)+\frac14+\frac{8C}{\rho}.              \tag{13}
\]

Such a common threshold exists because the left side increases without
bound and the right side decreases to a finite value. Equations
(12)–(13) prove the strict uniform bound

\[
\boxed{\ \Re(zA(z))\ge\frac{c_0}{16}\rho^3\log\rho>0
       \quad(\rho\ge\rho_*,\ |\arg z|\le\tfrac12).\ }   \tag{14}
\]

### Application to every order beyond one threshold

For z_j=R_k exp(i zeta_j) in the specified collar,

\[
|\arg z_j|=|\Re\zeta_j|\le\tfrac12,
\qquad R_k/e\le|z_j|\le eR_k.
\]

The equality of arguments uses that Re(zeta_j) lies in [-1/2,1/2],
inside the principal-argument interval. By L775, R_k tends to infinity.
There is thus one r_0 for which R_(r-1)/e>=rho_*^2 whenever r>=r_0.
At all these orders, (14) applies to every coordinate, including the
closed radial boundaries. If H_r!=0 and were stationary, (3) would
hold, whereas (14) gives

\[
\Re\sum_{j=1}^{r}z_jA(z_j)
 \ge\frac{c_0}{16}\sum_{j=1}^{r}|z_j|^{3/2}\log\sqrt{|z_j|}
 >0,
\]

a contradiction. Collisions or zeros of H_r cannot evade the argument:
they are expressly excluded by the required H_r!=0 condition. Points
on a boundary still require all unconstrained complex partials to
vanish, so no boundary criticality exception is relevant. This proves
the conclusion for every sufficiently large order, without finite
sampling, Hessian assumptions or dimension-dependent error bounds. ∎

The prior EXPLORE assessment covered this exact collar question and
the necessary complex derivative estimates. It did not identify a
matching exclusion theorem; the local result is not certified novel.
The standard gamma and Dirichlet-series inputs are imported or
specialized above. L775's mass-complement obstruction and the earlier
automatic-contour source stop are preserved and are not additional
mathematical premises of this exclusion. No determinant identity or
positivity criterion is reproved.

### Independent conceptual audit, 2026-11-06

The approved audit reproduces the conclusion; no load-bearing defect
or strengthened theorem is claimed. The standard inputs are those in
the proof and in L018/L775, with the unchanged source coverage recorded
in `drafts/literature/2026-11-06-actual-g-fixed-collar-exclusion-audit.md`.
The exact completion also agrees with
[NIST DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4).

The coordinate check is essential. Directly differentiating (4) with
respect to z_j gives

\[
\partial_{z_j}\log H_r
 =\frac{G'(z_j)}{G(z_j)}-\frac{k+r-1}{z_j}
       +2\sum_{l\ne j}\frac1{z_j-z_l}.
\]

Multiplication by z_j gives (2), since
2z_j/(z_j-z_l)=1+(z_j+z_l)/(z_j-z_l). Multiplication of (2) by z_j
then gives (3), with each unordered pair contributing z_i+z_j.
Thus the two coordinate calculations agree, including the sign and
the term r-1-k. Since i z_j is nonzero, vanishing of the z and angular
partials of this same function is equivalent. Multiplying the function
by the differential-form Jacobian would instead change the problem.
Local logarithms exist in a sufficiently small polydisc where H_r is
nonzero; a global logarithm is unnecessary.

For a detailed check of the uniform O(1) in (10), let K be a constant
such that the digamma remainder in (8) has modulus at most K/|w|^2
for |arg w|<=1/4 and sufficiently large |w|. This follows from the
fixed closed-sector remainder statement, not from differentiating
a real-variable estimate. Take rho>=2 large enough that w=(1+q)/4
lies in this range and sigma>=2. In order, the rational terms in (9),
the -1/(2w) digamma term, its remainder, the logarithm replacement and
the zeta term are bounded by

\[
\frac{\rho}{\rho-1},\quad
\frac{\rho}{4(\rho-1)},\quad
\frac{2K\rho}{(\rho-1)^2},\quad
\frac14,\quad B\rho\,2^{2-\sigma}.
\]

Consequently the total error in (10) is at most

\[
\frac{11}{4}+\frac{8K}{\rho}
 +B\rho\,2^{3/2-\rho\cos(1/4)/2}.
\]

This is bounded independently of the point, r and k. In the fourth
term the logarithms are compatible because q, 1+q and their positive
real dilates remain in the right half-plane; the principal power-series
logarithm of 1+1/q gives their difference. The last term uses the full
absolutely convergent differentiated Dirichlet series, and tends to
zero uniformly. The estimate (6), in particular its positive lower
bound 1/4 for |zeta(s)|, justifies division throughout this sector.
The factors s and s-1 and Gamma(s/2) are also nonzero there.

For the sign test, multiplication by z costs C rho^2 while the main
term has order rho^3 log rho. The factor cos(3 theta/2) is bounded
below by cos(3/4)>0 on the entire closed angular interval. The
subtracted term has modulus at most 1/4. In (13) the left side is
increasing and unbounded, and the right side is nonincreasing and
bounded. Thus a single rho_* works for every later rho, not just a
sequence. As rho_*>=4pi>1, the lower bound (14) is strictly positive.

L775's scalar-radius argument uses the strictly positive variance of
its coefficient distribution and the backward secant of F(t), so it
does not differentiate an asymptotic error. Its conclusion R_k->infinity
is enough here. On the lower radial face Im(zeta_j)=1 one still has
sqrt(|z_j|)=sqrt(R_k/e)->infinity; the other face only increases this
modulus. Choosing one r_0 for all r>=r_0 therefore applies (14)
simultaneously to every coordinate, even as their number grows.
No separation bound or uniform logarithmic Hessian is needed: the
pair cancellations are exact at distinct points. Collision points,
possibly stationary zeros of H_r, are outside the stated nonzero
premise. The boundaries use unconstrained complex partials throughout.

The audit accepts the fixed-collar route exclusion only. No numerical
onset, critical point outside this collar, contour participation,
signed remainder, minor sign or RH conclusion follows. This is local
verification of the existing argument, not a novelty claim.

## Mathlib

Full matching coverage is unchecked and remains unknown. No Mathlib
theorem is used to certify the exclusion. General complex derivatives,
finite sums and special-function facts would be supporting results,
not a full matching theorem. Unknown availability is not evidence of
absence.
