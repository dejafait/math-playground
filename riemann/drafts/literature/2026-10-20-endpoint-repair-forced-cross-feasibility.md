# Source gate for the endpoint repair's forced cross entry

TARGET: Test positive-semidefinite bulk covariance feasibility of the derivative-forced xy entry q'/(2L) for L447's endpoint-repaired density, keeping L447's rare components, bulk mean and conditional y-second density unchanged.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 288 searched Schur-complement singular cases, occupation/covariance positive-semidefinite derivative moments, prescribed variance/derivative covariance and prescribed occupation second moments; compared L447 (1)--(15), L446 (1)--(5), L445 (5)--(6), L443 (1) and L438 (9)--(15), the ready calculus/occupation assessments and three scoped failure records. No inspected theorem decides this complete fixed-data law; failed searches establish no novelty.
SOURCE_EVIDENCE: Freshly inspected Boyd--Vandenberghe, Convex Optimization (2004, corrected seventh printing 2009), Appendix A.5.5, printed pp. 650--651, quadratic minimization (A.13)--(A.14), positive-definite and singular-block PSD cases; reuse the inspected Hunter/Bell weak-derivative and Lasserre--Henrion--Prieur--Trelat necessary occupation identities in the ready assessments identified below.
COMPARISON: The cited Schur-complement theorem supplies an exact finite-dimensional PSD test, including zero-variance cases, but evaluates no law-specific entry. L446 fixes a raw cross entry for an AC density, while L447 supplies a different Lipschitz density and only scalar endpoint compatibility. Bulk centering and subtraction of all fixed rare terms must precede the matrix test; neither positive total raw seconds nor Schur--Horn alone settles that test.
GAP: A later research attempt must evaluate necessary bulk PSD feasibility of the forced entry for L447's exact repaired density with all specified data fixed, on an eventual real-H ray or with rigorous failure at arbitrarily large H. Complete rare terms, translation, cutoff branches and endpoint layers remain unestimated for this derivative constraint.
REASON: Essential source coverage for this necessary matrix test is adequate. Its unresolved quantitative comparisons are local mathematical obligations, not missing theorem coverage. SPECIALIZE approves a later attempt only; no feasibility criterion specific to this law has been derived or evaluated in this literature turn.
SCOPE: Necessary positive-semidefinite feasibility with L447's repaired conditional x- and y-second densities and rare components fixed; no claim about other temporal identities, all other entries, negative-cone realization, actual trajectories or RH.
COVERED_TARGET: Test positive-semidefinite bulk covariance feasibility of the derivative-forced xy entry q'/(2L) for L447's endpoint-repaired density, keeping L447's rare components, bulk mean and conditional y-second density unchanged.
LITERATURE_REASON: The invocation gates the changed derivative-forced covariance target, which lies outside the prior endpoint-construction and audit scopes; this is its first completed source comparison, not repeated browsing on a ready target.

The main gap remains global mixed positivity. The proposed intermediate
test would decide whether this particular audited scalar repair can
support the first all-temporal x-squared condition without changing its
other specified data. A positive scalar endpoint identity is only an
integrated necessary condition; no covariance converse is assumed.

Essential local inputs are L447's exact repaired density and rare/bulk
matrix decomposition; L446's weak uniqueness formula, applied to the
new Lipschitz representative; L445's pointwise regularity interface;
and L443/L438 for the fixed raw second data, probabilities and mean.
No cross-notebook input is proposed. The canonical L444/L446 failures
remain on their original fixed-density scopes and must not be promoted
to a ban on changed-density tests.

After source approval, a discriminating mathematical test must retain
the complete rare xy and y-second terms and the bulk translation when
forming any necessary positive-matrix inequality. It must decide
feasibility on one eventual real-H ray or give a rigorous obstruction
on arbitrarily large heights, not sample endpoint layers. A failure
would stop only this fixed-data extension of L447; a pass would still
leave the remaining matrix entries, support, other occupation tests,
inter-H consistency and actual/global realization unresolved.

