# Lemma 490: Explicit two-term remainder on a fixed positive-time band

## Hypotheses

Use the exact functions and conventions of D. H. J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn–Newman constant*,
Research in the Mathematical Sciences **6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
equations (1), (5)–(12). In particular,

    H_t(z)=integral_0^infinity exp(tu^2) Phi(u) cos(zu) du,
    Phi(u)=sum_(k>=1) (2*pi^2*k^4*exp(9u)-3*pi*k^2*exp(5u))
                         *exp(-pi*k^2*exp(4u)),
    alpha(s)=1/(2s)+1/(s-1)+(1/2)Log(s/(2*pi)),
    M_t(s)=exp(t*alpha(s)^2/4)*M_0(s).

Here M_0 is exactly source equation (6), with the logarithm and
nonvanishing domain C minus (-infinity,1] specified in (7); no change
of normalization is allowed. For z=x+iy put

    s_+=(1+y-ix)/2,       s_-=(1-y+ix)/2,
    B_t(z)=M_t(s_+),     gamma=M_t(s_-)/M_t(s_+).

Assume 1/25<=t<=11/50, 0<=y<=1 and x>=4*pi*exp(10000).
The proof imports source Theorem 1.3 and Proposition 6.6(ii), including
their explicit constants. Their underlying saddle estimates are not
independently audited here. No RH or real-zero premise is assumed.

## Conclusion

Uniformly throughout this closed range,

    abs(H_t(z)/B_t(z)-(1+gamma)) < 153/10^6 < 1/100.

This is a quantitative specialization of the source approximation,
not a new asymptotic mechanism. It gives no numerical real/simple
zero cutoff, phase estimate, zero count, finite-collision exclusion,
or conclusion as t tends to zero. It does not imply relative accuracy
near a zero of 1+gamma.

## Proof

### Exact imported inequalities

Put L=log(x/(4*pi)), b_n=exp((t/4)*log(n)^2), and

    N=floor(sqrt(exp(L)+t/16)),
    s_*=s_++(t/2)*alpha(s_+),
    kappa=(t/2)*(alpha(s_-)-alpha(conjugate(s_+))).

The cited Theorem 1.3, equations (13), (20), (22)–(24), and
Proposition 6.6(ii) apply since x>=200, 0<t<=1/2 and 0<=y<=1.
They give, with v_+=max(v,0),

    f_t=sum_(1<=n<=N) b_n/n^(s_*)
         +gamma*sum_(1<=n<=N) n^y*b_n/n^(conjugate(s_*)+kappa),
    abs(H_t/B_t-f_t)<=e_A+e_B+e_(C,0),
    abs(gamma)<=exp(.02*y-y*L/2),
    Re(s_*)>=(1+y)/2+t*L/4
             -t*(1-3*y+8*y*(1-y)/x^2)_+/(2*x^2),
    abs(kappa)<=t*y/(2*(x-6)),
    e_A+e_B<=sum_(1<=n<=N)
      (1+abs(gamma)*N^abs(kappa)*n^y)*b_n/n^Re(s_*)
      *[exp(((t^2/16)*(L-2*log(n))^2+.626)/(x-6.66))-1],
    e_(C,0)<=exp(-(1+y)*L/4-t*L^2/16
       +1.24*(3^y+3^(-y))/(N-.125)
       +(3*abs(L+i*pi/2)+10.44)/(x-12)).

All finite decimals here are exact rational constants. The source
nonvanishing of B_t justifies its divisions, including at y=0 and y=1:
s_+ and s_- have nonzero imaginary parts, so both avoid the cut
(-infinity,1] and the points 0,1. In source (6), the factors s(s-1),
pi^(-s/2) and the exponential are therefore nonzero; source (10)
multiplies by another nonzero exponential. This also gives a
holomorphic nonvanishing B_t on a neighborhood of each point under
consideration. No division by 1+gamma is used.

This application uses only the literal tL/4 real-part bound, not the
stronger coefficient displayed elsewhere in the source's asymptotic
proof. The real-part correction here is specifically Proposition
6.6(ii)'s 8y(1-y), not Theorem 1.3(21)'s distinct 4y(1+y).
The two finite-sum definitions and all other error bounds above match
Theorem 1.3(13)–(20),(22)–(24).

### Uniform bounds for the two finite sums

We have L>=10000 and x>=exp(L)>=L^4/24; the last inequality is the
fourth nonnegative Taylor term of exp(L). These imply x>24 and
x^(-2)<1/100. Write r=log N. The floor satisfies

    2<=N<=exp(L/2)+1,       0<=r<=L/2+1.

Indeed sqrt(exp(L)+t/16)<=exp(L/2)+1, and the lower bound follows
already from exp(L/2)>=3. For the logarithmic upper bound, write
log(exp(L/2)+1)=L/2+log(1+exp(-L/2))<=L/2+1.
Thus all denominators below are positive.
Since 0<=y<=1 and x>=200,

    1-3*y+8*y*(1-y)/x^2<=1+y*(-3+8/x^2)<=1.

The positive part is at most one, so the real-part correction is
at most t/(2*x^2)<=x^(-2). For 1<=n<=N this yields

    b_n/n^Re(s_*)
      <= n^(-(1+y)/2-t*(L-log(n))/4+x^(-2))
      <= n^(-(1+y)/2-t*(L/8-1/4)+x^(-2))
      <= n^(-50-y/2) <= n^(-50).

