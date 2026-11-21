# All-order full-base comparison — working step403

The approved target is exactly the COVERED_TARGET in
`literature/2026-11-04-all-order-full-base-localization-review.md`.
That EXPLORE assessment predates this invocation; no new literature
gate is being approved here. The main gap is actual-Xi all-degree
positivity. Eventual finite-order smoothing would be a useful input,
but exceptional-index transfer remains independent.

Read L019 and the full audited L769/L770 proofs, including step401's
qualifications. Reused the step391/392 transfer stops and step402's
primary-source comparison. No unsmoothed source conjecture, numerical
beta-root pattern or different-kernel theorem is an input. Existing
notebook changes are preserved.

## Partial reasoning saved before further development

For arbitrary r put d=r(r-1)/2, p=m-r, T=x*d/dx-x,
q_j=T^j(x-3/2), and h_j(y)=y^r q_j(1/y). The signed cumulant
integral should equal a positive leading-term reference integral
times the expectation of G_B=det[h_j(y_l)]/Delta(y), y_l=1/x_l.
Both parity factors must be retained; r=4 hid them. Each h_j has
degree at most r, coefficient norm at most 3*r!, and its least
degree is r-j-1 with coefficient (-1)^j. The confluent divided-
difference matrix at zero therefore has determinant one.

Candidate explicit bounds: H=3*2^r*r!, C=r!*H^r. Newton divided
differences on [0,1/3] give |G_B|<=C; telescoping the determinant
against its value at zero suggests |G_B-1|<=r^2*C*max(y_l).
Thus sufficiently high coordinates can be signed without a new
closed-form beta polynomial. This does not yet pay the signed low
region. No general theorem is claimed at this checkpoint.

Next within this single attempt: prove an arbitrary-order C^(r-1)
bound on the complete-theta remainder in reciprocal coordinates;
then generalize L770's free-interval conditional argument using r
intervals against r-1 conditioning points. If both costs are explicit,
choose A(r) and M(r) jointly. Stop if any low, mixed, confluent or
unbounded-height regime is unpaid. No finite grid is a substitute.

Only L019 is an essential kernel input so far; L769/L770 are audited
method precedent. No new result is ready for critical acceptance.

## Completed development

The full argument is now canonical in L771. It supplies explicit
integer constants A(r), M(r), a base/reference lower factor 11/16,
and a complete-K relative error below 2/11<1/2. The low region is
retained with its possibly negative sign and paid by the reference
probability; reciprocal divided differences pay coalescence at every
order. The proof requires separate conceptual audit and implies no
exceptional coefficient transfer or RH resolution.

A preliminary sharper choice used A>=max(4r^2*C,
(4/3)*log(R*F_*)+1) and a logarithmic formula for the m cutoff.
For an unambiguous integer-only threshold the final proof instead
uses A=4r^2*C+4R*F_* and q^p<=exp(-p/(2A)), then absorbs the
remaining logarithms by log P<=P and exp V>V. This deliberately
sacrifices numerical size; it does not change the target or add a
new assumption. Full constants and reasoning belong in L771.

The exact finite normalization check at r=2,...,7 passed 30 checks;
it is only a parity/reciprocal/confluent consistency check. Its
certificate is `scripts/cumulant-comparison/all-order-normalization-403.json`.
It neither verifies the infinite quantifiers nor supplies the later
independent audit. No mathematical failure or unpaid height regime
remained in this proof attempt, subject to that review.
