# C750m: The prescribed sine64 two-sided norm budget cannot pass

## Hypotheses

Work in H=L2((-b,b);C), with zero extension, unweighted measure and
inner product linear in its first argument. Fix, without optimization,

    L=log(101), b=L/2, c_n=2 Lambda(n)/sqrt(n),
    A=sum_(2<=n<101) c_n, T=2*pi*exp(A+2), beta=2-1/T,
    m(t)=Re psi(1/4+it/2)-log(pi),
    p(t)=sum_(2<=n<101) c_n*cos(t*log(n)), Psi(t)=m(t)-p(t).

All35 prime-power terms below101 are included. The25 primes are
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97;
the further powers are4,8,16,32,64,9,27,81,25,49. The delay log101=L
has zero overlap. Define

    F_f(t)=integral f(x)*exp(-itx) dx,
    M_+(f)=integral f(x)*exp(x/2) dx,
    M_-(f)=integral f(x)*exp(-x/2) dx,
    C_f(u)=integral f(x+u)*conj(f(x)) dx,
    J(f)=integral log(2+|t|)*|F_f(t)|^2 dt/(2*pi),
    V={f in H: J(f)<infinity}.

The complete form is L744(6), after translation to this interval:

    E(f)=integral m(t)*|F_f(t)|^2 dt/(2*pi)
         +2Re(M_+(f)*conj(M_-(f)))
         -sum_(2<=n<101) c_n*Re C_f(log(n)), f in V.       (1)

Its bounded frequency-split lower form and perturbation are

    R(f)=beta*||f||^2+integral_(-T)^T (Psi(t)-beta)
                         *|F_f(t)|^2 dt/(2*pi)
                       +2Re(M_+(f)*conj(M_-(f))),
    K=R-beta*I,                                            (2)

where an operator and its quadratic form are identified only in (2).
Let P be the orthogonal projection onto precisely phi_1,...,phi_64,

    phi_j(x)=b^(-1/2)*sin(j*pi*(x+b)/(2*b)), |x|<b,
    Q=I-P.

The prescribed certificate seeks nonnegative delta,epsilon with

    ||QKQ||<=delta, ||PKQ||<=epsilon,
    beta-delta-epsilon>0.                                 (3)

The approved assessment is
[1160](../drafts/literature/2026-11-16-full-weil-sine64-lower-form-feasibility-1160.md),
separately approved1161. This is its fixed feasibility test, with no
head assembly, change of64, support change or retuned cutoff.

