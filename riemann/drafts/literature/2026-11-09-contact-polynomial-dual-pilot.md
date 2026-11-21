# Fixed degree-nine contact density-dual pilot

TARGET: Test the fixed seven-coefficient degree-nine density-dual pilot for L874's genuine d=1 contacts on 1/4<=lambda<=1/2, proving a complete residual certificate or recording the first rigorous obstruction without enlarging the class.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step176's completed exact/stronger density-operator, polynomial-dual and stationary-expectation search in 2026-11-09-contact-polynomial-dual-discovery.md; the named actual-theta score, two-point/generic-monotone/fixed-reciprocal Stein, bare-contact, reciprocal-determinant and primitive-square stops were compared. No matching actual-contact sign theorem was found; novelty is not established.
SOURCE_EVIDENCE: Ley-Swan ECP18(2013), paper7, Definition2.1/Theorem2.2 and both proof directions, pp2-3; Fantuzzi-Goluskin-Huang-Chernyshenko arXiv:1512.05599v2 Section4(4.2)-(4.10), Proposition3 and boundary argument, pp8-9. Direct primary sources: https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf and https://arxiv.org/pdf/1512.05599v2 ; version and actual-law differences are retained in the completed source review. L874's existing step11 audit validates its finite identities, not a dual sign.
COMPARISON: Known density integration by parts covers the correction rule after its explicit boundary/integrability checks. Neither it nor the auxiliary-function comparison guarantees a degree-nine signed residual. The exact theta score is nonpolynomial, so a finite SOS solver or compact-support approximation cannot be imported as a complete certification method.
GAP: Find one constant tuple in the specified box giving the full residual sign on the actual contact set, or prove a rigorous obstruction within this fixed class. Contact existence, nonempty domain, parameter-wide sign, equality/tangency, initialization, lambda=0 and all higher degrees remain unproved. No new theorem or candidate coefficients have been derived.
REASON: This is an independently testable direct sign ansatz with an explicit finite coefficient class; it bypasses the parked GHS sources and asks for evidence beyond the existing zero-expectation identity. The separate literature approval on 2026-11-09 (step177) confirms this unchanged target and scope after checking direct primary URLs; no expansion of its class is authorized by an inconclusive pilot.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in this ready assessment; reuse the completed step176 comparison and verify the two primary links, without repeating discovery or testing the residual.
SCOPE: Only the exact seven-constant residual and domain below; coefficients are parameter-independent constants in [-16,16], lambda in [1/4,1/2], c0^2+c1^2=1, c1 nonzero, and the full actual-law H1 PSD/null hypotheses. No generic-law sweep, higher degree, larger coefficient box or wider parameter window is covered.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This pilot seeks only a conditional d=1 decreasing-parameter boundary
sign in one band. It is a new proposed sign mechanism, not a new Stein
identity, an RH-equivalent positivity import or a complete RH route.

Use L019/L058/L874 and their exact tilted law. Write R as in L874,
retaining its normalized moments and exact theta score. Choose a single
tuple (a0,...,a4,alpha,beta) in [-16,16]^7, independent of lambda,
moments, c and u, and set

    P(u)=sum_(j=0)^4 a_j u^(2j+1),
    Q(u)=u^2 R(u)+P'(u)+(2lambda u+K'(u)/K(u))P(u)
                                   +alpha R(u)+beta uR'(u).

The proposed discriminating test is Q(u)<=0 for all u>=0 and all
actual-theta contacts satisfying the scope. Both null equations
S2 c0+S3 c1=0 and S3 c0+S4 c1=0 and H1>=0 are mandatory;
S2=0 is not excluded. No contact is asserted to exist in this band.
The constants and band are fixed exploratory restrictions, not a
source theorem guaranteeing sufficient degree or size.

Before claiming a certificate, verify the primary density rule's exact
half-line specialization, absolute integrability and both endpoints
from L874's recorded K/K' bounds; retain the positive-tilt score term.
Then give a complete residual sign including zero, compact interior
and infinity. The source review proposes this expression; it has not
proved a new multiplier identity or any inequality for it.

Continue only on a separate signed residual or an informative rigorous
obstruction to this exact class. An identity that only rewrites L874,
an unsigned tail or a sampled mesh is insufficient. Failure on arbitrary
moment tuples or on noncontacts obstructs only that relaxation and must
not be called actual-law infeasibility. If no complete sign or valid
obstruction emerges in the bounded attempt, preserve the unresolved
term and reassess; do not enlarge the class within this nomination.
Unknown contact existence must be reported, and no vacuous success may
be counted as a new boundary mechanism.

No cross-notebook input, L904 dependency, GHS cone or theta-potential
convexity import is used. The known operator is imported, while any
successful new signed estimate would be only potentially new relative
to the recorded search. Full/supporting Mathlib coverage is unchecked.

## Separate source-gate approval — 9 November 2026, step177

Direct retrieval confirmed [Ley–Swan's final journal paper](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf),
Definition 2.1 and Theorem 2.2, pp. 2–3: interval-supported positive
normalized differentiable density, differentiable product and vanishing
endpoint products. Its forward proof integrates the product derivative;
the local application must still check absolute integrability and both
half-line endpoints. This review does not discharge those checks.

Direct retrieval also confirmed [Fantuzzi et al., v2](https://arxiv.org/pdf/1512.05599v2),
Section 4, pp. 8–9, especially (4.4)–(4.10) and Proposition 3:
stationarity, the vanishing boundary integral (4.5), and a global
pointwise generator inequality are essential. Polynomial SOS is a
sufficient formulation when drift and observable are polynomial.
This remains a template comparison, with no theta diffusion import.

The prior discovery assessment's duplicate/failure comparison is reused
unchanged. No new mathematical input, multiplier identity, coefficient,
contact, residual sign or obstruction was established. The exact TARGET
and seven-constant scope above are approved for one subsequent research
attempt; the density-rule specialization and full residual certification
remain that attempt's obligations. This repairs the missing direct-URL
process field only: outcome STALLED, with no mathematical counter reset
or claim of progress beyond the checked sources. Full/supporting Mathlib
coverage remains unchecked.
