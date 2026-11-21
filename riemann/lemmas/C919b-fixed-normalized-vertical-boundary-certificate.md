# Corollary 919b: fixed normalized vertical boundary certificate (audited)

## Hypotheses

Use L019's exact kernel and L058's entire heat family F(lambda,z), with
0<=lambda<=1/20. Use the L919 normalization F(lambda,z)=8H_(4lambda)(2z).
Numerical statements below rely on Python 3.15.2's documented Decimal
arithmetic contracts, as in L037, extended explicitly below to complex
rectangles. The source theorem is D. H. J. Polymath, *Effective
approximation of heat flow evolution of the Riemann xi function, and a
new upper bound for the de Bruijn-Newman constant*, Research in the
Mathematical Sciences 6 (2019), article 31, arXiv:1904.12438v2,
4 August 2019, Theorem 1.3 and Corollary 1.4, equations (5)-(19),
(23)-(25), with the complete error proof in Section 6.3,
Proposition 6.6(iv)-(vi): https://arxiv.org/html/1904.12438v2#S1.
No optional estimate (20)-(22), ABC correction, zero census, simplicity,
RH, or all-real-zero assumption is an input.

## Conclusion

The fixed computer-assisted test passed on all 2048 boxes, with no guard
failures. Subject to the stated arithmetic contracts, the argument below
gives

    F(lambda,100+iy) != 0,
    0<=lambda<=1/20,  |y|<=1/2.

In source coordinates it gives the stronger normalized bound

    |H_t(200+iY)/B_t(200+iY)| >= 18367/100000,
    0<=t<=1/5, 0<=Y<=1.

This is an **audited local computer-assisted certificate**, accepted
under the stated arithmetic contracts in step2154 below. It is not
a complete RH candidate or a formally verified arithmetic calculation.
This is a local specialization of the published criterion, not progress
beyond its approximation theorem. It does not certify a complete region
boundary, a radial head, its reality/census/continuation or eigenvalue
margin, higher-degree positivity, or RH.

## Proof

### Source coordinates and exact expressions

Write t=4lambda and Y=2y. For nonnegative local y, the source parameters
are x=200, 0<=Y<=1, 0<=t<=1/5. At positive t these satisfy every
hypothesis of (5). The source theorem gives

    |H_t(200+iY)/B_t(200+iY)-f_t(200+iY)| <= e_A+e_B+e_C,0.

Here f_t and its actual gamma, s_* and kappa are defined in (14)-(19).
The implementation evaluates exactly those expressions, using gamma
as exp(log M_t((1-Y+200i)/2)-log M_t((1+Y-200i)/2)). It evaluates
s_*=(1+Y-200i)/2+(t/2)alpha((1+Y-200i)/2) and
kappa=(t/2)(alpha((1-Y+200i)/2)-alpha((1+Y+200i)/2)).
The two sums each have n=1,2,3. The positive weights b_n^t are
exp(t(log n)^2/4), and n to any complex power is exp of that power
times the real log n, with the signs in (14).

The complete errors are bounded by the full right sides of (23) and
(24); both are evaluated, without dropping terms or using their
asymptotic substitutes. In (23) the enclosed actual |gamma| and
|kappa| are used, and the actual Re(s_*) is retained. Source decimal
constants 0.626, 6.66, 1.24, 0.125 and 10.44 are exact rationals.
In (24) |log(x/(4pi))+i*pi/2| is a complex modulus, not a real
absolute-value substitute. This imports the already proved complete
theta/integration error; no new asymptotic approximation is claimed.

The cutoff guard encloses sqrt(200/(4pi)+[0,1/5]/16) strictly
between 3 and 4, proving N=3 throughout. Thus no cutoff jump occurs,
including at zero time. This guard precedes the box evaluations.

### Real and rectangular complex inclusion

Run `python3 scripts/heat/fixed_boundary_2152.py`. The complete evidence
is `scripts/heat/fixed-boundary-2152.json`. All numerical operations
use 100 significant Decimal digits. No binary floating-point input
or general Decimal noninteger power is used. Integer and printed
decimal constants are exact; rational input endpoints are converted
with separate downward/upward divisions.

Real interval addition, subtraction, multiplication and division have
the directed endpoint rules in L037; a denominator containing zero
is rejected. The square operation takes zero as its lower endpoint
when the input interval straddles zero, otherwise the smaller squared
endpoint. Its upper endpoint is the larger squared endpoint. Both
are rounded outward. Thus it preserves the real square even when
the same variable occurs twice. Real exp and log are monotone; their
documented correctly rounded half-even endpoint values are widened
to adjacent representable numbers. Supporting primary documentation:
https://docs.python.org/3.15/library/decimal.html (exp, ln, contexts,
next_minus/next_plus). For sqrt, widened endpoints are accepted only
after exact Fraction comparisons lo^2<=input.lo and hi^2>=input.hi;
the lower endpoint is zero for an input lower endpoint zero.
Division by zero, invalid operations, overflow, underflow, subnormal
operations and clamping are trapped. A failed arithmetic or domain
guard makes the box fail, rather than supplying evidence of nonvanishing.
This relies on the Decimal implementation, not an independently
verified arithmetic kernel.

