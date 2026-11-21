# Corollary 919n: a uniform origin margin and root-qualified local decrease

## Hypotheses

Use the actual kernel K of L019 and the normalization in L058. For every
real x in the closed interval[14,29/2], define the half-line function

    G_x(u)=x integral_u^infinity K(t)sin(x(t-u))dt, u>=0.

The quantitative certificate assumes correct CPython integer/Fraction
arithmetic and libmpdec directed basic operations, representable neighbors,
and correctly rounded HALF_EVEN exp. This is the same explicit backend
contract retained in accepted C919f, not an independent verification of
the backend. The actual run reports CPython3.15.2/libmpdec4.0.1, precision80.
For the last, root-qualified conclusion additionally assume 14<x<29/2
and Xi(x)=0, using audited C919m. No simplicity, first-zero or census
assumption is made. Use the Simpson and real Taylor theorems cited below.

## Conclusion

Under these arithmetic qualifications, uniformly for every x in[14,29/2],

    G_x(0)-K(0)>1/5.                                          (1)

For every actual root x in the open bracket, the smooth even residual
kernel of C919m consequently satisfies

    G_x'(0)=0,   G_x''(0)<-x^2/5.

There exists epsilon_x>0 such that G_x'(u)<0 for 0<u<epsilon_x.
Thus zero is a strict local maximum of its even extension. No numerical
value or uniform lower bound for epsilon_x is asserted. There is no
conclusion of decrease on the whole half-line, another factor removal,
iteration, all-degree mixed positivity or RH. This quantitative local
specialization is accepted by the separate critical audit2233 below,
subject to the stated arithmetic contracts.

## Proof

### Existing tools and complete tails

