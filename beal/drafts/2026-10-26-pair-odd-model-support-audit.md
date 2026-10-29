# L138 critical audit working record

The prior SPECIALIZE contract is
`literature/2026-10-25-pair-odd-model-support-audit.md`. Exactly its fixed
audit is being performed; no new descent or rank calculation is authorized
by that contract. Main gap: the residual primitive Beal signatures.
Intermediate target: accept or correct L138's actual model, field, order,
discriminant and support interface for subsequent Jacobian descent.
Stop dependent use on the first substantive failure. Units, local images,
rank, points and the original recovery problems remain independent gaps.

Initial review: read L138 completely, the relevant L110 maps and proper
charts, L133's field identification, L134's full maximal-order statement
and lattice proof, and L137's ordinary-localization argument. Read both
complete implementations. Reused source coverage; ATTEMPTS/050,059–060
and history/491,493 confirm that this audit duplicates neither a completed
critical audit nor an exhausted point/relation search.

Before computation: the printed exceptional charts are consistent with
the affine inverse functions. The field maps and complete basis matrices
are consistent in direction; maximality is transported through the field
isomorphism, not inferred from a polynomial discriminant. No mathematical
failure identified yet. Remaining checks: bind every printed numeric
object to full replay evidence, inspect whole discriminant factorizations
and cofactor proofs, and check source hypotheses and class-group direction.

Fixed test: preserve the previous replay, execute it once, then supplement
its complete arithmetic checks with canonical literal binding and exact
exceptional-chart identities. Maximum polynomial degree 12, matrix size
12 and rational bits 4096 are the existing bounds. No search expansion,
upstream arithmetic rerun, unit computation or backend probe is planned.

Completed: the full replay passes 82 checks and exactly matches its
preserved prior output. The supplement passes 30 checks with no failure;
it binds canonical numeric objects and verifies both complete exceptional
chart identities. The separate audit, mathematical justification, precise
source applications, evidence paths and actual/cap bounds are canonical
in L138. No correction or new dependency was needed. The accepted result
is the descent interface only. No rank or Selmer bound was obtained.

A proposed S-unit/class dimension-bound continuation is recorded in a
separate REVIEW_REQUIRED assessment. This step does not derive or approve
that new target. The pre-existing overview and DAG are unchanged.
