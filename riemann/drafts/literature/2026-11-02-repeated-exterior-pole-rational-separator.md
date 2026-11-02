# Repeated exterior-pole rational action — source comparison

TARGET: Test whether real rational actions P_n(w)=N_n(w)/(1-r_n*w)^n, with deg N_n<=n and 0<r_n<4*(n-1)/(5*n), can satisfy the same normalization, prescribed zero, closed-segment signs and rate-1/100 angular inverse budget.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 55 searched repeated prescribed-pole rational functions, arc positivity, weighted Hardy/Hadamard inverse ranges and rational coefficient expansions; inspected the primary statements and proof cases recorded below. No matching product-specific rate-1/100 result was identified in this bounded comparison; novelty is not established.
SOURCE_EVIDENCE: Flajolet--Sedgewick, INRIA RR-4103 (January 2001), Section 1.1, Theorem 8.1 and full proof, printed pp.6--7 (PDF pp.13--14); Kalmykov--Nagy--Totik, author manuscript dated 10 October 2016, Theorem 2.4 printed pp.4--5 and Proposition 3.1 with complete proof/(3.1), printed p.8. Reuse the inspected Levitt Fourier/Parseval, Douglas Theorem 1 and Yang--Xie Theorems 2--3 within the qualifications below.
COMPARISON: Rational coefficient expansion and pole-sensitive norm/derivative bounds are known. None of the inspected results identifies this full-product inverse with its rate-1/100 cost or resolves its zero coefficients. Arc positivity can be compared with the existing polynomial certificate only after a justified rational reduction. L677's polynomial exclusion is retained without extending its cutoff estimate to an infinite tail.
GAP: Construct a full exact L2 action with all normalization/segment signs and uniform paid inverse, or prove a class-wide excess cost. Possible zero beta_k, every free mode, infinite-tail convergence and n-dependent constants remain unresolved mathematical tasks, rather than essential unread theorem inputs.
REASON: This separate literature-only step completes the saved rational target's missing comparison. EXPLORE covers one later bounded family-specific analytic construction or obstruction attempt; no new mathematical result, range criterion, coefficient nonvanishing or cost estimate is asserted here.
SCOPE: Exactly TARGET with the complete L666 product, normalized angular L2, q>=1, n=12q+3, x=-5/4, R=11/8 and tau=(n-1)/n; all constraints and uniform quantifiers are given below. Permitted techniques are full rational/Fourier coefficient analysis, explicit closed-segment sign certification and a justified prescribed-pole mass comparison. No general cone, favorable spectrum, restricted minimum-norm identification or Xi realization is assumed.
LITERATURE_REASON: The genuine exterior pole introduces an infinite Taylor tail outside the prior finite-polynomial assessment. Primary coefficient and pole-sensitive norm comparison was essential before dependent research; this is not a repeat approval of the unchanged polynomial target.

## Initial nomination retained from step 54

The following nomination records the pre-review scope and tests. Its
REVIEW_REQUIRED wording describes step 54; the completed comparison
below now supplies the separate source approval for the same TARGET.

## Proposed bounded target and inputs

Allow a real polynomial N_n of degree at most n and a real parameter
0<r_n<4*tau/5, chosen with n. Set

    P_n(w)=N_n(w)/(1-r_n*w)^n.

Retain exactly P_n(0)=0, P_n(1)=1 and P_n(10/11)=0. Require
Re P_n(x/(x+i*y))>=0 for all real |y|<=9/20. The exact action is

    mean_u conjugate(psi_n(u))*W_a(u)=P_n(x/a), |a|>tau,
    ||psi_n||_2<=exp(n/100)*n^C,

for one absolute real C and every sufficiently large allowed n. Both
the equality and the norm refer to the complete original product and
normalized measure. The candidate pole is outside the required action
disk by the stated parameter restriction. No denominator cancellation,
nonvanishing coefficient or minimum-norm formula is assumed. A candidate
that cancels to a degree-at-most-n polynomial remains subject to L677.

L666 supplies the exact product. The audited portions of L675 Sections
2--3 supply its factorization and general analytic moment identity.
L677 supplies the now audited polynomial exclusion and its exact scope.
Its coefficient cutoff does not furnish an estimate for this new tail.
L676's restricted inverse result is not an unrestricted premise.

The source review should compare exact rational-action range and
weighted Hardy inverse costs, closed-arc positivity after multiplication
by the denominator, and known rational analogues of polynomial mass
bounds. Read primary hypotheses and essential proof cases; record any
exact overlap or obstruction instead of rederiving it. A general
factorization criterion without its product-specific cost is not a
solution. Existing Fourier coverage can be reused where applicable.
This nomination does not assert that any needed coefficient is nonzero,
that an exact inverse exists, or that a new source will decide the cost.

