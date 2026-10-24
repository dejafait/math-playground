# Step 420 — bounded full-factor enclosure working record

The main gap is arbitrary-center 67/68-agreement safety; this route's
intermediate gap is L098's shared capacitated-triangle feasibility.
Approved target: Attempt one certified Krawczyk enclosure of L111's full 64-factor contraction system and test the enclosed root's x_5^3<=c_5 capacity.
Use the supplied prior SPECIALIZE assessment unchanged. L110/ATTEMPTS/093
stop only the equilateral allowance; ATTEMPTS/082 stops a distinct full-variable
prescription. L111's audited existence is available, without uniqueness.

Predeclared before computation: use Decimal precision 90 digits, initial
x_i=c_i*K where K is the positive integer floor cube root of H/(N-1).
Use rational diagonal scales s_i=10^floor(log10(x_i(initial))), with
u_i=x_i/s_i; the initial u is exactly c_i*K/s_i. Normalize each original
polynomial by its positive d_i=(N-2)c_i, without deleting equations.
One damped Newton trajectory, at most 100 iterations, at most 20 halvings
per iteration; require positivity and strict decrease in maximum absolute
normalized residual. Stop on residual <10^-65; candidate failure has no retry.
Round the final u and its numerical inverse Jacobian to denominator 10^70.
One box only: uniform u-radius 10^-45. Use integer endpoints with common
unit 10^-70 and outward-rounded addition/multiplication; the resulting
endpoints are exact rationals. One preconditioner only. Candidate budget
300 seconds; exact enclosure budget 180 seconds; independent verification
budget 300 seconds. Preserve incomplete certificates if a budget expires.
No precision/radius scan, logarithmic residual, gauge or removed equation.

The full compressed coefficients are the exact integer sums of D for each
fixed i and unordered (j,h), together with exact s_i and d_i. This lossless
polynomial representation is checked against a separate full four-region
enumeration, including six presentations, t-s, repetitions and null cases.
Krawczyk evaluation uses the full residual and derivative enclosure, all
64 margins, and saves each interval operation's resulting vector/matrix.
The checker reconstructs these independently. Continue only on strict
inclusion and positivity; compare the enclosed x_5 lower/upper cubes to
c_5 exactly. Failure/straddling is inconclusive; a capacity rejection affects
only this enclosed root. Other capacities, Boolean lower rows, source/PSD
feasibility, RS realization and the 955–957 bracket remain unresolved.

Mathlib: full matching enclosure application and implementation not checked.

Completed: the sole trajectory converged after four iterations (residual
2.2885387945285232602627134e-68 against 1e-65). The sole exact box has
all 64 strict inclusion margins positive. Full independent reconstruction
checks all 1,500,625 original orbits, 81,355 aggregated monomials and every
residual/Jacobian/interval operation: 4,100,192 checks, zero failures.
The enclosed root passes x_5^3<c_5; its ratio is about 1.071789e-11.
Canonical proof and exact artifact paths are in L112. No other capacity
was tested. The next all-capacity proposal is REVIEW_REQUIRED, preserving
the original single-capacity cap and all remaining qualifications.
