# Uniform low-time H1 certificate attempt (step180)

The approved target is the exact TARGET in
`drafts/literature/2026-11-09-low-time-h1-uniform-moment-test.md`.
Reuse that EXPLORE assessment; no additional browsing is needed.
Main gap: L030–L032/C032a all-degree actual-Xi mixed positivity.
Intermediate target: strict S2 and det H1 on [0,1/20]. Its use would
be exclusion of degree-one contacts, not a contact sign or RH.
Continue only if every closed panel has strictly positive lower
endpoints; otherwise stop this fixed certificate and retain failures.

## Saved reasoning before computation

Inputs read: L019, L033, L035–L038, L058, L874 and the existing
`scripts/hankel/certify_hankel.py`. No previous files are overwritten.
The source comparison in the prepared assessment already checked the
exact target; L038 certifies only lambda=0. Historical pilot retirement
and blocked GHS sources are retained; this calculation does not use them.

Let M_k(lambda)=integral_0^infinity u^k exp(lambda u^2)K(u)du,
k=0,2,4,6,8. L058 justifies extraction of the cosine coefficients and
M0>0 for real lambda. Thus L033's finite logarithm algebra remains
valid at every real lambda, with a=M2/(2M0), b=M4/(24M0),
c=M6/(720M0), d=M8/(40320M0). No deformed real-zero product or
zero ordering is assumed. The S2 sign must be certified again.

For an explicit tilted tail, put X=exp(2u) and beta=119/40.
The exponential series implies X>=2u^2 for u>=0, so
lambda*u^2<=X/40<=n^2 X/40 throughout [0,1/20]. The same
positive-kernel argument as L035 gives

    u^k exp(lambda*u^2)K(u) <= 256 exp(25u/2) exp(-beta X).

Here u^k<=exp(8u), pi<4, pi>3, and the original untilted sum is
bounded by 2exp(-pi X) using n^4<=16^(n-1),
n^2>=1+3(n-1), and 16exp(-3pi X)<1/2.
After X substitution the tail beyond u=2 is at most

    128 integral_50^infinity X^6 exp(-beta X)dX
    =128 exp(-50beta) sum_(j=0)^6
          [6!/(6-j)!] 50^(6-j)/beta^(j+1).

This uses exp(4)>50, proved by its positive series, and
X^(21/4)<=X^6 on X>=1. For omitted n>=5, integrate over all u>=0:

    omitted <=64*720 sum_(n>=5) n^4 exp(1-beta*n^2)
            <=57,600,000 exp(1-25beta).

Indeed exp(-beta*n^2 X)<=exp(1-beta*n^2)exp(-X) for X>=1;
the gamma integral of X^6 is 720. Write n=5+j, use
n^4<=625*16^j and n^2>=25+11j. Since
16exp(-11beta)<1/2 (beta>2, exp(22)>32 by its positive
series), the geometric sum is <=2. Both discarded contributions
are nonnegative; their sum E_tilt is a valid common upper error for
all five moments, uniformly over the full closed parameter interval.

Use the unchanged L037 arithmetic implementation at precision 100.
Cache untilted midpoint and full-spatial-panel jets and multiply by
the normalized derivative jet of exp(lambda*u^2). The latter has
exponent coefficients lambda*u^2, 2lambda*u, lambda, then zeros;
the L036 recurrence encloses all derivatives on full lambda panels.
Use 256 closed equal parameter panels and 64 closed spatial panels,
four theta terms, Taylor coefficients through 6 and an eighth-derivative
remainder. Add [0,E_tilt], normalize, then evaluate L033's polynomials.
Retain all panel moment, remainder, S2/S3/S4 and determinant intervals.
This is a computer-assisted attempt under the Decimal contracts,
not an independent validation of the Python arithmetic library.

Completed: all 256 closed panels certify strict signs. The full proof
is canonical in L914; all moment/tail/determinant enclosures are in
`scripts/heat/low-time-h1-uniform-180.json`, and the complete exact-rational
moment-algebra replay is in `scripts/heat/low-time-h1-uniform-180-check.json`.
Both runs completed without failures. Uniform thresholds are
S2>3.714e-5 and det H1>9.7e-16 under L037's contracts. Independent
proof audit remains pending; Mathlib coverage is not checked.
Higher degrees, initialization/tangency and degree-uniform continuation
remain open. No degree-one contact residual was searched.
