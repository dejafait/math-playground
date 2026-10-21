# Source comparison for a width-one endpoint variant

TARGET: Test whether L447's width-one variant preserves the selected constraints and has a positive-semidefinite derivative-forced bulk x,y block, with the rare components and bulk mean fixed.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 292 compared L447's complete construction and moment budgets, L448's centered-block obstruction and recorded stop, L438 (9)--(20) and cap/envelope bounds, and L443/L445/L446 interfaces against the three reusable source assessments below; fresh queries for prescribed variance/derivative covariance and endpoint occupation-measure covariance returned no inspected theorem deciding this law.
SOURCE_EVIDENCE: Reuse the inspected Hunter cutoff Theorem 1.29/Example 1.30 p. 12 and weak-derivative/AC Theorems 3.60, 3.62--3.63 pp. 79--80; Boyd--Vandenberghe (2004, corrected seventh printing 2009) pp. 34--36 and Appendix A.5.5 pp. 650--651; Carlen--Lieb arXiv:0904.0734v2 pp. 1--2; Bourgain arXiv:1408.5794v2 Theorem 5 (0.5) p. 2 and completion cases p. 19; DLMF 1.9.30--31, 5.5.1 and 5.11(i)--(ii), with applicability and reuse records below.
COMPARISON: These sources cover fixed-width cutoffs, matrix positivity, finite-dimensional realization and AC/PSD interfaces without an H^-10 hypothesis. They do not prove the changed-width amplitudes, moment costs, translated support or forced-cross PSD; L447 and L448 prove only their original-width conclusions.
GAP: A later mathematical attempt must recompute all width-dependent bounds and test the complete centered forced block after rare/mean subtraction; neither success nor failure for width one is established here.
REASON: Width one changes the endpoint transition and integrated peak costs outside prior local conclusions, while retaining the same source hypotheses; a local specialization is necessary, with no reproof of imported general theorems.
LITERATURE_REASON: The changed width is outside the original-width assessments' approved targets; this turn compares that changed hypothesis and reuses their essential inspected sources rather than repeating their retrieval.
SCOPE: Only delta=1 in L447's defining formulas, with original cutoff, rare components, probabilities, w and bulk mean fixed; selected-constraint retention and the necessary centered x,y block test, without independent enlargement of y variance or global realization.

The main gap remains global mixed positivity. The proposed intermediate
target changes only L447's width to delta=1 and recomputes its amplitudes,
weighted recentering and finite correction by the same defining formulas.
Keep the original L429 cutoff, high and both intermediate components,
their probabilities and w, and L438's bulk mean. Use the resulting raw
x- and y-second entries as the fixed diagonals for the proposed test;
do not independently enlarge the y-second entry. Do not assume that
the resulting covariance, support or selected moment tolerances pass.

Essential local inputs are L438, L443, L445, L446, L447 and audited
L448, with L366/L391 for quantitative temporal control if needed.
The previous relevant source records are
`drafts/literature/2026-10-20-endpoint-repair-critical-audit.md`,
`drafts/literature/2026-10-20-endpoint-repair-forced-cross-feasibility.md`
and `drafts/literature/2026-10-20-endpoint-forced-cross-critical-audit.md`.
Reuse their inspected results where hypotheses match. The completed comparison below assesses this changed scope. This
literature turn derives no changed-width estimates; mathematical work
requires the supervisor's separate next-turn approval.

The downstream use is deciding whether a slower endpoint correction
can survive this necessary covariance test while retaining the
selected-law obstruction. The eventual mathematical pass threshold is
all selected tolerances together with PSD of the complete centered
forced x,y block a.e. in time on an eventual real-H ray. Rigorous
failure on positive-measure temporal sets for arbitrarily large H,
or failure of a required selected constraint, would stop this specific
variant. Endpoint samples or estimates that merely fail to prove PSD
would not establish failure. No inequality for this variant is derived
here, and no expectation of a pass is asserted.

