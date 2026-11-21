# Corollary 999f: centered theta-power derivative and the endpoint comparison

## Hypotheses

Use theta(y)=sum_{n in Z} exp(-pi*n^2*y), for real y>0. Let
xi_Q(w,s) be Lagarias--Rains's completed two-variable zeta function,
with their normalization

    xi_Q(w,s)=s(s-w) Z_Q(w,s)/(2w).

The imported source is J. C. Lagarias and E. Rains, *On a Two-Variable
Zeta Function for Number Fields*, [arXiv:math/0104176v5, 7 July 2002](https://arxiv.org/pdf/math/0104176v5),
Theorem 2.1 and equation (2.9), printed pp. 8--9. Its entire completion
and integral representation are inputs, not claims reproved here.
The unshifted Theorem 4.4 and Lemmas 4.5--4.7, pp. 21--24, provide
the corresponding differentiated-kernel representation. No shifted
contour formula is used. L018 and L019 identify the w=1 normalization
and theta convention: G(1,t)=Xi(t), where

    G(w,t)=xi_Q(w,w/2+i*t).

Throughout, 1<=w<=3/2 and 40<=t<=45. Derivatives in w below are total
derivatives of this centered family, holding real t fixed. Set

    T(x)=theta(exp(2x)), B(x)=log T(x), b(x)=x/2+B(x),
    Q=t^2+w^2/4,
    H(w,x)=exp(wx/2)(T(x)^w-1)/w,                    x>=0.

The logarithm on the real axis is the real logarithm. No collision,
zero simplicity, zero location, RH, or sign of a transform is assumed.

## Conclusion

The exact centered derivative is

    G_w(w,t)=-integral_0^infinity F(w,t,x) cos(tx) dx,
    F=(w/2)H+Q H_w,
    H_w=exp(wx/2)[x(T^w-1)/(2w)
                          +(w B T^w-(T^w-1))/w^2].                (1)

For every a>=0 its omitted tail has the explicit uniform bound

    |integral_a^infinity F(w,t,x) cos(tx) dx|
       <=(2703/2) exp(-3 exp(2a)).                                (2)

In particular the tail after a=2 is less than 10^(-61), and the
full absolute estimate gives only |G_w|<68.

There is also the exact representation

    G_w(w,t)=integral_0^infinity M(w,x) cos(tx) dx,
    M=exp(w b)[b b''+(1+w b)((b')^2-1/4)].                        (3)

M extends to a smooth even function of x on R, with rapidly decreasing
derivatives. Its central value satisfies M(w,0)<-1/40. For every
integer N>=1,

    G_w(w,t)=(-1)^N t^(-2N)
                integral_0^infinity partial_x^(2N)M(w,x) cos(tx) dx. (4)

Consequently the particular comparison that keeps finitely many
integration-by-parts endpoint terms and bounds the remaining integral
only in absolute value supplies an interval centered at zero. It
cannot supply either a strict positive margin or a strictly negative
value. This is a limitation of that comparison, not a no-go theorem
for signed integral estimates. M(w,0)<0 is NOT G_w(w,t)<=0.

The approved uniform sign test remains inconclusive. No value of G_w
in the test box has been signed, and no collision or RH consequence
is established by this corollary.

## Proof

### Exact normalization and differentiation

Source equation (2.9), with r=exp(-x), gives

    Z_Q(w,s)=-1/s+1/(s-w)
       +integral_0^infinity (T(x)^w-1)
                         (exp(sx)+exp((w-s)x)) dx.

At s=w/2+i*t, s(s-w)=-Q. The two rational terms combine to
w/[s(s-w)], so their contribution to xi_Q is exactly 1/2.
The remaining two exponentials combine to 2 exp(wx/2) cos(tx).
Thus, with all completion factors retained,

    G(w,t)=1/2-Q integral_0^infinity H(w,x) cos(tx) dx.             (5)

Here and below the integrals converge absolutely before the indicated
integration by parts. The required differentiations are justified by
the following explicit compact domination; we do not assume that
pointwise smoothness licenses differentiation of an improper integral.

Put v=exp(2x)>=1 and S=T-1. Since n^2>=1+3(n-1) for n>=1,

    0<S=2 sum_{n>=1} exp(-pi*n^2*v)
        <=2 exp(-pi*v)/(1-exp(-3*pi*v))
        <=3 exp(-3*v)<3/20.                                    (6)

We used pi>3 and exp(3)>20; the latter follows already from the
Taylor sum through degree eight, 806769/40320>20. Thus
0<B<=S and exp(2B)=T^2<(23/20)^2<2.

For complex |w|<=2, write h=(T^w-1)/w as the entire expression

    h(w,x)=integral_0^B exp(wu) du.

Then |h|<=B exp(2B)<=2S and
|h_w|<B^2<=S^2. Consequently

    |H|<=6 exp(x) exp(-3v),
    |H_w|<=exp(x)[xS+S^2]
           <=exp(x)(3x+1) exp(-3v).                             (7)

For the last bound, 9 exp(-3v)<1. Multiplication by exp(c*x),
for any fixed c, preserves integrability of these bounds. They
therefore dominate the integrands uniformly on a complex
neighborhood of the prescribed compact w,t box, including the
factor |cos(tx)|<=exp(|Im(t)|x). Standard dominated holomorphic
differentiation applies. Differentiating (5), with Q_w=w/2, proves
(1). The displayed H_w is the derivative of h times exp(wx/2), plus
the derivative x/2 of that exponential. It includes the moving
center and theta logarithm. The rational contribution 1/2 has zero
derivative; it has not been dropped before completion.

For orientation only, h>0 and h_w>0 for real w>0, because their
integral expressions have positive integrands. Thus H,H_w and F
are positive for x>=0. The sign-changing cosine prevents this fact
from signing G_w.

### Effective tail bound

For the real box, w/2<=3/4 and Q<2026. Equation (7) gives

    |F|<=exp(x)(6078x+2031) exp(-3 exp(2x))
        <=8109 exp(2x) exp(-3 exp(2x)),

where x<=exp(x) and 1<=exp(x) for x>=0. Integrating the last
expression from a to infinity proves (2), since its integral is
(8109/6) exp(-3 exp(2a)). At a=0 this is less than
2703/40<68.

At a=2, exp(4)>50: exp(3)>20 and the degree-three Taylor sum for
exp(1) is 8/3. Hence (2) is less than (2703/2) exp(-150).
Also exp(150)>20^50>10^65, since 2^50>10^15. It follows that
this bound is less than 10^(-61). This is an absolute bound on
every omitted tail contribution to (1), not a sign evaluation of
the retained integral from 0 to 2.

### Centered kernel, parity and endpoints

The standard Jacobi theta transformation used in L019 is

    T(-x)=exp(x) T(x).

It makes exp(x/2)T(x), and hence b(x), even for real x. In
particular B'(0)=-1/2. Differentiating H at x=0 gives

    H_x(w,0)=(T(0)^w-1)/2-T(0)^w/2=-1/2,
    H_wx(w,0)=0.                                                (8)

All boundary terms at infinity in the following integrations vanish.
For completeness, repeated differentiation of the theta series
produces terms P_m(pi*n^2*v) exp(-pi*n^2*v), where P_m is a
polynomial of degree at most m. For each fixed m their sum is
bounded by a fixed polynomial in v times exp(-3v). To see the
summability, factor exp(-3v) and bound the remaining n-sum by a
constant times sum n^(2m) exp(-(pi*n^2-3)), which converges.
The same type of bound holds for derivatives of B=log T, since
T>=1. In particular B and all its derivatives tend to zero at
this rate. Factors polynomial in x and exp(wx/2), for w in the
compact interval, do not affect integrability or decay.

Twice integrating H against cos(tx), using (8), gives

    integral_0^infinity [H_xx-(w^2/4)H] cos(tx) dx
       =1/2-Q integral_0^infinity H cos(tx) dx=G(w,t).

Writing H=[exp(wb)-exp(wx/2)]/w shows that its kernel is

    K=H_xx-(w^2/4)H
      =exp(wb)[b''+w((b')^2-1/4)].

Differentiating K with respect to w gives exactly M in (3).
The preceding derivative bounds, with the additional at-most-linear
factor b=x/2+B, justify this differentiation under the integral.
They also show that every fixed x derivative of M decays rapidly
and is integrable on [0,infinity). Indeed (b')^2-1/4=B'+(B')^2
and b''=B'', so every term has a decaying B factor. Evenness
extends these bounds to the negative half-line. Formula (3) is
also the w derivative of the source's unshifted kernel formula;
no heat equation or shifted-contour normalization is being assumed.

Since b is even, M is even. Every odd derivative of M at zero
therefore vanishes. Integrating (3) twice by parts yields
-t^(-2) times its cosine transform with M replaced by M_xx;
the boundary term -M_x(w,0)/t^2 is zero. Repeating proves (4).
Absolute estimation of its last integral gives only

    -R_N(w)/t^(2N) <= G_w(w,t) <= R_N(w)/t^(2N),
    R_N(w)=integral_0^infinity |partial_x^(2N) M(w,x)| dx.

Each R_N is finite and positive. If R_N were zero, continuity would
force partial_x^(2N)M to vanish identically on [0,infinity), making
M a polynomial there. Its decay would force M=0, contrary to the
strictly negative value at zero proved below. No quantitative smallness
or N-uniform bound for these constants is asserted. Irrespective of
their sizes, these particular two-sided bounds straddle zero and have
no signed endpoint term. They therefore do not meet the approved sign
thresholds, including certification of a nonpositive value.

### A strictly negative kernel value, with no transform inference

Here is a fully elementary bound separating the kernel from a
purported nonnegative-integrand argument. The usual rational bounds
157/50<pi<22/7 imply exp(pi)>23. Indeed exp(3)>20, and the
degree-three Taylor sum for exp(7/50) is 862693/750000; multiplying
it by 20 gives a number greater than 23.

At x=0, (6) with exp(pi)>23 gives

    T(0)-1<2*23^2/(23^3-1)=1058/12166<9/100,
    0<b(0)=log T(0)<9/100.                                    (9)

Directly differentiating the theta series gives

    T''(0)=8 sum_{n>=1} pi*n^2*(pi*n^2-1) exp(-pi*n^2).

The n=1 term is less than 2640/1127<47/20. For n>=2,
n^4<=16^(n-1) and n^2>=4+5(n-2). Since pi^2<10,
the remaining terms have total less than

    80 sum_{n>=2} n^4 exp(-pi*n^2)
       <1280*23/(23^5-16)=29440/6436327<1/200.

The two elementary n inequalities follow respectively by induction
using ((n+1)/n)^4<16 for n>=2, and by
n^2-4-5(n-2)=(n-2)(n-3)>=0. Thus T''(0)<5/2.
Since T(0)>1 and B'(0)=-1/2,

    b''(0)=T''(0)/T(0)-1/4<5/2.

Equations (9) and b'(0)=0 now give

    M(w,0)=T(0)^w [b(0)b''(0)-(1+w b(0))/4]
           <T(0)^w [9/40-1/4]
           =-T(0)^w/40<-1/40.

If b''(0) were nonpositive the product bound would be immediate;
if it is positive it follows by multiplication of the positive
upper bounds. This proves the asserted inequality without any
floating-point evaluation. It concerns M at x=0, not G_w at a
point of the w,t box. Positive contributions from other oscillatory
lobes remain entirely unpaid. In particular it neither refutes nor
proves uniform positivity of G_w. No conclusion concerning G_tt,
events, transport or w=1 zero preservation follows.

## Mathlib

Full matching coverage is not checked and is unknown. No formal
verification of the two-variable family, the derivative, or these
effective constants is claimed. Standard differentiation, dominated
integration, theta transformation and integration by parts support
the calculation; the precise external family input is cited above.