For the last step, t*(L/8-1/4)>=49.99 and
1/2+49.99-x^(-2)>50. The formula also holds at n=1.

The gamma estimate and log(n)<=r give

    abs(gamma)*n^y<=exp(y*(.02-L/2+r))<=exp(1.02)<4.

For example e<3 and exp(.02)<=1/(1-.02)=50/49 justify the
last numerical comparison. Also x-6>=x/2 and t<=1 give

    abs(kappa)*r<=r/x<1,

where r<=L/2+1<x follows from x>=L^4/24 and L>=10000.
Consequently N^abs(kappa)<e<3. Taking absolute values of powers
of positive integers, the magnitude of each second-sum term is at
most 12*n^(-50), including its factor gamma. This uses
n^(-Re(kappa))<=N^abs(kappa); no sign of Re(kappa) is assumed.
The two n=1 terms are exactly 1 and gamma. Therefore

    abs(f_t-(1+gamma))<=13*sum_(n=2)^infinity n^(-50)
       <=13*2^(-50)*(1+2/49)<26*2^(-50)<10^(-6).

The integral comparison used here is
sum_(n=2)^infinity n^(-50)<=2^(-50)+integral_2^infinity u^(-50)du.
The final rational comparison follows, for instance, from
2^50=(2^10)^5>1000^5=10^15.

### Uniform bounds for every approximation error

For 1<=n<=N, -2<=L-2*log(n)<=L, hence its absolute value is at
most L. Since t^2/16<=1 and x-6.66>=x/2, the nonnegative exponent
inside the e_A+e_B sum satisfies

    v_n<=2*(L^2+1)/x
        <=48*(L^2+1)/L^4<=49/L^2<=49/10^8<10^(-6).

For 0<=v<=1/2, the exponential series gives
exp(v)<=sum_(j>=0)v^j=1/(1-v), so exp(v)-1<=2v.
The weight sum in this error is at most
13*sum_(n>=1)n^(-50)<26 (the same integral comparison suffices).
It follows that

    e_A+e_B<26*2*10^(-6)=52/10^6.

For the remaining error, N-.125>=1, 3^y<=3 and 3^(-y)<=1,
so its first positive exponent is at most 4.96<5. Using pi<4,
x-12>=x/2 and the triangle inequality, its last positive exponent
is bounded by

    (3*(L+2)+10.44)/(x-12)
      <=(6*L+34)/x
      <=24*(6*L+34)/L^4<1.

For explicit verification of the last comparison, when L>=10000
we have 6L+34<=7L, hence 24*(6L+34)/L^4<=168/L^3<1.
Discarding only nonpositive terms now gives

    e_(C,0)<exp(-L/4+6)<=exp(-2494)<10^(-4).

Here exp(2494)>=1+2494+2494^2/2>10000, so no numerical
underflow or finite sampling is involved. Combining all estimates,

    abs(H_t/B_t-(1+gamma))
      <10^(-6)+52*10^(-6)+10^(-4)=153/10^6<1/100.

Every inequality is uniform over the unbounded height range, the
moving floor N and both time and y endpoints. No zero-count argument
or interchange of infinite limits occurs; the infinite series above
are only convergent positive majorants for finite sums.

In particular, at a jump exp(L)+t/16=m^2 the definition takes N=m,
and all estimates apply to the newly included n=m term. Immediately
below the jump they apply with N=m-1. No continuity or holomorphicity
of f_t across jumps is assumed. Complex powers use the source's
Section 2 convention n^w=exp(w log n) for positive integers n;
thus abs(n^(-w))=n^(-Re(w)), and n=1 contributes no phase or
branch ambiguity. The lower time endpoint is used in the decay
bound and the upper endpoint is within 0<t<=1/2; no limiting
argument in t or y is required at any closed endpoint.

### Independent application audit, 2026-10-30

The complete source transcription and uniform argument above pass
independent replay. For explicit arithmetic checks, the decay exponent
at the relaxed endpoint is
1/2+(1/25)(10000/8-1/4)-1/100=1262/25>50;
the gamma factor is bounded by 150/49<4; the error exponent by
49/10^8<10^(-6); the last C exponent by
168/10000^3=21/125000000000<1. Also
1+2494+2494^2/2=3112513>10000 and
26/2^50=13/562949953421312<10^(-6).
These bounds persist for every L>=10000 by the displayed uniform
inequalities, rather than by height sampling. All seven exact rational
comparisons, including 153/10^6<1/100, are retained in
`scripts/heat/l490-audit-exact-arithmetic.json`; the full reasoning
is the proof above, not the arithmetic certificate alone.

This audit verifies the local quantitative application, a reproduction/
specialization of known source estimates. It neither independently
audits their saddle proofs nor supplies the missing phase, strict
contour count, exhaustion, finite-collision or zero-time arguments.

## Mathlib

Full matching coverage of this explicit Polymath specialization is
not checked. No Mathlib theorem is used as a substitute for Theorem
1.3 or Proposition 6.6(ii); elementary exponential and integral
comparisons are proved in the argument above. No formal verification
is claimed.
