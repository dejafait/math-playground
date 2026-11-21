# L815: explicit real-path tails for the bounded Pólya census

## Hypotheses

Use exactly K,F,Q,S,c,G and W of L019/L020/L814. For real x and
j=0,1,2, evaluate the j-th x derivative of F by integrating its cosine
or sine integrand on 0<=u<=3, using only theta terms 1<=n<=4.
Evaluate S and its derivatives by integrating Q on the same interval.
The finite integrals must themselves be enclosed, not merely sampled.

## Conclusion

For each of the three orders, the omitted theta-series contribution on
[0,3] has absolute value at most

    E_n=27*16*pi^2*exp(13.5)*625*exp(-25*pi).

For each order and either kernel, the improper-integral contribution
on [3,infinity) has absolute value at most

    E_u=16*pi*exp(13.5)*exp(-pi*exp(6)).

Thus the F enclosure needs an added symmetric error E_n+E_u, and the
S enclosure an added symmetric error E_u. These are uniform in all
real x, including x=0 and 40. Normalization c must be evaluated from
full F(0),S(0) enclosures, with S(0) bounded strictly positively.
These are loose reproduction/specialization bounds, not new decay theory.
The implementation and numerical enclosures below are unaudited.

## Proof

The trigonometric factors in the derivative integrands have modulus at
most one; the additional factor is u^j. On [0,3], u^j<=9 for j<=2.
Dropping the negative part of each positive theta term of L019 gives,
for n>=5 and 0<=u<=3,

    0<k_n(u)<=8*pi^2*exp(13.5)*n^4*exp(-pi*n^2).

For a_n=n^4 exp(-pi n^2), n>=5,

    a_(n+1)/a_n <= (6/5)^4 exp(-11*pi)<1/2.

The last bound follows already from pi>3 and exp(33)>1+33.
Consequently sum_(n>=5) a_n<=2*625 exp(-25*pi).
Multiply by the interval length 3 and the moment bound 9 to get E_n.
Absolute convergence from L016/L020 justifies integrating the bound
and identifying these tails with the omitted derivative integrands.

For the improper tail put v=pi exp(2u), u>=3. Dropping negative parts
again bounds K by

    8*pi^2 exp(9u/2) exp(-v)
                  * sum_(n>=1) n^4 exp(-(n^2-1)v).

The last sum is less than 2 for v>=pi. Indeed its n=1 term is 1;
the n=2 term is at most 16 exp(-3*pi)<1/4 (use pi>3 and the
first five terms of exp(9)). Subsequent ratios for n>=2 are at most
(3/2)^4 exp(-5*pi)<1/2: pi>3 and exp(15)>1+15 suffice.
The n>=2 sum is therefore less than 1/2. In particular

    K(u)<=16*pi^2 exp(9u/2) exp(-pi exp(2u)).

For Q, drop the negative cosh term in L814, bound cosh(9u/2) by
exp(9u/2), and use 2cosh(2u)>=exp(2u). Exactly the same upper bound
holds; Q is positive by L814. Since u^j<=exp(ju) for u>=3, the
absolute tail for either kernel is at most

    16*pi^2 integral_3^infinity
                      exp((9/2+j)u) exp(-pi exp(2u)) du
      =8*pi^2 integral_(exp(6))^infinity y^(5/4+j/2) exp(-pi*y) dy.

Set b=5/4+j/2<=9/4 and y0=exp(6). The logarithmic derivative of
y^b exp(-pi*y) is b/y-pi<=-pi/2 for y>=y0, since y0>1+6 and
pi>3 imply b/y0<pi/2. Integration of this exponential majorant gives
an upper bound

    16*pi * exp((5/2+j)*3) exp(-pi exp(6)) <= E_u.

No complex-path bound, asymptotic error, or infinite-series quadrature
callback is used. All tails and derivatives are real-path estimates.

### Bounded implementation evidence and qualifications

Run `python3 scripts/polya-census/census-579.py`. The source implements
directed 50-digit Decimal interval arithmetic. Decimal exp is rounded
to nearest and enlarged by one representable neighbor on each side.
Pi is enclosed by Machin's identity, using 120 terms in each alternating
arctangent series and its next-term remainder. For trigonometric factors,
reduce the midpoint argument by 256, where its magnitude is at most 1
(the actual unreduced arguments are in [0,120]); use Taylor polynomials
through cosine degree32 and sine degree33, each with error <=1/34!,
then eight double-angle steps. Extend to the whole argument interval by
the Lipschitz bound |sin'|,|cos'|<=1. Every finite integral is enclosed by
summing whole-u-cell interval images times width, using 1024 closed cells.
The x cover consists of 80 closed cells of width 1/2, with shared
endpoints retained. No adaptive subdivision or root-isolation pass is used.

