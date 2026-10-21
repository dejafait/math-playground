# Coverage: finite nonnegative three-prime witness

TARGET: Construct a fixed centrally symmetric nonnegative trigonometric polynomial with strictly negative integral against L435's density, with an exact finite-character certificate.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 239 checked the named local prime-route assessments, L431/L432/L434/L435 and October-18 histories/failure record; searched product Fejer localization, negative signed densities, quantitative approximation and the exact cubic scope; inspected the primary statements and relevant proof cases below. No inspected source supplies this density's effective certificate; no novelty inference follows.
SOURCE_EVIDENCE: Huang, A generalized Fejer's theorem for locally compact groups, March 17 2016 author manuscript, Definition 2.1 and Propositions 2.2--2.3 pp. 4--5, Theorem 3.1 pp. 7--9, Corollary 4.1 p. 11; Rodriguez, MIT 18.102 Spring 2021 Lecture 16, Theorem 174 pp. 85--86. Reuse audited L435's complete density/character interface and the prior analytic assessments.
COMPARISON: Known product-kernel localization covers the qualitative approximation mechanism. L435 meets its boundedness and continuity hypotheses; the remaining work is an effective specialization and exact finite integral, not a new general approximation theorem. L431's calibration and L432's positive prefix are narrower contrasts, not barriers to this three-prime test.
GAP: Choose one fixed centrally symmetrized translated product kernel, justify its finite cosine expansion, prove a sufficient degree/error bound from L435's explicit rational factors or absolute coefficient series, and certify the complete finite integral strictly below zero. No degree, polynomial, new bound or integral is established in this review.
REASON: This separate literature-only step completes the missing source comparison for the unchanged saved target; essential coverage is ready for one SPECIALIZE research attempt using imported kernel results and only the stated local quantitative specialization.
LITERATURE_REASON: The step-238 assessment expressly excluded finite nonnegative witnesses and had not assessed quantitative localization or finite certification; this review fills that essential changed-target scope.
SCOPE: One fixed centrally symmetric nonnegative trigonometric polynomial on the three-torus, a rigorous strictly negative integral and finite-character certificate; no law construction, actual sine limit, growing-character uniformity, actual clipping or regulator conclusion.

## Completed comparison — 2026-10-18, step 239

LITERATURE / EXPLORATION / NOVELTY_UNCHECKED; actual task
literature_comparison. This is new source-scope coverage, not a proved
witness or mathematical advance beyond the checked literature. No
lemma, mathematical script or certificate was written or run. The
original proposal below is retained as historical context; its request
for a literature-only invocation is discharged by this section.

### Primary inputs and their exact scope

