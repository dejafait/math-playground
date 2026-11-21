# Convex blend of finite-product and Robin weights: signed obstruction

The bounded test is recorded canonically in
[C681c](../lemmas/C681c-positive-blend-signed-saddle-obstruction.md),
with its exact scalar certificate under `scripts/one-sided-hankel/`.
Its separate conceptual audit is recorded in C681c Section 7 (step 73).

WHY IT FAILS: the full residual at angular point -1 retains a contribution
with the same sign for both constructions. Each right contour has a
negative signed leading integral; its complementary edges are exponentially
smaller. Every convex blend therefore preserves a polynomial times
exp(-121*n/13000) lower bound, and the exact rational quadrature pays
only a polynomial cost to reach continuous L2. C681c gives the eventual
lower bound exp(-19*n/2000), which rules out the required rate above
1/100 for these blends, even with n-dependent mixing. This does not stop
arbitrary positive weights. It is a signed-integral obstruction, unlike
the preserved fixed-rectangle stop and the finite four-size diagnostic.

The step-73 audit verified the uniform signed limit, complementary edges,
finite-product errors and enlarged-pole point-to-norm specialization;
all scalar evidence replayed without failures. Reopening this blend
requires a material defect in that proof or genuinely changed weights;
fitting another mixing coefficient is not a new mechanism. The source
manuscript qualifications and existential onset in C681c are retained.
