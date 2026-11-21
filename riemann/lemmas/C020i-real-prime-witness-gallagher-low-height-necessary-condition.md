# C020i — A low-height necessary condition for the full Gallagher energy

## Hypotheses

Use C019y's original integer-d witness, without changing any coefficient.
Thus d tends through positive integers, T>2*pi*e solves

\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad X=T/\sqrt{2d},
 \quad q=\log X,\quad B=(\sqrt2-1)X,\quad h=3\pi/q,
\]
\[
 D=[X,\sqrt2X-h],\quad U=(B-h)/2,\quad
 Y_c=((1+\sqrt2)X-h)/2,\quad
 L=\lfloor X^{1/1000}\rfloor,\quad\ell=\log L,\quad R=L^4.
\]

The real multiplicative alpha(n) are the coefficients of the Euler-product
branch of zeta(s)^(-1/2) on Re(s)>1. With the original linear taper put

\[
 M(t)=\sum_{n\le L}\alpha(n)\frac{\log(L/n)}\ell n^{-1/2-it},
 \qquad M(t)^2M(t+h)^2=\sum_{s\le R}c_s s^{-1/2-it}.
                                                        \tag{1}
\]

The last identity defines exactly C019y(1)'s four individually tapered
factors, including its two shifted factors. The variable t here denotes
real height; the heat times below remain frozen at Y0 and Y0+h.
Let P be the primes in [sqrt(X)/10,sqrt(X)/5]. For every unordered
distinct p<r in P, let v=pr and retain

\[
 a_v(Y_0)=r^{-ih}E_p(Y_0)E_r(Y_0+h)
             +p^{-ih}E_r(Y_0)E_p(Y_0+h),
\]
\[
 E_p(Z)=\exp\left\{\frac{Z^2}{8d}
     \left((\tfrac12\log(Z/(2\pi))-\log p)^2-\pi^2/16\right)
   +\frac{i\pi Z^2}{16d}(\tfrac12\log(Z/(2\pi))-\log p)\right\}.
                                                        \tag{2}
\]

Fix any Y0 in D. The original coefficients are J_(vs)(Y0)=a_v(Y0)c_s,
zero elsewhere, with N=Z_*=N_*^2R and
N_*=floor(sqrt(sqrt(2)X/(2*pi)+X^2/(16d))). Their representation is
unique by C019y's prime/support separation. Define the complete energy

\[
 E(Y_0)=\int_0^\infty
 \left|\sum_{y<k\le ye^{1/U}}J_k(Y_0)k^{-1/2-iY_c}\right|^2\frac{dy}{y},
 \qquad
 H_L=\int_{-1/10}^{1/10}|M(t)M(t+h)|^4\,dt.
                                                        \tag{3}
\]

All statements below have absolute constants and one absolute
existential integer onset. No RH, random-phase law, balancedness,
actual-P estimate, or fixed-to-moving transfer is assumed.

## Conclusion

Uniformly for Y0 in D, for all sufficiently large integer d,

\[
 E(Y_0)\ge \frac{c}{Xq^4}H_L,\qquad
 \frac{E(Y_0)}{Bq^2/U^2}\ge c'\frac{H_L}{q^6}.
                                                        \tag{4}
\]

Consequently a uniform O(Bq^2/U^2) estimate for this exact energy
requires H_L=O(q^6). If H_L/q^6 is unbounded along the prescribed
integers, that sufficient energy estimate fails, uniformly in Y0.
This is a conditional test: neither H_L=O(q^6) nor its negation is
proved here. In particular (4) does not yet stop the energy estimate.

The bound concerns the entire signed coefficient array. Its low-height
contribution lies outside D. Even a future failure of the energy test
would not refute the high-height frozen norm estimate, the moving real
denominator, or RH. The signed numerator, E_P and Xi transfer remain
unresolved. This is a Fourier specialization under EXPLORE assessment1440,
classified REPRODUCTION; no originality beyond the checked sources is
claimed. Independent conceptual audit1446 below retains (4).

## Proof

### Exact signed correlations and Fourier normalization

Put delta=1/U and beta_k=J_k(Y0)k^(-1/2-iYc). After x=log y, the
window sum in (3) is the compactly supported step function

