# Lemma 914: uniform low-time first logarithmic Hankel positivity

## Hypotheses

Use the exact positive kernel K of L019 and the L058 heat family

    F(lambda,z)=integral_0^infinity exp(lambda*u^2)K(u)cos(zu)du,
    M_k(lambda)=integral_0^infinity u^k exp(lambda*u^2)K(u)du.

Assume the arithmetic contracts of L037 for Python's standard-library
Decimal implementation: directed basic arithmetic, correctly rounded
exponential widened to adjacent representable neighbors, and rejection
of invalid operations, zero-containing divisors, overflow, underflow
and subnormal arithmetic. The certificate uses 100 significant digits.
No independent verification of that arithmetic library is claimed.

For real lambda define the logarithm germ at z=0, with value zero, by

    log(F(lambda,z)/M_0(lambda))
        =-sum_(k>=1) S_k(lambda) z^(2k)/k,
    H_1(lambda)=[[S_2,S_3],[S_3,S_4]].

These are L874's local coefficients, without a deformed reciprocal-zero
interpretation or any hypothesis that all zeros are real.

## Conclusion

For every real lambda in the **closed** interval [0,1/20],

    M_0(lambda)>0.49712,
    S_2(lambda)>3.714*10^(-5),
    9.7*10^(-16)<det H_1(lambda)<7.026*10^(-15).

Consequently H_1(lambda) is positive definite throughout that interval.
There is no nonzero real vector c with H_1(lambda)c=0 there; both null
rows and the possible S_2=0 case are excluded by strict enclosures.

This is a computer-assisted finite partial result, independently
audited in step182 under the stated arithmetic contracts (it was
unaudited at creation). It proves neither a contact-flux sign nor
higher-degree positivity, initialization, tangency, global parameter
continuation or RH. The source comparison did not supply a matching
uniform determinant theorem; no claim of certified originality is made.

## Proof

### Positive-time normalization and finite extraction

L058 gives joint entirety, differentiated moment formulas and
M_0(lambda)>0 for every real lambda. Around any fixed such lambda,
F(lambda,z)/M_0(lambda) is nonzero near z=0 and equals 1 at zero.
Its normalized analytic logarithm therefore exists locally. Its
Taylor series is

    F(lambda,z)/M_0(lambda)
        =1-a*z^2+b*z^4-c*z^6+d*z^8+O(z^10),
    a=M_2/(2M_0), b=M_4/(24M_0),
    c=M_6/(720M_0), d=M_8/(40320M_0).

The finite logarithm calculation of L033 applies to this series
unchanged. In particular,

    S_2=a^2-2b,
    S_3=a^3-3ab+3c,
    S_4=a^4-4a^2*b+2b^2+4ac-4d,
    D=S_2*S_4-S_3^2.

This reuses the finite coefficient identity, not L033's zero-time
positivity premise. Every sign asserted below is certified anew.
No zero ordering, product over zeros or global logarithm is used.

### Complete uniformly tilted tails

Put X=exp(2u) and beta=119/40. For u>=0 the positive exponential
series gives X>=2u^2. Thus for 0<=lambda<=1/20 and n>=1,

    lambda*u^2<=X/40<=n^2*X/40.

For k=0,2,4,6,8, u^k<=exp(8u): on [0,1] use u^k<=1,
and on [1,infinity) use k*log u<=8u. Each K_n is positive by
L019. As in L035, pi>3, pi<4 and

    sum_(n>=1) n^4 exp(-pi*n^2*X)
        <= exp(-pi*X)/(1-16exp(-3pi*X))
        <=2exp(-pi*X),                    X>=1.

Here n^4<=16^(n-1) follows from n<=2^(n-1) by induction;
n^2>=1+3(n-1) follows from (n-1)(n-2)>=0. Finally
16exp(-9)<1/2, for example by the positive exponential series.
Dropping the negative term of K_n and using the first tilt inequality
therefore gives

    u^k exp(lambda*u^2)K(u)
        <=256 exp(25u/2) exp(-beta*X).

The full spatial tail after u=2 is at most

    E_space=128 exp(-50beta)
        *sum_(j=0)^6 [6!/(6-j)!]50^(6-j)/beta^(j+1).

Indeed d u=dX/(2X) leaves X^(21/4), which is at most X^6
on X>=1; exp(4)>50 by the series through degree seven.
Enlarge the integration range to [50,infinity), and integrate
X^6 exp(-beta X) by parts six times to obtain that expression.

For the omitted theta terms n>=5, bound their contribution on
[0,2] by their integral over [0,infinity). The second tilt
inequality and the same substitution give the upper bound

    64 sum_(n>=5) n^4 integral_1^infinity X^6 exp(-beta*n^2*X)dX
    <=64*720 sum_(n>=5) n^4 exp(1-beta*n^2).

