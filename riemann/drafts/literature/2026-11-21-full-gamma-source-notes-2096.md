# Full gamma source comparison2096

One literature-only screen of review2095's exact target. No theorem is
newly proved or imported into a canonical lemma. The main gap is
L030-L032/C032a actual-Xi all-degree algebraic mixed positivity.
The intermediate objective was a signed full-vector estimate toward
subpower energy, retaining C034v's head, boundary and every divisor
column. The screen found no such estimate in the sources inspected.

## Sources actually inspected

1. Maisara Shoeib, *Möbius Cancellation and the Limits of Operator
   Norms*, July2026, author-hosted
   [full manuscript](https://www.researchgate.net/publication/410602420_MOBIUS_CANCELLATION_AND_THE_LIMITS_OF_OPERATOR_NORMS),
   DOI10.13140/RG.2.2.23893.38884. Read Theorem2.3 and its complete
   phase-alignment proof, Corollary3.1, Proposition8.1, Lemma8.2,
   Theorem8.3, Lemma8.4 and Theorem8.5 with their proofs; also
   Section8.2, Theorem8.6 and its complete forward/converse proof,
   Corollary8.7 and Proposition8.8 with proof (printed pp5-6,18-21).
   For finite nonnegative coefficients twisted by a unit completely
   multiplicative character, unrestricted logarithmic-translation norms
   equal unsigned mass. For 0<=alpha<3/4, its Riesz-state energy has
   kernel Gamma(3/2-2alpha)(mn)^(1-4alpha)/(m^2+n^2)^(3/2-2alpha).
   State integrability for every positive alpha is RH-equivalent;
   unconditional finite-to-infinite convergence is stated only for
   1/4<alpha<3/4. These are manuscript assertions, not locally audited
   theorems. [Zenodo v1](https://zenodo.org/records/21455583), July20,
   was identified; its PDF returned429. Equality of that PDF with the
   inspected author-hosted text was not verified.

2. Terence Tao, *The logarithmically averaged Chowla and Elliott
   conjectures for two-point correlations*, Forum Math. Pi4(2016),e8,
   DOI10.1017/fmp.2016.6,
   [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/48514F53D73B2C1277BD7232630F0694/S2050508616000068a.pdf/the-logarithmically-averaged-chowla-and-elliott-conjectures-for-two-point-correlations.pdf).
   Read Theorem2, printed p3: fixed a1,a2 positive integers and b1,b2
   integers with a1*b2-a2*b1!=0; 1<=omega(x)<=x tending to infinity;
   the Liouville correlation weighted by1/n on (x/omega(x),x] is
   o(log omega(x)). Read the proof-strategy discussion pp4-5 and
   reduction cases in Propositions9/10, pp9-12. Theorem3 was retrieved
   only in part; its complete nonpretentiousness hypotheses are not an
   imported input. No general Möbius specialization is claimed here.

3. OpenAI, *Ordinary two-point correlations of multiplicative
   functions*, September24,2026, release revisionfd4aeeb2e,
   [primary introduction TeX](https://raw.githubusercontent.com/openai/math/fd4aeeb2e/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex),
   lines17-89 and169-233. Read Theorem1.1, definitions(1.1)/(1.2),
   Theorem1.2, Corollary1.3, explicit fixed-form/no-uniformity clauses
   and the centered-prime/vertex-normalization strategy. The quantitative
   Liouville claim is O_forms(X/(log X)^c), c>0 absolute, for fixed
   positive slopes and nonnegative intercepts with nonzero determinant.
   The general unit-disk multiplicative claim requires one uniformly
   nonpretentious factor: for every fixed Dirichlet character,
   inf_(|t|<=N)D(f,chi*n^(it);N) tends to infinity, with prime sum
   D^2=sum_(p<=N)(1-Re(f(p)*conj(chi(p)*p^(it))))/p. It gives no rate
   for fixed distinct nonnegative shifts. Proof sections were not
   audited; no claimed formalization was replayed. The discovery wiki
   was a locator only; comparison uses the primary statements.

4. Terence Tao, [*The Cotlar-Stein lemma*](https://terrytao.wordpress.com/2011/05/25/the-cotlar-stein-lemma/),
   May25,2011, Lemma1/(11)-(13). Read the finite Hilbert-space
   statement and ensuing explanation of scale decomposition. For
   T_i:H->H', both sums over j of ||T_i*T_j^*||^(1/2) and
   ||T_i^**T_j||^(1/2) must be <=M, uniformly in i; then
   ||sum_i T_i||<=M. No infinite-sum version or proof is imported.
   This is the author's exposition of the named classical theorem,
   not an arithmetic cancellation theorem.

5. NIST DLMF, current online equations
   [5.11.9](https://dlmf.nist.gov/5.11.E9) and
   [25.2.8](https://dlmf.nist.gov/25.2.E8), read November21,2026.
   The former states the vertical gamma asymptotic
   |Gamma(x+iy)|~sqrt(2pi)|y|^(x-1/2)exp(-pi|y|/2), y->+/-infinity.
   The latter, for Re(s)>0, integer N>=1 and away from s=1, is
   zeta(s)=sum_(k<=N)k^(-s)+N^(1-s)/(s-1)
   -s*integral_N^infinity {x}x^(-s-1)dx; source Apostol(1976),
   equation(25), p269, via Theorem12.21. Read both actual formulae
   and domains, not just search snippets. These known inputs support
   a proposed localization specialization; no tail inequality is
   proved in this turn. TeX downloads had unsupported content types;
   the displayed HTML mathematics was accessible. No access blocker.

## Comparison of the three mechanisms

**Gamma-state Gram control.** The inspected state is not C034r's
fixed theta-convolved bump, nor C034v's boundary-completed vector.
Its positive Gram formula supplies no upper for this vector. An
unrestricted translation norm cannot be substituted for a fixed-state
average. Conversely its norm obstruction cannot simply be applied to
the theta-smoothed completed operator: that is a different multiplier.
This distinction is important and prevents an overbroad stop. A finite
Gram formula without a quantitative estimate fails the discovery test.

**Multiplicative bilinear cancellation.** The known C034u(1) complete
square has all n,k in a moving dyadic interval, not one fixed shifted
correlation. Neither the older logarithmic statement nor the inspected
newer fixed-form claims supply growing-shift uniformity or the required
subpower quadratic-form upper. This is a hypothesis/strength mismatch,
not a mathematical impossibility theorem. No assertion that the newer
ordinary-correlation theorem is false, unproved in general, or absent
is made. Its long graph proof is unnecessary for this scope rejection.

**Logarithmic-scale almost orthogonality.** The local definitions do
not supply either of the required cross-product row sums for a
boundary-retaining decomposition. Smoothness, a positive Gram matrix
and a choice of integer cap are not those estimates. No actual-data
Cotlar obstruction or new cross-product bound is derived here.

All three direct imports are parked. This is new source comparison
that changes the next task, not a new upper bound or discovery beyond
the checked sources. No full signed cancellation mechanism was found.

## One independently testable restricted continuation

Nominate the exact target in review2096: at C034v's cap, test whether
the energy outside |u|<=4 log X is O_h(X^(-1)). This is a proper
localization subtarget, not the full subpower criterion renamed.
Its possible use is to separate remote phase alignment from the
remaining signed, dense low-frequency problem. Source evidence above
is enough to nominate a standard-input specialization, not to label it
creative or to assert its conclusion. The prospective proof must pay
the actual weighted Fourier multiplier, polynomial zeta factor, both
frequency ends and projection of the *whole* completed-operator error.
The required tail, logarithmic core upper, cumulative-energy bound and
actual-Xi mixed signs are all still unproved by this source review.

Continue only if the proposed tail holds at the single fixed cutoff,
uniformly for sufficiently large real X, using the existing joint cap
and no stronger Mertens or arithmetic sign premise. If it needs a
polynomial frequency cutoff, input-dependent cap or boundary deletion,
record the first unpaid inequality and abandon this specialization.
Even success justifies no chain of further tail lemmas: the next
central task would need a specific signed estimate inside that band.
A creative attempt is blocked by that missing estimate, not by the
historical route stops or the absence of a lemma quota.

## Local overlap, search evidence and limits

Reused source-notes2093 for GC1-GC11 rather than reopening its audit.
Read the stated input/conclusion and relevant sections of C034r/u/v;
read all six named stop records2076/2077/2079/2084/2087/2089. No local
pole or analytic-boundary stop is extended to global cancellation.
Targeted searches in November21 literature/attempts and C034 proofs
found no prior Shoeib/Cotlar/fixed-form comparison. A targeted tail
search also found C032y; its hypotheses/conclusion concern a
zero-ordinate Gaussian-resolvent tail, not this Fourier projection.
The old heat/Fourier relevance stop was read to check that a tail
alone is not being presented as paying an independent core estimate.
No cross-notebook input or all-notebook checkpoint scan was used.

Discovery queries included `"riemann-xi-zero-detection" "gamma"
cancellation`, `Möbius dilations theta kernel bilinear cancellation
Nyman Beurling unconditional norm`, `renormalized gamma Gram
logarithmic dilations Cotlar Stein almost orthogonality Riemann
hypothesis`, `"MÖBIUS CANCELLATION AND THE LIMITS OF OPERATOR NORMS"
github`, `"MÖBIUS CANCELLATION" "Theorem 8.5"`, `Möbius correlations
logarithmic averaged Elliott Tao theorem two point 2015 arxiv`, and
`Cotlar Stein lemma author lecture notes operators sum norm square
root summability pdf`. Followed the newer-correlations lead to its
pinned primary introduction. Other returned Nyman-Beurling,
quasi-orthogonal and rstation papers are unread leads, not premises.
Failed searches do not establish novelty. Full matching Mathlib
coverage of either the original full-energy target or the nominated
specialization was not checked. No mathematical exploration budget
was spent, counters were not reset, and no supervisor state was edited.
