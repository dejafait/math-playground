# Actual-theta quartic additive square root — completed source gate

TARGET: Construct the finite-free additive self-convolution square root of the centered monic actual-theta P_4 and certify its real-rootedness using L791's audited coefficient enclosures.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step623 searched quartic complete real-root classification, finite free quartic divisibility, finite free theta square root and fractional convolution powers; reused step620's inversion/preservation assessment and step495's complete Hermite proof assessment; compared the recorded Favard, inverse, LP/Appell and automatic-Gram stops.
SOURCE_EVIDENCE: https://arxiv.org/pdf/1911.01745v2 pp.1–3 Lemmas1–2/Theorem1 and both proof cases; https://ocw.mit.edu/courses/6-972-algebraic-techniques-and-semidefinite-optimization-spring-2006/260460cc36cd5c2c78b0b04f9b3fe7bd_lecture_05.pdf Sections3.1/6, equation(2), Lemma15/Theorem16 pp.5-2,5-6–5-7; https://arxiv.org/pdf/1611.06598v2 Section6 pp.15–17 including Remark6.7; reused https://arxiv.org/pdf/1504.00350v2 Definition1.1/Theorem1.3 and Arizmendi–Perales Propositions3.4/3.6 pp.7–8 via step620.
COMPARISON: General finite inversion and the multiplicity-safe Hermite–Sylvester criterion suffice for one independent d=4 factor test; no inspected source supplies its actual signs. Known central Jensen hyperbolicity and forward preservation do not certify the inverse factor. Arbitrary fractional powers are not automatically real rooted.
GAP: Construct and prove uniqueness of the actual centered monic d=4 self-convolution factor, then certify its Hermite matrix signs using complete audited intervals; no factor formula or sign has been evaluated here.
REASON: Complete coefficient-based real-rootedness coverage, including every repeated-root case, closes the essential source gap for the unchanged target. Approve one known-method calculation next turn; no quartic derivation, lemma or mathematical script in this literature turn.
SCOPE: Only symmetric additive self-convolution at d=4, real monic factors, actual L019/L021/L795 normalization and L791 coefficients through j=4 under inherited L778 contracts. No new evaluator, degree sweep, arbitrary-power claim, theta Gram identity or shifted/mixed transfer.

This nomination is made after the positive cubic result, not after an
exhausted calculation. The named intermediate target tests the first
degree with root constraints not decided by a cubic discriminant.
It could distinguish an extendible finite realization from a solely
cubic phenomenon. It is a bounded d=4 test, not an automatic degree sweep
or a claimed central creative mechanism. No quartic calculation or
identity was derived in step622. Newly supplied scope approval must be
a separate next turn and does not invalidate the completed cubic result.

Review the exact statement, standard terminology, stronger results and
known obstructions. Reuse general finite inversion/preservation coverage;
retrieve complete primary hypotheses and proof cases for a sufficient
and necessary quartic root test, including zero discriminant, repeated
roots and possible nonreal pairs. Check the degree-four example in
Arizmendi–Perales Remark6.7 and distinguish arbitrary polynomial powers
from this one actual law. Do not import infinite divisibility or root
preservation before the actual factor hypotheses hold. Compare the
existing LP/Appell, common-Favard, multiplicative and inverse stops
already located by the cubic assessment; do not rederive their failures.

Potential actual inputs are L019/L021/L795 and L791's full coefficients
through j=4, under the same inherited L778 analytic/software contracts.
L823 is context, not a premise of any degree-four assertion. No new
quadrature, parameter search or evaluator is proposed. Any arithmetic
requires complete relevant intervals and audit/hash checks; invalid
input blocks evaluation. No cross-notebook input. Full matching Mathlib
coverage remains unchecked.

A future calculation may continue only if the complete applicable test
passes; a certified failure of a necessary condition parks the quartic
factor mechanism after algebraic uniqueness is proved. Straddling
intervals or uncovered multiplicity cases are inconclusive. Even a
passing test leaves degree-uniform realization and all shifted/mixed
sufficient-sign transfer unpaid. A justified creative central target
still needs an independently sufficient uniform coefficient mechanism;
this routine finite specialization does not provide one.

LITERATURE_REASON: Degree four is outside the saved cubic assessment; the complete quartic real-root criterion and relevant finite-divisibility obstruction are essential unread/unassessed coverage.

