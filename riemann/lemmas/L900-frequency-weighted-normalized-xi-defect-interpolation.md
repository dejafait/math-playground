# Lemma 900: frequency-weighted normalized Xi-defect interpolation

## Hypotheses

Use the actual Xi and full-line theta kernel Phi of L898, with its
normalization integral_R Phi(u) exp(izu) du = Xi(z). For spatial
variables u,w in R put p=u+w, q=u-w, and define

\[
 W_y(u,w)=p^2\operatorname{sinhc}(yp)\Phi(u)\Phi(w),\qquad
 C_y(x)=\iint W_y(u,w)\cos(xq)\,du\,dw,\qquad
 A_0(y)=\iint W_y(u,w)\,du\,dw.
\]

Here sinhc(z)=sinh(z)/z with its removable value 1 at zero.
Assume x is real and 0<=v,y<=1/2. As established in L898 and L899, set

\[
 a=A_0(0)>0,\qquad
 Q=\iint p^4\operatorname{sinhc}(p/2)\Phi(u)\Phi(w)\,du\,dw
       \in(0,\infty).
\]

All double integrals are over R². The lower bound A_0(y)>=a holds
throughout the real height interval. No RH, zero simplicity,
nonvanishing of Xi, or positive reference-frequency margin is assumed.

## Conclusion

There is one finite positive K, independent of x,v,y, such that

\[
 \left|\frac{C_y(x)}{A_0(y)}-\frac{C_v(x)}{A_0(v)}\right|
 \leq K(1+|x|)^5 e^{-\pi|x|/2}|y^2-v^2|.
 \tag{1}
\]

Specifically, if E_1>0 is any constant in L320 (6) at R=1, then

\[
 K=2^{9/2}E_1\left(\frac{256}{27a}+\frac{16Q}{27a^2}\right)
 \tag{2}
\]

suffices. This expression is finite but has not been numerically
evaluated. The estimate includes either zero height, both upper
endpoints and coincident heights. It is an absolute error estimate,
not a sign assertion or relative estimate at small values.

## Proof

### Imported analytic input and scope of the specialization

Reuse the uniform completed-Xi strip estimate and its product bound
L320 (4)/(6). With R=1, the latter states, for every real x,

\[
 \max_{|z|=1}|H_x(z)|\leq M_x,
 \qquad H_x(z)=\Xi(x+iz)\Xi(x-iz),\qquad
 M_x=E_1(2+|x|)^{9/2}e^{-\pi|x|/2}.
 \tag{3}
\]

If using L320's full parameter setting, fix eta=3/4, so
R>eta>1/2. Its proof of (6) needs no anchor estimate; no witness
cutoff, reciprocal series or sign conclusion of L320 is used here.
Equation (3) already covers negative and bounded x, including x=0.