No conclusion about that inequality, its satisfaction or failure was
derived in step 287 or in this source review. The initial uncovered
continuation is now assessed below; mathematical work awaits the
supervisor's separate next-turn approval. Actual clipping, capped
nondegeneracy, L413's full-error regulator margin, global mixed
positivity and RH remain unresolved. Full matching Mathlib coverage
is not checked; this is not evidence of absence.

## Completed source comparison — step 288

This is LITERATURE / NOVELTY_UNCHECKED / literature_comparison, with
outcome EXPLORATION. It adds primary source coverage and an exact-scope
comparison, without a new lemma, mathematical script, law-specific
derivation or feasibility verdict. Mathematical exploration usage stays
0 of 3, without spending or renewing that budget. TARGET is unchanged.

### Newly read primary matrix theorem

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge
University Press, 2004, corrected seventh printing 2009,
[Appendix A.5.5, printed pp. 650--651](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=664).
For a real symmetric block matrix X=[[A,B],[B^T,C]], A positive
definite gives X positive semidefinite exactly when
C-B^T A^(-1)B is positive semidefinite. Equations (A.13)--(A.14)
minimize the quadratic form over the first block. For singular A,
the source requires A positive semidefinite, range(B) contained in
range(A), and C-B^T A^dagger B positive semidefinite; it also states
the unbounded minimization cases. The full relevant text, including
both cases, was inspected. Scalar blocks give the familiar test for
[[a,b],[b,c]]: a,c nonnegative and b^2<=ac; the singular range condition
requires b=0 when a=0. Import the theorem without reproving it.

The application is to a principal block of the centered **bulk**
covariance, with its actual fixed diagonal entries. The raw forced
cross entry must first be converted through L443's full matrix
decomposition. This theorem neither asserts that the test passes nor
supplies a covariance completion with prescribed support or moments.
No division by a variance is allowed without its hypothesis.

Initial retrievals from the web.stanford.edu PDF host timed out; the
www.stanford.edu author-hosted copy supplied the complete text and
equations. Its copyright page identifies the edition above. Screenshot
requests timed out, but the relevant mathematical text was fully
available; no essential passage remains source-blocked. A separate
Vandenberghe--Boyd *Semidefinite Programming* PDF was a search lead
with a failed direct retrieval and is not an additional inspected input.

### Reused calculus and occupation coverage