Pi uses precisely L037's 96 rational terms in each Machin arctangent.
The next alternating term encloses each remainder; rational lower
and upper bounds and their outward decimal conversions are saved.
The resulting enclosure, rather than a machine pi constant, is used
in every subsequent expression.

A complex rectangle is a pair of real intervals. Addition and
multiplication use (a+ib)(c+id)=(ac-bd)+i(ad+bc), with outward
real operations. Division uses the positive enclosure of c^2+d^2
and (ac+bd)+i(bc-ad), rejecting a zero lower bound for the denominator.
Conjugation negates the imaginary interval exactly. Modulus encloses
sqrt(a^2+b^2), with the square rules just specified. Consequently
each expression encloses its values over the whole parameter box;
loss of correlations can only widen it.

### Elementary complex functions, branches and full tails

The needed identities are the principal logarithm in NIST DLMF
4.2.5, https://dlmf.nist.gov/4.2.E5, its local series DLMF 4.6.1,
https://dlmf.nist.gov/4.6.E1, and the exponential/trigonometric
identities and series in DLMF 4.14.3 and 4.19.1-2,
https://dlmf.nist.gov/4.14.E3 and https://dlmf.nist.gov/4.19.
The following tail estimates and branch checks justify this particular
finite implementation of those identities, rather than reproving the
source heat approximation.

For each complex log argument z the imaginary interval has one strict
sign sigma in {+1,-1}. Choose the positive exact endpoint
A=max |Im z|, and form w=z/(sigma*i*A)-1 by enclosing operations.
The code verifies |w|<=rho<1 and Re(1+w)>0. Hence 1+w is in the
right half-plane and arg(1+w) is strictly between -pi/2 and pi/2.
Adding sigma*pi/2 puts the resulting argument strictly in (0,pi)
when sigma=+1 and (-pi,0) when sigma=-1. It is therefore the
principal log, with no omitted branch integer:

    Log z = log A + sigma*i*pi/2
            + sum_(n=1)^128 (-1)^(n+1) w^n/n + R,
    |R| <= rho^129/(129*(1-rho)).

The tail bound follows by replacing 1/n by 1/129 in the remaining
absolute series and summing a geometric series. A symmetric real
interval of that radius is added to each coordinate. In source (7)
and (9), Log(s/2)=Log(s)-log 2 and
Log(s/(2pi))=Log(s)-log(2pi), since both scaling factors are positive.
All required s and s-1 have imaginary part +100 or -100, so they
are away from the cut and zero; actual inclusion guards remain
recorded for each occurrence.

For exp(a+ib), enclose exp(a)(cos b+i sin b). Choose an integer q
and form r=b-2q*pi, with the *interval* pi. The integer is selected
from a midpoint quotient, then the complete reduced interval is
required to satisfy |r|<=4. Selection accuracy is immaterial once
this guard passes: the exact 2q*pi subtraction and periodic identity
are enclosed. The sums retain 128 nonzero terms each, through
degree 254 for cosine and 255 for sine. If a_r bounds |r|, their
absolute remaining tails are bounded by

    cosine: [a_r^256/256!] / [1-a_r^2/(257*258)],
    sine:   [a_r^257/257!] / [1-a_r^2/(258*259)].

The denominator ratios bound every successive absolute term ratio
after the first omitted term, and are <1 since a_r<=4. The code
adds the respective symmetric tail intervals. Series recurrences
and every tail operation are outward interval operations. Thus
reduction, truncation, input width and arithmetic error are all paid.

The normalizer is B_t=M_t(s) for s=(1+Y-200i)/2. Formula (7) is a
finite holomorphic log there; its ingredients s,s-1,s/2 avoid the
principal cuts and zero. Adding t*alpha(s)^2/4 gives log M_t(s),
so B_t is its exponential and never vanishes. The code encloses
this logarithm and saves the normalizer/branch guards; it does not
assume an uncertified complex special-function routine.

### Whole-box coverage and zero time

The boxes are exactly

    t in [j/160,(j+1)/160], j=0,...,31,
    Y in [k/64,(k+1)/64], k=0,...,63.

All are closed and together cover [0,1/5]x[0,1]. On each box the
rectangle for f supplies a modulus lower bound l; the right sides
of (23)+(24) supply an upper bound e. Downward rounding of l-e
gives its certified margin. Every box, rational endpoint, actual
finite-sum term, error component and guard is saved in the certificate,
with a separate failure list. This is a whole-box calculation, not
sampling. The pass condition is l-e>0 on every box.

