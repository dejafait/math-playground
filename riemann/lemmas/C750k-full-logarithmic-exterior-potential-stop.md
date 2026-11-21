# C750k: The full logarithmic exterior potential cannot pay prime97/8

## Hypotheses

Set a=9/4, b=log101/2, r=(a/b)log97, w=2a-r,
k=2log97/sqrt97, I=(-a,a),
I_L=(-a,-a+w), I_R=(a-w,a), and E=I_L union I_R.
Use Lebesgue measure, complex L2 spaces, and almost-everywhere zero
extension outside I. With the Fourier transform interpreted in L2,
put

    F_f(t)=integral_R f(x)exp(-itx)dx,
    J[f]=(1/(2pi))integral_R log(2+|t|)|F_f(t)|^2dt,
    D_a={f in L2(R): f=0 a.e. outside I, J[f]<infinity}.

For supported L2 inputs the displayed Fourier integral also exists
pointwise since f is L1. The fixed support, collars, coefficient and
allocation are those of C750i. In particular C750i supplies the
geometry 0<w<a, r>w and the exact complex pairing/dilation bound

    C_(U_b f)(log97)=C_f(r),
    |C_f(r)| <= (1/2)integral_E |f|^2,
    (U_b f)(x)=sqrt(a/b)f(ax/b),
    C_f(s)=integral_R f(x+s)conj(f(x))dx.                (1)

No parity, neutrality, continuity of f, boundary trace, or equality
of killed and subordinated operators is assumed. Assessment1150,
completed in source review1151, approves precisely this exterior-only
specialization. No parameters or allocation fraction are optimized.

## Conclusion

Define, for z!=0 and d>0,

    j(z)=(1/pi)integral_0^infinity exp(-2s)/(s^2+z^2) ds,
    H(d)=(1/pi)integral_0^infinity
                         exp(-2s) arctan(s/d) ds/s,
    V_I(x)=log2+H(a-x)+H(a+x),  x in I.

For every f in D_a there is the exact identity

    J[f]=integral_I V_I(x)|f(x)|^2 dx
          +(1/2)integral_(I x I)
                       |f(x)-f(y)|^2 j(x-y) dx dy.       (2)

Both terms are nonnegative and finite. The identity also holds as an
extended nonnegative equality for all supported L2 inputs. Values on
the double integral's diagonal may be set to zero.

However, on the two open intervals

    A_R=(a-1/32,a-1/64),  A_L=-A_R,

which are contained in the unchanged E and together have measure1/32,

    V_I(x) < 137/40 < 18/5 < 4k,
    4k-V_I(x) > 7/40.                                  (3)

Consequently V_I>=4k a.e. on E is false. This stops the proposed
exterior-only mass certificate, not the original allocation
k|C_(U_b f)(log97)|<=J[f]/8: the nonnegative interior term in(2)
has been discarded by that certificate. No original-domain violating
witness or RH consequence is obtained. This is a known-method local
specialization and an informative negative test, not a claim of
originality beyond the sources checked. Correctness audit1154 below
confirms the identity and this restricted stop, with the source-domain
qualification corrected explicitly.

## Proof

### Imported form and kernel inputs, with the required scale

