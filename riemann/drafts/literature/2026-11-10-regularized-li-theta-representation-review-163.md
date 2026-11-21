# Regularized Li observable and the actual theta kernel — source comparison

TARGET: Assess whether L964's regularized form Q_eta(n)=sum_j beta_j^2 a_n(beta_j)^2/(beta_j+eta), with eta=1/(64*9^n), has an explicit convergent representation in the actual L019 theta kernel that isolates a nonnegative contribution and a fully specified signed remainder, without assuming RH.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step164 searched Li/theta logarithmic integrals, rational zero resolvents, theta-Laguerre formulas and product logarithmic derivatives; compared L242/L044/L046 and saved step159 coverage. No inspected theorem states this regularized Q_eta representation or signs its remainder; bounded coverage does not establish novelty.
SOURCE_EVIDENCE: NIST DLMF1.10(viii)-(x), especially1.10.18-24 and surrounding hypotheses, and1.4.12-13, version1.2.8; Lagarias AIF57(5)(2007) Theorem3.1/(3.1)-(3.6), pp.1704-1706, reused with saved applicability assessment and checked against the primary passage. Local L019-L021/L024-L026/L030/L242/L964 read in full. Coffey JAT146(2)(2007),267-275 remains abstract-only, not theorem evidence.
COMPARISON: Known product differentiation, dominated analytic integration and finite higher-chain rules cover representation tools; L242 supplies the first actual-theta signed derivative and its pointwise-sign obstruction. They do not supply the higher rational combination for Q_eta, its nonnegative part, full signed remainder or a remainder inequality. Lagarias's Li-class evaluation does not directly cover the additional regularizing denominator.
GAP: Specialize these tools to the exact rational observable, preserving every node/multiplicity and cancellations at beta=0, and give finite coefficient formulas and absolutely convergent theta integrals for every retained term. A useful sign decomposition and any inequality controlling its remainder remain unproved.
REASON: Essential tools are accessible independently of the unread Coffey paper. Approve one bounded representation attempt under the unchanged target using finite rational partial fractions and local theta/logarithmic identities; cite the standard tools and do not infer a sign from K>0. This literature-only turn derives no representation.
SCOPE: Actual Xi; integer n>=1; a_n exactly L964(5); eta=1/(64*9^n); actual paired beta nodes with multiplicity; algebraic squares; actual L019 K. Only finite rational-resolvent/higher-logarithmic-derivative specialization and its complete convergence/sign-decomposition test; no RH, ordinate substitution, positive Stieltjes measure or new zero-free region.

## Gap, use and decision test

The main gap remains L030-L032/C032a actual-Xi mixed positivity.
The intermediate target is a representation identifying an explicit
signed remainder suitable for a later inequality test. Audited L964-L965
explain its downstream relevance through conditional finite polynomial
detection. Neither an actual negative Li margin nor all-degree signs follow.

Continue only with a finite checkable coefficient recipe, every
interchange justified, an identified nonnegative contribution and a
fully retained remainder. Its sign may remain open. Reject an RH-assuming
positive-measure import, summation of divergent separated constants,
modulus-square substitution or an omitted tail. A formal identity or
the tautology Q=max(Q,0)-max(-Q,0) is not the requested input. Failure of
one ansatz is not nonexistence of all representations.

## Primary statements actually inspected

