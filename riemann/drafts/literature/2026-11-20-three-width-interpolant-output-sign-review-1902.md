# Fixed three-width interpolant: output-sign source review1903

TARGET: Assess source coverage for testing nonnegativity of C034k's exact mass-one interpolant at widths 1,3/2,2, prioritizing a negative bounded Laplace or finite-difference witness and allowing signed common-base quotients.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed1903: exact signed-mixture/complete-monotonicity, signed-measure finite-difference and Hausdorff-moment searches; scoped C034k/j, C032q/u/m, C033j/l interfaces, notes1552/1562/1797/1875/1894/1898, audit1879 and stop1798. Queries and primary cases are recorded below. No matching theorem decides this exact output; no novelty inference.
SOURCE_EVIDENCE: Diaconis--Freedman, The Markov Moment Problem and de Finetti's Theorem: Part I, author version15June2003, equation(1) pp1-2, Theorem1 and Lemma1(a)/proof p2, https://www.stat.berkeley.edu/~census/631.pdf ; Mimica2015 Proposition1.4(i),(iv), pp6-7 and Proposition1.8 pp9-10, https://web.math.pmf.unizg.hr/~amimica/lt.pdf , directly inspected with notes1552/1562 reused. Bertoin finite-activity coverage and signed-mixture comparison1894 are reused, not rederived.
COMPARISON: C034k already establishes the unique two-observation interpolant and its cap below3/2; rebuilding or reevaluating that system is duplicate work. C033j supplies signed factors and C034p excludes positive quotients for arbitrarily accurate residual approximation. Neither decides whether this fixed interpolant has a positive output on every Borel set. Two exact observations do not establish a small uniform error.
GAP: The sources cover a density-free bounded third Hausdorff-difference diagnostic, not its sign for C034k. The exact combined observation at s=3 remains unpaid; the j=1,2 bounds cannot be extended silently. A negative certificate rejects this output; a nonnegative value or unresolved enclosure leaves output positivity open.
REASON: This completes the required separate source comparison without evaluating any coefficient, transform or test. Nominate one analytic third-difference attempt under the new assessment1903; its separate approval is still required. No general positive repair or central creative mechanism is supplied.
SCOPE: Only C034k's exact fixed interpolant, the same C033i/C033l residual, C032q's signed output convention and C033j's existing signed factors. No new coefficients, enlarged width span, full-cone separation, uniform approximation, cancellation or Xi realization is authorized.

## Precise object and downstream use (nomination scope retained)

Use C034k's existing a=(a_0,a_1,a_2), defined by its exact mass and
two-observation system at widths (1,3/2,2). The object whose sign is
unresolved is the finite signed Borel measure

    Q=a_0*nu_1+a_1*nu_(3/2)+a_2*nu_2 on [0,infinity).

Its mass and matches at s=1,2 are existing results, not new claims of
this nomination. Positive output would supply one concrete building
block for sign-constrained approximation; a negative witness would
show why even the existing small-variation exact fit needs a different
repair. Neither result alone supplies uniform accuracy, moments, full
odd cancellation, signed height or actual-Xi all-degree positivity.
Retain every C034k external and normalization qualification. The
historical missing count in stop1876 was later paid in C034k/audit1879;
do not revive that source blocker or treat its old stop as global.

## Compared mechanisms and bounded decision

1. Positive mass-one quotient repair after nu_1: stopped by C034p,
   first audited1902. Repeating the same observation adds nothing.
2. Automatic positivity from full signed factors or affine closure:
   parked in notes1898 and stop1894. Neither supplies a sign/error
   repair preserving the original width span.
3. Selected: test the output of the already fixed three-width fit,
   allowing its common-base factor to be signed. This asks for an
   output constraint absent from the earlier interpolation/cap work;
   it does not retry its numerical evaluator or source access.

The source turn should search the exact signed-mixture positivity
statement and its standard terminology, compare applicable primary
theorem hypotheses and essential proof cases, and nominate at most
one concrete sign test. A bounded Laplace witness means a finite s>0
with integral exp(-s*u)dQ(u)<0. A finite-difference witness must be
stated as an explicit bounded nonnegative test with a rigorously
negative integral, with its signs justified before use. Such witnesses
are possible test forms, not asserted to exist. No mathematical
evaluation or sign deduction is made here.

Continue only if that review identifies adequate source coverage and
a fully specified test using available canonical bounds. Otherwise
park this fixed interpolant's sign route with the precise missing
input. Do not turn a passed finite screen into all-Borel positivity.
Full matching Mathlib coverage remains unchecked/unknown.