Preserve L448's H^-10 stop and L444/L446's original scopes. Even a
pass would leave the other covariance entries and temporal identities,
mean transport, inter-H consistency, actual/global realization,
clipping, capped nondegeneracy, L413's full-error regulator margin and
global mixed positivity unresolved. Matching Mathlib coverage is
unchecked. This proposal does not assert a new law or RH candidate.

## Completed comparison — step 292

LITERATURE / NOVELTY_UNCHECKED / literature_comparison; outcome
EXPLORATION. This is an actual source-scope comparison, not a repeated
approval, mathematical result or novelty finding. No new lemma,
mathematical script or width-one inequality is established.

### Reused primary theorem hypotheses and application limits

The three source records named above contain the inspected primary
statements and essential proof cases. They are reused, with no claim
of fresh external retrieval. Their original approved targets do not
silently expand: this assessment explicitly covers the changed target.

[Hunter, Notes on Partial Differential Equations, Chapter 1,
Theorem 1.29 and Example 1.30, printed p. 12](https://www.math.ucdavis.edu/~hunter/pdes/ch1.pdf#page=13)
provide a smooth cutoff between compactly nested open sets, valued
in [0,1] and equal to one on the inner set. The compiled notes have
revision 18 June 2014; the separately hosted chapter is undated.
The convolution proof and example were inspected in the source record
reused by the endpoint audit. The same fixed real-line rho may be
restricted to either endpoint after translation at fixed width; no
width-dependent hypothesis of this existence theorem changes.
This supplies a cutoff, not a moment-preserving or PSD interpolation.

[Boyd--Vandenberghe, Convex Optimization (2004, corrected seventh
printing 2009), sections 2.2.5--2.3.1, pp. 34--36](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=48)
cover convexity of the real positive-semidefinite cone.
[Appendix A.5.5, pp. 650--651, (A.13)--(A.14)](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=664)
covers the block Schur-complement test: for positive definite A,
PSD is equivalent to C-B^T A^(-1)B being PSD; for singular A it also
requires A PSD and range(B) contained in range(A), with the generalized
inverse in the complement. The quadratic minimization and singular
cases were inspected in step 288. The scalar case tests nonnegative
diagonals and B^2<=AC, with B=0 if either diagonal vanishes. Neither
cone convexity nor this exact test assumes a small temporal width.
They do not bound the signed recentering/correction or evaluate the
new matrix entries. The complete raw rare cross and translation must
be subtracted before testing the centered bulk block; positive raw
seconds alone are insufficient. Do not assume strict diagonals for
the changed law merely because L447 proved them for its old width.

[Carlen--Lieb, Short proofs of theorems of Horn and Mirsky on diagonals
and eigenvalues of matrices, arXiv:0904.0734v2, 13 May 2009,
pp. 1--2](https://arxiv.org/pdf/0904.0734v2), Horn theorem following
(1.1), proof through (1.2), supplies the real diagonal/eigenvalue
majorization theorem, including the scalar/equality case and induction.
It can be imported for L419's six-state realization only after the
changed covariance is positive and the trace and translation margins
are proved. Its theorem supplies neither a measurable parameter
selection nor negative support after translation; L419's existing
Borel implementation handles the former. L443's unchanged triangular
finite correction uses the same w and correction space. Its already
proved inverse and conditioning, with supporting Boyd EE263 Lecture 8
slides 8-2--8-7 and 8-9 in the endpoint audit record, require no new
rank theorem. The changed residual and its size remain to be checked.

[Hunter, compiled notes, Definition 3.1 pp. 47--48 and Theorems 3.60,
3.62--3.63 pp. 79--80](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf)
and [Bell, Sobolev spaces in one dimension and absolutely continuous
functions, 21 October 2015, Section 1 Theorem 1 and subsequent uniqueness
paragraph](https://jordanbell.info/LaTeX/mathematics/sobolev1d/)
cover locally integrable weak derivatives, AC reconstruction,
uniqueness and integration by parts with both endpoint terms.
These hypotheses are unchanged at each fixed H: the new density must
have its specified Lipschitz representative, and L=log(2+t) is smooth
and strictly positive on the compact interval. All stage parameters,
amplitudes and height integrals are held constant in t. L445/L446's
interface then applies; their old-density obstruction does not transfer
automatically. No atom derivative, H derivative or uniform Lipschitz
constant is assumed. [Lasserre--Henrion--Prieur--Trelat,
arXiv:math/0703377v1, sections 2.1--2.3, (2.7), (2.10)--(2.12),
pp. 3--5](https://arxiv.org/pdf/math/0703377v1) supplies only the necessary
finite-interval C1 occupation identity, on compact boxes at fixed H,
as already specialized in L443/L446; it is not a converse realization
theorem. All these passages were inspected in the reused assessments.

[Bourgain, Decoupling, exponential sums and the Riemann zeta function,
JAMS 30 (2017), 205--224, arXiv:1408.5794v2, Theorem 5 (0.5),
p. 2](https://arxiv.org/pdf/1408.5794v2#page=2) gives the unconditional
critical-line bound with exponent 13/84+epsilon for each fixed positive
epsilon. The original inspections include completion cases (4.1)--(4.3),
p. 19. Its hypotheses are unaffected by changing the artificial width.
L447 uses it only for the scalar actual peak; L391 supplies the audited
strip/disk interface for ordinary jets if needed. [DLMF 1.9.30--31](https://dlmf.nist.gov/1.9.E31)
covers Cauchy derivatives of every fixed positive integer order for an
analytic function on a contour and its interior; [5.5.1](https://dlmf.nist.gov/5.5.E1)
and [5.11(i)--(ii)](https://dlmf.nist.gov/5.11) cover gamma recurrence and
sector-qualified Stirling/psi expansions with complex remainders.
Those passages were read in step 290. Pole-free disks, branches and
normalizations remain local obligations. Import these results rather
than reprove them. They supply no pointwise sign for the forced block.

### Exact difference to test and prior failures

Read L447's endpoint definitions, recentering, correction and complete
support/moment proof, L448's centered test and modulus mechanism,
L438 (9)--(20) and its cap/envelope bounds, and the relevant L443,
L445 and L446 interfaces. No existing local theorem read decides this
width. In particular every width-dependent estimate in L447 (7)--(16),
(18)--(21) needs an applicability check or recomputation; do not copy
its H^-10 powers. The original selected list includes exact integrated
seconds/first B, all three finite occupation equalities, first D and
weighted seconds at their original tolerances, the signed cubic
remainders and every separately fixed three-prime character, all 23
quartics, both third envelopes, fixed physical bounds, strict support,
and the same-family capped absolute cubic for every fixed cap.
A bulk covariance that exists before imposing the forced cross is not
already evidence that the latter is PSD.

The recorded L448 stop in
`ATTEMPTS/2026-10-20-endpoint-repair-fixed-data-forced-cross.md`
uses its narrow layer together with a quantitative old-density modulus.
That proof does not decide a unit layer. L444's uniformly bounded
zero-11 stop and L446's unchanged-density endpoint stop remain intact,
but neither rules out this changed density. L447 is a valid scalar
and finite-test repair at its original width, not a duplicate proof
of the proposal. No historical stop is promoted to a global prohibition.

The fresh bounded search used the exact queries
`"prescribed variance" "derivative" covariance positive semidefinite`
and `"endpoint" "covariance" "occupation measures" positive semidefinite`.
Results did not identify an adequate matching primary theorem; unrelated
snippets were not treated as evidence or read as mathematical inputs.
Reuse of the primary statements above is the substantive coverage.
No novelty inference follows from those searches. Mathlib full matching
coverage is unchecked, not established absent.

The pass/stop thresholds and unresolved downstream gaps stated above
remain unchanged. A coarse bound that is merely too large to prove
PSD is inconclusive. This SPECIALIZE decision approves only a later
known-tool application, classified REPRODUCTION, after separate
supervisor approval. It asserts no success for the changed width.
