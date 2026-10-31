# L528 — Uniform periodic majorant for the fixed common-pole shape functional

## Hypotheses

Let h be real and even, in C_c^infinity(-1,1), with
integral |h(x)|^2 dx=1. Use

    H(t)=integral h(x) exp(-itx) dx,   dm(t)=dt/(2pi),
    K(t)=(e exp(2it)-1)/(1+2it),
    q(t)=Re(K(t)/|K(t)|),
    c(h)=integral |H(t)|^2 q(t) dm(t).

Here e=exp(1). In particular K never vanishes on the real line.
This is exactly the fixed-symbol functional motivating L527's shape
variation. No generalized trace asymptotic, Sonin projection estimate,
nullvector, full-Weil identification or actual-Xi assertion is assumed.
L526/L527 supply motivation and conventions, rather than a theorem used
in this proof. The pre-existing EXPLORE assessment is
`drafts/literature/2026-10-30-common-pole-test-shape-variational-test.md`.
It did not locate a matching threshold result; it does not certify novelty.

The standard imported result is the Fourier-series Parseval theorem:
the functions 2^(-1/2) exp(i pi k x), k in Z, form a complete
orthonormal basis of L2(-1,1), and the sum of squared coefficients
equals the squared L2 norm. We use this exact finite-interval form
below, not a finite-section convergence or spectral-isolation theorem.
Real-line Plancherel ensures that the defining integral for c(h) is
absolutely convergent, since |q|<=1. Precise imported sources are
MIT RES.18-015, *Topics in Fourier Analysis*, Spring 2024,
[Lecture 1](https://ocw.mit.edu/courses/res-18-015-topics-in-fourier-analysis-spring-2024/mitres_18_015_s24_lec01.pdf),
Theorem 1.2 and (1.2), p.2 (complex L2([0,1)), Lebesgue measure),
and Gerald Teschl, *Mathematical Methods in Quantum Mechanics*,
GSM 99, edition dated 12 February 2009,
[author-hosted text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Theorem 7.5, pp.163--164, with transform (7.3), p.161, and
Plancherel identity (7.9). Their applicability and normalizations
are checked in the audit below, without reproving these theorems.
The symbol-specific estimate is proved here because the checked
sources supply no such estimate; this does not establish originality.

## Conclusion

Put theta_0=arccos(e^(-1)) and

    mu=(theta_0+e+1-sqrt(e^2-1))/pi.

Uniformly over the stated class,

    c(h)<=mu<147/188<47/60<pi/4.

Consequently

    pi/4 - sup_h c(h) > 1/705.

This rules out a witness above pi/4 by varying only h in this class
with this K and support interval. It does not determine the actual
supremum, extend L527's trace formula, control collective signs, or
prove/disprove RH. The separate conceptual audit below validates this
local bound under the stated hypotheses, without changing its value.

## Proof

### 1. Pointwise periodic majorant

Write

    a(t)+i b(t)=(e exp(2it)-1)/sqrt(e^2+1-2e cos(2t)).

Thus a^2+b^2=1; a is even, b is odd, and both have period pi.
The denominator is at least e-1>0. Multiplication by the conjugate
of 1+2it shows exactly, including for negative t, that

    q(t)=(a(t)+2t b(t))/sqrt(1+4t^2).

Define the bounded nonnegative pi-periodic function

    m(t)=1       if a(t)>=0,
         |b(t)| if a(t)<0.

In the first case q<=1 by Cauchy--Schwarz for the two real vectors
(a,b) and (1,2t). In the second case a/sqrt(1+4t^2)<0 and
2t b/sqrt(1+4t^2)<=|b|. Hence q<=m on the ENTIRE real line.
At a=0, |b|=1, so the two definitions agree continuously. No
discarded frequency region or coupling estimate is implicit here.

### 2. Exact period averaging from the support interval

For each fixed real t apply Fourier-series Parseval on (-1,1) to
g_t(x)=h(x)exp(-itx). Its k-th coefficient is
H(t+k pi)/sqrt(2). Its squared norm is one. Therefore

    sum_(k in Z) |H(t+k pi)|^2=2.                       (1)

The modulation is unitary and requires no periodicity of h at the
endpoints. Since m>=0, splitting the real integral into intervals
[k pi,(k+1)pi) and applying Tonelli is legitimate. Periodicity and
(1) give

    integral_R m(t)|H(t)|^2 dt/(2pi)
       =(1/(2pi)) integral_0^pi m(t)
                         sum_k |H(t+k pi)|^2 dt
       =(1/pi) integral_0^pi m(t) dt.                  (2)

Thus c(h) is at most the mean of m, independently of the shape.
Equation (1), rather than a numerical truncation or an assumption
about high-frequency behavior, controls the whole infinite sum.
Parity is not needed for this bound, so in particular the required
real-even sector is covered. We do not infer an extremizer.

### 3. Exact mean and strict rational comparison

With theta=2t, m equals one where cos(theta)>=1/e and otherwise
equals e|sin(theta)|/sqrt(e^2+1-2e cos(theta)). Reflection about
theta=pi reduces its mean to

    (1/pi)[theta_0 + integral_(theta_0)^pi
                     e sin(theta)/sqrt(e^2+1-2e cos(theta)) dtheta].

The integrand is the derivative of
sqrt(e^2+1-2e cos(theta)). Its values at the two endpoints are
e+1 and sqrt(e^2-1), respectively. This proves that the mean is mu.

For completeness all strict numerical comparisons can be proved by
rational arithmetic and elementary Taylor remainders, as follows.
The exponential series gives 8/3<e<3: its terms through degree
three sum to 8/3, with positive remainder; for n>=2 the inequality
n!>=2^(n-1), strict for n>=3, bounds the remaining sum by one.

First establish pi/4>47/60 without a numerical pi approximation.
The arctangent addition formula gives
atan(1/2)+atan(1/3)=atan(1)=pi/4; both positive angles have sum
less than pi/2 because their tangent denominator is 1-1/6>0.
Integrating the finite alternating geometric expansion of
1/(1+x^2) gives the strict lower bounds

    atan(1/2)>1/2-1/24+1/160-1/896,
    atan(1/3)>1/3-1/81.

Their sum is 284663/362880, exceeding 47/60 by 407/362880>0.
In particular pi>47/15, so 5/4<pi/2.

The alternating cosine series at 5/4 has decreasing term magnitudes
and its truncation after the positive fourth-degree term is an upper
bound. Hence

    cos(5/4)<=1-25/32+625/6144
             =1969/6144<1/3<1/e.

Cosine is strictly decreasing on [0,pi], so theta_0<5/4.
Also e>8/3>13/5 implies

    e^2-1 > (e-1/5)^2,
    sqrt(e^2-1)>e-1/5,
    e+1-sqrt(e^2-1)<6/5.

The positive square root is legitimate since e>1 and e-1/5>0.
Combining these inequalities gives

    mu < (5/4+6/5)/pi =49/(20pi)
       < (49/20)/(47/15)=147/188.

Finally 47/60-147/188=1/705>0 and pi/4>47/60. Since every c(h)
is at most the SAME mu, taking its supremum preserves that upper
bound, and yields the asserted strict uniform gap. No existence of
a maximizing h, compactness, or smooth approximation is needed.

The exact rational checks are reproducible by

    python3 scripts/common-pole-variational/majorant_certificate.py

The full small certificate is
`scripts/common-pole-variational/majorant-certificate.json`.
It verifies the rational comparisons, not Parseval or the analytic
majorization; those are justified above. No floating-point sample
or finite eigenpair is load-bearing.

### 4. Separate conceptual audit, 30 October 2026

This is the first critical audit of the argument above, under the
pre-existing SPECIALIZE scope in
`drafts/literature/2026-10-30-l528-periodic-majorant-audit-coverage.md`.
It reproduces the existing bound; it supplies no stronger estimate or
new discovery. The full-line, normalization, mean and strictness checks
all pass. L526/L527 remain contextual only, so no local lemma input or
DAG edge is added.

**Phase and full-line cases.** For N=e exp(2it)-1, |N|>=e-1>0
and |1+2it|>0. Thus K/|K|=(N/|N|)(1-2it)/sqrt(1+4t^2),
which verifies the sign of 2tb in q. If a<0, its contribution is
strictly negative and |2t|/sqrt(1+4t^2)<=1; hence the claimed
upper bound by |b| holds also when t<0 or tb<0. If a>=0,
Cauchy--Schwarz gives q<=1 without a sign restriction on b.
At a=0, a^2+b^2=1 gives |b|=1, so m is continuous, bounded
between zero and one, and pi-periodic. No region was omitted.

**Imported normalizations and interchange.** For each fixed t, set
F_t(y)=sqrt(2)h(2y-1)exp(-it(2y-1)), 0<y<1. Then
||F_t||_2=1 and its MIT Fourier-series coefficient at k is

    integral_0^1 F_t(y)exp(-2pi i k y)dy
       =(-1)^k H(t+k pi)/sqrt(2).

The complex L2 Parseval theorem applies even though h is real and
F_t need not be; it imposes no endpoint matching. This proves (1)
for every real t, not just almost every t. Zero-extended h belongs
to L1(R) intersect L2(R). In Teschl's n=1 convention its transform
is H/sqrt(2pi), so integral |H|^2 dt/(2pi)=1 exactly. This proves
absolute integrability of q|H|^2 and also of m|H|^2.

The map (s,k) -> m(s)|H(s+k pi)|^2 on [0,pi) x Z is
nonnegative measurable (H and m are continuous), on the product of
Lebesgue and counting measures, both sigma-finite. The standard
named Tonelli theorem applies. The half-open translated periods
partition R, and periodicity identifies m(s+k pi) with m(s).
Substitution of (1) gives precisely the mean in (2), with factor
1/pi. There is no signed-series interchange, decay truncation or
compactness assumption.

**Mean and strict inequalities.** The change theta=2t first gives
1/(2pi) times an integral over a full 2pi period. Reflection then
gives 1/pi times the integral on [0,pi]. On that half-period the
branch a>=0 is exactly [0,theta_0], sin(theta)>=0, and the
antiderivative sqrt(e^2+1-2e cos(theta)) has endpoint values
sqrt(e^2-1) and e+1. This checks both the mean and its factor two.

The exponential series proves strict 8/3<e<3 as in Section 3.
For the arctangent lower polynomials, integrating the finite
geometric expansion leaves respectively the strictly positive
remainders integral_0^(1/2) x^8/(1+x^2)dx and
integral_0^(1/3) x^4/(1+x^2)dx. If alpha=atan(1/2),
beta=atan(1/3), their sum lies in (0,pi), has positive cosine
because 1-1/6>0, and has tangent one. Thus it is pi/4 with
the correct branch. This proves pi>47/15, hence 5/4<pi/2.
The cosine-series terms decrease from k=0 at x=5/4, since their
successive magnitude ratios are (25/16)/((2k+1)(2k+2))<1.
Its positive fourth-degree truncation is an upper bound. With
e<3 this implies cos(5/4)<1/e, and strict monotonicity on
[0,pi] gives theta_0<5/4. Finally

    (e^2-1)-(e-1/5)^2=(2/5)e-26/25>2/75>0,

using e>8/3. Both quantities being compared as square roots are
positive, which validates the strict radical bound. The numerator
of mu is positive, so division by pi>47/15 preserves the required
strict comparison. The independent exact check gives

    atan lower sum =284663/362880,
    atan margin over 47/60 =407/362880>0,
    cosine upper =1969/6144<1/3,
    mean upper =147/188<47/60,
    47/60-147/188=1/705>0.

The class is nonempty (normalize any nonzero real even smooth bump),
and Plancherel bounds every c(h) in [-1,1]. Its supremum therefore
exists as a finite real number. The SAME mu bounds every member,
so sup c(h)<=mu<147/188; no extremizer or individual strictness
argument is substituted for this uniform bound. Combining the two
strict rational comparisons proves pi/4-sup c(h)>1/705.

**Complete finite evidence.** Read the entire original generator and
all six certificate comparisons. Independently recomputed the Taylor
polynomials from their general finite sums and verified all six
scalar fields and all six comparisons by integer cross multiplication.
The original generator then reproduced its complete saved certificate
byte for byte. No failures occurred. Reproduction command:

    python3 scripts/common-pole-variational/audit_certificate.py

Full exact evidence, including original/replay hashes, comparisons,
strict margins and generator output, is in
`scripts/common-pole-variational/majorant-audit-certificate.json`.
The certificate checks arithmetic only; the preceding audit checks
the analytic premises. No sampled evidence is used. This confirms
the fixed-symbol, fixed-support shape obstruction. It does not audit
upstream trace manuscripts, extend any trace formula, or establish a
collective prime sign, the actual supremum, or any actual-Xi assertion.

## Mathlib

Full matching coverage is not checked. Fourier-series Parseval,
Plancherel, Cauchy--Schwarz and elementary exponential/trigonometric
facts are standard supporting results; no exact Mathlib theorem
name or formalization of this symbol bound is claimed. The checked
literature did not establish coverage of this particular uniform
threshold. The local bound has passed the separate conceptual audit
above. Full Mathlib availability remains unchecked, not asserted
absent; this is neither a certified originality claim nor an RH resolution.