## Completed review1903 — 20 November2026

The preceding proposed review is now completed. The main gap remains
actual-Xi all-degree positivity in L030-L032/C032a. Only this fixed
output's necessary sign condition is assessed; no sign is evaluated.

### Primary statement, essential case and applicability

Persi Diaconis and David Freedman, *The Markov Moment Problem and
de Finetti's Theorem: Part I*, author version dated15June2003,
[equation(1), pp1-2, Theorem1 and Lemma1(a), p2](https://www.stat.berkeley.edu/~census/631.pdf).
Read these statements and the complete Lemma1(a) proof. With forward
difference Delta t_j=t_(j+1)-t_j, their auxiliary quantity is
(-1)^(n-j)*binom(n,j)*Delta^(n-j)t_j. For a probability on [0,1]
it equals binom(n,j) times the integral of x^j(1-x)^(n-j), hence is
nonnegative. The proof is induction; endpoints and atoms are allowed.
Theorem1 states the all-orders Hausdorff criterion and uniqueness;
its sufficiency proof is referenced there and is NOT imported here.
The density bound in their separate Markov Theorem2 is NOT required.

The proposed specialization is their n=3,j=0 case under x=exp(-u).
It would test the bounded nonnegative function (1-exp(-u))^3 using
observations at 0,1,2,3. No moment of u or density is required. The
test vanishes at u=0, so it cannot detect a negative zero atom by
itself. C032q already supplies finite signed integration, and C034k
fixes the mass and observations1,2. Only a prospective diagnostic is
specified here; its family-specific integral and sign are not proved.

Mimica's Proposition1.4(i) proof was revisited: positive-parameter
derivatives use exponential domination, not moments at zero. Its
convolution and uniqueness statements/proof cases were revisited with
notes1552's endpoint/typographical qualifications retained. Reuse
notes1562/1894 for Bernstein--Hausdorff--Widder: all derivative signs,
not a finite screen, are needed. No reproof or sufficiency application
is proposed. C033j's signed factors impose no extra positive-quotient
constraint. The sampler in Robert--Stoehr, arXiv2401.16828v1,
[Sections1-3](https://arxiv.org/html/2401.16828v1), remains covered by
comparison1894: positivity/density/domination are hypotheses, not a
constructor for this output. Its source was reopened only to confirm
the fixed version; the ready theorem-level comparison is reused.

### Searches, duplicates and access qualifications

Queries: signed mixture Laplace completely monotone; signed measures
Laplace transform finite differences positivity; mixture convolution
negative coefficients positivity Laplace; Hausdorff moment completely
monotone sequence finite differences theorem; signed mixture infinitely
divisible distributions nonnegative measure; Sra three width positivity
Xi interpolant; Hausdorff finite differences Berg Duran; three Laplace
interpolation complete monotonicity signed; Hausdorff signed mixture
positivity. Inspected primary evidence is identified above. Search
snippets, unrelated distribution classes and index pages are not imports.
No adequate exact-output sign theorem was found in this bounded search.

The optional Berg author PDF bdur5a.pdf timed out via HTTPS and HTTP.
It was not read or used; the directly inspected Diaconis--Freedman
lemma supplies the needed finite-difference case, so this is no essential
source blocker. No optional density/certification source parked1894 was
retried. No archive-wide originality or absence claim is made.

C034k/audit1879 already pays its finite count and variation cap. Its
cofactor formula and determinant allowance are available for an analytic
combined test. C032j/q and C033l define the transform at every s>0;
C032m supplies analytic regularity/common bounds. These do not supply
the required combined sign at3. C034b/i/k's displayed quantitative
observation estimates are for1,2 only. Stop1798 concerns the literal
compact scalar evaluator; do not rerun it or assume affordable scalar
enclosures. An analytic sign bound would be the unpaid specialization.

### Decision and bounded continuation

Nominate exactly one third-difference test in assessment1903. Seek a
strictly negative rigorous bound without scalar quadrature, new zero
data, changed coefficients or more tests. A certificate would reject
only this fixed output and redirect sign repair. If its sign cannot
be certified in one analytic attempt, record the missing comparison
and park this diagnostic; passing it is inconclusive. No computation
or new lemma is undertaken in this review. A creative central route
still lacks a span-preserving sign/error mechanism and a decisive test;
do not relabel this classical necessary-condition specialization creative.
All external qualifications stated above remain unresolved, as do
uniform accuracy, moments, cancellation, signed height, realization and
full matching Mathlib coverage.
