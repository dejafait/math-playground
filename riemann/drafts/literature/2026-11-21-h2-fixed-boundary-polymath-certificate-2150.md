# Fixed normalized boundary certificate: proposed calculation

TARGET: Implement and test Polymath's normalized nonvanishing criterion for F(lambda,100+iy) on 0<=lambda<=1/20 and |y|<=1/2 using the fixed 32-by-64 parameter boxes and 100-digit enclosing arithmetic specified in the step2150 review.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step2150 exact-boundary comparison in 2026-11-21-h2-fixed-boundary-nonvanishing-review-2149.md, including searches, duplicate/failure comparison and inspected primary cases. This nomination performs no additional mathematical calculation.
SOURCE_EVIDENCE: https://arxiv.org/html/1904.12438v2#S1 (D. H. J. Polymath, arXiv:1904.12438v2, 4 August 2019), Theorem1.3, Corollary1.4, (5)-(25), Section6.3/Proposition6.6(iv)-(vi); L058 continuity and L919 normalization; L037 arithmetic contracts augmented by Python3.15.2 Decimal and DLMF elementary-function statements inspected in step2150. Exact links/read limits are in that review.
COMPARISON: The source already proves a normalized finite-sum approximation with a complete analytic error for positive time. Needed differences are its fixed closed-band application, verified zero-time limiting argument, whole-box inclusion and an actual strict certificate. No new approximation theorem is sought.
GAP: No value of the required minimum, feasibility of a strict margin, constant-cutoff certificate or complex arithmetic implementation has been established. Full head/census/continuation and H2 margin remain unpaid even if this boundary test succeeds.
REASON: One bounded test of a covered existing method can pay or park a distinct boundary prerequisite without repeating moment boxes, endpoint Rayleigh contractions, product discovery or a zero-free-region theorem.
SCOPE: Only exact TARGET, with the immutable budget and stop conditions in the completed step2150 review. Research may justify the stated routine specializations and implement them; no mesh/precision/cutoff sweep, ABC fallback, zero census or head search is covered. Newly written ready continuation: separate supervisor approval is still due.

Essential local inputs are L019, L058 and L919; C919a explains the
prospective head tolerance but is not a premise for nonvanishing.
L037 supplies only its stated real arithmetic contracts; its existing
finite moment certificate is not a complex-box certificate. L036 is
not used by the selected finite-sum method. No RH, simplicity,
all-real-zero, existing certified complex library or cross-notebook
input is assumed. Full matching Mathlib coverage is unchecked.

This is a known-method implementation/specialization, not a creative
attempt or a claim of novelty. A successful calculation would be a
local boundary input requiring its later critical audit, and would
leave the actual-Xi all-degree mixed-positivity gap unresolved.

## Step2151 source-field repair

LITERATURE_REASON: Supervisor recovery requires a direct source URL in this ready assessment; the detailed step2150 comparison is reused without broadening its scope.

Opened the primary URL above on 21 November 2026 and rechecked (5),
Theorem 1.3, (14)-(19), (23)-(25), Corollary 1.4 and Section 6.3,
(69)-(74), Proposition 6.6(iv)-(vi). The stated region remains
0<t<=1/2, 0<=y<=1, x>=200. The explicit nonvanishing test is sufficient,
not necessary. The definition of N and the complete errors are accessible;
no constant-cutoff verification or boundary evaluation was performed.
The zero-time limit, branch guards and whole-box arithmetic remain
implementation obligations already recorded in step2150.

Supporting arithmetic documentation is directly accessible at
https://docs.python.org/3.15/library/decimal.html ; the prior comparison's
rounding qualifications remain in force. No installed runtime version or
complex-arithmetic implementation is certified by this repair.

DECISION remains SPECIALIZE for the unchanged TARGET and immutable
step2150 budget. This is a metadata/source-access repair, not mathematical
progress, a fresh overlap result or a renewed exploration budget.
Existing failures and all independent gaps are unchanged. No lemma,
mathematical script or proof assembly was modified. Full matching
Mathlib coverage remains unchecked.
