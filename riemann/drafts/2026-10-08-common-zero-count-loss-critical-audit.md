# L378 common-zero count-loss critical audit

Approved target: Critically audit L378's common-zero count-loss theorem, including finite-interval localization, analytic dependence, full F multiplicities and closed endpoints.

Prior coverage: `drafts/literature/2026-10-08-common-zero-count-loss-audit.md`
(EXPLORE), supplied at invocation start and reused unchanged.

Main gap: actual-theta mixed positivity and the total L367 signed margin.
Intermediate target: validate or correct canonical L378's conditional
universal constant-one count bound. Downstream use: combine it with
L377's count excursions under an independently established eventual
actual D≤0 premise to constrain common-zero counts. Neither that premise
nor actual common-zero control is established here.

Test: retain the bound only if the localized pencil argument and every
analytic, multiplicity and closed-endpoint case pass; otherwise identify
and repair the exact defect or withdraw the affected claim. L373's
common-zero obstruction remains relevant and is not an input.

Saved unfinished reasoning: the pointwise pencil matrix has positive
second diagonal and nonnegative Schur complement, so restriction to
constant pencil members remains semidefinite. A finite multiple zero
beside a nonzero member violates its discriminant inequality using a
right-sided Taylor limit, including at H and X. Connected analytic
identity excludes a locally zero pencil member in the independent case.
The partition count appears consistent: with k common points, q other
G zeros and p occupied pieces, the claimed F count is at least q-p+k,
and p≤k+1. Remaining audit work is to check each endpoint/empty-piece
case and document the full verification canonically. No theorem is yet
marked reviewed in this checkpoint note. No mathematical script needed.

Completed: all cases pass; the full separate verification is now in
canonical `lemmas/L378-common-zero-discriminant-count-loss.md`.
The original unfinished note above is preserved as such. No correction,
strengthening, new input or mathematical script was needed. Outcome
EXPLORATION honestly records completed verification rather than a newly
established mathematical input. Classification POTENTIALLY_NEW retains
the prior bounded source assessment only; it is not a novelty claim.
PROOF.md and DAG.md remain unchanged because the argument and its direct
inputs are unchanged. The canonical review supersedes the overview's
older pending-audit phrase for L378.

For continuation selection only, the prior actual-disjointness assessment
and the statement of L377 were read. The former covers shifted-pair
projection comparisons, not quantitative coincidence with unshifted
F_0. L377's stated deficit scale is sqrt(log log T). The proposed next
target screens arithmetic common-zero control on that scale; it does not
reopen the L375/L376 geometric inference. Its new assessment is explicitly
REVIEW_REQUIRED. No source approval, count-bound proof or actual-family
application is performed in this audit.