Import composite Simpson's theorem for C4 real functions with positive
even panel count M, error at most U^5 sup|f''''|/(180 M^4), from NIST
DLMF3.5(ii),(3.5.6)-(3.5.8), Davis--Rabinowitz(1984),pp57-58:
https://dlmf.nist.gov/3.5.ii . Import real Taylor's theorem with Lagrange
remainder from Strang--Herman, *Calculus Volume2*, Section6.3,Theorem6.7:
https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series .
These exact tools and their hypotheses were already assessed in2230
and2166. Their general proofs are not repeated. Every finite integrand
used below is smooth. L019/L058 supply all required weighted integrability
and differentiated integral formulas, without a root premise.

Write alpha_n=pi*n^2. The actual theta summand is

    K_n(t)=4v_n(2v_n-3)exp(t/2-v_n), v_n=alpha_n exp(2t).

C919f equations(1),(2), at lambda=0 and integer0<=p<=9, bound the
omitted indices n>=5 on[0,4] and the complete spatial tail t>=4 by

    B_I(p)=15000000 exp(-75) p!/145^(p+1),
    B_T=(200/768) exp(-384),                                  (2)

respectively, for integrals of t^p K(t) in absolute value. These are
inside C919f's proved p<=18,0<=lambda<=1/20 domain. Since every sine
and cosine derivative factor here has absolute value at most1, (2)
also bounds the signed coefficient tails. The two omitted regions
are disjoint and their union covers everything outside the finite
rectangle. The spatial bound uses all theta indices.

For K(0), the pre-integration comparison in C919f's index-tail proof
gives, using positivity, pi>3 and pi^2<10,

    0<sum_(n>=5) K_n(0)
      <=80 sum_(n>=5)n^4 exp(-3n^2)
      <=15000000 exp(-75).                                  (3)

In particular an integral tail cannot be substituted for this pointwise
tail. Equation(3) retains the larger, nonintegrated bound.

### One fixed finite calculation

The preserved prerecord is
`drafts/calculations/2026-11-21-origin-margin-work-2231.md`.
The single fixed evaluator is

    python3 scripts/real-zero-origin/origin_margin_2231.py

It uses U=4,N=4,M=65536 Simpson panels,1024 equal closed spatial
derivative-bound cells, Taylor degree8 at c=57/4 with radius r=1/4,
and32 equal closed x cells covering[14,29/2]. Settings were not tuned.
Full evidence is `scripts/real-zero-origin/origin_margin_2231.json`
and `scripts/real-zero-origin/origin_margin_preflight_2231.json`.
The preflight, including every derivative and tail bound, was saved
before the node pass. This is a direct certificate for the present
signed sine integral, not reuse of C919f's cosine signs.

Set S(x)=integral_0^infinity K(t)sin(xt)dt. Differentiation under
the integral is justified by t^j K(t) integrability. Therefore

    A_j=S^(j)(c)/j!
       =(1/j!) integral_0^infinity t^j K(t)sin(ct+j*pi/2)dt,
    S(x)=sum_(j=0)^8 A_j(x-c)^j+R(x),
    |R(x)|<=r^9 M9/9!, M9=integral_0^infinity t^9 K(t)dt.     (4)

For a spatial cell[l,b], enclose v_n(t) between v_lo and v_hi.
The two exponential terms of K_n are
8 alpha_n^2 exp((9/2)t-v_n(t)) and
-12 alpha_n exp((5/2)t-v_n(t)). For either a=9/2 or5/2, put

    E0=|prefactor| exp(a*b-v_lo),
    H1=a+2v_hi, H2=4v_hi, H3=8v_hi, H4=16v_hi.

Absolute derivatives of that exponential term through order4 are
bounded by E0 times

    1; H1; H1^2+H2; H1^3+3H1 H2+H3;
    H1^4+6H1^2 H2+3H2^2+4H1 H3+H4.

This follows by differentiating exp(a*t-v_n(t)) four times and taking
absolute values; the bounds use the whole closed cell. Sum both terms
and n=1,...,4 to obtain E_k. For P_j(t)=t^j/j!, its s-th derivative
has absolute upper bound P_js=b^(j-s)/(j-s)! if s<=j, and0 otherwise.
Two finite Leibniz rules bound the coefficient integrand's fourth
derivative by

    D_jt=sum_(s=0)^t binom(t,s) P_js E_(t-s),
    B_j4=sum_(t=0)^4 binom(4,t) D_jt c^(4-t).                (5)

The maximum over all1024 closed cells is used in Simpson's theorem.
It is not an estimate from samples. The program evaluates all9 signed
coefficient quadratures Q_j and enlarges each by the symmetric error

    E_j=4^5 max(B_j4)/(180 M^4)+(B_I(j)+B_T)/j!.             (6)

The complete ninth moment is bounded on each spatial cell by
(b-l)b^9 E_0, then by adding B_I(9)+B_T. The saved bounds give

    M9<0.000133370,     |R(x)|<1.403e-15.                    (7)

No infinite tail or signed lobe has been dropped.

### Arithmetic, parameter coverage and full evidence inspection

The evaluator copies C919f's reviewed directed interval operations,
Machin pi enclosure, exponential enclosure and trigonometric step
routine, without modifying that input. Decimal/Fraction contracts are
those recorded in C919f and assessment2166; exp's nearest-rounding
contract is https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp .
Exp on[A,B] is enclosed by the lower representable neighbor of the
HALF_EVEN exp(A) and upper neighbor of exp(B). Basic operations use
FLOOR/CEILING separately; exp is not assumed to obey directed rounding.
Machin's identity uses80 exact atan terms at1/5 and25 at1/239,
with the next alternating terms as errors. Its branch and inequalities
3<pi<22/7,pi^2<10 are exactly those justified in C919f.

The mesh step angle d=c*(4/M) is positive and below0.001. Degree31
real Taylor polynomials for sine and cosine, with absolute error
d^32/32!, enclose both step values. Interval addition formulas starting
at(cos0,sin0)=(1,0) then enclose all65537 node pairs by induction.
Their accumulated widths are retained. No builtin trigonometric routine
is used. Every dyadic node i/16384 is exactly represented; its equality
to the corresponding Fraction is checked. Node evaluation uses the
positive factor 4v_n(2v_n-3) and the outward exponential enclosure.
The moment recurrence multiplies by t/(j+1), so its successive values
are K(t)t^j/j!, with exact Simpson weights1,4,2,...,4,1. The phase
sequence is sin,cos,-sin,-cos, repeated. Thus both the signs and j!
normalization in(4) are retained in Q_j. All errors in(6) are charged
on both sides, independent of signs or cancellation.

For k=0,...,31, let X_k=[14+k/64,14+(k+1)/64]. Outward interval
Horner on X_k-c using all9 enlarged coefficients, followed by
[-r^9 M9/9!,r^9 M9/9!], encloses S(x) for every x in X_k.
Multiply this interval by the positive interval X_k, and subtract
the K(0) interval from finite node0 plus(3). This is an enclosure
for xS(x)-K(0); independence of interval factors only widens it.
The cells cover both outer endpoints and all shared boundaries.

The hull of all32 saved margins is contained in the exact rational
interval

    [0.2420677,0.2779602].                                  (8)

Its actual lower endpoint starts0.2420677330694019324790463167;
the full80-digit endpoints are saved. In particular(8) proves(1),
strictly above the required threshold0 and the convenient rational1/5.
K(0) is enclosed near1.78678760186849, with index-tail upper bound
4.018e-26. The complete ninth moment, both K(0) endpoints, full
trigonometric records and full runtime/flags were inspected exactly.

Internal evidence inspection is rerunnable as

    python3 scripts/real-zero-origin/inspect_origin_margin_2231.py

It consumes every one of the1024 spatial records,9 coefficient records
and32 parameter records. Exact Fraction reconstructions check all
fourth-derivative maxima from the saved E_k, Simpson factors, ninth
moment sums, coefficient error additions, closed parameter coverage,
all Horner inclusions and final products/subtractions. All3327 checks
pass with no failures; full records and hashes are in
`scripts/real-zero-origin/origin_margin_inspection_2231.json`.
This is internal inspection, not a separate critical audit, independent
exponential recomputation or independent node replay. Bounds E_k are
justified by(5) and the evaluator's directed arithmetic. The actual
65537-node/65536-rotation run sets only Inexact/Rounded flags; all
other exceptional signals are trapped. Backend correctness remains
an explicit assumption; no formal Lean proof is claimed.

### Specialization at actual roots and limitations

For an actual root in the open bracket, audited C919m supplies
G_x'(0)=0, smoothness, evenness and

    G_x''(0)=x^2(K(0)-G_x(0))<-x^2/5<0.

Continuity of G_x'' at zero provides epsilon_x>0 with G_x''(u)<0
on[0,epsilon_x). For 0<u<epsilon_x the fundamental theorem of
calculus gives G_x'(u)=integral_0^u G_x''(v)dv<0. Evenness then
gives a strict local maximum at zero. This argument uses the exact
root to eliminate the linear origin term; it asserts no such local
maximum for a nonroot. C919f guarantees at least one root in the
bracket, retaining its own arithmetic qualifications, without a
first-zero identification or simplicity assertion.

The source assessment found no inspected exact quantitative margin
theorem, so the new local quantitative input is POTENTIALLY_NEW only
in that limited reporting sense. No originality is certified. The
general quadrature/Taylor/ODE mathematics is imported or specialized.
Global-u cosine signs, repeated removal and the L030-L032/C032a
bridge remain unresolved. This is not a complete RH candidate. QED.

### Separate critical audit, 21 November 2026 (step2233)

Accepted the exact statement under assessment2231, separately approved
in2232. This completed audit is REPRODUCTION: independent acceptance
of the existing specialization, not an original mathematical discovery.
The whole evaluator2231 and its internal inspector were read. The
independent implementation imports neither program and preserves every
original artifact. Reproduction command and full evidence are

    python3 scripts/real-zero-origin/origin_margin_audit_2233.py
    scripts/real-zero-origin/origin_margin_audit_2233.json

The mathematical settings remain U=4,N=4,M=65536,1024 closed spatial
cells, degree8 at57/4, radius1/4 and32 closed parameter cells. Only
the independent arithmetic precision is100, as permitted by the approved
audit; the claimed80-digit certificate is not retuned or overwritten.
Both runs use CPython3.15.2/libmpdec4.0.1. Only Inexact/Rounded flags
occurred. All3228 independent checks pass, with an empty failure list.

**Complete omitted regions.** Reconstructed C919f's specialization:
for n>=5, the positive summand is at most
80n^4 exp(-3n^2)exp(-145t) on[0,4], since
6n^2-9/2>=145.5>145; the stronger lambda<=1/20 comparison in
C919f is also valid here. With n=5+m, its fourth-power series is
bounded by625 exp(-75)sum_(m>=0)(m+1)^4/2^m, whose sum is300.
Thus the pointwise K(0) upper error is15000000 exp(-75).
Integration against t^j gives precisely the extra factor j!/145^(j+1)
for each j=0,...,9. The pointwise error is not divided by145.

For t>=4 the all-index majorant has prefactor less than200.
Using j<=9 within C919f's proved j<=18 bound gives
t^j K(t)<=200 exp(-(3/2)exp(2t)). The comparisons
log(t)<=t, (1/20)t^2+(45/2)t<=2t^3 and
2t^3<=(3/2)exp(2t) are valid on this whole half-line; the first
quadratic comparison is positive and increasing after division by t.
Convexity and exp(8)>256 give the integrable envelope
200 exp(-384-768(t-4)). Its integral is exactly B_T in(2).
These are disjoint omitted regions, including all indices on the
spatial tail, with no missing corner or signed-lobe hypothesis.

**Derivative and remainder reconstruction.** Each exponential term
has exponent a*t-alpha_n exp(2t), whose derivatives are a-2v,
-4v,-8v,-16v. On a closed cell, |a-2v|<=a+2v_hi and
exp(a*t-v)<=exp(a*b-v_lo). The fourth complete Bell polynomial
has coefficients1,6,3,4,1 as displayed above. The independent code
builds the Bell polynomials by their binomial recurrence, uses generic
interval endpoint products, and recomputes the exponential enclosures
on every cell. Each of its five bounds is no larger than the original
saved upper bound. Its flattened double Leibniz sum reconstructs(5),
including the derivatives of t^j/j!, not t^j alone. Every original
fourth maximum and Simpson/index/spatial coefficient error dominates
the independent bound. Simpson's panel count is positive and even,
and its factor is4^5/(180*65536^4). The ninth moment uses the sum of
(b-l)b^9 E_0 on every closed cell, plus both complete tails. The
independent upper bounds are

    M9 < 0.000133369815344196,
    |R| < 1.402022e-15.

These rounded numbers are outward qualifications of the full saved
bounds, not new inputs. Taylor applies on the entire closed bracket,
and every coefficient integral is differentiated using L058's absolute
weighted domination. No boundary or ninth-order remainder is omitted.

**Independent node and range reconstruction.** Machin fractions were
resummed in reverse order using exact rational arithmetic; both exact
endpoints and their inclusion in the serialized pi interval were checked.
The independent code forms the degree31 trigonometric step polynomials
as exact rationals at d=57/65536 before conversion to intervals, using
the common d^32/32! remainder. It uses all four endpoint products for
signed multiplication, rather than the original positive-factor
optimization. The addition formulas propagate the enclosures through
all65536 rotations. Every dyadic node t=i/16384 is evaluated independently.
The kernel is evaluated as the difference of its two exponential terms,
rather than the original positive polynomial expression; this identity
is exactly L019's summand expansion. Successive t powers, explicit j!
division, phases sin,cos,-sin,-cos and weights1,4,2,...,4,1 independently
produce all nine Simpson sums. No original quadrature values are used
as mathematical inputs to these sums.

Each original finite quadrature interval contains the independent
interval; so do the finite/full K(0), enlarged coefficients and final
trigonometric records. The independent Horner calculation charges its
complete Taylor remainder and checks all32 original closed cells and
their outer endpoints. Each original margin interval contains its
independent counterpart. The independent uniform hull is contained in
[0.2420677,0.2779602], with lower endpoint beginning
0.2420677330694019324790463167669847596. Thus every error is paid
against the required rational1/5. Full endpoints, all spatial bounds,
coefficients, cells, checks and original/source hashes are saved in the
audit certificate. The original rational_claim JSON field advertises
only1/10; this conservative metadata discrepancy is preserved, and
is not the evidence for1/5. The independent32 lower-endpoint checks
establish the stronger canonical claim directly.

**Root qualification and acceptance.** C919m's exact identities give
G_x'(0)=-x^2 Xi(x) and G_x''(0)=x^2(K(0)-G_x(0)). Only the
first uses the root assumption. At an actual root (1) gives strictly
negative curvature, and continuity gives an interval with negative
second derivative. Integrating from the exact zero first derivative
gives strict decrease for positive u in that interval. Smooth even
extension then gives the stated strict local maximum. This argument
works with every possible root multiplicity and uses no first-root
identification. It supplies no effective or uniform epsilon_x.
The numerical margin itself is valid at nonroots too; local decrease
at zero is not asserted there. The original proof's direct inputs and
DAG row remain unchanged. Backend correctness is still an assumption,
not a result of agreement between implementations. Global decrease,
second removal, iteration and all-degree mixed positivity remain open.

## Mathlib

Full matching coverage of this quantitative sign and root-qualified
local decrease is unchecked; no absence claim is made. General
calculus or interval support would not certify the numerical margin
without the specialization above. No declaration was verified here.
Documentation: https://leanprover-community.github.io/mathlib4_docs/ .
