# Direct actual-theta coefficient certificate — completed source review2066

TARGET: Review effective tail and integration coverage for certifying Romik's c0,c2,c4,c6 directly from (1.7)/(3.3), without using the centered Taylor series.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused October30 actual-moment normalization, L530 and comparison2065; narrow local direct-coefficient/quadrature searches distinguished L768/L821's different observables. External exact coefficient/certification queries and primary integration references are recorded below; no inspected matching four-coefficient certificate or novelty claim.
SOURCE_EVIDENCE: Romik1902.06330v3 Section2.2 Lemma2.3/(2.5)-(2.7), (1.7)/(3.1)-(3.5), Section3.3/(3.13)-(3.14); Johansson1802.07942v1 Sections2/2.1; Arb2.23 acb_calc evaluator/integration contract; NIST DLMF3.5(ii)/(3.5.6)-(3.5.8), 8.2.2/8.4.8/8.4.11; Python Decimal exp, neighbors, contexts, rounding and signals. Exact links/applicability below.
COMPARISON: Source identities and certified compact quadrature are available; Romik's decay estimates have unspecified constants and do not certify the improper tails. A finite direct specialization is justified, with every tail constant and derivative enclosure still to prove. No coefficient table or generic preserver supplies the answer.
GAP: Prove explicit theta-index and spatial-tail bounds, bound the truncated integrand's fourth derivative throughout the compact interval, and certify arithmetic/constants for all four coefficients. No coefficient enclosure or actual-family discriminant/root count is established.
REASON: Essential coverage identifies a concrete finite certification method and its exact outstanding estimates; no inaccessible source blocks that specialization. This is source-scope exploration, not new mathematics beyond the checked sources or a completed certificate.
SCOPE: Completed literature-only review. A separate saved SPECIALIZE continuation specifies the finite calculation and requires next-turn source approval; no mathematics was executed in this turn.
LITERATURE_REASON: The changed direct-integral remainder mechanism required essential unread tail and certified-quadrature coverage. This review supplies it; repeated centered-theta browsing is unnecessary.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target/use: determine whether a certified finite actual-input
screen is available before proposing a theta-specific all-degree invariant.

Read narrow existing direct coefficient-certification assessments first.
Compare exact primary formulas, effective remainder hypotheses and
certified integration methods; do not treat a generic implementation
homepage, decimal table or unspecified O-constant as sufficient. L530
supplies the finite polynomial template only. The October30 assessment
fixes c_(2j)/c0; tilted beta_k and Q6 certificates cannot replace these.
No cross-notebook input is proposed. Mathlib matching is unchecked.

Continue to a separate mathematical step only if coverage supports
finite enclosures for each of c0,c2,c4,c6 with rigorously bounded
series, spatial and integration errors, and a concrete finite
root/discriminant test can use them. The research step may derive the
specialized effective estimates; this review must identify exactly
which estimates are missing rather than assume them. No automatic
source import supplies their values. If an essential source remains
blocked, park this dependent test and choose a ready independent target.
Do not expand to a high-degree sweep or a new arbitrary-measure search.

The intended later polynomial remains precisely the nomination2064
actual degree-six p_r, with 0<r<=1 and the full actual c0,c2,c4,c6.
Any later test must distinguish existence of six initial real roots
from preservation and must handle collisions and multiplicities.
All-degree estimates, a useful invariant, root stability and Xi transfer
remain unresolved regardless of a finite sign. This is coefficient
certification, not creative all-degree development.

## Completed comparison — step2066

The preceding nomination scope is preserved. The October30 assessment
already fixes the actual coefficient normalization; it is reused.
L530 was read in full, including its cubic test and qualifications.
Its endpoint atoms are not actual data; stop2065 remains preserved.
Narrow local checks located L768's cumulant and L821's logarithmic-theta
certificates. Their defining observables/domains and saved arithmetic
assessments do not supply the present coefficient enclosures. Their
certificates were not audited or used as mathematical inputs.

### Primary scope and imports

