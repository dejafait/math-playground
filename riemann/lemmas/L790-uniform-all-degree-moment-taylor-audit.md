# Lemma 790: uniform all-degree Taylor bound for the actual moment quotient

## Hypotheses

Let
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                   e^{-\pi n^2e^{4u}},\quad
 I(z)=\int_0^\infty u^{2z}\Phi(u)\,du,\quad
 a(z)=I(z)/\Gamma(2z+1).
\]
The power in the real integral uses the real logarithm of u>0.
Fix integers k>=10^9 and d>=3. Write D_k={|z-k|<=k/20} and
Omega_k={|z-k|<k/20}. In L786's normalization a(n)=a_n for
nonnegative integers n. Only that normalization, not its order-three
positivity theorem, is used here.

Use the restricted-tube, real-saddle and analytic full-saddle conclusions
of L789, the conditional phase estimates of L788 and the conditional
factorization of L787. Their premises are matched below, so no
additional saddle, nonvanishing, positivity or RH assumption is made.

## Conclusion

The actual a(z) is nonzero on D_k. On Omega_k it has an analytic
logarithm f, normalized by f(k)=log(a_k), and
\[
 \left|\frac{f^{(d)}(k)}{d!}\right|
 <\frac{2503}{5000}\,40^d k^{1-d}
 <3\,40^d k^{1-d}.                                      \tag{1}
\]
The first constant is only an audit margin for the second inequality;
no improvement beyond the source's estimates is claimed.

