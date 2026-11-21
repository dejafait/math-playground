# L739: a small-window witness against Suzuki square order

## Hypotheses

Use L018's completion
\(\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\).
For \(\theta=2,4\), use the complete real continuous causal kernels
and the original operators specified in L618's hypotheses:

\[
 (K_\theta[t]f)(x)=\mathbf1_{x<t}
       \int_{-\infty}^{t}K_\theta(x+y)f(y)\,dy,
 \qquad f\in L^2(({-\infty},t),dx).
\]

Their defining transform is
\(\exp(-2\theta\xi'(s)/\xi(s))\), with
\(s=1/2-iz\), \(\Im z>1/2\). The derivative is in \(s\).
For \(t>0\), set
\(f_t=\mathbf1_{[-t,t]}/\sqrt{2t}\), extended by zero in the
original space. Endpoints are immaterial in \(L^2\).

The imported local representations below are from Masatoshi Suzuki,
*Integral operators arising from the Riemann zeta function*,
[arXiv:1907.07302v2](https://arxiv.org/pdf/1907.07302v2)
(6 March 2020), Theorem 1.2, (1.11), (1.13), Propositions 3.1–3.2,
(3.8)–(3.10), and (3.13), printed pp.3,5–7. No RH, innerness,
global contraction or parameter-order theorem is assumed.

## Conclusion

As \(t\to0+\), on the actual compressed operators,

\[
 \boxed{\quad
 \langle f_t,(K_4[t]^2-K_2[t]^2)f_t\rangle
       =-\frac{64\pi^4}{5}\,t^4+O(t^5)<0
       \quad\text{for all sufficiently small }t>0.\quad}       \tag{1}
\]

In particular \(K_2[t]^2\le K_4[t]^2\) in quadratic-form order
fails for every sufficiently small positive window. The implied
constant in (1) is fixed: only parameters 2 and 4 occur. A positive
existential onset is proved below; no numerical onset is claimed.

This is a local specialization of the cited source formulas. It
rules out this proposed sufficient square-order mechanism, not the
bare implication between global contractivity statements and not RH.

## Proof

### Local complete-kernel remainder

Suzuki's Proposition 3.2 gives, for each of the two fixed parameters,

\[
 \Psi_\theta(v)=\frac{v^{\theta-1}}{\Gamma(\theta)}
                    +O_\theta(v^\theta),\qquad v\to0+.
                                                               \tag{2}
\]

The printed proof also displays a weaker additive \(O(v)\). To
justify using the stated stronger remainder here, its (3.8) writes
\(\Psi_\theta=\Psi^0_{\theta,\theta}
+\Psi^0_{\theta,\theta}*\Psi^1_\theta\) on the positive half-line.
Equation (3.9), obtained there from the convergent Bessel series
(3.10), gives
\(\Psi^0_{\theta,\theta}(v)=v^{\theta-1}/\Gamma(\theta)
+O_\theta(v^\theta)\).
Proposition 3.1 bounds \(\Psi^1_\theta\) near zero. Thus choose
finite \(D,M\) and \(r>0\) such that
\(|\Psi^0_{\theta,\theta}(y)|\le D y^{\theta-1}\) and
\(|\Psi^1_\theta(y)|\le M\) for \(0<y\le r\). For \(0<v\le r\),

\[
 \left|\int_0^v\Psi^0_{\theta,\theta}(y)
                         \Psi^1_\theta(v-y)\,dy\right|
 \le MD\int_0^v y^{\theta-1}dy=\frac{MD}{\theta}v^\theta.
\]

This verifies precisely the remainder in (2) needed at \(\theta=4\),
without redoing the source construction or using its weaker display.
Consequently there are \(r_\theta>0\), \(b_\theta\ge0\) such that
for \(0\le v\le r_\theta\),

\[
 \left|\Psi_\theta(v)-\frac{v^{\theta-1}}{\Gamma(\theta)}\right|
       \le b_\theta v^\theta,
 \qquad
 |\Psi_\theta(v)|\le P_\theta v^{\theta-1},
 \quad P_\theta=\Gamma(\theta)^{-1}+b_\theta r_\theta.
                                                               \tag{3}
\]

The value at zero follows by continuity for these parameters.
Set
\(0<\delta\le\min\{1,(\log2)/2,r_2/2,r_4/2\}\).
Retain Suzuki's full formula (3.13):

\[
 \begin{split}
 g_\theta(x)={}&2\pi^\theta e^{-3x/2}\Psi_\theta(2x)\\
 &-4\theta\pi^\theta e^{-3x/2}
  \int_0^x\Psi_\theta(2(x-y))e^{2y}
       \frac{J_1(2\sqrt{2\theta y})}{\sqrt{2\theta y}}\,dy.
 \end{split}                                                   \tag{4}
\]

The removable quotient at zero is 1: the defining convergent series
is
\(J_1(2\sqrt w)/\sqrt w
=\sum_{m\ge0}(-1)^m w^m/(m!(m+1)!)\).
Hence
\(H_\theta=\sup_{0\le y\le\delta}
 |e^{2y}J_1(2\sqrt{2\theta y})/\sqrt{2\theta y}|<\infty\),
with that continuous extension. By (3), the integral in (4) has
absolute value at most

\[
 P_\theta 2^{\theta-1}H_\theta
       \int_0^x(x-y)^{\theta-1}dy
  =\frac{P_\theta 2^{\theta-1}H_\theta}{\theta}x^\theta
       \qquad(0\le x\le\delta).                              \tag{5}
\]

The first term in (4), using
\(0\le1-e^{-3x/2}\le3x/2\), differs from
\(a_\theta x^{\theta-1}\), where
\(a_\theta=(2\pi)^\theta/\Gamma(\theta)\), by at most
\((2^{\theta+1}\pi^\theta b_\theta+3a_\theta/2)x^\theta\).
Combining this with (5) proves

\[
 |g_\theta(x)-a_\theta x^{\theta-1}|
       \le C_\theta x^\theta\quad(0\le x\le\delta),
 \quad
 C_\theta=2^{\theta+1}\pi^\theta
                  (b_\theta+P_\theta H_\theta)+3a_\theta/2.
                                                               \tag{6}
\]

Finally (1.13) is the exact arithmetic sum
\(K_\theta(x)=\sum_{n\ge1}\lambda_\theta(n)n^{-1/2}
g_\theta(x-\log n)\), with \(g_\theta(v)=0\) for \(v<0\).
The coefficients in the exponential Dirichlet series (1.11) are
normalized by \(\lambda_\theta(1)=1\): its exponent has no
\(n=1\) term, so only the constant term of the exponential contributes
there. For \(0\le x\le\delta<\log2\), every \(n\ge2\) term
vanishes by causality. Thus \(K_\theta(x)=g_\theta(x)\) exactly
on this interval, and (6) is a uniform remainder for the complete
kernel, not an arithmetic truncation approximation. In particular
\(a_2=4\pi^2\) and \(a_4=8\pi^4/3\).

### Composition on the original space and the normalized vector

For fixed \(t>0\), L618's support reduction confines both input and
output to \([-t,t]\). Continuity gives a bounded kernel on its
square, hence a Hilbert–Schmidt operator on the original space.
Reality and symmetry of \(K_\theta(x+y)\) make this operator
self-adjoint. Fubini is justified since on the finite square each
\(L^2\) function is \(L^1\) and the kernel is bounded. Therefore

\[
 \langle f_t,K_\theta[t]^2 f_t\rangle
          =\|K_\theta[t]f_t\|_2^2,\qquad \|f_t\|_2=1.          \tag{7}
\]

For \(-t\le x\le t\), causality removes \(y<-x\), so with
\(u=x+t\),

\[
 (K_\theta[t]f_t)(x)=\frac1{\sqrt{2t}}\int_0^u K_\theta(v)dv.
                                                               \tag{8}
\]

It is zero for \(x<-t\). If \(0<t\le\delta/2\), integrating (6)
gives, uniformly for \(0\le u\le2t\),

\[
 \int_0^u K_\theta(v)dv=\frac{a_\theta}{\theta}u^\theta
                                     +R_\theta(u),
 \qquad |R_\theta(u)|\le\frac{C_\theta}{\theta+1}u^{\theta+1}.
                                                               \tag{9}
\]

Expanding the real square in the integral of (8) and bounding both
the cross term and the remainder square yields the full error bound

\[
 \begin{split}
 \left|\|K_\theta[t]f_t\|_2^2
       -\frac{a_\theta^2(2t)^{2\theta}}
                    {\theta^2(2\theta+1)}\right|
 \le{}&\frac{a_\theta C_\theta}{\theta(\theta+1)^2}
                            (2t)^{2\theta+1}\\
 &+\frac{C_\theta^2}{(\theta+1)^2(2\theta+3)}
                            (2t)^{2\theta+2}.
 \end{split}                                                   \tag{10}
\]

Indeed these follow by integrating \(u^{2\theta+1}\) and
\(u^{2\theta+2}\), respectively, and dividing by \(2t\).
For \(t\le1\), the right side is at most
\(d_\theta t^{2\theta+1}\), where the fixed finite constant is

\[
 d_\theta=\frac{2^{2\theta+1}a_\theta C_\theta}
                         {\theta(\theta+1)^2}
       +\frac{2^{2\theta+2}C_\theta^2}
                         {(\theta+1)^2(2\theta+3)}.
\]

Thus, writing \(c_2=64\pi^4/5\), \(c_4=1024\pi^8/81\),

\[
 \|K_2[t]f_t\|_2^2=c_2t^4+E_2(t),\quad |E_2(t)|\le d_2t^5,
 \qquad
 \|K_4[t]f_t\|_2^2=c_4t^8+E_4(t),\quad |E_4(t)|\le d_4t^9.
                                                               \tag{11}
\]

For \(0<t\le\min\{1,\delta/2\}\), (7) and (11) imply
\(|\langle f_t,(K_4[t]^2-K_2[t]^2)f_t\rangle+c_2t^4|
\le Mt^5\), with \(M=d_2+d_4+c_4>0\).
Take

\[
 \tau=\min\{1,\delta/2,c_2/(2M)\}>0.
\]

For every \(0<t\le\tau\), the defect is at most
\(-c_2t^4/2<0\), proving (1) with a rigorous remainder and positive
onset. A single negative unit-vector quadratic form contradicts the
specified operator order. ∎

### Critical audit (2026-11-04, step 269)

The separate audit passed under the stated hypotheses. The primary
source was checked at Theorem 1.2, (1.11), (1.13), Proposition 3.1,
Proposition 3.2 and (3.8)–(3.10), (3.13), printed pp.3,5–7.
Both fixed parameters satisfy the theorem's strict condition
\(\theta>1\). The boundedness from Proposition 3.1 and (3.9)
justify the convolution estimate above; the weaker additive \(O(v)\)
display alone would not justify the \(\theta=4\) remainder.
The value of \(\Psi^1_\theta\) at an endpoint is irrelevant to the
integral. Formula (4) preserves both source exponentials and the
removable quotient. In (6), multiplying (5) by \(4\theta\pi^\theta\)
gives exactly \(2^{\theta+1}\pi^\theta P_\theta H_\theta x^\theta\).
The arithmetic coefficient at 1 is one, and every other summand is
identically zero on the chosen interval, including throughout all
arguments \(0\le x+y\le2t\le\delta<\log2\).

For the original space, the bounded square kernel has absolute
bilinear integral at most its supremum times the two restricted
\(L^1\) norms. This proves the needed Fubini and adjoint assertions
without a full-line multiplier or an untruncated second application.
For an independent replay of (10), set \(U=2t\),
\(A=a_\theta/\theta\), \(B=C_\theta/(\theta+1)\).
The squared norm is \(U^{-1}\int_0^U(Au^\theta+R(u))^2du\).
Its leading term is \(A^2U^{2\theta}/(2\theta+1)\);
the two error bounds are
\(2ABU^{2\theta+1}/(2\theta+2)\) and
\(B^2U^{2\theta+2}/(2\theta+3)\). These are precisely (10).
Substitution at 2 and 4 gives the stated \(c_2,c_4\).
All local constants are fixed and finite. On \(0<t\le1\),
\(c_4t^8+d_4t^9+d_2t^5\le Mt^5\), so the displayed positive
\(\tau\) proves negativity on the entire interval \((0,\tau]\).
No mathematical correction or strengthened conclusion was needed.

### Qualifications

This compares compositions of the compressed operators, not the
parameter-doubled scalar kernel or an unweighted full-line multiplier.
There is no vector, parameter or window sweep and no numerical
evidence. L618's large-parameter norm bound was not used or replayed;
only its operator setup and support reduction enter. The local result
does not decide contractivity at any large window, any other descent
mechanism, determinant equivalence, realization or actual-Xi mixed
positivity. The separate audit above verifies only this local witness;
it supplies no fixed-parameter all-window estimate or RH resolution.

## Mathlib

Full coverage of this Suzuki-kernel square-defect specialization has
not been checked; availability is unknown. No formal verification or
absence claim is made. The elementary integral and Hilbert-space
steps above are supplied as an informal proof with the stated primary
source inputs.
