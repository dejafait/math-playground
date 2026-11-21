# Actual Jensen companion logarithmic regularization: reviewed1994

TARGET: Assess polynomial-scale singular-value regularization of the actual centered Jensen companion log determinant, identifying the small-singular-value estimates needed for a degree-uniform signed-window transfer and comparing the recorded companion-cost stops.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1994 searched deterministic Hermitization/logarithmic integrability, shifted companion singular values, replacement principles, noisy deterministic equivalence and Gram minor expansions; scoped C028*/C029*/companion records contain no matching fixed-minor regularization test. Queries and inspected ranges: drafts/literature/2026-11-20-companion-regularization-source-notes-1994.md
SOURCE_EVIDENCE: Bordenave-Chafai1109.3343v4 (4.7), Lemmas4.3/4.5 and proofs; Tao-Vu0807.4898v5 Theorem2.1/(9)-(11), Lemma3.1/proof; Vogel-Zeitouni2001.09024v1 Assumption2/Theorem3; Higham's companion convention reused1523; Knill's June2014 manuscript Theorem7/Corollary9 and complete exterior-power proof. Precise citations and hypotheses are in source-notes1994.
COMPARISON: Conditional deterministic Hermitization assumes logarithmic uniform integrability and supplies neither a polynomial rate nor unscaled real-window transfer; noisy theorems require actual random perturbations. Knill's ordinary determinant identity does apply to the real shifted companions and isolates a different fixed-minor test. The actual integrated estimate remains uncovered.
GAP: No degree-uniform small-singular-value logarithmic bound or signed upper payment is proved. The fixed-interval minor/coefficient comparison is an unproved bounded specialization to test separately, not a theorem established by this assessment.
REASON: Park automatic Hermitization/noisy-equivalence import and test the polynomial cutoff deterministically before pursuing signed estimates. Earlier trace-norm stops remain within their scopes; the new minor test does not repeat them.
SCOPE: Completed literature-only source comparison; no new actual-family estimate, lemma, mathematical script or theorem reproof. Source coverage for the nominated minor test is prepared separately in assessment1994, subject to the supervisor's separate next-turn approval.
LITERATURE_REASON: Invocation-start assessment1993 was REVIEW_REQUIRED for essential deterministic logarithmic regularization coverage; ready scalar/companion-cost assessments did not cover its hypotheses. This review supplies that comparison without repeating unrelated literature.

Main gap: L030-L032/C032a, and C028b's H_d=o(d) on this branch.
Essential inputs for defining the proposed test: C028b/d/e,C029i/j.
Retain Q_d(y)=P_d(y-b_1)=y^d+sum_(k=1)^d c_(d,k)*y^(d-k),
b_j=gamma_j/gamma_0 and every integer d>=3. Let A_d be the monomial
Frobenius companion with subdiagonal entries1 and last column
(-c_(d,d),-c_(d,d-1),...,-c_(d,1))^T. No similarity optimization or
theta-Gram basis is proposed. The source review must verify this
convention's characteristic-polynomial identification before using it.
Review1994 verifies that convention using the already assessed Higham
identity; see source-notes1994. The following bound remains proposed.

For epsilon>0 and real y!=0 the candidate regularized statistic is

    R_(d,epsilon)(y)
      =(1/(2d))*log det((y*Id-A_d)^*(y*Id-A_d)+epsilon^2*Id)
        -log|y|.

The proposed discriminating threshold is the existence of one finite
fixed K>0 for which, for every fixed finite A>=1,

    limsup_(d->infinity) integral_[-Ad,Ad]
       |R_(d,d^(-K))(y)-t_d(y)|dy=0.

The origin and all real/multiple roots retain their Lebesgue null-set
convention. This is a proposed bound to assess, not a proved determinant
identity, convergence statement or positivity claim. Preserve the
unscaled window and the factor1/d; changing coordinates must account
for its Jacobian. An informative failure or a necessary faster scale
may reject this polynomial-scale prerequisite without saying anything
about actual H_d or RH.

Potential use: permit controlled singular-value/resolvent estimates of
the signed window integral. Even a successful regularization bound
would leave its signed upper estimate, an actual arithmetic input,
C028e's exterior assembly and the ordered limits unresolved. Retain
q=1/(4d),L=2Ad and limsup_A limsup_d (L/q)*log Z<=0 if returning to
C029j. No RH, real roots, simplicity, normality, random coefficients,
uniform condition number or interchange of limits is allowed.

Continue only if primary hypotheses give a deterministic applicable
bound or isolate a concrete coefficient/singular-value test independent
of the desired signed payment. Park if they merely assume the needed
logarithmic uniform integrability, require randomness/normality, or
repackage the existing stopped trace-norm cost. Full matching Mathlib
coverage remains unchecked. Review1994 found no applicable automatic
import and prepared a single fixed-interval minor test in
drafts/literature/2026-11-20-companion-fixed-minor-regularization-test-1994.md.
No mathematical derivation of that test is part of this literature turn.
