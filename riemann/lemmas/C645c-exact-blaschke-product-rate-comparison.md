# Corollary 645c: the exact product crosses the envelope rate threshold

## Hypotheses

Retain L645 and audited C645b: fixed \(0<\delta<1/2\),
\(a=3/2\), \(d=a-\delta\), \(R=a-\delta/2\), and, conditionally,
a stipulated simple zero \(\rho=1/2+\delta+i\gamma\),
\(\gamma\ge e^5\). Use their unchanged disk, nodes and matrix.
For an integer \(n\ge1\), set

\[
 b(t)^2=\frac{R^2(d^2+t^2)}{R^4+d^2t^2},\quad
 B_n=\prod_{j=0}^{n-1}b(j/n),\quad
 f(t)=-\log b(t),\quad \Lambda=\int_0^1 f(t)\,dt.
\]

All square roots and logarithms in these real expressions have positive
arguments. For the envelope comparison use C645b's fixed
\(\epsilon>0\), positive constants \(C=C_{\delta,\epsilon}\),
\(D=D_{\delta,\epsilon}\), exponents
\(u=1/4-\delta/4\), \(v=1/4-\delta/2\), and common height onset:

\[
 U(\gamma)=C\gamma^{u+\epsilon}\log\gamma,\qquad
 0<|\zeta'(\rho)|\le D\gamma^{v+\epsilon}.
\]

Under temporary PSD the positive-real interpolant \(P\) and residual
norm \(\mathcal M_P\) are exactly those of C645b; \(P\) may depend
on \(n\). No derivative lower bound, actual PSD, residual saving, zero
existence, small-\(\delta\) uniformity or multiple-zero extension is
assumed. The product-rate calculation itself requires no zeta zero.

## Conclusion

For every allowed fixed \(\delta\),

\[
 \Lambda>\delta\left(\arctan(2/3)-\frac13\right)
 >\delta\left(\frac14+\frac{779}{306180}\right)>\frac\delta4.
 \tag{1}
\]

Put
\(c=(f(0)-f(1))/2>0\) and \(K=d^2/R^4+1/d^2\).
For every integer \(n\ge1\), the full finite-grid estimate is

\[
 -\log B_n=n\Lambda+c+r_n,\qquad |r_n|\le\frac{K}{8n}.
 \tag{2}
\]

Consequently, for \(N=\lfloor\log\gamma\rfloor\ge5\),

\[
 e^{-c-K/(8N)}\gamma^{-\Lambda}
 \le B_N
 <e^{\Lambda-c+K/(8N)}\gamma^{-\Lambda}.
 \tag{3}
\]

In particular the benchmark formed using the derivative *upper* bound
satisfies

\[
 Q(\gamma):=\frac{U(\gamma)B_N}{D\gamma^{v+\epsilon}}
 \le\frac CD e^{\Lambda-c+K/40}
       \gamma^{\delta/4-\Lambda}\log\gamma\longrightarrow0.
 \tag{4}
\]

