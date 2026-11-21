# C020j — Uniform low-height asymptotic for the original tapered mollifier

## Hypotheses

Let alpha be the real multiplicative coefficient sequence defined by
the Euler-product branch of zeta(s)^(-1/2) on Re(s)>1, normalized
positively for real s>1. Thus alpha(1)=1 and
alpha(p^k)=(-1)^k binom(1/2,k). For an integer L>=2 set ell=log L and

\[
 M_L(t)=\sum_{n\le L}\alpha(n)
       \frac{\log(L/n)}{\ell}n^{-1/2-it},\qquad t\in\mathbb R.
\]

The coefficient and taper are exactly those in C019y and C020i;
the present statement holds for every sufficiently large integer L,
independently of those results or the original integer-d prescription.
The proof imports the fixed-parameter Selberg--Delange expansion
specified below. No RH or reciprocal Dirichlet-series continuation
to Re(s)=1/2 is assumed.

## Conclusion

Uniformly for real |t|<=1/5, as L tends to infinity through integers,

\[
 M_L(t)=\frac{L^{1/2-it}}{\ell^{5/2}}
 \left\{\frac{1}{\Gamma(-1/2)(1/2-it)^2}
                  +O\left(\frac1\ell\right)\right\}.       \tag{1}
\]

All implicit constants are absolute. In particular, there is one
absolute integer L0 such that for every integer L>=L0 and |t|<=1/5,

\[
 |M_L(t)|\ge \frac{25}{29\sqrt\pi}
                  \frac{\sqrt L}{(\log L)^{5/2}}.           \tag{2}
\]

The onset is existential; no effective numerical value is claimed.
This is a known-theorem specialization under assessment1443,
classified REPRODUCTION. It does not estimate H_L, audit C020i,
or establish a Gallagher-energy stop, a high-height norm estimate,
actual-Xi positivity or RH. Independent conceptual audit1446 below
retains the specialization; the separate energy application is C020k.

## Proof

### Imported summatory theorem and its applicability

