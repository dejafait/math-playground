# Corollary C030f: audited archimedean pointwise bounds

## Hypotheses

Let psi=Gamma'/Gamma be the digamma function and, for real r, set

\[
 m(r)=\Re\psi(1/4+ir/2)-\log\pi.
\]

Use the principal logarithm, the usual positive real logarithm on
(0,infinity), and Euler's constant gamma=lim_n(H_n-log n).
The named analytic inputs are NIST DLMF
[5.7.6](https://dlmf.nist.gov/5.7.E6), valid away from the nonpositive
integer poles, [5.4.19](https://dlmf.nist.gov/5.4.E19), for integers
0<p<q, and [5.9.15](https://dlmf.nist.gov/5.9.E15), for Re z>0.
For the Bose integral use [25.5.1](https://dlmf.nist.gov/25.5.E1),
Re s>1, and [25.6.1](https://dlmf.nist.gov/25.6.E1), zeta(2)=pi^2/6.
These primary formulas and their domains were inspected in approval1187
and rechecked during this audit. No zeta-zero hypothesis is used.

## Conclusion

The two pointwise inputs from Nicholas G. Polson,
[*On Hilbert's 8th Problem*, arXiv:1708.02653v24, 11 September2026,
Lemma6.1, printed pp11-12](https://arxiv.org/pdf/1708.02653v24#page=11),
pass the independent proof audit:

\[
 m(r)\ge-6\quad(r\in\mathbb R),\qquad
 m(r)>1\quad(|r|\ge20).
\]

In particular all four source correction budgets are valid uniformly
for r>=20, and

\[
 |m(r)-\log(r/(2\pi))|<3/1000\quad(r\ge20),\qquad
 1<m(20)<2.
\]

This is REPRODUCTION of known source estimates for reliability of
C030e, under the unchanged SPECIALIZE assessment1186/approval1187.
It is not progress beyond those source conclusions. The head-integral
bound136, explicit formula, heat-series theorem, far-time estimates,
actual-Xi all-degree signs, theta signing and realization are outside
the conclusion. L744(8) already gives a stronger asymptotic error;
that existing result is a comparison, not a premise of this proof.

## Proof

### Elementary scalar enclosures

We will use 3<pi<22/7. For a self-contained input to C030e, reproduce
only its elementary Machin calculation, rather than depend on the heat
assembly which this result supports. Put a=arctan(1/5), b=arctan(1/239).
The tangent addition formulas give tan(4a)=120/119 and tan(4a-b)=1.
The integral bounds 1/5-1/(3*5^3)<a<1/5 and 0<b<1/239 give
0<4a-b<4/5. Also pi/2>1 because arctan(1)>1/2 by its integral.
Thus 4a-b=pi/4. Alternating integral expansions for arctan give

\[
 \pi>16\left(\frac15-\frac1{3\cdot5^3}
       +\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)-\frac4{239}
       =\frac{1231847548}{392109375}>3,
\]
\[
 \pi<16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}\right)
       -4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
       =\frac{670143059704}{213311234375}<\frac{22}{7}.
                                                        \tag{1}
\]

Positive Taylor terms give

\[
 e^{7/10}>\sum_{k=0}^3\frac{(7/10)^k}{k!}>2,\qquad
 e^{6/5}>\sum_{k=0}^4\frac{(6/5)^k}{k!}>22/7,
 \qquad e^3>\sum_{k=0}^8\frac{3^k}{k!}>20.             \tag{2}
\]

Hence log2<7/10, log pi<6/5, and e^{10pi}>e^{30}>20^{10}.
Integrating a finite geometric expansion of 1/(1-u^2), with its
positive remainder on (0,1/2), gives

\[
 \log3=2\int_0^{1/2}\frac{du}{1-u^2}
       >2\left(\frac12+\frac{(1/2)^3}{3}\right)=13/12. \tag{3}
\]

Finally e^{3/2}>1+3/2+(3/2)^2/2>10/3, so log(10/3)<3/2.
The comparisons of sums and rationals in this proof are exact;
no decimal approximation of a transcendental constant is assumed.

### Series, value at zero, and evenness

Fix x=1/4 and y=r/2. In DLMF5.7.6, each paired summand
1/(j+1)-1/(j+x+iy) is O((j+1)^(-2)) for fixed y, locally uniformly
in y. The same holds at y=0. Subtraction and taking real parts
therefore give

\[
 \Re\psi(x+iy)-\psi(x)
 =\sum_{j=0}^{\infty}
   \left(\frac1{x+j}-\frac{x+j}{(x+j)^2+y^2}\right)
 =\sum_{j=0}^{\infty}
   \frac{y^2}{(x+j)((x+j)^2+y^2)}.                    \tag{4}
\]

The last summands are O((j+1)^(-3)) uniformly for y in compact
sets; all denominators are positive. Every term is even in y and
strictly increasing in y>=0 apart from the common endpoint y=0.
Comparing convergent sums directly shows that m is even and strictly
increasing on [0,infinity). No differentiation of this series is
needed. In particular m(r)>=m(0) for every real r.

Gauss's formula DLMF5.4.19 with p=1,q=4 applies. Its k=1,3 cosine
terms vanish, and its k=2 term is -(1/2)log4=-log2. Together with
-log4 and cot(pi/4)=1 this gives

\[
 m(0)=-\gamma-\pi/2-3\log2-\log\pi.                 \tag{5}
\]

Integral comparison for 1/u gives log(n+1)<=H_n<=1+log n;
taking the defining limit gives 0<=gamma<=1. Thus (1)-(2) imply

\[
 -6<-411/70=-\left(1+11/7+21/10+6/5\right)<m(0)<0. \tag{6}
\]

The last strict inequality uses gamma>=0, pi>3 and log2,log pi>0.
This already proves the required all-real lower bound, including r=0.

### Both pieces of Binet's integral

For r>=20 put z=1/4+ir/2. Re z=1/4>0, so DLMF5.9.15 gives

\[
 \psi(z)=\log z-\frac1{2z}
    -2\int_0^{\infty}\frac{u\,du}{(u^2+z^2)(e^{2\pi u}-1)}.
                                                        \tag{7}
\]

Re log z=log|z| on the principal branch. The two elementary
corrections satisfy

\[
 0\le\log|z|-\log(r/2)
   =\tfrac12\log(1+1/(4r^2))\le1/(8r^2)\le1/3200,
 \qquad
 0<\Re\frac1{2z}=\frac2{1+4r^2}\le2/1601,           \tag{8}
\]

using log(1+v)<=v for v>=0. To bound the integral, split at u=r/4.
On 0<=u<=r/4,

\[
 \Re(u^2+z^2)=u^2+1/16-r^2/4
      \le(1-3r^2)/16<0,
 \qquad |u^2+z^2|\ge(3r^2-1)/16\ge1199/16>74.       \tag{9}
\]

DLMF25.5.1 at s=2, Gamma(2)=1, and DLMF25.6.1 give, after
the substitution v=2*pi*u,

\[
 \int_0^{\infty}\frac{u\,du}{e^{2\pi u}-1}
 =\frac{\Gamma(2)\zeta(2)}{4\pi^2}=1/24.
\]

Thus the absolute head contribution, including the factor2 in (7),
is at most 2/(74*24)=1/888. This uses a complex-modulus bound from
the real part in (9), not a positive-real-z denominator estimate.

For every real u, Im(u^2+z^2)=r/4, so on u>=r/4>=5 its modulus
is at least r/4>=5. For u>=5,

\[
 \frac1{e^{2\pi u}-1}
 =\frac{e^{-2\pi u}}{1-e^{-2\pi u}}
 \le\frac{e^{-2\pi u}}{1-e^{-10\pi}}.
\]

Enlarging the integration interval to [5,infinity) and evaluating its
exponential first moment therefore bounds the absolute tail by

\[
 \frac25\frac{e^{-10\pi}}{1-e^{-10\pi}}
       \left(\frac5{2\pi}+\frac1{4\pi^2}\right)
 <\frac{31}{90(20^{10}-1)}<10^{-11}.                 \tag{10}
\]

Here pi>3 gives the prefactor bound31/90, and (2) bounds the
exponential quotient by 1/(20^{10}-1). The displayed integral
converges absolutely: the integrand is bounded near u=0, all these
denominators are nonzero, and the tail has an integrable exponential
majorant. Taking real parts and splitting the integral are justified.

Combining (7)-(10), for every r>=20,

\[
 |m(r)-\log(r/(2\pi))|
 \le 1/3200+2/1601+1/888+10^{-11}<3/1000.            \tag{11}
\]

This verifies the source's four budgets uniformly, not at sample points.
At r=20, (1) gives 20/(2pi)>35/11>3, so (3) and (11) give

\[
 m(20)>13/12-3/1000=3241/3000>1.
\]

Also 20/(2pi)<10/3 and log(10/3)<3/2 give
m(20)<3/2+3/1000=1503/1000<2. By monotonicity and evenness from
(4), m(r)>=m(20)>1 for every |r|>=20, including r=20 and r=-20.
Together with (6) this proves the two requested bounds. No required
estimate failed, and no assumption on the critical line was introduced.

For supplementary exact arithmetic run
`python3 scripts/near-zero-assembly/pointwise_margins_1188.py`.
Its full certificate is
`scripts/near-zero-assembly/pointwise-margins-1188.json`.
It verifies only the rational comparisons; the convergence arguments
and imported DLMF identities are the analytic proof above.

## Mathlib

Full matching Mathlib coverage of these pointwise estimates and exact
constants is unchecked, not asserted absent. DLMF supplies the cited
analytic identities, not a formalized matching theorem. The scalar
certificate is not a formal verification. This reproduction removes
only C030e's pointwise-source qualification; its explicit-formula and
heat-series imports remain unaudited, and the main RH gap stays open.
