# Full mixed-distance factors — bounded enclosure implementation proposal

TARGET: Attempt one certified Krawczyk enclosure of L111's full 64-factor contraction system and test the enclosed root's x_5^3<=c_5 capacity.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed theorem-level comparison in drafts/literature/2026-10-23-positive-factor-interval-capacity.md; this is its concrete enclosed-root implementation target, with the same fixed hypotheses and no global-uniqueness or full-feasibility extension.
SOURCE_EVIDENCE: Rump (2010), DOI 10.1017/S096249291000005X, corrected author PDF https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf , Theorem 13.3 and full proof author p.89, Algorithm 13.4 pp.89–90 and §5.3–5.5 pp.27–28, as recorded in foundations/14-validated-nonlinear-enclosure-source.md; reuse audited L111 and foundations/04,12,13.
COMPARISON: The standard theorem covers a sufficient strict local inclusion test; the new work is exact orbit reconstruction, a finite positive candidate box, a complete polynomial Jacobian enclosure and a single actual capacity comparison. No reproof of the enclosure theorem or global uniqueness is needed for this restricted verdict.
GAP: No candidate, interval box, residual/Jacobian certificate or distance-5 verdict exists yet. Local inclusion may fail even though L111 proves positive-factor existence. All other capacities and stronger moment/RS conditions remain unresolved.
REASON: A known theorem now supports a materially different bounded capacity test using every mixed-distance contraction, rather than L110's equilateral-only allowance or ATTEMPTS/082's full-variable prescription; this newly saved target requires separate approval next turn.

SCOPE: Exactly TARGET, using L021,L098,L109,L110,L111 and foundations/04,12,13,14; one candidate trajectory and one exact enclosure attempt, with no ansatz-wide rejection, enlarged system, precision/radius scan or full-variable solve.

## Contract for a later approved mathematical turn

Keep N=floor(65537^28/2^128)+1 and all 64 original equations (7),
positive x_i for 5<=i<=68, every actual D and t-s class, null edges,
both repetitions and the coincident row. Reconstruct exact rational
c_i from the existing L021/L098 input. A compressed coefficient array
is acceptable only with a full original-orbit reconstruction check.
Different source orbits remain distinct outside this product ansatz.

Before computation, save the chosen initial positive point, fixed
precision, iteration cap (at most 100 damped Newton iterations), step
halving cap (at most 20 per iteration), and deterministic box rule in
the working record. Use one trajectory only; unvalidated approximations
are proposals. Then choose one finite positive rational box and one
rational preconditioner and evaluate the residual, full polynomial
Jacobian enclosure and Krawczyk inclusion with exact rational endpoints.
Use the original x coordinates, or an explicitly invertible rational
diagonal rescaling checked back against all original equations. Do not
introduce an unassessed logarithmic residual, gauge or deleted equation.
If candidate construction fails, report that failure without a retry.
If exact verification exceeds its predeclared execution budget, preserve
all artifacts and label the enclosure incomplete.

Save full coefficients, candidate/preconditioner, box, residual and
Jacobian bounds, all 64 strict inclusion margins and the exact capacity
comparison to disk. An independent checker must reconstruct the
original sums, derivatives and every interval operation; selected
previews or a numerical residual are not verification. Console output
should give pass/failure, achieved versus required strict bounds and
certificate paths. No mathematical script is written in step 419.

Continue on this bounded test only if strict inclusion and positivity
are certified. An upper cube <=c_5 passes this capacity only; a lower
cube >c_5 rejects this enclosed weighting only. A straddling box,
failed inclusion, failed candidate or unfinished check is inconclusive.
No global-factor uniqueness or exhaustive positive-root coverage is
assumed. A pass leaves all other capacities, Boolean lower rows, full
source feasibility, PSD, RS realization and arbitrary-center safety at
67/68 agreements unresolved. Preserve L110/ATTEMPTS/093 and ATTEMPTS/082;
the bracket is 955–957. Full Mathlib coverage is not checked.
