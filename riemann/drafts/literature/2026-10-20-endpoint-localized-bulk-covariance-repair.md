# Source comparison: changing the endpoint density

TARGET: Review source coverage for an endpoint-localized change of L443's bulk covariance that enforces L446's scalar constraint J(H)=0 while preserving the exact integrated second matrix, strict negative bulk support and all selected moment tolerances.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 284 searched smooth endpoint interpolation with prescribed integrals, positive matrix interpolation with moment constraints, prescribed smooth moments and Schur--Horn support realization; compared L443 (1), (14)--(20), L445's pointwise density, L446 (2), (12)--(17), L438 (9)--(20), L429's envelope interface and the two exact failure records. No inspected theorem supplies this full supported endpoint repair; no novelty inference is made.
SOURCE_EVIDENCE: Freshly read Hunter, author-hosted Chapter 1, Theorem 1.29 and its convolution proof, Example 1.30, printed p. 12; Boyd--Vandenberghe, Convex Optimization (2004, corrected seventh printing 2009), sections 2.2.5--2.3.1, printed pp. 34--36, including the quadratic-form convexity proof. Reuse the precise Boyd right-inverse, Carlen--Lieb real Horn, Hunter/Bell endpoint and finite Poisson coverage in the ready assessments identified below.
COMPARISON: Smooth cutoffs provide localization, matrix-cone convexity permits interpolation only between already admissible matrices, and full-row-rank projection provides exact linear correction only after rank and size checks. Real Horn and L419 provide supported realization after quantitative covariance/trace checks. None controls this law's full rare endpoint terms, recentering costs or all-real-H preservation estimates; L444 and L446 do not cover changed entry 11.
GAP: One later attempt must construct or obstruct endpoint-localized covariance interpolation with exact J(H)=0 and exact integrated seconds, quantitative translated support, fixed envelopes and every selected tolerance under the original cutoff; full rare endpoint values and any loss of the finite occupation block must be tracked explicitly.
REASON: Essential source coverage is adequate for the covered mathematical target. The unresolved endpoint range, conditioning, peak-size, recentering and tolerance estimates are law-specific mathematical obligations, not an essential unread theorem. SPECIALIZE approves an attempt, not existence, a formula or an obstruction.
SCOPE: Only the scalar endpoint repair by changing bulk covariance, including entry 11, on endpoint neighborhoods with an exact weighted mean correction; unchanged high and both intermediate components, masses, mean, actual response and original L429 cutoff. The old three finite occupation identities are a separate preservation question, not an inherited conclusion. No all-temporal or trajectory realization is covered.
COVERED_TARGET: Construct or obstruct an endpoint-localized bulk covariance repair of L443 with L446's exact J(H)=0, the exact integrated second matrix, strict negative bulk support and every original selected tolerance on one eventual real-H ray.
LITERATURE_REASON: Entry 11 is now allowed to change near the temporal endpoints, with covariance and support constraints absent from L446's scalar audit; this is an uncovered target, not additional review of the ready unchanged-density target.

The following initial proposal is retained as the scope record. Its
pending-review sentences are superseded by the completed review below;
no mathematical construction has been added.

The main gap is global mixed positivity. The proposed intermediate
target tests whether the newly audited endpoint obstruction can be
removed inside a supported selected-moment law. Its downstream use
would be to make a later all-temporal covariance test meaningful;
it would not itself solve that test or realize an actual trajectory.

Essential local inputs for the comparison are L446's exact functional
J and audited stop; L445's pointwise complete density and fixed-H
regularity; L443's complete covariance and exact six second moments;
L438's full probabilities, mean/covariance corrections and tolerance
estimates; L429's original cutoff; and L419's covariance realization
with strict negative-discriminant support. L444's bounded zero-11
obstruction remains recorded. No cross-notebook input is proposed.

The later mathematical question, if source-approved, is existence on
one eventual real-H ray, not endpoint samples or an asymptotic J=o(1).
Endpoint neighborhoods may shrink with H; their widths and any
recentring must be quantified against every selected error allowance
and the fixed pointwise envelopes. The complete rare endpoint terms
must remain in J. Changing a density only at endpoint points is
inadmissible: the continuous representative and its weak derivative
must agree. The old exact finite occupation block is a separate
obligation to identify explicitly; its preservation is not assumed.

