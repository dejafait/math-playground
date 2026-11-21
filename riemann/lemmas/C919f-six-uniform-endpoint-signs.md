# Corollary 919f: six uniform real endpoint signs

## Hypotheses

Use L019's exact positive kernel K and L058's actual normalization

    F(lambda,x)=integral_0^infinity exp(lambda*u^2) K(u) cos(x*u) du,
    0<=lambda<=1/20.

For the finite arithmetic certificate assume correct CPython integer
and Fraction arithmetic and libmpdec directed basic operations,
representable neighbors, and correctly rounded HALF_EVEN exp, under
the reviewed Python Decimal contract. The recorded actual runtime is
CPython3.15.2, libmpdec4.0.1, with80 decimal digits. This is an explicit
backend trust assumption, not a formal verification of that backend.
There is no RH, initial zero bracket, simplicity, zero census, or
propagation premise. C919c/C919d/C919e motivate the target but are not
mathematical inputs to these integral signs.

## Conclusion

The fixed step2167 certificate encloses F uniformly on the entire
closed time band as follows. All displayed decimal endpoints denote
exact rationals rounded outward from the full saved enclosures.

| x | uniform enclosing interval |
|---|---|
| 14 | [1.1403e-4,2.0130e-4] |
| 29/2 | [-4.6765e-4,-4.0682e-4] |
| 41/2 | [-1.350e-5,-1.149e-5] |
| 43/2 | [5.817e-6,6.656e-6] |
| 49/2 | [7.648e-7,8.530e-7] |
| 51/2 | [-5.113e-7,-4.556e-7] |

Thus each of the three specified pairs has strictly opposite signs
for every lambda, including both time endpoints. The smallest signed
margin in the full certificate is greater than4.55e-7; the required
threshold is strictly greater than zero. Continuity in x (L058) and
the intermediate value theorem place at least one real zero in each
of the three disjoint open intervals for every lambda. This is an
existence conclusion at each time, not a labeled branch, exact count,
or simplicity assertion.

This is a source-covered calculation classified REPRODUCTION, not a
new general theorem beyond the checked sources. The separate step2169
conceptual audit accepts it under the stated backend assumptions. It
does not assemble H2, address higher degrees/global coverage, or
constitute a candidate complete solution of RH. Actual use with
C919c/C919d would retain their separate arithmetic qualifications.

## Proof

### Imported theorems and the one fixed computation

