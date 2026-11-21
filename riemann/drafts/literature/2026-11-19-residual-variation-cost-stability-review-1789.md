# Residual approximation versus signed-width variation: nomination1789

TARGET: Assess quantitative inverse-Laplace stability for an explicit lower bound on approximation of C033i's residual over s in [1,2] by mass-one signed widths of TV at most V, using C033j's jump and C033r's local regularity, without evaluating the observable or reopening the stopped schemes.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1790 completed the bounded inverse-Laplace and bounded-analytic-continuation search; exact queries, inspected cases, duplicate checks and optional unread leads are in drafts/literature/2026-11-19-residual-variation-cost-source-notes-1790.md. No exact rate for this law family was located among inspected results; this is not a novelty finding.
SOURCE_EVIDENCE: Inspected Lederman--Steinerberger1605.03866v1 Theorems1/2 and Sections4/5; Saitoh--Tuan--Yamamoto2001 Theorems1/2 and Section3; Trefethen2020 Lemma2.1/Theorem3.1 with complete proofs and the relevant Theorems4.1/5.2/7.1 cases. Reused C033i/j/l/p/r and Gaver coverage1774; checked Mimica Proposition1.4's real, positive-measure scope.
COMPARISON: The inverse theorems require global Sobolev/weighted bounds or whole-positive-axis data unavailable here; compact width support is not compact time support. Trefethen supplies quantitative strip/disk tools for a finite-node interval-data bridge, but no inspected source supplies the assembled e(V). C033r remains cap2 and freely sampled. No general inverse theorem is directly imported or reproved.
GAP: Prove an explicit interval-to-finite-node propagation bound, then separately justify cap-V Gaver parameters, signed tails/atoms, deconvolution factors and coefficient amplification. These are unproved application obligations; no e(V), actual evaluation, universal V-only rate or Xi consequence is established.
REASON: The review parks direct global inverse-theorem import but identifies a source-supported independently testable analytic bridge. A narrower SPECIALIZE continuation is nominated in review1790 for separate approval; this literature-only turn derives no new estimate and changes no lemma or mathematical script.
SCOPE: Actual qualified laws nu_sigma, width interval [1,2], residual mu of C033i, real signed eta with mass1 and TV<=V for finite rational V>=1, and uniform absolute Laplace error on s in [1,2]. No positive-width substitution, source-wide certification, global inverse, numerical reopening or Xi realization.

## Exact proposed interface and downstream use

Review1790 completed this nomination's source assessment. The precise
theorem comparisons and unproved continuation are recorded in
[source notes1790](2026-11-19-residual-variation-cost-source-notes-1790.md).
The original rate target below is preserved. Direct application of the
inspected global inverse estimates is parked; the fixed-interval
finite-node bridge is nominated separately in
[review1790](2026-11-19-interval-laplace-node-propagation-review-1790.md).
Its source coverage requires separate approval before research. No rate
or variable-cap extension is proved by this review.

Let A_V be the class of real finite signed Borel eta on [1,2]
with eta([1,2])=1 and |eta|([1,2])<=V. Using the original laws,
not a finite convolution approximant, the object to assess is

    d(V)=inf_(eta in A_V) sup_(1<=s<=2)
           |muhat(s)-integral exp(-B_sigma(s)) deta(sigma)|.

The proposed result is an explicit positive lower bound e(V)<=d(V)
with specified dependence on V and the existing constants. This is a
target, not an assertion proved here. Qualitative nonmembership or a
new abstract existence lemma alone would not meet this rate target.
The source review must retain the distinction between uniform transform
data on a fixed interval and the freely located finite samples in C033r.

C033j's finite signed deconvolution and density jump provide the
prospective obstruction; C033r's local regularity gives a possible
way to track its dependence on variation. Source review must check
whether finite signed TV control, local regularity near the jump and
the available tail bounds suffice for the cited inverse problem, and
whether dividing by nu_1's transform costs an explicitly paid factor.
Do not assume compact support of the full laws, positive R_sigma,
global density smoothness, a bounded convolution inverse or exponential
moments. No such specialization or bound is derived in nomination1789.

If available, a rate could distinguish low-variation approximate law
realizations from sequences requiring growing cancellation. It does
not supply an actual-Xi realization, a necessary width budget for such
a realization, all-degree positivity or signed-height payment. The
main L030-L032/C032a gap therefore remains independent. This target
has a plausible intermediate use, not an established route to RH.

## Bounded source test and prior stops

Inspect primary quantitative inverse-Laplace/analytic-continuation
stability statements and their essential proof cases, checking exact
norms and a jump-versus-regularity comparison. Reuse existing transform,
compactness and separation coverage. Continue only if this supplies
an assessable quantitative specialization, or a specific missing input
whose necessity can be tested independently. If all applicable sources
give only qualitative existence, require unavailable global smoothness
or leave the V dependence unspecified, record the informative scope
limit and park this rate mechanism. Do not repeat generic searches
for the already established qualitative separation.

Midpoint1781 and common-prime ellipse1782 remain parked with audits1789
and1784 respectively. Independent-box1571 and expanding-disk1576 are
also preserved. This target changes the analytic question; it does not
authorize an evaluator, adaptive prime cutoffs or another quadrature.
All actual-divisor, conjugation/multiplicity, ordinate-zero exclusion,
strict-strip/gamma>14, counting, through100 real zeros, retained real
zero, reciprocal-square tail, heat, fixed-j, half-variance and both
fixed-v1 qualifications remain. Full matching Mathlib coverage is unknown.

Discovery1747 still supplies no independent actual-theta representation,
weighted height transfer or quantitative signed majorant. Accordingly
no justified proof_attempt/creative nomination is made from this audit.
This missing central input is a current blocker, not a global stop.
The proposed literature task must not be mislabeled creative research.
