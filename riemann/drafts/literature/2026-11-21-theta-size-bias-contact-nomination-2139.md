# Theta-law size-bias interface: completed source comparison

TARGET: Assess whether Biane-Pitman-Yor Proposition 3.1(i)'s size-biased theta-law identity yields a closed operator after the log-coordinate half-tilt and L058's positive quadratic tilt, with an independently testable d=2 contact constraint.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2140 searched exact size-bias/log-quadratic-tilt/heat-Hankel terms, stronger fixed-point and shot-noise terminology, and narrow theta/contact records. Retrieved Pitman-Yor2003 Proposition12 and its relevant proof cases; reused the ready BPY probability, weighting and score comparisons. No inspected source supplies the requested tilted contact constraint; no novelty inference.
SOURCE_EVIDENCE: BPY2001 Sections2.1-2.2/(2.8)-(2.17), Proposition3.1(i)/(3.20), p446; Pitman-Yor, Canad.J.Math.55(2)(2003),292-330, DOI10.4153/CJM-2003-014-x, Section6.3 Proposition12(i),(iii)-(v), (120)-(126), pp318-320, including the full relevant transform/ODE proof. Existing Patil-Rao1978 Section1/(1.1) and Ley-Swan2013 Definition2.1/Theorem2.2 coverage reused. Two newly located rStation theorem statements compared below without importing their claims.
COMPARISON: The classical identity characterizes the unweighted positive theta variable, with independent variables on its right side. Its published proof uses an ordinary Laplace transform, not logarithmic moments after positive heat tilt. Ready weighting calculus permits an explicit applicability attempt with domain checks; it does not preserve independence or supply contact signs. The physical law is distinct from C874b's auxiliary node measure.
GAP: Construct and verify the changed-law operator; determine whether its direct action closes on the finite even-log-polynomial space needed by d=2, or exhibits an unpaid nonpolynomial observable. No such operator, closure, contact exclusion or flux sign is established here.
REASON: Essential classical proof coverage is now accessible. Authorize only the bounded changed-law/finite-closure specialization below, after the supervisor's separate approval of this newly ready continuation; no same-turn mathematical derivation and no automatic sign import. Further source work needs a changed essential hypothesis or specific unread source.
SCOPE: Known-method specialization at lambda=1/16, full log coordinate followed by the justified even/half-line identification with L058, and direct operator action on span{1,u^2,...,u^16}. Retain conditional H3>=0, H2c=0, real c!=0, lower-degree null vectors and S_2=0 as separate cases; do not assume a contact exists. No iteration, zero preservation, finite-moment-law sweep or all-degree inference is covered.
COVERED_TARGET: Construct the BPY size-bias operator for L058's law at lambda=1/16 with all log-coordinate, half-tilt and normalization factors, and test direct closure on even polynomials through degree sixteen as a bounded d=2 contact mechanism.
LITERATURE_REASON: The supplied target was REVIEW_REQUIRED because Proposition3.1(i)'s proof and its changed-law scope had not been inspected; existing Section2, weighted-law and score coverage alone did not assess this specific identity.

## Completed review — 21 November 2026, step2140

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate source question is exactly TARGET. A
closed, independently informative relation for the actual law could
constrain the otherwise unpaid degree-two flux. No complete route to
RH, contact sign, contact existence or impossibility is obtained.
Outcome EXPLORATION, kind LITERATURE, classification NOVELTY_UNCHECKED:
this is a source comparison and a bounded continuation, not a new
mathematical result. No lemma, script, PROOF.md argument or DAG edge
is changed.

### Primary statements and essential proof cases

[Biane-Pitman-Yor2001](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf),
published version, Section2.2 Proposition2.1, p439, identifies
Y=(pi S2/2)^(1/2), with density y^(-1)H(y) and E[Y^s]=2xi(s).
Section2.1 defines H in (2.8)-(2.9) and gives yH(y)=H(1/y).
Reuse the ready Section2 assessment rather than reprove these facts.
Proposition3.1(i), p446, characterizes nonnegative X of mean 2/3
by X*=X+HX* in distribution: X* has the size-biased law and the
three right-hand variables are independent, with H-density
h^(-1/2)-1 on (0,1). The proof paragraph points to reference[75]
and Yor's PartII, p26. The latter remains unread and is unnecessary
because the published reference[75] proof is accessible below.
The random H here differs from both the density function H(y) and
the local Hankel matrices. BPY's S2 is not the coefficient S_2.

[Pitman-Yor2003](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D91B384C84FA02C55A332B396BB85385/S0008414X00033484a.pdf/infinitely-divisible-laws-associated-with-hyperbolic-functions.pdf),
published version, Section6.3 Proposition12, pp318-320, supplies the
missing proof source. For X>=0 with mean 2/3, its parts(i),(iii),(iv)
equate the S2 law, the Laplace equation

    phi'(a)/phi(a)=2 integral_0^1 (1-m)phi'(a m^2) dm, a>0,

