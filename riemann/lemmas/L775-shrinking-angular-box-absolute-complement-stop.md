# Lemma 775: shrinking angular box cannot pay the full absolute complement

## Hypotheses

Use the actual completion of L018 and positive moments of L021. Set

\[
 G(z)=\frac18\xi\left(\frac12+\frac{\sqrt z}{2}\right)
     =\sum_{n\ge0}a_nz^n,\qquad
 a_n=\frac{M_{2n}}{8\,4^n(2n)!}>0.
\]

The square-root notation defines an entire function by evenness, not a
choice of a multivalued function. Write
D_(r,k)=det[a_(k+j-i)]_(i,j=0)^(r-1); when k=r-1 all indices are nonnegative.
For each integer r>=2 put k=r-1, and
let R_k>0 solve R_k G'(R_k)/G(R_k)=k; existence and uniqueness are proved
below. For theta in [-pi,pi]^r define

\[
 w_r(\theta)=\prod_{j=1}^r\frac{|G(R_ke^{i\theta_j})|}{G(R_k)}
       \prod_{1\le i<j\le r}|e^{i\theta_i}-e^{i\theta_j}|^2,
 \qquad B_r=[-k^{-2/5},k^{-2/5}]^r.
\]

Write C_in for the Lebesgue integral of w_r on B_r, and C_out for its
integral on [-pi,pi]^r minus B_r. All logarithms are natural. No RH,
coefficient-minor sign, or global zero-location hypothesis is assumed.

## Conclusion

The radius exists uniquely for every k>0, and 0<C_in<infinity and
C_out<infinity. There is an existential integer r_0 such that for r>=r_0,

\[
 \begin{split}
 C_{\rm in}&\le (2k^{-2/5})^{r^2},\\
 C_{\rm out}&\ge
 \exp\bigl(-(6+\log(4\pi))r(r-1)-r\log(8r)\bigr),                 \tag{1}\\
 \log\frac{C_{\rm out}}{C_{\rm in}}
 &\ge \frac25r^2\log(r-1)-r^2\log2
       -(6+\log(4\pi))r(r-1)-r\log(8r).                           \tag{2}
 \end{split}
\]

Consequently

\[
 \liminf_{r\to\infty}
 \frac{\log(C_{\rm out}/C_{\rm in})}{r^2\log r}\ge\frac25,
 \qquad
 \frac{C_{\rm out}}{C_{\rm in}}
       \ge \exp(r^2\log r/10)\quad\hbox{eventually}.               \tag{3}
\]

The conclusion rules out paying the *entire complement modulus* from
this core in the known signed angular formula. It does not bound the
modulus of the signed complement integral from below, determine any
D_(r,r-1) sign, or exclude other cores, cancellations or contours.
The onset is not made effective; no finite-r certificate is claimed.

## Proof

