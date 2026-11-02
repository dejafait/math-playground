# Corrected total-law quartic defect: completed source comparison

TARGET: Test L473's full corrected law for an eventually nonzero quartic stationary-path defect, retaining its rare component, covariance correction and actual-Hardy endpoint terms.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L473 at its complete construction and source interfaces, L580, the paired-moment coverage/application assessments, L424's different transport test and the uncorrected-bulk failure; bounded external derivative-bound and stationary-quartic searches found no inspected theorem deciding this exact corrected law. No novelty inference follows.
SOURCE_EVIDENCE: Reuse the inspected transport/integrability sources in 2026-10-31-quartic-stationarity-bulk-separator.md; newly inspect Bui--Hall arXiv:2304.05178v1 printed p. 1 immediately before (1), Proposition 3 p. 14 and Sections 5/7 pp. 15--16. The primary fixed-order pointwise derivative bound covers the endpoint input; arithmetic-source proofs remain imported.
COMPARISON: L580 supplies the necessary stationary identity and only the uncorrected-bulk value; L473 supplies the full rare measure and matrix correction. The source bound covers ordinary Hardy derivatives at both dyadic endpoints, but neither source evaluates their contribution to this total-law defect. Leading fourth asymptotics alone are inadequate for that signed comparison.
GAP: Specialize transport with ell fixed, retain and bound the actual endpoint term, and test the complete corrected-law signed defect including the exact rare quartics and the matrix perturbation. No total-law value, asymptotic or sign has been derived in this review.
REASON: Essential source coverage now suffices for one bounded corrected-law calculation, with no process-realization theorem needed. This newly changed ready assessment receives separate approval before research; the completed source review itself supplies no new lemma.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes from an uncorrected finite bulk to L473's exact total law and adds an actual-Hardy endpoint requirement; the earlier ready scope expressly excluded both.
SCOPE: Exactly L473's nu_H with ell=log H fixed, paired separation 1/ell, w_H, eta_H, R_H and A_H as in (14)--(18), and the first-marginal polynomial x_0^3 z_0+3x_0^2 y_0^2 from L580. Eventual real H with uniform constants; ordinary derivatives, all rare quartics and both actual endpoints. No re-fitted law, moving divisor, additional polynomial search, derivative-preserving correction, realization or Xi conclusion.

## Original nomination, retained

The main gap is actual-Xi all-degree positivity at unbounded height.
The proposed intermediate purpose is to decide whether the full existing
finite-moment counterlaw, rather than its uncorrected bulk alone, has
the elementary stationary extension obstruction. This could identify
an exact requirement on a derivative-preserving replacement, but would
not decide general feasibility or supply actual-Hardy/Xi transfer.

Essential local inputs are L580's finite-fourth stationary identity,
L473 Sections 5--6 (rare fourth moments and covariance correction), and
the actual-Hardy moment/boundary sources used by that construction.
L472 explains the bulk's provenance; L424 and L576--L579 are contrasts,
not additional premises. No cross-notebook result is nominated.

The next source review must keep the exact corrected distribution and
all terms, distinguish the fixed-H jet scaling from ordinary path
derivatives, and retain any boundary term before seeking its bound.
Approximate matching of fourth moments alone does not sign their
quartic linear combination. No cancellation, asymptotic size or sign
of the total defect has been derived here. In particular the small
probability of a component never licenses dropping its fourth moments.

Continue toward mathematics only if the source comparison covers the
exact construction, transport specialization and requisite endpoint
estimates sufficiently to permit a discriminating nonzero test. The
literature-only turn must not derive or evaluate the changed law's defect;
any uncovered specialization belongs to a later approved research turn.
If essential source hypotheses or error bounds remain unavailable, park
that dependent calculation and choose an independently testable mechanism;
do not retry the stopped wave/packet parameter searches. A zero total
defect would stop this separator and would not establish stationary
realization. Mathlib coverage of the changed application is not checked.


## Completed review, 2026-10-31

### Exact construction and reusable coverage

Read L473's definitions, Sections 5--6 and their application-audit
checks, together with its arithmetic interface and scope qualifications.
The law being tested is the sum of its unnormalized rare measure eta_H
and mass w_H times the law of sqrt(ell/w_H) A_H B. In particular (14)
retains every actual fourth monomial F_m(H) exactly; (15)--(18) give the
bounded second-matrix contribution, the noncommuting positive-square-root
correction, its uniform norm estimate and the bulk's quartic scale.
These are existing canonical results, not fresh calculations here.
The correction acts on six coordinates and need not preserve jet dynamics.
Its effects on the selected polynomial must be estimated, not omitted.

