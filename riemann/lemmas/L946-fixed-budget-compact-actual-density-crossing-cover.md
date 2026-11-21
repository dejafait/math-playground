# Lemma 946: a fixed-budget compact actual-density crossing cover

## Hypotheses

Use exactly L938's actual density v, its 34 signed rows, twelve labelled
factors, factorials and retained M_0^12 normalization. Reuse its audited
degree256 polynomial p, 257 nodes, theta cutoff8, precision200 and
coefficient grid10^-120, with all3073 signed coefficients R_l and C^12
from L938(18). Use C944a's full value and derivative inclusions on [0,8],
including H=2+epsilon and its cited actual-kernel bound.

Retain L938's directed Decimal/exponential execution contracts and
exact-integer implementation trust. The step50 integer identity and
step75 audit are reused under matching hashes, not independently
reconstructed here. No crossing, contact, parameter sign, realization
or RH premise is assumed. The new range calculations use integers only.

## Conclusion

Subject to these execution contracts, every zero E of v in the closed
interval [1/4,4] satisfies v'(E)>0. The independent step78 conceptual
audit below validates this compact certificate under the retained
execution contracts. The original step76 consistency checks alone
did not establish its Taylor ranges.

Specifically, 50 closed dyadic leaves cover [1/4,4]: 22 have v<0,
24 have v>0, and four have v'>0 throughout. There are no unresolved
leaves. The traversal examines99 intervals and reaches depth9, within
the preapproved depth12/8191-interval limits. Both outer endpoints and
every shared endpoint are retained. No assertion about zeros outside
this compact interval, other degrees, contacts, parameter signs,
initialization, realization or RH follows.

## Proof

### The two unchanged observables and their analytic allowances

Put y=E/4 and, for s=17,16, define the finite polynomial

    f_s(y)=sum_(l=0)^3072 a_(s,s+l)y^(s+l),
    a_(s,s+l)=R_l 4^(s+l)/[C^12(s+l)!].                         (1)

Coefficients below degree s are zero. L938(18) gives exactly

    f_17(y)=v_p(4y)/pi^6,
    f_16(y)=v_p'(4y)/pi^6.                                    (2)

The second observable is differentiation in E before evaluation at
4y, not differentiation in y. Thus no factor4 is missing. Only the
polynomial argument is rescaled; v and its normalization are unchanged.

Write A,D,Z for C944a's A_H,D_H,Z. Its already justified bounds are

    |v(E)/pi^6-f_17(E/4)|<=Z E^17 A,
    |v'(E)/pi^6-f_16(E/4)|<=Z E^16(17A+ED).                   (3)

All constants are positive. These allowances include the entire
analytic interpolation error, coefficient errors, full theta tail,
derivative series, twelve-factor error and E^17 differentiation.
No cell-mass bound is differentiated. C944a supplies dominated
differentiation despite the singular simplex faces and the two-sided
derivative at each positive energy. No L942 identity is used.

### Directed integer polynomial ranges

Set S=2^1024. For every coefficient in (1), exact Euclidean division
gives integers L_j,U_j such that

    L_j=floor(S a_j), U_j=ceil(S a_j), L_j/S<=a_j<=U_j/S.       (4)

The implementation checks the division identity and remainder bounds
for all coefficients of both polynomials. It retains every coefficient
in the report. Set J=768 and truncate only the *evaluation* polynomial:

    P(y)=sum_(j=0)^(J-1) a_j y^j,
    T=sum_(j>=J) max(|L_j|,|U_j|).

For 0<=y<=1, the discarded part has absolute value at most T/S.
This is a fully paid finite-polynomial tail, not a changed kernel fit,
theta cutoff or interpolation degree. No coefficient is silently
discarded on account of its size.

Let [a,b] be a dyadic y interval in [1/16,1], c=(a+b)/2 and
h=(b-a)/2. Take Taylor order K=128. We enclose the first K coefficients
of P(c+z) in integer intervals [l_k,u_k]/S. Initialize all these
integers to zero. Traverse the retained coefficients in descending j;
update k=K-1,...,1 in descending order by

    l_k <- floor(c l_k)+l_(k-1),
    u_k <- ceil(c u_k)+u_(k-1),