Import composite Simpson's theorem for a real C4 integrand, positive
even panel count M, length b-a and h=(b-a)/M, with absolute error

    (b-a)*h^4*sup|g''''|/180.

The precise source is NIST DLMF3.5(ii),(3.5.6)-(3.5.8), citing Davis
and Rabinowitz (1984), pp57-58: https://dlmf.nist.gov/3.5.ii.
Import Taylor's theorem with Lagrange remainder from G. Strang and
E. Herman, *Calculus Volume2* (OpenStax,2016), Section6.3,
Theorem6.7 and its proof:
https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series.
Only its safe smooth real-interval case is used. L058 supplies time
smoothness and integral derivative formulas; the finite integrands
below are C-infinity. These general theorems are not reproved.

Run from the notebook:

    python3 scripts/h2-head/six_endpoint_2167.py

The single run uses U=4, N=4, M=2^18 equal Simpson subintervals,
exactly1024 closed equal spatial bound cells, degree8 at a=1/40,
and exactly128 closed equal time range cells. No setting was tuned.
Full certificates are
`scripts/h2-head/six_endpoint_preflight_2167.json` and
`scripts/h2-head/six_endpoint_2167.json`. Their hashes, constants,
all54 coefficient enclosures, all derivative/error bounds, all768
endpoint/time-cell inclusions and all failures are retained. The
preflight was saved before the262145-node integration pass. The
initial reasoning is preserved in
`drafts/calculations/2026-11-21-six-endpoint-work-2167.md`.

The specialized bounds below are necessary because neither cited
general theorem supplies this kernel, its constants, or any signs.

### Two complete tails

For an integer0<=p<=18 and0<=lambda<=1/20, first consider omitted
indices n>=5 on0<=u<=4. L019 gives positive summands, each bounded by

    8*pi^2*n^4*exp(9u/2-pi*n^2*exp(2u)).

Use pi>3, pi^2<10, exp(2u)>=1+2u and lambda*u^2<=u/5.
After multiplication by u^p exp(lambda*u^2), its upper bound is

    80*n^4*exp(-3*n^2)*u^p*exp(-145u),

because6*n^2-47/10>=150-47/10>145. Write n=5+m. Then
n^4<=625(m+1)^4, n^2>=25+10m, and exp(-30)<1/2. L058's
geometric fourth-moment identity, evaluated at1/2, gives

    sum_(m>=0)(m+1)^4/2^m=300,
    sum_(n>=5)n^4 exp(-3n^2)<=187500 exp(-75).

Tonelli applies to these nonnegative majorants. Integrating the
majorant to infinity, rather than only4, proves

    B_index(p)=15000000*exp(-75)*p!/145^(p+1).             (1)

Here integral_0^infinity u^p exp(-145u)du=p!/145^(p+1), the
nonnegative-integer elementary gamma integral (or p integrations by
parts with vanishing exponential boundary terms). This supplies an
absolute error for the omitted signed cosine integral.

For the complete spatial tail, L058 gives

    K(u)<=C exp(9u/2-pi*exp(2u)),
    C=8*pi^2*(1+11q+11q^2+q^3)/(1-q)^5, q=exp(-pi).

The positive exponential series through degree8 proves exp(3)>20.
Consequently q<1/20 and the positive series defining this prefactor
is increasing in q. The exact rational comparison

    80*(1+11/20+11/400+1/8000)/(19/20)^5 < 200

proves C<200. For u>=4, log(u)<=u gives u^p<=exp(pu), and

    lambda*u^2+(p+9/2)u <= u^2/20+(45/2)u <= 2u^3
                         <= (3/2) exp(2u).

The middle comparison follows on dividing by u: the function
2u^2-u/20-45/2 is positive at4 and increasing for u>=4.
The last comparison uses the cubic term of exp(2u). Since pi>3,
the complete weighted tail integrand is at most
200 exp(-(3/2)exp(2u)). Convexity gives
exp(2u)>=exp(8)(1+2(u-4))>256(1+2(u-4)), since exp(1)>2.
Integration therefore yields the common absolute bound

    B_space=(200/768)*exp(-384) < 4.432e-168.             (2)

This includes every theta index on u>=4. It is not a compact-only
estimate. Bounds(1),(2) hold for every required coefficient and for
the complete ninth time derivative; all inequality endpoints are
included. No cancellation is assumed in either tail.

### Complete fourth-derivative bounds

Put alpha_n=pi*n^2. The finite kernel at time a=1/40 is the sum,
for n=1,...,4, of the following two exponential terms:

    8*alpha_n^2 exp(a*u^2+(9/2)u-alpha_n exp(2u)),
    -12*alpha_n exp(a*u^2+(5/2)u-alpha_n exp(2u)).

On a spatial cell[l,r], let v_lo<=alpha_n exp(2l) and
v_hi>=alpha_n exp(2r) be the outward bounds saved by the program.
For phi=a*u^2+b*u-alpha_n exp(2u), with b=9/2 or5/2, set

    A1=2a*r+b+2v_hi, A2=2a+4v_hi,
    A3=8v_hi, A4=16v_hi.

These bound the absolute values of phi',...,phi'''' throughout the
cell. The absolute exponential derivatives are bounded by
exp(a*r^2+b*r-v_lo) times, respectively,

    1,
    A1,
    A1^2+A2,
    A1^3+3A1*A2+A3,
    A1^4+6A1^2*A2+3A2^2+4A1*A3+A4.                      (3)

