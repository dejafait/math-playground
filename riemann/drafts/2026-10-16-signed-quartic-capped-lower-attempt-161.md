# Step 161: saved two-scale counterlaw attempt

The preexisting EXPLORE assessment is
`drafts/literature/2026-10-16-signed-quartic-capped-cubic-lower-bound.md`.
The exact approved lower implication is being tested, not the actual
capped statistic or RH. Source coverage and prior failures are reused.

Candidate construction, pending complete checks: carry every actual
quartic at its original height using radius
max(ell^3, 2^(1/4) rho_actual), probability (rho_actual/radius)^4,
and sign chosen to make Delta Bcal nonnegative. Fiber mass is <=1/2;
the total cubic is O(ell). Reserve a second component of radius
ell^(3/2), oriented with Delta>0 and Bcal>0, and height-dependent
probability beta_* ell^2/(radius^3 Delta(n;t) Bcal(n;t)).
A uniform positive unit direction can be selected from the signed
vectors (2/3,+/-1/3,2/3); exact ell_F is negative and one Bcal
projection is bounded away from zero. This gives exactly the required
leading cubic, with second matrix O(sqrt(ell)) and quartics O(ell^(7/2)).

Adapt L419's bulk by subtracting the entire rare second matrix plus
the bulk mean outer product, rather than only two odd entries.
The covariance correction is O(sqrt(ell))=o(ell), so positive
definiteness and its strictly negative quadratic trace should survive.
The imported six-state construction then matches all six second
moments exactly and the first Bcal mean exactly. First Delta permits
o(ell), so this correction is within its tolerance. Must verify every
mass, envelope, exact curvature, all-real-H bound and capped integral.
The expected capped budgets are O(ell), O_lambda(ell^(3/2)), O_lambda(1)
for the high, intermediate and bulk components. No result is claimed
until the complete construction is written in the canonical lemma.

Completed: the checks and proof now reside in
`lemmas/L421-prescribed-response-vanishing-capped-cubic-counterlaw.md`.
The candidate construction above is retained as the saved work-in-progress
sketch, superseded by that full canonical argument. It refutes only the
selected-moment implication and awaits a separate critical audit.
