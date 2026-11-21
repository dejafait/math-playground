# Corollary 944a: sharper common factor bound resolves the fixed endpoint

## Hypotheses

Use exactly L938's actual signed density v, its M_0^12 normalization,
34 rows and twelve factors, and its unchanged degree256 polynomial p
on [0,8]. Retain the 257 nodes, theta cutoff8, precision200,
coefficient grid10^-120, full coefficient errors eta_l, and the
directed Decimal/exponential and exact-integer execution contracts.
Reuse L944's derivative enclosure delta and common derivative bound B,
defined in its (1), and L945's actual-kernel bound. No crossing,
contact, parameter endpoint, realization or RH assumption is made.

## Conclusion

Let epsilon be L938(15)'s complete error, and set

    H=2+epsilon,
    A_H=12 epsilon H^11,
    D_H=delta H^11+11 B epsilon H^10,
    Z=(293/540)/(2^36 17!).

For 0<E<=8, with the same finite polynomial density v_p,

    |v(E)-v_p(E)|/pi^6 <= a_H(E):=Z E^17 A_H,
    |v'(E)-v_p'(E)|/pi^6 <= b_H(E):=Z E^16(17A_H+E D_H).

At E=4, exact rational comparisons give

    141790 < [v_p(4)/pi^6]/a_H(4) < 141791,
    921 < -[v_p'(4)/pi^6]/b_H(4) < 922.

Consequently v(4)>0 and v'(4)<0, conditional on the retained numerical
input contracts. The value enclosure passes the endpoint preflight.
This supplies no compact crossing cover or sign condition at a zero;
the negative derivative here does not refute upward crossing since
the value is strictly positive. Other energies, parameter signs,
contacts, other degrees, realization and all-degree Xi positivity remain
unresolved. L944's coarse-radius obstruction remains valid as stated.

## Proof

L945 gives 0<k(x)<2 for x>=0, where k(x)=K(sqrt(x)). L938(15)
gives |p(x)-k(x)|<=epsilon on [0,8]. Thus |k|,|p|<=H there.
This pays the complete polynomial error; no positivity or bound2 for
p is assumed. L944 independently obtains |k'-p'|<=delta and
|k'|,|p'|<=B from the analytic Chebyshev series and full coefficient
errors, using T_m'=m U_(m-1) and |U_(m-1)|<=m on [-1,1]
([DLMF18.9.21](https://dlmf.nist.gov/18.9#E21),
[18.14.4](https://dlmf.nist.gov/18.14#E4)). Those bounds are unchanged.

For t_i>=0 with sum t_i=1 and E in [0,8], every E t_i is in [0,8].
The standard difference-of-products identity bounds the error in the
twelve-factor products by 12 epsilon H^11. In their E derivatives,
replace the differentiated factor first: term i costs at most

    t_i[delta H^11+11 B epsilon H^10].

The sum of t_i is one, so the derivative error is D_H. This is the
same telescoping and product-rule argument as L944 with a justified
smaller common majorant, not differentiation of a real error inequality.

In each of L938(9)'s rows the simplex weight has parameters
k_i+1/2>0. The kernel and polynomial factors and their first derivatives
are bounded uniformly on this compact domain. A constant multiple
of the integrable row weight therefore dominates the integrand and
its E derivative independently of E. Dominated differentiation is
valid despite singular coordinate faces. Euler's beta identity
([DLMF5.12.1](https://dlmf.nist.gov/5.12#E1), positive parameters)
and the half-integer gamma identity, including all (2k_i)! and 2^-12
factors, give absolute total weight pi^6 Z, as in L938 and L944.
Summing all34 rows with absolute coefficients gives 293/540.
Multiplication by E^17 yields the value bound. Its derivative contributes
17E^16 A_H plus E^17 D_H, proving the derivative bound without an
unjustified interchange or an extra factor twelve.

Precisely, use L944's local open-energy-neighborhood argument and the
mean value theorem to dominate the difference quotients by a constant
times each row weight, then apply Lebesgue dominated convergence.
This gives the two-sided derivative at4. At8 use the slightly larger
analytic interval only for differentiation; the bound H is used at
the evaluation point, where every E t_i still lies in [0,8]. No bound
H outside [0,8] is asserted or needed.

The centers are exactly L944(4), from L938(18): for s=17 and16,

    c_s=sum_(l=0)^3072 R_l 4^(s+l)/[C^12(s+l)!].

Use common factorial (3072+s)! and exact integer Horner evaluation.
No pi approximation enters: c_17=v_p(4)/pi^6 and c_16=v_p'(4)/pi^6.
The script checks equality of both full rational centers with L944's
saved centers, as well as unchanged epsilon, delta, B and Z. It then
computes A_H,D_H and both radii exactly and verifies the displayed
strict rational brackets. Since each radius is positive, the first
bracket implies c_17-a_H(4)>0, and the second implies
c_16+b_H(4)<0. The two inclusions prove the signs.

Reproduction:

    python3 scripts/heat/l938-two-bound-endpoint-73.py

The full constants, exact centers, radii, interval endpoints, brackets,
hashes and check entries are in
`scripts/heat/l938-two-bound-endpoint-73.json`. The producer reads all257
coefficient intervals and checks each complete radius, all34 beta rows,
the fixed budgets and denominator, all5101 prior audit flags and the
completed exact-polynomial residual. It checks the three audited input
hashes and all prior endpoint flags. The saved polynomial contains all
3073 coefficients. Full rational comparisons, not rounded previews,
establish the signs. The audited theta-node and signed-polynomial
production are reused rather than independently replayed in this step.

For scale only, the centers are respectively 8.85584862764e-42 and
-8.02308777963e-41; radii are 6.24574459969e-47 and 8.70393904097e-44.
These rounded displays do not establish inclusion. One singleton was
tested, no interval subdivision or budget sweep was performed, and
the closed domain [1/4,4] remains uncertified as a whole.

The first run passed the two sign comparisons but failed an anticipated
reporting bracket 200<(-c_16)/b_H(4)<300. Its script and report are
preserved as `scripts/heat/l938-two-bound-endpoint-73-first-pass.py` and
`scripts/heat/l938-two-bound-endpoint-73-bracket-failure.json`.
The corrected run uses exact integer-floor brackets for presentation;
no polynomial, allowance or mathematical threshold was changed.
This is a local specialization of known enclosure methods, not a new
general theorem or progress beyond those methods.

### Independent conceptual audit — 9 November 2026, step75

The pre-existing SPECIALIZE audit scope and the independent verifier
are recorded in L944. The full certificate is
`scripts/heat/l944-c944a-audit-75.json`; all15620 checks pass.
In particular, the argument pays both sides of H=2+epsilon and the
complete epsilon, retains delta and B, and uses the same twelve-factor
and positive-parameter beta normalization as L938. L945 is retained
as its precisely cited theorem application with the audited L826(8)
r=0 input; this audit does not reprove theta monotonicity or replay
that separate endpoint computation.

Independent exact integer accumulation reproduces both rational
centers, radii and interval endpoints. It verifies the fixed brackets
(141790,141791) and (921,922), rather than only recomputing integer
floors. Positive error radii and these strict comparisons establish
the two signs under the retained execution contracts. The full replay
`scripts/heat/l938-two-bound-endpoint-73-replay-75.json` equals the
original report, including all check entries and hashes.

Every flag of the preserved first-pass failure report was inspected
programmatically: both actual sign tests passed and the sole failed
test was the reporting bracket 200<(-c_16)/b_H(4)<300. Its falsity
is independently reproduced, and the original producer comparison
shows only output-path/reporting-bracket changes. No failed test is
removed or promoted into sign evidence. The audit's separate initial
check-count error is preserved as described in L944.

This validates the existing singleton conclusion, not a new crossing
or sign discovery. At E=4 the negative derivative is compatible with
the strictly positive value, so it does not refute upward crossing
at zeros. Compact coverage and the independent main-goal gaps remain.

## Mathlib

Full and supporting Mathlib coverage of this exact enclosure and
certificate is unchecked; absence is not asserted. The cited DLMF
identities support the analytic and beta calculations. Integer-program
and Decimal/exponential execution trust remains informal.