## Completed comparison — 5 November 2026, step623

The pending language above is the preserved nomination, superseded by this
completed review. The TARGET is unchanged and this assessment itself now
approves that exact calculation; no differently worded continuation is
being introduced. The main gap remains actual-Xi all-degree mixed
positivity. The finite factor test could discriminate an extendible
realization from the cubic-only evidence. Uniform realization and
shifted/mixed sufficient-sign transfer remain independent gaps.

### Complete root criterion without a simple-root assumption

Reuse step495's assessment in
[central Hermite/theta Gram](2026-11-05-central-hermite-theta-gram.md).
Nathanson, *The Hermite-Sylvester criterion for real-rooted polynomials*,
[arXiv:1911.01745v2](https://arxiv.org/pdf/1911.01745v2),
24 November 2019, pp.1–3, Lemmas1–2/Theorem1, was also inspected directly.
For any real polynomial of degree n>=1, its root power sums, with
multiplicity and s_0=n, form H=(s_(i+j)) for 0<=i,j<n. All roots are
real iff H is positive semidefinite. Newton identities obtain its entries
from coefficients. The proof explicitly treats distinct roots with their
multiplicities; interpolation detects any nonreal conjugate pair, even
when repeated. Thus neither a nonzero discriminant nor simplicity is a
hypothesis. No reproof is needed. Apply to the constructed real monic
degree-four factor, not to an assumed real root measure.

For a finite coefficient check use Parrilo, MIT6.972, Lecture5,
23 February 2006 (scribe Noah Stein),
[Section6, Lemma15 and Theorem16, pp.5-6–5-7](https://ocw.mit.edu/courses/6-972-algebraic-techniques-and-semidefinite-optimization-spring-2006/260460cc36cd5c2c78b0b04f9b3fe7bd_lecture_05.pdf).
A real symmetric matrix is PSD iff every principal minor is nonnegative;
strictly positive leading principal minors suffice for positive
definiteness. Nonstrict leading minors alone do not suffice. Theorem16
and its proof via Lemma17 give an alternative characteristic-coefficient
test. Section3.1 equation(2), p.5-2, also computes root power sums as
traces of companion-matrix powers, including multiplicities. These are
coefficient algorithms, not assumptions on the factor's roots.
For d=4 the required matrix is finite and its complete principal-minor
test includes singular cases. This specializes a standard criterion;
no quartic identity or inequality is derived in this review.

### Divisibility and existing overlap

Reuse step620's
[inversion/preservation comparison](2026-11-05-theta-cubic-free-square-root-scope.md):
MSS Definition1.1/(1)–(2), Theorem1.3, and Arizmendi–Perales
Propositions3.4/3.6 apply to fixed monic degree d, including d=4.
The former preserves roots only after both input factors are real rooted;
the latter supplies finite coefficient/cumulant reconstruction and
additivity without a root-location premise. The calculation must verify
its own exact identity and uniqueness. Do not extend L823's cubic
formula by analogy.

Arizmendi–Perales, *Cumulants for finite free convolution*,
[arXiv:1611.06598v2](https://arxiv.org/pdf/1611.06598v2),
Section6, pp.15–17, was inspected including the relevant proof cases.
Remark6.7 uses degree-four z^4-z^3 and exponent4/3, and displays a
nonreal pair for the fractional power. This is a source warning against
automatic power preservation, not a counterexample to the actual
theta half-power. Its printed approximate roots were not independently
certified here. Theorem6.5 concerns all positive powers under centered,
variance-one normalization; it does not exclude a single square root.
Proposition6.6 is eventual in large powers, and its proof normalizes a
positive second cumulant. It does not establish the t=1/2 case.
Retain step620's caution about the printed power definition: implement
Proposition3.6's additivity and the coefficient equations directly.

L795's full-support interlacing stop, the common-Favard stop in
`ATTEMPTS/2026-11-05-actual-theta-common-favard-stop.md`, and the
audited L822 stop in
`ATTEMPTS/2026-11-05-theta-universal-inverse-variation-stop.md`
were compared. None tests this additive factor. Step495's
`ATTEMPTS/2026-11-05-hermite-automatic-gram-source-limit.md`
excludes importing a positive theta Gram identity from Hermite alone;
the present proposal instead calculates the factor matrix's signs.
Reuse step385's LP/Appell comparison and step597's multiplicative
comparison; no common measure, LP premise or multiplicative factor
is supplied by additive inversion. Known low-degree central Jensen
hyperbolicity, noted in step495, concerns the original polynomial,
not its convolution square root. No duplicate exact actual-quartic
factor certificate was found in the narrowly checked local material;
this is no claim of novelty or global search completeness.

### Inputs and the bounded calculation decision

Read the definition and normalization in L795, L791's actual-coefficient
construction and audit qualifications, and L823's conclusion/operation
only for cubic context. Essential inputs are L019/L021/L795 and L791
through j=4. The actual leading coefficient is nonzero by L021's
positive moments. Monic normalization and centering must be justified
without presuming any roots real. L823 and L791's fitted model are not
mathematical premises of the d=4 factor assertion.

The later calculation must inspect complete `actual_a` and `gamma`
intervals in `scripts/central-jacobi/fixed-model-certificate-476.json`,
and the relevant hash/replay evidence in
`scripts/central-jacobi/audit-478/audit-report.json`. L791 includes the
Cauchy coefficient error from L778's uniform complex-disk approximation.
Keep that analytic error and every software qualification. This source
review has not inspected the JSON intervals or replayed their checks;
the documented audited coefficient contract is reused conditionally.
Use the JSON inspector on selected complete load-bearing values, not
previews or printed midpoints. Invalid inherited evidence blocks use;
no evaluator replacement or new quadrature is approved.

Construct the unique real monic factor and prove its exact convolution
identity before deciding hyperbolicity. Compute its coefficient-based
Hermite matrix with outward rational enclosures. Certified strictly
positive leading minors suffice to continue this finite realization;
alternatively certify every principal minor nonnegative, allowing exact
zeros and retaining root multiplicities. Any certified negative
principal minor or exact negative quadratic-form witness excludes
real-rootedness and parks this d=4 factor mechanism after uniqueness.
Zero determinant alone decides nothing. An interval crossing zero,
unproved equality or invalid input is INCONCLUSIVE, not a negative
result. No degree sweep or precision campaign is authorized. A script,
if used next turn, must save its complete certificate, all checked
minors/witnesses, bounds, failures and source hashes to disk.

The calculation is REPRODUCTION by known finite methods. This review
does not produce a factor formula, sign, new lemma, mathematical script
or change in the proof assembly. Full matching Mathlib coverage remains
unchecked. No cross-notebook input is used. A central creative attempt
still lacks an independently sufficient uniform coefficient mechanism;
this finite specialization is not classified as creative.

### Search and access record

New queries were `quartic polynomial real roots complete discrimination
system Yang Xia depressed quartic discriminant repeated roots`;
`Arizmendi Perales finite free cumulants Remark 6.7 fourth convolution
power`; `Quantifier Elimination for Quartics pdf Yang Xia`;
`Hermite matrix positive semidefinite polynomial all roots real repeated
roots theorem pdf author`; `finite free quartic divisibility`;
`finite free theta square root`; and `finite free convolution powers
real-rooted fractional t`. The exact finite-free quartic/theta queries
located no inspected theorem settling this actual factor. General
inversion and fractional-power literature was reused instead of searched
again for novelty.

Prodanov's 2021 quartic article introduction/(2)–(3) was inspected only
as a lead to Arnon's discriminant classification; its image table and
underlying proof were not adopted. Yang–Xia's author-hosted quartic PDF
timed out twice and its CiteSeer mirror failed; Anghel's PDF returned403.
Those are inaccessible alternative classifiers, not essential blockers:
Nathanson's full proof provides all multiplicity/nonreal cases needed
here. UCSD's PSD-note preview was insufficient and follow-up reads timed
out; the complete applicable MIT Section6 replaced it. Search results
for newer finite Hermite–Poulain semigroups and Campbell's published
Appell paper are unread leads, not additional adopted inputs. Reused
versioned Campbell coverage in step385/620 remains the relevant scope.

All changes are confined to this assessment, the current checkpoint and
a concise history entry. Prior unfinished work is preserved. Literature
does not spend or reset the mathematical exploration budget.