These formulas follow by four finite differentiations of exp(phi).
All coefficients are nonnegative, so replacing each derivative by
its magnitude upper bound is valid. Multiply by8*alpha_n^2 or
12*alpha_n, respectively, and add both magnitude bounds over n.
Denote the resulting five numbers by E_0,...,E_4 for this cell.
They are saved for all1024 cells, not evaluated only at sample points.

For j=0,...,8 put P_j(u)=u^(2j)/j!. Its t-th derivative on the
cell has absolute bound

    P_j,t=(2j)!*r^(2j-t)/((2j-t)!*j!) if t<=2j, else0.

Leibniz gives D_j,t=sum_(s=0)^t binom(t,s)P_j,s E_(t-s).
For x one of the six positive endpoints, the t-th spatial derivative
of cos(xu) has magnitude at most x^t. Thus a valid cell bound for
the fourth derivative of the full coefficient integrand is

    sum_(t=0)^4 binom(4,t) D_j,t x^(4-t).                (4)

The maximum over all cells gives M_j,x. Formula(4), with every
operation rounded upward, is exactly the recorded computation.
This proves a full-interval C4 bound, including adjoining endpoints.
Simpson now supplies

    E_S,j,x=4^5*M_j,x/(180*M^4).                         (5)

The maximum recorded M_0,x is less than8906864, and its Simpson
error is less than1.073e-14. The other53 bounds and their maximizer
cells are retained in the preflight; no old coefficient errors transfer.

### Complete time remainder and coefficient intervals

The exact time coefficients are

    A_j(x)=(1/j!)*integral_0^infinity
                      u^(2j) exp(a*u^2)K(u)cos(xu)du.

The quadrature program encloses their finite[0,4], n<=4 integrals
in Q_j,x, including all arithmetic, constants and trigonometric
uncertainty. It enlarges each Q_j,x symmetrically by

    E_j,x=E_S,j,x+B_index(2j)/j!+B_space/j!.              (6)

Although K's summands are positive, the cosine integral is signed;
both tails and the Simpson error are therefore charged on both sides.
No sign follows from kernel positivity alone.

For the ninth time derivative, L058's differentiation formula and
|cos(xu)|<=1 give the uniform majorant integral
integral_0^infinity u^18 exp(u^2/20)K(u)du. On each of the same
1024 cells, use the E_0 construction above at time1/20 and bound
the compact contribution by (r-l)*r^18*E_0. Add(1) at p=18 and
(2). The saved upward bounds are

    compact < 3.371428476e-6,
    omitted indices < 2.210e-51,
    spatial < 4.432e-168,
    complete derivative M9 < 3.38e-6.

The complete numerical bound, before shortening for display, gives

    R9=M9*(1/40)^9/9! < 3.55e-26.                       (7)

Taylor's theorem on the closed time band consequently gives

    F(lambda,x)=sum_(j=0)^8 A_j(x)*(lambda-a)^j+R,
    |R|<=R9.

All54 time coefficients and both of their tails are enclosed; the
ninth derivative bound is not obtained from the truncated kernel
alone. At every endpoint, the maximum sum of the analytic errors
sum_j E_j,x*(1/40)^j+R9 is less than1.08e-14. Polynomial range
width from a time cell is retained separately, rather than hidden
in that analytic-error number.

### Arithmetic and trigonometric enclosure

The Decimal basic-operation and exp contract is
https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp,
with the context, rounding, neighbors and signals sections assessed
in comparison2166 and arithmetic coverage2066/2067. Lower operations
use ROUND_FLOOR, upper operations ROUND_CEILING, both at precision80.
For exp on[A,B], use the lower neighbor of nearest exp(A) and upper
neighbor of nearest exp(B). Correct HALF_EVEN rounding plus monotonicity
justifies this enclosure; no directed-exp behavior is assumed.
All exceptional signals except Inexact and Rounded are trapped.
Emin=-999999 and Emax=999999; neither subnormals nor clamping occurred.

