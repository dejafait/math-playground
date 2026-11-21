# L906: the formal inverse fails on the enlarged finite theta domain

## Hypotheses

Use Hedenmalm, *Spectral interpretation of Riemann zeta zeros*,
[arXiv:2606.17494v1](https://arxiv.org/pdf/2606.17494v1), pp2–3,
(1.2.1)–(1.2.3), for the function (w(t)=\Theta_{00}(it^2)), (t>0).
Set (\delta=t\,d/dt), (D=\delta/i), (\phi=-\log w),

\[
Lf=Df+(D\phi)f,\qquad V=\operatorname{span}_{\mathbb C}\{w,Dw\}.
\]

The codomain under consideration is (C^\infty((0,\infty);\mathbb C)).
No inclusion of (V) in the source's spectral span (H_{\rm finite})
is assumed. No Mellin normalization or zero theorem is an input.

## Conclusion

The functions (w,Dw) are smooth and decay at both endpoints faster
than every power, as do all their ordinary derivatives. Also (w>0),

\[
Lw=0,\qquad (LDw)(1)>\frac16.
\]

Consequently the assignment (T(Lu)=-LDu), (u\in V), does **not**
define a representative-independent map on (L(V)), even with the
unrestricted smooth codomain above. This rejects only this enlarged
domain prescription; it says nothing about its validity on
(H_{\rm finite}), other restricted inverses, or positive metrics.

## Proof

**Source inputs and analytical justification.** The cited defining series
and inversion identity give, with (x_n=\pi n^2t^2),

\[
w(t)=t^{1/2}\sum_{n\ge1}P_0(x_n)e^{-x_n},\quad
P_0(x)=2x^2-3x,\quad w(1/t)=w(t).
\]

This is directly the source's series; no identification with the local
kernel K is used. For (t\ge1), all summands are positive, since
(x_n\ge\pi>3/2). Inversion proves positivity for (0<t<1).
On any compact interval ([a,b]\subset(0,\infty)), every fixed-order
derivative of a summand is bounded by a constant times
(n^M e^{-\pi a^2n^2}) for some fixed M. These majorants are summable
(for example their consecutive-term ratio tends to zero). Uniform
convergence of all such derivative series justifies termwise
differentiation and proves smoothness.

In logarithmic derivatives the exact recurrence is

\[
\delta^k w(t)=t^{1/2}\sum_{n\ge1}P_k(x_n)e^{-x_n},\quad
P_{k+1}=(1/2-2x)P_k+2xP_k'.
\]

Here (P_k) has degree at most (k+2), so for (x\ge1),
(|P_k(x)|\le C_kx^{k+2}). For (t\ge1), splitting the exponential
as (e^{-\pi t^2}e^{-\pi(n^2-1)t^2}) gives the complete bound

\[
|\delta^k w(t)|\le C'_k t^{2k+9/2}e^{-\pi t^2},\qquad
C'_k=C_k\pi^{k+2}\sum_{n\ge1}n^{2k+4}e^{-\pi(n^2-1)}<\infty.
\]

Differentiating the exact inversion identity, rather than an asymptotic
error, gives (\delta^kw(t)=(-1)^k(\delta^kw)(1/t)). Thus for (t\le1)
the corresponding bound is (C'_kt^{-2k-9/2}e^{-\pi/t^2}).
Finally (d^j/dt^j=t^{-j}\delta(\delta-1)\cdots(\delta-j+1)).
These estimates prove the asserted endpoint decay for (w,Dw) and
all their ordinary derivatives. They also imply (\delta w(1)=0).
No printed small-t estimate from the source is used.

**Certified one-point sign.** The recurrence yields

\[
P_1=-4x^3+15x^2-\tfrac{15}{2}x,\qquad
P_2=8x^4-56x^3+\tfrac{165}{2}x^2-\tfrac{75}{4}x.
\]

Use the classical Archimedean bounds (3<\pi<22/7).
For (Q(x)=P_2(x)/x), the signs of its terms give

\[
Q(\pi)<8(22/7)^3-56\cdot9+(165/2)(22/7)-75/4
=-20737/1372<-15.
\]

Hence (P_2(\pi)<-45). To bound its exponential factor without
floating point, the series for e gives
(e<8/3+(1/24)/(1-1/5)=87/32<11/4).
The geometric majorant for the exponential series gives
(e^{1/7}<\sum_{j\ge0}(1/7)^j=7/6). Therefore

\[
e^\pi<e^{3+1/7}<(11/4)^3(7/6)=9317/384<27,
\qquad P_2(\pi)e^{-\pi}<-5/3.
\]

For every (n\ge2), put (x=\pi n^2>12). Dropping negative terms,

\[
P_2(x)\le8x^4+(165/2)x^2<9x^4<900n^8,
\]

since (8+165/288<9) and ((22/7)^4<100). Also
(e^3>\sum_{j=0}^8 3^j/j!=89641/4480>20).
If (P_2(x)>0), this implies
(P_2(\pi n^2)e^{-\pi n^2}<900n^8/20^{n^2});
if (P_2(x)\le0), the same upper bound holds trivially.
For (a_n=n^8/20^{n^2}), (n\ge2),

\[
\frac{a_{n+1}}{a_n}
\le\frac{(3/2)^8}{20^5}=\frac{6561}{819200000}<\frac1{100000}.
\]

All derivative series converge absolutely, as proved above. Consequently
their **entire** remaining contribution satisfies

\[
\sum_{n\ge2}P_2(\pi n^2)e^{-\pi n^2}
<\frac{900\cdot256}{20^4}(1-10^{-5})^{-1}
=\frac{16000}{11111}<\frac32.
\]

Combining first term and tail proves (\delta^2w(1)<-5/3+3/2=-1/6).

**Representative failure.** The source's kernel identity
(Lf=wD(f/w)) (Theorem3.3.1 proof, pp5–6) gives (Lw=0).
Its commutator (Remark3.3.2(b), p6) gives
(LDw=-(D^2\phi)w). At (t=1),
(\delta w=0), (\delta^2\phi=-\delta^2w/w), and (D^2=-\delta^2).
Thus (LDw(1)=-\delta^2w(1)>1/6).
The representatives (0,w\in V) have the same L-image, zero,
but the prescribed outputs are respectively zero and (-LDw\ne0).
This is already a failure of well-definedness, without any assertion
that outputs belong to (L(V)).

The exact rational subchecks can be replayed with
`python3 scripts/hedenmalm/finite_domain_kernel_143.py`; the complete
certificate is `scripts/hedenmalm/finite-domain-kernel-143.json`.
Those subchecks supplement the analytical proof above; numerical
sampling and the source's eigenvalue criterion play no role.
This is an elementary specialization of the cited identities, not a
claim of new mathematics beyond the sources checked. ∎

### Independent audit, 8 November 2026 (step144)

The audit passes at the stated scope. The primary version-1 PDF was
checked again at (1.2.1)–(1.2.3), (3.2.1)–(3.2.2), the kernel step
of Theorem3.3.1, and Remark3.3.2(b). In (1.2.3), combining the two
equal nonzero-index summands gives exactly the displayed P_0, with
no extra factor of two. The inversion acts on t as t maps to 1/t.
No Mellin identity, eigenfunction characterization or printed
small-t estimate is needed.

Independently collecting coefficients in the displayed recurrence
gives P_1=(-15/2)x+15x^2-4x^3 and
P_2=(-75/4)x+(165/2)x^2-56x^3+8x^4, agreeing with the proof
and the complete certificate's polynomial entries. The negative-term
inequality for Q uses pi^2>9; after Q(pi)<-15, multiplication by
pi>3 gives P_2(pi)<-45. Since exp(-pi)>1/27, multiplying this
negative bound gives a first contribution less than -5/3, with the
required direction. The e-series remainder starts at 1/4!, with
successive ratio at most 1/5; thus its geometric majorant 5/96 is
valid. The exponential lower bound uses the full finite sum through
degree eight, not a rounded decimal.

For n>=2 the upper polynomial bound remains valid even if P_2 is
negative; no lower tail bound is needed. Its ratio majorant applies
to every n>=2, since (1+1/n)^8 decreases and 20^(2n+1)
increases. The resulting complete tail bound is 16000/11111,
strictly below 3/2. Replaying the script and inspecting the full
selected certificate entries `/polynomials`, `/bounds`,
`/all_passed` and `/failures` gave nine passing rational comparisons,
the matching polynomial, and no failures. In particular the stronger
recorded upper bound is -7555/33333<-1/6. This checks the arithmetic;
the analytical argument above is still essential.

That analytical argument also passes: fixed-order compact derivative
majorants are summable; the large-t bound retains the entire n-tail;
and differentiation of the exact inversion supplies all small-t
logarithmic derivatives. The ordinary-derivative identity then handles
both w and Dw, including arbitrary further derivatives. Positivity
makes phi smooth on the open interval. No endpoint control of phi
itself or closure of V under D is assumed or required for the stated
smooth codomain.

Finally the commutator has sign LD-DL=-(D^2 phi), while
D^2=-delta^2. With delta w(1)=0 these give LDw(1)=-delta^2w(1),
as claimed. The two representatives 0 and w both lie in V and have
zero L-image, yet yield distinct outputs. There is no premise that
w belongs to H_finite. The audit therefore validates retirement of
this V prescription only; it supplies neither a positive metric nor
a theorem about the source's finite spectral domain. This is local
verification of the source specialization, not a new literature result.

## Mathlib

Full matching and supporting theorem coverage is unchecked. No absence
claim is made. This proof does not depend on a Mathlib implementation.
