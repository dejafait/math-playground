# Boundary-supported metric: finite test scope2009

TARGET: Test whether the symmetrically scaled comrade of Kuznetsov's exact full T_6 admits a nonsingular metric G=I+e_1 z^T+z e_1^T with A^T G=GA and negative index at most one, or certify an obstruction to this ansatz.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed structured-matrix discovery2009 in assessment2008 inspected primary hypotheses and narrowly checked local duplicates/failures; no matching actual-family boundary-metric theorem was established. Reuse that comparison; no originality claim.
SOURCE_EVIDENCE: Full primary citations and inspected proof cases are in drafts/literature/2026-11-20-tilted-xi-structured-matrix-discovery-2008.md: arXiv:1912.04157v2 Definition2.1/Theorem2.2/Section2.2; https://files.ele-math.com/articles/oam-05-49.pdf Sections2.2–2.3/Lemma2.2; https://www.cs.mcgill.ca/~chris/pub/PaiSWZ08.pdf Section2(8)–(16); Kuznetsov https://doi.org/10.4153/CMB-2008-055-0 exact coefficients/recurrence/weights as extracted in review2001 and C029m.
COMPARISON: Known linearization, finite positive-recurrence scaling and metric root-count/inertia machinery cover the interface; they do not solve the proposed constrained metric equations for these coefficients. The boundary ansatz is an unproved choice motivated by the one-row comrade correction, distinct from generic preservation and common-measure claims.
GAP: Determine exact feasibility and nonsingularity at N=6; eventual uniform metrics remain independent and entirely unproved.
REASON: One bounded actual-coefficient test can retain or reject a concrete metric mechanism without the parked Arb runtime. New mathematical work is confined to this finite ansatz, not reproduction of known general matrix theorems.
SCOPE: Single N=6 proof attempt, exact full coefficients, no degree escalation, no runtime discovery, no common orthogonality or automatic rank-one root-count premise. Newly written scope awaits separate supervisor approval; no mathematical test was performed in the literature turn.

## Exact test and permitted difference

Use C029m's full Jensen-weighted T_N at N=6, with all beta_0,...,beta_6
and exact source u_n through u_8. Do not replace it by an even polynomial
or a fitted/rounded coefficient family. First determine its actual degree;
if it is not six, report that finding rather than silently applying
six-dimensional formulas. Review2001's source formulas are reusable;
its Arb implementation is not a prerequisite for this analytic test.

Use the descending-basis, **left-metric** convention of Noferini et al.
Definition2.1. After normalizing by the nonzero top basis coefficient,
form C from that definition. Obtain a positive diagonal D so the basis
part of A=D^(-1) C D is symmetric; fix its otherwise arbitrary common
scale by D's last diagonal entry=1. Verify this finite identity directly
from the exact Pollaczek recurrence; do not assume the compact-support
orthonormality premise in the opening of that paper's Section2.2.
These normalization checks are part of the attempt, not supplied results.

With e_1 at the coefficient-correction row, seek real z in

    G=I+e_1 z^T+z e_1^T,     A^T G=GA.

This is a proposed constrained metric, not an asserted representation.
Keep the complete exact linear compatibility system or an equivalent
elimination certificate. A solution must also be real, nonsingular and
have at most one negative eigenvalue; use the cited Schur-inertia
identity with the identity bulk and verify all its premises. Every
cleared denominator must be proved nonzero. Exact symbolic compatibility
may be tested before any transcendental evaluation. Any elementary
coefficient inequalities or finite enclosures used must have full proofs,
including error bounds; floating point residuals are not certificates.
If a different non-elementary theorem or unassessed algorithm becomes
essential, save the unresolved algebra and route to its source review.
No package installation, API access or unchanged Arb retry is authorized.

Continue only after an exact feasible nonsingular metric and its inertia
are certified. The plausible next use would be to look for a uniform
formula from the actual coefficients. An incompatible equation system,
or proof that every feasible metric is singular, stops this ansatz.
Unresolved signs are inconclusive. N=6 failure alone says nothing about
an eventual-only variant unless its obstruction is shown to persist;
no such extension is part of this target. Do not broaden to other
bandwidths, degrees, metrics or a precision campaign within this attempt.

## Inputs, limitations and purpose

Essential inputs: C029m/C029l for the conditional downstream use;
Kuznetsov recurrence(2), coefficients(4)/(13) and weights pp568–569;
review2001 for exact-family source extraction; assessment2008's completed
matrix-source comparison. C029m's compact-limit upstream[9] qualification
persists. No actual metric feasibility, degree, simplicity or index is
assumed. The Pontryagin interface allows repeated eigenvalues but needs
nonsingular G; it bounds distinct nonreal locations, which is enough
for the C029l/C029m conditional route. A finite pass is not RH evidence
of uniform strength. All-degree mixed positivity remains open.

This is a proposed new boundary metric mechanism at the actual index
bottleneck, not a new general comrade theorem or a routine recalculation
of the published finite roots. A negative compatibility result would be
useful scope evidence; no lemma quota applies. Preserve L530/L955,
common-Favard and runtime/summability stops in their original scopes.
Mathlib coverage unchecked. No cross-notebook input is needed.
