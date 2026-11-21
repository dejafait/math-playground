# Lemma 922: shared-parameter H2 enclosure and a fixed-budget stop

## Hypotheses

Use L019's exact positive kernel K, L058's entire family
F(lambda,z)=integral_0^infinity exp(lambda u^2)K(u)cos(zu)du,
and L874's local-logarithm convention

    log(F(lambda,z)/M0(lambda))=-sum_(n>=1) S_n(lambda)z^(2n)/n,
    Mk(lambda)=integral_0^infinity u^k exp(lambda u^2)K(u)du,
    H2=(S_(i+j+2))_(0<=i,j<=2).

Assume precisely L037's directed Decimal arithmetic and widened
correctly-rounded exponential contracts, with 100 digits in each
of the three contexts. Reject zero-containing divisors, invalid
operations, overflow, underflow and subnormals. Decimal-library
correctness is assumed; no independently verified library is supplied.
No real-zero, contact, PSD or RH hypothesis is used.

The closed parameter panel is [0,1/5120]. Set c=r=1/10240 and
x=(lambda-c)/r in [-1,1]. Fix parameter degree two, 64 equal spatial
panels on [0,2], four theta terms, and L036 spatial remainder order
eight. No refinement of any budget is part of this result.

## Conclusion

Conditionally on those arithmetic contracts, the full determinant
on every point of this closed panel is enclosed by the saved interval
in `scripts/heat/h2-shared-taylor-213.json`, strictly inside

    -4.482e-31 < det H2(lambda) < 1.073e-30.

The saved degree-two final polynomial has interval coefficients;
its combined parameter/composition remainder has magnitude <4.893e-37.
Its constant coefficient interval already contains zero. Thus the
complete enclosure does not decide the sign, even after retaining a
common parameter through normalization, finite logarithm and determinant.
In particular, the required strict positive determinant lower endpoint
was not attained. This is an informative failure of this implementation,
not a negative actual determinant, a contact, or failure of positivity.

All even full moments through order eighteen at c and 1/5120 are enclosed.
The common nonnegative discarded theta/spatial contribution is <4.345e-20
for these moments on the containing band [0,1/20]. The new mass model
has lower endpoint >0.49712, so its reciprocal is legitimate.
The first two minor ranges also remain positive; their positivity was
already available from audited L917. A strict positive third minor
would exclude d=2 PSD contacts here, but it remains unproved.

This is a known-method specialization and a conditional local
computational enclosure. The independent step215 conceptual audit below
accepts its analytic and implemented inclusions under the stated
arithmetic contracts. It makes no claim of mathematical novelty,
all-degree positivity, global continuation or RH.

## Proof

### Known method and actual-family specialization