If the completed run provides a common positive bound m, then for
every positive source time the source theorem and triangle inequality
give |H_t/B_t|>=m. At t=0 the source theorem is not applied directly.
By L058 and L919, H_t is continuous in t,Y on this band; the explicit
nonzero B_t is continuous there as just checked. For each fixed Y,
pass to t down to zero in |H_t/B_t|>=m. This proves the same bound
at t=0, hence nonvanishing there. Finally F=8H_(4lambda)(2z)
transfers the conclusion to 0<=y<=1/2, and L058's conjugation
for real lambda transfers it to -1/2<=y<0.

### Completed numerical evidence and integrity checks

All 2048 boxes returned enclosures and positive margins, with zero
failures. The minimum downward-rounded margin was

    0.183670203528956838645203645708405963280030713240498154996944659823371210136139499573626057166830854

at j=0,k=63, namely t in [0,1/160], Y in [63/64,1]. On that box
the saved modulus lower bound is

    1.381822231829855332272485945734916420381376488181887759129278524109162509052952923111736427556046430

and the complete error upper bound is

    1.198152028300898493627282300026510457101345774941389604132333864285791298916813423538110370389215576.

The cutoff square-root interval lies in (3.9894,3.9910). Every log
series radius is <=0.0100001, and every reduced trig argument has
absolute value <3.237. The maximum recorded log tail radius is
<7.831e-261; the maximum trig tail radius is <4.291e-377. These tails
are already included in the enclosures, not further unpaid errors.
There are 18432 complex log and 14336 trig calls, 53250 exact squared
sqrt endpoint checks and 116736 recorded domain/branch guards.

Run `python3 scripts/heat/fixed_boundary_integrity_2152.py` for a
complete exact-rational inspection of the saved coverage, every box's
modulus lower bound, addition of the two complete error upper bounds,
downward margin, >18367/100000 threshold, and each recorded guard's
numerical threshold. All 6150 integrity checks pass, with zero failures;
the full report is `scripts/heat/fixed-boundary-integrity-2152.json`.
It records source-script and certificate SHA256 hashes and the worst
box's complete bounds. The complete worst bounds and empty failure
list were inspected, alongside the enclosing rectangle for f. This
integrity pass is not an independent mathematical audit or a second
boundary calculation. Inclusion of the source expressions and tails
is justified above, rather than by a preview or the integrity checks.

Take m=18367/100000 in the preceding positive-time and limit argument.
All hypotheses for that conditional implication are supplied by the
fixed run and explicit branch proof. This establishes the stated local
certificate under its arithmetic contracts; the audit below accepts it.
No unpaid head/global assumptions are inferred.

### Independent conceptual audit, 21 November 2026 (step2154)

**Verdict.** Accepted under precisely the original Decimal contracts.
The fixed test, source script and original two JSON artifacts are
unchanged. No mathematical defect was found. The audit checks inclusion
and logical applicability separately from reproduction of the output;
replay alone would not justify this verdict. This accepts an existing
known-method specialization, not a new analytic bound beyond Polymath's
theorem and not an all-degree positivity result.

**Source-to-code comparison.** Reopened the cited v2 primary source,
(5)-(19), (23)-(25), (69)-(74), Proposition 6.6(iv)-(vi), and the
proof cases from (77) through its conclusion. The theorem includes
x=200 and both Y endpoints; only t=0 is excluded. In `alpha`,
1/(2s)+1/(s-1)+(Log(s)-log(2)-log(pi))/2 is exactly (9).
In `logm`, the constant is log(sqrt(2pi)/16), and the factor of
Log(s/2) is s/2-1/2, as in (7). Its added t alpha(s)^2/4 is (10).
Thus `gamma`, `star`, `kappa`, `first` and `second` are respectively
(16), (17), (18), and the two sums of (14), with n=1,2,3.
Conjugation is applied to star before adding kappa, as required.
No use of either version of the disputed optional bound (21) occurs.

For (23), `LOGR-2*l` is log(x/(4pi n^2)); the exponential numerator
is t^2 times its square divided by 16, plus 0.626; its denominator
is x-6.66. Each summand uses b_n^t/n^Re(s_*) multiplied by the
full factor 1+|gamma|N^|kappa| n^Y. The singleton
`upper(gamma.modulus())` and `upper(kappa.modulus())` are upper
bounds, not two-sided enclosures of the exact moduli. This is valid
here: log(3)>0 and every remaining factor is nonnegative, so replacing
the two moduli by larger values increases the right side of (23).
Only the upper endpoint of this majorant is used. Its lower endpoint
is not asserted to bound the original e_A+e_B from below.