Continue only with adequate theorem coverage and a concrete candidate
whose exact J and full support/moment errors can be tested. A proved
incompatibility of those requirements would stop this changed-density
mechanism. Merely repeating L446 with fixed entry 11 would not test it.
No result or mathematical construction is derived in this placeholder.
In particular it is not a ready assessment.

Even success would leave the cross entry fixed by the new derivative,
its covariance feasibility, all temporal occupation identities, the
finite block if changed, actual/global realization, clipping, capped
nondegeneracy, L413's full-error margin and global mixed positivity
unresolved. Full matching Mathlib coverage has not been checked.

## Completed source comparison — step 284

This is LITERATURE / NOVELTY_UNCHECKED / literature_comparison,
with outcome EXPLORATION: new primary coverage and a delimited later
attempt, without a mathematical result or feasibility conclusion.
No lemma, mathematical script, DAG or PROOF change is made. Mathematical
exploration usage remains 0 of 3; this review neither spends nor resets
that budget. The newly ready continuation requires the supervisor's
separate next-turn approval; this review does not invoke mathematics.

### Newly inspected localization and matrix sources

J. K. Hunter, *Notes on Partial Differential Equations*, author-hosted
[Chapter 1, section 1.9.1, Theorem 1.29 and Example 1.30, printed p. 12](https://www.math.ucdavis.edu/~hunter/pdes/ch1.pdf#page=13).
The separately served chapter's revision date is not displayed in the
retrieved passage; the compiled notes identify revision 18 June 2014.
The theorem requires open sets Omega' compactly contained in Omega,
and provides a smooth compactly supported function in Omega, valued
in [0,1], equal to one on Omega'. Its proof convolves the indicator
of a distance neighborhood with a standard mollifier. Example 1.30
gives a first-derivative bound inversely proportional to the gap
between concentric radii. The complete theorem, proof and example
were read. In one dimension, endpoint neighborhoods can be taken in
the ambient real line before restriction to the closed time interval;
an interior-only cutoff would not change the endpoint values. This
source prescribes neither an integral nor an admissible covariance.
Import the cutoff theorem rather than reprove it. Parameter scales,
Borel dependence and all integral costs remain application obligations.

S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge University
Press, 2004, corrected seventh printing 2009,
[sections 2.2.5--2.3.1, printed pp. 34--36](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=48).
Read the real symmetric positive-(semi)definite definitions, the
quadratic-form proof that nonnegative matrix combinations stay
semidefinite, and preservation of convexity under intersections.
These tools concern matrix feasibility and affine constraints; they
do not prove that a prescribed affine slice is nonempty. Strict
eigenvalue and negative-trace margins, including after a signed
mean correction, must be verified in the application. No interpolation
or convex optimization existence theorem for the present law is imported.

The compiled Hunter PDF had inconsistent targeted retrieval, but the
author's separate chapter supplied the full needed passage. No
essential source blocker remains. Dyatlov's Lecture 1 PDF was located
but its relevant proof was not inspected; Lee's cutoff proposition
was only a locator lead. Neither is theorem evidence here.

### Ready coverage reused without new derivations

`drafts/literature/2026-10-20-exact-quadratic-block-covariance-repair.md`
records Stephen Boyd, EE263 Autumn 2007--08, Lecture 8,
[slides 8-2--8-7 and 8-9](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/min-norm.pdf).
For a real full-row-rank matrix A, the minimum-norm right inverse is
A^T(AA^T)^(-1). The assessment inspected the orthogonality proof and
nullspace projection. Reuse this result for any proposed finite
correction space, after checking rank and uniform conditioning. It
supplies no positivity, support or sup-norm bound for coefficient fields.
No reproof or automatic extension of L443's triangular map is justified.

`drafts/literature/2026-10-20-prime-two-occupation-covariance-repair.md`
records E. A. Carlen and E. H. Lieb,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), 13 May 2009,
Horn theorem following (1.1), pp. 1--2, full proof through (1.2).
Real orthogonal diagonal realization requires majorization; the
inspected proof includes the two-dimensional equality case and
induction. For a candidate covariance Sigma, L419's deterministic
Borel branches and translated six-state interface remain the local
implementation. Positive definiteness and a sufficiently negative
trace of Sigma against the discriminant matrix must precede use of
that interface. Constant-diagonal realization alone does not control
the translation or any moments beyond the covariance.