[NIST DLMF1.10.23-24](https://dlmf.nist.gov/1.10.x) assumes analytic
factors on a domain and locally uniform product convergence. If all
factors are nonzero there, the product is nonzero and its logarithmic
derivative is the sum of the factor logarithmic derivatives. Use a
zero-free neighborhood, not a global logarithm across zeros.
[1.10.18-19 and the M-test](https://dlmf.nist.gov/1.10.viii) allow
analytic differentiation of an improper parameter integral under compact
uniform convergence; an integrable common majorant suffices.
[1.10.20-21](https://dlmf.nist.gov/1.10.ix) gives a product M-test.
These tools supply no sign. Version1.2.8, released15 September2026,
was inspected on10 November2026.

[DLMF1.4.12-13](https://dlmf.nist.gov/1.4.E13) gives Leibniz and
Faà di Bruno formulas. In1.4.13 the finite sum is over nonnegative
m_1,...,m_r with sum(j*m_j)=r and k=sum(m_j), with term

    r!/(m_1!...m_r!) * f^(k)(g(x))
      * product_j (g^(j)(x)/j!)^m_j.

All requisite constituent derivatives must exist at the evaluation point.
The formula licenses neither an unverified integral differentiation nor
a logarithm through a zero. A later use must specify f,g and their domain.

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier57(5)(2007),1689-1740,
[Theorem3.1, pp.1704-1706](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=17),
evaluates the Weil form on G_n(s)=1-(1-1/s)^n. The Li class comprises
rational functions vanishing at infinity with poles contained in {0,1}.
The broader test class in(3.1) requires holomorphy in the open strip and
uniform O(1/|s|) outside the central horizontal band; its quadratic sum
is absolute. The positivity discussion uses RH.
Reuse L964's normalization and
[step159's assessment](2026-11-10-li-negative-margin-mixed-transfer-review-158.md),
including the Suzuki moment and ordinate-only warnings. The extra
denominator in Q_eta is not a direct instance of this exact Li-class
evaluation. A rational resolvent reduction needs its own applicability
and convergence argument; no new Weil identity is asserted here.

## Local overlap and recorded failures

L019-L021 give actual K, its superexponential bound and the entire
cosine representation with every fixed derivative. L024-L026 give the
paired product, absolute reciprocal mass, geometry and multiplicities.
L030 retains algebraic squares; L964 defines a_n and proves Q_eta absolute.
These are reused, not reconstructed.

L242 is a partial match: for F(x)=Xi(i sqrt(x)) and G=F'/F on x>=0,
it gives G'=E_x[b_x]+Var_x(a_x) as a complete double theta integral.
Its kernel has both signs on actual support. It does not evaluate this
n-dependent regularized observable. L044 disproves preservation of
ordinary moment Gram positivity by the required logarithm map. L046
records the variance correction invalidating termwise log-concavity.
All three proofs were read. None excludes a theta-specific integrated
inequality retaining every term.

The read records
ATTEMPTS/2026-11-05-theta-nested-threshold-stable-law-stop.md and
ATTEMPTS/2026-11-07-exact-finite-quartic-theta-representation-stop-98.md
exclude different realizations, not rational differentiation of actual K.
No model law or fitted positive measure is proposed.

## Bounded specialization for a later mathematical turn

Start from L964's exact P_n and a_n, respecting its branch normalization
until the algebraic square is treated correctly. Test finite rational
partial fractions using the displayed denominator factors beta+eta
and 1+beta/4. This is an ansatz, not a proved reduction or sign claim.
Test expression of the convergent zero sums through logarithmic
derivatives of F at positive real arguments, using the paired product.
Then apply the cited finite chain rule and actual theta integrals.
Determine the evaluation points and derivative orders in the attempt;
no specialized formula is imported here.

Every separated zero sum must converge or stay grouped with its exact
cancelling constant. Cover beta->0, pole multiplicities, all n including1,
realness and every zero multiplicity. Prove denominator positivity and
integrable bounds for each derivative/product at every evaluation point.
Finite products become multiple integrals only after absolute Fubini.
Keep all negative coefficients and subtraction terms explicit. A split
into positive integrals and a signed remainder is useful only if it
identifies a later non-tautological inequality; it supplies no estimate.

The tools are known calculus; the complete representation and informative
decomposition remain obligations. No new lemma, script, identity or
sign estimate was derived in this literature-only review. No change
to PROOF.md or DAG.md is needed. Full Mathlib coverage was not checked
and remains unknown. No cross-notebook input is used.

## Search and access record

Queries actually used included `Li coefficients theta function integral
representation logarithmic derivative cumulants`, `Riemann xi logarithmic
derivative theta integral rational functions zeros resolvent`, `DLMF
partial fractions rational function logarithmic derivatives canonical
product`, the exact Coffey theta-Laguerre title with pdf/arxiv qualifiers,
and `Coffey Li constants Bell polynomials xi derivatives theta integrals`.
No inspected theorem matches Q_eta. Failed search proves neither novelty
nor nonexistence.

M. W. Coffey, *The theta-Laguerre calculus formulation of the Li/Keiper
constants*, J. Approx. Theory146(2)(2007),267-275,
[DOI10.1016/j.jat.2006.10.006](https://doi.org/10.1016/j.jat.2006.10.006),
is abstract-only: the publisher PDF endpoint returned403. Its advertised
theta reformulation is not read theorem evidence. Park direct import
from it; the independent elementary test above does not depend on it.
Related arXiv:math-ph/0505052v1 was searched narrowly for theta/integral/
Bell/cumulant terminology; no relevant full theorem was inspected or
imported. McCullagh cumulant and external RH/positivity search hits
are unused leads, not essential inputs: the inspected finite chain
rule supplies the required tool.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. Essential coverage
is now ready for a separately gated mathematical attempt. This is not
a mathematical advance or a claim beyond the sources checked.