Reuse
`drafts/literature/2026-10-20-complete-x-second-integrated-xy-compatibility.md`:
[Hunter, *Notes on Partial Differential Equations*, revision 18 June 2014](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
Definition 3.1 and uniqueness discussion, printed pp. 47--48, and
Theorems 3.60, 3.62--3.63, pp. 79--80, treat locally integrable weak
derivatives, AC reconstruction and closed-interval integration by parts.
[Bell, *Sobolev spaces in one dimension and absolutely continuous functions*, 21 October 2015](https://jordanbell.info/LaTeX/mathematics/sobolev1d/),
Section 1, Theorem 1 and the following uniqueness paragraph, supplies
the tested-function uniqueness proof. These primary passages and
their qualifications were already inspected; no new retrieval is claimed.

L447 supplies a Lipschitz representative at each fixed H. Smooth
positive L(t)=log(2+t) on that compact interval meets the unchanged
weight hypotheses. Thus L446's proved weak-uniqueness interface is
applicable to the changed representative; this does not transfer
L446's old-density failure to the new density. Derivatives are a.e.
temporal derivatives with H, its integrals and cutoff stage fixed.
No H derivative, uniform Lipschitz constant or atom derivative is assumed.

The same ready assessment and
`drafts/literature/2026-10-20-exact-quadratic-block-critical-audit.md`
record J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat,
*Nonlinear optimal control via occupation measures and LMI-relaxations*,
SIAM J. Control Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1, sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5](https://arxiv.org/pdf/math/0703377v1).
Its C1 finite-interval chain-rule identity includes both endpoint
evaluations. Ordinary C2 trajectories fit compact state/control boxes
at each fixed H. L446 already supplies the necessary temporal x-squared
specialization; no occupation-measure converse is used. A pointwise
matrix test cannot replace the missing full dynamical compatibility.

Real Schur--Horn and L419's supported Borel realization, assessed in
the ready endpoint audit record, begin only after an admissible
covariance and quantitative trace/translation margins are established.
They supply no automatic feasibility for a derivative-prescribed entry.
No further reading or reproof of those realization tools is required
for this necessary-condition test.

### Exact fixed data, duplicates and failed approaches

L443 (1) retains the complete raw decomposition
q=R+w(Sigma+mm^T), with
R=pYY^T+k_+Z_+Z_+^T+k_-Z_-Z_-^T. L438 (9)--(15) defines every
probability, remaining mass, normalization, mean and matrix correction.
L447 changes Sigma alone, including its endpoint K multiples and
finite correction; its repaired Sigma_22 and raw q_22 are fixed data
for this test. L445 (5)--(6) identifies the old complete scalar
representative and its regularity, while L447 specifies the change.
These passages were read for source applicability, not recalculated.
Neither a rare cross entry nor a translation product may be dropped
when a raw entry is turned into a centered bulk entry. The same
warning applies to the fixed y-second diagonal.

The three scoped ATTEMPTS records were checked:
`ATTEMPTS/2026-10-20-all-temporal-bounded-covariance-extension.md`
retains L444's uniformly bounded zero-11 stop;
`ATTEMPTS/2026-10-20-complete-x-second-singular-variation.md`
retains L445's removal of that regularity obstruction; and
`ATTEMPTS/2026-10-20-unchanged-x-second-integrated-xy-extension.md`
retains L446's exact endpoint obstruction for the unchanged density.
None decides PSD feasibility for L447's changed density. L447's
audited existing covariance and finite occupation block are likewise
not a duplicate proof for the forced entry. These historical stops
remain valid in their original scopes.

Queries actually run included `site.stanford.edu boyd convex optimization
A.5.5 Schur complement positive semidefinite singular`, `"occupation
measures" "covariance" "positive semidefinite" derivative moments`,
`"prescribed variance" derivative covariance positive semidefinite`,
`"occupation measures" "prescribed" "second moments" covariance
derivative`, and `"covariance" "derivative" "variance" "Cauchy"
stochastic differentiable process`. The stronger primary matrix
criterion above covers the necessary algebra. Generic stochastic
regularity and covariance-adjustment leads were not inspected or
used as theorems about this law. No matching fixed-data evaluation
was found in the inspected material; no originality is inferred.

### One bounded mathematical continuation

The later attempt should first test the centered bulk x,y principal
block using the cited criterion, the complete repaired raw density
and the derivative-forced raw entry. Endpoint cutoff transitions are
a concrete region to examine because L447 controls their values and
moment costs but asserts no derivative feasibility there. This is a
candidate diagnostic, not a derived lower bound or failure claim.
Keep rare contributions, the translation, all finite corrections and
the original real-H cutoff; do not replace them with leading terms.

The threshold is PSD almost everywhere in t for each H, not a small
integrated residual. A rigorous violation on positive-measure temporal
sets for arbitrarily large real H would stop this fixed-data extension.
Isolated nondifferentiable points, endpoint samples, or a numerical
determinant do not suffice. A pass on one eventual real-H ray removes
only this necessary block obstruction; a pass only for this block
must not be reported as a full three-dimensional covariance or law.
An inconclusive estimate should preserve its unresolved comparison.

The potential downstream use is to decide whether to retain this
particular scalar endpoint repair for a later compatibility attempt.
Unresolved independent requirements include the remaining covariance
entries, strict negative support, other temporal tests, their finite
block after any cross replacement, mean transport, inter-H consistency,
actual/global realization, clipping, capped nondegeneracy, L413's full
error margin and global mixed positivity. No additional theorem
coverage is essential for the stated necessary block test; any expanded
realization or changed-density target requires its own source review.
