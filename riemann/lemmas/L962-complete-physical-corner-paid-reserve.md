# Lemma 962: complete physical lower-corner paid reserve

## Hypotheses

For the finite assertion use L960's exact definitions with

    t=98/625, x=6000000185827,
    s=(1+ix)/2, N=floor(sqrt(x/(4pi)+t/16)),
    alpha(s)=1/(2s)+1/(s-1)+(1/2)Log(s/(2pi)),
    w=s+t*alpha(s)/2=sigma+i*tau,
    ell=2Re(alpha(s)+t*alpha(s)*alpha'(s)/2),
    a_n=exp(t*(log n)^2/4-sigma*log n),
    A=sum_(n=1)^N a_n exp(-i*tau*log n),
    L=sum_(n=1)^N a_n log n exp(-i*tau*log n),
    S=ell*A-2L, R=|A|, F=Re(conj(A)*S),
    p=101/200000000,
    q=142/10000000+1/250000000000,
    E=p*(25R+81/2)+q*R+p*q.

Take the principal logarithm near s, with the conjugate branch near
conj(s); these neighbourhoods are disjoint from its cut. All natural
support terms, including n=1, are retained. No stability, torus floor,
remainder estimate or assertion about H_t is assumed for this finite sum.

For the conditional transfer only, retain L960's local analytic,
real-type, conjugate-coordinate and real-gauge hypotheses, G(x)>0,
|P(x)|=1, the frozen-N derivative convention, and

    |r(x)|<101/10^8, |r'(x)|<71/10^7,
    |B-S|<1/250000000000,
    M32=sum_(n<=N) a_n |log(n/32)|<81/4,
    ell-log N>13, 0<ell-2log32<25.

The moment bound is available from L960's independent rational audit;
the remaining analytic/remainder/companion hypotheses are retained,
not verified here. This conditional assertion has neither of L960's
full-polydisc stability and torus-modulus premises.

## Conclusion

N=690988, and the complete finite physical sum satisfies the strict
rational bounds

    150.30628 < F < 150.30629,
    2.49096 < R < 2.49097,
    0.00008727 < E < 0.00008728,
    F-E > 150.30619 > 0.

Under the additional transfer hypotheses,

    Re(conj(A_true)*B_true)>150.30619,
    A_true=A+r/(2P), B_true=B-2i*r'/P,

and (H_t(x),H_t'(x)) is not (0,0) at this single centre. This is a
finite interval certificate with an informal implementation proof;
step150 independently replayed all elementary values and scalar bounds.
It proves
no rectangle-wide sign, unconditional H_t assertion, global or zero-time
continuation, Xi mixed positivity, or RH candidate.

## Proof

### Inputs and reason for the specialization

Reuse the source assessment
`drafts/literature/2026-11-10-physical-corner-reserve-147.md`, saved as
SPECIALIZE before this calculation. Its exact target is this one-point
test, not an extension. L960's carrier derivative and product expansion
come from Michel Planat and Dale James Raymond,
*Certified Collision Exclusion and an Unconditional Upper Bound
Lambda<0.156821 for the de Bruijn–Newman Constant*,
[arXiv:2611.06245v1, Corollary3.2, Sections3.7–3.8, Lemma3.4](https://arxiv.org/html/2611.06245v1#S3).
We do not import the global theorem or its asserted stability band.
The finite physical sign is absent from the passages checked, and
the source's all-character proof retains the two model premises.
An actual complete signed calculation, rather than a citation of that
proof, is therefore required. This is REPRODUCTION/specialization of
known validated finite evaluation and the existing scalar payment,
not a claim of a new general positivity mechanism.

Arithmetic references are Daumas–Lester–Muñoz,
*Verified Real Number Calculations: A Library for Interval Arithmetic*,
[arXiv:0708.3721v1, SectionIII, Propositions9/10/12](https://arxiv.org/html/0708.3721),
and [NIST DLMF3.1(ii–iii)](https://dlmf.nist.gov/3.1#ii).
For finite series use [DLMF4.6.4](https://dlmf.nist.gov/4.6.E4),
[4.2.19](https://dlmf.nist.gov/4.2.E19),
[4.24.3](https://dlmf.nist.gov/4.24.E3), and
[4.19.1–2](https://dlmf.nist.gov/4.19); periodic reduction uses
[4.45.6–7](https://dlmf.nist.gov/4.45#i).
Johansson, *Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval
Arithmetic*, IEEE Trans.Comput.66(8)(2017),1281–1292,
[Sections5–5.3](https://fredrikj.net/math/arbpaper.pdf), explains the
inclusion and branch requirements; Arb itself is not used. These
citations license methods, not this Python implementation. The inclusion
and finite-remainder specializations needed here are checked below.

### Exact carrier and support

Write alpha=u+iv, alpha'=d+ie. Since x>0, arg(s)=atan(x) lies in
(0,pi/2). Direct algebra gives

    u=(1/2)log(sqrt(1+x^2)/(4pi))-1/(1+x^2),
    v=(1/2)atan(x)-3x/(1+x^2),
    alpha'=-1/(2s^2)-1/(s-1)^2+1/(2s),
    sigma=1/2+t*u/2, tau=x/2+t*v/2,
    ell=2u+t*Re(alpha*alpha').

In particular tau is not replaced by x/2. L960's identity
(log M_t)'=alpha+t*alpha*alpha'/2 gives this exact ell=4Theta'.
The code computes the two complex reciprocals by real division with
denominator 1+x^2, then computes alpha' and alpha*alpha' by included
complex multiplication. Conjugation fixes the opposite carrier.

Let Q=2^256. Every stored (lo,hi) represents [lo/Q,hi/Q]. Both strict
floor gates enclose the respective margins

    x/(4pi)+t/16-690988^2>0,
    690989^2-x/(4pi)-t/16>0.

Their recorded lower integer endpoints are positive. This independently
proves N=690988; L961's matching floor is only a comparison, not a
numerical input. The same calculation verifies ell-log N>13,
0<ell-2log32<25 and sigma-t*log N/4>0 at this point. The last inequality
implies t*(log n)^2/4-sigma*log n<0 for 2<=n<=N.

A smallest-prime-factor sieve marks every composite n: its least prime
factor p satisfies p<=sqrt(n), so the p^2,p^2+p,... loop reaches n.
Each stored mark divides n; unmarked n>=2 is prime. For a composite,
m=n/p satisfies p*m=n and 2<=p<=m<=N/2. Induction in n therefore
allows the included identities

    log n=log p+log m,
    chi(n)=chi(p)*chi(m), chi(n)=exp(-i*tau*log n).

All necessary cached values have already been computed; values above
N/2 cannot occur as these proper factors. At each prime the log and
phase are evaluated directly. The n=1 values log1=0,chi(1)=1,a_1=1
are exact. This visits every integer, not merely smooth numbers,
and does not hold the physical character constant in a derivative.

### Included arithmetic and elementary functions

The implementation is `scripts/physical-corner/certify_148.py`.
It reuses the IV operations, logarithm, square root and Machin pi from
`scripts/centred-moment/rational_replay_140.py`, whose inclusion proof is
in L960. These functions' relevant code was read for this step.
Rational endpoints are rounded by exact integer floor/ceiling.
Multiplication takes all four endpoint products before outward division
by Q. Reciprocals reverse the endpoints and require exclusion of zero;
square roots use integer square roots followed by an exact square test.
Python integers have no fixed-word overflow. These operations give
inclusion for signed inputs as well as positive ones. No floating value
is accepted as mathematical input.

The reused log evaluator scales a rational positive argument to
m in [1,2], z=(m-1)/(m+1) in [0,1/3], and encloses

    log m=2 sum_(j=0)^99 z^(2j+1)/(2j+1)+R_log,
    0<=R_log<=2z^201/(201(1-z^2)).

The omitted positive denominators are >=201 and the squared-power
ratio is <=z^2. Independently enclosed log2 restores the scale;
monotonicity encloses interval inputs. Machin's named identity
pi=16atan(1/5)-4atan(1/239) uses 120 and40 alternating terms.
The first omitted term bounds each remainder because absolute terms
decrease to zero. For atan(x) use pi/2-atan(1/x): eight alternating
terms at 1/x have positive remainder at most x^(-17)/17.

The new exp evaluator takes a nonpositive interval v, with the n=1
zero argument handled exactly. Divide -v by an exact power of two to
obtain an interval z in [0,1/8], explicitly checked. The polynomial
sum_(j=0)^39 z^j/j! is evaluated by included Horner arithmetic with
outward-enclosed rational coefficients. For any real z in that interval,

    0<=exp(z)-sum_(j=0)^39 z^j/j!
      <= (1/8)^40/(40!*(1-1/(8*41))).

Indeed the first omitted term is <=(1/8)^40/40!, and subsequent ratios
are <=1/(8*41). Adding this positive upper remainder, squaring the
appropriate number of times and reciprocating encloses exp(v).
The polynomial's positive lower endpoint is checked before reciprocation.
For every term the exponent enclosure is checked nonpositive and the
resulting amplitude lower endpoint strictly positive.

At a prime, enclose theta=-tau*log p. Choose the integer k nearest the
ratio of interval midpoints, using integer arithmetic, and set
z=theta-2k*pi by included operations. The code explicitly checks the
entire z interval is inside (-4,4). There is no assertion that a
midpoint quotient alone determines a valid reduction. Any integer k
preserves sine and cosine by periodicity, including uncertain quotient
boundary cases; the checked full-interval size licenses the following
uniform remainder bounds without choosing a branch of an inverse trig
function. The theta and pi uncertainties remain in z.

Evaluate cos z through degree94 and sin z through degree95, each with
48 nonzero terms and rational coefficients, by included Horner arithmetic
in z^2 (then multiply by z for sine). Taylor's theorem with bounded
real sine/cosine derivatives gives

    |cos z-P_94(z)|<=4^96/96!,
    |sin z-P_95(z)|<=4^97/97!.

For cosine the degree95 Taylor coefficient is zero; for sine the
degree96 coefficient is zero. Thus the stated orders follow directly
from Taylor's theorem of orders95 and96 respectively. Both real
derivative bounds are1. Add the outward-rounded remainders on both
sides. This encloses exp(-i*tau*log p)=(cos theta,sin theta), with its
sign retained. Composite phases are then enclosed by the exact
multiplicative identity above; their dependency overestimation is harmless.

### Complete execution and exact endpoint inspection

Run from the notebook directory:

    python3 scripts/physical-corner/certify_148.py
    python3 scripts/physical-corner/inspect_certificate_148.py

The full computation took approximately88.36 seconds, within its
600-second cost ceiling. It saves incremental evidence and yielded
through the tool during execution. No refinement was needed.
`scripts/physical-corner/certificate-148.json` contains exact carrier
constants, all11 global gates, series remainders, source/helper hashes,
and all338 consecutive block records covering exactly1,...,690988.
Each block records its complete count, signed A/L sums, prime count,
positive minimum amplitude, positive minimum prime reduction margin,
and maximum log/phase/amplitude enclosure widths. Each per-term gate
must succeed to emit its block record. Incomplete blocks or exceptions
cannot produce the complete-support gate or the successful final status.
All failures are retained; this run's failure list is empty.

The second script imports no generating arithmetic. It inspects every
block, verifies exact adjacency/counts, independently sieves prime counts,
sums all rational block endpoints and checks equality with the recorded
totals. It recomputes S,F and E by exact Fraction endpoint operations,
checks the R square comparisons, and checks the displayed decimal
rational bounds against the exact final endpoints. All1370 inspection
checks pass. Its full evidence is
`scripts/physical-corner/inspection-148.json`. This is complete record
and endpoint inspection, not an independent replay of transcendental
values; no such stronger audit was claimed at step148. The separate
step150 replay below now supplies that audit.

The F,R,E and F±E exact endpoint records and all global gates were also
inspected in full after execution, using the supervisor's JSON inspector.
The numerical printout is only a convenience; all four bounds in the
conclusion are exact rational comparisons with the saved dyadic endpoints.
Thus the finite statement follows from the inclusion proof and complete
execution, subject to the stated informal implementation qualification.

### Two-sided scalar payment and conditional admission

From M32<81/4 and 0<ell-2log32<25, write
L32=L-(log32)A. Then |L32|<=M32 and

    S=(ell-2log32)A-2L32, |S|<25R+81/2.

Put a=A_true-A and b=B_true-S. The retained analytic/remainder/companion
bounds and |P|=1 give |a|<p and |b|<q. The exact expansion is

    Re(conj(A+a)*(S+b))-F
      =Re(conj(a)*S+conj(A)*b+conj(a)*b).

Its absolute value is <p*(25R+81/2)+R*q+p*q=E, by the triangle
inequality. This is the two-sided version of L960's existing payment;
it uses neither stability nor any lower bound for R. All cross terms,
including p*q, are charged. Hence

    F-E < Re(conj(A_true)*B_true) < F+E.

The finite bound just proved gives the conditional positive reserve.
L960's carrier identities, valid with N frozen, are
u=2Re(P*A_true), u'=-Im(P*B_true)/2. If u=u'=0, P*A_true is purely
imaginary while P*B_true is real, so their Hermitian product has zero
real part. Since |P|=1, this contradicts the reserve. Finally H_t=G*u,
H_t'=G'*u+G*u' with G(x)>0, proving the stated exclusion at this point.

This does not verify the assumed actual remainder or companion bounds.
Nor does one strict finite reserve pay any time/space extension, index
seams, initialization/recovery, exterior coverage, global continuation,
zero-time passage, or remaining Xi signs. It is a qualified local input.

### Independent complete replay (step150)

The unchanged SPECIALIZE coverage is
`drafts/literature/2026-11-10-physical-corner-independent-audit-148.md`,
separately approved before invocation. This audit reproduces known
included finite evaluation; it asserts no new general positivity theorem.
The primary arithmetic and series references above apply with the same
domains. The new evaluator imports neither the generator nor its helpers,
constants or stored numerical values. Source comparisons occur only
after the complete independent run. Reproduction commands are

    python3 scripts/physical-corner/independent_audit_150.py
    python3 scripts/physical-corner/inspect_audit_150.py

Here Q=2^224. The independently written `Box` represents integer endpoint
intervals divided by Q. Exact integer floor and ceiling enclose rational
constants; addition, sign reversal, and multiplication by integers are
exact. General multiplication takes all four endpoint products and
rounds the minimum down and maximum up after division by Q. For a divisor
excluding zero, reciprocal endpoints are the exact rational values
Q/hi and Q/lo, rounded outwards, followed by included multiplication.
Positive integer division rounds endpoint quotients outwards directly.
The square-root endpoints are isqrt(lo*Q), isqrt(hi*Q) with the upper
endpoint incremented precisely if its square is too small. These formulas
prove inclusion for every sign permitted by the code; the18 exact signed
operation checks are supplementary checks, not that proof.

Pi is recomputed by the different identity

    pi=4(atan(1/2)+atan(1/3)).

Tangent addition gives tangent1, and both positive angles are less than
pi/4, so their sum is pi/4. Each arctangent uses128 exact rational
alternating terms and its first omitted term. For atan(1/x) use four
terms and the same theorem; atan(x)=pi/2-atan(1/x), since x>0. Thus
the principal argument is checked without importing a numerical pi.

Logarithms use exact rational power-of-two scaling into [1,2), and a
separately evaluated log2. With z=(m-1)/(m+1) in [0,1/3], use64 terms:

    log m=2 sum_(j=0)^63 z^(2j+1)/(2j+1)+R,
    0<=R<=2z^129/(129(1-z^2)).

The terminal recurrence term encloses z^129. The positive-tail bound
follows by decreasing denominators and a geometric sum. Monotonicity
encloses logarithms of positive intervals. This is a fresh implementation,
with a different truncation from step148, not an imported log value.

The carrier is recomputed by independent algebra:

    Re(alpha)=log(1+x^2)/4-log(4pi)/2-1/(1+x^2),
    Re(alpha')=6(x^2-1)/(1+x^2)^2+1/(1+x^2),
    Im(alpha')=-4x/(1+x^2)^2-x/(1+x^2).

The earlier displayed Im(alpha), sigma, tau and ell then apply exactly.
Differentiation of log(M0) gives alpha (the 1/s terms combine to
1/(2s)); differentiation of t*alpha^2/4 supplies t*alpha*alpha'/2.
Since s_+'=i/2 and the minus branch is conjugate, ell=4Theta' has the
stated sign and alpha-prime correction. The physical character retains
the negative sign in -tau*log n. Both strict floor margins, ell-logN>13,
0<ell-2log32<25 and negativity of nonconstant amplitude exponents pass.
Their exact rational records are in the independent certificate.

A largest-prime-factor sieve independently supplies log n=log p+log(n/p).
An unmarked integer is prime because every composite has already been
visited by a smaller prime divisor. Marking all multiples of successive
primes leaves the largest prime divisor. In the composite case both
proper factors are less than n and have their logs computed already.
The prime logs use the fresh evaluator above. In contrast to step148,
**every** n>=2 has its phase evaluated directly from -tau*log n; no
composite phase is obtained by multiplying previously computed phases.
For n=1, log1=0, chi(1)=1 and a_1=1 are exact.

For each full phase interval choose an integer k, subtract 2k*pi, and
check the entire reduced interval is inside (-4,4). Any integer k is
permitted by periodicity; its midpoint-based selection is not itself a
branch certificate. Divide the reduced interval by16, obtaining |z|<1/4.
Evaluate cos through degree46 and sin through degree47 by independent
included Horner polynomials. Taylor orders47 and48, whose final
coefficients vanish, give absolute errors bounded respectively by

    (1/4)^48/48!, (1/4)^49/49!.

Their outward dyadic upper bounds are added on both sides. Four included
applications of (cos(2z),sin(2z))=(2cos(z)^2-1,2sin(z)cos(z)) give the
original reduced phase, retaining its sign and all input uncertainty.
This differs from the generator's direct large-angle polynomials and
prime-phase multiplication. No phase width is suppressed.

For every exponent v, the entire enclosure is checked in [-32,0]. Put
z=v/256 in [-1/8,0]. Evaluate sum_(j=0)^28 z^j/j! and add on both
sides the bound (1/8)^29/29!. Taylor's theorem licenses this bound:
exp's29th derivative is at most1 between z and0. After checking positive
lower endpoint, eight included squarings enclose exp(v). This directly
evaluates the negative-argument exponential, instead of the generator's
positive exponential followed by reciprocal. All terms have positive
amplitude lower endpoints; no natural-support term is dropped.

The complete run finished in approximately91.03 seconds and saved338
consecutive blocks through690988. It directly evaluated690987
nonconstant phases. All31 global gates pass with no recorded failure.
The full certificate `scripts/physical-corner/independent-audit-150.json`
contains carrier constants, finite remainders, every block's signed A/L
sum, support/prime/direct-phase counts, positive amplitude and reduction
minima, and maximum elementary enclosure widths. Each block can be
emitted only after its every-term assertions pass. The run did not need
a precision refinement, installation, parameter sweep or partial restart.

The independently written Fraction endpoint inspector reads every block,
checks exact adjacency and counts, independently sieves prime counts,
adds every block endpoint and checks equality with the saved totals.
It checks every carrier constant and every block A/L component for
agreement with the original enclosure; all overlap, with none used as
an input to the new run. It independently checks the norm by exact square
comparisons, S and F by all-sign endpoint arithmetic, the exact p,q and
the full payment including pq, and both endpoints F-E,F+E. All3087
checks pass; full evidence is `scripts/physical-corner/inspection-150.json`.
All recorded elementary widths are less than10^(-30). The comparison
checks are corroboration; the independent inclusion proof and complete
execution above establish the replay's bounds.

In particular its exact lower bound for F-E is

    4052247067866128686002974053300136901056835179059243764134790099644110 / 2^224
      >15030619/100000.

All stated F,R,E bounds are also independently confirmed. Complete final
carrier/gate/remainder/result values and the empty failure list were
inspected after execution. The two-sided transfer proof above was checked
against L960: |a|<p, |b|<q and |S|<25R+81/2 pay every cross term;
u=u'=0 forces the Hermitian real part to vanish, contradicting the
conditional reserve. This audit does not verify those retained analytic
hypotheses, the real gauge, or uniform frozen-N remainders. Nor does it
extend the sign away from this centre or supply any zero-time/Xi bridge.
The original step148 evidence is preserved. This is a successful local
proof audit with an informal implementation proof, not formal verification
or progress beyond the checked sources toward RH positivity.

## Mathlib

A full matching theorem for this exact complete physical sum and its
certificate is not checked. Supporting interval and elementary-function
results were not newly searched here; reuse the assessed mathematical
methods above, with no Lean port or formal verification claim. Unknown
matching coverage is not evidence of absence. No cross-notebook input.
