# Lemma 811: exponential exterior suppression at a positive-envelope scale

## Hypotheses

Let K be the actual positive theta kernel of L019, and let
m_0=integral_0^infinity K(u)du, which is finite and positive by L021.
Use exactly L795's normalization

\[
 F_{d,u}(x)=\frac{d!}{(1/2)_d}L_d^{(-1/2)}(u^2x/4).
\]

For integers d>=3 and real 1<=kappa<=2 put l=log d,
x=kappa*d/l^2, I_d=[l/4,3l/4], and define

\[
 A_d(\kappa)=\int_{I_d}K(u)e^{\kappa d u^2/(8l^2)}\,du,
 \qquad
 B_d(\kappa)=\int_{(0,\infty)\setminus I_d}
       K(u)|F_{d,u}(x)|\,du.
\]

All logarithms are natural. The endpoints do not affect these integrals.
The denominator is a positive envelope, not a signed approximation.

## Conclusion

There is an integer d_0>=3, independent of kappa, such that

\[
 B_d(\kappa)\le e^{-d/2048}A_d(\kappa)
 \quad(d\ge d_0,\ 1\le\kappa\le2).                 \tag{1}
\]

The proof supplies explicit sufficient inequalities defining a common
existential onset. It does not supply an effective numerical value for
d_0. No lower bound for the signed theta average P_d, its signed bulk
contribution, or its ratio to A_d is asserted. Consequently (1) does
not establish a sign, a zero count, mixed positivity, or RH.

## Proof

