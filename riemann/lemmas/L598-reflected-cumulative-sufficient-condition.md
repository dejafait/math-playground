# Lemma 598: a reflected cumulative sufficient condition

## Hypotheses

Let A:[0,infinity)->[0,infinity) be continuous with
integral_0^infinity (1+t)A(t)dt finite. Define

    G(t)=integral_t^infinity A(u)du,
    S_h(r)=sum_(j>=0) [G(r+2jh)-G(r+(2j+1)h)],
    D_h(r)=G(0)-S_h(r)-S_h(h-r),       0<=r<=h, h>0.

The actual-theta specialization is
A(t)=integral_R s^2 k(s+t)k(s-t)ds, with k from L019 and its even
continuation from L239. L233 supplies continuity and all absolute
moments. No Fourier sign or RH is assumed. This result is unaudited.

## Conclusion

The series is absolutely and uniformly convergent for r in [0,h], and
for x=pi/h,

    G(0)/x - integral_0^infinity G(t)sin(xt)dt
      = integral_0^(h/2) D_h(r)sin(pi r/h)dr.

In particular D_h(r)>=0 throughout [0,h/2] suffices for the cumulative
upper bound at x. An all-frequency conclusion needs every h>0. The
condition is sufficient; its necessity is not asserted. This is the
standard half-wave folding from Csordas, arXiv:1309.0055v2, Remark 3.11,
printed pp.8-9, followed by complementary-position reflection. See
[the versioned primary PDF](https://arxiv.org/pdf/1309.0055v2).
The x factor in Proposition 3.10's integration by parts must be retained;
only positive frequencies are used here.

For the actual-theta numerical diagnostic, cutting the cumulative
integral at L=3 changes D by at most G(3)<10^(-500). On the approved
box 1/8<=h<=4, h/8<=r<=h/2, truncating theta to n<=8 and the defining
s integral to |s|<=6 changes this clipped defect by less than 10^(-92),
provided the remaining finite integrals are evaluated exactly. These
are improper-tail estimates only. No quadrature, interpolation or
rounding error bound, and no actual-theta sign, is proved here.

## Proof

### Convergence and reflection

G is nonnegative, continuous and decreasing, and Tonelli gives
integral_0^infinity G(t)dt=integral_0^infinity tA(t)dt<infinity.
For m>=1, hG(mh)<=integral_((m-1)h)^(mh) G(t)dt. Thus
sum_(m>=0) G(mh)<infinity. Since G(r+mh)<=G(mh), this also proves
uniform absolute convergence of the alternating series on [0,h].
The paired definition of S_h equals that alternating series.

The sine integral is absolutely convergent. Divide it into intervals
[mh,(m+1)h] and substitute t=r+mh. Since
sin(x(r+mh))=(-1)^m sin(pi r/h), absolute integrability permits
summing under the integral and gives

    integral_0^infinity G(t)sin(xt)dt
      = integral_0^h S_h(r)sin(pi r/h)dr
      = integral_0^(h/2) [S_h(r)+S_h(h-r)]sin(pi r/h)dr.

Finally integral_0^(h/2) sin(pi r/h)dr=h/pi=1/x. Subtraction proves
the identity and the sufficient condition. Absolute convergence also
gives S_h(0)+S_h(h)=G(0), so D_h(0)=0; symmetry gives D_h(h-r)=D_h(r).
No monotonicity of A, positive-definiteness theorem or spectral sign
was needed for this folding argument.

### Complete theta and cumulative tails

For v>=0 the positive summands in L019 and 3<pi, pi^2<10 give

    0<k(v)<=80 exp(9v/2) sum_(n>=1) n^4 exp(-3n^2 exp(2v))
           <=160 exp(9v/2-3exp(2v)).

For the last inequality, factor out exp(-3exp(2v)) and use
sum n^4 exp(-3(n^2-1))<2: the ratio of successive terms is at most
16exp(-9)<1/2. Also exp(2v)>=1+2v implies
k(v)<=160exp(-3)exp(-3v/2)<8. Evenness gives the same bounds at |v|.

For t>=L=3 and s>=0, bound k(s-t) by 160exp(-3), and bound k(s+t)
by the previous envelope. Put lambda_t=6exp(2t)-9/2. Using
exp(2(s+t))>=exp(2t)(1+2s), and integrating s^2 exp(-lambda_t s),

    A(t)<=4*160^2 exp(-3) exp(9t/2-3exp(2t))/lambda_t^3.

Here the factor 2 for s<0 follows from evenness of both k factors.
For t=L+v, lambda_t>=lambda_L and the exponential numerator is at
most exp(9L/2-3exp(2L))exp(-lambda_L v). Therefore

    G(L)<=4*160^2 exp(-3) exp(9L/2-3exp(2L))/lambda_L^4.

At L=3, exp(6)>400, lambda_L>2000 and log(10)<2.31 make this less
than 10^(-500). All these bounds concern the complete theta kernel.

Define G_L(t)=integral_t^L A(u)du for t<=L and zero otherwise.
Then E=G-G_L equals G(L) on [0,L] and G(t) above L. E is decreasing,
nonnegative, and tends to zero. Its alternating series S_h^E lies in
[0,E(r)] by the alternating-series bound (or by pairing consecutive
terms). Consequently

    D_h-D_h^L=G(L)-S_h^E(r)-S_h^E(h-r)

has absolute value at most G(L). This retains the entire alternating
tail; it does not delete it or assume its desired sign.

### Omitted theta modes and s tail for the diagnostic

Let k_8 keep the first eight positive summands. The omitted modes obey

    0<=k(v)-k_8(v)<=160*9^4 exp(-243) exp(-v)
                        <10^(-99) exp(-v),       v>=0.

Indeed exp(2v)>=1+2v makes each n>=9 term's v factor at most
exp(-(6n^2-9/2)v)<=exp(-v). The remaining n sum is at most twice
its n=9 term: successive ratios are at most (10/9)^4 exp(-57)<1/2.
The numerical bound follows from log(160*9^4)<14 and
99log(10)<228.69<243-14. Evenness again covers the full real line.

For 0<=t<=3, positivity and k_8<=k<8 give

    0<=A(t)-A_8(t)
      <=2 integral_0^infinity s^2 [8*10^(-99)exp(-|s+t|)
                                 +8*10^(-99)exp(-|s-t|)]ds
      <=64 exp(3)*10^(-99)<2*10^(-96).

Here |s+-t|>=s-3 and integral_0^infinity s^2 exp(-s)ds=2.
For s>=6, k_8(s-t)<=8, and monotonicity of the scalar envelope
9v/2-3exp(2v) for v>=0 bounds k_8(s+t) by its envelope at s.
The resulting omitted s tail is at most

    2560 exp(27-3exp(12)) integral_0^infinity (6+v)^2 exp(-v)dv
      =128000 exp(27-3exp(12)) <10^(-1000).

We weakened 6exp(12)-9/2 to 1 in this bound. Thus the combined A
error is <3*10^(-96), and its cumulative integral on [0,3] has error
<9*10^(-96). Each S has at most 26 evaluated terms at h>=1/8 in
the implementation, with terms above L identically zero. Including
G_L(0), a triangle bound uses at most 53 such values; hence the
clipped-defect error is <53*9*10^(-96)<10^(-92).

The script `scripts/reflected-majorant/scan.py` numerically evaluates
these finite integrals using Gauss quadrature and Chebyshev integration.
Its certificate `scripts/reflected-majorant/scan-certificate.json` is
explicitly DIAGNOSTIC_ONLY_NO_RIGOROUS_SIGN_CERTIFICATE. Agreement
between resolutions is not an enclosure for the remaining numerical
errors. No sign inference is made from that agreement or from the
positive sampled values.

## Mathlib

Full matching coverage and supporting convergence/integration results
have not been checked. No absence is claimed. The imported half-wave
argument is cited above; the reflection and tail specialization are
written out to fix conventions and the complete-kernel error budget.
General reference: https://leanprover-community.github.io/mathlib4_docs/
