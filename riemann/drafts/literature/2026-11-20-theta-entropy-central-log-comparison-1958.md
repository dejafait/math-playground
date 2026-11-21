# Theta entropy comparison1958 — completed source review1959

TARGET: Review entropy and variational log-integral inequalities for C028d's actual theta-moment polynomials, seeking a finite-degree signed-central upper bound with vanishing normalized cost as the cutoff grows, without assuming positive polynomial values or real roots.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1959 searched Gibbs/Donsker-Varadhan variational formulas, signed polynomial logarithmic integrals and Carbery-Wright log-norm bounds; checked scoped theta/central/height/Jensen assessments and C028a/c for duplicates. Queries, inspected passages and unread leads are in drafts/literature/2026-11-20-theta-entropy-source-notes-1959.md; no novelty inference follows.
SOURCE_EVIDENCE: Inspected Lacker-Mukherjee-Yeung arXiv:2206.01260v1 (2 June2022), (1.1)-(1.2), Theorem1.1 hypotheses/(1.5), and Theorem3.3/(3.1)-(3.2) with its complete proof, printed pp13-14. Reused source-notes1747/1587 and review182 only within their scopes. Carbery-Wright primary proof text was inaccessible/garbled and is not imported.
COMPARISON: Gibbs permits negative potentials and minus-infinity values; polynomial sign alone does not exclude it. But its partition function must be controlled, a trial variational law gives a lower partition bound, and the inspected quantitative refinement requires smooth strong concavity absent from the actual-family inputs. C028d gives log-integrability, not the required exponential or entropy estimates. No inspected theorem pays the central term.
GAP: No actual-theta partition-function upper bound with vanishing normalized cost is supplied. A numerator-only fractional-moment comparison can avoid a positive-polynomial premise but its baseline loss must be tested before actual-family use. Neither that loss nor an asymptotic estimate is calculated in this literature turn.
REASON: Complete essential source comparison and park automatic entropy transfer. Nominate only an elementary monomial-reference cost diagnostic under separate assessment1959; this tests the comparison itself without repeating Riccati, Cartwright or theta-variance work. It is not a creative central-gap solution.
LITERATURE_REASON: Startup assessment1958 was REVIEW_REQUIRED and no entropy primary theorem had been inspected; existing height and variance coverage did not cover variational direction, singular potentials or the partition-function interface.
SCOPE: Source comparison only for the exact L019/L021 theta moments and C028b/d/e reciprocal Jensen family, all integer d>=3, algebraic multiplicity, repeated real zeros and the ordered limits d then cutoff A. No shifted family, Gaussian replacement, heat-flow parameter, RH-equivalent positivity premise or new zero-free-region claim is covered.

## Exact interface and success threshold

Use L021's actual moments M_(2j), gamma_j=j!*M_(2j)/(2j)!,
b_j=gamma_j/gamma_0, and precisely C028d's

    P_d(x)=sum_(j=0)^d binom(d,j)*b_j*x^(d-j),
    Q_d(y)=P_d(y-b_1),
    f_d(y)=log|Q_d(y)|-d*log|y|.

C028d already supplies integral_R f_d=pi*H_d; C028e supplies
integral_(|y|>A*d)|f_d|<=8*M*d/A, M=exp(b_1)*F(1), A>=2sqrt(M).
These are inputs, not new derivations. The unpaid scalar target is

    limsup_(A->infinity) limsup_(d->infinity)
      (1/d)*integral_(|y|<=A*d) f_d(y)dy <= 0.

This is sought, never assumed. A useful intermediate source comparison
may instead isolate one explicit finite-degree error term with the
required vanishing normalized upper cost; other independent gaps can
remain open. A constant O(d) allowance is insufficient. C028b states
the relevance of H_d=o(d) to RH, not its availability as an input.

Read primary theorem hypotheses and essential proof cases for a
variational/entropy formula and any proposed signed extension. First
verify whether it applies to the actual factorial-weighted theta-moment
polynomial; do not assume a positive log-moment-generating representation.
Then check the direction of the inequality, the combined logarithm's
real singularities and a degree-uniform error. The usual positive
integrand Jensen inequality alone is no signed cancellation mechanism.
Do not repeat C028d's identity, C028e's tail proof, review1747's three
methods or the completed Riccati calculation.

Continue only if an inspected theorem and the actual-family interface
justify one concrete finite-degree test, with its exact sign and error
threshold. Otherwise record the first missing positivity, representation
or uniformity hypothesis and park this automatic transfer. This is not
permission to derive that missing mathematics during the literature
step. A future ready nomination needs separate approval; if creative,
it must specify a bounded discriminator and central-gap relevance.

## Completed comparison1959

The paragraphs above specify the unchanged reviewed target and threshold;
they do not approve that threshold as true. The precise source comparison
and qualifications are in
[source-notes1959](2026-11-20-theta-entropy-source-notes-1959.md).
Outcome EXPLORATION: no sufficient theta bound, new theorem, numerical
experiment or mathematical advance. Full matching Mathlib coverage is
unchecked. No cross-notebook input is used. The independently testable
continuation in assessment1959 needs separate approval before research.
