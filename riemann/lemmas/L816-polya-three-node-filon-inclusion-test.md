# L816: bounded three-node Filon inclusion specialization

## Hypotheses

Use the precise K,F,Q,S,c,G of L814 and real-path tails of L815.
The finite kernels are K_4=sum_(n=1)^4 k_n and Q on [0,3], with

    k_n=(8pi^2 n^4 exp(9u/2)-12pi n^2 exp(5u/2)) exp(-pi n^2 exp(2u)).

Fix exactly 1024 closed u panels, each of halfwidth h=3/2048,
and the 67 closed x cells [k/2,(k+1)/2], k=13,...,79.
For j=0,1,2 interpolate each of the six finite real amplitudes
u^j K_4(u), u^j Q(u) at each panel's endpoints and midpoint.
All arithmetic enclosures below require correct execution of the written
source, directed basic Decimal operations, and correctly nearest-rounded
Decimal exp expanded by one adjacent representable value at each end.
These are the same backend contracts qualified in L815 step584; there
is no blanket correct-rounding assumption for Decimal power.

## Conclusion

The formulas below give finite full-cell inclusion enclosures for all
three x derivatives of F,S,G, and hence W=FG'-GF' and W'=FG''-GF''.
Every interpolation error and both L815 tails must be added. A strict
same-sign F,G interval or nonzero W interval is an L814 event exclusion;
containing zero proves neither a zero nor an event. This is a standard
quadrature specialization, not a new sign theorem. Actual numerical
output and its independent-audit status are qualified below.
Step588 completed the independent source and saved-data audit: the seven
recorded exclusions pass under the stated backend/correct-execution
hypotheses. This is validation of a known-method specialization, not an
independent numerical replay or a new general sign theorem.

## Proof

### Imported interpolation result and finite applicability