and the same size-bias identity. Read the full (iii)<=> (iv)
argument (125), the (iii)<=> (v) integration/ODE argument
(126),(123), and (v)<=> (i), including the initial normalization
and mean. These arguments concern nonnegative Laplace parameters.
The adjacent Poisson fixed-point implication (ii)=> (iii) uses
the Levy-density/Fubini calculation (124). It supplies no domain
theorem for a positive exponential of a squared logarithm. The
Meixner tilt in Section4, (67), uses a linear tilt of a different
variable and cannot justify that substitution. No reproof of the
classical characterization or audit of its ODE uniqueness is claimed.

The ready
`2026-11-10-h-derivative-boundary-profile-review-174.md` and its
audit review already inspected Patil-Rao, Biometrics34(2)(1978),
179-189, Section1/(1.1), pp179-180: a nonnegative weight requires
a finite nonzero normalizer. Reuse that definition only. Their
OCR-damaged optional mean-comparison theorem is not needed.
Reuse Ley-Swan2013's endpoint/test-domain qualifications through
`2026-11-09-actual-theta-score-contact-41.md`; no Stein sign is imported.

### Applicability limits and recorded failures

L019 identifies the local positive kernel and its superexponential
tail; L058 gives compact domination of polynomially weighted heat
integrals. BPY supplies the full positive-variable density and its
reciprocal relation. Together these provide the inputs for checking
a change of variables and its endpoints in a later mathematical
specialization. They do not by themselves identify a transformed
coupling or establish its absolute integrability. In particular,
all ordinary powers being integrable alone would not license the
positive squared-logarithm tilt. Its two endpoint estimates must be
checked using the actual density, retaining the Jacobian, half-tilt,
normalizer and reflection to the local half-line convention.

An identity in distribution allows integrable tests of its two sides.
It does not license replacing X,X* and H independently by their
tilted counterparts. Any weighted two-variable formula must retain
the joint weight evaluated at the sum. A closed nonlocal operator
with an explicit fixed kernel is also different from closure on a
finite polynomial space; neither property gives a sign automatically.
No transformed formula or claimed independence is derived here.

Read L874's response and domain proof, C874b's contact reduction,
and the conclusions/hypotheses of C874c-d. The flux uses the degree
twelve R and the degree fourteen u^2R; the H3 premise also involves
S_8 and hence ordinary moments through degree sixteen. A test
ending at degree fourteen would omit part of the contact input.
C874b's two positive-flux formal examples and C874c-d's ordinary
moment compatibility are preserved. Those laws are not actual theta
or counterexamples to this specific law identity. Repeating finite
PSD or ordinary moment compatibility cannot supply the new interface.

Reuse the November6 and November9 score reviews and
`ATTEMPTS/2026-11-06-contact-score-automatic-sign-source-stop.md`.
Generic positivity, curvature, absolute covariance, the same score
integration by parts and an RH-conditional real-zero theorem do not
pay the signed observable. The node-mass stop of step2139 concerns
the missing comparison with the auxiliary atomic measure; its inverse
Christoffel formula is singular at contact. A size-bias operator for
the physical law does not identify those two measures. The proposed
finite operator-closure test is distinct from reopening either sign
import or an exhausted moment sweep.

### New leads: compared statements, no imported theorem

