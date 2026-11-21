# L842 independent audit — work in progress

Exact approved target: Independently audit L842's rank-five negative second-ray certificate for the dyadic cubic product, including analytic scope, coefficient recurrences and determinant orientation.

Ready source assessment: `drafts/literature/2026-11-06-l842-negative-second-ray-audit.md` (SPECIALIZE, supplied at invocation). Classification REPRODUCTION. Main gap remains L030–L032/C032a actual-Xi mixed positivity. Only the analytic setup of L841 is used; its first-ray sign and L840 are not premises.

Initial analytic check: summable compact deviations give the entire compact limit, F(0)=1, and self-similarity. Continuity gives a small reciprocal disk with positive minimum modulus; compact convergence makes the finite reciprocals converge uniformly there. Cauchy gives fixed coefficient convergence. No global zero exclusion or uniformity in rank is needed. Macdonald's partition (r,r), conjugate (2^r), gives precisely the stated ordinary-coefficient determinant and h_r^2-h_(r-1)h_(r+1).

Completed: independent coefficients from Newton power sums, reciprocal inversion, both displayed recurrence residuals, exact elimination, and exhaustive inspection of all 153 stored permutation terms (120 at rank five). All 200 checks pass; the generator reproduces the retained certificate byte for byte. The full analytic and arithmetic reasoning is now canonical in L842; complete evidence is `scripts/dyadic-cubic/second-ray-independent-audit.json`. The actual determinant is -1409024/2966607, below the required zero bound. This independently validates this exact model's all-shift stop. No new model or Xi transfer was attempted.
