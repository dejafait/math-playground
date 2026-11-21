# One-sided actual-family exclusion — source comparison2037

TARGET: Review primary one-sided zero-location results for the full Jensen-weighted Kuznetsov family, testing whether coefficient-specific hypotheses could exclude nonreal zeros in Re(t)<0 eventually without a global index bound.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded one-sided/Hurwitz discovery and exact Kuznetsov overlap searches; inspected Tyaglov's primary coefficient criterion and its essential R-function proof case. Scoped local comparisons found no previous generalized-Hurwitz test on the full weighted family; no novelty inference.
SOURCE_EVIDENCE: Tyaglov ELA24(2012), Definitions4.1-4.2, Theorem4.3 and (2.1)/(2.5), pp217,224-225; arXiv1005.3032v1 endpoint, Definitions5.1-5.2, Theorems5.3/5.6, pp41-43,49-50; Kuznetsov CMB51(2008), (11)/(13)/(15)-(17), pp564,566-567, weighted discussion pp568-569. Exact access qualifications below; C029m/n source normalization reused.
COMPARISON: Generalized Hurwitz type II supplies a coefficient-explicit sufficient condition for the desired exclusion, while imposing additional real-root simplicity and parity restrictions. It is stronger than bare one-sided exclusion and is not an actual-family theorem. A necessary leading-minor sign on the even-degree subsequence is a distinct uniform coefficient test; no sign has been evaluated here.
GAP: Actual reflected-family Hurwitz-minor signs, actual degrees and eventual uniformity are unpaid. The source's auxiliary oscillatory asymptotic must survive the full beta transformation with a controlled error before deciding even the first necessary sign. Bare one-sided exclusion and the qualified limit/symmetry bridge remain unresolved.
REASON: Nominate one asymptotic coefficient obstruction test rather than another finite root campaign; it can reject this sufficient-condition class for arbitrarily large degrees without claiming to refute one-sided exclusion or RH. A positive result for one necessary minor cannot establish class membership.
LITERATURE_REASON: The target changes from a fixed inverse lower-half-plane count to eventual one-sided nonreal exclusion for the actual weighted family; prior operator and global-index source coverage does not cover this hypothesis.
SCOPE: Completed literature-only comparison2037. No lemma/script writes, coefficient identity, determinant evaluation, asymptotic specialization or new limit implication. The separate assessment2037 proposes one mathematical attempt and requires independent next-turn approval.

## Completed comparison2037

The main gap is still L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target reviewed here is eventual nonreal
zero exclusion in Re(t)<0 for the full T_N, retaining odd coefficients
and exact Jensen weights. Its plausible downstream use is a later
compact-limit/symmetry argument in C029m's setting, not C029m's
already-proved global-index implication itself. That different
one-sided implication has not been proved in this literature turn.

The continuation test was an explicit coefficient-checkable condition;
generic root-location hypotheses and another isolated root campaign
were rejection conditions. One stronger known condition was found.
No actual coefficient hypothesis has yet been paid.

### Primary theorem and proof scope

