# L162 independent critical audit — completed scope comparison

TARGET: Critically audit L162's explicit four-row infinite family, including original-label eligibility, all parameter values, exact ranks, and injectivity over the algebraic closure of F_97.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 498's exact finiteness searches and duplicate/failure comparison; read L162 completely for source requirements, L109's map and kernel passages, ATTEMPTS/052, history/503 and the step-494/496 arbitrary-field applicability records. No new external search or mathematical audit was performed.
SOURCE_EVIDENCE: Reuse inspected Kostrikin–Manin, Linear Algebra and Geometry, Gordon and Breach 1997 paperback, Chapter 1 Theorem 3.12 pp. 20–21 and sections 6.2–6.9 pp. 44–46; projective tools in Chapter 3 sections 6.2–6.4 pp. 222–226, 6.8–6.10 pp. 227–228, 8.1 p. 233 and 8.10 pp. 239–240. Step 494 additionally inspected the publisher's 1989/2010 preview, Chapter 1 sections 1.1–1.2 and 3.11–3.13 including the proof of Theorem 3.12; no primary passage was freshly retrieved here.
COMPARISON: These arbitrary-field tools cover finite-dimensional kernels, linear identities, nonzero minors and projective normalization, but do not certify L162's original labels, matrices, vectors or injective family. L158's three finite loci and L115's family on a different support domain do not settle this audit. L159–L161 and their classification are discovery context, not premises.
GAP: Independently verify the displayed local specialization: original-label eligibility, product-defined matrices, both coefficient-vector identities, pair-kernel disjointness, exact ranks and injectivity for every projective parameter. Source approval does not establish any of these claims.
REASON: The saved arbitrary-field coverage suffices for one bounded first critical audit of L162 without new classification inputs; direct local verification is necessary because the sources contain no matching explicit quadruple or family.
LITERATURE_REASON: The newly written L162 audit had a REVIEW_REQUIRED target; this separate turn compares its exact obligations with existing source coverage rather than repeating source discovery or auditing the construction.
SCOPE: L162 as written over E equal to the algebraic closure of F_97, using precisely L109's original quotient-map formula and the four displayed original labels (35,522,477,566); field-valued planes only, with no coding, descent or scheme-theoretic conclusion.

## Reused primary coverage and qualifications

The exact reading/version record is in
`drafts/literature/2026-10-25-two-additional-row-factor-compatibility-review.md`,
with the prior audit applicability comparison in
`drafts/literature/2026-10-25-l157-critical-audit-review.md`.
The [primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf)
and [publisher preview](https://api.pageplace.de/preview/DT0400.9781466593480_A38306675/preview-9781466593480_A38306675.pdf)
have the versions and locators recorded above. The preview confirms only
its inspected Chapter 1 material; later projective coverage is reused
from the earlier full-book reading, not inferred from the preview.

The tools permit characteristic 97 and extension fields. The audit must
justify extension of each nonzero base-field minor and each linear
identity; it must not infer all-parameter validity from finite samples.
Projectivization identifies nonzero scalar multiples; zero vectors and
rank-zero restrictions must be excluded by the actual linear argument.
The book's projection constructions requiring nonzero summands do not
justify dropping singular cases. No general theorem needs reproof.
The elementary algebraic-closure infinitude argument in L162 is an
applicability check of the definition, not a classification input.
Matching Mathlib coverage remains not checked; unknown is not absence.

Step 498's inspected Sottile and Breiding–Rydell–Shehu–Torres passages
are comparison material only. Generic incidence or complex-field results
are unnecessary here. The inaccessible Medina–Zavadskij classification
remains unread and parked; the audit does not depend on it.

## Duplicate/failure comparison and approved bounded test

The reused step-498 comparison distinguishes selected finite loci from
universal finiteness and L115's family from the two-disjoint-pairs domain.
ATTEMPTS/052 records the explicit counterfamily mechanism; its conclusion
still awaits the independent audit. Earlier stops of rank stratification
and repeated passed-input audits do not prohibit this first audit of a
new construction. No prior certificate, input audit or census was replayed.
No source-level novelty claim follows from this scope approval.

Essential inputs are L109's map definition and L162's complete proof.
Reproduction artifacts are `scripts/seven-coordinate/residual_pencil_family.py`
and `scripts/seven-coordinate/residual-pencil-family.json`. The later
research audit should independently reconstruct the four maps from their
products, label ordering and all six support intersections. Check both
coefficient-vector identities and the two stated nonzero seven-by-seven
minors without relying solely on the producer's success flag. The full
sixteen-by-fourteen elimination and singleton discovery certificate are
not required premises and need not be audited as classification claims.

Then check nonzero X and Y, their independence, all four exact ranks,
the distinct kernel-intersection lines and every use of 26. Check
projective well-definedness and injectivity, including r=0 and s=0,
without parameter sampling or a genericity restriction. Inspect complete
load-bearing evidence if a certificate is used; a preview is insufficient.

Pass threshold: an independently checked family on the exact stated
domain, covering every projective parameter and rank-zero case. A defect
requires a precise correction or preserved failed argument; never silently
narrow the domain. Successful audit would justify stopping unconditional
four-row finiteness on this domain and motivate a separately assessed
additional-row or coding constraint. It would supply no twelve-row or
coding counterexample. Second-pair extraction, twelve-row compatibility,
all weights/chart gates, coding realization, representation, challenge
identification and sharp radius remain unresolved. Do not expand this
single audit into an all-label enumeration or unrelated input reviews.

This completed scope approval supersedes the original REVIEW_REQUIRED
proposal. The mathematical audit itself has not been performed.