Pi is enclosed using Machin's identity with80 exact rational atan
terms at1/5 and25 at1/239, with the next alternating term as remainder.
To verify the branch of the identity, tangent addition gives
tan(2atan(1/5))=5/12 and tan(4atan(1/5))=120/119. Subtracting
atan(1/239) gives tangent1. The angle is positive by
4*(1/5-(1/5)^3/3)>1/239, and is less than pi/2 because
2atan(1/5)=atan(5/12)<atan(1). Thus the angle is pi/4.
The alternating bounds follow by integrating the finite geometric
identity for1/(1+t^2), or the usual arctangent remainder theorem.
The exact rational pi bounds verify3<pi<22/7 and pi^2<10; directed
division encloses those rationals in Decimal. This finite constant
certification is needed for this evaluator, not a new expansion theorem.

No built-in Decimal cosine is used. For each endpoint x, the mesh
angle d=x*h is positive and less than0.001. The degree31 sine and
cosine Taylor polynomials each have remainder at most d^32/32!,
since the relevant real derivatives have magnitude at most1.
The zero odd coefficients of cosine are included in this degree31
statement. All polynomial operations are enclosed, and both errors
are added outward. Starting from the exact pair(1,0), interval
addition formulas propagate cos(i*d),sin(i*d) for i=0,...,M.
Induction proves every pair contains the exact trigonometric values.
The dependency widening of these rotations is retained, not discarded.
No range reduction or uncharged trigonometric routine is used.

Each node u_i=i/65536 is exactly represented: multiplying the exact
dyadic decimal mesh by the integer i has fewer than80 significant
digits. At every node the finite kernel is evaluated as

    sum_(n=1)^4 4v_n(2v_n-3)
                      *exp(a*u_i^2+u_i/2-v_n),
    v_n=pi*n^2*exp(2u_i).

All v_n>3/2; the program checks positive lower bounds of the
polynomial factors before using positive interval multiplication.
Multiplying successively by u_i^2/(j+1) generates the nine weights
u_i^(2j)/j! with their outward arithmetic errors. Multiplication by
the enclosed cosine, exact Simpson weights1,4,2,...,4,1, summation,
and factor4/(3M) give Q_j,x. Its actual saved interval width is the
arithmetic/constants/trigonometric error; it is not a requested
tolerance. Signed interval multiplication uses all necessary endpoint
products. Thus every rounding/cancellation error is included.

### Closed time cells, full records and limits

For k=0,...,127 use the exact closed interval

    [k/2560,(k+1)/2560].

The union is[0,1/20]. Shared boundaries and both outer endpoints
belong to the tested ranges. Subtract a, range the polynomial by
outward interval Horner using all nine coefficient intervals from(6),
then add[-R9,R9]. Interval inclusion, by induction through Horner,
contains every value throughout each cell, not only its endpoints.
All768 resulting intervals exclude zero, with constant endpoint
sign pattern(+,-,-,+,+,-). All384 pair/cell sign products are-1.
Taking the hull over the128 cells yields the displayed six enclosures.
The intermediate value theorem then gives the stated existence result.

The actual run completed262145 nodes and1572864 enclosed rotations,
with2662422 exp endpoint calls, in about95 seconds. Runtime and
all sticky flags were inspected completely: only Inexact and Rounded
were set; the failure list is empty. Both complete tail vectors,
the54 derivative/Simpson bounds and all trigonometric step/final
records were inspected, not accepted from an unlabeled preview.

The additional full-record inspection is saved as
`scripts/h2-head/six_endpoint_inspection_2167.json`. It consumed all
1024 spatial records,54 coefficient records and768 time values.
Its2124 checks include exact Fraction coverage checks, both artifact
hashes, every coefficient's enlarged error inclusion, and independent
exact rational Horner inclusions from the saved decimal endpoints,
with every time remainder, pair sign and uniform margin checked.
All pass. It also checks finite positive spatial records; it does
not independently recompute their exponential bounds or replay the
node pass. Those bounds are justified by(3)-(4) and the stated
backend contract. This is internal certificate inspection, not the
separate critical conceptual audit or a formal Lean proof.

