# Lemma 899: normalized Xi-defect measure is Lipschitz in the squared height

## Hypotheses

Use the actual theta kernel K of L019, with the full-line normalization
Phi(u)=K(|u|)/2 used for Xi in L898. For spatial variables u,w in R,
put p=u+w and, for 0<=y<=1/2, define

\[
 W_y(u,w)=p^2\operatorname{sinhc}(yp)\Phi(u)\Phi(w),\qquad
 A_0(y)=\iint_{\mathbb R^2}W_y(u,w)\,du\,dw,
\]

where sinhc(z)=sinh(z)/z for z!=0 and sinhc(0)=1. The second spatial
variable is named w to distinguish it from a second height v.
Write nu_y for the measure with Lebesgue density W_y/A_0(y).
L898 establishes 0<A_0(0)<=A_0(y)<=A_0(1/2)<infinity and the
polynomial-exponential domination for these actual theta densities.

## Conclusion

For all 0<=v,y<=1/2,

\[
 \iint_{\mathbb R^2}
 \left|\frac{W_y}{A_0(y)}-\frac{W_v}{A_0(v)}\right|\,du\,dw
 \leq M|y^2-v^2|,
 \tag{1}
\]

with the following explicit finite positive theta-integral constant:

\[
 \begin{split}
 a&=A_0(0)=\iint p^2\Phi(u)\Phi(w)\,du\,dw,\\
 Q&=\iint p^4\operatorname{sinhc}(p/2)\Phi(u)\Phi(w)\,du\,dw,\\
 M&=\frac{Q}{3a}\in(0,\infty).
 \end{split}
 \tag{2}
\]

All integrals in (2) are over R². No numerical evaluation or optimality
of M is claimed. This is a specialization of known normalization
stability; the general stability theorem is imported, not reproved.
The bound includes y=0, v=0 and the coincident endpoints. It is independent
of a polynomial truncation degree. It asserts no sign for any Fourier
transform, no independent positive reference margin, and no resolution
of L030–L032/C032a.

## Proof

### Imported quantitative stability and scalar formulas