### Imported sector input and the exact specialization

Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
[arXiv:math/0505174v1, Lemma 4(c), pp.11–12](https://arxiv.org/pdf/math/0505174v1#page=11),
gives, for xi_1(z)=xi(1/2+sqrt(z)),

\[
 \begin{split}
 \log|\xi_1(xe^{i\theta})|
 ={}&\tfrac14\sqrt{x}\log x\cos(\theta/2)
 -\tfrac14\sqrt{x}\,\theta\sin(\theta/2)\\
 &-\tfrac12\sqrt{x}(\log2+1+\log\pi)\cos(\theta/2)
 +O(\log x).                                                    \tag{4}
 \end{split}
\]

Only uniformity on |theta|<=1/2, as x tends to infinity, is used.
The source's proof obtains (4) from the absolutely convergent zeta Euler
product in Re(s)>=2 and sectorial Stirling's formula. To check uniform
applicability here, s=1/2+sqrt(x) exp(i theta/2) has
Re(s)>=1/2+sqrt(x) cos(1/4), hence eventually Re(s)>=2 uniformly;
s/2 stays in |arg(s/2)|<=1/4 and tends uniformly to infinity. Thus the
zeta upper and reciprocal bounds and Stirling remainder have constants
independent of theta. The elementary factors s(s-1) in L018 are nonzero
there and also have uniform logarithmic remainders. This checks the
compact sector specialization of the cited proof, without importing the
source's auxiliary generic-C derivative estimates or fixed-order sign
theorems. The source input and identity below are known results.

Retain the dilation exactly: G(z)=xi_1(z/4)/8. Substituting x=e^t/4 in
(4), and absorbing the fixed normalization, gives

\[
 \log|G(e^{t+i\theta})|
   =\tfrac18 e^{t/2}t\cos(\theta/2)+O(e^{t/2}),\qquad
       |\theta|\le\tfrac12,\quad t\to\infty,                    \tag{5}
\]

with one uniform constant. In particular the left side is nonnegative
for all sufficiently large t, uniformly on A=[1/4,1/2]. This follows
because cos(theta/2)>=cos(1/4)>0 and t tends to infinity.
Explicitly, if the absolute remainder in (5) is at most C e^(t/2)
for t>=T, take t>=max(T,8C/cos(1/4)). No lower bound near an unknown
zero is assumed: the cited zero-free compact sector supplies (5).

### Scalar radius and an order-uniform lower weight on A

L018/L021 give the expansion in the hypotheses by substituting
z=-i sqrt(w)/2 into Xi(z); all its a_n are strictly positive.
Let F(t)=log G(e^t) and p_n(t)=a_n e^(nt)/G(e^t). Then

\[
 F'(t)=\sum_{n\ge0}n p_n(t),\qquad
 F''(t)=\sum_{n\ge0}(n-F'(t))^2p_n(t)>0.                          \tag{6}
\]

These differentiations are legitimate: the entire power series and its
first two derivatives converge locally uniformly; equivalently, for
fixed positive R, the factors n^2 in sum n^2 a_n R^n are dominated
using convergence at 2R. Strict variance positivity follows from
p_0,p_1>0. Also F'(t) tends to zero as t tends to minus infinity,
since G(R)=a_0+a_1R+O(R^2) near R=0.

At theta=0, (5) gives

\[
 F(t)=\tfrac18e^{t/2}t+O(e^{t/2}),\quad
 H(t):=F(t)-F(t-1)
   =\tfrac18(1-e^{-1/2})e^{t/2}t+O(e^{t/2}).                     \tag{7}
\]

Convexity gives F'(t)>=H(t), so F'(t) tends to infinity. By continuity
and strict increase, F'(t_k)=k has exactly one real solution for each
k>0, with t_k tending to infinity as k does. Thus R_k=e^(t_k) is the
required radius. This verifies the specialized saddle construction of
[Katkova, equation (33), p.14](https://arxiv.org/pdf/math/0505174v1#page=14);
no asymptotic error has been differentiated.

Moreover (7) shows that F(t)/H(t) tends to
1/(1-e^(-1/2))<3: indeed e^(1/2)>1+1/2. For sufficiently large t,
both F,H are positive and F(t)<=4H(t)<=4F'(t). Combining this with
the uniform nonnegative lower bound from (5), at t=t_k, proves

\[
 \frac{|G(R_ke^{i\theta})|}{G(R_k)}\ge e^{-4k}
       \quad(\theta\in A),                                    \tag{8}
\]

for every sufficiently large k, with one onset independent of theta
and of r. This is a coarse modulus estimate only.
To make the quantifiers explicit, choose a single T_* beyond both the
uniform-sector threshold and the threshold for 0<F(t)<=4H(t).
Since t_k tends to infinity, there is a K_* such that t_k>=T_* for
all k>=K_*. Substitution k=r-1 then uses this same K_* for every
coordinate; it does not require an r-dependent analytic remainder.

### Inside upper bound and positivity

Positive coefficients and absolute convergence imply
|G(R exp(i theta))|<=G(R) for every R>0 and real theta. For
delta=k^(-2/5), each chord in B_r has length at most
|theta_i-theta_j|<=2delta. There are r(r-1)/2 squared chords and
the box has volume (2delta)^r. Therefore

\[
 C_{\rm in}\le (2\delta)^{r(r-1)}(2\delta)^r
                   =(2\delta)^{r^2}.                            \tag{9}
\]

The integrand is continuous on the compact full cube, so both integrals
are finite. Since G(R_k)>0, it stays nonzero on a sufficiently small
angular interval around zero. Choose r distinct angles in that interval
and in the interior of B_r. At that configuration w_r>0; continuity
gives an open neighborhood of positive measure in B_r on which w_r>0.
Hence C_in>0, including all finite r>=2.

### A positive-volume outside region retaining all pair distances

For j=1,...,r take the interval

\[
 I_j=\left[\frac14+\frac{j-1/2}{4r}-\frac1{16r},\,
           \frac14+\frac{j-1/2}{4r}+\frac1{16r}\right].
\]

Each lies strictly inside A, has length 1/(8r), and they are disjoint.
For sufficiently large r, delta<1/4, so Q_r=product_j I_j is contained
in the complement of B_r and has volume (8r)^(-r). For theta in Q_r
and i<j, with d=j-i, one has

\[
 0<\frac{d}{8r}\le\theta_j-\theta_i<\frac14,
 \qquad
 |e^{i\theta_j}-e^{i\theta_i}|
 =2\sin((\theta_j-\theta_i)/2)\ge\frac{d}{4\pi r}.              \tag{10}
\]

The first lower bound follows from
d/(4r)-1/(8r)>=(d/(8r)); the chord bound uses
sin u>=2u/pi for 0<=u<=pi/2. Thus, pointwise on the entire Q_r,

\[
 \prod_{i<j}|e^{i\theta_j}-e^{i\theta_i}|^2
 \ge (4\pi)^{-r(r-1)}
           \prod_{d=1}^{r-1}(d/r)^{2(r-d)}.                      \tag{11}
\]

To bound the whole product, rather than substituting its smallest
spacing, note that log(r/d)>=0 and

\[
 \begin{split}
 \sum_{d=1}^{r-1}(r-d)\log(r/d)
 &\le r\sum_{d=1}^{r-1}\log(r/d)
   =r(r\log r-\log(r!))\le r(r-1).                              \tag{12}
 \end{split}
\]

The last inequality follows from
log(r!)>=integral_1^r log x dx=r log r-r+1, by monotonicity of log.
Consequently (11) is at least
exp(-(log(4pi)+2)r(r-1)). The r factors in (8) contribute at least
exp(-4kr). Integrating this bound over Q_r, including its full volume,
and using k=r-1 proves the outside estimate (1). Permuting Q_r would
give additional mass but is not needed or counted.

### Threshold and precise implication for the sign certificate

Divide the outside lower bound by the positive inside upper bound (9)
and take logarithms to obtain (2). Its right side divided by
r^2 log r tends to 2/5, since log(r-1)/log r tends to 1 and all the
remaining terms have smaller order on this scale. Since 2/5>1/10,
(3) follows with an existential onset. All bounds concern actual G;
there is no generic replacement weight or point-mass approximation.

For clarity, the known signed integrand is

\[
 h_r(\theta)=\prod_j\left[e^{-ik\theta_j}
                      \frac{G(R_ke^{i\theta_j})}{G(R_k)}\right]
                    \prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2.
\]

[Katkova, Lemmas 1–2, (10)–(13), pp.7–8](https://arxiv.org/pdf/math/0505174v1#page=7)
applies because G is entire with nonnegative coefficients, R_k>0,
k>=0 and r>=1; it identifies the full integral as
r!(2pi)^r R_k^(kr) D_(r,k)/G(R_k)^r. This identity is cited, not
reproved. Pointwise |h_r|=w_r. If J_in=Re integral_(B_r) h_r, then
J_in<=C_in<C_out eventually. Thus a certificate of positivity based
on J_in exceeding the full C_out is impossible, even if the core
could be shown positive. However |integral_(complement) h_r| can be
far smaller than C_out, and its real part may be positive. No claim
about that signed integral, the minor sign or RH follows. ∎

This is the bounded test approved before step420. The source assessment
did not identify a matching growing-order mass bound; the local proof
is not a claim of certified originality. Earlier coefficient/real-moment
stops are comparisons only and are not mathematical inputs here.

### Conceptual audit, 2026-11-04, step422

The approved independent audit found no load-bearing error. The
normalization, entire-series differentiations, strict variance,
backward-secant argument and fixed-sector specialization were checked
against L018/L021 and the already inspected Katkova inputs. The explicit
uniform threshold above clarifies the existing proof; it does not make
the eventual dimension bound effective or strengthen its conclusion.

For the positive-volume check, the smallest left endpoint is
1/4+1/(16r) and the largest right endpoint is 1/2-1/(16r).
Thus all intervals lie in A; k>32 suffices for delta<1/4. Their lengths
are exactly 1/(8r), not point samples. For separation d, the smallest
angle difference is (2d-1)/(8r)>=d/(8r); its multiplicity is r-d.
Consequently the squared-distance product has logarithmic cost at most
[log(4pi)+2]r(r-1), as in (11)–(12), with no missing r^2 log r cost.
Combining the r separate factors e^(-4k) and the full box volume
recovers exactly (1). This check does not use disjoint permutations
of Q_r or count their volume twice.

The limit comparison checks the achieved 2/5 against the required 1/10;
it supplies an existential common onset after increasing the thresholds
above. Positive coefficients bound the inside mass, not its signed
contribution from below. The exact Katkova integral has the factor
r!(2pi)^r R_k^(kr)/G(R_k)^r with a positive sign; transposing the
coefficient convention does not change its determinant. Finally
Re integral_(B_r) h_r<=C_in<C_out excludes only a certificate paying
the full complement modulus. It supplies no lower bound on the modulus
of the signed complement and no minor-sign conclusion. The canonical
input set remains L018/L021; no additional lemma is used.

## Mathlib

Full matching coverage has not been checked and remains unknown. No
Mathlib result is used as a premise or completion certificate. The cited
analytic inputs are imported from the primary source above; generic
power-series, convexity, integral and finite-product facts do not by
themselves supply this actual-Xi growing-order comparison.