For X>=1, exp(-beta*n^2*X)<=exp(1-beta*n^2)exp(-X), since
(beta*n^2-1)(X-1)>=0. The gamma integral of X^6 is 720.
Write n=5+j. Then n<=5*2^j by induction, n^4<=625*16^j,
and n^2>=25+11j for integral j>=0, since j(j-1)>=0. Hence

    E_theta=57,600,000 exp(1-25beta)

is an upper bound: the geometric denominator
1-16exp(-11beta) exceeds 1/2. For example beta>2 and
exp(22)>32 by its positive series suffice for this last inequality.
The complete common discarded contribution is nonnegative and at most

    E_tilt=E_space+E_theta<7.836*10^(-25).

The last rational threshold is checked by the outward exponential
evaluations in the saved certificate. This bound includes both the
entire omitted theta series and the unbounded spatial tail, uniformly
for all lambda in the closed interval. It is not an untilted-tail
substitution. Overlap of the two upper bounds only enlarges the error.

### Uniform finite quadrature and arithmetic

The producer is `scripts/heat/low-time-h1-uniform-180.py`. It imports
the unchanged interval primitives, rational Machin pi enclosure and
normalized derivative recurrences from
`scripts/hankel/certify_hankel.py`, setting all three arithmetic
contexts to precision 100. L037 proves their inclusion property
under the stated contracts; its 96 rational arctangent terms give
an enclosing pi interval at this precision as well. The official
[Decimal arithmetic documentation](https://docs.python.org/3/library/decimal.html)
is the arithmetic contract, not a theorem about the theta moments.

The parameter panels are exactly

    [p/5120,(p+1)/5120], p=0,...,255.

They share endpoints, cover [0,1/20], and contain no gaps. On each,
64 spatial panels [2i/64,(2i+2)/64], i=0,...,63, cover [0,2],
with half-width h=1/64 and midpoint (2i+1)/64. Only K_1,...,K_4
are integrated finitely. For each k the untilted spatial derivative
jets are cached, both at the midpoint and over the whole spatial
panel, and multiplied by the jet of exp(lambda*u^2).

The exponent jet has normalized coefficients lambda*u^2,
2lambda*u, lambda, followed by zeros. Enclosing u by the whole
spatial panel and lambda by the whole parameter panel in the
product and exponential recurrences of L036 encloses the eighth
normalized spatial derivative at every point of the rectangle.
At the spatial midpoint the same full parameter interval encloses
all lower coefficients for every lambda in the panel. No parameter
is represented just by a sampled value.

For each fixed lambda in that panel, L036 gives the integral enclosure

    2 sum_(j=0,2,4,6) f_j h^(j+1)/(j+1) + [-R,R],
    R=2h^9/9 * sup |f^(8)|/8!.

The uniform derivative intervals supply this supremum bound. Sum
the 64 enclosures by outward addition and add [0,E_tilt] to every
moment. The coefficient and determinant formulas above are then
evaluated by enclosing operations. Every mass lower endpoint is
strictly positive, so all normalized divisions are permitted.
Induction over these finite interval operations establishes
containment of the exact quantities for every lambda in each panel.

### Complete certificate and sign verification

Reproduction commands, relative to this notebook, are

```text
python3 scripts/heat/low-time-h1-uniform-180.py
python3 scripts/heat/low-time-h1-uniform-180-check.py
```

The full producer certificate is
`scripts/heat/low-time-h1-uniform-180.json`. It retains all 256 closed
parameter intervals, all five moment enclosures and quadrature
remainder bounds per panel, normalized coefficients, S_2/S_3/S_4,
both determinant expressions, all tail bounds and the complete empty
failure list. All 256 panels have strictly positive lower endpoints
for S_2 and D; no exceptional arithmetic occurred. The rational
thresholds in the conclusion are strict bounds on the minimum lower
or maximum upper endpoints across all panels, not point estimates.

The separate checker uses exact Fraction endpoint operations to
replay all moment-to-coefficient-to-determinant calculations,
checks their containment in the saved outward Decimal intervals,
verifies the exact closed endpoints and all strict thresholds,
and recomputes the summary extrema. Its complete report is
`scripts/heat/low-time-h1-uniform-180-check.json`, with 256/256
panels passed and no failures. This replay addresses the substantial
algebraic cancellation in D; it does not independently check the
exponential library or reprove the quadrature inclusion argument.

The expanded polynomial for D from L033 is also evaluated in the
producer and must overlap the first determinant expression on every
panel. Its interval can contain zero: it is a consistency check,
not the sign certificate. The sign uses S_2*S_4-S_3^2 and its complete
enclosing arithmetic. Neither samples nor an interval preview is
used as evidence of coverage.

Finally, for real x,y the exact identity

    (x,y)H_1(x,y)^T
        =S_2*(x+S_3*y/S_2)^2+(D/S_2)*y^2

is strictly positive for every nonzero pair by the certified strict
lower bounds. It proves positive definiteness and excludes every
nonzero null vector, without dividing by an unproved sign. This
completes the stated conditional computer-assisted proof.

### Independent audit — 9 November 2026, step182

The audit accepts the stated bounds under L037's contracts. It is a
reproduction and verification of this finite partial result, not a new
mathematical discovery beyond the sources checked. No defect was found.

The local normalization needs only M_0>0, joint analyticity from L058,
and the logarithm germ with value zero; it uses neither a global
logarithm nor a deformed reciprocal-zero product. Comparing the
coefficients of t=z^2 in log(1-at+bt^2-ct^3+dt^4) gives the displayed
S_2,S_3,S_4 with the correct factors 2,3,4. The positive-definiteness
identity uses the independently certified S_2>0. L874's contact
equations and C874a are not assumptions of this proof.

For the tails, the audit checked X>=2u^2 from the quadratic term of
exp(2u), each positive K_n, and both distinct tilt inequalities. The
spatial bound uses exp(X/40) times the summed untilted majorant; the
omitted-series bound uses exp(n^2 X/40) term by term. Both leave decay
at least exp(-beta X), respectively exp(-beta n^2 X), with beta=119/40.
The Jacobian is 1/(2X); the remaining power is X^(21/4)<=X^6. All
constants, the geometric denominators, the extension down to X=50,
and the gamma integral 720 were checked. The nonnegative omitted
pieces exhaust the complement of the finite rectangle. Counting part
of that complement twice only increases the bound.

The code audit checked the actual kernel jet, not only the generic
recurrences: with v=pi*n^2*exp(2u), it computes
exp(u/2)*(8v^2-12v)*exp(-v), equal to K_n. Multiplication by the
binomial jet of u^k and then exp(lambda*u^2) gives precisely the
intended integrand derivatives. The latter exponent's normalized
coefficients are lambda*u^2, 2lambda*u, lambda, and zeros. Full-panel
evaluation therefore contains the eighth derivative on every closed
rectangle. The midpoint weights and 2h^9/9 remainder are those of
L036; the absolute endpoint maximum bounds the eighth coefficient.
The implementation adds symmetric upper remainder bounds and the
nonnegative tilted tail to every moment. All mass divisions are safe.

Endpoint constructors are exact for integers and directed for
rationals. The live three contexts use precision 100, the required
FLOOR/CEILING/HALF_EVEN modes, and all five exceptional-arithmetic
traps. Integer powers use multiplication, not Context.power. Endpoint
negation and absolute value are exact copy operations; exponentials
use Context.exp widened with its neighboring representable values.
No forbidden flags were set during the full replay. Inexact and
Rounded flags are expected and do not invalidate inclusion. A few
elementary self-test comparisons use the default Decimal context;
they do not enter the integral enclosures, and their inequalities
were separately confirmed by exact rational arithmetic.

Reproduce the expanded audit with

```text
python3 scripts/heat/low-time-h1-uniform-audit-182.py
```

Its complete report is `scripts/heat/low-time-h1-uniform-audit-182.json`;
the full replay is `scripts/heat/low-time-h1-uniform-replay-182.json`.
The complete replay equals the original certificate in every field,
including all 256 moment and remainder records. The separate Fraction
checker was rerun and every entry of its 256-panel report was verified.
The original scripts, certificate and checker report retained their
SHA256 hashes. The report binds these inputs and the interval module;
the observed Python version was 3.15.2. Replaying the producer is an
execution check, not an independently implemented quadrature algorithm;
the analytic and code review above establishes its inclusion argument.

The audit additionally encloses the tail constants using exact rational
arithmetic, independently of Decimal.exp. For x>=0, sum the positive
series of exp(x) through degree 1000. The tail is at most its next term
divided by 1-x/1002, since subsequent term ratios are at most x/1002<1
for every x used. Reciprocation encloses exp(-x). These rational
enclosures of the exact spatial, theta and summed constants lie inside
the original saved intervals and prove E_tilt<7.836*10^(-25).
The Machin/arctangent rational enclosure of pi was independently
recomputed and is contained in the saved pi interval. This does not
verify Decimal.exp for the finite quadrature, which remains assumed.

All 256 exact closed parameter endpoints and strict sign thresholds
passed. The minimum lower determinant endpoint occurs on panel 0
and is greater than 9.7189*10^(-16); the largest upper endpoint occurs
on panel 255 and is less than 7.0254*10^(-15). The saved complete
endpoints, rather than these abbreviated values, were tested against
the claimed rational bounds. The expanded-polynomial interval on
panel 0 contains zero, as expected from dependency overestimation;
the separately enclosing primary expression remains strictly positive.
There is no contact, sign counterexample, higher-degree certificate or
global continuation conclusion in this audit.

## Mathlib

Full matching coverage and supporting theorem names are not checked.
This is not evidence of absence from Mathlib. The finite interval
computation has not been formalized in Lean. The inherited arithmetic
contracts and real analytic/moment arguments have the qualifications
stated above; no Mathlib completion claim is made.