`drafts/literature/2026-10-20-complete-x-second-integrated-xy-compatibility.md`
records Hunter's Theorems 3.60, 3.62--3.63, printed pp. 79--80,
and Bell's 2015-10-21 Section 1, Theorem 1 and derivative uniqueness.
Their AC representative and endpoint hypotheses are unchanged.
L446 (2) is the already proved exact scalar functional to test; no
new compatibility criterion is derived in this review. A changed
pointwise density must still be AC on the whole closed interval.

The same exact-block assessment records the necessary occupation
identity in Lasserre--Henrion--Prieur--Trelat, math/0703377v1,
sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5, and the finite
Poisson identity of Aistleitner--Berkes--Seip, JEMS 17 (2015),
section 3, p. 1527. Reuse this coverage if needed; no stronger
occupation-measure converse, new sine coefficient or growing-prime
averaging theorem is required or supplied for the scalar test.

### Comparison, candidate mechanism and bounded test

The searched terminology included smooth interpolation with prescribed
integrals/moments, matrix interpolation under positivity and integral
constraints, and prescribed covariance with quadratic-cone support.
The searches located scalar functional-interpolation and matrix
transport leads, not an inspected matching theorem. In particular,
*Theory of Functional Connections Extended to Continuous Integral
Constraints*, Math. Comput. Appl. 30 (2025), 105,
[publisher page](https://www.mdpi.com/2297-8747/30/5/105), returned HTTP
429 on opening. Its search extract is not theorem evidence; no claim
about its hypotheses or positivity conclusions is relied upon.
Resolving that optional lead is not essential to use the elementary
primary inputs above. Failed search and unread leads prove no novelty.

L443's exact finite repair has zero 11 entry. L444 excludes uniformly
bounded zero-11 all-temporal repairs; L446 excludes even integrable
cross entries when the entire 11 density is fixed. Preserve the two
failure records in ATTEMPTS. Allowing continuous endpoint-neighborhood
changes of entry 11 is a materially different and testable scope.
L445 establishes regularity of the old density only, not feasibility
of a new endpoint interpolation. L438's finite cubic Gram calibration
is a method precedent, not a duplicate solution of this target.

One candidate for the later attempt is cutoff interpolation of the
bulk covariance near the two temporal endpoints toward positive
multiples of L419's K, together with an exact weighted matrix
recentering/correction. This is a proposed ansatz only: no endpoint
levels, widths, coefficient map, attainable interval or solution are
computed or asserted here. It must retain the complete rare raw
matrix, w and m. The proof attempt should first test whether this
admissible endpoint range can enforce exact J(H)=0 after recentering,
then check the full support and moment budgets. Failure of this
particular ansatz alone would not rule out every changed covariance.

In particular L446 (15)--(17) control rare endpoint errors in an
outer-H average, not pointwise at every H. They do not permit dropping
rare endpoint terms or assuming the old polylogarithmic covariance
norm suffices for a repair. Any larger endpoint peaks require their
own fixed-envelope, translated-support and integrated-moment estimates.
Shrinking width alone does not control the new derivative or prove
positive covariance for the derivative-forced cross entry.

The quantitative preservation checklist is the existing one in L438
(18)--(20) and L443 (17)--(20): all six integrated seconds exactly,
including zero odd entries; unchanged mean and first B value;
first D with its original o(ell) error; W^2 and every fixed-prime
x-second correlation at o(ell); the three original cubic O(ell)
remainders and every separately fixed three-prime cubic coefficient
at o_v(ell^2); all 23 quartic coefficients at o(ell^4); absolute
third/fourth and pointwise physical envelopes; and one family's
capped absolute cubic o(ell^2) for every fixed positive cap. Here
ell=log H. Exact weighted recentering cannot be replaced by a small
error against the tiny odd-second allowances. The former finite
occupation block is an additional equality block: preservation or
loss must be stated, not silently inherited from L443.

Continue only with a rigorous full-real-H construction satisfying the
covered target, or an independently checkable obstruction identifying
which allowed range or budget fails. Exact J=0, not J=o(1), is the
threshold. Stop a particular endpoint ansatz upon a proved unavoidable
failure of its endpoint range, support or tolerance budget; an unchecked
estimate is unfinished work, and a universal stop requires an argument
covering all allowed repairs. No new lemma or script is approved merely
to accumulate outputs. Full matching Mathlib coverage is not checked;
these sources establish supporting tools only. No originality claim,
RH improvement or actual clipping/realization conclusion follows.