The imported general inclusion method is K. Makino and M. Berz,
*Taylor Models and Other Validated Functional Inclusion Methods*,
IJPAM 4(4) (2003), publisher version printed pp379-452,
[primary PDF](https://www.ijpam.eu/contents/2003-4-4/2/2.pdf):
Definitions1-3 pp383-386; Theorem2 and proof pp389-391;
Theorem3 and proof p398; Section6 pp415-416.
The prior assessment is
`drafts/literature/2026-11-09-h2-shared-taylor-panel-review.md`.
Those results justify polynomial-plus-remainder inclusion under
admissible arithmetic and defined composition; they guarantee no sign
or error threshold for this problem. The following effective tails,
coefficient construction and operation checks justify the specialization
to the actual moments and this Python implementation. They do not
reprove the general theory or invoke a COSY implementation theorem.

### Complete tails through eighteen

For k=0,2,...,18, u^k<=exp(18u) on u>=0: use u^k<=1 on [0,1],
and k log u<=18u on [1,infinity). Put X=exp(2u), beta=119/40.
As in L917, exp(2u)>=2u^2 and 0<=lambda<=1/20 imply
lambda u^2<=X/40<=n^2 X/40. Dropping the negative part of L019's
positive summand and using 3<pi<4 gives

    K_n(u)<=128 n^4 exp(9u/2)exp(-pi n^2 X).

For integer n>=1, n^4<=16^(n-1) and n^2>=1+3(n-1).
Since 16exp(-9)<1/2 and X>=1,
sum n^4 exp(-pi n^2 X)<=2exp(-pi X).
Thus every full tilted moment integrand here is bounded by

    256 exp(45u/2) exp(-beta X).

Under du=dX/(2X) the resulting power is X^(41/4)<=X^11.
Since exp(4)>50, a uniform spatial tail after u=2 is

    E_space=128 exp(-50beta)
       *sum_(j=0)^11 [11!/(11-j)!]50^(11-j)/beta^(j+1).

This is eleven integrations by parts for the enlarged integral
over X>=50. To cover omitted theta terms n>=5 over all u>=0,
the termwise tilt inequality instead gives

    64 sum_(n>=5) n^4 integral_1^infinity X^11 exp(-beta n^2 X)dX.

For X>=1, exp(-beta n^2 X)<=exp(1-beta n^2)exp(-X).
Enlarge the remaining gamma integral to [0,infinity), where it is 11!.
Writing n=5+j gives n^4<=625*16^j and n^2>=25+11j.
The ratio 16exp(-11beta)<1/2 therefore proves the valid bound

    E_theta=128*625*11!*exp(1-25beta).

Add E_space+E_theta; overlap between these positive discarded regions
only increases the bound. This is a new effective order-eighteen
specialization; L917's constants through twelve were not reused as
order-eighteen constants. The producer encloses the sum below 4.345e-20;
the spatial part is below 5.679e-45. Every numerical premise is checked
by exact positive exponential-series witnesses: sum_(j=0)^7 4^j/j!>50,
sum_(j=0)^4 9^j/j!>32, and 11beta>9. The latter two give both ratios.

The checker independently encloses the two negative exponentials by
exact rationals. For t>=0, P=sum_(j=0)^1000 t^j/j! and
E=(t^1001/1001!)/(1-t/1002) give P<=exp(t)<=P+E when t<1002.
Both t=50beta and t=25beta-1 satisfy this condition. Reciprocation
gives [1/(P+E),1/P] for exp(-t). The complete rational tail values
are saved and lie in the producer's intervals, including their sum.

### Full center coefficients and parameter remainders

At each of the two fixed parameters c and b=1/5120, integrate every
even moment from zero through eighteen. For spatial panel j=0,...,63,
center u_j=(2j+1)/64 and half-width h=1/64, form the normalized
spatial jets through order eight of

    u^k exp(lambda u^2)sum_(n=1)^4
      exp(u/2)(8v_n^2-12v_n)exp(-v_n),
    v_n=pi n^2 exp(2u).

L036's product/exponential recurrences apply. The power jet has
coefficient binom(k,l)u^(k-l) when l<=k and zero otherwise;
retaining all l<=8 suffices even for k=18. The exponent lambda u^2
has normalized coefficients lambda u^2, 2lambda u, lambda, then zero.
The base kernel/jet routines and pi enclosure are those inspected in
L037/L917. The new loop first multiplies kernel and tilt, then u^k;
this changes the finite expression grouping but not the integrand.

For midpoint coefficients f_l, the integral polynomial is
2 sum_(l=0,2,4,6) f_l h^(l+1)/(l+1). The whole spatial-panel jet
supplies B>=sup |f^(8)|/8!, and L036 adds [-2Bh^9/9,2Bh^9/9].
Sum all 64 panels and add [0,E_space+E_theta]. Every midpoint jet,
whole-panel eighth coefficient, polynomial integral, local error,
summed error and full moment is stored. L037 inclusion proves these
are enclosures, including the endpoints and all omitted positive mass.

By L058, M_k^(j)(lambda)=M_(k+2j)(lambda). These are positive and
increasing on the real axis. Taylor's theorem at c therefore yields,
for k=0,2,...,12 and all x in [-1,1],

    M_k(c+rx) = sum_(j=0)^2 [r^j M_(k+2j)(c)/j!]x^j + R_k(x),
    |R_k(x)| <= r^3 M_(k+6)(b)/6.

The seven model coefficients enclose these *full* moments, including
the tails, coefficient quadrature errors, pi and arithmetic errors.
The right-endpoint full moments cover every third derivative on the
closed panel, with order eighteen necessary at k=12. No truncated-core
coefficient is substituted for the full-family Taylor coefficient.

### Verified finite composition

Every represented function is p(x)+R(x), with degree<=2 and each exact
polynomial coefficient lying in its recorded interval. Its pointwise
remainder lies in the recorded interval J. The code uses

    P(c0,c1,c2)=c0+c1[-1,1]+c2[0,1]

as a polynomial range enclosure. Addition and negation are coefficient
operations plus the corresponding remainder operations. For a product,
first convolve all coefficients through degree four. Keep degrees<=2;
add degree3 coefficient times [-1,1] and degree4 coefficient times [0,1]
to the remainder, as well as P(p)J_q+P(q)J_p+J_p J_q.
This is the assessed multiplication inclusion rule. Coefficients have
interval uncertainty, but x remains one shared variable throughout.
Whole-panel moment boxes are not substituted before composition.

For the mass inverse, let f=a0+v, where a0 is its true constant
coefficient, enclosed by the recorded a0 interval; v has zero constant
coefficient and the mass's unchanged remainder. Both a0 and the full
mass range are strictly positive. Use the exact identity

    1/f=1/a0-v/a0^2+v^2/a0^3-v^3/(a0^3 f).

No infinite geometric-series convergence assumption is needed. The
model v^2 includes all discarded terms and all remainder interactions.
Take the first three terms' degree<=2 coefficients and full remainder,
then add -range(v)^3/(a0^3 range(f)). Directed interval products enclose
the cube even on a sign-changing range. All denominator ranges exclude
zero. This produces the saved inverse model; interval coefficient
dependence can enlarge it, but never invalidate inclusion. The mass
range exceeds 0.49712 at its lower endpoint.

L917 already proves the finite-log identities; no new logarithm theorem
is required. Form q_n=(-1)^n M_(2n)/((2n)! M0), then

    S_n=-n q_n-sum_(k=1)^(n-1) S_k q_(n-k), 1<=n<=6.

All operations use shared models and include discarded parameter terms.
This is coefficient extraction from the local z-logarithm germ, not a
global or real logarithm of F(lambda,z). With A=S2,B=S3,C=S4,D=S5,E=S6,
form AC-B^2 and A(CE-D^2)-B(BE-DC)+C(BD-C^2) by those same operations.
Only then range the final polynomial and add its full remainder.
Thus the saved determinant is an enclosure on the entire panel.

### Complete evidence, replay and limitations

Reproduction commands from this notebook:

```text
python3 scripts/heat/h2-shared-taylor-213.py
python3 scripts/heat/h2-shared-taylor-check-213.py
```

The producer saves all 20 full moment intervals and errors, all 1,280
spatial/moment records, all 99 model-expression nodes with parent
references, all seven seeds, normalization/log/minor model references,
arithmetic contexts and input hashes. The certificate is
`scripts/heat/h2-shared-taylor-213.json`.
Its full final endpoints were inspected, not inferred from a preview:
they are approximately -4.48140385758002e-31 and 1.07223875480168e-30,
strictly within the conclusion's outward bounds. The final remainder
is contained in [-4.893e-37,4.893e-37]. The constant coefficient is
enclosed approximately between -4.47939391651103e-31 and
1.07203775147054e-30 and already straddles zero. This identifies a
coefficient-uncertainty obstruction in the stored representation even
before ranging the nonconstant terms; it does not prove that any
specific alternative integration method would decide the sign.

The separate checker saves
`scripts/heat/h2-shared-taylor-check-213.json`. It independently uses
Fraction endpoint arithmetic for the new tail bounds, all seven seed
coefficient/remainder constructions and every one of the 99 model nodes.
It checks full moment and reciprocal denominators, all discarded terms,
all error interactions, the finite-log recurrence and determinant
assembly against the saved models. Every exact inclusion passes.
It also reconstructs all 1,280 spatial/moment records and all 20 summed
moment/error intervals in a separate integration loop with moments
outermost; all are exactly equal to the producer's records. This
reuses the inspected Decimal/jet primitives, rather than independently
implementing that library. The exact-rational expression replay is
independent of the producer's model class. It verifies the complete
outward thresholds and the zero-containing constant coefficient.
All exceptional arithmetic flags are false and required traps active.

A preliminary producer version used Python's ambient-context unary
Decimal minus in two symmetric error-bound constructors. That can
round an endpoint inward. Its code/certificate are preserved as
`scripts/heat/h2-shared-taylor-213-first-pass.py` and the corresponding
JSON, and are **not** valid enclosure evidence. The corrected producer
uses exact copy_negate for both endpoints, was rerun at the identical
budget, and is the only input to the passing replay. The checker's first
execution hit Python's integer-string limit while serializing its exact
tail fractions, before checking quadrature or writing a result; a local
serialization limit increase permits the complete evidence. Neither
repair refines the mathematical budget or conceals a sign failure.

The failed strict-sign threshold ends this fixed representation test.
No extra panel, degree, precision, cutoff, theta count, head census or
flux test was run. This conditional enclosure and explicit local stop
are progress in assessing a strategy, not progress beyond the imported
general Taylor-model method and not a resolution of H2 positivity.
The later independent audit below accepts this conditional enclosure.
Other parameters/degrees, actual flux signs, initialization, equality,
global continuation and L030-L032/C032a remain unresolved.

### Independent conceptual audit, 9 November 2026 (step215)

The audit accepts the stated enclosure and fixed-budget stop. It uses
the prior SPECIALIZE scope
`drafts/literature/2026-11-09-l922-shared-taylor-conceptual-audit.md`,
reusing the precise Makino-Berz citation above and L037's arithmetic
contract. No sign theorem, refined budget or additional assumption about
zeros is introduced. The clarification to "even full moments" in the
conclusion makes the computed orders explicit; no bound needed repair.

**Analytic tails and differentiation.** Positivity is termwise:
K_n=4v_n(2v_n-3)exp(u/2-v_n)>0, since v_n>=pi>3. Thus dropping
the negative part and double-counting omitted regions both give upper
bounds of the required sign. For the spatial tail,
n^4<=16^(n-1) follows from ((n+1)/n)^4<=16, and
n^2-1>=3(n-1). Hence its geometric ratio is at most 16exp(-9)<1/2.
Multiplying the resulting 256 exp(9u/2-pi X) by the moment and tilt
bounds gives 256 exp(45u/2-beta X). Substitution contributes the factor
1/(2X), so the power is exactly 41/4, below 11 for X>=1. Enlarging the
lower limit exp(4) to 50 and integrating X^11 eleven times gives the
displayed spatial expression, with the final constant term included.

For the theta tail, retain the n-dependent bound
lambda u^2<=n^2 X/40 before replacing pi by 3. The transformed coefficient
is 64 n^4, not 128 n^4; the extra factor 2 arises only when summing the
geometric majorant. For n=5+j, j^2>=j proves n^2>=25+11j and
(5+j)^4<=625*16^j. The inequality
exp(-beta n^2 X)<=exp(1-beta n^2)exp(-X) follows from
(beta n^2-1)(X-1)>=0. The enlarged gamma integral equals 11!.
These justify the same tail for all ten even orders at both parameters
and indeed for their discarded mass throughout [0,1/20].
The positive exponential-series witnesses and both complete rational
tail intervals were verified anew by the replay. They establish the
quoted 5.679e-45 spatial and 4.345e-20 total thresholds.

L058's compact domination applies to all finite moment derivatives
here, including M_12'''=M_18. Since K>0 and u>=0, each such moment
is positive and increasing in the real parameter. Taylor's theorem
between c and c+rx therefore uses the right endpoint b on either side
of c, including both endpoints; the factor is |rx|^3/3!<=r^3/6.
There is no unbounded-order differentiation or exchanged infinite
Taylor series. The seeds enclose full moments, not just finite cores.

**Spatial integration and arithmetic.** The inspected base routine
forms exactly four theta summands, normalized jets through 8, and
binom(k,j)u^(k-j) for each power jet. Truncating these jets at 8 loses
no coefficient used in L036, even when k=18. The tilt jet has the
three exponent coefficients stated above. All 64 domains cover [0,2]
with their endpoints. The whole-domain eighth coefficient bounds the
Taylor remainder for the same integrand used at the midpoint.
Its upper error endpoint is negated with exact copy_negate, as is the
parameter-error endpoint. All other signs in the producer are applied
to interval objects or exact integers/Fractions. Basic endpoint
operations use the explicit DOWN/UP contexts; endpoint exponentials
use NEAR and its adjacent neighbors. No ambient-context negation
enters the corrected enclosure. The inherited preliminary arithmetic
self-checks are not substitutes for these inclusion arguments or for
the exact series witnesses.

**Shared models and nonlinear composition.** Interpret each node as
one polynomial with fixed exact coefficients selected inside the
coefficient intervals, plus a function taking values in its remainder
interval. Induction preserves this interpretation uniformly in the
same x. Independent endpoint arithmetic may forget correlations among
coefficients but still encloses those fixed choices. For multiplication,
the exact degree 3 and degree 4 terms are covered by [-1,1] and [0,1],
respectively. The remaining error is precisely p R_q+q R_p+R_p R_q;
each of these three terms is present. No coefficient uncertainty is
dropped or replaced by an exact midpoint.

For inversion, choose a0 as the fixed true constant coefficient of the
mass seed. Its interval and the full mass interval are positive.
The remove_constant node has exactly zero constant coefficient, so
the absence of a -v_0/a0^2 term in the implementation is justified.
Its v^2 node includes both high-degree terms and all errors. Multiplying
the displayed reciprocal identity by a0^3 f proves it for f!=0,
without a smallness assumption. The implementation includes
-R_v/a0^2+R_(v^2)/a0^3 and the complete geometric residual separately.
Repeated interval multiplication of a sign-changing range can widen
the cube but still contains every actual cube. The rational replay
checks the widened divisor and geometric intermediate before they are
used, so their rounding is not hidden in a fused expression.

L917's finite-log recurrence has the required factorial normalization
and minus signs. The replay verifies its evaluation through S6 from
the seven actual moment seeds, and verifies the three-by-three
cofactor determinant with all six off-diagonal occurrences. L874 is
used for conventions only, not its conditional contact hypothesis.
The first two minor intervals are positive; the third contains zero.
Thus Sylvester's criterion gives no positive-definiteness conclusion.

**Complete replay and exact output checks.** Run from this notebook:

```text
python3 scripts/heat/h2-shared-taylor-audit-215.py
```

The driver verifies the producer and earlier replay input hashes,
then executes the entire inspected checker into the new artifact
`scripts/heat/h2-shared-taylor-audit-replay-215.json`.
Every rational tail, seed and operation inclusion and every one of the
1,280 spatial records and 20 moment/error sums is recomputed. The whole
fresh replay equals the earlier replay, including its full exact
fractions, not just its summary. The shared Decimal/jet primitives
remain the explicitly assumed library layer; this is not a second
implementation of that library.

`scripts/heat/h2-shared-taylor-audit-215.json` records 41 passing checks
and no validity failure: complete provenance, unchanged fixed budget,
array/seed coverage, all summary-to-model inclusions, both positive
minor lower endpoints, exact outward determinant/tail/remainder/mass
thresholds, and fresh arithmetic contexts with all required traps
active and exceptional flags false. It verifies that the historical
producer, replay and invalid first-pass code/data remain unchanged.
The full determinant endpoints, inverse model and final polynomial
coefficients were also inspected as exact saved values. The conclusion
is consequently a valid conditional enclosure, while its strict-sign
test still fails. The zero-containing constant interval is an
obstruction to this stored representation's certificate, not evidence
for an actual zero or a negative determinant. No new sign attempt was
made. This is local validation of a known-method specialization, not
progress beyond the checked sources toward an all-degree sign theorem.

## Mathlib

Full matching theorem and supporting specialized coverage have not
been checked. Availability is unknown, not asserted absent. The finite
Decimal program and its certificate are not formalized in Lean.
L036/L037 retain their analytic inclusion and library qualifications;
Sylvester's criterion supplies only the conditional interpretation of
a strict third sign. Reference: https://leanprover-community.github.io/mathlib4_docs/.
