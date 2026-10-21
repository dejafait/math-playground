# Source coverage: bounded covariance repair of the prime-2 identity

TARGET: Test whether a bounded prime-2-dependent off-diagonal bulk covariance correction can make L440's residual o(1) while preserving every L438 selected constraint and the original cutoff.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 260 searched occupation/covariance/Schur--Horn combinations, prescribed-covariance negative quadratic support and Riemann/occupation/jet moments; compared L419, L438 (9)--(20) and tolerance bounds, L440's raw-second and weighted-Poisson interfaces, the step-154/209/248/256 assessments and scoped lift/Gaussian failures. No inspected theorem covers this complete changed-law target; no novelty is inferred.
SOURCE_EVIDENCE: Freshly inspected Carlen--Lieb arXiv:0904.0734v2 (13 May 2009), Horn theorem following (1.1), full two-dimensional and inductive proof through (1.2), pp. 1--2; reuse the inspected Lasserre--Henrion--Prieur--Trelat C^1 finite-interval identity, finite Poisson identity and compact-group/nonstationary sources recorded below.
COMPARISON: The sources cover necessary occupation identities, pointwise real matrix realization and finite-product averaging. L419 supplies the additional Borel construction; L438 supplies strict margins and full moment-calibration interfaces. None supplies a bounded prime-2 correction with all preserved constraints or an actual trajectory. A law-specific specialization remains necessary.
GAP: Find or obstruct a uniformly bounded off-diagonal correction and its constant integrated recentering; verify the complete residual is o(1), covariance positivity, translated negative support, exact six seconds, both first-mean requirements, every cubic/quartic tolerance and the cap bound on the full eventual real-H ray.
REASON: Essential source coverage is sufficient for one later bounded specialization attempt on the exact TARGET. Import the standard theorems and reuse the canonical local interfaces; this review proves no perturbation formula, cancellation, feasibility or obstruction.
LITERATURE_REASON: The invocation target was REVIEW_REQUIRED because changing the law was outside L440's audit; this turn compares that changed scope while reusing ready occupation, Poisson and matrix assessments.
SCOPE: An absolutely uniformly bounded symmetric correction confined to the bulk (x,y) entries, plus the constant matrix recentering required by integrated raw seconds; unchanged height/response marginal, high and both intermediate components, original L429 cutoff and all L438 selected tolerances. No relative or logarithmically growing perturbation, new actual moment or trajectory realization is covered.

## Relevance and discriminating test

The main gap remains global mixed positivity. The intermediate target tests
whether L440's additional-identity obstruction is robust under this one
change of covariance. Its plausible downstream use is to distinguish a
constraint on the selected relaxation from a defect of one representative,
and to guide later trajectory tests. It is not an RH completion mechanism.

Continue only if one explicit supported family has complete residual o(1),
all six integrated raw seconds exact, and every original tolerance and
capped-cubic conclusion intact for all sufficiently large real H. Stop this
restricted repair if the necessary size violates its absolute boundedness,
positive definiteness, translated negative support or a selected tolerance,
or if a nonzero residual remains. An unchecked preservation estimate is an
unfinished obligation, not proof of impossibility. Even success matches only
this asymptotic test, not every exact finite-H identity.

## Primary matrix input and its boundary

Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2),
13 May 2009, pp. 1--2, Horn theorem following (1.1), proof through (1.2).
For finite real lists, majorization of the desired diagonal by the
eigenvalues is necessary and sufficient for real orthogonal realization.
The inspected proof includes the two-dimensional rotation and induction
with a matched coordinate removed. The equal-eigenvalue two-dimensional
case needs no division; it is already scalar. The cited original is
A. Horn, *Doubly stochastic matrices and the diagonal of a rotation matrix*,
Amer. J. Math. 76 (1954), 620--630, reference [2]; it was not independently
read. Import the real theorem, not the separate Mirsky statement.

For a prospective changed covariance the relevant matrix remains real
symmetric S J S. Constant-diagonal applicability and strict negative trace
must be checked. Pointwise existence is insufficient for a Borel kernel;
reuse L419's deterministic finite branches, including ties. No continuity
of those branches, eigenvector selection or covariance-repair theorem is
asserted by this source. No reproof of Schur--Horn is needed.

## Ready occupation and averaging coverage reused

The precise primary record is
`drafts/literature/2026-10-19-prime-two-quadratic-occupation-test.md`.
J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
13 March 2007, Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5,
supplies the C^1 finite-interval necessary identity with endpoints.
At fixed H the trajectory and conditional states fit finite compact boxes.
The same phi_H and zero-extended eta retain their regularity; changing
conditional moments does not require a stronger identity. No uniform
compactness, sufficiency, no-gap theorem or critical trajectory is imported.
No derivative of the changed kernel or cutoff belongs in this identity.