Huichi Huang, *A generalized Fejer's theorem for locally compact
groups*, [March 17, 2016 author manuscript](https://huichihuang.wordpress.com/wp-content/uploads/2016/03/fejergr3.pdf),
uses T=R/Z and normalized Haar measure. Definition 2.1 requires bounded
L1 norms, mass one and vanishing absolute mass outside each identity
neighborhood. Proposition 2.2 gives a nonnegative mass-one kernel
with coefficients 1-|j|/(n+1), |j|<=n, and the bound
1/((n+1)sin^2(pi lambda)) on [lambda,1-lambda], 0<lambda<1/2.
Proposition 2.3 and its preceding display give the product kernel's
finite coefficients, nonnegativity and mass one. Corollary 4.1 applies
for d>=2 to bounded functions with all directional limits at the
evaluation point, returning their average. Read its proof and the
bounded-function part of Theorem 3.1, including both neighborhood and
complement estimates; no extra pointwise supremum-decay hypothesis is
needed in that part. These are imported tools, without a general reproof.

Casey Rodriguez, [MIT 18.102, Spring 2021, Lecture 16](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/eb44436072623f60f8f416875d4b2c11_MIT18_102s21_lec16.pdf),
Theorem 174, printed pp. 85--86 (PDF pp. 3--4), confirms uniform
one-dimensional Fejer convergence for continuous periodic functions.
Read the neighborhood/complement proof. Its kernel includes 1/(2pi)
against ordinary angular Lebesgue measure. The overview's whole-real-line
mass-one display and a repeated kernel in the proof's complement display
are not used as quantitative inputs; Huang supplies the unambiguous
normalization and tail bound. This auxiliary theorem alone is not the
three-variable effective certificate.

### Applicability and what remains to specialize

L435 proves continuity and joint absolute convergence, not merely
almost-everywhere convergence. Its density is bounded on the compact
torus, so it belongs to the bounded-function scope. Rescaling all three
angles by 2pi matches normalized Haar measure. Every directional limit
at its certified negative point equals its continuous value. Thus the
assessed product-localization hypotheses fit the proposed input;
neither positivity of W nor coordinatewise symmetry is required.
Use this existing theorem, rather than present the general finite
localization mechanism as new mathematics.

The source does not select an effective degree for L435 or evaluate
its integral. That difference is the approved local specialization:
retain the exact negative margin and normalization, bound the smoothing
error, and evaluate one finite coefficient contraction rigorously.
The quantitative ingredients are the cited kernel/complement bound
and L435 (3), (8)--(12), including its annular absolute generating
series. The next attempt may instead use the exact finite Fourier
weights and those generating series to obtain an effective coefficient
error; this is the same one-kernel implementation, not a second search.
No such estimate is derived or approved as a proved fact here.

Central symmetrization must be justified locally at the polynomial
level. It must preserve nonnegativity and the desired integral using
L435's central symmetry, without silently imposing separate reflections.
Its finite real cosine expansion must then be recorded completely.
Only after that polynomial and degree are fixed may L435 (1) be applied
to its finitely many characters. No infinite sum of physical limits,
actual sine limit or height-dependent degree is licensed.

Exact arithmetic can use the rational local generating functions with
algebraic phase coordinates from L435 (5); prove coefficient extraction,
nonzero denominators and any discarded tails. Finite convolution may
exploit product structure, provided it certifies the complete integral.
An algebraic sign certificate or rational outward enclosure strictly
below zero meets the threshold; a floating approximation does not.
No claim of optimal degree, efficient complexity or a new approximation
theorem is part of this scope. Reproof is justified only for these
specific normalization, effective-error and finite-arithmetic obligations.

### Search, reuse and failures

Local queries covered Fejer, nonnegative witness, finite witness,
product kernel, approximate identity and tail/coefficient terms in
October-18 literature/history paths and the relevant canonical files.
Read L435's full-density and negative-point argument, its fixed-character
qualifications, L431's degree normalization, L432's finite-prefix scope
and exact local-tail formula, and the two-prime failure record. The
step-217 one-variable Fejer--Riesz assessment and steps 235/238 supply
reusable comparison and audit context, not the missing effective witness.
No cross-notebook input was used. General analytic moment sources in
L406--L409/L434 are reused, not reopened or reproved.

External queries included `Fejer kernel approximate identity quantitative
uniform convergence product torus lecture notes pdf`, `nonnegative
trigonometric polynomial negative continuous signed density Fejer kernel
positivity measure`, `Fejer negative density trigonometric polynomial
measure`, and `Fejer cubic zeta witness`. The inspected primary match
covers the standard construction; no inspected theorem supplies this
specific arithmetic certificate. Unrelated zeta/zero-free-region hits
are not inputs, and unsuccessful searches establish no originality.
Other approximation-rate papers were locator hits, not inspected or
needed sources. A Mathlib locator search found a formalization discussion,
not a checked matching theorem: full matching Mathlib coverage remains
unchecked. No absence claim follows.

L433/L434's positive densities retire their precise one-/two-prime
obstruction tests; they do not sign L435's three-factor density. L432's
positive finite prefix does not prohibit a different finite three-prime
test. L431's successful selected calibration remains valid. The parked
core/tail and finite-minor searches are not reopened by relabeling this
localization construction.

### Single bounded continuation

Keep the exact TARGET. Attempt one centrally symmetrized translated
product-Fejer localization at L435's certified negative point, with an
a priori sufficient degree/error bound and an exact complete finite
integral certificate. Do not perform arbitrary degree escalation or an
increasing minor search. Continue only with proved nonnegativity and a
strict negative upper bound; if the selected bound cannot certify the
sign, preserve the failed actual/required comparison and reassess this
implementation. Failure of that bound is not nonexistence of witnesses.

The downstream use is a finite selected-character obstruction to a
positive calibration measure. Actual/global realization, actual clipping,
capped nondegeneracy, L413's full-error regulator margin and global mixed
positivity remain independent gaps. Mathematical exploration usage stays
0 of 3; this literature step spends none of that calculation budget.

## Original step-238 proposal (retained; source request completed above)

The main gap is global mixed positivity. The proposed intermediate
target could turn L435's full-family obstruction into a finite test
against nonnegative mass calibration. It does not reject every modified
law or the original selected constraints of L431.

Essential input is audited L435, especially its complete coefficient
formula, absolute summability, continuity and exact negative point, with
`scripts/discriminant/three_prime_cubic_density_certificate.json`.
L406--L409 and audited L434 supply the inherited physical interface;
L431 is a contrast, not a premise for signing the new test. Fixed
cosine limits permit only a finite combination after a polynomial has
been fixed. No physical sine limit or height-dependent degree is given.

The next invocation is literature-only. Reuse ready source records
where adequate, but inspect primary hypotheses for the proposed
localization and effective certification, and check duplicates and
known obstructions. LITERATURE_REASON for that invocation: the prior
assessment expressly excluded finite nonnegative witnesses and does
not cover the required quantitative approximation step. Record whether
a known result suffices by citation or precisely what specialization
remains. Do not derive a witness while approving its coverage.

The prospective mathematical test is a single localization construction
anchored at L435's certified negative point, with central symmetrization
and a priori control of its complement. Continue only with proved
nonnegativity and an exact negative integral or a rigorous negative
upper bound. An uncertified numerical value, arbitrary degree escalation
or another increasing Toeplitz-minor search does not meet the target.
If the selected bound fails, retain the precise failure and reassess
that implementation rather than claiming all finite witnesses fail.

Actual/global realization, actual clipping, capped nondegeneracy and
L413's full-error regulator margin remain independent unresolved steps.
No new lemma, certificate or general approximation theorem is proved
by this proposal. Full matching Mathlib coverage is unchecked.