The certificate `scripts/polya-census/census-579.json` saves all x-cell
F,G derivative enclosures, W,W', normalization, tails, cover checks,
backend and caps. A strict same-sign F,G enclosure excludes an interior
parameter event by L814; it does not exclude W zeros. A strict nonzero
W enclosure is a different event exclusion. Every remaining cell is
unresolved, including possible multiple/common zeros. An interval
containing zero is never interpreted as a zero certificate. There are
no certified event boxes, parameters or orientations in this attempt.
The included edge40 and any undecided region are retained in the cover.
The code and certificate require independent audit before reliance.
No global sign, absence of events on unresolved cells, all-real reference
assertion, or RH consequence is established.

<!-- BEGIN STEP581 AUDIT -->
### Step581 audit: an actual inward-rounded power endpoint

On 5 November 2026 the independent audit reached its prescribed arithmetic
stop. This section supersedes reliance on the implementation description
above as a validated inclusion argument. It neither refutes the analytic
tail inequalities nor establishes an erroneous value of pi or an event.
The analytic bounds, trigonometric evaluator, normalization and whole-cell
exclusions have **not** passed the full independent audit.

The reproducible test is `python3 scripts/polya-census/audit-581.py`.
It executes only the preserved source prefix through the definitions,
then the two Machin arctangent series; it does not execute the census.
Its full certificate is `scripts/polya-census/audit-581.json`. Exit status1
is the intended report of a failed inclusion, not a successful audit.
The original seven input hashes match before this section was added;
subsequent replay reconstructs the exact prior L815 text by removing only
this marked section and checks the same hash. The original source and
census certificate are unchanged. Python3.15.2/libmpdec4.0.1 match the
recorded backend, and the recomputed pi endpoints equal the saved ones.

Here are the exact hypotheses of the arithmetic counterexample. In the
atan(239) evaluation, the interval for z=1/239 has upper endpoint

    b=0.0041841004184100418410041841004184100418410041841005.

The source's 50-digit ROUND_CEILING context returns for b^13

    h=1.2045568111401624418728752411145395224600280741411e-31.

An inclusion extension of the power on that closed input interval must
have upper endpoint at least b^13. In fact h<b^13. This is checked using
only exact integer arithmetic, not a higher-precision transcendental call.
Write

    m=41841004184100418410041841004184100418410041841005,
    a=12045568111401624418728752411145395224600280741411.

Then b=m/10^52, h=a/10^80, and exact multiplication gives

    b^13-h = (m^13-a*10^596)/10^676,
    2*10^591 < m^13-a*10^596 < 3*10^591.

The complete positive integer difference is saved at
`/failure_witnesses/0/exact_positive_difference_numerator` in the audit
certificate. It can also be reproduced directly from the two displayed
integers. The sharper outward rational enclosure of b^13-h is

    [2.0286541919254014186e-85, 2.0286541919254014187e-85].

Since the output unit is 10^-80, the least 50-digit decimal upper bound
is `1.2045568111401624418728752411145395224600280741412e-31`.
The returned bound is one representable step below that required ceiling;
its deficit relative to the exact power is about 0.000020287 units.

There are exactly242 interval-power calls, all on positive intervals with
odd exponents1,3,...,239,241. These arise from120 series terms and one
remainder for each q=5,239. The script checks both endpoints of every call
against `Fraction(Decimal(endpoint))**exponent`, using arbitrary-size
integer arithmetic. Of484 directed endpoint comparisons, only this upper
comparison fails (zero-based call127, exponent13 in the second series).
No general correctness guarantee for other integer powers is inferred.
The ambient Decimal operations used to make the x-grid are not reached
by this test and receive no audit conclusion here.