The downstream use would be a segment-positive angular separator
outside the excluded polynomial class. The cone threshold, original
unit-residue H, support and Xi realization remain independent gaps.
The bounded eventual mathematical test is one exact construction with
the full continuum signs and uniform paid inverse, or an unavoidable
cost above exp(n/100) times every fixed polynomial factor for this
rational ansatz. Finite feasibility or a finite Taylor truncation does
not meet either threshold. No such test was performed in step 54.

Known stops retain their evidence: L677's degree-constrained Poisson
balance, L674's stronger open-domain positivity stop, and the finite
polar screen's missing continuum/asymptotic bounds. They neither
authorize replaying those routes nor establish a global ban. The new
target remains REVIEW_REQUIRED until a separate source comparison;
full matching Mathlib coverage has not been checked.

## Completed comparison — 2 November 2026, step 55

### Primary coefficient coverage

P. Flajolet and R. Sedgewick, *Analytic Combinatorics: Functional
Equations, Rational and Algebraic Functions*, INRIA RR-4103,
January 2001, HAL inria-00072528 (submitted 24 May 2006),
[author-hosted report](https://sedgewick.io/wp-content/themes/sedgewick/papers/2001Functional.pdf),
Section 1.1, Theorem 8.1 and complete proof, printed pp.6--7
(PDF pp.13--14). Read the normal-form hypotheses and all four
equivalences. A rational power series has an eventual constant-coefficient
recurrence and an eventual finite sum of polynomial-exponential
coefficient terms. The relevant proof uses partial fractions and
binomial coefficient extraction, including repeated poles; the converse
uses the binomial-polynomial basis. This is a theorem about each fixed
rational function. It gives neither an n-uniform onset nor quantitative
lower bounds for this family's coefficients, and does not rule out
individual zero coefficients. A later specialization must retain actual
pole cancellations and every exceptional initial coefficient. No such
specialization or weighted summability result is derived here.

Some mathematical glyphs in this report's text extraction are damaged;
no numerical residue formula is imported from that extraction. The
author's [AC04 lecture](https://sedgewick.io/wp-content/uploads/2022/04/AC04-Poles.pdf),
slides 24--29 and 59--62, was also inspected as supporting material for
the distinct-, repeated- and dominant-pole cases, not as a quantitative
family theorem. Screenshot retrieval was unreliable. The book's
Theorem IV.9, *Analytic Combinatorics* (Cambridge, 2009), printed p.256,
was identified in search but its full PDF could not be opened
(INRIA: size limit; Princeton: 403). It is an unread alternate citation,
not an essential source blocker: the inspected report supplies the
qualitative rational-series statement needed for this comparison.
No claim of a book-proof reading is made.

### Primary pole-sensitive norm comparison

S. Kalmykov, B. Nagy and V. Totik, *Bernstein- and Markov-type
inequalities for rational functions*,
[author manuscript](https://www.math.u-szeged.hu/pot/Rational.pdf),
dated 10 October 2016. Read the pole/total-degree conventions on
printed p.3, Theorem 2.4 on pp.4--5, and Proposition 3.1 with its
complete proof on p.8. For a C2 Jordan curve and a fixed closed pole
set disjoint from it, Proposition 3.1 bounds the derivative supremum
by C times total degree times the function supremum. Equation (3.1)
retains every pole, with multiplicity, in a Green-function sum; its
maximum-principle proof's interior argument and stated exterior
counterpart were read, followed by the local Green bound and Cauchy
estimate. Theorem 2.4's
arc statement retains the two normal-derivative sums and excludes
endpoints from its uniform subarcs. Its longer proof was not read or
used. These estimates do not give positivity, a paid inverse, or the
required exponential cost. Any future use must verify transformed pole
locations, fixed separation, multiplicities, infinity and endpoints;
polynomial degree alone is not a substitute. No rational mass bound
for this ansatz is asserted.

### Reused range/sign coverage and its exact limits

Reuse the primary readings and theorem references in
`drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`,
Sections "Primary arc theorem and proof cases inspected" and "Reused
exact-range and norm coverage". Those passages were read this turn.
The earlier source comparison in
`drafts/literature/2026-11-02-polynomial-arc-cost-audit.md` was also
checked; no unchanged external Fourier proof was fetched again.

- Levitt, *Analyse de Fourier et applications*, Theorem 1.3/Exercise
  1.2 and Theorem 1.11/Corollary 1.12, printed pp.6,8, with completeness
  p.53, supplies scalar Fourier orthogonality and Parseval. Use normalized
  circle measure, establish L2 membership, and justify every infinite
  expansion/interchange. It does not bound reciprocal beta_k or identify
  the least-cost preimage in the presence of the weight F.
- Douglas, *On majorization, factorization, and range inclusion of
  operators on Hilbert space*, Proc. AMS 17 (1966), Theorem 1,
  pp.413--415, DOI 10.1090/S0002-9939-1966-0203464-1, characterizes
  range inclusion by operator majorization/factorization. It does not
  establish that majorization or its constant for W_a. A formal
  factorization is not an evaluated angular inverse budget.
- Yang--Xie, arXiv:1605.02431v3 (21 July 2017), Theorems 2--3,
  Sections 3--4, PDF pp.6--11, gives an exact nonnegative-trigonometric-
  polynomial certificate on a closed proper arc, including endpoints.
  Rational data are not automatically that polynomial. A later attempt
  must specify the circle coordinate, justify denominator clearing by
  a strictly positive multiplier on the whole arc, and retain the
  resulting exact degree and coefficient constraints. The general
  certificate is imported if used; deriving this data-specific
  reduction is the permitted specialization. It supplies no inverse
  norm estimate. Sampling cannot replace its coefficient identity.

The inspected Bal--Martin--Naderi transform and Herglotz theorem retain
their earlier measures, induced norms and open-domain hypotheses.
There is no identification with this action. Neither is needed merely
to study signs on the closed segment. General Hardy multiplier and
orthogonal-rational-function search hits are unused leads, rather than
unread premises for the elementary rational/Fourier attempt.

### Local overlap and recorded failures

Read L666's full-product hypotheses, L675's hypotheses/conclusions and
Sections 1--3, and L677's hypotheses and coefficient-input passage;
searched L677's proof for its mass/balance/cutoff uses. L675's analytic
moment identity is already stated for the full action, rather than
only its polynomial truncation. Its sufficient inverse (2) and finite
criterion (1) are stated for polynomials and are not imported as an
infinite-tail theorem. Sections 2--3 used by L677 have the step-54
audit recorded in L677; no additional mathematical audit occurred here.
Read the step-54 history to preserve that precise qualification.

L677 uses a coefficient cutoff and a degree-dependent positive-arc
mass estimate. This review does not extend either to the rational
family. Complete denominator cancellation to a polynomial remains in
its audited excluded class. Read L674's hypotheses/conclusion: its
stronger open-domain positivity requirement is absent here, so its
disk stop is a comparison, not a class obstruction. L676 remains
unused; no restricted inverse is substituted for all preimages.

Read `ATTEMPTS/2026-11-02-positive-cone-polar-finite-screen-inconclusive.md`.
Its finite floating repairs leave continuum signs and asymptotic costs
unproved. This target must use an exact rational action and full tail;
repeating that finite screen would not be a new mechanism. The prior
low-degree/cubic conclusions of L675 are not reaudited or used to
infer a rational cost bound. No local duplicate settling the exact
saved rational target was identified in these scoped paths.

### Search record and readiness decision

Queries on 2 November 2026 included:

- `rational functions positive real part circular arc prescribed poles
  sum squares rational trigonometric polynomial`
- `Hardy space Hadamard multiplier range inverse weighted Taylor
  coefficients rational functions repeated pole`
- `rational functions prescribed poles Bernstein Walsh lower bound
  arc positive real part`
- `Flajolet Sedgewick Theorem IV.9 expansion rational functions
  coefficients polynomials exponential pdf`
- `rational Hadamard multiplier weighted Hilbert space coefficients
  range inverse Blaschke product`
- `"rational" "positive real part" "arc" "minimum norm"`
- `"Blaschke" "Taylor coefficients" "zero" "positive zeros" inverse rational`

Followed the rational inequality and coefficient-expansion leads to
the primary sources above; other search hits, including Hadamard
multiplier papers with different spaces/sign hypotheses, prescribed-zero
derivative papers and rational arc approximation, were not used as
theorem inputs. Searches found no inspected theorem furnishing the
specific joint sign/range/rate conclusion. This is bounded negative
search evidence, not certified novelty or a new obstruction.

DECISION EXPLORE approves exactly the unchanged TARGET for one later
bounded mathematical attempt. Essential standard coverage is adequate
for elementary rational algebra and normalized Fourier analysis;
product-specific range, zero modes, convergence and uniform cost are
the work to attempt, not assumed known results. Known general theorems
must be cited if used; only the family specialization needs proof.
No new lemma, mathematical script, range criterion, coefficient
nonvanishing result, separator or class-wide cost bound was produced
in this literature-only step. Full matching Mathlib coverage remains
not checked; no absence claim is made.

The discriminating test remains one full exact construction with
P_n(0)=0, P_n(1)=1, P_n(10/11)=0, every closed-segment sign and
||psi_n||_2<=exp(n/100)*n^C for one absolute C and all sufficiently
large allowed n, or an unavoidable cost above that rate for every
eligible pair and every fixed C. In either direction retain all free
modes and possible zero beta_k. A construction alone would advance a
separator input; cone/H/support/Xi transfer would still be open. An
informative obstruction parks only this rational ansatz. A partial
calculation must be recorded honestly with its unresolved claims;
finite fits, n-fixed tail asymptotics and an unevaluated inverse formula
do not decide the test. No independent new target was nominated.
