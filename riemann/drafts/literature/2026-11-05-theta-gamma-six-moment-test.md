# Six compensated theta moments — finite-test coverage nomination

TARGET: Certify or refute positive [0,infinity)-moment representability of s_j=4^j(1/2)_j m_0/m_j for 0<=j<=5 by the two 3-by-3 Hankel matrices and the singular range condition, retaining the audited actual-theta coefficient errors.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step637's exact truncated-Stieltjes, gamma-ratio, reciprocal-theta and Bernstein-product searches and the scoped duplicate/failure comparison in 2026-11-05-theta-gamma-reciprocal-moment-scope.md; no actual matrix test or novelty claim.
SOURCE_EVIDENCE: Curto–Fialkow, Houston J.Math.17(1991), Theorem5.1 p625, https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf ; Berg arXiv:math/0412340v1 Theorems1.1/1.2 and5.1/5.2, https://arxiv.org/pdf/math/0412340v1 ; essential Section3/4 proof cases and full qualifications reused from step637; L778 complex evaluator/error and L791 coefficient normalization, standard Cauchy estimate and Sylvester criterion remain the prescribed local inputs.
COMPARISON: Known criteria decide a six-moment problem; actual compensated theta data remain untested. The proposed law is a necessary finite premise of the existing conditional Bernstein construction, not a common Favard measure or a lower-oscillation theorem.
GAP: Actual matrix signs and any singular compatibility remain uncomputed; full moment law, actual Bernstein membership, sufficient lower oscillation, degree uniformity and mixed/shifted transfer remain open.
REASON: Approve one bounded application of known criteria as a representation-premise diagnostic. A negative result stops this premise; a pass retains only finite feasibility. Separate source approval completed in step638: primary URLs opened and theorem statements rechecked; target and scope unchanged.
SCOPE: Exactly indices0..5 and the two full 3-by-3 matrices; rigorous coefficient extraction, interval/rational sign checking and any singular range verification needed for this single test. No higher-degree search, new moment evaluator, Mellin inversion, root survey, sign-transfer derivation or claimed RH progress.

The main gap is actual-Xi all-degree mixed positivity. This intermediate
test can reject a concrete positive-representation premise of a proposed
dual averaging route and of the conditional Mellin/Bernstein construction.
There is no assumption that a surviving finite premise transfers signs.
This is reproduction/specialization, not a creative proof attempt.

Use the primary theorem and normalization comparison in
[the completed source assessment](2026-11-05-theta-gamma-reciprocal-moment-scope.md).
The source statements are imported by citation; do not reprove the moment
theorem or derive a new Bernstein implication. If recording a mathematical
result later, give its actual hypotheses and qualifications in its own
canonical lemma, with the precise source citation and Mathlib status.

Essential inputs are L019/L021/L795 and the finite evaluator component of
L778 with L791's audited coefficient conversion. L018 supplies the existing
G convention when that conversion is used. L796/L822 are contrasts only.
No fitted model identity supplies actual data at index5. The full input
certificate is `scripts/actual-fredholm/fixed-pair-certificate-431.json`;
the current five-entry gamma list in
`scripts/central-jacobi/fixed-model-certificate-476.json` stops at index4.
Read the complete needed evaluator/error proof and software contract before
using these certificates. Widen each selected P_0 coefficient interval by
the complex Cauchy error from L778 (5), before normalization or reciprocal
division; prove denominators positive. Preserve the actual coefficient
correlations by valid enclosing operations, never by rounded previews.

For positive definiteness, the named Sylvester criterion applies to the
real symmetric matrices. If claiming only semidefiniteness, all required
principal minors or an equally rigorous matrix certificate must be paid;
the two determinants alone do not suffice. If an interval meets zero,
do not infer exact rank or a nullspace. A singular case needs exact
compatibility under the cited criterion; otherwise report inconclusive.
An early certified obstruction in a proper principal block may end the
single test without unnecessary computation of further entries.

Save full evidence and program under `scripts/theta-gamma-moments/`, print
only result/bounds/failures/paths, and inspect complete load-bearing values
with the prescribed inspector. No mathematical script exists for this test
yet. A negative witness rejects representation of these six data and any
representation requiring them; it does not refute RH. A complete pass does
not establish an infinite measure law, variation diminution, lower
oscillation, actual polynomial real roots or all-degree signs. There is
no automatic degree extension after either outcome.

All inherited analytic/software contracts remain assumptions of a future
computer-assisted informal result; no installed binary or arithmetic is
formally verified. No cross-notebook input. Full matching Mathlib coverage
is unchecked. If the target expands outside this scope, use REVIEW_REQUIRED
and a separate source turn before mathematical work.

## Separate source approval and URL repair (step638)

LITERATURE_REASON: Supervisor reported missing direct source URLs in this ready assessment; repair that source-evidence field and approve the unchanged finite test without repeating discovery or calculating moments.

Direct primary sources: [Curto–Fialkow, Theorem 5.1, printed p625](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf#page=23) and [Berg, version-specific PDF](https://arxiv.org/pdf/math/0412340v1). Both opened successfully on 2026-11-05. Curto–Fialkow's p625 theorem and adjacent Theorem 5.2 retain the semidefinite and range conditions recorded in step637; OCR of Theorem 5.1(iv) remains degraded. A screenshot request returned only a reference, so no visual inspection is claimed. Reuse the prior exact comparison and essential proof-case reads rather than treating this retrieval as fresh mathematical evidence. Berg's Theorems 1.1/1.2 again explicitly require a nonzero Bernstein function and positivity at the starting parameter; these hypotheses are not established for the actual proposed factor.

This is a metadata/source-access repair, not a new import or mathematical result. No target, hypothesis, scope, stopping test or evaluator contract changed. The unchanged SPECIALIZE decision is ready for the saved calculation; all analytic/software contracts must still be inspected before numerical use. No additional literature turn is prescribed.
