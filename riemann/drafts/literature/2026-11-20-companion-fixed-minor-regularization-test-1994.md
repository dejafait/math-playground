# Fixed-minor polynomial-cutoff test: coverage prepared1994

TARGET: Test whether the fixed subdiagonal minor and actual entire-function growth force liminf_(d->infinity) integral_I |R_(d,d^-K)-t_d|dy>0 for every fixed K>0, where I=[b_1+1/4,b_1+1/2].
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1994 searched deterministic shifted-companion logarithmic regularization, Hermitization, polynomial cutoff estimates, and Cauchy-Binet Gram minor expansions; scoped C028*/C029* and companion stop/assessment searches found no matching test. This bounded check establishes no novelty; queries/ranges are in source-notes1994.
SOURCE_EVIDENCE: Knill, Cauchy-Binet for pseudo-determinants, 10June2014 author manuscript, Theorem7/Corollary9 pp16-17 and exterior-power proof pp18-19, https://people.math.harvard.edu/~knill/graphgeometry/papers/bi.pdf ; Higham companion identity (*), https://nhigham.com/2021/03/23/what-is-a-companion-matrix/ ; finite SVD coverage reused from Vogel-Zeitouni2001.09024v1 Section2/(2.1)-(2.2), https://arxiv.org/pdf/2001.09024v1 ; actual growth contract remains C028f/C029i. Full comparison: drafts/literature/2026-11-20-companion-regularization-source-notes-1994.md
COMPARISON: The determinant minor expansion and entire-function growth are known methods; no inspected source states this actual Jensen fixed-interval lower bound. Specialize only the minor, scalar coefficient estimate, cutoff power and integral. Random/noisy Hermitization is not used, and the old trace-norm floors do not imply this result.
GAP: Verify the specified minor contribution, every epsilon/d factor, a uniform actual-polynomial upper estimate on I, and the resulting positive integrated liminf; all are unproved in this review. A failed comparison need not refute polynomial regularization.
REASON: A positive lower liminf on one fixed interval would reject every finite polynomial cutoff in nomination1993, independently of the unpaid signed mean. This is a concrete independently testable obstruction using available deterministic sources, not a new signed mechanism or an RH counterexample.
SCOPE: Coverage prepared during literature-only review1994 and source-URL repair1995; no mathematical result derived. Separate literature turn1995 rechecked the primary determinant statement/proof and companion convention; the unchanged target is ready for a known-method calculation/specialization with REPRODUCTION classification. No additional coverage or creative mechanism is claimed.

## Exact contracts and bounded attempt

Use the actual b_j,F,P_d,Q_d,t_d of C028b/d/f and C029i/j,
with d>=3, b_0=1, b_j>0, b_1 fixed real positive and
log F(r)<=K_0*r^(3/4) for r>=1 with one fixed K_0.
The old growth input may be cited under its existing contract; it is
not to be replaced by an assumption about root reality or RH.

Use exactly nomination1993's monomial companion A_d: subdiagonal
ones, last column (-c_(d,d),...,-c_(d,1))^T, all other entries zero,
where Q_d=y^d+sum_(k=1)^d c_(d,k)y^(d-k). Higham's imported
identity gives det(yI-A_d)=Q_d(y), with multiplicity.
For real y, put M_d(y)=yI-A_d and retain

    R_(d,epsilon)(y)
      =(1/(2d))*log det(M_d(y)^T M_d(y)+epsilon^2 I)-log|y|.

The proposed minor uses rows {2,...,d} and columns {1,...,d-1}
of M_d(y). Its value and contribution must be calculated in the
mathematical attempt; no value or lower bound is asserted here.
Use the ordinary determinant identity of Knill, not a pseudo-determinant.
All matrices are real for this test, so transpose is the required adjoint.
The source imposes no invertibility, normality or rank hypothesis.

On the fixed interval I=[b_1+1/4,b_1+1/2], seek one c>0
independent of each fixed finite K>0 such that

    liminf_(d->infinity) integral_I |R_(d,d^-K)-t_d|dy >= c.

The degree onset may depend on K; no uniformity in unbounded K is
requested. This is a proposed stronger discriminating threshold, not
a proved bound. Derive any actual-polynomial estimate from the finite
positive coefficients and the recorded F growth, retaining factorials.
No numerical root or singular-value computation is required or sufficient.
Keep the unscaled y integral and 1/(2d) normalization. All repeated
real roots have their existing finite-null-set convention.

Continue only if this finite minor/coefficient mechanism produces an
explicit positive c, or identifies a precise failure. Abandon this
specific comparison if it needs unknown signed cancellation, condition
numbers or root separation. Failure alone does not establish that the
full growing-window error vanishes. Do not enlarge this bounded turn
into an unrestricted singular-value or similarity search.

If the proposed positive liminf is proved, explain why I lies inside
[-Ad,Ad] eventually for every fixed A>=1, then park nomination1993's
polynomial-cutoff route. This would exclude only that regularization
prerequisite. C028b's H_d=o(d), C029j's signed upper payment and
C028e exterior assembly would remain unresolved. Preserve
q=1/(4d), L=2Ad and the ordered A/d limits if those are later used.
No change of polynomial, similarity optimization, randomness, RH,
simple-root assumption or limit interchange is authorized by this test.

## Mathlib

Not checked. Full matching theorem availability is unknown. The general
determinant, SVD and finite-sum facts are supporting inputs, not evidence
of a formalized actual-family asymptotic. No absence is asserted.

## Source-URL recovery review1995 (2026-11-20)

The ready assessment lacked a direct source URL in its own required fields,
although source-notes1994 contained the links. Added them to SOURCE_EVIDENCE.
Reopened Knill's dated author manuscript, Section 5 Theorem 7 and Corollary 9
(printed pp.16-17), and Section 6 (pp.18-19): checked the empty minor,
exterior-power minor entries and multiplication, and complete trace proof.
The ordinary identity applies to arbitrary real rectangular matrices;
no pseudo-determinant assertion or rank hypothesis is needed. Higham's
opening definition, identity (*) and alternate conventions were rechecked.
The finite SVD coverage and local growth input are reused without a new audit.

This is a process/source-location repair, not new mathematics or a changed
source comparison. The exact TARGET, SPECIALIZE decision and bounded test
are unchanged. Review1994's duplicate and failure comparison remains in scope:
trace-norm stops1525/1588/1713 do not decide this logarithmic error.
The selected minor, cutoff powers, coefficient estimate and positive
integrated liminf remain wholly for the next mathematical attempt.
No lemma, mathematical script, PROOF.md or DAG.md was changed.
