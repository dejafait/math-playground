# Source coverage: exact finite-height quadratic block repair

TARGET: Determine whether uniformly bounded, exactly height-recentered bulk covariance perturbations can enforce all three fixed prime-2 quadratic occupation identities exactly for every sufficiently large real H while preserving L441's selected constraints and conditional x-second density.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 268 searched occupation/covariance/moment projection, exact quadratic occupation repair, bounded moment Gram projection and equality-constrained least-norm terminology; compared L438's existing exact calibration, L441's bounded repair and audit, L442's residuals and audit, and the scoped Gaussian stop. No inspected source supplies this complete law-specific target; failed searches establish no novelty.
SOURCE_EVIDENCE: Freshly inspected Stephen Boyd, EE263 Autumn 2007-08, Lecture 8, slides 8-2 through 8-7 and 8-9, primary Stanford PDF: full-row-rank least-norm formula, nullspace orthogonality proof and right-inverse/projection formulas. Reuse the previously inspected Carlen--Lieb real Horn theorem, finite-interval occupation identity and finite Poisson/averaging coverage recorded below.
COMPARISON: Standard finite-dimensional projection solves full-row-rank equalities; it supplies neither rank nor a uniform bound for this height-dependent constrained covariance operator. L441 supplies bounded-matrix support and tolerance estimates, and L438 supplies an exact finite-height Gram-calibration precedent, but neither solves these simultaneous covariance equations.
GAP: Establish or obstruct uniform exact solvability of the three full finite-H residual equations on bounded symmetric covariance fields with zero 11 entry and exact w-weighted mean zero; then verify supported Borel realization and every L441 preservation obligation under the unchanged cutoff.
REASON: Essential source coverage is adequate for one later finite-dimensional specialization attempt on exactly TARGET. The remaining operator, uniform-bound and preservation checks are mathematical application obligations, not missing external source coverage; this review proves no construction, rank, bound or impossibility.
LITERATURE_REASON: Invocation required review of the changed simultaneous exact finite-H target; prior ready assessments covered only one asymptotic repair and residual evaluation. Reuse their occupation, matrix and averaging inputs without repeating those source reviews.
SCOPE: Only the three fixed tests e sin(omega t)x^2/L, e sin(omega t)xy/L and e sin(omega t)y^2/L, with L440's eta and omega=log 2; unchanged high and both intermediate components, m, w, g_H, actual response and original L429 cutoff. Absolutely uniformly bounded symmetric bulk covariance changes only; exact zero 11 entry and exact weighted recentering are mandatory.

## Relevance and decision test

The main gap remains global mixed positivity. This intermediate target
asks whether the verified three-test occupation obstruction is a defect
of the representative law or an obstruction to its bounded-covariance
repair. Exact finite-height compatibility would sharpen the limitation
of this finite diagnostic; an unavoidable incompatibility or unbounded
required correction would stop this implementation. Neither result
would realize a trajectory or evaluate actual clipping.

Continue to mathematics with one explicit finite-dimensional projection
or an independently checkable compatibility test for the exact equations.
Success requires one uniformly bounded supported Borel family on a full
eventual real-H ray, all three residuals exactly zero, every integrated
raw second unchanged and the conditional x-second density unchanged.
An o(1) residual or pointwise-in-H solvability is insufficient. Abandon
this implementation only upon a proved unavoidable compatibility
obstruction or unbounded correction requirement. Rank loss of one trial
family alone does not exclude all allowed covariance fields. Do not
change rare components or the cutoff to rescue this target.

## Newly inspected projection source

Stephen Boyd, *EE263: Introduction to Linear Dynamical Systems*, Autumn
2007-08, Lecture 8, [Least-norm solutions of underdetermined equations](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/min-norm.pdf),
slides 8-2--8-7 and 8-9. For real A of size m by n, m<n, and rank m,
every y has the unique minimum-Euclidean-norm solution
x=A^T(AA^T)^(-1)y. The proof on 8-5 uses orthogonality of this x to
the nullspace and the Pythagorean identity for every feasible vector.
Slide 8-7 identifies the right inverse and the projection
I-A^T(AA^T)^(-1)A onto the nullspace; 8-9 gives the multiplier derivation.
These statements, hypotheses and proof were read in the primary PDF.
No uniform-in-parameter bound or function-space sup-norm conclusion is
asserted there. Import this standard result instead of reproving it.

For the application, a proposed finite coefficient space must first
respect the prescribed entry and exact mean constraints. The resulting
height-dependent residual map must satisfy the imported rank hypothesis;
an eventual uniform bound for its right inverse and the pointwise size
of its coefficient fields must be justified separately. A small residual
or an invertible matrix at one height is insufficient. No such family,
matrix, determinant, limiting spectrum or solution is computed here.

The larger Boyd--Vandenberghe VMLS PDF was located, but targeted retrieval
timed out; its exercises and search extracts are not used as theorem
evidence. The accessible primary Lecture 8 supplies the needed finite
linear-algebra input, so this optional access failure is not a blocker.

## Ready sources and local applicability reused

The adequate source records are
`drafts/literature/2026-10-20-prime-two-occupation-covariance-repair.md`,
`drafts/literature/2026-10-20-repaired-law-remaining-quadratic-occupation.md`
and `drafts/literature/2026-10-19-full-three-prime-signed-law-feasibility.md`.
Their primary theorem hypotheses and proof cases were already inspected;
the changed scope does not require rereading the same sources.

