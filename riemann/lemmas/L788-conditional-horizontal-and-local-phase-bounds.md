# Lemma 788: conditional horizontal and local phase-bound audit

## Hypotheses

Define the actual kernel and its first summand by
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                    e^{-\pi n^2e^{4u}},\qquad
 B(u)=2\pi e^{4u},\qquad
 \Phi_1(u)=\pi e^{5u}(B(u)-3)e^{-B(u)/2}.
\]
These series are holomorphic on |Im(u)|<pi/8: on compact subsets,
the terms and their derivatives have bounds C n^N exp(-c n^2).
Fix an integer k>=10^9 and D_k={z:|z-k|<=k/20}.
The following source inputs remain **assumptions** of this lemma.

1. There is a real u_k satisfying
   \[
    1<u_k<\log(k)/4,\quad B_0=2\pi e^{4u_k},\quad
    H_0=B_0-9/2-6/(B_0-3),\quad k=u_kH_0,\quad
    (21/25)B_0\le H_0\le B_0.
   \]
   Set sigma=sqrt(u_k/k), so sigma^2=1/H_0.
2. Write R=Phi/Phi_1-1. Assume the source tube estimate restricted
   to x_0>=0 and 0<=nu<pi/8: if X=exp(4x_0), 2pi X>3, and
   q=16 exp(-3pi X cos(4nu))<1, then on
   T(x_0,nu)={Re(u)>=x_0, |Im(u)|<=nu},
   \[
    |R(u)|\le {2\pi X+3\over2\pi X-3}{q\over1-q}.
   \]
   Also assume its stated numerical specialization
   |R|<=rho=11/10^15 on T(7/20,1/10).
   Admissibility of q at both tubes used below is checked in the proof;
   the tube theorem and this numerical specialization are not audited here.
   The small-strip restriction is explicit after step470's input audit;
   the proof below uses only nu=1/10 and is unchanged by this restriction.
3. For z in D_k there is an analytic full saddle u_s(z), continuous
   on the closed disk, with |u_s-u_k|<=3/200 and
   Psi_z'(u_s)=0, where
   \[
    \Psi_z(u)=2z\operatorname{Log}u+\log\Phi(u).
   \]
   The logarithm agrees with the real logarithm on the positive real
   interval. Its tube branch is constructed below. Existence, uniqueness
   and analytic dependence of the saddle are not conclusions of this audit.