\[
 f(x)=\sum_{k\le N}\beta_k
               \mathbf1_{[\log k-\delta,\log k)}(x).
\]

Endpoints have measure zero. It is a finite sum in L1 intersect L2.
In particular E is finite. Direct integration of intersecting intervals
also gives the complete signed correlation formula

\[
 E(Y_0)=\sum_{k,l\le N}\beta_k\overline{\beta_l}
                   (\delta-|\log(k/l)|)_+ .             \tag{5}
\]

No terms have been replaced by their absolute values. To test this form
use the standard Plancherel theorem with transform
hat(f)(xi)=integral f(x)exp(-i*xi*x)dx. This is the compact-window
Fourier method used in Coppola--Laporta, *A generalization of Gallagher's
lemma for exponential sums*, arXiv:1411.1739v1 (21 October 2014),
Section 2, compact-weight proof, printed p.5;
[primary PDF](https://arxiv.org/pdf/1411.1739v1). Section 1, printed p.1,
gives the exact Dirichlet-window inequality assessed in review1440.
The theorem is not reproved; the following calculation fixes its local
phase and normalization and exposes the contribution relevant here.

Let F_(Y0)(t)=sum_(k<=N) J_k(Y0)k^(-1/2-it). A finite termwise integral
gives hat(f)(xi)=(exp(i*xi*delta)-1)/(i*xi) F_(Y0)(Yc+xi), with its
continuous value at xi=0. Plancherel and t=Yc+xi therefore give exactly

\[
 E(Y_0)=\frac1{2\pi}\int_{\mathbb R}|F_{Y_0}(t)|^2
       \left(\frac{2\sin((t-Y_c)/(2U))}{t-Y_c}\right)^2dt.
                                                        \tag{6}
\]

At t=Yc the quotient is 1/U. All transforms involve finite arrays;
there is no conditional-series interchange. The integrand in (6) is
nonnegative, so restricting its height range gives a legitimate lower
bound. This does not permit deleting a subset of the coefficients in (5).

### The full frozen prime factor near height zero

Exact multiplication of the finite arrays in (1), with C019y's
injectivity and support check, gives

\[
 F_{Y_0}(t)=A_{Y_0}(t)M(t)^2M(t+h)^2,\qquad
 A_{Y_0}(t)=\sum_{p<r\in P}a_{pr}(Y_0)(pr)^{-1/2-it}.
                                                        \tag{7}
\]

C020h Section 2 proves a_v(Y0)=2i+O(q^-1), uniformly on the original
two heat-time ranges, and Section 3, equation (10), gives
#P comparable to sqrt(X)/q. Retain the actual a_v in (7); choose one
onset so that |a_v-2i|<=1/2 for every v and Y0. For |t|<=1/10,
v/X belongs to [1/100,1/25], hence |t log(v/X)|<=1/2 since log 100<5.
Thus

\[
 \operatorname{Re}\{-i a_v(Y_0)e^{-it\log(v/X)}\}
 \ge2\cos(t\log(v/X))-|a_v-2i|
 \ge2(1-1/8)-1/2\ge1.
\]

Rotate A_(Y0)(t) by the single unit factor -i exp(it q) and sum these
inequalities with positive weights v^(-1/2). Since v<=X/25,

\[
 |A_{Y_0}(t)|\ge\sum_{p<r\in P}(pr)^{-1/2}
 \ge\frac5{\sqrt X}{\#P\choose2}
 \ge c_P\frac{\sqrt X}{q^2}.                            \tag{8}
\]

This pays the whole prime-pair factor on this fixed height interval.
It asserts no common phase or lower bound for the mollifier factor.

### The translated weight does not vanish there

Uniformly for |t|<=1/10,

\[
 \frac{Y_c-t}{2U}\longrightarrow
 \frac{1+\sqrt2}{2(\sqrt2-1)}=\frac32+\sqrt2\in(5/2,3).
\]

Here h/X tends to zero and U is comparable to X, by C020h's unchanged
scales. Eventually this ratio belongs to [5/2,3] and 0<Yc-t<=2X.
Put kappa=min_(r in [5/2,3]) sin r>0; positivity follows from 3<pi
and continuity. Consequently the squared weight in (6) is at least
kappa^2/X^2 throughout this height interval. Combining this with
(7)--(8) and retaining the complete mollifier yields

\[
 E(Y_0)\ge\frac{\kappa^2c_P^2}{2\pi Xq^4}
                 \int_{-1/10}^{1/10}|M(t)M(t+h)|^4dt.
\]

This proves the first bound in (4). Finally B is a fixed positive
multiple of X and U=(B-h)/2 is comparable to X. Therefore
Bq^2/U^2 is comparable to q^2/X, proving the second bound and the
necessary condition, with constants independent of Y0 and d.

No estimate of H_L was used. In particular the diagonal coefficient
norm K1 from C019z does not by itself estimate this fixed low-height
integral; identifying it with a time average would require a separate
argument. A Selberg--Delange estimate for M(t) is not a premise of
this necessary-condition proof; the later application is in C020k.

### Independent conceptual audit1446 — 18 November 2026

This audit retains (1)--(8) and the necessary condition (4) under
unchanged SPECIALIZE assessment1445. The comparison with H_L is made
separately in C020k. It uses only the source coverage already recorded
in1440/1443/1445, not a new theorem or critical-line continuation.

**Original support and phases.** C019y (1) has shifted positions 2
and 4, giving exactly M(t)^2 M(t+h)^2. For large d, every witness
prime exceeds R and lies below both source floors; hence unique
factorization recovers v and s from vs. All of these indices are
at most N=N_*^2 R. Thus the complete finite F factors as (7), with
no discarded diagonal, prime pair, taper or shifted factor. The heat
parameters remain Y0 and Y0+h, not the integration variable t.

For completeness, lambda=log(T/(2pi)) satisfies
d=e^lambda(lambda-1) and

    X^2=2pi^2 e^lambda/(lambda-1),
    q=lambda/2-log(lambda-1)/2+log(2pi^2)/2,
    d/X^2=(lambda-1)^2/(2pi^2).

The first expression for d is strictly increasing for lambda>1 and
unbounded, so q tends to infinity along all positive integers d.
On Z in [X,sqrt(2)X], u(Z)-log p is bounded and t(Z)=O(q^-2).
Consequently E_p(Z)=1+O(q^-2). The phase p^(-ih)=i+O(q^-1),
since log p=q/2+O(1). These uniform bounds verify C020h's
a_v=2i+O(q^-1) for both own heat times. The qualitative PNT in
C020h Section3 gives #P~sqrt(X)/(5q). Only this count is used.

**Finite transform and complete factor.** The transform of the
interval [log k-delta,log k) is
k^(-i xi)(exp(i xi delta)-1)/(i xi). Thus the translation is
Yc+xi, with no conjugation or sign reversal. With the stated angular
Fourier convention the Plancherel factor is 1/(2pi), proving (6).
At xi=0 the multiplier is delta. The finite L1/L2 step function
justifies both this formula and the intersection formula (5).
Only the nonnegative height integrand in (6) is restricted; none
of the signed correlation coefficients is removed.

The rotation -i exp(it q) in (8) leaves each term with real part
at least 2 cos(1/2)-1/2>=5/4, uniformly for |t|<=1/10.
With v<=X/25 and #P tending to infinity, this proves the stated
c_P sqrt(X)/q^2 lower bound for the entire prime factor.

**Weight and simultaneous onset.** The ratio (Yc-t)/(2U) tends
uniformly on this compact interval to 3/2+sqrt(2), strictly between
5/2 and 3. Also 0<Yc-t<=2X eventually. Therefore (6)'s squared
multiplier is at least kappa^2/X^2, where
kappa=min_[5/2,3] sin r>0. Together with (7)--(8), this gives
exactly (4), since Bq^2/U^2 is comparable to q^2/X. The finitely
many onsets can be replaced by their maximum, independent of Y0.

The audit finds no load-bearing error. It verifies a necessary
condition for the sufficient whole-energy estimate only. The height
interval used is disjoint from D eventually, and Gallagher's upper
bound for a norm cannot be reversed to get a norm lower bound.

## Mathlib

Full matching coverage for (4) and this finite coefficient specialization
was not checked. Plancherel and finite-sum manipulation are supporting
standard mathematics, not evidence of a matching Mathlib theorem. No
absence claim is made. The precise inspected source and the Fourier
convention used here are recorded in the proof.