J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5, supplies the necessary
C^1 finite-interval identity with endpoints. At each fixed H, ordinary
C^2 trajectories fit compact state/control boxes and the three tests
are C^1 with zero endpoints. L424, L440 and L442 already give the exact
ordinary dynamics and complete transport polynomials. Reuse them with
all slow derivatives retained; do not differentiate a Borel kernel,
probability, cutoff or selected atom. Matching three necessary identities
does not invoke a sufficiency or trajectory-representation theorem.

Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), 13 May 2009,
pp. 1--2, Horn theorem following (1.1), proof through (1.2), supplies
real orthogonal constant-diagonal realization under majorization.
Its two-dimensional and equality cases are covered by the reused
assessment. L419 supplies the additional deterministic Borel branches.
For a prospective covariance, positivity and the strictly negative
trace of SJS must be verified before applying this interface. The
source supplies no continuous atom selection or calibration theorem.

C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, [published primary text](https://ems.press/content/serial-article-files/32047?nt=1),
Section 3, p. 1527, identity preceding Lemma 1 and (23), covers finite
Poisson character moments at radii below one. It is not a moving-height
error estimate. L440's finite-Fourier estimates and L442's quantitative
sine estimates are the available local moving-height inputs under the
original cutoff. No new prime averaging or actual sine moment is needed
merely to define exact finite-H residuals of the given law.

## Specialization obligations and duplicate comparison

L438 (4)--(7) already implements exact finite-height Gram calibration
for a different three-test signed cubic problem. It is a reusable local
method, not a solution of these covariance equations: the linear map,
admissible mean constraints and uniform conditioning must be checked
for this block. Neither the number of free entries nor the nonzero
limiting y-squared defect proves full rank or incompatibility.

L441 (2)--(13), with its step-263 audit, supplies exact conditional
raw-second change w times the covariance perturbation, original
positivity/negative-trace margins, translated six-state support and
bounded-covariance moment estimates. The proof treats a specific xy
matrix. Any extension to other allowed entries must verify the
corresponding matrix bounds rather than cite that conclusion without
checking scope. Reusing central-symmetry estimates avoids assuming
continuity or closeness of the newly selected atoms.

The later attempt must preserve all six integrated raw seconds exactly,
including the two tiny odd tolerances; a bounded integrated error is
not allowed. It must preserve the 11 raw entry at every height, hence
the original x-second correlations, and keep the mean m and first B
mean exact. Check the first D tolerance, all 23 quartics, the three
original cubic remainders and every separately fixed three-prime cubic
limit, fixed envelopes, strict negative bulk support and the same-family
capped absolute cubic for every fixed cap. Verify joint Borel dependence
and one common support onset; no cross-H trajectory consistency is
imposed. These are pending checks, not conclusions of this review.

L441 and L442 give the three complete old residual asymptotics, hence
boundedness of the eventual residual vector; they do not give an exact
right inverse. Retain every rare second, translation, full covariance
and slow derivative in the new exact equations. An asymptotic replacement
may help prove uniform conditioning but cannot replace the finite-H
equalities being solved. Do not infer actual sine limits or independence
from central symmetry.

Scoped searches covered the step-261 attempt, step-263 audit history,
step-265 calculation record, step-267 audit history, relevant canonical
ranges and `ATTEMPTS/2026-10-19-full-poisson-law-gaussian-occupation.md`.
No completed exact simultaneous repair was found in these records.
L439 stops a different fixed-Gaussian nonzero-limsup diagnostic.
L440's unchanged-law separation, L441's one-test asymptotic repair and
L442's unchanged-repair y-squared separation retain their exact scopes.
L428's bounded normalized x-density obstruction remains valid; this
target keeps the growing Poisson x-second density unchanged. Historical
stops are neither erased nor treated as a ban on this different test.

External locator queries were `"occupation measures" "covariance"
"moment constraints" projection`, `"equality constrained least norm"
"full row rank" Boyd`, `"covariance" "occupation" "Riemann" quadratic`,
`"quadratic occupation" "covariance" repair`, and `"bounded" "moment
constraints" "Gram matrix" projection`. Most hits concerned unrelated
stochastic occupation covariance or numerical moment matching. These
are not imported inputs. Exact terminology and the stronger standard
linear-equality result led to the inspected primary source above;
no absence or originality claim follows from the search.

## Decision and continuation boundary

SPECIALIZE makes exactly TARGET ready for a later RESEARCH /
REPRODUCTION attempt, subject to the supervisor's separate approval of
this newly completed assessment. The elementary application may succeed
or produce an informative obstruction. No new law, lemma, mathematical
script, DAG edge or proof-assembly claim is established here.

Essential continuation inputs are L419's exact J,b,K and Borel
realization; L424 ordinary dynamics; L438 full matrix and tolerances;
L440 complete x-squared residual and averaging; L441 audited bounded
stability; L442 audited remaining residuals; L429 original cutoff through
those interfaces; and the primary projection citation above.
Unresolved: exact uniform block feasibility, preservation for a changed
covariance, other occupation tests, actual sine limits, growing-character
uniformity, actual/global realization, clipping, capped nondegeneracy,
L413's full-error regulator margin and global mixed positivity.
Full matching Mathlib coverage has not been checked; this is not evidence
of absence. Existing local Mathlib qualifications remain unchanged.
