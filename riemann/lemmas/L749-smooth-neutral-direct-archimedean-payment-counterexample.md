# L749: Smooth exact-neutral counterexample to direct archimedean payment

## Hypotheses

Put b=2log3, L=2b=4log3 and delta=L/40. For real s define
eta(s)=exp(-1/s) for s>0 and eta(s)=0 otherwise, and put

    theta(s)=eta(s)/(eta(s)+eta(1-s)),
    chi(x)=theta((x-delta)/delta)*theta((L-delta-x)/delta),
    phi_k(x)=chi(x)sin(k*pi*x/L),  k=1,...,6.

Use zero extensions to R, the Fourier convention
F_f(t)=integral_R exp(-itx)f(x)dx, and precisely the archimedean
part of L744 (6):

    m(t)=Re psi(1/4+it/2)-log pi,
    A(f)=integral_R m(t)|F_f(t)|^2dt/(2pi).                 (1)

For h(y)=f(y+b), use L748's entire resource

    W_b(h)=R(h)+integral_(-b,b) log(b/|y|)|h(y)|^2dy,
    R(h)=(1/4) integral_(R x R)
       |sqrt(|y|)h(y)-sqrt(|z|)h(z)|^2
                         /(|y-z|sqrt(|yz|)) dy dz.         (2)

Every exterior pair is included. L748's audited conclusion gives
W_b(h)>=C_*||h||_2^2 with C_*>2, and its identity (5) establishes
the full resource normalization and finiteness on the smooth class.