L580's proved finite-fourth stationary identity applies to each fixed-H
law if it were the ordinary jet marginal of a translation-invariant
Borel C2 path law. L473's fixed-H support supplies finite moments; no
height-uniform fourth-moment bound for such hypothetical paths is assumed.
L580's expectation/Fubini argument need not be reproved.

Reuse the exact primary coverage already inspected in
`2026-10-31-quartic-stationarity-bulk-separator.md`:
Lasserre--Henrion--Prieur--Trelat, SIAM J. Control Optim. 47 (2008),
1643--1666, [arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7),(2.10)--(2.12), manuscript pp. 3--5; and
Henrion--Korda--Kruzik--Rios-Zertuche,
[*Occupation measure relaxations in variational problems: the role of convexity*, 2023-03-04](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
Definitions 2.4/2.7, (6)--(8), pp. 3--4, and Lemma B.1/proof,
pp. 17--18. The necessary deterministic identity retains endpoints.
No realization, no-gap, invariant-law or height-limit theorem is imported.
The changed finite-interval specialization remains research work.

### Primary endpoint statement and arithmetic qualifications

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/pdf/2304.05178v1),
printed p. 1, Introduction immediately before (1), states the pointwise
bound Z^(k)(t) <<_k T^(1/6) at height t of order T, for fixed derivative
order k. The PDF and [primary HTML](https://arxiv.org/html/2304.05178v1)
agree. Import only k=0,1 here; no RH, simplicity, exceptional-height or
growing-order hypothesis is attached to that bound. The paragraph uses
it without proof; no independent subconvexity proof audit is claimed.
Proposition 3, p. 14, has four independent complex shifts O(1/log T),
uniform error O(T(log T)^3), and explicitly omits its proof. Sections
5/7, pp. 15--16, give the Cauchy and Hardy-conversion passages. These
confirm the already assessed arithmetic scope; the pointwise bound,
rather than a signed fourth-moment asymptotic, supplies the endpoint lead.

For applicability, both endpoints have large positive height and only
fixed derivative orders are required. The divisor is the single fixed
ell in L473, not log(2+t). A later proof must rescale the ordinary path
before using L580's polynomial, keep the two terminal test values and
show that their complete contribution is below the proposed separating
scale. This review does not perform that chain-rule or boundary estimate.
No random-process stationarity is asserted for sharp dyadic sampling.

### Searches, overlap and decisive later test

Reused the paired-height assessment
`2026-10-28-two-height-hardy-jet-moment-coverage.md` and the separate
L473 application assessment `2026-10-28-l473-critical-audit-coverage.md`.
Read the relevant L424 source interface and exact boundary identity:
it treats L423, a Gaussian test and a moving divisor, so its small
boundary budget cannot be copied for this polynomial. The prior
uncorrected-bulk stop and L576--L579 wave/packet stops remain scoped
evidence, not a prohibition of this distinct full-law test.
The relevant construction, assessment and failure records contain no
completed corrected-law evaluation of this polynomial.

External queries included `Hardy Z derivatives pointwise bound Z prime
T 1/6 logarithm fourth moments boundary Bui Hall`, `Hardy stationary
fourth moments derivatives`, `Bui Hall stationary quartic`, and
`occupation measures stationary fourth derivatives`. The searches
returned general moment/occupation results and unrelated leads, not an
inspected matching corrected-law theorem. Search snippets, AI research
pages, repository mirrors and informal probability discussions are not
inputs. A Bourgain subconvexity query was an unused alternative lead;
its theorem/proof was not read or imported, since the exact Hardy
derivative bound above already addresses the needed source scope.

The later bounded test is eventual nonvanishing of the complete signed
expectation of L580's polynomial under this exact nu_H. A useful
sufficient discriminator is a positive eventual lower bound for its
absolute value divided by ell^2, after all endpoint and correction costs
are proved. This is a sought threshold, not an achieved estimate. Retain
the signed rare contribution exactly until the transport comparison
legitimately bounds it. Do not replace actual moments by their leading
coefficients with a larger uncontrolled remainder.

A proved nonzero defect excludes this particular stationary extension;
zero defect stops this separator without establishing realization.
Failure of a covered estimate must be recorded honestly, without packet
parameter retries. General stationary feasibility, derivative-preserving
replacement, all fourth constraints, actual-Hardy clipped mass and
actual-Xi signs remain independent open gaps. No justified central
creative mechanism is supplied by this routine specialization. Full
matching Mathlib coverage remains unchecked. This review writes no
lemmas or mathematical scripts and evaluates no changed-law defect.