NIST [DLMF §3.3](https://dlmf.nist.gov/3.3), equations3.3.1–5 and
3.3.11–13, gives the real Lagrange remainder: for three distinct nodes
and a real C^3 function f on their closed hull, the quadratic interpolant
p obeys f(u)-p(u)=f'''(xi)(u-a)(u-m)(u-b)/6, with xi in that hull.
The equally spaced case is also stated in 3.3.16–18. Source statements
were inspected in the step585 assessment
`drafts/literature/2026-11-05-polya-oscillatory-quadrature-scope.md`.
The Filon construction (integrate the interpolant against the oscillator)
and the absolute interpolation-error integral are imported from
Gao–Iserles, *Error analysis of the extended Filon-type method for highly
oscillatory integrals*, Research in the Mathematical Sciences4,21 (2017),
Section1, Theorem1/(1.5)–(1.6),
[DOI10.1186/s40687-017-0110-4](https://link.springer.com/article/10.1186/s40687-017-0110-4).
No asymptotic constant from that paper is used as a finite error bound.
The six amplitudes are finite elementary entire expressions, so are real
C^3 on every closed panel. A bound at the midpoint alone would not suffice.

Write u=m+t, |t|<=h. Then

    p(m+t)=A+B t+C t^2,
    A=f(m), B=(f(b)-f(a))/(2h),
    C=(f(b)+f(a)-2f(m))/(2h^2).

The nodal product is t(t^2-h^2), whose modulus is at most h^3,
because |t|<=h and |t^2-h^2|<=h^2. If M bounds |f'''| throughout
the panel, |f-p|<=M h^3/6. Integrating against either real sine or
cosine over length2h therefore costs at most M h^4/3. This looser
explicit bound avoids a square-root constant. Sum it over all panels,
separately for every amplitude. There is no frequency differentiation
of a remainder: each j has its own interpolated amplitude u^j K_4 or Q.

### Whole-panel third derivatives

The implementation propagates enclosures of f^(r)/r!, r=0,...,3,
over a whole closed panel U, starting with the variable jet (U,1,0,0).
Addition is componentwise and the product coefficients are
(fg)_r=sum_(k=0)^r f_k g_(r-k), directly from Leibniz's rule.
For e=exp(f), the chain rule e'=f'e gives

    e_0=exp(f_0), e_r=(1/r) sum_(k=1)^r k f_k e_(r-k).

These identities hold pointwise at every u in U; applying inclusion
operations inductively encloses all actual derivatives, even though
the interval coefficients have dependencies. Evaluate the finite K_4,Q
and their u,u^2 multiples with these jets. Six times component3 encloses
the actual third derivative over U. M is the maximum absolute endpoint
of that interval, enlarged only by directed multiplication/division in
M h^4/3. This is an explicit applicability calculation, not new automatic
differentiation theory or a differentiation of a midpoint sample.

### Finite centered moments on full x cells

All x here are positive, so divisions by x and its repeated products
avoid zero. Put z=xh. The fundamental theorem of calculus and integration
by parts, evaluated at t=+-h, give exactly

    M0=integral_-h^h cos(xt) dt=2 sin(z)/x,
    M1=integral_-h^h t sin(xt) dt=2[sin(z)-z cos(z)]/x^2,
    M2=integral_-h^h t^2 cos(xt) dt
       =2[(z^2-2)sin(z)+2z cos(z)]/x^3.

For example an antiderivative for the last integrand is
t^2 sin(xt)/x+2t cos(xt)/x^2-2sin(xt)/x^3; differentiation cancels
the lower-degree terms. The first two formulas follow from sin(xt)/x
and -t cos(xt)/x+sin(xt)/x^2. Odd integrands have zero integral on
[-h,h]. With c_m=cos(xm), s_m=sin(xm), the interpolated cosine integral
is c_m(A M0+C M2)-s_m B M1. The sine integral is
s_m(A M0+C M2)+c_m B M1. Thus orders0,1,2 use respectively the
cosine integral, minus the sine integral, and minus the cosine integral
of their own u^j amplitudes, exactly as in L815.

Every x cell satisfies 0<xh<=120/2048<1<pi/2. Cosine decreases and
is positive on [0,1]. If L>0 is a lower bound for cos(xh) over the
whole x cell, then for all its x and |t|<=h,

    L<=cos(xt)<=1,
    2h L<=M0<=2h,
    0<=M1<=2 x_max h^3/3,
    2h^3 L/3<=M2<=2h^3/3.

For M1 use t sin(xt)>=0 and |sin(xt)|<=x|t|, followed by
integral_-h^h t^2 dt=2h^3/3. The sine inequality follows from the
fundamental theorem and |cos|<=1. Intersect these independently valid
bounds with the exact moment-formula intervals. Both contain each
moment for every x in the full cell; intersection preserves inclusion.
The script asserts the computed L>0 and z range, and never replaces
the x cell by its midpoint. This bounds a finite polynomial integral;
it imports no new improper tail or arbitrary high x derivative.

### Arithmetic, tails and reproducible evidence

Run `python3 scripts/polya-census/filon-586.py`. New integer powers are
repeated directed interval multiplications, including moment divisors
and h^4. Python integer products n*n*n*n are exact. Decimal grid
coordinates 3k/2048 and k/2 are exact terminating rationals of far fewer
than50 digits; the former are also checked exactly with Fraction.
All other operations on interval endpoints are explicitly in the
50-digit directed contexts. Division asserts that its divisor excludes
zero. The fixed saved pi is the independently justified interval of
L815 step583; the fixed saved c is L815 step584's positive enclosure
of the full quotient. Neither old census nor its invalid power code is
executed, and the script checks the saved-certificate hash and saved
pi agreement with the repair certificate. The prior audit qualifications,
including correct execution of saved original output, remain inputs.

The trig evaluator uses exactly the audited Taylor/double-angle inclusion
of L815 step584: reduced midpoint argument by256, |argument/256|<=1,
sixteen recurrence updates through degrees32/33, symmetric remainder
1/34!, eight simultaneous double-angle identities, then the full
argument interval radius by the global Lipschitz bound. New argument
ranges are recorded and the reduced bound is asserted on every call.
Here the unreduced arguments xm are in [0,120], and xh in [0,1].
The exp rule encloses each actual endpoint by monotonicity and the
stated correctly nearest-rounded contract. No additional libmpdec
power guarantee is used. Jet exp arguments for the decaying finite
terms stay within the Decimal exponent range; finite ordered output
is asserted at every interval construction.

Add the summed symmetric interpolation remainder to each directed
finite sum. Then add L815's E_n+E_u to F_j and E_u to S_j, j<=2.
Multiply the full S_j intervals by saved c to enclose G_j. Interval
products/differences then enclose W,W'. Correlation loss can widen the
results but cannot invalidate them. L814 proves the strict exclusion
tests including its exceptional/common-zero qualifications.

The full output `scripts/polya-census/filon-586.json` records all2049
node amplitudes, all1024 whole-panel third-derivative intervals and
integrated errors, coefficients, full-cell moments (raw, integral bounds
and intersection), every panel integral and finite sum, all67 complete
F,G derivatives/W/W' enclosures, provenance, thresholds and unresolved
cover. Rounding and input uncertainty are enclosed in each arithmetic
interval; no separate scalar rounding estimate or achieved tolerance is
claimed. Interpolation and omitted tails are explicitly separated from
those arithmetic-inclusive finite intervals. Comparison with census579
uses its actual corresponding unresolved cells and includes endpoint40.
The output is an implementation attempt, pending independent audit.
The ancillary `F0_width_ratio` field divides upward-rounded widths;
it is a diagnostic proxy, not a certified enclosure of the ratio of
exact widths. It is not used for an exclusion, margin or route threshold.

### Step586 recorded outcome (unaudited implementation)

At the declared caps the saved output proposes seven new whole-cell
exclusions: F>0.14439 and G>0.01447 on [6.5,7], followed by W<0 on
the six half-unit cells covering [7,10]. Their smallest distance of the
W upper endpoint from zero exceeds0.00012224, on [9.5,10]. The sixty
remaining cells cover [10,40] and remain unresolved, including edge40.
Shared endpoint10 is included in both the last proposed exclusion and
the unresolved cover; it is not silently dropped. Existing [0,6.5]
exclusions retain precisely L815 step584's qualifications. A same-sign
cell does not exclude W zeros; a nonzero W cell excludes common zeros
as well as nondegenerate events, since a common zero would force W=0.
No common-zero statement is made on the unresolved cover.

The accumulated interpolation upper errors, before normalization,
are less than (7.747e-8,3.420e-8,1.482e-8) for F orders0–2 and
(1.031e-8,4.801e-9,2.430e-9) for S orders0–2. The achieved strict
sign margins, rather than these small error budgets alone, are the
relevant exclusion thresholds. Actual trig arguments were in
[0.009521484375,119.94140625], within the justified reduced range.

Run `python3 scripts/polya-census/check-filon-586.py` for exact rational
saved-data consistency checks. These check every panel error against its
saved third-derivative enclosure, all finite sums against all saved panel
integrals, error additions, normalization, W/W', the two closed covers,
every classification, margins and saved hashes. They do not replay or
independently verify the jet propagation, exp/trig computations or
moment implementation. Full checks and failures are saved in
`scripts/polya-census/check-filon-586.json`. This limited consistency
check complements the written inclusion argument; it is not the later
independent audit required before relying on the seven exclusions.
The result passes the provisional one-new-cell threshold and warrants
that audit; it supplies no event orientation or global sign.

### Step588: independent inclusion audit of the preserved run

The scope is exactly the 1024 panels and 67 closed x cells in the
hypotheses. The source `scripts/polya-census/filon-586.py` was reviewed in
full without executing it. The original source and output, the prior
limited checker/output, and the saved input certificates remain intact.
The following verifies their inclusion argument, conditional on correct
execution of that source with its recorded Python3.15.2/libmpdec4.0.1
contracts. Neither a hash nor the checks below prove correct execution
or independently validate the transcendental backend.

**Whole panels and amplitudes.** The source's variable is precisely
J([U,1,0,0]) for each full closed panel U. At any fixed u in U its entries
enclose u,1,0,0, the scaled derivatives of the identity. The convolution
in J.__mul__ uses all r+1 summands for every r<=3. The exp loop uses only
already computed entries e_(r-k), k=1,...,r, with the exact factor k/r.
Thus induction in the expression tree and in r applies the stated Leibniz
and chain-rule identities at every point of U. It does not differentiate
an interval endpoint or a point sample. The implementation's I.__mul__
returns NotImplemented for a jet operand, so mixed scalar/jet products
dispatch to J and do not silently discard derivative entries.

The two summands for each n are exactly the displayed k_n, including
the negative 12pi term and exponent9u/2 versus5u/2. The Q expression
uses cosh(v)=(exp(v)+exp(-v))/2, the coefficients8pi,2pi,-3 and the
decay exp(-2pi cosh(2u)), as in L814. The family array contains K_4,uK_4,
u^2 K_4 and Q,uQ,u^2 Q in that order. Multiplication by6 encloses the
unscaled third derivative. Taking the maximum modulus of its endpoints
therefore supplies a bound throughout the panel for each of the six
amplitudes. All input uncertainty in pi is carried through those
expressions; correlations can widen the result but do not weaken
inclusion. No infinite theta derivative is inserted into these finite
jets: the omitted theta terms are handled by L815's separate tails.

The three exact grid nodes are a=m-h,m,b=m+h, h=3/2048. The implemented
A,B,C match the quadratic interpolant, with denominators2h and2h^2.
The DLMF real C^3 hypotheses hold for these finite elementary amplitudes
on their entire closed panel. The earlier nodal-product calculation
then gives the conservative integrated bound M h^4/3, independently of
x. The code computes h^4 by four directed products, divides by3, sums
each family's nonnegative errors, and adds its symmetric upper bound.
There is no unsupported differentiation of the quadrature error. Exact
saved-data checks verify all6144 coefficient triples from the actual
node values, all6144 integrated errors from the saved third-derivative
intervals, and all six accumulated error bounds.

**Centered moments and frequency coverage.** Differentiating each of
the three displayed antiderivatives gives its asserted integrand; at
the two endpoints the resulting M0,M1,M2 have exactly the signs and
factors in `moments`. Each cell has x>=6.5 and xh<=120/2048<1, so every
moment denominator is positive. Repeated interval products of x may
lose dependence, but still enclose x^2,x^3 and their reciprocals.
The saved cosine lower endpoint L is positive in all67 cells. Since
cosine is even and decreasing on [0,1], cos(xt)>=cos(xh)>=L for
|t|<=h. Also t sin(xt)>=0 and |sin(xt)|<=x|t| there. Consequently all
three integral bounds used in the intersection hold uniformly in the
whole cell. Exact checks verify all201 raw formula inclusions, all201
crude bound inclusions, and all201 intersections of the actual saved
intervals. Empty intersection would fail, not certify a moment.

Expanding cos(x(m+t)) and sin(x(m+t)), and removing the odd integrands,
gives respectively c_m(A M0+C M2)-s_m B M1 and
s_m(A M0+C M2)+c_m B M1. The source uses the negative of the latter
for j=1, and the negative of the former for j=2. Thus it encloses
F,S and both of their x derivatives, with the correct amplitudes and
signs. The trig arguments are the full intervals x*m and x*h, never
their x midpoints. The checker
reconstructs every one of the67*(1024+1) argument intervals from the
exact grids. Their exact minimum and maximum are0.009521484375 and
119.94140625, agreeing with the saved range; division by256 stays
strictly inside [-1,1].

**Outward operations and input contracts.** Basic endpoint operations
are explicitly in the50-digit FLOOR/CEILING contexts. Integer/string
construction, copy_negate and copy_abs are exact. All four endpoint
products are retained; every divisor excludes zero. There is no Decimal
power call or Python power syntax in the evaluator. Its helper `power`
is repeated directed multiplication; n*n*n*n is exact integer arithmetic.
The only ambient Decimal arithmetic is the half-integer x grid, exact
at the default precision. The u nodes and halfwidth are exact dyadic
rationals, verified individually by the saved-data checker.

Exp uses nearest-rounded endpoint values enlarged by adjacent neighbors;
monotonicity then gives interval inclusion under the stated exp contract.
Its scalar arguments lie within the same conservative (-50000,14) range
justified in L815, including the whole-panel value entries of the jets.
For example pi<4, n<=4 and exp(6)<729 bound the magnitude of the decaying
theta exponent by46656. Derivative entries in the finite order3 jet
recurrence introduce only finite products and sums; no new exponential
of a derivative coefficient is taken. There is no exponent-range change
hidden by the jet construction.

The trig routine is the audited L815 recurrence: terms through32 and33,
a symmetric1/34! remainder, then eight simultaneous double-angle steps.
Taylor's theorem bounds both initial errors when |mid/256|<=1. At each
step both right-hand sides use the old sine and cosine intervals. The
last radius max(mid-a,b-mid), rounded upward, covers the entire argument
interval even if midpoint rounding occurred. The global Lipschitz bound
then completes the inclusion. It is neither a first-order truncation
nor a modulus-square substitution.

The saved pi and c match the previously qualified L815 step583/584
inputs, and the original input hashes match. The exact saved c contains
the full F(0)/S(0) interval quotient with S(0)>0; this audit does not
renormalize from a truncated integral. The new n/u tail intervals
agree exactly with the audited old ones. The code adds E_n+E_u to all
F orders and E_u to all S orders before multiplying by c. Exact
saved-data checks include every panel-integral endpoint in all402
finite sums, every interpolation/tail addition and all201 normalized
derivative intervals. W,W' contain the complete endpoint products and
differences for all67 cells. These tests complement the source proof;
they do not regenerate node exponentials, jets, trig values or panel
integrals and make no claim to numerical replay.

**Complete recorded evidence and conclusion.** Run
`python3 scripts/polya-census/audit-588.py`. All30 check groups pass;
the complete comparisons, counts, hashes, seven exclusions, all67
derivative/W/W' records and sixty-cell unresolved cover are saved in
`scripts/polya-census/audit-588.json`. The original14-check result is
bound to the unchanged original output, and the new checker independently
checks its load-bearing arithmetic relations, adding coefficients,
moments, input matching and the complete argument grid. It reads all
2049 nodes,1024 panels and67*1024 panel-integral records; previews and
selected sampled panels are not used as verification. The previously
reported interpolation caps all hold, but strict signs are the actual
exclusion threshold.

On [6.5,7] the exact saved lower endpoints are

    F_lower=0.14439189288062777507924337702946788895041881874277,
    G_lower=0.014479881886909814735119280498630695410655959722322.

On each of the six closed cells covering [7,10], W<0. The least
negative upper endpoint occurs on [9.5,10] and equals

    -0.00012224063956741186242395835696398956965531846512345.

Thus the seven exclusions survive this independent audit under its
explicit execution hypotheses. The first cell has no zero of H_tau
for 0<=tau<=1. The other six have no interior-parameter double-zero
event: if F=G=0 then W=0; if D!=0 a double zero implies W=0 by L814.
This includes degenerate double-zero events, without assuming W'!=0.
It does not assert that H_tau has no simple zeros on those six cells.
The W sign of the first cell need not be used for its classification.

The sixty remaining closed cells are exactly [k/2,(k+1)/2], k=20,...,79,
whose union is [10,40]. Shared endpoint10 also belongs to the final
excluded cell; it is therefore already excluded, although the first
unresolved cell is retained whole. No other resolution is inferred
there, and edge40 remains included and unresolved. No event parameter,
event orientation, all-real reference assertion, unbounded-x conclusion
or degree-uniform positivity follows. This is local validation of the
known-method finite certificate, not progress beyond the general source
theorems or a resolution of RH. L814's independent relative signed
estimate and the global gaps remain open.

## Mathlib

Full matching coverage of this quadrature specialization, backend or
certificate is unchecked. Named elementary calculus/interpolation inputs
are cited above; no formal verification or novelty claim is made.