Thus C645b's forced-divergence argument using \(q_\delta^N\) does
**not** extend to the exact product by the same exponent comparison:
the explicit derivative-upper-bound benchmark instead tends to zero.
This removes that particular rate obstruction, and does not prove that
the actual envelope \(U B_N/|\zeta'(\rho)|\) tends to zero, that
the sufficient test succeeds, or that any \(K_N\) is non-PSD.
Actual signs and RH remain open. This elementary specialization passed
a separate critical audit on 1 November 2026, recorded below; no novelty
or mathematical discovery beyond the sources checked is asserted.

## Proof

### Imported inputs and why a specialization is needed

Reuse L645 (6)'s exact finite-Blaschke product and C645b's analytic
quotient and envelope, with their canonical citations and hypotheses.
In particular the bounded holomorphic finite-division theorem is
S. Zakeri, *A Course in Complex Analysis*, author
[Notes and Comments, Section 8.3](https://zakerimath.com/CAbook/COM.html),
complete argument following Example 8.33, accessed 1 November 2026.
It already supplies, under temporary PSD,

\[
 |\zeta'(\rho)|\le\mathcal M_P B_n\le U(\gamma)B_n.
 \tag{5}
\]

For controlled summation import NIST DLMF version 1.2.8
(15 September 2026), [Section 2.10(i), equation 2.10.1](https://dlmf.nist.gov/2.10#E1).
For integers \(A<B\) and \(m>0\), with \(F^{(2m)}\)
absolutely integrable, it gives Euler–Maclaurin including the finite
remainder. Here \(m=1\); its exact form is

\[
 \sum_{j=A}^B F(j)=\int_A^B F(x)\,dx+
 \frac{F(A)+F(B)}2+
 \int_A^B\frac{B_2-\widetilde B_2(x)}2F''(x)\,dx.
 \tag{6}
\]

The invocation-start SPECIALIZE assessment inspected these primary
inputs. They are imported without reproof. They supply the product and
finite summation identity, but not its comparison with \(\delta/4\)
for this geometry. The following elementary comparison is the needed
specialization. C645a's completed norm and C644a's fixed reserve are
comparisons only and are not used to bound the present residual.

### Rate bound throughout the fixed-displacement interval

We have \(1<d<R<3/2\). Hold \(R\) fixed in the following
auxiliary integration, and define for \(d\le x\le R\),
\(0\le t\le1\),

\[
 k(x,t)=\frac{x}{x^2+t^2}-\frac{xt^2}{R^4+x^2t^2}.
\]

Differentiating the expression for \(f\) with respect to its
\(d\)-slot, with \(R\) fixed, or evaluating its antiderivative,
gives exactly

\[
 f(t)=\int_d^R k(x,t)\,dx.
\]

Indeed \(f(t)=-\log R+\tfrac12\log(R^4+d^2t^2)
-\tfrac12\log(d^2+t^2)\), whose value at \(d=R\) is zero
and whose derivative in that slot is \(-k(d,t)\).
On the specified rectangle,

\[
 \partial_x k(x,t)=\frac{t^2-x^2}{(x^2+t^2)^2}
 -\frac{t^2(R^4-x^2t^2)}{(R^4+x^2t^2)^2}<0.
\]

The first numerator is strictly negative because \(x>1\ge t\);
the second term is nonpositive because
\(x^2t^2\le R^2<R^4\). Denominators are positive.
Thus \(k(x,t)>k(R,t)\) for \(x<R\). Integration over the
positive-length interval \([d,R]\) and then over \([0,1]\)
is legitimate for these continuous functions and yields

\[
 \begin{aligned}
 \Lambda&>(R-d)\int_0^1 k(R,t)\,dt\\
 &=(R-d)\int_0^1\frac{R^2-t^2}{R(R^2+t^2)}\,dt\\
 &=(R-d)\left(2\arctan(1/R)-\frac1R\right).
 \end{aligned}
 \tag{7}
\]

The derivative of \(H(R)=2\arctan(1/R)-1/R\) is

\[
 H'(R)=\frac{1-R^2}{R^2(R^2+1)}<0\quad(R>1).
\]

Since \(R<3/2\) and \(R-d=\delta/2\), (7) proves the first
inequality in (1). To certify the strictly positive remaining margin,
the exact algebraic identity

\[
 \frac1{1+y^2}=1-y^2+y^4-y^6+\frac{y^8}{1+y^2}
\]

integrated from zero to \(x=2/3\), gives

\[
 \arctan(2/3)>
 \frac23-\frac{(2/3)^3}{3}+\frac{(2/3)^5}{5}
              -\frac{(2/3)^7}{7}
 =\frac{44846}{76545}
 =\frac7{12}+\frac{779}{306180}.
\]

The remainder integral is strictly positive. Subtracting \(1/3\)
proves all of (1) with exact rational arithmetic. There is no equality
case within \(0<\delta<1/2\). Neither excluded endpoint is needed.

### Endpoints, finite-grid error and both floor directions

The positive arguments in \(f\)'s logarithms make it smooth on
\([0,1]\). Apply (6) with \(A=0,B=n,F(x)=f(x/n)\).
Its second derivative is continuous, hence absolutely integrable.
Subtract the included endpoint \(F(n)=f(1)\) to get precisely
the left-endpoint sum defining \(-\log B_n\). This gives

\[
 -\log B_n=n\Lambda+\frac{f(0)-f(1)}2+r_n.
\]

For \(z=x-\lfloor x\rfloor\), the kernel in (6) is
\((z-z^2)/2\in[0,1/8]\), including the integer endpoints.
Also

\[
 f''(t)=\frac{d^2(R^4-d^2t^2)}{(R^4+d^2t^2)^2}
          -\frac{d^2-t^2}{(d^2+t^2)^2},\qquad
 |f''(t)|\le\frac{d^2}{R^4}+\frac1{d^2}=K.
\]

The displayed bound follows by bounding the absolute values of the
two terms separately; their denominators never vanish. Rescaling
\(F''\) in the remainder gives

\[
 |r_n|\le\frac18\int_0^n\frac{|f''(x/n)|}{n^2}\,dx
       \le\frac{K}{8n},
\]

proving (2). L645's strict increase of \(b(t)\) for \(t>0\)
also gives \(f(0)>f(1)\), so \(c>0\).
Exponentiating the two-sided error bound gives

\[
 e^{-c-K/(8N)}e^{-N\Lambda}\le B_N
 \le e^{-c+K/(8N)}e^{-N\Lambda}.
\]

Because \(\Lambda>0\) and
\(\log\gamma-1<N\le\log\gamma\), including integral
\(\log\gamma\),

\[
 \gamma^{-\Lambda}\le e^{-N\Lambda}
                  <e^\Lambda\gamma^{-\Lambda}.
\]

These are both required rounding directions and prove (3).
They control the entire finite product, including its endpoint term;
no Riemann-sum preview is being used as an equality.

### What changes in the envelope test

Substitution of the upper bound in (3), \(N\ge5\), and
\(u-v=\delta/4\) gives (4). Its exponent is strictly negative
by (1), so the logarithmic factor does not prevent convergence to zero.
This is a continuous-height benchmark; no existence of stipulated zeros
is needed to establish its limit.

For the actual normalized envelope, however, the available derivative
estimate has the direction

\[
 \frac{U(\gamma)B_N}{|\zeta'(\rho)|}\ge Q(\gamma).
\]

A lower bound tending to zero proves neither convergence nor eventual
failure or success of the sufficient condition
\(U(\gamma)B_N<|\zeta'(\rho)|\). Equation (5) still supplies a
contradiction to temporary PSD only if that strict condition is proved.
No such proof is supplied here. C645b's analogous benchmark with
\(q_\delta^N\) diverges, whereas (4) tends to zero; this is the
precise change established by retaining the factors. A very small
actual derivative could still defeat the test. The upper bound
\(\mathcal M_P\le U\) likewise gives no lower bound on the actual
residual. Independent sign, realization and derivative-control gaps
remain. The earlier completed-norm and fixed-reserve obstructions have
not been altered or contradicted.

### Independent critical audit — 1 November 2026

Accepted under the invocation-start SPECIALIZE assessment for this
unchanged target. This is a replay of the existing elementary
specialization, not a new analytic estimate. No mathematical repair
was necessary. The essential inputs remain L645 (6), audited C645b and
the cited DLMF finite summation formula; L018 is inherited. Neither
C645a nor C644a supplies a residual lower bound here.

1. **Whole parameter rectangle and the fixed-R integral.** The actual
   parameters obey \(1<d<R<3/2\), \(R>5/4\) and
   \(R-d=\delta/2>0\). Substitution of \(d=R\) in the displayed
   expression for \(f\) gives zero exactly. Its derivative in that
   slot is \(-k\) while R is held fixed, so integration from d to R
   has the displayed positive orientation. This is an auxiliary
   single-variable identity, not differentiation along the curve
   relating R to delta. Throughout the full rectangle the first
   term of \(\partial_x k\) is strictly negative, including t=0
   and t=1, because \(x>1\ge t\). The second is nonpositive,
   since \(x^2t^2\le R^2<R^4\). Thus the strict inequality
   survives integration over the positive-length x interval and
   the t interval. All integrands are continuous on a compact
   rectangle; no infinite interchange or zero-free premise occurs.
2. **Strict rate and exact margin.** At x=R the integrand reduces
   exactly to \((R^2-t^2)/(R(R^2+t^2))\), whose integral is H(R).
   Recomputing its derivative gives
   \((1-R^2)/(R^2(R^2+1))<0\). Hence R<3/2 gives the stated
   strict lower bound, with the factor \(R-d=\delta/2\).
   For the rational certification, the four integrated polynomial
   terms have numerators 51030, -7560, 2016 and -640 over 76545;
   their sum is 44846. Exactly
   \(4\cdot44846-7\cdot25515=779\), so subtracting 7/12
   leaves 779/306180. The integrated remainder
   \(\int_0^{2/3} y^8/(1+y^2)\,dy\) is strictly positive.
   Subtracting 1/3 gives (1) on the entire open delta interval.
   No equality case or limit at an excluded delta endpoint is used.
3. **Finite formula, endpoint and absolute error.** The logarithm
   arguments are strictly positive on [0,1], so f is smooth.
   The imported formula applies on [0,n] for every integer n>=1
   with m=1. It includes both endpoints; subtracting f(1) leaves
   exactly the n factors indexed from 0 through n-1, and gives
   \(c=(f(0)-f(1))/2\) with the correct sign. Directly
   differentiating f twice reproduces the displayed f''.
   For positive A,B, \(|A-B|\le A+B\); applied to each
   numerator it bounds the two absolute terms by d^2/R^4 and
   1/d^2 respectively. The exact Bernoulli kernel is
   \((z-z^2)/2\in[0,1/8]\). Its product with f'' has no
   assumed sign. Since \(F''(x)=n^{-2}f''(x/n)\), integration
   over length n yields K/(8n). This also covers n=1: the
   left sum is f(0), and its error is exactly
   \((f(0)+f(1))/2-\Lambda\), the same bounded remainder.
   L645's strict factor increase gives c>0. No asymptotic
   Riemann-sum assertion replaces the finite identity.
4. **Floors and benchmark direction.** Exponentiating (2) gives
   both displayed bounds with \(-c\), and errors of opposite
   signs. For N=floor(log gamma),
   \(\log\gamma-1<N\le\log\gamma\) holds even when
   log gamma is integral. Since Lambda>0, this yields the
   non-strict lower and strict upper bounds in (3) in exactly
   their stated directions. N>=5 bounds K/(8N) by K/40.
   In Q the common epsilon cancels and u-v=delta/4, so (1)
   makes the exponent strictly negative; the remaining logarithm
   cannot prevent the limit zero. The positive constants may
   depend on fixed delta and epsilon, as stipulated.
5. **Only the qualified comparison is accepted.** At a stipulated
   simple zero above the common analytic onset, C645b supplies
   \(0<|\zeta'(\rho)|\le D\gamma^{v+\epsilon}\).
   Dividing by this upper bound gives
   \(UB_N/|\zeta'(\rho)|\ge Q\), not an upper bound.
   Thus Q tending to zero does not settle the actual envelope.
   Under temporary PSD the inherited inequality (5) still
   requires that envelope to be at least one. There is no
   contradiction without an independent strict upper bound
   below one. Simplicity permits division but gives no
   quantitative lower bound; n-dependent interpolants remain
   covered by the inherited uniform upper envelope. No off-line
   zero existence, effective onset, small-delta uniformity,
   multiple-zero extension or matrix sign has been established.

The audit accepts removal of the factorwise forced-divergence argument
only. The previous q_delta stop and separate completed-norm/reserve
obstructions remain valid in their own scopes. All load-bearing checks
above are analytic or exact rational arithmetic; the earlier diagnostic
floating-point values were not used. No direct mathematical input or
argument has changed, so the DAG row and PROOF.md remain unchanged.

## Mathlib

Full matching coverage for this grid-specific rate comparison and
finite-error specialization has **not been checked**; absence is not
claimed. The supporting Borel–Caratheodory theorem and unassessed
finite-Blaschke coverage remain as qualified in L645/C645b. The precise
Euler–Maclaurin input is cited above. No Lean replay is claimed.
The proof is analytic with an exact rational inequality; diagnostic
floating-point values in the working note are not used as verification.
