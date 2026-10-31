# Positive transition compactness specialization — proposed ready continuation

TARGET: Establish the finite-collision reduction for F at 0<lambda_*<1/8: right-hand all-real times and nonreal zeros along lambda_j increasing to lambda_* force a real zero of finite multiplicity at least two inside L488's common compact rectangle.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed source comparison in drafts/literature/2026-10-30-positive-transition-finite-collision-reduction.md; exact transition/multiple-zero searches and narrow local duplicate/failure checks found known compactness tools, not a need for a new collision mechanism.
SOURCE_EVIDENCE: Polymath arXiv:1904.12438v2 Section 3, Proposition 3.1(i)–(ii) and complete proof, Theorem 3.2 and Proposition 3.3 first-contact cases; https://arxiv.org/html/1904.12438v2 . Common tail coverage is reused from L488 and drafts/literature/2026-10-30-polymath-uniform-tail-audit.md; standard named supporting inputs are Rouche's theorem, isolated zeros, compactness and the holomorphic implicit function theorem.
COMPARISON: The exact local family and simple-zero persistence are in L058; L488 provides a common compact positive-time rectangle for all nonreal or multiple zeros. Combining these into the exact transition implication is a standard specialization, not an established new result or a source theorem excluding collisions.
GAP: Check endpoint reality, capture of every incoming nonreal zero, a convergent subsequence and the simple-zero contradiction with finite multiplicity; retain L488's source and independent-review qualifications.
REASON: A successful reduction would isolate the finite positive-time obstruction left after escape to infinity is removed. It would not exclude the obstruction or prove RH.
SCOPE: Only the exact transition implication below; no all-time zero labeling, endpoint inverse-gap bound, global Dini inequality, theta-specific collision exclusion, lambda=0 limit or RH result. This newly saved continuation requires separate supervisor source approval before mathematical invocation.

Assume some epsilon>0 has all zeros real for
lambda_*<lambda<=lambda_*+epsilon, and there are real lambda_j<lambda_*
increasing to lambda_* with a nonreal zero on each slice. Shrink the
parameter neighborhood within (0,1/8); no endpoint reality or simplicity
is an assumption. Use one fixed 0<a<lambda_*<b<=1/8 and L488's R(a),
whose common rectangle is |Re z|<=R(a), |Im z|<=1/2. The requested zero
must have |Re z|<R(a); threshold equality belongs to the real/simple tail.

Essential inputs: L018/L019/L058 for the exact family, normalization,
joint entirety, conjugation and nonzero slices; L488 for the common tail
and strip with cited-source qualifications. L060/L061 and Polymath
Proposition 3.1 are checked supporting comparisons, not requirements
to reprove arbitrary-multiplicity splitting. L126/L128 are warnings
against replacing compact capture by an infinite-supremum derivative.

Continue only if the proof accounts for endpoint closure and every
incoming nonreal zero without a global labeling or an assumed endpoint
gap. A failure of common capture or simple-zero uniqueness is a stopping
test to record explicitly. A successful reduction still leaves exclusion
of real multiple zeros at positive parameters and the zero-time limit
unresolved. Reuse the comparison's known failures rather than opening
another generic shape/energy route. Full Mathlib matching is unchecked.