These inputs are the relevant parts of W. Michałowski,
*An explicit uniform cubic wedge for consecutive Toeplitz minors of the
Riemann xi-coefficients*, [arXiv:2607.16795v1, Section 3](https://arxiv.org/html/2607.16795v1#S3),
18 July 2026, definitions (5), Lemmas3.1–3.3 and the real-saddle data
at the start of Lemma3.5's proof. All numbering binds to v1.

Step470 qualification: L789 separately proves these restricted inputs
for the stated k-range. This file retains its conditional implication;
L789 is not used in the proof below, and neither direction is circular.

## Conclusion

For every z in D_k, writing u_s=x_s+iy_s, one has
\[
 -\operatorname{Re}\Psi_z''(x+iy_s)\ge {8\over5}{k\over u_k^2}
                 \qquad(x\ge7/20).                         \tag{1}
\]
On the entire complex disk |u-u_s|<=1/40, one has
\[
 -\operatorname{Re}\Psi_z''(u)\sigma^2>6.633>6,\qquad
 |\Psi_z''(u)|\sigma^2<13.709<14.185,                         \tag{2}
\]
\[
 |\Psi_z'''(u)|\sigma^3<51\sigma<100\sigma.                 \tag{3}
\]
In particular A=-Psi_z''(u_s)sigma^2 satisfies |A|<14.185.

This is a conditional reproduction of the estimates in source
Lemmas3.4–3.5, restricted to k>=10^9. It supplies precisely the derivative
antecedents of L787, while leaving its tube and saddle premises open.
L786 matches the coefficient normalization, but no coefficient theorem
or conclusion of L787 is used in this proof. No actual-I zero-free disk,
saddle-action bound, whole cubic wedge or new minor sign is asserted.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-05-uniform-moment-phase-bounds-audit.md`.
Reproduction is needed to check the complete Cauchy circles, extend
sector positivity to the local disk, and verify constants without
accepting uninspected ancillary enclosures. We use elementary bounds
with room below the required thresholds, rather than claiming a replay
of the source's tighter decimal enclosures.

### Logarithmic tails on complete circles

First consider T(3/10,1/10). Using pi>25/8 and
cos(2/5)>=23/25, the positive exponential series gives
\[
 X=e^{6/5}>33/10,\qquad
 3\pi X\cos(2/5)>2277/80=28+37/80.
\]
For explicit checks, summing the exponential series through degree5
at 6/5 exceeds 33/10; through degree9 at 4 exceeds 54. Thus
\[
 q<Q:={16\over54^7(117/80)}<1,
 \quad {2\pi X+3\over2\pi X-3}<63/47,
 \quad |R|<M:={63\over47}{Q\over1-Q}<11/10^{12}.
                                                               \tag{4}
\]
Here exp(28+37/80)>54^7(1+37/80). The rational prefactor bound
uses 2pi X>165/8 and its monotone decrease with 2pi X.
For x_0=7/20, with the same nu, q is smaller, so its geometric
series is also admissible. Both tubes meet the other stated conditions.

Let L=Log(1+R), defined by its power series. By (4) it is analytic
in the larger tube interior, and
\[
 |L|\le {|R|\over1-|R|}< {111\over10^{13}}.                  \tag{5}
\]
The first summand has a logarithm there: Re(B)>3, so use
log(pi)+5u+Log(B-3)-B/2. Adding L constructs the required log(Phi)
branch; it agrees with the real logarithm on the real interval.

At each horizontal point u=x+iy_s, x>=7/20, a circle of radius
1/20 stays in T(3/10,1/10): its real part is at least 3/10 and
its imaginary part has modulus at most 3/200+1/20=13/200<1/10.
Cauchy's estimate applied to L gives
\[
 |L''(x+iy_s)|\le2(20)^2{111\over10^{13}}
                 =8.88\cdot10^{-9}<10^{-8}.                 \tag{6}
\]
If a circle touches Re(u)=3/10, apply the estimate at radii below
1/20 and pass to the limit; the same supremum bound holds throughout.

For a point of |u-u_s|<=1/40, one has |u-u_k|<=1/25.
Its complete circle of radius1/25 stays within distance2/25 of u_k,
so Re(u)>23/25 and |Im(u)|<=2/25 on that circle. This lies strictly
inside T(7/20,1/10). The assumed smaller-tube bound yields
\[
 |L|\le {\rho\over1-\rho}<12/10^{15},\quad
 |L''|<15/10^{12},\quad |L'''|<1125/10^{12}.                 \tag{7}
\]
The derivative multipliers are 2!(25)^2 and 3!(25)^3 respectively.
No derivative bound has been inferred from a value only at the center.

### Derivatives and positivity on both domains

Direct differentiation of the first summand gives
\[
 -\Psi_z''={2z\over u^2}+8B+{48B\over(B-3)^2}-L'',          \tag{8}
\]
\[
 \Psi_z'''={4z\over u^3}-32B+
                  {192B(B+3)\over(B-3)^3}+L'''.             \tag{9}
\]
For B=a+ib, multiplication by the conjugate denominator gives
\[
 \operatorname{Re}{B\over(B-3)^2}
   ={a(a-3)^2+(a-6)b^2\over|B-3|^4}>0\quad(a>6).           \tag{10}
\]
This checks the resolvent sign directly on the needed domains.
On the horizontal line, x>=7/20 and |y_s|<=3/200.
On the local disk, x>24/25 and |y|<=1/25. In either case
x>=7/20 and |4y|<=1/5, so
\[
 \operatorname{Re}B\ge2\pi e^{7/5}\cos(1/5)
                  >6\cdot2\cdot(49/50)>6.
\]
Thus both 8Re(B) and the resolvent contribution in (8) are positive.

Because Re(z)>=19k/20 and |Im(z)|<=k/20,
|arg z|<=arctan(1/19). On the horizontal line,
|y_s|/x<=3/70<1/7. Hence
\[
 |\arg(z/u^2)|\le\arctan(1/19)+2\arctan(1/7)<17/50,
                                                               \tag{11}
\]
and Re(z/u^2)>0. On the entire local disk, separately,
|y|/x<1/24 and therefore
\[
 |\arg(z/u^2)|<1/19+1/12<1/7<\pi/2.                        \tag{12}
\]
Equation (12), not an inference from a horizontal-line bound, justifies
discarding the power contribution in the local lower estimate.

### Horizontal curvature in both regimes

For 7/20<=x<=u_k, (11), |z|>=19k/20 and
|u|^2<=x^2(1+1/49) imply
\[
 2\operatorname{Re}{z\over u^2}
 \ge {19\over10}\left(1-{(17/50)^2\over2}\right){49\over50}
                {k\over x^2}
 >{7\over4}{k\over u_k^2}.                                 \tag{13}
\]
The exact coefficient before k/x^2 is 1.7543764>7/4.
For x>=u_k, instead use B(x)>=B_0>=H_0 and u_k>1:
\[
 8\operatorname{Re}B\ge8(49/50)B_0
 \ge8(49/50)u_k{k\over u_k^2}
 >{7\over4}{k\over u_k^2}.                                 \tag{14}
\]
All other terms apart from L'' have nonnegative real part. Moreover
\[
 {k\over u_k^2}={H_0\over u_k}
 \ge {21\over25}{2\pi e^{4u_k}\over u_k}>252,               \tag{15}
\]
since e^(4t)/t increases for t>1/4, u_k>1, pi>3 and e^4>50.
The loss in (6) is smaller than
((7/4)-(8/5))*252=37.8. Equations (13)–(15) prove (1).
Integrating from x_s, where Re(Psi_z')=0, would also give the
source's corresponding horizontal Gaussian envelope, without an
assumed maximum or a contour deformation.

### Local bounds with uniform strict margins

Since u_k>1, B_0>2pi e^4>300 and H_0>(21/25)300=252>1.
On |u-u_k|<=1/25, the elementary inequalities
exp(t)<=1/(1-t) for 0<=t<1, exp(-t)>=1-t and
cos(t)>=1-t^2/2 give
\[
 |B|\le e^{4/25}B_0<{6\over5}B_0,\quad
 \operatorname{Re}B\ge {21\over25}{617\over625}B_0,
                                                               \tag{16}
\]
\[
 |B-3|\ge |B|-3\ge e^{-4/25}B_0-3>{83\over100}B_0,
 \qquad |u|\ge {24\over25}u_k.                              \tag{17}
\]
The first bound in (16) uses exp(4/25)<=25/21<6/5. The lower
bound for |B-3| uses |B|=B_0 exp(4Re(u-u_k)), and 3/B_0<1/100;
it does not replace modulus by an unjustified real-part bound.

Normalize (8) by sigma^2=1/H_0. By (10), (12), H_0<=B_0,
H_0>1, and (7), its real part is bounded below by
\[
 8{21\over25}{617\over625}-{15\over10^{12}}
 =6.633984-{15\over10^{12}}>6.633.                           \tag{18}
\]
For the absolute upper bound, |z|<=21k/20, k=H_0u_k and u_k>1
give the power contribution at most (21/10)(25/24)^2.
Using H_0>=(21/25)B_0 for the other terms, (16)–(17) yield
\[
 { |\Psi_z''(u)|\over H_0}
 <{21\over10}\left({25\over24}\right)^2+{80\over7}
   +{48(6/5)(25/21)\over(83/100)^2\,300^2}
   +{15\over10^{12}}<13.709<14.185.                          \tag{19}
\]
This is pointwise on the full local disk, so also holds at the saddle.

For (9) the required third-derivative ratio is
|Psi_z'''|sigma^3/sigma=|Psi_z'''|/H_0, in the same normalization.
The power part is at most (21/5)(25/24)^3 because u_k^2>1.
The exponential part is at most 320/7. Finally
|B+3|<((6/5)+(1/100))B_0=(121/100)B_0, so
\[
 { |\Psi_z'''(u)|\over H_0}
 <{21\over5}\left({25\over24}\right)^3+{320\over7}
  +{192(6/5)(121/100)(25/21)\over(83/100)^3\,300^2}
  +{1125\over10^{12}}<51<100.                               \tag{20}
\]
Equations (18)–(20) prove (2)–(3) on every stated point, without
sampling k or the complex variables.

All nontrivial rational comparisons above, including the two positive
exponential partial sums and (4)–(7), (11)–(13), (18)–(20), are checked
with exact fractions by
`python3 scripts/complex-moment-audit/phase-bounds-468.py`.
The complete scalar certificate is
`scripts/complex-moment-audit/phase-bounds-468.json`; every comparison
passes. That certificate verifies arithmetic, not the analytic reductions,
source hypotheses or any original ancillary program. The analytic
domain and branch checks are the proof above. The strict margins improve
only our local verification budget; they are not claimed as a new result
beyond the checked source's derivative conclusions.

## Mathlib

Full matching coverage has not been checked. No formal theorem for
these actual-kernel constants is asserted. Cauchy estimates, holomorphic
logarithms and elementary exponential/trigonometric bounds are supporting
standard mathematics; neither their presence in a library nor the rational
certificate would verify the conditional tube and saddle inputs.
