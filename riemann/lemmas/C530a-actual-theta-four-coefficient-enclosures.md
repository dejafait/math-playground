# C530a — Four actual Romik coefficients by direct certified quadrature

## Hypotheses

Let omega and c_(2j) have exactly Dan Romik's normalization in
*Orthogonal polynomial expansions for the Riemann xi function*,
arXiv:1902.06330v3 (5 May 2019), equations (1.7) and (3.3),
[primary text](https://arxiv.org/html/1902.06330v3):

    omega(x) = sum_(n>=1) (2 pi^2 n^4 x^2 - 3 pi n^2 x) exp(-pi n^2 x),
    c_(2j) = 4 sqrt(2) integral_1^infinity
             omega(x) (x-1)^(2j) (x+1)^(-2j-3/2) dx.

These identities and their normalization are imported, not reproved.
Here j=0,1,2,3 only. The computational part assumes correct CPython
integer/Fraction arithmetic and libmpdec directed basic arithmetic and
correctly rounded exponential, as specified below. This is an informal
certificate with explicit backend trust, not a formal machine proof.

## Conclusion

The four coefficients admit positive finite enclosures of absolute
width at most 2^-40. Complete decimal endpoints and exact rational
widths are recorded under `/coefficients` in
`scripts/pollaczek/direct-theta-coefficients-2068.json`. The proof and
certificate passed the independent budget reconstruction and full replay
audit2070 described below, under the explicit backend trust assumptions.
Their production and verification reproduce known formulas and quadrature;
they are not a claim of new mathematics beyond the sources checked.

For convenient display, the following slightly wider rational decimal
intervals also enclose the coefficients and meet the same width bound:

| Coefficient | Lower endpoint | Upper endpoint |
| --- | --- | --- |
| c0 | 0.48099000592797654 | 0.48099000592798365 |
| c2 | 0.01941821719853482 | 0.01941821719854973 |
| c4 | 0.0020319448877264396 | 0.0020319448877538714 |
| c6 | 0.00031408664874727607 | 0.00031408664879341623 |

No ratio, polynomial discriminant, root count, all-degree sign or RH
conclusion is asserted. In particular, L530's two-atom obstruction is
only motivation for a possible later actual-coefficient test; it is not
a mathematical input here. The actual theta density is retained.

## Proof

### Imported quadrature and tail integral identities

For real f in C^4[a,b], even positive m, h=(b-a)/m, the composite
Simpson rule S satisfies

    |integral_a^b f - S| <= (b-a) h^4 sup_[a,b] |f''''| / 180.

Import this standard theorem from [DLMF 3.5(ii), (3.5.6)–(3.5.8)](https://dlmf.nist.gov/3.5.ii).
Only the finite theta sum is differentiated or integrated by Simpson.
For A>0, the integer upper-gamma identity gives

    integral_A^infinity x^2 exp(-3x) dx
      = exp(-3A)(A^2/3 + 2A/9 + 2/27),
    integral_1^infinity x^2 exp(-3n^2 x) dx
      = exp(-3n^2)(1/(3n^2) + 2/(9n^4) + 2/(27n^6)).

These are specializations of [DLMF 8.2.2](https://dlmf.nist.gov/8.2.E2),
[8.4.8](https://dlmf.nist.gov/8.4.E8) and
[8.4.11](https://dlmf.nist.gov/8.4.E11), with positive real endpoint
and nonnegative integer gamma parameter. The identities evaluate the
majorants below; the comparisons themselves still require proof.

Set X=16, N=4, m=2^18. Put k=2j,

    a_n=pi n^2, g_n(x)=(2a_n^2 x^2-3a_n x)exp(-a_n x),
    u(x)=(x-1)/(x+1), v(x)=(x+1)^(-3/2),
    f_k(x)=4sqrt(2) sum_(n=1)^4 g_n(x) u(x)^k v(x).

All these finite integrands are real C^infinity on a neighborhood of
[1,16], including x=1. For x>=1 every g_n is positive, since
2pi n^2 x-3>0; also 0<=u<1 and 0<v<=1. Thus the omitted integrals
are nonnegative. The rational comparisons 3<pi<22/7 and e^3>20
are certified below, and 4sqrt(2)<6, 12pi^2<120 follow.

### Theta-index remainder

The integral over [1,16] of the n>=5 terms is bounded above by the
integral over [1,infinity) of their positive majorants. Dropping u^k v
and the negative term in g_n gives

    T_N <= 120 sum_(n>=5) n^4 integral_1^infinity x^2 exp(-3n^2 x) dx
        <= 80 sum_(n>=5) n^2 20^(-n^2).

For the second inequality use the imported integral identity and

    120(n^2/3 + 2/9 + 2/(27n^2))
       <= 120 n^2(1/3+2/9+2/27) < 80 n^2,
    exp(-3n^2) < 20^(-n^2).

For n>=5 the ratio of successive n^2 20^(-n^2) terms is at most
(6/5)^2 20^-11 < 1/2. The geometric sum therefore proves the uniform
bound, valid for all four k,

    0 <= T_N <= B_N := 4000 / 20^25.

### Full spatial remainder

For x>=16 the ratio of successive n^4 exp(-3n^2 x) terms is at most
16exp(-9x)<=16exp(-144)<16*20^-48<1/2. Hence their sum over n>=1
is at most 2exp(-3x). The complete original integrand is bounded by
240x^2 exp(-3x), so the spatial remainder satisfies

    0 <= T_X <= B_X := (240/20^16)(256/3 + 32/9 + 2/27).

This is the full theta spatial tail, not just the first four terms.
Both majorants are integrable. Positivity permits Tonelli for the
tail comparisons; their finite bounds also establish the required
absolute integrability. No conditional summation, limiting quadrature
or numerical tail estimate is used.

### Uniform fourth-derivative bound

The following explicit triangle bounds are deliberately coarse. They
avoid sampled derivative maxima. For r=0,...,4 define exact rational
numbers

    A_n = 22n^2/7,
    G_r = sum_(n=1)^4 20^(-n^2) [
            A_n^r (2A_n^2+3A_n)
            + r A_n^(r-1)(4A_n^2+3A_n)
            + binom(r,2) A_n^(r-2) 4A_n^2 ].

The middle term is omitted when r=0, and the last when r<2.
To verify this bound, apply Leibniz to g_n=P_n exp(-a_n x), where
P_n=2a_n^2 x^2-3a_n x. In absolute value,

    |P_n| <= 2a_n^2 x^2+3a_n x,
    |P_n'| <= 4a_n^2 x+3a_n,  P_n''=4a_n^2,
    P_n^(l)=0 for l>2.

For q=0,1,2, x^q exp(-a_n x) decreases on x>=1 because its
logarithmic derivative q/x-a_n is negative. Therefore it is at most
exp(-a_n). Replace exp(-a_n) by 20^(-n^2) and each remaining
positive power of a_n by A_n to obtain
sup_(x>=1) |sum_(n=1)^4 g_n^(r)(x)| <= G_r.

For the weight, |v^(r)(x)|=(3/2)_r (x+1)^(-3/2-r)
<=V_r:=(3/2)_r/2^(r+1), since x+1>=2 and sqrt(x+1)>=1.
Also |u|<=1, and for s>=1,

    |u^(s)(x)|=2s!/(x+1)^(s+1)<=s!/2^s.

Let U_s=s!/2^s for s=0,...,4 (so U_0=1). Start W_r=V_r and
repeat the replacement

    W_r <- sum_(s=0)^r binom(r,s) W_(r-s) U_s

exactly k times, with all right sides from the preceding iteration.
Repeated Leibniz proves |(u^k v)^(r)|<=W_r uniformly on x>=1.
This also covers k=0. A final Leibniz application gives

    sup_[1,16] |f_k''''| <= M_k
       := 6 sum_(r=0)^4 binom(4,r) G_r W_(4-r).

Every number in this construction is rational. The certificate stores
all five G_r and V_r, each complete five-entry W vector and exact M_k.
The M_k are respectively less than 7905, 16651, 30670 and 51612.
The associated exact Simpson errors

    E_k = 15^5 M_k / (180 m^4)

are each less than 4.611*10^-14. The bound covers the entire interval
and the complete finite integrand, including the normalizing factor.

### Constants and finite arithmetic

The reproducible implementation is
`scripts/pollaczek/direct_theta_coefficients_2068.py`. Run, from this
notebook, `python3 scripts/pollaczek/direct_theta_coefficients_2068.py`.
It writes the full certificate to the JSON path in the conclusion.
No installed numerical dependency or floating-point approximation is
used to establish an enclosure; printed scientific widths are summaries.

Pi endpoints come from the classical Machin formula
pi=16 arctan(1/5)-4 arctan(1/239). For completeness its applicability
here can be checked by tangent addition: tan(2 arctan(1/5))=5/12,
tan(4 arctan(1/5))=120/119, and subtracting arctan(1/239) gives
tangent 1. The resulting angle is positive
(4 arctan(1/5)>4*(1/5-(1/5)^3/3)>arctan(1/239)). Its upper
bound pi/2 can also be seen without a numerical pi bound:
2 arctan(1/5)=arctan(5/12), so 4 arctan(1/5)<2 arctan(1)=pi/2.
Thus the resulting angle is pi/4. Exact alternating rational series, with 80 terms for 1/5
and 25 for 1/239, enclose each arctangent between its partial sum and
that sum plus its next term. Combining endpoints outward gives the
pi interval and verifies 3<pi<22/7 by rational comparisons. The
positive exponential series through degree 8 verifies e^3>20.
This is only constant certification, not a reproof of any source
expansion. Rational endpoints are converted by directed division.

All three Decimal contexts have precision 60, Emin=-999999,
Emax=999999, clamp=0. Basic lower operations use ROUND_FLOOR and
upper operations ROUND_CEILING. InvalidOperation, DivisionByZero,
Overflow, Underflow, Subnormal, Clamped and FloatOperation are trapped;
Inexact and Rounded are allowed and their sticky flags recorded.
The actual Python, module and libmpdec versions, contexts, flags and
operation counts are retained under `/runtime`. Correct backend
operation remains an explicit trust assumption; smoke tests do not
prove backend correctness.

The [Decimal API contract](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp)
specifies correctly rounded HALF_EVEN exp. Thus, for interval argument
[a,b], compute exp(a), exp(b) in the nearest context, then take the
preceding and following representable numbers. Monotonicity makes
these outward endpoints. No directed-exp assumption is made. All
sqrt evaluations similarly start in the nearest context and take
neighbors, but their endpoint squares are additionally checked with
exact Python integers against the exact positive radicand, at every
node and for sqrt(2). These comparisons establish the sqrt enclosures
without relying on a directed-sqrt rounding interpretation. Positivity
and nonzero denominator assertions guard every interval multiplication
or division. Interval subtraction uses opposite endpoints.

Nodes x_i=1+15i/2^18 are exactly representable decimals. The code
constructs them using 5^18*10^-18 and checks each against its exact
Fraction value; x_i+1 and x_i-1 are also exact at 60 digits. For
each node it evaluates all four g_n, sums omega, multiplies by
4sqrt(2)/[(x+1)sqrt(x+1)], and obtains successive k values by
multiplication by u^2. Each operation encloses the exact real value.
Simpson weights are 1 at endpoints, 4 at odd nodes, 2 at even interior
nodes; multiplication of their interval sum by 15/(3m) gives
[Q_k^-,Q_k^+] containing the exact finite Simpson sum. Its full
width is the explicit arithmetic-and-constants error, rather than a
heuristic estimate based on working precision.

Finally form, with directed rounding,

    I_k = [ Q_k^- - E_k, Q_k^+ + E_k + B_N + B_X ].

Since missing tails are nonnegative and quadrature error can have
either sign, this encloses c_k. The program checks every endpoint
is finite, each lower endpoint is positive, and the exact Fraction
difference of upper and lower endpoints is <=1/2^40. It preserves
all four complete intervals and individual error components, as well
as the failure list. Caps are X<=64, N<=32, m<=2^18, precision<=100;
the actual choices satisfy them. Runtime square comparisons, flags,
final positivity and widths must all pass; requested tolerance alone
is not evidence. See the saved execution evidence in the certificate.

The completed run used CPython 3.15.2 and libmpdec 4.0.1. All 262145
nodes were evaluated, with 524292 exact square comparisons (two for
each node's sqrt and for sqrt(2)). The only raised sticky flags were
Inexact and Rounded, in each of the three contexts. The failure list
and unexpected-signal list are empty. The four exact saved widths are
strictly below, respectively, 7.095e-15, 1.491e-14, 2.744e-14 and
4.615e-14, all below 2^-40=1/1099511627776. Their quadrature interval
widths, which include all arithmetic/constants error, are below
5e-55, 5e-56, 5e-57 and 5e-58 respectively. The exact common tail
bounds simplify to B_N=1/83886080000000000000000000000 and
B_X=1201/36864000000000000000. Complete error vectors, constants,
runtime fields and intervals were inspected, not just a preview or
requested precision. The original execution checks alone did not establish
independent verification; the following audit supplies that additional check.

### Independent budget reconstruction and full replay — 21 November 2026

Run `python3 scripts/pollaczek/direct_theta_audit_2070.py`.
The full audit evidence is `scripts/pollaczek/direct-theta-audit-2070.json`;
the separate replay is
`scripts/pollaczek/direct-theta-coefficients-replay-2070.json`.
All 49 checks passed, with an empty failure list. All non-runtime fields
of the replay agree exactly with certificate2068, whose original bytes
are preserved. Both complete runtime records were inspected: CPython
3.15.2, libmpdec 4.0.1, the stated three contexts and traps, all 262145
nodes and 524292 exact square comparisons, with only Inexact/Rounded
flags. This is an independent local reconstruction/code audit, not an
external review or a proof of the arithmetic backend.

The analytic audit checked positivity on the complete tail domains and
the disjoint decomposition into n>=5 on [1,16] and all n on [16,infinity).
The index majorant deliberately extends its domain to [1,infinity), which
only enlarges a nonnegative integral. The two geometric ratios are at most
36/(25*20^11) and 16/20^48, respectively, each strictly below 1/2.
The integrated index constant is bounded using
120(1/3+2/9+2/27)<80. Thus neither a missing tail nor a signed cancellation
is hidden. The saved B_N and B_X agree exactly with these comparisons.

To check the global derivative estimate independently, the audit expands
each monomial of 2A_n^2 x^2+3A_n x using falling factorials rather than
the generator's three-term expression. The monotonic bound
x^q exp(-a_n x)<=exp(-a_n) applies to every resulting q=0,1,2,
since a_n>3>q. This reproduces all five exact G_r.
For W_r the audit uses the multinomial Leibniz expansion over the k
individual u factors and the one v factor: for nonnegative integers
s_1,...,s_k with sum S<=r, its summand is

    [r!/(r-S)!] V_(r-S) product_(i=1)^k 2^(-s_i).

Indeed the multinomial denominator s_i! cancels the s_i! in U_(s_i).
Summing these terms also covers the empty product k=0, and independently
reproduces every full five-entry W vector. The final binomial sum for M_k
and E_k=15^5 M_k/(180*2^72) then agrees exactly with the certificate.
No derivative maximum is inferred from sampled nodes or the replay.

The constant audit reconstructs the arctangents by paired alternating
terms, checks both exact Machin endpoints and their outward decimal
conversions, the rational pi comparisons, e^3>20 and the exact sqrt(2)
square enclosure. Inspection of the generator checks that all variable
node arithmetic is exact before enclosure operations: the mesh constant
and node products have fewer than 28 significant digits, and x+/-1 has
fewer than 60. Even the mesh construction's default-context scaleb is
therefore exact. Every node is additionally compared to its Fraction.
All remaining signed operations use opposite interval endpoints;
multiplication/division use asserted nonnegative factors and positive
denominators. Exponentials use monotonicity, correctly rounded nearest
evaluation and outward neighbors, rather than assumed directed exp.
Square enclosures have exact integer comparisons at every node.

Finally, exact rational comparisons independently check, for each k,
the complete quadrature width, lower<=Q_k^- - E_k and
upper>=Q_k^+ + E_k+B_N+B_X, positivity and the exact final width<=2^-40.
The four widths are respectively below
7.095e-15, 1.491e-14, 2.744e-14 and 4.615e-14. The full audit check
list, rational M/E/width records, original coefficient/error/constant
fields and both runtime records were inspected, not just previews.
The independent reconstruction and the conceptual bounds justify using
the four intervals under the stated trust assumptions; reproducibility
alone would not justify them. No discriminant or root count was computed.

### Qualifications and downstream use

This finite certificate is not an RH-equivalent positivity assertion.
It cannot settle root collisions, initial hyperbolicity, multiplicities,
uniformity in degree or transfer from finite polynomial families to Xi.
Any use of its numerical intervals in a further diagnostic requires a
separately covered target and audit of these load-bearing error bounds.

## Mathlib

Matching coverage of the full coefficient certificate, Romik's formula,
the quadrature specialization and Decimal backend semantics is not
checked. No claim of absence is made. The imported analytic identities
have precise primary citations above; this is not a Lean proof.