using the old k-1 values, and then update

    l_0 <- floor(c l_0)+L_j,
    u_0 <- ceil(c u_0)+U_j.                                  (5)

All floors and ceilings multiply by the exact rational c. Horner's
identity P_next(c+z)=(c+z)P_old(c+z)+a_j proves (5) by induction:
coefficients of order<K are unaffected by discarded higher orders,
and c>=0 preserves interval order. Every rounding in (5) is outward.
This finite algebra is included to justify this implementation; it is
not a reproof of a general validated-integration theorem.

The nonconstant Taylor part is bounded by V/S, where an upward-rounded
Horner recurrence computes

    V >= sum_(k=1)^(K-1) max(|l_k|,|u_k|) h^k.                 (6)

The classical Taylor theorem with Lagrange remainder applies to the
real polynomial P on [a,b], expanded through degree K-1. Its remainder
at order K is at most

    h^K sum_(j=K)^(J-1) |a_j| binom(j,K) b^(j-K).             (7)

Indeed P^(K)(x)/K! is the corresponding sum with signed coefficients;
0<=x<=b bounds each absolute monomial by b^(j-K). Precisely, import
[NIST DLMF1.4.35-37](https://dlmf.nist.gov/1.4#vi), with its
C^K hypothesis satisfied by the polynomial. For displacements left
of c apply the theorem to P(c-z); for displacements right of c apply
it to P(c+z). At zero displacement the remainder is zero. The
intermediate derivative points remain in [a,b], including the closed
endpoints. No infinite Taylor-series assertion is used. The finite sum in
(7), multiplied by S, is bounded above by Q: use the nonnegative
integer coefficients max(|L_j|,|U_j|)binom(j,K), Horner evaluation
at b, and upward rounding after every multiplication. Set

    W=ceil(Q h^K).

Equations (4)-(7) therefore give the rigorous full-polynomial range

    f_s([a,b]) subset
      [(l_0-V-W-T)/S, (u_0+V+W+T)/S].                       (8)

Coefficient rounding, Taylor-coefficient rounding, Taylor variation,
the Taylor remainder and the discarded polynomial tail are all paid
separately. The very large signed coefficients are combined in (5)
before the final absolute bounds (6)-(7). Pointwise sampled signs or
an unqualified floating Horner evaluation are not used as ranges.

### Actual ranges and the closed cover

For an energy interval [4a,4b], let q_0 and q_1 be (8)'s value and
derivative ranges. Both right sides of (3) increase with E>0. Enlarge
q_0 and q_1 symmetrically by, respectively,

    ceil(S Z(4b)^17 A)/S,
    ceil(S Z(4b)^16[17A+4bD])/S.                             (9)

These are ranges for actual v/pi^6 and v'/pi^6 on the whole closed
energy interval. The positive constant pi^6 does not change signs.

Start with [1/4,4]. A node at depth d,index i is exactly

    [(2^d+15i)/(4*2^d), (2^d+15(i+1))/(4*2^d)].             (10)

If the actual value range excludes zero, accept that node as a leaf.
Otherwise compute the derivative range and accept the leaf only if
its lower endpoint is strictly positive. Otherwise bisect, except
that depth12 leaves would remain unresolved. The algorithm never
deletes a shared endpoint or substitutes opposite endpoint signs
for whole-interval inclusion.

The complete certificate records every visited node, both computed
ranges as applicable, all components of (8)-(9), decisions and exact
dyadic endpoints. It has99 nodes, depth<=9, 50 closed leaves and no
unresolved leaf. A separate exact check confirms the two children of
each internal node, each parent, all consecutive shared endpoints,
the outer endpoints, all range assemblies and every strict decision.

For each accepted leaf compare its polynomial-range clearance from
zero, in its chosen sign, with its positive radius in (9). The minimum
ratio over all50 leaves is strictly between78557 and78558; the
required threshold is1. It occurs at depth5,index31, a positive-value
leaf. The exact ratio and integer gap are retained in the certificate;
the actual lower margin there is approximately4.90641538357e-42 in
units v/pi^6. These rounded displays are not the proof of inclusion.

At an actual zero E, some closed leaf contains E. Neither a positive-
nor a negative-value leaf can contain that zero. That leaf consequently
has a strictly positive derivative range, and v'(E)>0. This proves
exactly the stated compact crossing assertion, not the global
sign-change premise required for a Laplace-transform zero-count argument.

### Evidence, sources and qualifications

Reproduction commands, relative to this notebook:

    python3 scripts/heat/l938-direct-cover-76.py
    python3 scripts/heat/check-l938-direct-cover-76.py

The full producer certificate is `scripts/heat/l938-direct-cover-76.json`;
the consistency/point-check certificate is
`scripts/heat/l938-direct-cover-check-76.json`. The producer checks every
coefficient division, all prior audit flags and identities under matching
hashes, every range decision and all strict leaf margins. The checker
has983 passing checks and no failures. Besides reading every recorded
range component, it computes full-polynomial values by independent
ascending exact integer summation at the four derivative-leaf midpoints
and the two outer endpoints. At the four midpoints it also checks the
Taylor constant enclosure after paying only the discarded tail.
All complete relevant evidence was checked programmatically; these
point checks alone would not establish (8) or interval coverage.

The ready method comparison is the step67/68 direct-density assessment.
Its inspected primary interval-exclusion contract is FLINT v3.3.1,
`doc/source/arb_calc.rst`, root isolation lines102-149 and callbacks
lines26-39, with the complete isolation implementation:
[contract](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/arb_calc.rst),
[implementation](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/arb_calc/isolate_roots.c).
The elementary implication from a certified positive derivative range
is specialized above; no FLINT routine or convergence guarantee is
assumed. Polynomial Taylor's theorem is used only with its stated
smoothness and compact-interval hypotheses. L938 and C944a retain the
precise analytic/Chebyshev/beta citations for (1)-(3).

This is a specialization of known enclosure methods to this fixed
actual density, not a claim of a new general theorem or progress beyond
the sources' numerical methods. L944's coarse endpoint obstruction,
the earlier reporting failures and all unfinished independent work
remain intact. The required later independent audit is recorded below.
No complete RH argument has been assembled.

### Independent conceptual audit — 9 November 2026, step78

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-11-09-l946-cover-audit-scope-76.md`.
It covers precisely this application of the named Taylor theorem,
the inherited analytic inclusions and the closed-cover logic. No
new source coverage, degree, domain, precision or fit is introduced.
Run the independent verifier with

    python3 scripts/heat/audit-l946-cover-78.py

The complete report is `scripts/heat/l946-cover-audit-78.json`.
All 56097 checks pass, with no failures. It validates all 152 recorded
polynomial ranges on all99 nodes, and all50 leaves. It imports no
functions from either step76 program and does not use their rounded
shifted-Horner recurrence to establish interval inclusion.

Here is the independent range calculation and why it suffices. For
each observable, independently verify every signed coefficient's
floor and ceiling by exact integer inequalities, including all zero
coefficients below s, all3073 R coefficients, the factorials, 4 powers
and the denominator C^12. At a midpoint c>=0 define

    B_k^- = sum_(j=k)^(J-1) L_j binom(j,k)c^(j-k),
    B_k^+ = sum_(j=k)^(J-1) U_j binom(j,k)c^(j-k), 0<=k<K.     (11)

The binomial theorem identifies these as bounds for S times the
coefficient of z^k in P(c+z). Nonnegative weights justify applying
L_j and U_j separately even when their values are negative. This
calculation uses the exact coefficient intervals and contains no
assumption that polynomial coefficients are positive.

Each sum (11) is evaluated as its own rational polynomial at c=n/d,
with no rounding during accumulation. For a degree-m coefficient
list b_0,...,b_m, start A=b_m,D=1; at each descending step replace
D by dD and A by nA+b_j D, using the updated D. Inductively A/D is
the current exact rational Horner value. This evaluates the explicit
binomial sums separately for each k; it never performs the producer's
in-place Taylor update. Round only the final sums to

    lhat_k=floor(B_k^-), uhat_k=ceil(B_k^+).

The report retains all128 resulting interval pairs for every one of
the152 ranges. It checks l_0<=lhat_0<=uhat_0<=u_0 against the saved
center range. Exact rational accumulation, followed by a single
ceiling, computes

    Vhat=ceil(sum_(k=1)^(K-1) max(|lhat_k|,|uhat_k|) h^k).

Every saved V is at least Vhat. Thus the constant and entire retained
nonconstant Taylor part are enclosed independently of (5)'s execution.
The descending order in (5), its use of old lower-order coefficients,
and its signed floors/ceilings were also checked mathematically;
discarding orders >=K cannot affect any retained order.

For the remainder, independently evaluate the complete nonnegative
polynomial sum_(j=K)^(J-1) max(|L_j|,|U_j|)binom(j,K)b^(j-K)
as an exact rational. Its numerator and denominator are retained for
each range. Every saved Q bounds that value, and every saved W equals
ceil(Qh^K). With the two-sided Taylor justification above, this pays
the remainder everywhere on the closed interval. Independently sum
every discarded coefficient through the true last degree,3089 or3088;
the result equals each saved T. These checks prove (8) for the full
polynomials; the finite tail is not substituted for any theta tail.

The verifier reconstructs epsilon,delta,B,H,A,D,Z from all257 complete
coefficient intervals and all34 signed beta rows, including positive
half-integer parameters, twelve factors, weighted degree12 and the
sum293/540. It checks equality with both C944a and the cover report.
All5101 step50 flags, the full exact identity record, all15620 step75
flags, the540 C944a flags, every step76 producer flag and all983
consistency flags are read completely, under matching input/code hashes.
The zero integer residual, theta-node production and source theorem
for k<2 are reused from their audited inputs, not independently
reproved or replayed. Both original step76 files and all hashed inputs
remain unchanged. The scope of that inherited trust is not enlarged.

The analytic review checks (2)-(3) directly against L938(18) and
C944a. The E derivative evaluated at4y is precisely f_16, and the
error is obtained by differentiated products under an integrable
simplex majorant, with the full17E^16 prefactor derivative. A,D,Z
are positive, so their allowances increase with E>0. Exact rational
comparisons verify each right-endpoint radius (9), every polynomial
and actual range assembly, every strict decision, each parent and
both children, unique nodes, all positive leaf lengths and every
outer/shared closed endpoint. There are22 negative-value leaves,
24 positive-value leaves and four positive-derivative leaves, with
maximum depth9. No depth-budget or unresolved leaf is suppressed.

The exact minimum clearance ratio over all50 leaves is in
(78557,78558), against the required >1, at depth5,index31. The
report also retains the exact positive derivative lower bounds for
each of the four possible-zero leaves. For scale only, their lower
bounds for v'/pi^6 are approximately3.4928087062223e-45,
1.2171140586612e-45,8.6480999367765e-43 and1.0004102105432e-38.
Acceptance uses their exact rational numerators and denominators,
not those rounded displays. The full summary, exact ratio, derivative
lower bounds and empty failure list were inspected after execution.

Consequently the closed-leaf argument above is validated: any actual
zero belongs to a leaf, cannot belong to a strict value-exclusion
leaf, and therefore has strictly positive actual derivative. This
audits an existing local specialization of known methods; it is not
a new general enclosure theorem, global one-crossing theorem or RH
resolution. The inherited Decimal/exponential/integer contracts,
other energies, degrees, contacts, parameter signs, initialization
and realization remain as stated. No new mathematical input edge
is needed, and L942 is not an input to this audit.

## Mathlib

Full or supporting Mathlib coverage of this exact density certificate,
directed integer Taylor algorithm and closed cover has not been checked.
Availability is unknown. Standard Taylor and interval-exclusion arguments
here are informal mathematics, not a formal verification of Python or
the inherited numerical libraries.