For (24), `ec` exponentiates the sum of all four displayed exponent
terms, including -(1+Y)log R/4. Its 1.24(3^Y+3^-Y)/(3-0.125)
term is retained, as are the complex modulus and 10.44/(x-12).
Section 6.3 distinguishes e_C from e_C,0; the latter contains the
constant contribution. The implementation uses the complete (24),
not the smaller e_C bound. The specified normalizer and its finite
holomorphic logarithm are exactly those of (7), (10), (11).

**Arithmetic and all elementary tails.** Read every operation in
`fixed_boundary_2152.py`. Decimal construction of integer/decimal
inputs is exact; rational division is directed. All bound-bearing
addition, subtraction, multiplication and reciprocal operations use
the specified contexts. Sign changes use copy_negate/copy_abs, not
context-rounded unary operations. No binary float or general Decimal
power enters a bound. The only approximate integer choice is the
trig reduction index; correctness follows from the complete reduced
interval guard for whichever integer is chosen. The elementary
context exponent limits are not reached and the exceptional arithmetic
signals listed above are trapped. Sqrt endpoints pass exact squared
checks, and exp/ln are widened under the imported contracts.

The real square rule, rectangular product, reciprocal, conjugation
and modulus rules enclose their exact operations by induction. Lost
correlations cannot narrow them. For each of the nine logs per box,
the rotation uses a positive exact A and a strict imaginary sign;
the radius and right-half-plane guards fix the principal branch.
The finite series includes n=1 through 128 and its entire geometric
tail beginning at 129. Log scaling by positive 2 or 2pi introduces
no branch offset. The cosine/sine recurrences end at degrees 254/255;
their first omitted terms are 256/257 and their subsequent ratios are
bounded by a_r^2/(257*258), a_r^2/(258*259). The guard a_r<=4 makes
both geometric denominators positive. Every term and tail is rounded
outward, including the interval pi used for reduction. Pi itself was
independently reconstructed from the exact 96-term rational series.

The `nonzero explicit normalizer` guard is hard-coded true, so it
cannot establish nonvanishing by itself. Its justification is analytic:
all the log arguments s,s-1 have imaginary part -100, hence are
nonzero and off their cuts for all Y in [0,1]. The specified log M_t
is finite and continuous throughout this band, and its exponential
never vanishes. No lower bound on a tiny computed |B_t| is needed.

**Complete saved evidence.** Run
`python3 scripts/heat/fixed_boundary_audit_2154.py`.
The full audit record is `scripts/heat/fixed-boundary-audit-2154.json`.
Under Python 3.15.2 all 2048 original boxes, every saved expression,
every finite-sum term and every guard reproduced exactly. This replay
uses the manually audited original implementation, not an independent
arithmetic backend. A separate exact-Fraction inspection checked every
box's rational coverage, squared modulus lower bound, sum of complete
error upper bounds, subtraction margin and strict 18367/100000 test.
It also checked every guard's actual evidence, not only its passed flag.
All 116736 guards pass: 45056 complex divisors, 18432 each for log
sign, log radius and log rotation, 14336 trig reductions, and 2048
normalizers. The 53250 squared sqrt checks and all saved extrema
reproduce. All nine global checks pass and the complete failure list
is empty. Source, certificate and original integrity hashes match the
old report and remain unchanged after the audit.

The exact cutoff bounds, full worst-box rectangle and bounds, global
checks and complete empty failure list were inspected from the report.
The worst box remains j=0,k=63 with the full margin printed above;
that exact decimal exceeds 18367/100000. The count of 2048 closed
boxes and their rational endpoints gives the full band, including
every edge. This is stronger evidence than sampling or a JSON preview.

**Endpoint and dependency check.** L019 gives K(u)=4 Phi(u/2), so
the substitution u=2w in L058's absolutely convergent integral proves
the L919 normalization F(lambda,z)=8H_(4lambda)(2z). It uses no
zero-location or product premise from other parts of L919. L058's
compact domination gives continuity in both parameters. The nonzero
continuous normalizer therefore permits the limit t down to zero
at each fixed Y with the same positive margin. Neither uniformity
of an asymptotic as t goes to zero nor a zero enumeration is used.
Conjugation for real lambda completes the negative-height segment.
The direct inputs remain L019,L037,L058,L919; no DAG change is needed.
The initial census, remaining region boundary, radial/rectangular
accounting, head reality/continuation and eigenvalue margin, and
higher-degree/global assembly remain independent unpaid obligations.

## Mathlib

Full matching coverage of this complex-box certificate, explicit source
errors, and endpoint specialization has not been checked. L037 also
does not assert a full matching formal theorem. Supporting definitions
alone would not certify the code or its recorded outputs. Unknown
availability is not evidence of absence.