Import the zero-drift subordinate form and its domain from
Chen–Song, *Two-sided eigenvalue estimates for subordinate processes
in domains*, J. Funct. Anal.226(2005),90–113,
DOI10.1016/j.jfa.2005.05.004,
[Section2(2.5)–(2.7), printed pp94–96](https://rsong.web.illinois.edu/pages/evest.pdf).
For the whole-line conservative symmetric Cauchy semigroup P_s,
the cited real form is integral_0^infinity <u-P_su,u> nu(ds),
with jump measure (1/2)dx integral p_s(x-y)nu(ds)dy and no
killing term. Its form domain consists of the L2 functions for which
this nonnegative energy is finite, as stated in(2.6). This is an L2
form-domain assertion, not an identification of the possibly larger
extended Dirichlet space. The hypotheses hold on R with Lebesgue
measure and the usual symmetric Cauchy process: R is Lusin,
Lebesgue measure has full support and is sigma-finite, and this
process is conservative and symmetric. The subordinator is independent;
the zero-drift Levy-measure condition is verified below.

The normalized density is

    p_s(z)=s/[pi(s^2+z^2)],
    Fourier multiplier of P_s = exp(-s|t|).

The density normalization is imported from Jacob–Knopova–Landwehr–
Schilling, *A geometric interpretation of the transition density of
a symmetric Levy Process*, arXiv:1105.5016v1,
[(1.1), printed p1](https://arxiv.org/pdf/1105.5016v1).
Only this density is used; the additional integrability assumptions
and conclusions of its Theorem7.1 are not invoked.
The rate-one gamma Levy measure exp(-s)ds/s and exponent
log(1+lambda), including stable exponent |t| for alpha=1, are
imported from Grzywny–Ryznar, *Potential theory of one-dimensional
geometric stable processes*, arXiv:1107.0745v1,
[Section2, printed pp2–4](https://arxiv.org/pdf/1107.0745v1).

Here the required measure is instead nu_2(ds)=exp(-2s)ds/s.
It satisfies integral(1 wedge s)nu_2(ds)<infinity, since its density
times s is bounded near zero and it decays exponentially at infinity.
The standard Frullani integral, for positive parameters, gives

    integral_0^infinity exp(-2s)(1-exp(-s u)) ds/s
        =log((2+u)/2),  u>=0.                           (4)

Equivalently substitute v=2s into the rate-one gamma identity to
obtain log(1+u/2). Thus nu_2 supplies log(2+u)-log2;
the additive log2 must be restored separately. There is no drift
term. Substituting p_s and nu_2 into the cited jump measure gives
exactly j above and the factor1/2 in the whole-line difference form.
This is the necessary rate/constant specialization, not a reproof
of general subordination theory.

### Complex domain and both exterior orientations

For completeness identify the precise domain directly, avoiding any
identification of a part-process domain by boundary capacity.
For f in complex L2, Plancherel and(4), with nonnegative Tonelli,
give the extended equality

    J[f]-log2||f||_2^2
      =integral_0^infinity
         [||f||_2^2-<f,P_s f>] exp(-2s) ds/s.           (5)

The left side means the integral of log((2+|t|)/2)|F_f|^2/(2pi),
so no infinity-minus-infinity occurs. Each bracket is real and
nonnegative by the multiplier exp(-s|t|). The real symmetric
semigroup identity is

    ||u||_2^2-<u,P_su>
        =(1/2)integral_(R x R)|u(x)-u(y)|^2 p_s(x-y)dxdy.

It follows either from the imported form or from expanding the
square, using integral p_s=1 and symmetry. All expanded terms are
integrable: the two square terms integrate to ||u||^2 and the cross
term is absolutely integrable by 2|u(x)u(y)|<=|u(x)|^2+|u(y)|^2.
For f=u+iv the right side is the sum of the two real forms, since
|f(x)-f(y)|^2=|u(x)-u(y)|^2+|v(x)-v(y)|^2. The Fourier multiplier
is real and preserves real functions, so the brackets also add.
This justifies the complex extension on the full domain, rather
than assuming a real-valued theorem already covers complex phases.

Applying Tonelli again in(5) now gives

    J[f]=log2||f||_2^2
           +(1/2)integral_(R x R)|f(x)-f(y)|^2j(x-y)dxdy. (6)

The kernel is finite for z!=0, as follows directly by bounding the
small-s denominator below by z^2 and using exponential decay.
No finiteness on the measure-zero diagonal is needed. Equality(6)
identifies the finite-J domain exactly, including nonsmooth inputs.
It also shows finiteness of each retained nonnegative term when
f belongs to D_a.

For f=0 a.e. on I complement, the exterior-exterior contribution
vanishes. The I x I-complement contribution and its reverse are
equal by symmetry; their sum cancels the factor1/2. Hence the
exterior coefficient is integral_(R\I)j(x-y)dy, not half this value.
For d>0, nonnegative Tonelli and the elementary Cauchy tail give

    integral_d^infinity j(z)dz
       =(1/pi)integral_0^infinity exp(-2s)
                                arctan(s/d) ds/s = H(d).

The two exterior distances are a-x and a+x. Restoring log2 proves
(2) with the stated V_I. For all d>0, arctan(s/d)<=s/d also gives
H(d)<=1/(2pi d); in particular V_I is finite throughout I and
V_I>=log2 everywhere there. Dominated convergence on d>=delta>0,
with majorant exp(-2s)/delta, also proves H is continuous. The later
interval bound is direct and does not rely on a sampled value,
continuity extension, or an assertion about a minimum at an edge.
No killed-before-subordination operator has been substituted for(6).

### A fixed positive-measure collar interval with insufficient potential

First verify that the specified strips lie inside the original
collars. The integral of 1/t over [1,1+x] gives
log(1+x)>x/(1+x) for x>0. Also log101<5: the exponential series
gives e>8/3 and (8/3)^5=32768/243>101. Therefore

    w=(9/2)log(101/97)/log101
       >(9/2)*(4/101)/5=18/505>1/32.                  (7)

For x in A_R put d=a-x. Then 1/64<d<1/32<w and
D=a+x=9/2-d>4. Thus x lies in I_R, and reflection treats A_L.
For any 0<d<1 split H's integral into (0,d), (d,1), (1,infinity).
Use respectively arctan(s/d)<=s/d, arctan(s/d)<=pi/2, and
arctan(s/d)<=pi/2 together with 1/s<=1 on the last interval.
Keeping the exponential on the last interval gives

    H(d) <= 1/pi +(1/2)log(1/d)+exp(-2)/4
          < 1/pi +(1/2)log(1/d)+1/4.                 (8)

For the distant exterior H(D)<=1/(2pi D)<1/(8pi).
The elementary bounds pi>3 and log2<7/10 are enough. For the latter,
the positive exponential series gives
exp(7/10)>1+7/10+(7/10)^2/2+(7/10)^3/6=12013/6000>2.
Since log(1/d)<log64=6log2, (8) yields throughout A_R

    V_I(x) < 4log2+1/pi+1/4+1/(8pi)
             < 14/5+1/3+1/4+1/24=137/40.             (9)

For the threshold, the exponential series gives e<11/4:
n!>=2*3^(n-2) for n>=2, with strict inequality for n>=4,
so e=2+sum_(n>=2)1/n!<2+(1/2)sum_(m>=0)3^(-m)=11/4.
As 11/4<25/9, sqrt(e)<5/3. Consequently

    exp(9/2)=e^4 sqrt(e)<(11/4)^4*(5/3)=73205/768<97.

Thus log97>9/2, and sqrt97<10 implies

    4k=8log97/sqrt97>8*(9/2)/10=18/5.

Reflection leaves V_I invariant. This proves(3) on both intervals,
including the uniform deficit7/40 and their positive measure.
All bounds are elementary exact inequalities; no quadrature, mesh,
floating-point evaluation, or endpoint approximation is used.

### Scope of the failed certificate

If V_I>=4k a.e. on E, its nonnegativity elsewhere and(2) would give
J[f]>=4k integral_E|f|^2>=8k|C_(U_b f)(log97)| by(1).
The pointwise premise is false on A_L union A_R. This is precisely
the approved abandonment test for this sufficient certificate.
We do not reverse the lower comparison in(2), assert that it is
optimal, or remove the nonnegative interior energy from the original
allocation. C750i's whole-line inverse and C750j's cap stop are
historical contrasts, not premises for this negative test; only
C750i's exact supported pairing/geometry is used in(1).

The full-J allocation, the complete dilation budget, old shifts,
pole/digamma costs, J-to-baseline comparison, both sectors, all
supports and actual-Xi realization at L030–L032/C032a remain open.

### Correctness audit1154 — 16 November2026

This separate conceptual audit uses the unchanged SPECIALIZE coverage
in assessment1152, approved1153, and the primary statements and proof
cases already inspected in1150/1151. It verifies the entire argument
above, including the complex L2 domain and strict inequalities. It
does not claim a new result beyond this known-method specialization.
The original source paragraph called its finite-energy set an
"extended form domain"; that wording is corrected above. Chen–Song
(2.6) specifies L2, and no non-L2 extended-space claim is retained.
The extended equalities(5)–(6) instead allow the value infinity while
the input remains in L2. Their meaning and all conclusions are unchanged.

The following checks make the analytic and arithmetic scope explicit.
For every s>0, p_s has integral1 and is even. Its convolution is a
real-preserving self-adjoint contraction. For real u,v in L2,
the absolute integral of u(x)v(y)p_s(x-y) is at most
(||u||_2^2+||v||_2^2)/2, by the elementary product inequality and
Tonelli. Hence symmetry gives <u,P_s v>=<v,P_s u>, so the imaginary
cross terms in <u+iv,P_s(u+iv)> cancel. This justifies the bracket
splitting in(5) for all complex L2 inputs, without pointwise Fourier
decay or a smooth approximation assertion. For fixed s, Plancherel
gives the multiplier1-exp(-s|t|)>=0. Nonnegative Tonelli and Frullani
therefore apply even when the integrated energy is infinite.
The removed quantity log2||f||_2^2 is always finite. The rate-two
measure gives log((2+|t|)/2), so (6) has precisely the stated log2
term and kernel j, with no drift or hidden constant.

For supported f, both exterior orientations are equal nonnegative
integrals. Their sum times1/2 is one full exterior potential; this
remains valid for infinite energy. Endpoints and the diagonal are
Lebesgue-null, and an a.e. zero extension suffices. The Cauchy-tail
integral is arctan(s/d)/s, not arctan(d/s)/s. Thus both distances
a-x and a+x and the factor1/pi in H are correct. No part-process
domain, boundary capacity or killing/subordination commutation is
used. Each term in(2) is finite when J is finite because both are
nonnegative. These checks cover nonsmooth inputs as well.

C750i is used only for its exact conventions and pairing(1), not its
computer-assisted inverse bound. Its geometry can also be checked
here exactly: 97<101 and 97^2>101 imply
1/2<log97/log101<1, hence a<r<2a, 0<w<a and r>w.
The overlap of I and I-r is I_L, and I_L+r=I_R. Thus
C_f(r)=integral_(I_L) f(x+r)conj(f(x))dx; integrating
2|f(x+r)f(x)|<=|f(x+r)|^2+|f(x)|^2 yields(1).
The substitution y=ax/b cancels the dilation Jacobian with a/b.
No numerical geometry certificate or platform hypothesis is needed.

For(7), the integral estimate for log(1+x) is strict for x>0.
The terms through degree3 in e sum to8/3 and the remaining terms
are positive; 32768>101*243 proves log101<5. The last comparison
18/505>1/32 is exactly576>505. On A_R, d is in(1/64,1/32)
and D=9/2-d>143/32>4; A_R is therefore inside I_R.
Reflection gives the identical inclusion and bounds on A_L. Each
interval has length1/64 and they are disjoint, giving total measure1/32.

For(8), the three pieces are bounded respectively by1/pi,
(1/2)log(1/d), and exp(-2)/4. The last bound uses 1/s<=1 for
s>=1 before integrating exp(-2s), so its factor1/4 is correct.
Replacing exp(-2) by1 is strict; the distant bound is strictly
below1/(8pi). The displayed exponential polynomial for log2 has
numerator12013>12000, and d>1/64 gives log(1/d)<6log2.
Consequently(9) follows with the exact sum
14/5+1/3+1/4+1/24=137/40.
For the other strict threshold, n!>=2*3^(n-2) with a strict term
at n=4 proves e<11/4; 99<100 proves11/4<25/9;
and73205<74496=97*768 proves exp(9/2)<97.
Together with sqrt97<10 these give4k>18/5=144/40.
Thus4k-V_I>7/40 on the entire two-interval set, not only at sampled
points. All stated strict inequalities and the positive-measure
obstruction survive the audit; no numerical script was required.

The logical direction of the stop is also correct: a pointwise
floor4k would imply the sufficient mass estimate using(1)–(2).
Its failure does not reverse(2) or refute the original allocation.
The interior jump energy remains available to a different mechanism.
The audit establishes no positivity for the complete Weil form or
actual Xi.

## Mathlib

Full matching coverage was not checked. Supporting ingredients are
Plancherel, nonnegative Tonelli, complex L2 real/imaginary splitting,
Frullani's integral, exponential series and elementary arctangent
integration. The primary subordinate-form citations are informal
inputs; no matching formal theorem or formal verification is claimed.
Unknown Mathlib coverage is not evidence of absence.