- Dan Romik, *Orthogonal polynomial expansions for the Riemann xi
  function*, arXiv:1902.06330v3 (5 May2019),
  [primary text](https://arxiv.org/html/1902.06330v3), (1.7),
  Lemma2.3/(2.5)-(2.7), (3.1)-(3.5), and Section3.3's opening
  error case (3.13)-(3.14) were inspected. Lemma2.3 has asymptotic
  O-bounds without numerical constants/onsets; the explanation is
  first-summand dominance. Theorem3.1 concerns compact convergence
  of the polynomial expansion, not certified quadrature. The coefficient
  identity is imported using the October30 normalization assessment.
  These passages supply no finite four-coefficient error budget.

- Fredrik Johansson, *Numerical integration in arbitrary-precision
  ball arithmetic*, arXiv:1802.07942v1 (22 February2018),
  [Sections2/2.1](https://arxiv.org/html/1802.07942v1), read through
  the evaluation-limit case: interval evaluation must enclose the true
  function; analytic ellipse bounds require a holomorphy check. A work
  limit retains interval enclosures without guaranteeing accuracy.
  Inspect the final radius, not requested tolerances. This agrees with
  the stable [Arb2.23 acb_calc contract](https://arblib.org/acb_calc.html),
  evaluator and Integration sections, which leaves improper tails to
  the caller. Recently revised FLINT documentation was consulted but
  is not the sole authority for these claims.

- [NIST DLMF3.5(ii)](https://dlmf.nist.gov/3.5.ii), equations
  (3.5.6)-(3.5.8), supplies the selected real-arithmetic alternative:
  for real f in C^4[a,b], n positive and even, h=(b-a)/n, composite
  Simpson error is -(b-a)h^4 f^(4)(xi)/180 for some a<xi<b.
  The full rule, smoothness condition and remainder were read.
  Import this standard theorem; the finite integrand derivative bound
  remains a specialization. This method needs no complex branch check.

- [DLMF8.2.2](https://dlmf.nist.gov/8.2.E2) defines the upper gamma
  integral; [8.4.8/8.4.11](https://dlmf.nist.gov/8.4.E8) gives
  Gamma(k+1,z)=k! exp(-z) sum_(l=0)^k z^l/l!, k>=0 integer.
  Only positive real z is proposed; its path avoids zero and the
  negative axis. These identities evaluate polynomial-exponential
  majorant integrals after the comparison has been proved; they do
  not supply a theta majorant. DLMF8.4 identifies version1.2.8.

- [Python Decimal documentation](https://docs.python.org/3/library/decimal.html),
  exp, next_minus/next_plus, contexts, rounding and signals were
  inspected, reusing the November5 arithmetic assessment. Exp is
  correctly rounded half-even; neighbors and directed basic operations
  support outward evaluation. Flags persist. Constant enclosures,
  argument signs, denominator bounds, exponent range and actual runtime
  still require checks. Square-root endpoints can be independently
  validated by rational square comparisons; directed sqrt is not assumed.

The read-only environment check found no Python flint module.
This does not block the selected Simpson method with outward real
arithmetic. No package was installed or mathematical script run.

### Outstanding specialization and bounded test

For j=0,1,2,3 retain the actual (3.3) weight and (1.7) summands.
The later proof must choose X>1 and N and bound separately the omitted
n>N contribution on [1,X], the full x>X integral, finite quadrature
remainder and arithmetic/constants. It must justify sum/integral
comparisons and normalization. Explicit polynomial-exponential
majorants are needed; an O-constant or first-summand numerics do not
suffice. No such estimate is derived in this review.

For the finite integrand, verify C^4 and bound its fourth derivative
throughout [1,X], including x=1, before applying Simpson's theorem.
The complete derivative bound, two explicit tails and actual interval
width are the acceptance evidence. Coverage permits proving these
specializations later; it does not establish their constants or
guarantee adequate running time.

The concrete downstream diagnostic is L530's cubic in t^2 with actual
m_j=c_(2j)/c0, rational radii, interval discriminants and exact root/
multiplicity cases. Four enclosures make that test well-defined;
the proposed width is not assumed sufficient to sign its discriminant.
An interval meeting zero is inconclusive. Existence of six initial real
roots and preservation are separate. All-degree positivity, an actual
invariant and Xi transfer remain open regardless of a finite sign.

Queries: `Romik 1902.06330 Hermite coefficients numerical integration`
(Hermite results were distinguished from c_n),
`"Romik" "c_6" "coefficients"`, `"1902.06330" "certified"`,
`site.arblib.org acb_calc_integrate rigorous integration error holomorphic`,
and the DLMF integer upper-gamma identity. No stronger matching
certificate was inspected; search-only secondary hits are not inputs.
Petras's original paper and the Gaussian-error references remain unread
leads, unnecessary for the selected Simpson method. No absence or
novelty inference follows. Matching Mathlib coverage remains unchecked.

Decision: SPECIALIZE for one later finite certificate. The checked
sources do not provide its actual values; the needed work is explicit
error specialization and implementation, not reproof of the expansion.
Outcome EXPLORATION/NOVELTY_UNCHECKED records new source coverage,
not a coefficient result or lemma. Mathematical counters are unchanged.
A creative central mechanism remains unjustified without a concrete
actual-input invariant; routine coefficient certification is not creative.
