# C750h: The prescribed prime97 endpoint pair passes the allocation test

## Hypotheses

Let a=9/4, b=log(101)/2, r=(a/b)log(97), w=2a-r and c=a-w/2.
On the real line, with zero extensions and Lebesgue measure, put

    f=1_(-a,-a+w)+1_(a-w,a),
    F(t)=integral_R f(x)exp(-itx)dx,
    J[f]=(1/(2pi))integral_R log(2+|t|)|F(t)|²dt,
    (U_b f)(x)=sqrt(a/b) f(ax/b),
    C_g(s)=integral_R g(x+s)conj(g(x))dx,
    R=(2log(97)/sqrt(97))*|C_(U_b f)(log(97))|/J[f].

These are precisely assessment1140's single prescribed test and
fixed threshold; no width, fraction, parity or neutrality assumption
is changed. The coefficient agrees with bramble_trace, *Source-Gram
control and complete Weil positivity at radius 9/4*, paper162, v1,
15 November2026, [Section2 equation(2)](https://rstation.ai/problems/riemann_hypothesis/papers/162).
Only that convention is used, not the paper's positivity theorem.
C750f/C750g are the local normalization and finite-pilot context;
their sign assertions and certificates are not premises here.

Computer-assisted bounds below assume the installed MPFR4.2.2
implements directed rounding as documented in its
[manual, Section4.4](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Rounding),
and that Python/ctypes implements its documented integer and C ABI
semantics. They are not a formal verification or an independent
critical audit of the implementation.

## Conclusion

The pulse belongs to the stated logarithmic Fourier domain. Its
exact correlation is C_(U_b f)(log97)=w>0. Rigorous enclosures give

    0.2939908 < J[f] < 0.3058314,
    0.11968 < R < 0.12451 < 1/8.                         (1)

Thus this prescribed witness satisfies the allocation. It cannot
refute the all-complex-domain inequality. A passing single pair
neither proves that inequality nor supplies a uniform margin.
The prescribed single-pair search ends here without retuning.
This is a local calculation, not an RH advance or a claim of novelty
beyond the checked literature. Complete-form dilation, J-to-baseline
comparison, all-support positivity and actual-Xi realization remain
unresolved.

## Proof

### Activation, overlap and admissibility

The certificate enumerates all primes p<=101 by integer trial
division up to floor(sqrt(p)), and all their powers <=101. Directed
logarithm comparisons certify 34 with log(n)<9/2 and 35 with n<101;
the set difference is exactly {97}. The boundary n=101 has zero
intersection measure for support in (-b,b). No larger n can overlap.
The saved interval for b lies above23/10>a, so enumeration through101
covers the old radius as well as the new one.
The exhaustive lists are retained in the certificate. These confirm
the source's active-cutoff convention without using numerical signs.

The same directed operations certify 0<w<a and r>w. The pulse centers
are +/-c and r=2c=2a-w. Shifting by r maps the entire left interval
to the right interval; the other three pairings have empty
intersection, up to endpoints of measure zero. Hence C_f(r)=w.
Changing variables y=ax/b in the correlation integral gives
C_(U_b f)(s)=C_f(as/b), including its normalization, so the claimed
correlation follows exactly.

Integrating the two indicators gives

    F(t)=4sin(wt/2)cos(ct)/t,  t!=0;  F(0)=2w,
    J[f]=(16/pi)integral_0^infinity
                  log(2+t)sin²(wt/2)cos²(ct)/t² dt.       (2)

The integrand is bounded near zero and bounded by
(16/pi)log(2+t)/t² for t>=1. Its latter majorant is integrable.
This directly verifies this particular pulse's domain membership;
it does not reprove or require a general nonsmooth-domain theorem.
Equation(2) retains the interference factor cos²(ct) everywhere in
the finite integral.

### Finite quadrature and complete error bounds

Use composite Simpson quadrature with exact mesh h=1/32 separately
on [0,1] and [1,T], T=4096. Each has an even number of subintervals.
For a real C4 function on a panel of length 2h the standard Simpson
error bound is (2h)h^4 sup|G''''|/180. The density G in(2) is smooth
on [0,T] after its removable value at zero is inserted.

On [0,1], differentiating the absolutely integrable double integral
for |F(t)|² is justified by bounded support. Since ||f||_1=2w and
|x-y|<=2a there,

    |(d/dt)^j |F(t)|²| <= 4w²(2a)^j.

Put l_0=log3 and l_p=(p-1)!/2^p for 1<=p<=4. The logarithm's
p-th derivatives have magnitude at most l_p on [0,1]. Thus

    M_low=(4w²/pi)sum_(p=0)^4 binom(4,p)l_p(2a)^(4-p)

bounds |G''''| on [0,1], giving error E_low=h^4 M_low/180.
Here the even-axis density is log(2+t)|F(t)|²/pi, consistently
with(2), including at zero.

On t>=1 write G=(16/pi)A(t)B(t), with A=log(2+t)/t² and
B=sin²(wt/2)cos²(ct). In the finite exponential expansion of B,
the sum of absolute coefficients is at most1, and every frequency
has magnitude at most w+2c=2a. Consequently |B^(j)|<=(2a)^j,
including j=0. Define

    L_0(t)=log(2+t),  L_p(t)=(p-1)!/(2+t)^p, p>=1,
    D_n(t)=sum_(p=0)^n binom(n,p)L_p(t)(n-p+1)!/t^(n-p+2),
    M(t)=(16/pi)sum_(n=0)^4 binom(4,n)(2a)^(4-n)D_n(t).

The product rule bounds |G''''(t)| by M(t). Every D_n and M is
positive and decreasing for t>=1: this is immediate for p>=1;
for p=0, differentiating log(2+t)/t^q, q>=2, gives a negative
derivative since t/(2+t)<1<2log3<=q log(2+t).

For n=0,...,4 a convenient, deliberately loose integral bound is

    integral_1^infinity D_n(t)dt <= Z_n,
    Z_n=(n+1)!*(3/2)log3
          +sum_(p=1)^n binom(n,p)(p-1)!(n-p+1)!/(n+1).

Indeed the p=0 term is at most (n+1)!log(2+t)/t², whose integral
is (n+1)!*(3/2)log3. For p>=1 use (2+t)^(-p)<=t^(-p) and
integrate t^(-n-2) exactly. Let
Z=(16/pi)sum_(n=0)^4 binom(4,n)(2a)^(4-n)Z_n.
For the high panels, decreasing M gives the complete error bound

    E_high <= (h^4/180)*(2h M(1)+Z).                     (3)

To see the sum bound, its first panel contributes 2h M(1), while
each subsequent left-endpoint rectangle lies below the integral
of M over the preceding panel. Extending that integral to infinity
only enlarges the bound. This accounts for every panel, not an
average derivative estimate or a sampling-based error guess.

### Full tail and directed certificate

The positive omitted tail satisfies exactly

    0 <= integral_T^infinity G(t)dt
       <= (16/pi)[log(2+T)/T+(1/2)log(1+2/T)] =: E_tail. (4)

This follows from B<=1 and integration by parts; no omitted tail
is subtracted and no sign of the oscillation is assumed.

Run from this notebook:

    python3 scripts/prime-collar/certify_1142.py

The full certificate is
[certificate-1142.json](../scripts/prime-collar/certificate-1142.json),
produced by [certify_1142.py](../scripts/prime-collar/certify_1142.py).
The script reuses only the MPFR interval arithmetic implementation
in scripts/pivot-area/certify_1136.py. It records both source hashes,
precision384, MPFR version, exact mesh, complete interval cumulative
weighted sums at block boundaries, analytic majorants, errors,
activation lists and every asserted comparison. Products use four
endpoint extrema; nonnegative squares use absolute endpoints;
reciprocals reject zero. Sin/cos endpoint evaluations are widened by
the argument interval width using their global derivative bound1.
All decimal endpoints are again rounded outwards. Binary64 values
are console display only and do not decide a comparison.

The outward Simpson sum, widened by E_low+E_high, and(4) yield

    E_low < 0.0000000070,  E_high < 0.000127234,
    finite integral in [0.2939908910789317,0.2942453711381808],
    E_tail < 0.011585996,
    J in [0.2939908910789317,0.3058313664028087].

The last displayed endpoints have been rounded outwards from the
full decimal certificate, not used as higher precision inputs.
The exact numerator is 2log97*w/sqrt97, enclosed near
0.03660337625361048. Dividing its interval by the strictly positive
full J interval gives

    R in [0.1196848337832045,0.1245051372825803].

These imply(1). The certificate's failures list is empty. The
complete positive tail is loose but sufficient to decide this
single pair below1/8; it is not evidence of a uniform extremum.
The paired intervals, analytic bounds and arithmetic code above
are available for independent audit; none is inferred from a
preview, cutoff-only value or a rounded numerical eigenvalue.

## Mathlib

Full matching coverage was not checked. Supporting ingredients are
indicator integrals, Fourier transformation/translation, finite
Leibniz sums, dominated differentiation and Simpson's quadrature
error formula; no claim of a matching formal theorem or formal
verification is made. Unknown coverage is not evidence of absence.