**Exact polynomial bound.** Write
Q_d(z)=d! L_d^(-1/2)(z)/(1/2)_d. The finite expansion imported and
specialized in L795 is NIST DLMF
[18.5.12](https://dlmf.nist.gov/18.5.E12), together with
[13.2.2](https://dlmf.nist.gov/13.2.E2):

\[
 Q_d(z)=\sum_{j=0}^d a_j z^j,\qquad
 a_j=\frac{(-d)_j}{(1/2)_j j!},\quad a_0=1.
\]

This formula uses b=1/2, which is not a nonpositive integer, and the
series terminates for the integer d. Its coefficients satisfy
(j+1)(j+1/2)a_(j+1)+(d-j)a_j=0 for 0<=j<=d, with a_(d+1)=0.
Coefficient comparison therefore proves, as a polynomial identity,

\[
 zQ_d''+(1/2-z)Q_d'+dQ_d=0.                         \tag{2}
\]

For real v>=0 put y(v)=Q_d(v^2) and h(v)=e^(-v^2)y(v).
The chain rule applied to (2) gives
y''-2v y'+4d y=0, and hence

\[
 h''+2v h'+(4d+2)h=0,\qquad h(0)=1,\ h'(0)=0.
\]

All expressions are smooth at v=0; no division by v or limiting
asymptotic formula is used. For
E(v)=h'(v)^2+(4d+2)h(v)^2 differentiation gives
E'(v)=-4v h'(v)^2<=0. Thus E(v)<=E(0)=4d+2 and
|h(v)|<=1. In particular the exact global bound is

\[
 |Q_d(z)|\le e^z\ (z\ge0),\qquad
 |F_{d,u}(x)|\le e^{xu^2/4}\ (u,x\ge0).             \tag{3}
\]

This short energy calculation proves the bound needed for this
specialization directly from the assessed finite polynomial. It avoids
importing or reproving a uniform Bessel/Airy asymptotic theorem, and
has no excluded turning point or small-u regime. Its exponential
e^z is deliberately weaker than the oscillatory envelope e^(z/2).

**Two actual theta bounds and the denominator.** L019 gives a finite
constant C_K>0 such that, for every u>=0,

\[
 K(u)\le C_K e^{9u/2-\pi e^{2u}}.                    \tag{4}
\]

Every term of its theta series is positive. Retaining its n=1 term,
and using e^(2u)>=1, gives

\[
 K(u)\ge4\pi e^{5u/2}(2\pi e^{2u}-3)e^{-\pi e^{2u}}
       \ge C_0 e^{-\pi e^{2u}},\qquad
 C_0=4\pi(2\pi-3)>0.                               \tag{5}
\]

For l>=8/3 the interval [3l/8,3l/8+1] lies in I_d. On it,
u^2>=9l^2/64 and e^(2u)<=e^2*d^(3/4). Integrating (5) over this
unit interval proves the uniform lower bound

\[
 A_d(\kappa)\ge C_0
    \exp\{9\kappa d/512-\pi e^2 d^{3/4}\}>0.       \tag{6}
\]

This is a direct estimate for the specified denominator. It does not
identify its dominant region or turn it into a signed margin.

**Left exterior.** On 0<=u<=l/4, xu^2/4<=kappa*d/64.
Using (3) and m_0, and then (6), bounds its contribution B_- by

\[
 B_-\le m_0 e^{\kappa d/64},\qquad
 \frac{B_-}{A_d}\le\frac{m_0}{C_0}
      e^{-\kappa d/512+\pi e^2d^{3/4}}.             \tag{7}
\]

Set L_0=max{log(m_0/C_0),0}. Since kappa>=1, the sufficient condition

\[
 \pi e^2 d^{3/4}+L_0\le d/1024                    \tag{8}
\]

makes (7) at most e^(-d/1024). Such a condition holds for every
sufficiently large d, because its left side divided by d tends to zero.

**Right exterior, including all unbounded support.** Let b=3l/4
and assume b>=1. For u>=b, the functions u^2 e^(-2u) and
u e^(-2u) are nonincreasing: their derivatives are respectively
2u(1-u)e^(-2u) and (1-2u)e^(-2u). Consequently

\[
 \left(\frac{du^2}{2l^2}+\frac92u\right)e^{-2u}
 \le\frac9{32}d^{-1/2}+\frac{27}{8}l d^{-3/2}.
\]

The right side tends to zero. Impose the kappa-independent condition

\[
 \frac9{32}d^{-1/2}+\frac{27}{8}l d^{-3/2}\le\pi/2. \tag{9}
\]

Using kappa<=2 in (3), then (4) and (9), bounds the entire right
integrand by C_K exp(-(pi/2)e^(2u)). For t=u-b>=0,
e^(2u)=d^(3/2)e^(2t)>=d^(3/2)(1+2t). Hence its integral B_+ obeys

\[
 B_+\le\frac{C_K}{\pi d^{3/2}}
                  e^{-(\pi/2)d^{3/2}}.              \tag{10}
\]

This also proves the required global integrability using the bound
(3), without extending an asymptotic expansion past its domain.
Dividing (10) by (6) yields

\[
 \frac{B_+}{A_d}\le\frac{C_K}{\pi C_0d^{3/2}}
   \exp\{-(\pi/2)d^{3/2}-9\kappa d/512
                         +\pi e^2d^{3/4}\}.         \tag{11}
\]

Let L_1=max{log(C_K/(pi*C_0)),0}. A sufficient condition for (11)
to be at most e^(-d/1024), after discarding the favorable terms
-9*kappa*d/512 and -(3/2)log d, is

\[
 (\pi/2)d^{3/2}-\pi e^2d^{3/4}-L_1\ge d/1024.    \tag{12}
\]

It holds for every sufficiently large d: after division by d the
left side tends to positive infinity.

**Uniform onset and sum.** Choose an integer d_0 so that every real
d>=d_0 satisfies d>=3, l>=8/3, b>=1, (8), (9), (12), and
d>=2048*log 2. Each requirement holds eventually by the limits just
proved; the finite conjunction therefore has such a common onset.
All constants depend only on the fixed actual K and m_0, and none on
kappa. The two complementary regions are disjoint up to endpoints,
so (7)--(12) give

\[
 \frac{B_d}{A_d}\le2e^{-d/1024}\le e^{-d/2048},
\]

as required. No signed integral was bounded below, and no cancellation,
contour shift, or infinite polynomial sum was interchanged. This is
local progress by elementary specialization, not a claim of a new
general Laguerre theorem or progress beyond the checked sources' theory.

**Independent audit, 5 November 2026 (step564).** The stated conclusion
(1) passes the nominated proof audit, without a change in hypotheses or
exponent. In the coefficient check, the coefficient of z^j in (2) is
(j+1)(j+1/2)a_(j+1)+(d-j)a_j, including j=0 and j=d;
at the latter endpoint both terms vanish. For the damping check, direct
differentiation gives
h''=e^(-v^2)[y''-4vy'+(4v^2-2)y]. Thus the displayed equation for h
and the negative sign in E' are exact also at zero. This validates the
global polynomial bound, not an asymptotic surrogate.

The theta lower bound uses exactly the positive n=1 summand of L019.
The retained unit interval gives 9*kappa*d/512 in (6), whereas the
entire left exterior costs at most kappa*d/64=8*kappa*d/512.
Their difference is therefore precisely -kappa*d/512 in (7).
Condition (8) leaves at least d/1024 of decay uniformly in kappa.
For the right exterior, evaluating both decreasing ratios at b=3l/4
gives exactly the two constants in (9). Integration of
exp[-(pi/2)d^(3/2)(1+2t)] over all t>=0 gives the denominator
pi*d^(3/2) in (10); no finite-support preview replaces this tail.

Finally, the left side of (8), divided by d, tends to zero; the left
side of (9) tends to zero; and the left side of (12), divided by d,
tends to positive infinity. These are eventual inequalities for all
real d, so a finite maximum of their onsets works for every sufficiently
large integer d and every kappa in [1,2]. The last sum requires exactly
d/2048>=log 2. The audit accepts only exterior suppression relative to
A_d. Signed bulk margins, adequacy of that scale, initial degrees and
the transfer to mixed positivity remain unresolved. It does not import
an additional theorem or assert a discovery beyond the sources checked.

## Mathlib

Full matching coverage has not been checked. Availability of a theorem
for this actual theta/Laguerre support comparison is unknown. The proof
uses finite coefficient identities, a differentiated real energy,
positive integration and elementary exponential limits. No formal
verification, Mathlib absence claim, or numerical certificate is asserted.