Two relevant author manuscripts surfaced in the bounded search.
[bramble_trace, paper136/v1](https://rstation.ai/problems/riemann_hypothesis/papers/136),
9November2026, Section1 (2)-(4), Theorems1-3 and Section3.3
(20)-(21), concerns a mean-matched compressed heated theta source
under binary branching, with a boundary-layer limit. Its source
coordinate includes a separate compression a(tau), and its transition
is not BPY's size-bias equation. Theorem2 concerns positive boundary
measures; its explicit limits leave zero preservation and control
beyond the Laplace pole open. Theorem statements and these relevant
source/likelihood-ratio passages were inspected; its certificate and
full proof were not verified and are not inputs to this continuation.

[bramble_trace, paper141/v1](https://rstation.ai/problems/riemann_hypothesis/papers/141),
9November2026, Section1 (1)-(7), Theorem1 and Corollary2, concerns
additive gamma perturbations and an affine theta iteration. Its
perturbation, reciprocal Mellin transform and escaping-zero claim
differ from retaining L058's prescribed positive heat tilt. It
cannot be used as a zero-preservation theorem or a counterexample
to the present law. The stated size-bias specialization refers back
to the classical hyperbolic-law results. Only these statements and
the stated scope in Section2 were inspected; the Mellin-Barnes and
universality proofs remain unread. None of these claims is imported
or treated as independently audited evidence of an obstruction here.

### Bounded mathematical continuation

The exact COVERED_TARGET is the one next action. At lambda=1/16,
construct the operator by applying the classical identity to the
correctly changed test, without re-proving the fixed-point theorem.
Fix the direct convention: in the size-bias expectation identity use
the original test f(x)=w(x)P(log(sqrt(pi*x/2))), where w is the full
weight defining the desired changed law and P is the chosen even
polynomial. Determine w and its normalization in the attempt; do
not rescale the resulting operator by an arbitrary state function
or choose a different test to force finite closure.
State its integration measures and domain and prove all necessary
endpoint/absolute-integrability claims. Verify the full-log to even
half-line identification before interpreting a local moment. An
unknown tilted auxiliary law cannot be replaced by independence.

Then test the direct operator on the fixed finite space
V16=span{1,u^2,...,u^16}. Here finite closure means an exact
pointwise action in that space, with explicit coefficients and no
unpaid higher moments, fitted moment-dependent projections or
hidden signed expectations. If the operator first requires an even
projection, include it explicitly. Do not assume closure or tune a
different operator to enforce it. A proved nonpolynomial image of
one basis element is a discriminating negative result for this
specific finite-closure mechanism, independently of RH and without
assuming an actual contact. It does not disprove the existence of a
useful nonlocal operator.

Continue this finite-closure route only if the domain and exact
closure pass and an additional relation relevant to L874's degree-two
flux survives beyond its existing normalization/null equations.
Otherwise retire this sufficient mechanism and preserve the explicit
unpaid observable or obstruction. Do not repeat operator bookkeeping
as a sign advance. Even success would leave the sign, uniformity in
lambda, actual H3/contact existence, S_2=0/lower-degree cases,
initialization, tangency, higher degrees and endpoint continuation
unresolved. No solution candidate is asserted.

This is a known-method changed-law specialization and finite closure
test, appropriately routed calculation/standard/high with future
classification REPRODUCTION. A protected creative sign attempt is
not yet justified: no independently sufficient signed coupling
kernel has been specified. The supervisor separately approves this
newly ready continuation; no mathematical step runs in this review.
Full matching and supporting Mathlib coverage for this transformed
operator is not checked. No cross-notebook input is used.

### Search record

Queries included `Biane Pitman Yor Proposition 3.1 size biased S2 H X
theta 2001`, `theta size-biased quadratic tilt`, `S2 size biased fixed
points shot noise transform`, `Riemann size bias heat Hankel`,
`theta size-biased log operator`, `S2 Pitman quadratic tilt`,
`Biane Pitman Yor Hankel`, `Riemann theta size-bias operator tilt`,
`Pitman Yor logarithmic tilting S2` and `size biased log quadratic`.
Followed BPY reference[75] to the published primary proof. Shot-noise
and Barnes-beta hits remained uninspected leads, not theorem evidence.
No inspected statement supplies the transformed finite closure or
the desired signed contact constraint; search failure proves no
absence or originality.

Local searches used specific theta/contact assessments and stops,
with size-bias, perpetuity, gamma-sum, closed-operator and score terms;
then read only the named relevant ranges. Existing Section2 and
weighted-law reviews were reused. No sibling proof/checkpoint was
read. The initial notebook-scoped git status produced excessive
untracked-file output; it was not used to select mathematical inputs
and no global status or further archive orientation was performed.

## Original nomination — step2139, retained as history

The nomination below records the earlier unread proof/interface state;
the completed comparison and current decision above supersede it.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
A closed identity for the specific tilted law could expose information
absent from ordinary finite compatibility and support a kernel-specific
contact constraint. No signed implication is asserted.

The primary [BPY source](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf)
characterizes its nonnegative S2 law with mean 2/3 by the size-bias
identity X*=X+H X* in distribution, with independent right-hand variables
and H-density h^(-1/2)-1 on (0,1). Its proof paragraph refers to earlier
sources; their proofs and a tilted specialization remain unread.
This is a source lead, not an imported lemma in the RH argument.

Essential local objects: L019,L058,L874,C874b-C874d. Reuse the named
Section2 assessment for the original probability normalization. Search
narrowly for size-bias/branching/gamma-sum and tilted-law failures before
further proof retrieval. The half-tilt, log coordinate, positive quadratic
tilt, independence and normalizer require explicit source comparison.
No Brownian coupling, real deformed zeros or all-degree sign is assumed.

Continuation test: retrieve primary hypotheses and essential proof cases,
then identify a genuinely closed transformed operator and one finite
observable whose estimate can fail independently of RH. Abandon if
closure requires unknown tilted laws/normalizers with the same unpaid
sign, or merely rewrites the stopped modular/score interface. Do not
derive and approve the operator in the source turn. A later creative
nomination needs a precise new obstruction and bounded discriminator;
both remain missing here.

Actual contacts, H3 positivity, initialization, equality, higher degrees,
global continuation and Mathlib coverage remain unresolved. No
cross-notebook input is proposed. This nomination does not reject the
completed node-mass review.