Cauchy's integral/derivative formulas and analytic Taylor expansion
are the standard inputs: NIST DLMF, version 1.2.8 (15 September 2026),
[1.9.30–31](https://dlmf.nist.gov/1.9#iii) and
[1.10.1](https://dlmf.nist.gov/1.10.E1), as inspected in the prior
source comparison. The contour below is the unit circle and H_x is
entire, so the analyticity and contour hypotheses hold. These theorems
and L320's growth bound are imported, not reproved. The work required
here is their squared-height and real-normalization specialization;
neither source states (1) in this form. This is reproduction of a
standard analytic method, without a claim of originality.

### Even product and uniform removal at zero

The holomorphic function H_x is even in z, since replacing z by -z
exchanges its two factors. Write its Taylor expansion as

\[
 H_x(z)=\sum_{n\geq0}h_{2n}(x)z^{2n}.
\]

Cauchy's coefficient formula gives

\[
 h_{2n}(x)=\frac{1}{2\pi i}\int_{|z|=1}
                \frac{H_x(z)}{z^{2n+1}}\,dz,
 \qquad |h_{2n}(x)|\leq M_x.
 \tag{4}
\]

For |t|<1 define the analytic function

\[
 F_x(t)=2\sum_{n\geq0}(n+1)h_{2n+2}(x)t^n.
 \tag{5}
\]

For every r<1, (4) dominates this series and its first derivative
on |t|<=r by convergent weighted geometric series. Termwise
differentiation there is therefore justified. For 0<=t<=1/4,

\[
 \begin{split}
 |F_x(t)|&\leq 2M_x\sum_{n\geq0}(n+1)t^n
              =\frac{2M_x}{(1-t)^2}\leq\frac{32}{9}M_x,\\
 |F'_x(t)|&\leq 2M_x\sum_{n\geq1}n(n+1)t^{n-1}
              =\frac{4M_x}{(1-t)^3}\leq\frac{256}{27}M_x.
 \end{split}
 \tag{6}
\]

At t=0 the derivative series is understood by its analytic value,
whose only nonzero term in the displayed sum is n=1. Thus these
are uniform closed-interval estimates, not bounds divided by t.

For real y the reality of Xi gives H_x(y)=|Xi(x+iy)|².
L898 (2) gives H'_x(y)=y C_y(x). For y>0, differentiating the
Taylor expansion and dividing by y identifies C_y(x)=F_x(y²).
At y=0, L898's dominated differentiation gives
C_0(x)=H''_x(0)=2h_2(x)=F_x(0), so the same identification holds.
Only H_x, not the modulus-square expression at complex height, has
been used as the holomorphic function.

Integrating F'_x along the real segment from s=v² to t=y² and
using (6) now yields

\[
 |C_y(x)-C_v(x)|\leq\frac{256}{27}M_x|y^2-v^2|,
 \qquad |C_v(x)|\leq\frac{32}{9}M_x.
 \tag{7}
\]

This also proves the difference bound when a height is zero or
the heights coincide, without an endpoint limiting argument.

### Real normalizer variation

For real p and 0<=s,t<=1/4, L899 (5)/(6) establishes that

\[
 b_p(t)=\log\operatorname{sinhc}(p\sqrt t)
\]

is real, nondecreasing, and satisfies
|b_p(t)-b_p(s)|<=p²|t-s|/6, including t=0 and p=0.
The real mean value theorem for exp gives

\[
 |e^{b_p(t)}-e^{b_p(s)}|
 \leq e^{\max(b_p(t),b_p(s))}|b_p(t)-b_p(s)|
 \leq \operatorname{sinhc}(p/2)\frac{p^2}{6}|t-s|.
\]

Multiplication by the nonnegative p²Phi(u)Phi(w), followed by
integration, is legitimate because its dominating integral Q is
finite by L899 (9). Consequently

\[
 |A_0(y)-A_0(v)|
 \leq\iint|W_y-W_v|\leq\frac Q6|y^2-v^2|.
 \tag{8}
\]

This uses no derivative under an unbounded integral. In particular,
the p=0 line presents no singularity. Only positive real values of
A_0 are used; no assertion about its complex zeros is needed.

### Both quotient terms and the prescribed frequency envelope

The exact identity

\[
 \frac{C_y}{A_0(y)}-\frac{C_v}{A_0(v)}
 =\frac{C_y-C_v}{A_0(y)}
  +\frac{C_v(A_0(v)-A_0(y))}{A_0(y)A_0(v)}
\]

together with (7), (8) and A_0(y),A_0(v)>=a gives

\[
 \left|\frac{C_y(x)}{A_0(y)}-\frac{C_v(x)}{A_0(v)}\right|
 \leq M_x\left(\frac{256}{27a}+\frac{16Q}{27a^2}\right)
                  |y^2-v^2|.
 \tag{9}
\]

For u>=0, (2+u)^(9/2)<=2^(9/2)(1+u)^(9/2)
<=2^(9/2)(1+u)^5. Substituting (3) into (9) therefore proves
(1) with (2), retaining precisely the requested exponential rate.
Every constant is independent of x,v,y. ∎

The possible downstream use is interpolation against separately
proved positive reference margins on frequency bands. No such margin
is provided here. The estimate does not supply relative small-value
control, defect positivity at every height, or all-degree mixed
positivity in L030–L032/C032a. The fixed cross-endpoint obstruction
in L898 and the qualified oscillatory-ordering failure in L312
remain intact; the latter is a comparison, not a proof input.

### Independent audit of the full height square (2026-11-08, step117)

The bound (1), with exactly the constant (2), passes the separately
approved audit. The following checks replay the specialization; they
add no sign conclusion or stronger growth input.

In L320 (6), R=1 and eta=3/4 are admissible fixed parameters.
Its exponent is 7/2+R=9/2. For z=u+iv on the unit circle the two
completed-zeta heights are x-v and x+v, and
|x-v|+|x+v|>=2|x|. Thus their decay is at least the decay in (3),
also for negative x and |x|<1. Each polynomial height factor is
bounded by a fixed multiple of 2+|x|, already absorbed in E_1.
No part of the positive anchor or witness argument is being imported.

The length of the unit circle in (4) is 2pi and the denominator
has modulus one. Its coefficient estimate therefore has no missing
factor or dependence on n. Evenness eliminates every odd coefficient.
For all complex |t|<=1/4, the series (5) and its differentiated
series have respective summable majorants
2M_x(n+1)4^(-n) and 2M_x n(n+1)4^(-(n-1)), with the latter indexed
by n>=1. The same construction works on every |t|<=r<1, replacing
1/4 by r. Thus termwise differentiation holds on |t|<1, including
a neighborhood of the entire real interval; continuity at zero is
part of the same statement. Summing gives exactly
2/(1-1/4)^2=32/9 and 4/(1-1/4)^3=256/27.
At zero F_x(0)=2h_2 and F'_x(0)=4h_4. L898 (2), with its dominated
zero-height differentiation, identifies 2h_2=C_0(x). Consequently
integrating F'_x between either ordering of v² and y² proves (7)
on the entire closed square, including its diagonal and all corners.
This argument divides by y only for y>0 and never divides by Xi.

For the normalizer, L899 (5)/(6) is valid for every fixed real p,
including p=0, without needing a uniform logarithmic-series bound
in unbounded p. Monotonicity in t gives
exp(max(b_p(t),b_p(s)))<=sinhc(p/2). Multiplying the resulting
pointwise mean-value inequality by p²Phi(u)Phi(w) is harmless at
p=0, where this weight vanishes. Its full spatial integral is
bounded by Q|t-s|/6. Finiteness of Q is supplied separately by
L899 (9), so no uncontrolled parameter derivative is interchanged
with a spatial integral. Positivity of a follows from the actual
positive theta density on any open rectangle avoiding p=0.

Finally the exact quotient identity retains both terms. Their
coefficients are 256/(27a) and (32/9)(Q/6)/a²=16Q/(27a²).
All denominators are positive real normalizers bounded below by a;
no complex nonvanishing is assumed. The last conversion uses
2+|x|<=2(1+|x|) and (1+|x|)^(9/2)<=(1+|x|)^5, valid even at x=0.
This checks (2) with its stated power 5 and rate pi/2, rather than
a weakened envelope. K is positive, finite, and common to all
x,v,y, but remains numerically unevaluated.

The direct mathematical inputs remain L320, L898 and L899, as in
the unchanged DAG. The audit verifies a local reproduction of the
assessed Cauchy/Taylor method; it establishes neither a new source
theorem nor an independent reference margin. All-degree mixed
positivity and the other qualifications above remain open.

## Mathlib

Coverage of the full displayed bound has not been checked; its
availability is unknown. Supporting Mathlib theorems for Cauchy's
formula, analytic power-series differentiation and integration bounds
have not been checked either. The DLMF references above are classical
analytic inputs, not a claim of a formalized proof. No numerical
certificate or mathematical script is used for this analytic result.
