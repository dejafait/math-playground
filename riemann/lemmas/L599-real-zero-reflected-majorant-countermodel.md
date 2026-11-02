# Lemma 599: a real-zero comparison with a negative reflected defect

## Hypotheses

Use the Fourier convention F(x)=integral_R k(u) exp(ixu)du. Set

    g(u)=exp(-u^2/8)/sqrt(8*pi),
    k(u)=g(u)(11/16+u^2/32+u^4/256),
    A(t)=integral_R s^2 k(s+t)k(s-t)ds,
    G(t)=integral_t^infinity A(v)dv,                 t>=0,
    S_h(r)=sum_(m>=0) (-1)^m G(r+mh),               0<=r<=h,
    D_h(r)=G(0)-S_h(r)-S_h(h-r),                    h>0.

The alternating series is its full absolutely convergent series, equivalently
the paired definition in L598. No actual-theta hypothesis is made.

## Conclusion

The kernel k is strictly positive, real, even and Schwartz, and

    F(z)=(1-z^2)^2 exp(-2z^2)

belongs to the Laguerre–Pólya class, with only the double zeros +/-1.
The associated A is positive, even and Schwartz and has nonnegative Fourier
transform at every real frequency. Nevertheless, at h=pi/2 and r=pi/4,

    (2/pi)[-(4736/3)exp(-36)-156250exp(-100)]
      < D_(pi/2)(pi/4)
      < (2/pi)[-(4736/3)exp(-36)+156250exp(-100)]
      < -(4736/(3*pi))exp(-36) < 0.

Thus positive even Schwartz input and a Laguerre–Pólya transform do not force
L598's pointwise reflected condition. This refutes only that generic
implication. It gives no negative actual-theta value, no failure of the
sine-weighted sufficient inequality, and no conclusion about RH.

## Proof

### Imported results and kernel verification

