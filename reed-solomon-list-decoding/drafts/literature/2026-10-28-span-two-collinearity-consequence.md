# Full-sheet span-two consequence — source comparison completed

TARGET: Determine whether L137's common dual line rules out coefficient-difference span exactly two on the full pinned L030 affine sheet, including the exceptional evaluation direction and a common primal point at infinity.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read canonical L135 and L137's hypotheses, geometric representatives, conclusion and relevant proof cases; reused the common-cubic assessment and searched ATTEMPTS/109–112 and the relevant full-sheet assessments for duplicate consequences and stopped mechanisms. New bounded projective-duality/evaluation-line queries and their reading limits are recorded below; no exact published exclusion of this pinned sheet was located.
SOURCE_EVIDENCE: A. I. Kostrikin and Yu. I. Manin, Linear Algebra and Geometry, 1997 paperback edition, Chapter 3, Sections 6.4–6.12 and 7.1–7.2, printed pp. 225–229, https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf ; inspected the subspace/incidence statements, affine-completion construction and proof, Proposition 6.11 with proof, and the finite-dimensional arbitrary-field duality correspondence. Existing L135/L137 source imports and their qualifications are reused, not reaudited.
COMPARISON: Standard projective duality covers passage between the K-dual line and its primal pencil, including its point at infinity; it does not state the local coefficient-span exclusion. L135 supplies distinct genuine lines and full retained directions, while L137 supplies their common dual line. These inputs support a bounded specialization with two explicit affine-chart cases, rather than a reproof of net classification or duality.
GAP: A later research turn must establish the coefficient-span contradiction in both the finite and infinite primal-point cases using the actual evaluation-line incidences. No such contradiction, collapse theorem, retention bound or RS transfer is proved in this source-only step.
REASON: Essential primary-source coverage is now adequate for exactly TARGET under the unchanged pinned hypotheses. The remaining work is local applicability mathematics; the source assessment is ready, but the supervisor's different-next-action requirement routes the immediate continuation elsewhere.
LITERATURE_REASON: The target changes from existence of two compatible rank-two fibers to the consequence of audited full-sheet common-line geometry, and the prior common-cubic source assessment expressly reserved this consequence.
SCOPE: L030/L135/L137 pinned q=137, T={16,64,70,102,112,118,121}, E=F_65537, F=F_(65537^28), H=<19139> of order 1024, k=64, arbitrary 61-core C and bijection sigma, K=E or F, repeated degree-at-most-two messages, all full-sheet evaluation constancies and coefficient-difference span exactly two; six or seven complete retained directions as specified in L135.

## Intended source comparison and relevance

The main gap remains arbitrary-center 67/68 safety. A rigorously
justified exclusion of the full-sheet span-two case could narrow the
coefficient cases in the common-center obstruction. It would leave
span three, retention, arbitrary compatible laws and RS transfer open.
No implication from an arbitrary RS list to this full-sheet hypothesis
is assumed.

Reuse L135/L137 and their existing source records, preserving the
characteristic, ordinary-net and cubic-degeneracy qualifications. Check
the relevant named projective-duality/incidence statement in a primary
source, including its arbitrary-field scope. Compare the projective
completion with genuine affine evaluation lines and their shared
message values; do not silently assume a finite common primal point,
injectivity of the message map, or absence of repetitions. One omitted
evaluation direction is permitted exactly as in L135.

The bounded decision is whether the existing audited inputs and an
appropriate standard theorem cover the exact proposed consequence.
Approve only that specialization if applicability is complete; otherwise
state the precise missing implication or source. Do not derive the
consequence during the source-only turn or approve a broader full-sheet
collapse theorem. No new mathematical result is asserted here.

## Duplicate, failure and source status

The scoped comparison used the conclusions of
`lemmas/L135-span-two-evaluation-line-separation.md` and
`lemmas/L137-common-cubic-via-prime-order-incidence.md`, the scope
paragraph of `2026-10-28-l136-common-cubic-gluing.md`, and targeted
searches of the corresponding local working records and history/535–536.
The proposed consequence is expressly left unresolved there. No
claim of novelty or exhaustive literature discovery is made.

