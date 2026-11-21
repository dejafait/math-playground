# Degree-one contact polynomial dual — completed source review

TARGET: Assess primary coverage for a degree-at-most-nine odd polynomial integration-by-parts dual certificate of L874's genuine d=1 contact flux, retaining the exact tilted theta score and finite null equations, and specify one bounded residual-sign test or retire this ansatz.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step176 read L874 through its complete score/boundary argument, reused the November6 score and November9 GHS reviews, and compared the two-point, generic-monotone, reciprocal-quadratic, bare-contact, reciprocal-determinant and primitive-square stops. New density-operator and polynomial-dual queries are recorded below. No matching contact-sign theorem was found; no novelty or impossibility conclusion follows.
SOURCE_EVIDENCE: Ley-Swan, Electron. Commun. Probab.18(2013), paper7, Definition2.1, Theorem2.2 and both proof directions, pp2-3, primary journal PDF; Fantuzzi-Goluskin-Huang-Chernyshenko arXiv:1512.05599v2, Section4(4.2)-(4.10), Proposition3 and its integration-by-parts argument, pp8-9. Exact URLs and differences below. Reused Saumard coverage; did not retry parked EMN/Newman blockers.
COMPARISON: The density approach supplies the known zero-mean correction rule with explicit endpoint and integrability obligations, but no sign. The auxiliary-function source supplies a pointwise sufficient-bound template, not an actual-theta diffusion theorem or an SOS solver for the transcendental theta score. A fixed seven-coefficient pilot below asks for additional sign evidence beyond L874; feasibility is untested.
GAP: Prove or obstruct the specified complete pointwise residual under the actual finite contact equations. No coefficients, residual inequality, actual contact, contact flux sign, parameter-wide continuation or new mathematical lemma is established. Neither finite sampling nor a non-theta pseudo-moment obstruction decides the actual-law pilot.
REASON: Essential primary operator coverage is now available without the GHS access blockers. Prepare one bounded mathematical pilot rather than another automatic-score search; its new assessment requires separate next-turn approval before research. Retain all earlier stops at their original scopes.
SCOPE: Completed literature-only comparison for genuine d=1 contacts. The future pilot fixes lambda in [1/4,1/2], c0^2+c1^2=1 with c1 nonzero, a single constant coefficient tuple in [-16,16]^7, an odd multiplier of degree at most nine and the complete half-line residual. No derivation, coefficient search, optimization or mathematical script was performed.
LITERATURE_REASON: The new finite density-dual class was outside the ready score/GHS assessments; primary density-operator hypotheses and the polynomial-versus-transcendental certification distinction were essential unread coverage.

## Completed review — 9 November 2026, step176

The main gap is L030-L032/C032a's actual-Xi all-degree mixed positivity.
The reviewed intermediate target is a direct polynomial correction of
L874's genuine degree-one flux. A successful conditional certificate
could supply one decreasing-parameter boundary sign in a fixed parameter
band. Contact existence, initialization, tangency, other parameters,
lambda=0 and higher degrees remain independent gaps.

### Inspected primary results