This reproduces the first conclusion of W. Michałowski,
*An explicit uniform cubic wedge for consecutive Toeplitz minors of the
Riemann xi-coefficients*, [arXiv:2607.16795v1, Section3](https://arxiv.org/html/2607.16795v1#S3),
18 July 2026, Proposition3.7, using the saddle-action case of Lemma3.5.
Numbering binds to v1. No ancillary enclosure is assumed or replayed.
The curvature-normalized follow-up, other wedge gates, bounded k/r
positivity and all-degree mixed positivity are not conclusions here.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-05-uniform-moment-taylor-coefficient-audit.md`.
The reproduction checks the previously unaudited action/logarithm/Gamma
interface and the complete all-degree budget. Standard analytic logarithm
and Cauchy theorems are imported, not reproved. Cauchy's estimate is
|g^(m)(k)|<=m! M/r^m when g is holomorphic near the closed radius-r
disk and |g|<=M on its entire circle; see the Cauchy-estimate statement
in [Rutgers Math503, fall2004](https://sites.math.rutgers.edu/~greenfie/mill_courses/math503/diary.html).

### Discharging the conditional interfaces

L789 gives a real u_k with 1<u_k<log(k)/4, B_0=2pi exp(4u_k)>300,
H_0=B_0-9/2-6/(B_0-3), k=u_k H_0 and
(21/25)B_0<H_0<B_0. Fix sigma=sqrt(u_k/k), so sigma^2=1/H_0;
both k and sigma remain constant during differentiation in z.

L789 proves the general tube bound precisely on the small strips and
with q<1 required by L788. Its explicit smaller-tube bound is
|R|<11/10^15 on T(7/20,1/10). Its full saddle is holomorphic on
|z-k|<51k/1000, including a neighborhood of D_k, and satisfies
|u_s-u_k|<3/200 and partial_u Psi_z(u_s)=0. The common full phase is
\[
 \Psi_z(u)=2z\operatorname{Log}u+\ell_\Phi(u),
\]
where ell_Phi is L789's analytic logarithm, real on the positive real
interval of its tube. This is the same branch used by L788 and L787;
in particular its constant log(pi) is retained.

These facts supply every premise of L788. That lemma gives the global
horizontal bound (8/5)k/u_k^2, and on |u-u_s|<=1/40 the inequalities
-Re(Psi_uu)sigma^2>6.633>6, |Psi_uuu|sigma^3<51sigma<100sigma,
and |Psi_uu|sigma^2<13.709<14.185. They supply all the derivative
premises of L787, including its separately required 14.185 upper bound.
L789 supplies L787's other real/tube/saddle premises. L786 identifies
the integer coefficients. Thus L787 applies to the actual I and yields
\[
 I(z)=e^{S(z)}\sqrt{2\pi/C(z)}(1+\varepsilon(z)),\quad
 S(z)=\Psi_z(u_s(z)),\quad C(z)=-\Psi_{uu}(z,u_s(z)),
 \quad |\varepsilon(z)|<0.0158<0.018                       \tag{2}
\]
on D_k, with epsilon analytic in Omega_k and the principal square root.
In particular I is nonzero there. This inference uses no Taylor bound.

### Saddle action and its analytic domain

Every saddle lies in the domain of ell_Phi and in Re(u)>0, where
Log(u) is analytic. Composition makes S analytic in Omega_k.
There, Re(C)sigma^2>=6, so C is nonzero. Differentiating stationarity
in z gives
\[
 0=2/u_s+\Psi_{uu}(z,u_s)u_s',\qquad
 u_s'=-2/(u_s\Psi_{uu}(z,u_s)).
\]
The chain rule and stationarity then give the exact envelope identities
\[
 S'=2\operatorname{Log}u_s,\qquad
 S''=2u_s'/u_s=-4/(u_s^2\Psi_{uu}(z,u_s)).                 \tag{3}
\]
These are identities for the full phase, not derivatives of a numerical
remainder. Since |u_s|>u_k-3/200>(24/25)u_k and
|C|>=Re(C)>=6/sigma^2, throughout D_k
\[
 |S''|\le\frac{4\sigma^2}{6(24/25)^2u_k^2}
 =\frac{625}{864}\frac1{u_k k}<\frac5k.                  \tag{4}
\]
The source's sharper 0.645/k enclosure is unnecessary and is not
certified by this argument.

### Compatible logarithms and complete circles

Put A=C sigma^2. On D_k, Re(A)>=6 and |A|<14.185<20. Thus
\[
 1<6H_0\le |C|<20H_0=20k/u_k<20k,
\]
because H_0>(21/25)300=252. The right-half-plane principal logarithm
Log(C) is analytic, has |arg C|<pi/2 and has positive real part.
Consequently
\[
 |\operatorname{Log}C|\le\log|C|+|\arg C|
 <\log(20k)+\pi/2<k.                                    \tag{5}
\]
For the last uniform inequality, k-log(20k)-pi/2 is increasing for
k>1. At k=10^9, log20<4, log10<3 and pi/2<2 bound the subtracted
quantity by 4+27+2=33<10^9. The logarithm estimates follow from
e^4>20 and e^3>10, for example their positive partial sums.

Since |epsilon|<9/500, its power-series logarithm E=Log(1+epsilon)
is analytic and
\[
 |E|\le\frac{|\varepsilon|}{1-|\varepsilon|}
 <\frac9{491}<\frac{19}{1000}.                           \tag{6}
\]
Here epsilon was constructed in L787 by dividing I by a nonzero
analytic main term, before proving I nonzero. Thus no derivative of a
bare uniform error estimate is being taken.

For Re(z)>-1/2, Gamma(2z+1) is holomorphic and nonzero. Choose its
analytic logarithm g(z), real at positive real z. The standard facts
and logarithmic derivative are [NIST DLMF5.2(i), (5.2.1)–(5.2.2)](https://dlmf.nist.gov/5.2#i):
the only Gamma poles are the nonpositive integers and Gamma has no
zeros. The analytic-logarithm theorem applies on this simply connected
half-plane. By (2),
\[
 F=S-\tfrac12\operatorname{Log}C+E+\tfrac12\log(2\pi)-g   \tag{7}
\]
is analytic on Omega_k and exp(F)=a. L789's uniqueness and conjugation
give real u_s(k)>0; S(k) is real and C(k)>0. Every summand of Phi is
positive on u>=0, since 2pi n^2 exp(4u)-3>0. Hence I(k)>0, and
(2) gives 1+epsilon(k)>0. All terms in (7) are real at k, so
F(k)=log(a_k). Set f=F. Any other analytic logarithm differs by a
constant multiple of 2pi i and has the same positive-order derivatives.
No global principal logarithm of I is assumed.

The entire closed circle |z-k|=r with r=k/40 is strictly within
Omega_k. Each function in (7), and S'', is holomorphic on an open
neighborhood of its closed disk. Bounds (4)–(6) hold throughout that
circle. There is no boundary-continuation inference from sampled values.

### Cauchy estimates and the real-center Gamma term

Apply Cauchy to S'' at order d-2 and to the next two terms at order d.
After division by d!, the resulting bounds are
\[
 \frac{|S^{(d)}(k)|}{d!}
 \le\frac{5\,40^{d-2}}{d(d-1)}k^{1-d},\quad
 \frac{|(\tfrac12\operatorname{Log}C)^{(d)}(k)|}{d!}
 <\tfrac12\,40^d k^{1-d},\quad
 \frac{|E^{(d)}(k)|}{d!}<\frac{19}{1000}40^d k^{-d}.       \tag{8}
\]
The first estimate uses (d-2)!/d!=1/[d(d-1)]; the constant log(2pi)/2
in (7) has zero d-th derivative.

Import [DLMF25.11.12](https://dlmf.nist.gov/25.11.E12), for integer
n>=1, and the convergent Hurwitz series [25.11.1](https://dlmf.nist.gov/25.11.E1),
for Re(s)>1 and a outside the nonpositive integers (DLMF version1.2.8).
Specialize n=d-1>=2, s=d>1 and a=x=2k+1>0. Together with
psi=Gamma'/Gamma they give
\[
 \frac{|g^{(d)}(k)|}{d!}
 =\frac{2^d}{d}\sum_{j=0}^\infty(x+j)^{-d}.
\]
This retains the affine chain factor 2^d and the factor
(d-1)!/d!=1/d. Since t maps to (x+t)^(-d) is positive and decreasing,
the j>=1 sum is bounded by its integral on [0,infinity). Thus
\[
 \sum_{j\ge0}(x+j)^{-d}\le x^{-d}+\frac{x^{1-d}}{d-1},
 \qquad
 \frac{|g^{(d)}(k)|}{d!}
 \le\frac1{d k^d}+\frac2{d(d-1)}k^{1-d}.                 \tag{9}
\]
The last step uses x>2k and d>1. Only a positive absolutely convergent
series at a real center is used; no complex Stirling remainder or
unjustified interchange is needed.

### Uniform all-degree sum

Divide (8)–(9) by 40^d k^(1-d) and use the triangle inequality in (7).
The four bounds are
\[
 \frac5{1600d(d-1)},\qquad\frac12,\qquad
 \frac{19}{1000k},\qquad
 \frac1{40^d}\left(\frac1{dk}+\frac2{d(d-1)}\right).      \tag{10}
\]
For integers d>=3 the first bound decreases, the next two are constant
in d, and every positive factor in each Gamma summand decreases with d.
The k-dependent terms decrease with k; the others are constant in k.
Therefore the whole upper bound is at most its value at d=3, k=10^9:
\[
 \frac1{1920}+\frac12+\frac{19}{10^{12}}
 +\frac1{64000}\left(\frac1{3\cdot10^9}+\frac13\right)
 =\frac{96101000003649}{192000000000000}
 <\frac{2503}{5000}=0.5006<3.                            \tag{11}
\]
This monotonicity argument covers all degrees and heights. It is not a
finite-degree test. The source's tighter ancillary total is unused.

The exact scalar comparisons, including (4), (6), (11) and the disk
radius containment, are checked by
`python3 scripts/complex-moment-audit/taylor-472.py`; the complete
rational certificate is `scripts/complex-moment-audit/taylor-472.json`.
It checks arithmetic, not the analytic proof, which is given above.
The local gain is a checked assembly and reproduction of the named
source result. It establishes neither the rest of that manuscript nor
an unshifted/all-order sign, and it is not an RH candidate.

## Mathlib

Full matching coverage has not been checked. No formal theorem for
this specific moment quotient or all-degree constant is asserted.
Cauchy estimates, analytic logarithms and Gamma/polygamma formulas are
supporting standard results; their use here is informal and does not
constitute formal verification of the actual-kernel assembly.