Use R. de la Breteche and G. Tenenbaum, *Remarks on the
Selberg--Delange method*, Acta Arithmetica **200** (2021), no.4,
349--369, [DOI10.4064/aa201024-26-5](https://doi.org/10.4064/aa201024-26-5),
[author-corrected PDF](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf),
Section3.3, formula(3.8), internal p7, with coefficient normalization
from (1.9), internal p2. Their tau_rho are the coefficients of
the Euler-product branch zeta(s)^rho. For fixed complex rho and
fixed nonnegative integer H, the displayed theorem gives

\[
 \sum_{n\le x}\tau_\rho(n)
 =x(\log x)^{\rho-1}
   \left\{\sum_{j=0}^H\frac{\nu_j}{(\log x)^j}
          +O_\rho\left(
            \frac{(bH+1)^{H+1}}{(\log x)^{H+1}}\right)\right\},
 \quad x>2,
\]

where nu_j is the j-th Taylor coefficient of
{w zeta(1+w)}^rho/(1+w), divided by Gamma(rho-j).
Only the fixed case rho=-1/2, H=0 is used. The paper attributes
this classical expansion to G. Tenenbaum, *Introduction to analytic
and probabilistic number theory*, third edition, GSM163, AMS2015,
TheoremII.5.2. We import the displayed expansion, without reproving
Selberg--Delange or claiming to have audited the cited book proof.

Here tau_(-1/2)=alpha exactly. The analytic germ w zeta(1+w)
has value 1 at zero; choose its power with that normalization.
Consequently nu_0=1/Gamma(-1/2). This is permitted by the
complex-rho statement; rho=-1/2 is not a nonpositive integer.
The standard identities Gamma(1/2)=sqrt(pi) and
Gamma(z+1)=z Gamma(z) give

\[
 a_0:=\nu_0=-\frac1{2\sqrt\pi}\ne0.
\]

For precise Gamma references see
[DLMF5.4.6](https://dlmf.nist.gov/5.4.E6) and
[DLMF5.5.1](https://dlmf.nist.gov/5.5.E1).
Thus there are absolute C and x0>2 such that, for every real x>=x0,

\[
 A(x):=\sum_{n\le x}\alpha(n)
 =a_0x(\log x)^{-3/2}+R(x),\qquad
 |R(x)|\le Cx(\log x)^{-5/2}.                              \tag{3}
\]

This applies to the untwisted sequence only. The t dependence will
enter an elementary finite weight; no prime-mean theorem for the
twisted sequence is assumed.

### Exact Abel summation and the small-n range

For k>=1 the local coefficient ratio has modulus
|k-1/2|/(k+1)<1, and |alpha(p)|=1/2. Multiplicativity therefore
gives |alpha(n)|<=1 for all n, hence |A(x)|<=x for x>=1.

Put s=1/2+it and z=1-s=1/2-it. Throughout |t|<=1/5 we have
|s|<1 and Re(z)=1/2. For
w(x)=x^(-s)log(L/x)/ell,

\[
 -w'(x)=\frac{x^{-s-1}}\ell\{1+s\log(L/x)\}.
\]

Finite Abel summation, with A(1^-)=0 and w(L)=0, is exactly

\[
 M_L(t)=\frac1\ell\int_1^L
        A(x)x^{-s-1}\{1+s\log(L/x)\}\,dx.                 \tag{4}
\]

It retains the n=1 term, and the original n=L term has weight zero.
There is no limiting Dirichlet series in (4). Choose L large enough
that ell>=2 and sqrt(L)>=x0. On 1<=x<=sqrt(L),

\[
 \left|\frac{A(x)x^{-s-1}}\ell
                \{1+s\log(L/x)\}\right|
 \le x^{-1/2}\left(|s|+\frac1\ell\right)
 \le 2x^{-1/2}.
\]

Its integral is at most 4L^(1/4), uniformly in t. This controls
the entire small-n part of the exact Abel formula, including its
endpoint contribution; no small-n asymptotic is used.

### Main term and uniform remainder

On sqrt(L)<=x<=L insert (3) into (4) and substitute
v=log(L/x). The main term is

\[
 \frac{a_0L^z}\ell\int_0^{\ell/2}
       e^{-zv}(\ell-v)^{-3/2}(1+sv)\,dv.                  \tag{5}
\]

The error from R is bounded by

\[
 \frac{C\sqrt L}\ell\int_0^{\ell/2}
        e^{-v/2}(\ell-v)^{-5/2}(1+v)\,dv
 \le C2^{5/2}\sqrt L\,\ell^{-7/2}
        \int_0^\infty e^{-v/2}(1+v)\,dv
 =O(\sqrt L\,\ell^{-7/2}).                               \tag{6}
\]

For 0<=v<=ell/2 the real mean-value theorem gives

\[
 |(\ell-v)^{-3/2}-\ell^{-3/2}|
 \le \tfrac32 2^{5/2}v\ell^{-5/2}.
\]

Thus replacing that factor in (5) by ell^(-3/2) costs at most
an absolute constant times

\[
 \sqrt L\,\ell^{-7/2}
       \int_0^\infty e^{-v/2}v(1+v)\,dv,
\]

again finite and uniform. Extending the remaining integral from
[0,ell/2] to [0,infinity) costs at most

\[
 |a_0|\sqrt L\,\ell^{-5/2}
   \int_{\ell/2}^\infty e^{-v/2}(1+v)\,dv
 =|a_0|L^{1/4}\ell^{-5/2}(\ell+6)
 =O(L^{1/4}\ell^{-3/2}).                                 \tag{7}
\]

Since Re(z)=1/2, the completed integral converges absolutely and
can be evaluated directly:

\[
 \int_0^\infty e^{-zv}(1+sv)\,dv
 =\frac1z+\frac{s}{z^2}
 =\frac1{z^2},\qquad z+s=1.                              \tag{8}
\]

Combining (4)--(8) yields, uniformly in t,

\[
 M_L(t)=a_0L^z\ell^{-5/2}z^{-2}
       +O(\sqrt L\,\ell^{-7/2}+L^{1/4}).                 \tag{9}
\]

The ratio L^(1/4)/(sqrt(L)ell^(-7/2)) equals
exp(-ell/4)ell^(7/2), which tends to zero. Absorb it by increasing
one absolute onset and error constant. Because |L^z|=sqrt(L),
(9) proves (1) with an absolute uniform O(1/ell) inside braces.

### Nonzero main term and one uniform onset

For |t|<=1/5 the modulus of the coefficient in (1) is

\[
 \frac1{2\sqrt\pi\,|1/2-it|^2}
 =\frac1{2\sqrt\pi(1/4+t^2)}
 \ge\frac{50}{29\sqrt\pi}.                              \tag{10}
\]

Let K bound the absolute O(1/ell) remainder in (1) for all such t
and all sufficiently large L. Enlarge the integer onset until
K/ell<=25/(29 sqrt(pi)). The reverse triangle inequality and (10)
give (2) simultaneously for the entire compact t interval.
This proves the stated finite-taper target without replacing its
weight or dropping small n. No energy conclusion is drawn here.

### Independent conceptual audit1446 — 18 November 2026

Under unchanged SPECIALIZE assessment1445, this audit retains (1)--(10)
with the original taper and all coefficients. The external expansion
is imported with the precise citation above, as inspected in1443;
the cited book proof is not re-audited or reproved here.

**Branch and summatory scope.** The local Euler factor
(1-p^(-s))^(1/2) gives alpha(p^k)=(-1)^k binom(1/2,k), exactly
tau_(-1/2). The germ w zeta(1+w) equals 1 at w=0, so the
normalized power in the source has constant coefficient 1.
Formula(3.8) with fixed rho=-1/2,H=0 therefore gives (3), with
a0=1/Gamma(-1/2)=-1/(2sqrt(pi)). Negative noninteger rho is
within the inspected complex-parameter statement. No hypothesis
about twisted prime means or convergence at Re(s)=1/2 is added.

**Abel endpoints and error scale.** The coefficient ratio proves
|alpha(n)|<=1, whence |A(x)|<=x. In finite Abel summation the
lower endpoint is A(1^-)=0; the jump at n=1 is included by the
integral from 1, and w(L)=0 disposes of the upper endpoint even
when L is an integer. Differentiation gives exactly (4).
On [1,sqrt(L)] its absolute integral is at most 4L^(1/4).
For the remaining interval choose sqrt(L)>=x0 before using (3).
After x=L exp(-v), the factor is L^(1-s)exp(-(1-s)v)/ell,
giving precisely (5), with Re(1-s)=1/2 uniformly in t.

The R term is bounded as in (6), using
integral_0^infinity exp(-v/2)(1+v)dv=6. The real mean-value
bound for (ell-v)^(-3/2) is valid on all of [0,ell/2]; its
remaining integral is bounded by
integral_0^infinity exp(-v/2)v(1+v)dv=20. Both errors are
O(sqrt(L)ell^(-7/2)), uniformly for |t|<=1/5. The extension
tail is exactly bounded by the expression in (7), since its
unscaled absolute tail integral is (ell+6)exp(-ell/4).
It is O(L^(1/4)ell^(-3/2)) and hence absorbed in (9).

Finally 1/z+s/z^2=1/z^2 because z+s=1. There is no leading
cancellation omitted by the taper. The small-range error is
negligible at the required scale because exp(-ell/4)ell^(7/2)
tends to zero. These estimates establish one absolute uniform
constant K for the O(1/ell) in (1). On |t|<=1/5 the main
coefficient has modulus at least 50/(29sqrt(pi)); choosing
K/ell<=25/(29sqrt(pi)) proves (2) for all sufficiently large
integer L with one common onset. The audit finds no repair needed.

The energy application still requires C020i, both shifted t arguments
and the integer-d scales; none is tacitly assumed in this lemma.

## Mathlib

Full matching coverage of (1)--(3), including negative-half-power
Selberg--Delange and the uniform finite-taper specialization, has
not been checked. No absence claim is made. This informal proof
uses the precise cited summatory theorem and elementary finite
Abel summation; it is not a Lean verification.