[Ley and Swan, *Stein's density approach and information inequalities*](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf),
ECP18(2013), paper7, DOI10.1214/ECP.v18-2578, final journal version
superseding arXiv:1210.3921v1: Definition2.1 and Theorem2.2, pp2-3,
define the density operator T_p f=(fp)'/p on an interval-supported,
positive, normalized, differentiable density. The test class requires
fp to be differentiable inside the support and to vanish at both
endpoints. Read both proof directions: the direction needed here is
the integral of (fp)' with its endpoint difference; the converse uses
indicator-centered integral tests. We use only smooth tests with
absolutely integrable derivative, avoiding any reliance on an
unqualified improper-integral interpretation. This is a zero-expectation
rule, not a signed inequality or a finite-degree existence theorem.

[Fantuzzi, Goluskin, Huang and Chernyshenko](https://arxiv.org/pdf/1512.05599v2),
*Bounds for deterministic and stochastic dynamical systems using
sum-of-squares optimization*, v2, 11 June2016: Section4, pp8-9,
(4.2)-(4.10), Proposition3. Its stationary diffusion setting requires
a probability density satisfying the stationary Fokker-Planck equation,
an existing observable expectation and the boundary integral (4.5).
The proof adds a zero-expectation generator term and imposes a pointwise
sign; (4.10)'s polynomial SOS formulation requires polynomial drift and
observable. Read the integration-by-parts step and the reversed-sign
upper-bound case. This is a template comparison only: no theta SDE,
stationarity, ergodicity or polynomial drift is asserted or needed.

The second result is not a substitute for the first result's exact
density operator. The actual score contains K'/K; multiplying by K
leaves exponential theta series, not a polynomial. Thus neither an
unqualified finite SDP nor a polynomial Positivstellensatz is imported.
The new pilot would need its own rigorous complete score enclosures or
an analytic inequality. No existence/completeness guarantee is claimed
for a degree-nine multiplier or for the coefficient box.

### Applicability interface and fixed proposed test

L019/L058 give the positive normalized tilted law on (0,infinity).
L874 gives the exact score and complete polynomial-weighted K and K'
integrability/boundary estimates, including its independent step11
audit. That audit was already present; the older description of L874
as unaudited is stale. No new audit is performed here.

The primary rule's test is a multiplier, not L605's centered Stein
kernel. Its score must be that of the tilted half-line density: both
2lambda u and K'/K are retained. Odd multipliers vanish at zero;
the recorded theta tail estimates are the inputs for checking their
other endpoint and absolute-integrability hypotheses in a research
application. We specify the future residual expression below, without
deriving or certifying it in this literature turn.

The separately nominated pilot has seven real constants
(a0,...,a4,alpha,beta) in [-16,16]^7, chosen once, independently of
lambda, c, moments, flux and u. Set P(u)=sum_(j=0)^4 a_j u^(2j+1).
Use L874's exact R, with no truncated theta score. The proposed
upper-bound residual is

    Q(u) = u^2 R(u) + P'(u) + (2lambda u+K'(u)/K(u))P(u)
                         + alpha R(u) + beta u R'(u).

The pilot asks for Q<=0 for every u>=0 at every actual-theta contact
with 1/4<=lambda<=1/2, c0^2+c1^2=1, c1!=0, H1>=0 and H1 c=0.
Both null rows S2 c0+S3 c1=0 and S3 c0+S4 c1=0 must be retained,
including S2=0 cases; no division by S2 is licensed. The two final
terms use L874's already stated zero expectations, not replacements
for those full hypotheses. The coefficient normalization and window
are pilot restrictions, not known sufficient ranges. No actual contact
in the band is asserted. Conditional success must be reported as such;
an empty contact set is not evidence of a new boundary mechanism.

The exact Next action and this fixed scope are saved in
[the pilot assessment](2026-11-09-contact-polynomial-dual-pilot.md).
A certificate would have to check u=0, the compact interior and the
whole infinite tail. A numerical mesh supplies neither existence nor
a negative result. The distinguishing evidence is a separately signed
Q, rather than a restatement of L874's expectation identity. A rigorous
infeasibility argument must concern this actual-law constrained class;
failure on arbitrary moments or noncontacts only rejects a relaxation.
An unproductive attempt ends at its first unresolved term without
enlarging degree, box or parameter window. No calculation is approved
until this newly written continuation receives its separate review.

### Duplicates, failures and search record

The ready November6 score comparison already inspected Saumard's
identities and absolute bounds; these do not acquire a sign here.
The two-point stop L604 concerns a particular oscillatory two-copy
remainder. The audited L607 refutes generic monotone-Stein transfer,
while L606 places its fixed reciprocal-quadratic model in a known
real-zero class. None tests this actual-theta, finite-contact residual.
The bare L874 stop says u^2 R itself changes sign. Here an independently
signed correction is sought; merely choosing a multiple of uR and
reproducing (4) is not success. The reciprocal-determinant stop C785a
and primitive-square mismatch L876 concern different algebraic/operator
representations and supply no sign for Q. The GHS cone access blockers
remain parked and are not dependencies of the density rule.

Narrow local searches covered the nomination, the two ready source
comparisons, named ATTEMPTS and density-operator/polynomial-contact
terms in drafts/literature and ATTEMPTS. No local matching polynomial
dual was located; this is not a novelty assertion. New web queries:
`polynomial Stein operator dual certificates moment bounds integration
by parts polynomial optimization density method`; `"Riemann" "theta"
"polynomial" "Stein" contact`; `stationary distribution polynomial
test function moment bounds linear programming adjoint generator dual
certificate`; `Ley Swan density approach Stein operator 2013 boundary
f p derivative`; `Fantuzzi Goluskin bounds averages auxiliary functions
pointwise inequality theorem stochastic systems polynomial`; and the
exact Ley-Swan title. Retrieved the primary theorem hypotheses before
the relevant proof cases. The Luxembourg PDF timed out; the primary
journal mirror above supplied readable pp2-3, resolving access for this
input. No API key, paid source or GHS access retry was used.

Search hits on polynomial moment-SOS certificates and algebraic Stein
operators for Gaussian polynomials are unread theorem leads, not
applicability evidence. No bounded-domain theorem is extended to the
half-line by analogy. Full and supporting Mathlib coverage for the
specific pilot have not been checked; absence is not asserted.

Outcome EXPLORATION: new primary coverage removes the operator-source
blocker and makes a precise pilot reviewable, but no theta sign or
obstruction has been established. No progress beyond checked sources
is claimed. No lemmas, mathematical scripts, DAG or PROOF were changed.

## Original nomination (historical; not the current scope)

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
L874 has an independently audited finite contact identity but no signed
flux. Its genuine d=1 response has degree eight, which motivates a fixed
degree-nine odd multiplier cap for this source question; this cap is a
proposal, not a sufficiency claim. Essential inputs for any later attempt
would be L019/L058/L874, the exact theta score, its complete boundary and
tail control, and the source-defined dual rule. L904 is motivation only,
not a mathematical input to a contact inequality. No cross-notebook input.

The candidate differs in intended evidence from the blocked GHS route:
it would need a pointwise residual certificate with explicitly checkable
coefficients under the actual law, rather than membership in an unread
correlation cone. It also differs from simply deriving L874 again. No
claim that such a residual exists is made. A dual identity alone is not
a sign; allowing arbitrary coefficients or leaving an unbounded support
remainder unsigned would not give the proposed bounded test.

Continue only if inspected primary hypotheses and the overlap comparison
permit one finite coefficient class with explicit permitted dependence on
lambda, moments and c, a specified parameter domain, and a complete
residual-sign criterion including u=0 and infinity. The test must separate
a new theta-specific bound from L874's existing zero-expectation identity.
Retire this ansatz if it merely returns that identity, relies on the desired
flux/higher-degree positivity, duplicates a stopped pointwise Stein test,
or cannot specify such a bounded test with available primary coverage.
Do not enlarge the polynomial cap to rescue a failed test within this
nomination. Generic-law countermodels alone would not settle applicability
to the exact theta law.

The next source review should narrowly compare the existing actual-theta
Stein assessments and the recorded two-point/generic-monotone/fixed-
reciprocal-quadratic pointwise failures before pursuing new primary dual
theorems. Those detailed older proofs were not loaded for this nomination;
their relevance and exact overlap remain review obligations. Reuse their
ready portions rather than repeat source searches. This is not a new
approval of the already blocked automatic-score or GHS mechanism.

A successful conditional d=1 flux certificate could supply one boundary
direction for decreasing-parameter positivity. Contact existence, strict
versus tangential crossing, initialization, continuation to lambda=0,
higher degrees and uniformity remain independent gaps. No complete RH
candidate is proposed. Creative escalation is blocked until a distinct
source-covered residual test is specified. Full/supporting Mathlib
coverage for the proposed dual has not been checked.