Björn Sprungk, *On the Local Lipschitz Stability of Bayesian Inverse
Problems*, Inverse Problems 36 (2020), 055015,
[arXiv:1906.07120v3, Theorem 8, printed p.10](https://arxiv.org/pdf/1906.07120v3#page=10),
uses the following normalization convention. On a Polish space E with
probability measure mu, let f,g be measurable elements of L1(mu), with
essinf_mu f=0, and 0<Z_f,Z_g<infinity, where Z_h=integral exp(-h) dmu.
For dmu_h=exp(-h)dmu/Z_h, the theorem gives

\[
 d_{\rm TV}(\mu_f,\mu_g)
 \leq\frac{\exp(-[\operatorname{essinf}_\mu g]_-)}{Z_f}
       \|f-g\|_{L^1(\mu)},\qquad [b]_-:=\min(0,b).
 \tag{3}
\]

Here total variation is one half the full L1 density distance.
The source version is dated 22 January 2020; its Sections 2–3 and
Appendix A (normalization inequality preceding equation (13)) specify
the setting and convention. Only the nonnegative-potential case of (3)
will be needed. Verifying that case for this theta reference, including
essential infima and finite normalizers, is the specialization below.

The scalar inputs are the infinite product

\[
 \sinh z=z\prod_{n=1}^\infty
                  \left(1+\frac{z^2}{\pi^2 n^2}\right)
 \tag{4}
\]

from [NIST DLMF 4.36.1](https://dlmf.nist.gov/4.36.E1), the entire
sinh series from [DLMF 4.33.1](https://dlmf.nist.gov/4.33.E1), and
sum_(n>=1) n^(-2)=pi²/6 from
[DLMF 25.6.1](https://dlmf.nist.gov/25.6.E1). The prior source assessment
inspected DLMF version 1.2.8, release 15 September 2026. That assessment's
coverage is reused; no additional theorem or source version is required.
In particular the coth formula, which excludes zero, is not applied at zero.

### Scalar comparison including zero

Fix a real p and let 0<=t<=1/4. Define
H_p(t)=log(sinhc(p sqrt(t))). This is real because sinhc is positive
on the real line. Dividing (4) for nonzero argument and using the
removable value supplied by the sinh series at zero gives

\[
 H_p(t)=\sum_{n=1}^\infty
        \log\left(1+\frac{t p^2}{\pi^2 n^2}\right).
 \tag{5}
\]

To justify the logarithmic limit, each summand is nonnegative and at
most t p²/(pi² n²). For fixed p these upper bounds are summable uniformly
on 0<=t<=1/4, so the sums of logarithms converge to the logarithm of the
positive product. At t=0 or p=0 both sides are zero. Thus (5) does not
divide by zero or infer a uniform statement from pointwise analyticity.

For alpha,beta>=0 the mean value theorem applied to log(1+x) gives
|log(1+alpha)-log(1+beta)|<=|alpha-beta|. Applying this to finite
partial sums in (5), and then taking their convergent limits, gives

\[
 |H_p(t)-H_p(s)|
 \leq\frac{p^2}{\pi^2}|t-s|\sum_{n=1}^\infty\frac1{n^2}
 =\frac{p^2}{6}|t-s|\quad(0\leq s,t\leq1/4).
 \tag{6}
\]

The summands in (5) also show that H_p is nondecreasing. These facts
hold for each real p; no derivative is interchanged with a theta integral.

### Reference measure and every potential hypothesis

Set B=A_0(1/2) and take E=R² with its Euclidean metric and Borel
probability measure mu=nu_(1/2). It is a Polish space. Define everywhere

\[
 \Psi_y(u,w)=\log\frac{\operatorname{sinhc}(p/2)}
                              {\operatorname{sinhc}(yp)}
             =H_p(1/4)-H_p(y^2).
 \tag{7}
\]

The scalar functions and their positive quotient are continuous,
including at p=0, so Psi_y is measurable. Equations (5)–(6) give

\[
 0\leq\Psi_y\leq\frac{p^2}{24},\qquad
 |\Psi_y-\Psi_v|\leq\frac{p^2}{6}|y^2-v^2|.
 \tag{8}
\]

The needed second moment of p under mu is Q/B. Here is an explicit
finiteness check. Comparing the nonnegative even-power series, using
(2n+1)!>=(2n)!, gives sinhc(p/2)<=cosh(p/2)<=exp(|p|/2). Set
J_j=integral_R |u|^j exp(|u|/2) Phi(u) du for 0<=j<=4.
Every J_j is finite by L019's theta decay. Expanding
(|u|+|w|)^4 and using nonnegative Fubini gives

\[
 0<Q\leq 2J_4J_0+8J_3J_1+6J_2^2<\infty.
 \tag{9}
\]

Indeed |p|<=|u|+|w|, so the product integrand for the right side
dominates the integrand for Q. Positivity follows from Phi>0 and
any open rectangle avoiding p=0. Thus (8) puts every Psi_y in L1(mu),
and also provides an integrable majorant for its displayed differences.

It remains to establish an essential, not merely pointwise, infimum.
Given epsilon>0 choose delta>0 with delta²/24<epsilon. On the open
rectangle delta/4<u<delta/2, delta/4<w<delta/2 one has
0<p<delta, so Psi_y<epsilon by (8). The density W_(1/2)/B is strictly
positive throughout this positive-Lebesgue-measure rectangle, since
Phi>0 and p!=0. Hence the rectangle has positive mu measure. Since
Psi_y>=0 everywhere, essinf_mu Psi_y=0 for every y, including both
endpoints. No mass is assigned to the null line p=0.

The exact likelihood identity is

\[
 e^{-\Psi_y} W_{1/2}=W_y.
 \tag{10}
\]

It holds also on p=0, where both sides vanish. Consequently

\[
 Z_y:=\int e^{-\Psi_y}\,d\mu=\frac{A_0(y)}B,
 \qquad \frac aB\leq Z_y\leq1,
 \qquad \mu_{\Psi_y}=\nu_y.
 \tag{11}
\]

The lower bound uses L898's established raw-mass monotonicity and a>0;
it does not use positivity of an oscillatory integral. All hypotheses
of (3) now hold for f=Psi_y and g=Psi_v.

### Full-L1 normalization and the constant

The negative-essential-infimum factor in (3) is one. From (8) and
the definition of Q,

\[
 \|\Psi_y-\Psi_v\|_{L^1(\mu)}
 \leq\frac{Q}{6B}|y^2-v^2|.
\]

Since both normalized measures have Lebesgue densities, their full-L1
distance is exactly 2d_TV(nu_y,nu_v). Combining (3) and (11) gives

\[
 \begin{split}
 \iint\left|\frac{W_y}{A_0(y)}-\frac{W_v}{A_0(v)}\right|
 &=2d_{\rm TV}(\nu_y,\nu_v)\\
 &\leq 2\frac{B}{A_0(y)}\frac{Q}{6B}|y^2-v^2|\\
 &\leq\frac{Q}{3a}|y^2-v^2|.
 \end{split}
\]

This proves (1)–(2). Although the invocation of (3) chooses y as its
first potential, the final bound is symmetric in the two heights.
All endpoint cases are already included in the argument. ∎

The possible downstream use is absolute interpolation control for the
same normalized measure. Turning it into a sign statement still requires
an independently proved reference margin larger than the interpolation
error. No such margin, all-height relative estimate, or implication
from a negative lower polynomial to a negative Xi defect is asserted.
L898's fixed cross-endpoint obstruction and L312's qualified ordering
failure are comparisons only, and are not negated by this norm estimate.

### Audit of the closed-square bound (2026-11-08, step113)

The specialization above passes the separately approved audit. In (5),
the uniform summable majorant is p²/(4pi²n²) for each fixed real p;
no uniformity in unbounded p is needed there. Equation (6) is a
pointwise inequality for every p, whose later integration is licensed
by the separate finite Q estimate (9). Thus neither the product limit
nor the zero endpoint hides an interchange with the spatial integral.

For completeness, the integrals J_j have no local singularity: L019's
positive series and its bound give bounded Phi on every compact
interval, including zero. At infinity its faster-than-any-exponential
decay absorbs |u|^j exp(|u|/2). The binomial coefficients in (9) are
1,4,6,4,1; pairing the symmetric terms gives exactly 2,8,6.
The rectangle argument for the essential infimum works for each y
with the same delta, including y=0; at y=1/2 the potential is identically
zero. It uses strictly positive reference density off p=0, not reference
mass on that null line.

Finally (10) identifies the normalized measures exactly, not just up
to a parameter-dependent factor: their Lebesgue densities are W_y/A_0(y).
Sprungk's first-potential essential infimum is zero and both potentials
are nonnegative elements of L1(mu). The coefficient is consequently
2(B/A_0(y))(Q/(6B))=Q/(3A_0(y))<=Q/(3a), with the initial 2 required
by the source's half-L1 convention. This verifies the stated M on the
entire closed square, including its diagonal and corners. No stronger
constant, sign assertion, or independent positive margin was audited.
The direct mathematical inputs remain L019 and L898, with L020's Xi
normalization already carried by L898; no DAG change is required.

## Mathlib

Full matching coverage has not been checked; availability is unknown.
No supporting Mathlib theorem names were verified. The cited analytic
stability theorem and DLMF identities are mathematical inputs, not
formal proof certificates. The local specialization passed the informal
hypothesis, endpoint and constant audit recorded above; no Mathlib
coverage was checked by that audit.
