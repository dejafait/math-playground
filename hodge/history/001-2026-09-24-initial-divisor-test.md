# 2026-09-24 — Primary statement and first divisor-product test

STEP_ID: 2026-09-24-hodge-001-primitive-diagonal.

The notebook was initially empty, with no local changes, prior lemmas, or failed attempts. Changes elsewhere in the repository were inspected through git status and left untouched. The [source audit](../foundations/01-target-and-scope.md) checked Clay's current page and Deligne's official rational formulation before the bounded test; [standard inputs](../foundations/02-standard-inputs.md) retain the named theorem citations. Mathlib coverage was not checked.

The chosen gap was the primitive rational (2,2) part of fourfold cohomology. [L001](../lemmas/L001-low-dimensional-boundary.md) records the standard dimension boundary and exact reduction. The [saved assessment](../drafts/2026-09-24-initial-divisor-test.md) compared divisor products, correspondences, and variation in families. Divisor generation was selected because the primitive diagonal on a quartic self-product gives an immediate exact test.

The test returned an informative negative result: [L002](../lemmas/L002-primitive-diagonal-outside-divisor-products.md) exhibits a primitive algebraic class outside all divisor products. [Attempt 001](../ATTEMPTS/001-divisor-products.md) records why this mechanism fails. The achieved result is strict containment of the divisor-product span, whereas the required threshold is algebraic realization of every rational primitive class on every fourfold, and ultimately every X and p. No part of that missing surjectivity is claimed solved by this example.

The reason for changing direction is mathematical: correspondences already realize an action on H^(2,0) that divisor products cannot. Determining the residual classes after adjoining the diagonal is a bounded way to distinguish further correspondence needs from already accounted-for cycles. No unresolved exploration turns are carried forward (0 used); the result is classified NEGATIVE rather than a conjecture advance.

The proofs were checked for rationality, divisor splitting, degree shifts, the primitive correction coefficient, and the diagonal action. L001 and L002 use only named standard inputs and neither uses the other as a mathematical premise, so both DAG rows have empty right sides.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge` passed with 2 nodes, 0 edges, valid links, and compact overviews. Bytecode writing was disabled to keep shared infrastructure read-only. The initial check mistook plain-text correspondence notation for a Markdown link; standard math notation fixed it without changing the proof or checker. `git diff --check -- .` also passed. No numerical experiment is needed for this exact cohomological calculation.
