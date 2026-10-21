# Source coverage for the conditional signed-interval audit

TARGET: Critically audit L450 (19)--(22) as a conditional signed-interval obstruction, including the positive-measure conclusion, AC boundary terms and excursion constants, without assuming actual occurrence.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 297 compared the exact conditional target with L450 (19)--(22), L445's regularity, the width-one assessment and the prior forced-cross audit assessment; reused their inspected AC and matrix sources rather than searching again for elementary calculus.
SOURCE_EVIDENCE: Hunter, Notes on Partial Differential Equations (18 June 2014), Definition 3.1 pp. 47--48 and Theorems 3.60, 3.62--3.63 pp. 79--80; Bell, Sobolev spaces in one dimension and absolutely continuous functions (21 October 2015), section 1 Theorem 1; Boyd--Vandenberghe, Convex Optimization (2004, corrected seventh printing 2009), Appendix A.5.5 pp. 650--651, (A.13)--(A.14), via the inspected records below.
COMPARISON: AC fundamental theorem, product/integration-by-parts rules and scalar Schur complement cover the conditional test's general tools; the actual signed factors, constants, saturation cases and positive-measure inference require an independent mathematical audit.
GAP: Audit correctness of L450 (19)--(22), conditional on its stated earlier uniform remainder and positive-diagonal inputs; no actual excursion theorem is supplied or required for this audit.
REASON: Independent validation of the reusable conditional certificate remains testable after parking its unsupported actual-data application; no reproof of the general calculus or matrix theorems is justified.
SCOPE: Only L450 (19)--(22) for the unchanged width-one family, taking earlier L450 (1)--(6) and L449 (9)--(12) as explicit conditional inputs; no audit certification of all L449/L450, actual occurrence, changed law or width-one PSD verdict.
COVERED_TARGET: Critically audit L450 (19)--(22) as a conditional signed-interval obstruction, including the positive-measure conclusion, AC boundary terms and excursion constants, without assuming actual occurrence.
LITERATURE_REASON: The newly selected independent critical audit needs exact scope approval; it reuses ready calculus and matrix coverage, while avoiding any further search for the parked actual excursion.

## Reused inspected hypotheses

Use `drafts/literature/2026-10-20-width-one-endpoint-forced-cross.md`
and `drafts/literature/2026-10-20-endpoint-forced-cross-critical-audit.md`.
These records contain the inspected primary statements and proof cases.
[Hunter's notes](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf)
identify AC functions with integrals of L1 derivatives and justify the
fixed-interval calculus. [Bell's one-dimensional theorem](https://jordanbell.info/LaTeX/mathematics/sobolev1d/)
provides the AC representative for an L1 weak derivative.
The factors tau, x0, S, a and w are Lipschitz at each fixed H by L445
and L449; the audit must verify their use and every substitution,
including nonsmooth saturation points. No H derivative is allowed.

[Boyd--Vandenberghe, Appendix A.5.5](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=664)
gives the block Schur-complement criterion for positive A and its
singular qualification. Here L450 assumes strictly positive A,C,
so the scalar condition is |B_for|<=sqrt(A C). The audit must test
the centered cross after all rare and mean terms are subtracted.
It must justify why an integral excess excludes PSD on a set of
positive measure, rather than merely at an exceptional point.

## Relevance and discriminating test

The main gap is global mixed positivity. A correct conditional
failure certificate is an intermediate tool for examining the selected
law's temporal compatibility. The independent actual excursion input
is parked by the completed comparison in
`drafts/literature/2026-10-21-width-one-actual-excursion-input.md`.
Known maxima and moments must not be used as substitutes for it.

The audit should follow the entire signed calculation (19)--(22),
checking orientations, strict versus weak inequalities, AC integration
by parts, positivity/integrability of weights, constants, the onset's
dependence on c and every fixed-H hypothesis. Validate the certificate
only if its stated conclusion follows under exactly those hypotheses;
otherwise identify and correct or narrow the load-bearing claim.
This is a proof audit, not another attempt to derive an actual excess.

Essential inputs: L449 (9)--(12), L450 (1)--(6), (19)--(22), L445's
fixed-height smooth/AC interfaces, and the fixed family conventions
from L438/L443 already embodied in these formulas. Earlier remainder
estimates remain explicitly assumed inputs of this scoped audit;
validating this target alone must not label the full lemmas audited.
Independent unresolved assumptions include actual occurrence, remaining
endpoint and unsaturated layers, other occupation and mean identities,
inter-H realization, clipping and the full-error regulator margin.
No new lemma is requested. Mathlib matching coverage is unchecked;
unknown coverage is not an obstruction to this informal audit.

This assessment was written in a literature-only step. Its ready
continuation requires the supervisor's separate next-turn approval;
no mathematical audit was conducted while approving source scope.