External analytic inputs are the standard named Plancherel theorem,
its smooth Fourier derivative identity, Jensen's inequality for the
concave logarithm, and the digamma recurrence and remainder:
[NIST DLMF5.5.2](https://dlmf.nist.gov/5.5.E2),
[5.11.2](https://dlmf.nist.gov/5.11.E2) and the first paragraph of
[5.11(ii)](https://dlmf.nist.gov/5.11.ii), version1.2.8, release
15 September2026, directly inspected 4 November2026. The n=1 complex
remainder gives, for Re w>0 and the principal logarithm,

    psi(w)=log w-1/(2w)+rho(w),
    |rho(w)|<=sec^3(arg(w)/2)/(12|w|^2).                    (3)

The saved EXPLORE assessment covers one witness screen in this fixed
six-mode space, including replacement of numerical evaluation by
complete analytic estimates. Its earlier source comparison did not
establish this counterexample. The recurrence is a standard scalar
evaluation input, not a new payment theorem; no uncertainty theorem
or digamma expansion is reproved here.

## Conclusion

Define exact real integrals and an exact function by

    M_k=integral_0^L exp(x/2)phi_k(x)dx,  k=1,3,
    f=phi_3-(M_3/M_1)phi_1,       h(y)=f(y+b).              (4)

Then M_1>0, f is nonzero and real in C_c^infinity(0,L), and

    integral_0^L exp(x/2)f(x)dx
      =integral_0^L exp(-x/2)f(x)dx=0.                     (5)

Writing N=||f||_2^2=||h||_2^2>0, the analytic certificate is

    ||f'||_2^2/N<5050/59<100,
    A(f)<(43/50)N,       W_b(h)/2>N,
    A(f)-W_b(h)/2<-(7/50)N<0.                             (6)

Thus A>=W_b/2 fails in the approved trial space and hence in the
full complex globally neutral smooth class at this window. This is
an informative negative result for that sufficient payment inequality,
not a disproof of RH, a counterexample to full Weil positivity, or
a refutation of L748's allocation Q_2<=W_b/2. In particular (6)
does not compare A with Q_2. Other prime powers, signed complements
and support propagation remain open.

The independent proof audit in step313 below accepts (4)-(6) without
correction. The original construction's POTENTIALLY_NEW classification
has only the policy's bounded-search meaning; this audit is REPRODUCTION,
and originality beyond the inspected sources is not certified. No RH
candidate arises.

## Proof

### 1. Fixed smooth cutoff and its derivative

The usual flatness of eta at zero follows by differentiating on s>0:
each derivative is exp(-1/s) times a polynomial in 1/s, tending to
zero as s decreases to zero. The denominator defining theta is
positive for every real s, so theta is smooth, equals zero on s<=0,
equals one on s>=1, and takes values in [0,1]. Also
theta(1-s)=1-theta(s). For 0<s<1, differentiation gives

    theta'(s)=theta(s)(1-theta(s))
                              *(s^(-2)+(1-s)^(-2)).        (7)

We verify the convenient uniform bound |theta'|<=5. On [1/4,3/4],
the convex symmetric function s^(-2)+(1-s)^(-2) has its maximum
160/9 at an endpoint. Since theta(1-theta)<=1/4, (7) is at most
40/9<5 there. For 0<s<=1/4, put u=1/s>=4. Then

    theta(s)(1-theta(s))<=theta(s)
       <=exp(-1/s+1/(1-s))<=exp(4/3-u),
    s^(-2)+(1-s)^(-2)<=u^2+16/9.

The derivative of (u^2+16/9)exp(-u) is
exp(-u)(2u-u^2-16/9)<0 for u>=4. Therefore (7) is at most
(160/9)exp(-8/3)<40/9: indeed
exp(8/3)>1+8/3+(8/3)^2/2=65/9>4. Reflection gives the same
bound for 3/4<=s<1. Outside (0,1) the derivative is zero.

It follows that chi is smooth, vanishes for x<=delta and x>=L-delta,
equals one on [2delta,L-2delta], and satisfies chi(L-x)=chi(x).
Its derivative is supported in the two transition intervals
(delta,2delta) and (L-2delta,L-delta), where |chi'|<=5/delta.
These intervals do not overlap, and on each one the other theta
factor is identically one, since L=40delta. Thus no extra product
factor is missing in the derivative bound. Each phi_k has compact
support contained in [delta,L-delta], a compact subset of (0,L),
and its zero extension is smooth on R.

### 2. Uniform norm certificate in the two-mode subspace

Let c_1,c_3 be real, S=c_1^2+c_3^2>0, and set

    p(x)=c_1 sin(pi*x/L)+c_3 sin(3pi*x/L),   g=chi*p.

Elementary sine orthogonality on (0,L) gives

    integral_0^L p^2=L*S/2,
    integral_0^L (p')^2
       =pi^2(c_1^2+9c_3^2)/(2L)<=9pi^2*S/(2L).            (8)

For 0<=x<=2delta, Cauchy--Schwarz and |sin v|<=|v| give
|p(x)|^2<=10pi^2 x^2 S/L^2. The same bound with L-x in place
of x holds at the other edge because both frequencies are odd.
Since 1-chi^2 is between zero and one and supported in these two
edge strips, the lost mass is at most

    2*(10pi^2 S/L^2)*integral_0^(2delta) x^2 dx
       =160pi^2 delta^3 S/(3L^2)=pi^2 L*S/1200.

Consequently

    ||g||_2^2>=(1/2-pi^2/1200)L*S>(59/120)L*S.             (9)

For the cutoff derivative, using only its two transition strips,

    ||chi'*p||_2^2
       <=2*(25/delta^2)*(10pi^2 S/L^2)
                                *integral_delta^(2delta) x^2 dx
       =(3500/3)pi^2 delta S/L^2
       =(175/6)pi^2 S/L.                                 (10)

Since g'=chi*p'+chi'*p, the inequality |a+b|^2<=2|a|^2+2|b|^2,
0<=chi<=1, (8) and (10) give

    ||g'||_2^2<=[9+175/3]pi^2 S/L=(202/3)pi^2 S/L.

Use pi^2<10 and L>4 in (9). The latter follows from e<3.
The former follows, for example, from pi<22/7. Hence

    ||g'||_2^2/||g||_2^2
       <[(202/3)*10]/[(59/120)*16]=5050/59<100.            (11)

In particular g is nonzero for every nonzero coefficient pair.
These bounds are uniform in the exact coefficients; there is no
coefficient-rounding error or ill-conditioned numerical nullspace.

### 3. Both moments vanish exactly for a nonzero witness

The M_k in (4) are finite real integrals. The function phi_1 is
nonnegative and positive on the interior of the central strip, so
M_1>0. Thus (4) is well-defined, and its positive exponential moment
is exactly zero by linearity. Its coefficients have c_3=1, so (9)
proves N>0 without estimating M_3/M_1.

For odd k, sin(k*pi*(L-x)/L)=sin(k*pi*x/L). Together with the
cutoff symmetry this gives f(L-x)=f(x). Substitution u=L-x yields

    integral_0^L exp(-x/2)f(x)dx
       =exp(-L/2)integral_0^L exp(u/2)f(u)du=0.

This proves both global constraints exactly. The other four
coefficients in the fixed six-mode trial space are zero. The
translation h has support compactly contained in (-b,b) and preserves
N; its two corresponding exponential moments also vanish, by the
constant translation factors. Thus L748 applies with every stated
hypothesis. No parity restriction has been imposed on the universal
claim: a witness in its real symmetric subclass suffices to refute it.

### 4. All-frequency archimedean upper bound

For any real t put z=1/4+it/2 and w=z+1=5/4+it/2. The imported
recurrence is psi(z)=psi(w)-1/z. Both Re(1/z) and Re(1/w) are
positive. In (3), |arg w|<pi/2 and |w|>=5/4, so

    |rho(w)|<=2sqrt(2)/(12|w|^2)
       <=8sqrt(2)/75<4/25.

Taking real parts, dropping only the two nonpositive reciprocal
terms, and using Re log w=log|w| gives the global bound

    m(t)<(1/2)log(25/16+t^2/4)+4/25-log pi.                (12)

This is a scalar specialization of the cited recurrence/remainder,
not a large-t approximation at small t. The line Re w=5/4 stays
strictly in the right half-plane; in particular t=0 is included.

For the exact smooth f, F_f is Schwartz. The multiplier m is
continuous on the real line and grows at most logarithmically by
the same cited expansion, so (1) is absolutely convergent. The
probability measure

    dmu(t)=|F_f(t)|^2dt/(2pi*N)

has total mass one by Plancherel, and its second moment is
D/N, where D=||f'||_2^2. Its logarithmic integral in (12) is finite;
the argument is bounded below by 25/16 and bounded above by a
constant times 1+t^2. Jensen's inequality therefore applies and gives

    A(f)/N
       <=(1/2)log(25/16+D/(4N))+4/25-log pi
       <(1/2)log(425/16)+4/25-log pi
       <log6+4/25-log3
       =log2+4/25<7/10+4/25=43/50.                        (13)

Here we used (11), 425/16<36 and pi>3. The elementary
log2<7/10 follows from the positive exponential series:
sum_(j=0)^4 (7/10)^j/j!=482921/240000>2.
The source formula (1) has exactly the d t/(2pi) normalization
in the Plancherel probability measure. No frequency, logarithmic
singularity or omitted tail is evaluated by quadrature. The estimates
cover the full line. L744 (6)'s pole product is zero by (5), although
the assertion here concerns only its archimedean part.

### 5. Compare with the entire compensated resource

By the audited L748 bound, W_b(h)/2> N. The full resource is finite
by its smooth identity (5); no pairs or spatial terms have been
removed. Combining with (13) gives

    A(f)-W_b(h)/2<(43/50-1)N=-(7/50)N<0.

This is the required strict upper certificate. It needs no numerical
values for M_1 or M_3, since the exact integral definition and the
uniform coefficient estimates prove every needed property. It also
needs no premise from conditional L742. The result closes the one
approved screen without enlarging the family. Its only route-level
consequence is failure of this direct sufficient payment inequality;
the prime allocation itself and the independent main sign gap remain.

### Independent proof audit, 4 November 2026, step313

The exact COVERED_TARGET in the previously saved SPECIALIZE assessment
`drafts/literature/2026-11-04-direct-archimedean-payment-counterexample-audit.md`
is accepted. This is independent verification of the written local
certificate, not a new counterexample construction or source theorem.
The recurrence and quantified remainder (3) are imported in their
already inspected scope; L748 (2)/(5) and L744 (6) are reused.

**Cutoff, including both edges.** The positive denominator makes theta
smooth across both flat endpoints. Differentiating its logistic ratio
gives exactly (7), with a positive sign on both reciprocal squares.
On [1/4,3/4] the convex symmetric sum is at most 160/9, hence its
product with theta(1-theta) is at most 40/9. For s<=1/4, the bound
exp(4/3-u)(u^2+16/9), u=1/s>=4, decreases because
2u-u^2-16/9<0. Its endpoint is (160/9)exp(-8/3)<40/9,
using exp(8/3)>65/9>4. Reflection covers the other edge. Thus
|theta'|<=5 is valid globally. On either transition strip of chi,
the opposite factor is identically one; for example x<=2delta
gives (L-delta-x)/delta>=37. The derivative bound is 5/delta,
not twice that bound. Both transition strips must still be integrated.
Flatness gives smooth zero extensions supported in [delta,L-delta].

**Uniform norms and the exact witness.** For the two odd sine modes,
the coefficient Cauchy--Schwarz bound is
|p(x)|^2<=pi^2 x^2(1+9)S/L^2 at the left edge. Their reflection
has the same bound with L-x. The two lost strips therefore contribute
at most 160pi^2 delta^3 S/(3L^2)=pi^2 L S/1200. Independently,
the two derivative strips contribute

    2*(25/delta^2)*(10pi^2 S/L^2)*(7delta^3/3)
       =(3500/3)pi^2 delta S/L^2=(175/6)pi^2 S/L.

Sine and cosine orthogonality give (8). Applying the two-term square
bound to g' gives (9+175/3)pi^2 S/L=(202/3)pi^2 S/L.
Since pi^2<10 and L>4, the resulting ratio is strictly less than

    ((202/3)*10)*120/(59*16)=5050/59<100.

Also (1/2-pi^2/1200)>59/120, so every nonzero coefficient pair
has positive norm. In particular c_3=1 proves that (4) is nonzero
regardless of the exact value of M_3/M_1. The integral M_1 is
strictly positive because exp(x/2)phi_1(x) is positive on the
nonempty central strip. The positive moment cancels by its exact
integral definition. Both odd modes and chi are invariant under
x -> L-x, so substitution gives the negative moment as exp(-L/2)
times the positive moment. Translation to h multiplies the moments
by exp(-b/2) and exp(b/2), respectively, and preserves N. Hence
all of L748's smooth support and exact-neutral hypotheses hold.

**All frequencies and normalization.** At z=1/4+it/2,
w=z+1 has real part 5/4. Both arguments avoid poles, and the
principal-log remainder applies for every real t, including zero.
The two reciprocal terms have real parts

    Re(1/z)=(1/4)/((1/4)^2+t^2/4)>0,
    Re(1/w)=(5/4)/((5/4)^2+t^2/4)>0.

Thus their negative signs permit the stated upper bound. The sector
factor is at most 2sqrt2 and |w|^2>=25/16, giving
|rho(w)|<=8sqrt2/75<4/25 because sqrt2<3/2. This proves (12)
on the full line without a small-frequency exception. The same
expansion, together with the bounded reciprocal terms, gives an
absolute logarithmic-growth bound for m; smooth compact support
makes F_f Schwartz. Consequently A is absolutely convergent.
Plancherel with F_f(t)=integral exp(-itx)f(x)dx gives total mass
one for dmu and integral t^2 dmu=D/N, with precisely dt/(2pi).
The positive logarithm's argument is bounded below by 25/16 and
above by a constant times 1+t^2; its integral is finite. Jensen
therefore applies to that probability measure, yielding (13).
In its strict comparisons, D/N<100 gives 25/16+D/(4N)<425/16;
425/16<36 and pi>3 then give log2+4/25. Finally the exact partial
sum 482921/240000>2 proves log2<7/10. Thus A/N<43/50.
L744 (6) uses this same multiplier and normalization for arbitrary
smooth zero extensions. Its pole product is zero by both exact
moments; its arithmetic term is not part of the present comparison.

**Entire resource and scope.** L748 (5) proves finiteness for this
smooth h using the original whole-plane remainder, including every
exterior pair. L748 (2) then gives W_b/(2N)>=C_*/2>1. Combining
with the preceding strict upper bound yields defect<-7N/50. No
spatial term is removed, no Fourier tail is truncated, and no
approximate moment or rounded coefficient is used. No premise from
conditional L742 is needed. The direct mathematical inputs remain
L744 and L748, as recorded in the unchanged DAG row. All assertions
(4)-(6) pass without repair. This certifies only failure of A>=W_b/2;
it gives neither A<Q_2 nor negative complete Weil energy, and it
does not address other primes, complementary signs or support growth.

## Mathlib

Full matching Mathlib coverage of this finite smooth counterexample
was not checked; no absence claim or Lean verification is asserted.
Plancherel, Fourier differentiation, elementary finite-dimensional
algebra and Jensen are named supporting inputs. The scalar digamma
inputs and L748's resource bound are precisely cited above. This
informal certificate passed the independent audit above; no formal
verification is asserted.