No premise or conclusion concerns all zeros being real, a zero count,
or the signed complement of a selected head. A future H2 assembly
would still need the paid separate actual-family inputs and their
arithmetic qualifications. Higher-degree/global mixed positivity
remains open. The previous step206/2157/2161 stops are preserved in
their original scopes; this direct signed-integral result does not
retroactively validate those methods.

### Independent conceptual audit, 21 November 2026 (step2169)

The approved SPECIALIZE assessment was
`drafts/literature/2026-11-21-six-endpoint-conceptual-audit-2168.md`.
This audit is REPRODUCTION: first independent acceptance of these
existing numerical signs, not a new theorem beyond the checked methods.
The full proof above and all380 evaluator lines were reviewed; L019/L058
were read in full. The already inspected Simpson, smooth-real Taylor,
Decimal/Fraction and elementary-function source coverage was reused.
No parameter, endpoint, zero bracket or normalization was changed.

**Analytic hypotheses.** L019's summand is exactly
4v(2v-3)exp(u/2-v), so the node integrand and the two exponential
terms used for differentiation agree. L058 supplies joint entirety
and dominated time differentiation, without requiring any real-zero
premise. On the finite spatial interval all integrands are C4, the
panel count262144 is positive and even, and Simpson's factor is
4^5/(180*262144^4). The time coefficients include1/j!, whereas the
ninth derivative does not; its remainder has the separate factor
(1/40)^9/9!. Taylor's center and radius cover both time endpoints.

For the index tail, the exponent after the stated comparisons is
-3n^2-(6n^2-47/10)u. For n>=5 its decay rate is at least145.3,
so145 is conservative. The n=5+m comparison and the geometric
fourth moment300 give exactly15000000 in(1). The spatial tail is
over the complete kernel, including n<=4: for p<=18 and u>=4,
2u^2-u/20-45/2 is positive and increasing, and the cubic term of
exp(2u) gives2u^3<=(3/2)exp(2u). Convexity with exp(8)>256
then gives precisely200 exp(-384)/768. Thus the compact omitted
indices and the full spatial tail cover disjoint omitted regions;
neither is a finite-index substitute for the other. Both are charged
in every coefficient and in the ninth derivative. Positivity is used
only for absolute majorants, never for the signed cosine integral.

The four exponent derivatives and the order0 through4 Bell
polynomials in(3) were checked by differentiation. The power
derivatives and both Leibniz applications in(4) have the stated
binomial coefficients and factorials. Bounds use the complete closed
cell, not values at isolated points. The ninth compact contribution
uses the time1/20 absolute envelope and r^18 on every spatial cell.
This verifies the hypotheses for the two imported error theorems.

**Arithmetic logic.** Reviewed every basic-operation sign case.
For multiplication by a nonnegative interval, a negative lower
endpoint requires the positive factor's upper endpoint, and a positive
upper endpoint likewise requires that upper endpoint. The remaining
signed case takes all four products. Denominators are strictly positive;
negation uses exact copy_negate. Every bound involving a nonnegative
sum/product/power is rounded upward. Node locations, mesh widths,
time cells and the center are exactly representable finite decimals;
the integer-times-mesh product is below80 significant digits. No
binary float enters a mathematical quantity. Time and runtime logging
use floating point only for nonmathematical elapsed seconds.

For exp, the two adjacent representable neighbors enclose a correctly
rounded HALF_EVEN value, and monotonicity transports the two argument
endpoints. This uses the stated contract, not an assumption that exp
respects FLOOR/CEILING itself. All contexts trap every exceptional
signal other than Inexact/Rounded. The recorded and replayed flags
exclude underflow, subnormal, overflow, invalid operation and clamping.