C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, Section 3, p. 1527, identity preceding Lemma 1
and (23), [published primary text](https://ems.press/content/serial-article-files/32047?nt=1),
supplies the finite Poisson character formula. Reuse the inspected proof
record in `drafts/literature/2026-10-18-growing-prime-poisson-covariance.md`
and the step-252/256 assessments. Each product is finite and each radius
is below one. No infinite critical-line product is involved.

L440 (8)--(10) and its audit already establish the finite-Fourier tail
and frequency-separation bounds under the unchanged cutoff, followed by
the eta-weighted cosine limit. These are available local results, not an
invitation to strengthen the cutoff. Further oscillatory weights must be
justified within those estimates or directly. The compact-group criterion
and sharp nonstationary estimates in
`drafts/literature/2026-10-17-covariance-free-bulk-phase-averaging.md`
remain supporting coverage: Kowalski (19 January 2021), B.6.3/B.6.5/B.6.6,
pp. 146--147, and Tao, *Lecture Notes 8 for 247B* (2007), Lemma 2.3,
pp. 4--5. Qualitative fixed-test convergence is not a moving-test theorem.
No new actual sine coefficient, independence or conditional moment is needed
or authorized by this comparison.

## Local specialization still required

L438 (9)--(20) fixes the rare states, w, normalized g_H, bounded mean,
full constant correction and covariance. Its existing lower-eigenvalue
and negative-trace margins, translated support bound and moment estimates
are inputs to a later comparison, not results already proved for a changed
law. L419 supplies exact J, b, K and its general six-state implementation.

The later attempt must specify the changed conditional covariance and
constant integrated recentering together. Preserve all six raw second
entries exactly, including both tiny odd tolerances, rather than charging
a bounded conditional error to an asymptotic global allowance. Check
positive covariance and the negative quadratic value of every translated
atom with one eventual onset, Borel dependence through ties, both first
means at their original tolerances, all 23 quartics, original cubic
remainders and every separately fixed three-prime cubic character limit.
The same family must retain fixed-prime x-second limits, the response
correlation, fixed envelopes and vanishing capped absolute cubic for every
fixed cap. Changes to atom directions need fresh moment estimates; no
closeness of selected bases or implicit continuity through ties is assumed.

For the residual, retain all L440 terms: compact-height derivatives,
the x-second entry, signed cross seconds of both intermediate directions,
the high component, mean and entire recentering. Matching only one formal
leading coefficient does not discharge the test. No coefficient, size,
perturbation formula or new bound has been derived in this literature turn.
These are elementary finite-matrix and finite-height specialization
obligations with adequate source coverage, not missing external theorems.

## Discovery, duplicates and recorded failures

Queries run on 20 October 2026 were `"occupation measures" "covariance"
"Schur" "Horn"`, `"Schur Horn" prescribed covariance quadratic form
negative support`, and `"Riemann" "occupation" "covariance" jet moment`.
The exact combination yielded no matching inspected theorem. Broader hits
included Antezana--Massey--Ruiz--Stojanoff, arXiv:math/0508646, on prescribed
frame norms/operators, and Leite--Richa--Tomei (1999), on geometric
Schur--Horn proofs. These are unread leads, not stronger inputs. Search
snippets and general reference pages are not used as theorem evidence.
The two-page primary matrix source above was inspected directly.

The step-154 matrix and step-248 full-law assessments already separate
pointwise matrix realization from Borel support/calibration. Neither
constructs this changed law. L440 and step 259 reject only the unchanged
law; its constant old cross correction is not a theorem that every
height-dependent bounded cross correction has negligible effect.
L439 and `ATTEMPTS/2026-10-19-full-poisson-law-gaussian-occupation.md`
stop the Gaussian nonzero-limsup diagnostic, not this polynomial repair.
The sign-only and capped-radial records of 16 October concern different
restrictions; their exact odd-second and cubic-calibration failures warn
against weakening the present requirements. L428's bounded normalized
x-second-density obstruction remains valid; this target retains L429's
Poisson product and does not propose such a uniform normalized bound.
No historical stop is erased or converted into a global ban.

## Decision and continuation boundary

SPECIALIZE permits one later mathematical attempt, after the supervisor's
separate approval, using the existing named sources and canonical local
interfaces. A REPRODUCTION classification is appropriate for a construction
using only these finite-matrix/calculus specializations; the review makes
no originality claim. Adequate coverage is not a feasibility certificate.
No lemma, mathematical script, DAG edge or argument in PROOF.md changes.

Essential continuation inputs: L440's audited complete residual; L438
(9)--(20) and full tolerance/cap bounds; L419 exact forms, K and Borel
six-state realization; L429 unchanged cutoff; L421 and L437 high and both
intermediate interfaces through L438. Unresolved: the repair itself,
actual/global realization, actual clipping, capped nondegeneracy, L413's
full-error regulator margin and global mixed positivity. Full matching
Mathlib coverage is not checked; generic matrix/calculus support would
not formalize this law comparison.