The logical consequence is failure of the claimed compositional interval
proof: b belongs to the supplied input interval, but its power is outside
the returned interval. Every claimed exclusion uses the resulting pi
interval in both kernels, their tail bounds and normalization, so none
of the thirteen exclusions is promoted to independently validated status.
The list of affected cells is recorded in full in the certificate: the
closed cells [k/2,(k+1)/2], k=0,...,12, covering [0,6.5]. The67 originally
unresolved cells on [6.5,40], including the shared endpoint and edge40,
remain unresolved. This is not an assertion that any excluded point is
an actual event or that these numerical bounds are false.

In particular, the same exact-rational check finds that (1/239)^13 itself
is still inside this returned power interval. The strict endpoint failure
therefore does not prove that this particular arctangent term, the final
pi interval, or the final transform intervals miss their true values.
Other rounding slack may suffice, but has not been certified here.
An independent aggregate enclosure of the Machin expression is a possible
repair to assess separately; no repair or replacement census is performed.

The source limitation was already assessed: [Python3.15 Context.power](https://docs.python.org/3.15/library/decimal.html#decimal.Context.power)
and [mpdecimal4.0.1 power](https://www.bytereef.org/mpdecimal/doc/libmpdec/arithmetic.html#power)
do not promise blanket correct rounding for this backend. The exact
counterexample specializes that known limitation to an actual saved call;
it is not a new arithmetic theorem or a claim that the backend violates
its documented contract. Exp's separate neighbor-expanded guarantee is
unaffected by this counterexample, but its entire use is not audited here.

### Step583: independent repair of the saved pi input only

This section repairs one premise of the numerical implementation. The
step581 counterexample above and the original source remain unchanged.
The present annotation is inside the same marked audit block so that
removing that block still reconstructs exactly the original census input.

The sole numerical conclusion here is that the real pi belongs to the
stored closed interval [p_minus,p_plus], whose exact finite decimals are

    p_minus=3.1415926535897932384626433832795028841971693993650,
    p_plus =3.1415926535897932384626433832795028841971693993843.

Import the principal-real Machin identity

    pi=16 arctan(1/5)-4 arctan(1/239)

from Chris H. Rycroft, Harvard AM205 Unit0, slide13 (PDF page13),
[Formula of John Machin](https://people.math.wisc.edu/~chr/am205/slides/am205_unit0.pdf),
undated author-hosted version inspected 5 November2026. This is an import
of the named identity, not a new derivation from a tangent equality.
Its real branch applies: with alpha=arctan(1/5), beta=arctan(1/239),
0<beta<alpha<1/5, so 0<4alpha-beta<4/5<pi/2. In particular the
angle is in the first quadrant and the identity has no modulo-pi ambiguity.
The elementary inequality arctan(t)<t for t>0 follows by integrating
1/(1+t^2)<1; only the elementary pi>2 is needed for this branch check.

For q=5,239 define the following exact rationals, without Decimal powers:

    S_q=sum_(k=0)^119 (-1)^k / ((2k+1)q^(2k+1)),
    r_q=1/(241 q^241),
    A=16 S_5-4 S_239, E=16 r_5+4 r_239,
    P_minus=A-E, P_plus=A+E.

[DLMF4.24.3](https://dlmf.nist.gov/4.24#E3), inspected 5 November2026,
identifies the arctangent series for these arguments, strictly inside
its disk of convergence. Its positive term magnitudes t_k satisfy
t_(k+1)/t_k=(2k+1)/((2k+3)q^2)<1 and
0<t_k<=q^(-2k-1), hence tend to zero. The alternating-series and
remainder theorems, OpenStax Calculus Volume2 Section5.5,
[Theorems5.13–5.14](https://openstax.org/books/calculus-volume-2/pages/5-5-alternating-series),
online version inspected the same day, therefore give
|arctan(1/q)-S_q|<=r_q. Indices0,...,119 are120 terms; the next
index120 has exponent241 and denominator241 and is positive. The
symmetric remainder is conservative and does not assume an incorrect
sign. Machin's coefficients and the triangle inequality now give
|pi-A|<=E, including the absolute coefficient4 for the subtracted series.
Consequently pi belongs to [P_minus,P_plus].

The specialization still needed beyond those standard inputs is the
finite arithmetic comparison with the saved endpoints. Run
`python3 scripts/polya-census/exact-machin-583.py`. It reads the original
artifacts but never imports or executes the census source. All terms,
sums, errors and comparisons use Python Fraction with integer arguments;
the two saved strings are parsed exactly as rational numbers. No binary
float, rounded display, limit_denominator or Decimal power enters a
load-bearing comparison. Exact rational construction and operations use
the [Python fractions contract](https://docs.python.org/3/library/fractions.html),
version3.15.2 inspected in the prior source assessment. The complete
certificate is `scripts/polya-census/exact-machin-583.json`.

For clarity, for a comparison a/b<=c/d, b,d>0, the certificate saves
both full cross-products ad,cb and their difference cb-ad. Both endpoint
differences are strictly positive. It also verifies the following rational
inequalities by exact integer arithmetic:

    1010*10^(-50) <= P_minus-p_minus <= 1011*10^(-50),
     919*10^(-50) <= p_plus-P_plus  <=  920*10^(-50),
       2*10^(-170)<= E             <=    3*10^(-170).

Thus the required threshold, both margins>=0, is met strictly, and
[P_minus,P_plus] is contained in [p_minus,p_plus]. The complete rational
values live under `/series`, `/aggregate` and `/margins`; the exact
cross-products and positive integer differences under `/comparisons`.
The latter differences and the full error rational were inspected without
truncation. The small bounds above are exact rational enclosures, not
floating previews. Every one of the ten recorded checks passes.

Provenance is part of this conclusion: the original census certificate
hash equals the step581 saved hash, its pi strings equal step581's replay,
and all seven original input hashes match, reconstructing historical L815
only by removing the marked audit annotation. AST comparison checks
the actual atan truncation/remainder and Machin expression against the
stated formulas without running the source. Full current/original hashes,
the prior audit and current script hashes are saved under `/provenance`.
The original census and step581 files were not changed or rerun.

This supplies only an independent enclosure of the initial pi constant.
Downstream expressions may use that interval once their own operations
are justified; the original interval-power operation is still not an
inclusion extension. This repair neither validates the remaining analytic
tail estimates nor their numerical evaluation, trig, normalization,
ambient grid arithmetic or whole-cell integration. All thirteen event
exclusions remain unverified; [6.5,40], common/multiple zeros, unbounded x,
signs and actual-Xi all-degree mixed positivity remain open. This is a
standard exact-arithmetic reproduction/specialization, not new theory.
Full matching Mathlib coverage for this saved-interval certificate is
unchecked; the source assessment is
`drafts/literature/2026-11-05-polya-census-exact-machin-repair.md`.
### Step584: remaining inclusion audit and bounded exclusion

This section completes the prescribed audit of the written evaluator and
its preserved recorded output, using step583's independently justified
pi interval. It supersedes the earlier *current* unaudited qualifications
for the tails, downstream arithmetic and thirteen exclusions. It does
not repair `I.__pow__` or alter the historical failure. No census or
integral was rerun, and no higher precision was requested. As for the
original computation, interpreting the recorded output as execution of
the saved source uses the stated Python3.15.2/libmpdec4.0.1 backend and
ordinary correct-execution assumption. Hashes establish preservation,
not an independent numerical replay or a formal proof of that backend.

**Audited hypotheses and conclusion.** Use the exact real kernels and
normalization in L814, the derivative orders j=0,1,2, and precisely the
source/certificate `scripts/polya-census/census-579.py` and `.json`.
With the repaired pi premise, the program's downstream expressions are
inclusion extensions for the full derivative integrals. On every closed
cell [k/2,(k+1)/2], k=0,...,12, the recorded lower endpoints give

    F(x)>0.1609, G(x)>0.0304, S(0)>0.064.

Thus H_tau(x)=(1-tau)G(x)+tau F(x)>0 on [0,6.5] for 0<=tau<=1.
In particular there is no interior-parameter event there, including a
common-zero or higher-multiplicity event. This says nothing about absence
of W zeros: W(0)=0 is compatible with the conclusion. All 67 remaining
cells covering [6.5,40] retain their unresolved classification; their
shared endpoint6.5 is covered by the preceding strict exclusion, while
no claim covers their remaining points or the edge40. No actual event,
orientation, unbounded-domain result, reference-zero theorem, or RH result
is obtained.

**Analytic tails and derivatives.** The displayed proof of E_n and E_u
above checks without modification. In particular positivity of every
theta summand follows from 2pi*n^2*exp(2u)>3; positivity of Q follows
from (2pi-3)cosh(5u/2)>0. Dropping their negative pieces therefore bounds
absolute values. For n>=5 the ratio is at most
(6/5)^4 exp(-11pi)<1/2; multiplying its geometric sum by length3 and
u^j<=9 gives exactly E_n. For the improper K tail, the n=2 term is
16 exp(-3v)<1/4 for v>=pi, since exp(9)>64 (already its first four
terms exceed64). The subsequent ratio is at most
(3/2)^4 exp(-5pi)<1/2, since exp(15)>16>2*(3/2)^4.
Hence the residual sum is <1/2 and the complete sum is <2.
The identical 16pi^2 exp(9u/2) exp(-pi exp(2u)) upper bound for Q
uses only its positive bracket and 2cosh(2u)>=exp(2u).

For each j=0,1,2, substitution y=exp(2u) produces exponent
b=5/4+j/2<=9/4. On y>=exp(6)>7, b/y<pi/2. Integrating the resulting
exponential majorant gives 16pi exp((5/2+j)*3)exp(-pi exp(6)), at most
the stated E_u. This checks the factors16pi,13.5 and both derivative
orders at the endpoint. L016/L020 and L814 give absolute convergence
and dominated differentiation. The actual derivative factors are
cos(xu), -u sin(xu), -u^2 cos(xu); each has modulus <=u^j for real x.
The finite theta omission [0,3], n>=5, and complete kernel tail u>=3
are disjoint up to an integration endpoint. F receives E_n+E_u and
S receives E_u, for every order and also when evaluated at x=0.

**Arithmetic after pi.** Reuse the inspected primary contracts:
[Python3.15 decimal arithmetic/exp/neighbors](https://docs.python.org/3.15/library/decimal.html)
and [mpdecimal4.0.1 correct rounding](https://www.bytereef.org/mpdecimal/doc/libmpdec/context.html#correct-rounding).
Basic addition, subtraction, multiplication and division have directed
rounding in the explicitly created FLOOR/CEILING contexts. Construction
from integers, strings and Decimal instances is exact. The source uses
`copy_negate`, so negation is exact and avoids the ambient-context unary
minus problem. The four endpoint products enclose interval products even
when either interval crosses zero; no independence of repeated factors
is required. For an interval avoiding zero, reciprocal reverses endpoint
order on either connected sign range. Every denominator actually used
here is a positive integer or the strictly positive S(0) interval.

For exp, the correctly rounded HALF_EVEN result lies between its adjacent
representable neighbors. Exp is increasing, so the lower neighbor at the
lower input and upper neighbor at the upper input enclose the full image.
The subsequent `sym` uses the upper endpoint of a nonnegative error bound.
All these operations are used literally in the reviewed code. `I.__pow__`
has no call after the two arctangent series: the other powers are exact
Python integer `(-1)**k` and `n**4`. Step583 therefore repairs the sole
affected initial constant without assuming that the invalid power routine
has become valid. No hidden power call remains in trig or the tails.

The finite-domain arguments of exp are between -50000 and14: pi<4,
exp(6)<3^6=729 and n<=4 give ample room for every kernel and tail
expression, including interval rounding. Thus their positive outputs
are far inside the default exponent range +/-999999. The trigonometric
polynomial intermediates start with modulus <100; eight double-angle
steps are bounded conservatively by M_(r+1)<=3 M_r^2, so remain below
10^700. Subsequent finite products and sums remain below10^1500.
There is no overflow premise concealed by finite stored endpoints.
Directed small-result rounding also preserves inclusion; no test treats
an underflowed nonzero number as an exact zero. The actual stored
intervals are all finite and ordered.

**Taylor enclosure and whole argument intervals.** On the saved grids
0<=x<=40, 0<=u<=3, hence t=x*u is in [0,120]. Its decimal endpoints
are exact dyadic numbers; their midpoint calculation is exact at50 digits
here. More generally the code's upward-rounded
r=max(mid-t.a,t.b-mid) covers every |t-mid| even with midpoint rounding.
Put z=mid/256, so |z|<=15/32<1. Starting from c=1,s=z, the sixteen
recurrences include precisely cosine terms through degree32 and sine
terms through degree33. Taylor's theorem with Lagrange remainder, using
the vanishing next coefficient, bounds the cosine remainder by
|z|^34/34! and the sine remainder by |z|^35/35!, both <=1/34!.
The directed rational evaluation of 1/34! and addition of its symmetric
upper enclosure therefore include cos(z),sin(z).

Each simultaneous assignment `s,c=2*s*c,c*c-s*s` uses the old s,c on
both right sides, and the exact double-angle identities propagate their
joint inclusion. Interval dependency only enlarges the boxes. After
eight iterations these enclose sin(mid),cos(mid). The final addition of
[-r,r] uses the global real Lipschitz bounds |sin'|,|cos'|<=1, not a
first-order approximation. Hence the returned intervals enclose both
functions on the entire argument interval, including its endpoints.

**Grids, integration and normalization.** The u partition is exactly
[3k/1024,3(k+1)/1024], k=0,...,1023, with common width3/1024. Every
vertex has a terminating decimal with fewer than50 significant digits.
The ambient operations Decimal(k)/2, k=0,...,80, likewise have exact
results with at most three significant digits in the default28-digit
context. The x cells are exactly [k/2,(k+1)/2], k=0,...,79. The checker
verifies every stored endpoint against those rationals; no rounded grid
gap is inferred away.

On each u cell, `kernel` encloses the finite sum n=1,...,4 of the exact
L019 summands and the exact L814 Q formula. Its cosh(v) is
(exp(v)+exp(-v))/2. Multiplication by the three derivative-factor
intervals encloses each derivative integrand for every u and x in the
two cells. Multiplying by width and summing therefore encloses the
finite integral: this is interval integration of whole cells, not a
midpoint rule with an unproved error. Shared closed u endpoints have
measure zero and do not cause double counting. The already justified
two tails complete the full integrals.

At I(0) this same evaluator, including the tails, supplies F(0),S(0).
The saved S(0) enclosure is

    [0.064033426596879363338506775742763346147894808135205,
     0.068515962970270224294697545027554674515089853293260].

It avoids zero strictly. Exact rational comparison verifies that the
saved c interval contains the complete quotient of the saved F(0),S(0)
intervals, and lies in (7,8). Multiplication of each S derivative by this
fixed enclosure of c thus encloses the corresponding G derivative;
correlation with other intervals cannot invalidate an enclosure. The W
and W' formulas agree with L814, including cancellation of the mixed
first-derivative terms in W'. Their stored intervals contain the exact
interval products/differences of the stored F,G data for all80 cells.

**Recorded evidence and limits.** Run
`python3 scripts/polya-census/audit-584.py`; its complete certificate is
`scripts/polya-census/audit-584.json`. It never imports or executes the
census. It reads all saved intervals and uses exact Fraction arithmetic
for comparisons, quotient, products, W/W', classifications, margins and
coverage. The seven original input hashes agree after removing only this
marked historical audit block. The saved output hash agrees independently
with steps579,581,583; prior audit and repair-script hashes also match.
All twenty checks pass. These checks complement, and do not replace,
the analytic and source-level inclusion proof above. In particular the
integrals and exponentials in the saved run were not numerically replayed.

The full thirteen-cell lower-endpoint table is in `/exclusions` and was
inspected in full. Both minima occur on [6,6.5], with exact lower endpoints

    F_lower=0.16091383271430643601224375425665116239345468993867,
    G_lower=0.030407878006221997128882890563925140976625408035995.

The required threshold is strict positivity, not small tails alone. The
full80-cell evidence includes all three orders, W,W', closed endpoints,
and unresolved flags. This validates the existing bounded exclusion by
known interval methods, not a new mathematical discovery. The fixed-cap
cancellation stop remains: no additional point of an unresolved cell is
settled by this audit. Common/multiple zeros outside the excluded region,
signed compensation, infinity, and all-degree mixed positivity remain
open. Full matching Mathlib coverage has not been checked.
<!-- END STEP581 AUDIT -->

## Mathlib

Full matching coverage is unchecked. L016's supporting convergence
references do not formalize these explicit constants, interval code, or
census. The interval inclusion methods are standard and assessed in
`drafts/literature/2026-11-05-polya-certified-event-census.md`:
Hickey–Ju–van Emden, JACM48(5) (2001), Section4.8 Theorems9–10,
[author manuscript](https://fab.cba.mit.edu/classes/S62.12/docs/Hickey_interval.pdf),
PDF pp10–11. Only direct interval inclusion and strict sign tests are
used here; no general numerical-method reproof is intended.