Known reduction: Xuefeng Zhu, *Weil positivity in compact windows:
a finite reduction, certified two-sided bounds, and a Landau-Widom
decay law*, [arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
Theorem1.1/(4), Lemma3.1, Section4/(13), Lemma6.1 and its following
odd-sector paragraph, and Section11.1/(16). Only the analytic
reduction, parity statement, block criterion and sine transform are
used; none of its numerical certificates or RH-dependent statements
is used. L744(8) supplies the global digamma bounds. C750f is the
normalization/domain comparison, not a positive-floor premise.

## Conclusion

There is a real even unit vector phi_j in the UNCHANGED QH such that

    <K phi_j,phi_j> > 200269/50000 > 4.
    Consequently ||QKQ||>4, whereas 0<beta<2.              (4)

Every valid pair in (3) therefore satisfies

    beta-delta-epsilon < -2.                              (5)

This rules out even exact norms in the prescribed sufficient
certificate. It is stronger than failure of one coarse upper estimate.
All complete Hilbert-Schmidt upper estimates for those norms fail as
well. The large index used below is a complementary witness, never
an enlarged retained head or a replacement projection.

Outcome1162 is NEGATIVE, RESEARCH/REPRODUCTION: a source-supported
specialization gives a new local route obstruction, with no claim
of novelty beyond the searched literature. Separate conceptual audit1164
below accepts (4)-(5), without a mathematical repair or stronger spectral
conclusion. It proves neither a negative E direction nor a
negative R direction. A one-sided lower bound on QRQ could still
succeed. No original-form spectral floor, all-support positivity,
actual-Xi realization or RH conclusion follows.

## Proof

### 1. Complete complex normalization and logarithmic domain

Plancherel and translation give, for every f in H,

    Re C_f(u)=integral cos(t*u)*|F_f(t)|^2 dt/(2*pi).

Both sides exist: a shift is an L2 contraction and |F_f|^2 is
integrable. Thus the finite arithmetic sum in (1) equals the full
multiplier p. Translation from (0,L) preserves the gamma and shift
terms; its two moment factors acquire reciprocal positive real
factors, preserving their product. This is the same normalization
as C750f, without importing that lemma's radius-specific sign.
For |u|>=L, support intersections have measure zero; this includes
u=L. Hence the exact active prime-power list in the hypotheses is
valid on all H, with arbitrary complex coefficients.

Here is the domain justification at the full endpoints; C750f's
strictly interior mollifier argument alone would not suffice. Put
w(t)=log(2+|t|) and a0=2+8sqrt(2)/3+log(4*pi). L744(8) gives

    |m(t)|<=a0+w(t),
    |m(t)-log(|t|/(2*pi))|<=2/t^2 for |t|>=1.

It follows, exactly by splitting |t|<=1 and |t|>=1, that

    |m(t)-w(t)|<=B,
    B=max{a0+2log(3), 2+log(6*pi)}.

The two exponential functionals each have squared norm2sinh(b).
The absolute pole product is at most4sinh(b)||f||^2 and the absolute
prime form at most A||f||^2. Thus, with D=B+4sinh(b)+A,

    |E(f)-J(f)|<=D||f||^2,
    J(f)+||f||^2 <= E(f)+(D+1)||f||^2
                      <= J(f)+(2D+1)||f||^2.              (6)

These hold without a sign assumption. The supported weighted Fourier
space V is complete in the J norm: a J-Cauchy sequence has a weighted
Fourier limit and, since w>=log2, an L2 limit with the same support.

To prove that smooth compact tests in (-b,b) are a core, first set
f_r(x)=r^(-1/2)f(x/r), 1/2<=r<1. Its support is in [-rb,rb], and
F_(f_r)(t)=sqrt(r)*F_f(rt). The corresponding dilation on L2(w dt)
has squared norm at most2, because

    w(u/r)<=w(u)+log(2)<=2w(u).

It converges strongly to the identity as r increases to1: this is
dominated convergence on continuous compactly supported Fourier
functions, followed by their density in L2(w dt) and the uniform
bound just proved. Hence J(f_r-f)->0. For each fixed r convolve f_r
with a real nonnegative smooth unit-integral mollifier of radius
eta<(1-r)b. The result is compactly supported in (-b,b), and its
Fourier multiplier tends pointwise to1 with modulus at most1.
Dominated convergence in J gives smooth approximation to f_r.
A diagonal choice gives smooth approximation to f in J. By (6)
this is also approximation in the shifted form norm. Thus V and
(1) are precisely the closure of the complete smooth form; no
H1 condition on all of V or boundary trace is assumed.

Zhu's Theorem1.1/(4) and Lemma6.1 give (2)'s comparison on the
smooth core, retaining the negative odd pole and both complex
components. Equivalently, its Lemma3.1 bounds Psi(t) below by beta
for |t|>=T, once T>=15/4 is checked below. Equation(6) and boundedness
of R, proved next, pass the cited inequality E>=R to every f in V.
This checks its changed-domain applicability rather than reproving
the general reduction or assuming positivity of the closure.

### 2. The actual bounded kernel and complete tail norms

Set h(t)=Psi(t)-beta on [-T,T]. It is continuous and bounded there.
With c(x)=cosh(x/2), s(x)=sinh(x/2), the kernel of K is

    k(x,y)=2c(x)c(y)-2s(x)s(y)
           +(1/(2*pi))*integral_(-T)^T h(t)*exp(it*(x-y)) dt.
                                                               (7)

Indeed its pole form is 2|<f,c>|^2-2|<f,s>|^2, which equals
2Re(M_+(f)*conj(M_-(f))) for complex f. No moment is set to zero.
The Fourier kernel follows by substituting F and its conjugate;
finite support and finite T justify Fubini. h is real and even,
so (7) is real symmetric and K is bounded self-adjoint.

For example, if H0=max_[-T,T]|h|, then

    |k(x,y)|<=2cosh(b)+(T/pi)*H0,
    ||K||_HS <= L*(2cosh(b)+(T/pi)*H0) < infinity.          (8)

The kernel bound retains the complete pole and comb. It also proves
boundedness of R on H, independently of the unbounded original
logarithmic operator. The standard squared-kernel and complete-basis
identities used here are Gerald Teschl, *Mathematical Methods in
Quantum Mechanics*, GSM99, [author version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Section6.3 printed pp139-141, (6.8)-(6.18),(6.21), Lemmas6.9/6.10.
In the complete normalized sine basis they give

    ||QKQ||_HS^2=sum_(j,k>=65) |<K phi_k,phi_j>|^2,
    ||PKQ||_HS^2=sum_(j<=64,k>=65) |<K phi_k,phi_j>|^2.     (9)

Both compressions act on H, so there is no change-of-space issue.
Their operator norms are bounded by these complete Hilbert-Schmidt
norms. No absolute row summability or Legendre decay is asserted.
Rather than expend work sharpening (8)-(9), we will prove a necessary
lower bound exceeding the entire allowed resource.

### 3. Elementary parameter bounds with every prime retained

The Taylor series for exp gives 8/3<e<11/4<3. For the upper bound,
the terms through degree3 sum to8/3 and the remaining terms are at
most (1/24)/(1-1/5)=5/96, giving e<=87/32<11/4. Consequently

    4<L<5, 2<b<5/2, log(23)>3.

Here e^4<81<101, e^5>(8/3)^5>101 and e^3<(11/4)^3<23.
Take the following17 primes, a subset of the full sum:

    S={23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}.

Their primality is checked by trial divisors2,3,5,7, which exhaust
primes below sqrt(97). Each has log(p)>3 and sqrt(p)<10. Therefore

    A>17*(6/10)=51/5,
    d:=sum_(2<=n<101) c_n*log(n)/L
       >17*(18/50)=153/25.                               (10)

The subset provides lower bounds only; it never replaces A in the
frequency envelope or drops terms from the signed form. For the upper
bound, Lambda(n)<=log(n)<5 and monotonicity give

    A<10*sum_(n=2)^100 n^(-1/2)
      <10*integral_1^100 x^(-1/2) dx=180<200.              (11)

Since pi>3 and e>5/2, T>6*(5/2)^12>100000. In particular T>=15/4
and 0<beta=2-1/T<2, as required by the source envelope. Finally
log2<7/10, since the first five positive terms of exp(7/10) already
sum to482921/240000>2. Hence

    log8<21/10.                                         (12)

### 4. A witness in the unchanged sine complement

Choose the smallest positive odd integer j with

    alpha=j*pi/L>=T/4.

Odd-index frequencies are spaced by2*pi/L<2, using pi<4 and L>4.
Thus T/4<=alpha<T/4+2<T/2. Also j>=L*T/(4*pi)>25000>64.
The vector phi=phi_j has norm1, is real even, belongs to QH, and
has nonnegative pole product. It is in V: it vanishes at both
endpoints and its zero extension is H1, or directly its transform
below has quadratic decay at infinity. These properties concern
this one witness, not all of V.

Zhu Section1.6 uses the positive Fourier sign. Conjugating its
(16) and normalizing by sqrt(b) gives in our negative convention

    F_(phi_k)(t)=alpha_k*(exp(itb)-(-1)^k*exp(-itb))
                    /(sqrt(b)*(alpha_k^2-t^2)).           (13)

The apparent poles at t=+-alpha_k are removable by continuity of
the Fourier integral; (13) is used for estimates only away from
them. In particular for our odd j,

    |F_phi(t)|<=2alpha/(sqrt(b)*|alpha^2-t^2|).

Let dmu=|F_phi(t)|^2 dt/(2*pi), a probability measure. On
|t|<alpha/2 the squared bound is64/(9b alpha^2), whence

    ell0:=mu(|t|<alpha/2)<=32/(9*pi*b*alpha)<1/alpha.       (14)

On |t|>T, alpha<T/2 makes |t^2-alpha^2|>=3t^2/4. Thus

    ellT:=mu(|t|>T)
        <=64alpha^2/(27*pi*b*T^3)
        <=16/(27*pi*b*T)<1/T.                            (15)

These integrate the entire frequency tails, without pretending a
sine mode has compact Fourier support.

### 5. Complete arithmetic expectation and gamma lower bound

For every 0<=u<L, a direct product-to-sum integration on [0,L-u]
gives the exact correlation

    C_phi(u)=(1-u/L)*cos(alpha*u)+sin(alpha*u)/(L*alpha).
                                                               (16)

To check the boundary contribution, write phi in coordinates y=x+b
as sqrt(2/L)sin(alpha*y). The oscillating integral contains
sin(2alpha*L-alpha*u)=sin(2j*pi-alpha*u)=-sin(alpha*u),
yielding the plus sign in (16). This short computation is needed
for the effective finite-window loss, which the imported transform
alone does not state. In particular, simultaneously for all active
prime powers,

    integral_R p(t) dmu(t)
       =sum c_n*C_phi(log(n))
       <= A-d+A/(L*alpha).                               (17)

We used cos<=1, sin<=1 and 1-log(n)/L>0. This is an explicitly
identified absolute estimate on the actual supported correlations,
not the erroneous per-prime replacement of the envelope mass.
Since |p(t)|<=A, the omitted Fourier tail is fully paid:

    integral_(-T)^T p(t) dmu(t)
       <= A-d+A/(L*alpha)+A/T.                           (18)

For the gamma term we first note m(t)>=-11 on all real t.
On |t|<=1, L744(8) gives |m(t)|<=a0+log3<11: use sqrt2<3/2,
log(4*pi)<3 and log3<2. On |t|>=1 its other bound gives
m(t)>=-log(2*pi)-2>-5. Thus the stated global floor follows.

For alpha/2<=|t|<=T, Zhu Lemma3.1 and its increasing envelope give

    m(t)>=log(alpha/(4*pi))-2/alpha
         >=v:=A+2-log8-2/alpha.

By (10)-(15), 0<v<A+2. Splitting the entire band [-T,T] into
these high and low regions, with its missing mass ellT, proves

    integral_(-T)^T m(t) dmu(t)
       >=v*(1-ell0-ellT)-11ell0
       >=A+2-log8-(A+15)/alpha-(A+2)/T.                  (19)

All losses in (19) are explicit: 2/alpha from the envelope,
(A+13)/alpha from the low mass, and (A+2)/T from the missing mass.

### 6. Decisive norm inequality and scope of the stop

The even witness has nonnegative pole form. Also beta>0 and
mu([-T,T])<=1, so its negative beta contribution in K is at least
-beta>-2. Subtracting (18) from (19) therefore gives

    <K phi,phi>
       > d-log8-(A+15)/alpha-A/(L*alpha)-(2A+2)/T.

Using A<200, L>4 and alpha>=T/4, the total subtracted error is
strictly less than

    (215+50)*4/T+402/T=1462/T<731/50000.

Equations(10),(12) yield

    <K phi,phi> >153/25-21/10-731/50000
                =200269/50000>4.                        (20)

Since Qphi=phi and ||phi||=1, the defining operator-norm inequality
gives ||QKQ||>=|<QKQ phi,phi>|>4. This proves (4)-(5).
The exact complete norm, not merely an approximate tail sum,
already exceeds the required delta<beta-epsilon<=beta<2.
Computing epsilon or the finite head cannot rescue (3).

The obstruction is a LARGE POSITIVE complementary deviation from
beta*I. Therefore it cannot be used as an upper bound on the bottom
of QRQ or E, and it says nothing adverse about their positivity.
It retires only the specified two-sided-norm route at the fixed
parameters. The full kernel, both poles, all prime powers and all
Fourier remainders have been retained. No numerical quadrature,
external positive floor, zero data or Xi premise enters the proof.

The exact arithmetic was checked by
`python3 scripts/sine64/check_arithmetic_1162.py`, with all9 checks
passing; full output is [arithmetic-1162.json](../scripts/sine64/arithmetic-1162.json).
This checks the prime-power list, rational Taylor bounds and final
constants only. It does not verify the analytic inequalities, domain
argument or interpretation of the norm obstruction.

### 7. Independent conceptual audit1164 — 16 November 2026

This audits the whole statement (4)-(5) under the separately approved
assessment1162/1163, at the unchanged b, T and P64. It accepts the stop.
The original proof and arithmetic1162 remain intact; no bound is inferred
merely from their presence. The following checks supply the analytic
audit, separately from the exact arithmetic replay described last.

**Domain and full complex form.** The two cases in L744(8) imply the
displayed bound on m-w: on |t|<=1 the loss is at most a0+2log3;
outside, w-log(|t|/(2pi))<=log(6pi) and the remaining loss is at most2.
Each exponential moment has squared norm2sinh(b); Cauchy--Schwarz gives
the claimed4sinh(b) pole bound, with no restriction to real tests.
The finite shift sum has norm at most A. Thus (6) follows and makes
the shifted form norm equivalent to the complete weighted Fourier norm.
Its completeness follows because the weighted limit also converges
in L2 and the subspace of functions supported in [-b,b] is closed.

For the dilation used in Section1, changing variables gives exactly
integral w(u/r)|F_f(u)|^2 du/(2pi). This squared weighted norm is at
most twice J(f). For continuous compact Fourier data the dilates converge
in weighted L2 by dominated convergence on a common compact interval.
Density and this uniform operator bound extend strong convergence to
all weighted data. Dilation acts on the whole weighted space for this
argument; its physical application preserves support inside [-rb,rb].
Subsequent mollification has support strictly inside (-b,b) and Fourier
multiplier bounded by1. Dominated convergence applied to its difference
from1 proves convergence in J. Convolution of a supported L2 function
with a smooth compact mollifier is smooth. These facts prove the stated
core and the closure identification, not just a pointwise formula.
No H1 regularity or endpoint trace of an arbitrary f in V is used.

The source's radius is our b, its positive Fourier convention conjugates
to ours, and its full comb is our A. L744's modulation hypotheses K,M,chi
and its modulation conclusion are not imported: the smooth symbol
calculation in (6) and scalar bounds (8) are independent of the finite
window length, and Zhu's arbitrary-radius formula supplies the same
complete form at this b. Directly rechecked
[Zhu v2](https://arxiv.org/html/2608.24827v2), Theorem1.1/(4),
Lemma3.1 with proof, Section4's frequency split, Lemma6.1 with proof
and its following paragraph, and Section11.1/(16). The envelope requires
|t|>=15/4; Section3's T bound meets it. The negative odd pole and complex
decomposition are retained. Hence E>=R on the core, and (6) and bounded
R pass it to V. No source spectral floor or Legendre tail is used.

**Kernel and compressions.** With inner product linear first, the
integral operator with kernel (7) gives the Fourier quadratic integral
when paired against f: its factors are f(y)conj(f(x)) and exp(it(x-y)).
Writing the two moments as <f,c> plus/minus <f,s> gives exactly
2|<f,c>|^2-2|<f,s>|^2. The pole kernel is2cosh((x-y)/2), bounded by
2cosh(b); the frequency term is bounded by TH0/pi. Thus (8) bounds
the actual complete kernel. The cited Teschl Hilbert-Schmidt identities
apply on the same complex H and give (9), with no unbounded original
operator identified as a Hilbert-Schmidt kernel. Support intersections
at delay L have measure zero; this justifies all35 terms and the101
endpoint independently of boundary values. C750f is comparison only;
the mathematical local input remains L744, as recorded in the DAG.

**Witness, leakage and arithmetic.** An odd index exists with
T/4<=alpha<T/4+2<T/2, since consecutive odd frequencies are2pi/L<2.
The inequality j>=LT/(4pi)>25000 puts it in the unchanged QH.
Reflection makes it even and its squared norm is b^(-1)L/2=1.
Its endpoint-zero extension has an L2 weak derivative, proving V
membership for this witness alone. The source transform, conjugated
and divided by sqrt(b), is (13), including the even-index sign;
removable poles are never used as denominators in the estimates.

For low leakage the interval length is alpha and the squared transform
bound is64/(9b alpha^2); division by2pi yields32/(9pi b alpha).
For the two high tails, the squared bound is64alpha^2/(9b t^4);
their complete integral is64alpha^2/(27pi b T^3). Using alpha<T/2
and pi*b>6 gives precisely (14)-(15). Nothing between these regions
is discarded with an assumed sign.

Recomputing the product-to-sum integral in (16), its oscillating term is
minus[sin(2alpha(L-u)+alpha*u)-sin(alpha*u)]/(2Lalpha), which equals
plus sin(alpha*u)/(Lalpha), since alpha L=j*pi. This verifies the
boundary term for every0<=u<L. Each active coefficient is nonnegative
and 1-log(n)/L>0. Thus (17) includes every prime power. Subtracting the
entire omitted integral of p costs at most A*ellT, giving (18) with
the stated direction, even when that tail integral is negative.

The global floor m>=-11 follows from L744(8): a0+log3<11 on the
unit interval, and -log(2pi)-2>-5 outside it. The elementary estimates
used here follow from pi<4, sqrt2<3/2 and e>8/3; in particular e^3>16
and e^2>3. On the high part of the band, the source envelope is increasing
and alpha/2>=T/8>12500. It yields m>=v as in Section5, with0<v<A+2.
The band integral is at least v-(v+11)ell0-v*ellT. Replacing the two
loss coefficients by A+13 and A+2 gives exactly (19), including the
2/alpha term already inside v. This accounts for all band and tail mass.

Finally the pole is nonnegative for this real even witness, while
-beta*mu([-T,T])>=-beta>-2. Subtracting (18) from (19) gives the
stated lower bound, with total error less than1462/T<731/50000.
The17-prime subset proves d>153/25, without replacing the full A in
any envelope, and log8<21/10. Therefore (20) and both conclusions
follow strictly. A positive complementary expectation is a lower
bound on the symmetric operator norm; it gives no upper bound on the
bottom of R or E and cannot refute their positivity.

Independent finite-integer and rational replay:
`python3 scripts/sine64/audit_arithmetic_1164.py` writes
[audit-arithmetic-1164.json](../scripts/sine64/audit-arithmetic-1164.json).
All21 checks pass, including the complete prime-power list, Taylor and
leakage coefficients, total error and strict threshold. The full checks,
values and failure list were inspected. The achieved expectation bound
is200269/50000; the required symmetric norm bound is strictly below2.
The canonical argument above supplies the analytic verification; the
arithmetic certificate alone does not. Outcome1164 records independent
acceptance of a pending local obstruction, not a new or stronger theorem
beyond the source-supported specialization. No essential mathematical
input or DAG edge has changed.

## Mathlib

Full matching coverage for this complete Weil form, closed supported
logarithmic domain and fixed sine64 obstruction has not been checked.
Unknown coverage is not absence. Supporting facts are Plancherel,
weighted L2 density/dominated convergence, the elementary sine basis,
Hilbert-Schmidt kernel identities and the operator-norm inequality;
no exact Mathlib theorem names or Lean verification are claimed.
