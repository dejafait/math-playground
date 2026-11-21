# Fourth-order large-smoothing attempt — step399

Approved scope: the unchanged COVERED_TARGET in
`drafts/literature/2026-11-04-fourth-order-large-smoothing-comparison-review.md`.
This is a research proof attempt, using its pre-existing EXPLORE coverage.
No new source assessment is approved in this turn.

Main gap: actual-Xi all-degree positivity. Seek an explicit M4>=7 with
positive full-B S_(4,m) and complete-K relative determinant error<1/2
for every integer m>=M4 and every u>=0. This could supply uniform
fixed-order smoothing control; general order and exceptional coefficient
transfer remain independent gaps. Continue on an effective signed lower
bound plus paid uniform perturbation. An isolated onset failure does not
reject eventual comparison; unpaid regimes require a refined next input.

Prior coverage and stops: step398 and the step391–393 assessments are
reused. Nuttall's pure-exponential Conrey–Ghosh induction does not transfer
to full B by citation. L767/L768 are audited only at r=3,m=5; their
entry expansions do not supply constants uniform in m. L019 supplies
the exact kernels and decay. No certificate replay is needed for that
normalization-only use. No cross-notebook inputs.

Unfinished plan, saved before calculation: integrate by parts to express
S_(4,m) using a determinant of B derivatives at four integration points.
Factor that polynomial determinant exactly, including its possibly
negative region. Only then test whether smoothing suppresses that region
and whether the full theta perturbation can be compared without losing
the Vandermonde cancellation. No sign or uniform estimate is assumed.

Completed: L769 proves an exact four-point integral and the uniform
base lower bound S_(4,m)(B;u)>(19/72)S_(4,m)(F_0;u)>0 for m>=7,u>=0.
The apparent possible negative region disappears after the exact shift
x_j=y_j+3: all coefficients of P are positive, and those of
P-(19/72)prod x_j are nonnegative with a strictly positive constant.
The proof and its precise known-method attribution are canonical in
`lemmas/L769-fourth-order-full-base-signed-integral.md`. This is an
unaudited local quantitative specialization, not a new mechanism or
an RH candidate. Only L019 is a direct mathematical input.

The exact rational coefficient check is
`scripts/cumulant-comparison/fourth-order-polynomial-399.json`.
Its complete load-bearing difference coefficients were inspected;
the sample evaluation alone is not the polynomial proof. A small
confluent local diagnostic, explicitly noncertified, is saved separately
as `scripts/cumulant-comparison/fourth-order-local-diagnostic-399.json`.
It encloses neither rounding nor the omitted tail and proves no bound.
The attempted optional sympy import was unavailable; the coefficient
check uses standard-library rational arithmetic instead.

Why the full target remains open: L769(7)–(8) retain every theta
summand and give the exact remaining signed error integral. No bound
for that numerator relative to the positive reference integral has
been proved. In particular mixed small/large four-point configurations
and their moving m-dependent weight have not been controlled. Scalar
tail positivity and the local diagnostic cannot pay this cancellation.

Refined continuation on the unchanged approved target: use L769's
positive base and exact E integral to bound the complete signed
perturbation, splitting configurations only with paid uniform errors.
A sufficient numerator threshold is (19/144) times the positive
reference integral; it is sufficient, not asserted necessary. An
explicit M4 must handle every larger integer m and every u>=0.
This new signed base is material input permitting one development
continuation. No general-order or exceptional-coefficient transfer
is supplied, and no independently justified creative mechanism was
found within this focused attempt. Reuse the unchanged assessment;
do not create a new ready literature assessment in this turn.