Import the Gaussian Fourier pair, differentiation, inversion and Schwartz
periodization from A. W. Knapp, *Basic Real Analysis*, digital second edition
(2016), Chapter VIII, Proposition 8.1(f,g), pp.413–414, Proposition 8.2,
pp.416–417, Theorem 8.4, p.418, Proposition 8.10, p.423, and Theorem 8.15,
pp.427–428. [Primary text](https://www.math.stonybrook.edu/~aknapp/download/b2-realanal-inside.pdf).
Its convention exp(-2*pi*i*u*y) converts to ours by y=-x/(2*pi).
In particular the normalized pair is

    integral_R g(u) exp(ixu)du=exp(-2x^2).

All moment and derivative integrability hypotheses hold for the
polynomial-Gaussian functions below. Their derivatives vanish at infinity.
Consequently spatial differentiation twice multiplies the transform by
-x^2, and differentiation four times multiplies it by x^4. Directly,

    g''/g=u^2/16-1/4,
    g''''/g=u^4/256-3u^2/32+3/16,
    g+2g''+g''''=k.

The transform is therefore (1-2x^2+x^4)exp(-2x^2)=F(x); inversion applies
since both k and F are Schwartz. The displayed polynomial in k has a
strictly positive constant and nonnegative coefficients, so k is strictly
positive, real and even. Polynomial times Gaussian decay proves the
Schwartz property and L233's decay bound for every exponential rate.
Compact sets of complex z are dominated by an integrable
polynomial-Gaussian times exp(M|u|); the transform is entire and agrees
with the displayed entire F.

For class membership import Definition 1.1 in G. Csordas,
*Fourier Transforms of Positive Definite Kernels and the Riemann xi-Function*, arXiv:1309.0055v2
(21 February 2014), p.2, with the first Laguerre inequality (2.1).
[Versioned primary source](https://arxiv.org/pdf/1309.0055v2).
The finite real factors (1-z)^2(1+z)^2 times exp(-2z^2) have exactly the
allowed form: in canonical factors with roots 1,1,-1,-1 the exponential
linear factors cancel. The Gaussian parameter is 2>=0. This verifies
membership directly from that definition; no new class theorem is proved.
The stronger super-Gaussian decay in that source's Definition 1.2 is not
assumed, and its admissible-kernel theorem package is not invoked.

### Associated transform and regularity

Since k is polynomial times g,

    k(s+t)k(s-t)
      = (1/(8*pi)) exp(-s^2/4-t^2/4) p(s+t)p(s-t),
    p(u)=11/16+u^2/32+u^4/256.

Integration after multiplication by s^2 yields a polynomial in t times
exp(-t^2/4). This follows term by term from finitely many absolutely
integrable Gaussian moments; it also justifies every t derivative.
Thus A is Schwartz. The defining integrand shows A(t)>0 and A(-t)=A(t).
In particular integral_0^infinity (1+t)A(t)dt is finite, so L598's
convergence/endpoint argument applies.

L233, with its full-line normalization, gives

    Ahat(2x)=[F'(x)^2-F(x)F''(x)]/4,
    Ahat(xi)=integral_R A(t)exp(i*xi*t)dt.

To check this specialization's factor independently, put u=s+t and
v=s-t. The absolute Jacobian is 1/2 and s^2=(u+v)^2/4, so

    Ahat(2x)=(1/8) integral_R integral_R
                  (u+v)^2 k(u)k(v)exp(ix(u-v))du dv.

The absolute integrand is bounded by an integrable polynomial times
exp(-(u^2+v^2)/8). Fubini is therefore applicable. The u^2 and v^2
terms each give -F F'', and 2uv gives 2F'^2, yielding the stated 1/4.
This checks the use of L233; its other conclusions are unnecessary here.

For P(x)=(1-x^2)^2, differentiation of F=P exp(-2x^2) gives

    F'^2-FF''=exp(-4x^2)[P'^2-PP''+4P^2]
             =4exp(-4x^2)(1-x^2)^2(x^4-x^2+2).

Hence

    Ahat(2x)=(1-x^2)^2(x^4-x^2+2)exp(-4x^2).           (1)

This is nonnegative, since x^4-x^2+2=(x^2-1/2)^2+7/4.
It is also consistent with the imported first Laguerre inequality;
the polynomial calculation is needed for the exact Fourier coefficients,
not as a reproof of that general inequality.

### Reflection, periodization and integration constant

Here are the convergence and endpoint checks from L598 in this
specialization. Tonelli gives integral_0^infinity G(t)dt=
integral_0^infinity tA(t)dt<infinity. G is nonnegative and decreasing.
For m>=1,

    hG(mh)<=integral_((m-1)h)^(mh) G(t)dt.

Thus sum_(m>=0)G(mh)<infinity. Since G(r+mh)<=G(mh), the S_h
series is absolutely uniformly convergent on [0,h]. Absolute cancellation
gives S_h(0)+S_h(h)=G(0), so D_h(0)=0. These arguments use only the
convergence/endpoint portion of L598; its numerical theta estimates play
no role. Checking this portion here fixes the reconstruction constant
without promoting the rest of that unaudited lemma.

Because A is Schwartz, sum_(m>=0) A(r+mh) converges uniformly on [0,h].
With G'=-A, termwise differentiation of S_h is valid. For 0<r<h,

    D_h'(r)=sum_(m>=0)(-1)^m A(r+mh)
                -sum_(m>=0)(-1)^m A(h-r+mh)
            =sum_(m in Z)(-1)^m A(r+mh).              (2)

The negative indices in the last sum are m=-j-1; evenness of A gives
their terms as -(-1)^j A(h-r+jh), proving the sign in (2).
Uniform convergence also extends these derivatives to the endpoints.

Apply Knapp's Schwartz periodization theorem to A, scaled to period 2h.
Its Fourier coefficients, using evenness to remove the convention's
minus sign, give

    R_h(r):=sum_(j in Z) A(r+2jh)
       =(1/(2h))sum_(n in Z) Ahat(n*pi/h)exp(i*n*pi*r/h).

Both spatial and frequency series, and the needed differentiated series,
converge uniformly on compact r intervals. The alternating sum in (2)
is R_h(r)-R_h(r+h). Subtracting removes even n and doubles odd n;
pairing +/-n gives

    D_h'(r)=(2/h)sum_(n>=1, n odd) Ahat(n*pi/h)cos(n*pi*r/h).

Uniform absolute convergence permits integration from 0 to r. The already
verified D_h(0)=0 leaves no free constant. Therefore

    D_h(r)=(2/pi)sum_(n>=1, n odd)
                   [Ahat(n*pi/h)/n]sin(n*pi*r/h).     (3)

This periodizes the Schwartz function A, not a half-line extension of G.
No unproved smoothness of such an extension is used.

### The fixed pair and its complete remainder

At h=pi/2, (1) gives

    Ahat(n*pi/h)=(1-n^2)^2(n^4-n^2+2)exp(-4n^2).

At r=pi/4 the sine in (3) is sin(n*pi/2). The n=1 term is exactly
zero and the n=3 term is exactly -(4736/3)exp(-36), inside the
factor 2/pi. Write the sum of *all* remaining odd terms n>=5 as E.
For n>=5,

    0<[(1-n^2)^2(n^4-n^2+2)/n]<=n^7,

because (n^2-1)^2<=n^4 and n^4-n^2+2<=n^4. Put b_n=n^7 exp(-4n^2).
For consecutive odd indices n>=5,

    b_(n+2)/b_n=((n+2)/n)^7 exp(-16n-16)
       <=(7/5)^7 exp(-96)<2^7*2^(-96)=2^(-89)<1/2.

Only e>2 is used in this strict rational comparison. Thus the entire
absolute remainder, including arbitrarily high odd indices, satisfies

    |E|<=sum_(n>=5, n odd)b_n<2b_5=156250exp(-100).

Its ratio to the magnitude of the negative third term is strictly less
than

    (468750/4736)exp(-64)<100exp(-64)<100/2^64<1/2.

Substituting this complete bound in (3) proves the two-sided enclosure
and its strict negative upper bound in the conclusion. There is no
finite-grid, quadrature, numerical rounding or deleted-tail inference.

### Verification and qualifications

`python3 scripts/reflected-majorant/fixed_pair.py` checks the Gaussian
derivative polynomials, the spectral polynomial, the zero first term,
the third coefficient and the exact rational comparisons. It writes the
full supporting certificate to
`scripts/reflected-majorant/fixed-pair-certificate.json`. It does not
mechanically verify the analytic imports or interchanges; those are
justified above. The proof is analytic and does not depend on numerical
approximations to pi or e.

Independent audit, 31 October 2026: checked all moment/derivative and
Schwartz hypotheses, the entire extension and finite canonical factors,
the Jacobian and Fourier conventions, the negative-index sign and odd-mode
factor, uniform convergence and the endpoint constant, and every odd
index in the remainder estimate. Replayed the script and inspected its
complete derivative polynomials, spectral polynomial and rational checks.
All eight checks pass, with no failures. The rigorous relative-tail bound
is 25/4611686018427387904, strictly below the required 1/2. The audit
retains the two-sided enclosure and negative conclusion without a
mathematical correction; the source title above is corrected. It does
not audit the rest of L598 or the cited manuscripts generally.

This is local progress on an overstrong sufficient condition. The checked
source comparison found no exact matching countermodel; originality is
not certified. The countermodel supplies no actual-Xi signed estimate,
and every actual-Xi first-sign and all-degree gap remains unresolved.

## Mathlib

Supporting Schwartz periodization is present as
`SchwartzMap.tsum_eq_tsum_fourier` and
`Real.fourierCoeff_tsum_comp_add` in the
[official source at a151a9c425dad802e4e1578282116f26004739b8](https://github.com/leanprover-community/mathlib4/blob/a151a9c425dad802e4e1578282116f26004739b8/Mathlib/Analysis/Fourier/PoissonSummation.lean),
as recorded in the prior assessment. This supports periodization only.
Full matching comparison coverage and Laguerre–Pólya coverage have not
been checked; no absence is inferred. No Lean verification is claimed.