M. Tyaglov, *Sign patterns of the Schwarz matrices and generalized
Hurwitz polynomials*, Electronic Journal of Linear Algebra24 (2012),
215-236, [published primary PDF](https://emis.de/ft/34015),
(2.1)/(2.5), printed p217, Definitions4.1-4.2 and Theorem4.3,
pp224-225: for a monic real polynomial of actual degree n, the
type-I criterion is positivity of the leading Hurwitz determinants
Delta_(n-1), Delta_(n-3), ... down to the positive index of that parity.
These use descending monomial coefficients, with out-of-range
coefficients zero. In particular Delta_1 is the next-to-leading
coefficient. Type II means reflection is type I. Type I permits
nonreal zeros only in Re(z)<0; its opposite-side real zeros must be
simple, with additional interval parity restrictions. Thus type II
is sufficient, but not necessary, for this notebook's proposed
one-sided exclusion. The theorem does not require all determinants
nonzero; later Schwarz-matrix applications do. Those applications
and the order-count formulas are not needed here. This source
states the criterion with reference to its [17].

For its proof source, inspected M. Tyaglov, *Generalized Hurwitz
polynomials*, [arXiv endpoint1005.3032v1](https://arxiv.org/pdf/1005.3032v1),
Definitions5.1-5.2, printed p41; Theorem5.3 and the sufficiency
case pp42-43; Theorem5.6 and the criterion reduction pp50-51.
The associated rational function is the odd part divided by the even
part, in the squared variable. An R-function maps the upper half-plane
to the lower one. The proof uses its imaginary-part sign to locate
nonreal zeros. The determinant reduction separates even degree,
odd degree with nonzero next coefficient, and the zero-next-coefficient
case via Theorem5.5. Only the even-degree necessary condition is
nominated next; no zero-count formula or singular odd case is applied.
The endpoint carries an arXiv2010v1 stamp but an internal title date
26November2024; that discrepancy is retained, not silently normalized.
The published2012 statement fixes the criterion used. Its relevant
proof passages were read, not a full independent audit of every
upstream rational-function theorem. Screenshot calls returned labels
without inspectable images; no visual-scan verification is claimed.

A. Kuznetsov, CMB51(4) (2008),561-569,
[original publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf),
(11), p564, gives beta_n through three auxiliary a coefficients for
n>=2. Section3, pp566-567, (15)-(17) and the following expansion,
provides an oscillatory saddle representation and asymptotic for the
auxiliary integral, not an eventual adjacent-beta sign theorem.
Inspected the contour rotation, rescaling, local expansion and stated
integrated remainder. A next attempt must control the remainder after
the three-term transformation; taking the sign of an auxiliary leading
term alone is insufficient. Exact beta input remains (4)/(13).
The alternate URL containing `riemann-3` returned inconsistent factorial
and radical transcriptions; the original URL above gives the actual
double factorials and square-root dependence. No changed formula is
adopted from the alternate transcription. Weighted convergence remains
qualified as in C029m, with upstream[9] unaudited. No new convergence
or asymptotic error estimate is asserted.

### Bounded discovery, duplicates and route

Compared two mechanisms only. The ready Pollaczek multiplier and
imaginary-shift results require input-root control and do not pay the
actual one-sided premise; reuse discovery2026/2032 instead of browsing
them again. The selected generalized-Hurwitz mechanism has explicit
coefficient hypotheses but pays for stronger real-root geometry.
The almost-generalized variant was located in published Definition4.11/
Theorem4.13, p228; it is not selected or applied. Searches supplied no
inspected theorem for the full actual weighted family. Unread results
on basis asymptotics, rotated other-parameter Pollaczek systems and
Taylor-Jensen derivatives are not coverage of this target.

Queries included `Tyaglov generalized Hurwitz polynomials theorem
coefficients nonreal zeros left half plane self interlacing`,
`Kuznetsov Pollaczek left half zeros`, `one-sided real zeros polynomial
Hurwitz coefficients`, `Kuznetsov b_n Hurwitz`, `Meixner Pollaczek
generalized Hurwitz`, and `Kuznetsov Pollaczek coefficients asymptotic
zeros Jensen`. Search snippets were discovery only. Exact primary
statements and relevant proof cases were retrieved before wider
passages. Access succeeded; there is no essential retrieval blocker.

Local reads: full C029m and C029n's exact finite formulas/proof,
C029t's hypotheses, conclusion and inversion setup; full degree
review2019 and residue discovery2026, shift discovery2032 and finite
stop records2019/2034. Their established stops are comparisons, not
premises for the new coefficient question. The wider notebook-scoped
duplicate search for generalized Hurwitz/self-interlacing found only
the finite-PF source comparison of November6 and an unread lead in
contact-kernel review889; their matching passages were checked. Neither
tests this full family. No sibling notebook or certificate was loaded.

Select the first necessary coefficient sign along the even-degree
subsequence as the sole next test. This has an infinite-degree
quantifier; it is not a new N=6 signature or root count. The exact
target and all rejection cases are in
`drafts/literature/2026-11-20-tilted-hurwitz-leading-sign-test-2037.md`.
No reflected leading-coefficient formula or sign is derived here.
This is development of a known criterion, not a creative positivity
mechanism. A protected creative attempt remains blocked by the absence
of a viable uniform coefficient mechanism; do not invent one to meet
a scheduling preference. If the sufficient class is obstructed, retain
that evidence and choose a materially different target, rather than
switch parity, shift or isolated degree.

Outcome EXPLORATION: a new bounded source comparison supplies a
concrete uniform test but establishes no actual-family sign or result
beyond the sources. Full matching Mathlib coverage unchecked. No lemma,
mathematical script, PROOF, DAG, shared infrastructure or scheduler state
changed. No mathematical exploration budget spent or reset. Essential
continuation inputs: C029m/n exact family and normalization, the cited
primary criterion and coefficient passages; C029t is stop context only.
Actual degree/nonvanishing, transformed remainder, uniform signs,
initialization and the qualified limit/symmetry interface remain open.
No cross-notebook theorem input. No RH candidate.

## Original nomination2036 (historical scope)

Main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
This is a proposed alternative intermediate target, not a resolved
criterion or a claim that one-sided exclusion is easier. It permits
nonreal zeros in the right half-plane and avoids demanding a global
at-most-one-pair bound. Whether an eventual exclusion can interact
rigorously with the existing compact-limit/symmetry interface is part
of the next source comparison, not derived or approved this turn.

Bound the discovery to at most three distinct primary theorem mechanisms
with explicit hypotheses, then select at most one coefficient-level test.
Retrieve exact statements and relevant proof cases before broad source
extracts. In particular distinguish exclusion of nonreal zeros in an
open half-plane from Hurwitz stability, which also excludes real zeros
there. A theorem requiring all input roots to lie in the desired region
does not pay an actual-coefficient hypothesis. Do not infer a result
from generic Pollaczek basis preservation, moment representations with
uncontrolled sign, or source numerical observations.

Continue only if a primary theorem or a concrete uncovered mechanism
supplies an explicit sufficient condition that can be independently
tested on the full beta coefficients and exact Jensen weights. Otherwise
record the missing condition and abandon this nomination in favor of
a different independently testable target. No isolated degree campaign
or parameter scan is proposed. No theorem is imported by this document.

Local continuation inputs are C029m's exact family/conditional interface,
C029n's coefficients and C029t's audited stop. C029q/r/s and stop2019
are failure comparisons, not mathematical premises. Uniformity, degree
and boundary cases, initialization and the qualified compact convergence
including upstream[9] remain unresolved; no new convergence claim is
made. Mathlib coverage is unchecked. No cross-notebook input is proposed.

A creative central attempt is not yet justified: no coefficient-specific
one-sided mechanism has approved source coverage or an admissible
bounded mathematical test. The next review should prepare such a test
only if the primary comparison supports it; it must not relabel a known
specialization or this failed finite inverse as creative.
