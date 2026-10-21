# Degree-36 maximal-field discriminant lower-bound attempt

Approved target: certify a maximal-field discriminant lower bound for
L051's degree-36 field and test its true Minkowski cutoff against 10^6.
The saved SPECIALIZE assessment covers the Newton polygon, local
different, completion and tower inputs. No new source mechanism is used.

Completed exact arithmetic: m(U) at 3 and m(V+3) at 11 both have
ascending Newton vertices (0,1),(11,0),(12,0). The length-eleven
segment yields one degree-eleven totally ramified field, and the
remaining degree is one. Denominator eleven in the root valuation
forces the degree-eleven block to be irreducible. At 3 its different
exponent is 10 (tame); at 11 it is at least 11 (wild). L051 gives
[L96:K96]=3, so the maximal discriminant tower formula implies
3^30*11^33 divides Delta_L96. This already passes the uniform lower
comparison using 36!/36^36 and 4/pi>1, independently of signature.

Canonical proof: L052, with full coefficient, factor-coverage and tower
arguments. The full certificate is
`scripts/ninety-six-class-generation/discriminant-lower-bound-certificate.json`;
its complete local and cutoff fields were inspected. The uniform lower
comparison lies strictly between 7646157636 and 7646157637, so the true
Minkowski cutoff exceeds 10^6. Exact script checks pass. Direct input:
L051; the other inputs are precisely cited standard theorems. Independent
critical audit remains pending. This is a routing obstruction only.
Class/unit/Selmer completeness, global
emptiness of 96a1 and the other L032 branches, and arbitrary residual
signatures remain unresolved. Preserve ATTEMPTS/018 and unfinished work;
park enumeration at the true Minkowski cutoff as well. A large sufficient
cutoff is not a lower bound on necessary class-group complexity.