The exact alternating Machin fractions and their outward Decimal
conversion were independently reconstructed. To make its branch
explicit, theta=atan(1/5)<pi/4 implies2theta<pi/2; its tangent5/12
therefore gives2theta=atan(5/12)<pi/4. Hence4theta<pi/2.
The positive lower bound for4theta-atan(1/239), together with
its tangent1, identifies pi/4 without an ambiguous tangent branch.
The sine/cosine Taylor polynomials at each exact positive mesh angle
were reconstructed with rational arithmetic, including their common
order32 remainder. The original recurrence uses the old cosine and
sine together for each rotation, applies valid signed interval
operations, and retains all interval widening. Induction from(1,0)
therefore encloses every node's trigonometric pair. The moment
recurrence divides by j+1 after multiplying by u^2 and retains
the Simpson weights, giving exactly u^(2j)/j! times that weight.

**Independent reconstruction and replay.** The missing original
inspection source was not inferred from its PASS report. A new
rerunnable checker was written:

    python3 scripts/h2-head/audit_six_endpoint_2169.py

Its complete evidence is
`scripts/h2-head/six_endpoint_audit_2169.json`. It reconstructs all1024
spatial envelopes using a separate110-digit directed implementation
and Bell recurrence B_(m+1)=sum_(k=0)^m binom(m,k)B_(m-k)A_(k+1).
Every reconstructed bound lies below its saved80-digit upper bound.
The higher precision is an audit comparison, not a change to the
certificate or an independent validation of libmpdec's exp algorithm.
All54 maxima are also reconstructed from the saved spatial envelopes
by exact Fraction arithmetic, checking the maximizer cells and
Simpson factors. The complete ninth cell sum, both full tails and
the time-remainder factor pass the independent comparisons.

All54 enlarged coefficient intervals include both signed error sides.
Exact rational Horner reconstruction verifies all768 time-value
inclusions on the128 exact closed cells, all384 opposite-pair signs,
the six hulls and every displayed outward rounding. The minimum margin
is the saved exact rational with decimal value
4.55680908917662446661072168710651273548...e-7, strictly above
4.55e-7 and the required threshold0. The nine error terms and the
time remainder remain charged in those inclusions. The checker reads
all2124 original internal-check records but does not use their pass
flags as a replacement for this reconstruction.

The original source/artifact correspondence for the actual quadrature
and accumulated rotations was additionally tested by the full node
replay:

    python3 scripts/h2-head/replay_six_endpoint_2169.py

This wrapper changes only the two output destinations, recorded exactly
in `scripts/h2-head/audit2169-replay/provenance.json`; the original
source and all original certificates are preserved. The executed-source
hash and original-source hash are distinguished. Full replay artifacts
are in that subdirectory. Every mathematical record matches exactly,
including all54 quadratures, all trigonometric steps/final intervals,
all spatial bounds and all closed time cells. Only elapsed seconds
and the preflight digest that incorporates elapsed seconds differ;
the replay's own digest is independently checked. Both source and
original certificate digests also match the saved records.

The new checker completes6690 checks with no failures. The replay
completes262145 nodes and1572864 rotations. Both original and replay
report CPython3.15.2/libmpdec4.0.1 with80-digit evaluator contexts;
the independent reconstruction reports110-digit contexts. Complete
context/trap/flag records are saved and checked. Backend correctness
is still an explicit trust assumption; this is neither a formal Lean
proof nor an external attestation of the runtime.

**Conclusion and scope.** The audit accepts exactly the six uniform
signs and their IVT consequence, for every time in[0,1/20]. The
three open boxes are disjoint, so they give distinct real zeros at
each fixed time. There is no labeling across time, simplicity premise,
or exact zero count. A later head application must still handle its
remaining head and signed exterior and retain the separate inputs'
qualifications. No H2 assembly is performed here. The step206/2157/2161
failures remain unchanged. All-degree/global positivity and RH remain
open. The mathematical dependencies remain exactly L019 and L058.

## Mathlib

Full matching coverage of these six uniform signs and their numerical
certificate has not been checked. The precise sources above supply
the real Simpson and Taylor theorems; no matching Mathlib theorem
for this specialization is asserted. Unknown coverage is not evidence
of absence. Internal rational/interval checks are not formal verification.