ATTEMPTS/109's residual-rank route, ATTEMPTS/110's one-point patch,
and ATTEMPTS/111–112's reflected two-fiber tests are different mechanisms.
Their obstructions and unfinished reasoning are preserved. The proposed
full-sheet consequence does not reopen those searches or assume that
their partial assignments extend.

The creation-time REVIEW_REQUIRED gate is discharged by the source-only
comparison below. No cross-notebook input is used. Full and supporting
Mathlib coverage of the projective-pencil specialization is not checked;
no absence is asserted.

## Completed source comparison, step 542

The source is Kostrikin–Manin, *Linear Algebra and Geometry*, translated
by M. E. Alferieff, Gordon and Breach, paperback edition 1997,
ISBN 90-5699-049-7, at the direct PDF in SOURCE_EVIDENCE. The inspected
PDF indices 235–239 correspond to printed pp. 225–229. Chapter 3
Section 7.1 starts with a vector space over a field K and assumes finite
dimension for the subspace correspondence. No characteristic-zero or
algebraic-closure hypothesis is imposed. Section 7.3's later restriction
for quadratic polarities is not part of this import.

The inspected input is the annihilator correspondence: dual projective
subspaces have complementary dimension, incidence is reversed, and spans
correspond to intersections (Section 7.1(a),(b), p. 229; principle 7.2).
Sections 6.8–6.10, pp. 227–228, construct the affine complement of a
hyperplane. Proposition 6.11 and Section 6.12, p. 228, identify infinity
points with affine parallel classes and describe line completion.
Theorem 6.5 and Example 6.6(a),(b), p. 226, supply the dimension formula
and uniqueness statements. These are known inputs, not local results.

For applicability, L135's W is an affine plane over the permitted K;
its proof already chooses a K-basis of its two-dimensional translation
space. Its retained level sets are genuine pairwise distinct affine
lines. L137's common line is defined over that same K, rather than only
over its algebraic closure. Its dual representatives use the actual
labels and values. The cited field and dimension hypotheses therefore
match. Passing to a real plane, identifying F_137 with a subfield of K,
or assuming an injective message map would change the problem.

The later mathematical attempt has these obligations; none is resolved here:

- Apply the cited correspondence to the retained lines, keeping the finite
  affine chart and its line at infinity separate. Check K-rationality of
  the resulting primal point within that correspondence.
- In the finite-point branch, use the actual incidences at every auxiliary
  P and L135's distinctness. Establish the consequence for the whole
  coefficient family without assuming distinct messages.
- In the infinite-point branch, test compatibility with affine incidences
  of lines from different retained directions. Do not assume the common
  point is finite or remove this branch by terminology.
- Use only the six or seven complete retained directions. The omitted
  exceptional direction need not be reconstructed; all original full-sheet
  constancies remain available. Connect any restriction to dim_K V=2.

The specialization is needed because neither the textbook nor L137 states
the desired exclusion. No reproof of the imported geometry is needed.
Continue only if both affine-chart cases close under the original
hypotheses. An unresolved pencil case or incidence-to-coefficient gap
requires preserving the exact obstruction, not imposing message injectivity.

Queries actually run: `projective plane duality arbitrary field concurrent
lines collinear dual points lecture notes homogeneous coordinates`;
`projective geometry duality affine parallel lines common point at infinity
field textbook Cameron`; `"projective duality" "finite fields" "concurrent"
polynomial evaluation lines`; `quadratic polynomials affine plane parallel
classes distinct evaluation points constant line assignments nets
characteristic`. The UCR lecture PDF timed out and supplies no input;
the accessible authored textbook supplies the needed elementary geometry.
Other search hits were leads only. No exhaustive search or novelty claim
is made. Existing L137 source versions, including its cuspidal qualification,
and the July ABF qualification are unchanged.

This is source coverage only. No new lemma, exclusion proof, mathematical
script, calculation or DAG/PROOF change was made. This target is retained
as ready coverage, not labeled exhausted. Immediate routing obeys the
supervisor's different-next-action requirement, as recorded in PROGRESS.md
and history/542-2026-10-28-projective-source-recovery.md.
