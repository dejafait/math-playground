# Capped rare cubic: completed bounded source comparison

TARGET: Test whether L418's capped rare cubic satisfies F_lambda(H)=beta_* (log H)^2+o((log H)^2) for some fixed lambda>0.
CHECKED: 2026-10-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 156 checked the exact local definitions/failures and searched joint Hardy-jet tails, truncated absolute mixed moments, derivative moment lower bounds and scalar large deviations; the primary theorem comparisons below found no adequate match for the fixed radial cap. This bounded search does not establish novelty or nonexistence of a matching theorem.
SOURCE_EVIDENCE: Curran--Heycock arXiv:2403.00902v1, Theorems 1.1--1.2, Sections 2, 3.1--3.3 and 4; Arguin--Bailey arXiv:2202.06799v2, Theorem 1.1 pp. 1--2 and Section 2's three-case assembly p. 8; Arguin--Creighton arXiv:2603.01711v1, Theorem 1.1 and Section 2.2; Arguin--Bailey--Roberts arXiv:2604.25579v1, Theorem 1.1 and Proposition 1.3. Reuse L390/L406/L409/L410 and audited L419 within their unchanged scopes.
COMPARISON: The unconditional sources supply magnitude moment bounds or scalar level-set estimates, not a capped absolute polynomial of ordinary real jets coupled to the complete actual response. The newer general upper-tail theorem assumes RH. The known signed cubic and L419's O(log H) bulk do not evaluate the multiplier or its leading constant.
GAP: Evaluate or rigorously obstruct the fixed-lambda capped absolute mixed moment at beta_* log^2 H; in particular retain the response and critical-direction correlations on both sides of rho=lambda log^2 H. No suitable joint restricted-moment asymptotic or uniform-integrability premise was found in the inspected results.
REASON: Essential comparison is sufficient for one bounded mathematical test using the ready unconditional moments and the exact radial split; import those results by their existing citations and derive only an application or a certificate obstruction in a later research turn. No capped estimate or new lemma is proved here.
LITERATURE_REASON: The next target concerns a fixed radial cap correlated with the actual critical jets, outside the completed bulk-audit scope; the ready uncut signed moments do not assess this essential absolute-tail input.
SCOPE: Exactly L418's F_lambda on every sufficiently large real dyadic interval, fixed lambda>0, ordinary jets through order two, uniform height measure and full actual response including curvature; no H-dependent lambda, response relocation, RH, independence or new distributional hypothesis.

## Proposed test and relevance

The main gap remains actual negative-Bcal clipping and L413's complete
regulator-scale error margin toward global mixed positivity. This target
tests the independent remaining moment condition of one prescribed-response
partial law, not RH or an actual clipped statistic.

Use exactly L418's notation: X0=(f,f'/L,f''/L^2), rho=|X0|,
D=Delta(X0;t), B=Bcal(X0;t), E=H^-1 integral_[H,2H], and

    F_lambda(H)=E[|D B| min(1,rho/(lambda (log H)^2))].

Lambda is a positive constant independent of H. The required beta_* is
L409/L410's exact positive constant. L418 currently proves only
0<=F_lambda(H)=O((log H)^2). L419's audited bulk adds O(log H).
The unresolved equality must hold for every sufficiently large real H
in the asymptotic sense, not only along a subsequence. A height-dependent
lambda, an adjustable response or a relocated height is a changed target
and is not silently allowed.

The downstream use is completion or rejection of this rare/bulk ansatz's
last scalar asymptotic. Even success would leave actual/global critical
realization, actual clipping, the full-error regulator comparison and
global mixed positivity unresolved.

## Original review remit (completed below)

Use essential inputs L390, L406, L409, L410, L418 and audited L419.
Compare the existing primary moment sources first, then narrowly seek
joint ordinary Hardy-jet tails, truncated absolute moments and relevant
uniform-integrability hypotheses. Retain both sharp endpoints, the
actual complete response, exact curvature and all magnitude correlations.
Identify theorem statements and essential proof cases before drawing a
comparison; an unweighted moment or scalar tail is not automatically the
required mixed absolute asymptotic. The known signed benchmark is an
input, not a license to remove the cap or absolute value.

The October-16 sign-only and capped-radial failure records retain their
scopes. This is an unevaluated independent threshold, not a reopening of
the persistently blocked direct signed-clipping search. Do not repeat
that search or infer novelty from absent matches. If essential source
coverage is persistently blocked, park this dependent test and route to
a materially different, independently testable target.

Continue to a mathematical attempt only after this exact target has an
IMPORT, SPECIALIZE or EXPLORE assessment. A positive answer requires the
stated asymptotic for at least one fixed lambda; a rigorous incompatible
bound or failure of convergence can stop this ansatz without refuting
conditional feasibility in general. Inconclusive envelopes remain
inconclusive. No such estimate is derived in this proposal. Full matching
Mathlib coverage is not checked.

## Completed source comparison — 2026-10-16, step 156

### Exact scope and local reuse

Read L418's full statement and proof, L406's source application and
separate audit, L390's hypotheses and physical/fourth-moment bounds,
L409's signed asymptotic and exact coefficient, L410's constants and
constraint scope, and L419's conclusion. The complete response, ordinary
derivatives, curvature, sharp dyadic average and real-H quantifier are
part of this target. No new audit of these inputs is claimed. In
particular L418's full separate audit is still outstanding.

The approved cubic-physical-replacement and full-response-cubic-passage
assessments remain adequate for their existing uncut uses. The step-150
prescribed-marginal review and step-154 bulk review do not assert a
restricted absolute mixed moment. The exact capped and sign-only failure
records in ATTEMPTS were checked by their relevant passages. L418 is
already the partial construction; repeating it would not answer this
target. Audited L419 removes the bulk obligation only.

### Primary theorem comparison

**Curran--Heycock.** M. J. Curran and A. Heycock, *Sharp bounds for joint
moments of the Riemann zeta function*,
[arXiv:2403.00902v1, 1 March 2024](https://arxiv.org/html/2403.00902v1),
Theorems 1.1--1.2 (PDF pp. 1--2). For fixed n, 0<=k<=2,
h_j>=0 and h=sum h_j<=k, Theorem 1.1 bounds

    integral_[T,2T] |zeta|^(2k-2h) product_j |zeta^(j)|^(2h_j)
        << T(log T)^(k^2+2 sum_j j h_j).

Theorem 1.2 gives the corresponding lower bound for n=1, k>=0,
0<=h<k+1/2. Section 2 uses Re(zeta'/zeta); Sections 3.1--3.3
use Holder and prime-polynomial good/bad sets. Section 4 uses Cauchy,
reflection for negative real shifts and analytic rectangle approximation
for k>=1/2. Thus sharp intervals are covered. These are bounds, not
asymptotics for the target. Ordinary real Hardy derivatives contain the
phase terms in L406 (4); a complex derivative lower bound does not
directly lower-bound their real combinations. No theorem here keeps the
radial cap or the response correlation. Reuse L406's existing application;
no reproof is needed. The fixed-order Cauchy prefactor typo already
recorded in L406 does not change that bound.

**Scalar unconditional upper tails.** L.-P. Arguin and E. Bailey,
*Large Deviation Estimates of Selberg's Central Limit Theorem and
Applications*, [arXiv:2202.06799v2, 21 February 2022](https://arxiv.org/pdf/2202.06799v2),
Theorem 1.1, printed pp. 1--2: for uniform tau on [T,2T] and
V~alpha log log T, 0<alpha<2,

    P(log|zeta(1/2+i tau)|>V)
       << exp(-V^2/log log T)/sqrt(log log T),

uniformly for alpha in compact subsets of (0,2). Read the scalar
prime-sum reduction (p. 3) and Section 2's Propositions 2.1--2.3
and assembly (p. 8), separating initial failure, later failure and the
final good event. The range stops short of alpha=2; these events are
not ordinary-jet radial events. This upper estimate supplies neither
the target coefficient nor a response-weighted lower bound.

**Recent scalar lower tails.** L.-P. Arguin and N. Creighton,
*Lower bounds for the large deviations and moments of the Riemann zeta
function on the critical line*,
[arXiv:2603.01711v1, 2 March 2026](https://arxiv.org/html/2603.01711v1),
Theorem 1.1: for fixed alpha>0, V~alpha log log T, a positive
K_alpha gives

    T^-1 meas{t in [0,T]:log|zeta(1/2+it)|>V}
       >= K_alpha integral_V^infinity exp(-y^2/log log T)
                                      /sqrt(log log T) dy.

Read Section 2.2's restricted mollified second/fourth-moment
Paley--Zygmund mechanism and its required good-event conditioning.
The statement uses [0,T], not this target's sharp dyadic interval;
subtracting two lower bounds would not justify a dyadic lower bound.
It contains no lower bound for the absolute physical polynomial on
those scalar level sets. No extension to that observable is imported.
This is an inspected preprint statement, not an independent audit of
its proof.

**Conditional upper-tail extension excluded.** L.-P. Arguin, E. Bailey
and A. Roberts, *Conditional Upper Bounds for Large Deviations and
Moments of the Riemann Zeta Function*,
[arXiv:2604.25579v1, 28 April 2026](https://arxiv.org/html/2604.25579v1),
Theorem 1.1 allows fixed k>0 and V~k log log T but explicitly
assumes RH. Proposition 1.3 exposes the conditional pointwise
prime-sum bound used in the proof. This is not an unconditional
replacement for the endpoint missing from the preceding upper-tail
theorem and cannot be a premise here. No further proof extraction is
needed for that exclusion.

### Search record and unimported leads

Queries included `Riemann zeta joint derivatives truncated absolute
moments large values Hardy Z derivatives distribution`, `zeta joint
moments lower bounds derivatives Curran Heycock`, `Hardy derivatives
joint distribution moments truncated`, `zeta absolute mixed truncated
moments derivative`, and `Arguin Bailey Lower bounds for the large
deviations arxiv`. Searches also checked large-deviation estimates
without RH and exact joint-Hardy terminology. No exact cap theorem
was located in this bounded search; this is not a novelty claim.

The Arguin--Bailey off-line lower-tail paper (arXiv:2403.19803) was
an abstract-level lead only, superseded for this comparison by the
inspected critical-line statement above; no theorem from it is used.
Random-model derivative tails, CUE joint moments, scalar extreme-value
theorems and Heycock's thesis are search leads, not inspected matching
theorems. A model law does not transfer to the actual response graph.
No Mathlib matching theorem was checked; unknown coverage is not absence.

The NSF upper-tail PDF endpoint failed once and a requested nonexistent
v3 HTML did not load. The primary arXiv v2 PDF was then retrieved with
its version and theorem hypotheses. No essential source remains blocked,
and repeated access attempts are not a proposed continuation.

### Ready bounded attempt and stopping test

Decision EXPLORE authorizes exactly the TARGET, with no new theorem
claimed beyond these sources. Start with the split at
rho=lambda(log H)^2 and the ready fourth/absolute-third moment bounds;
test whether the available restricted or interpolated estimates give a
coefficient or a strict incompatibility with beta_*. Keep |Delta Bcal|,
both radial regions and the full actual response. Do not replace this by
the signed L409 integral, scalar zeta tails, a generic random law or an
independence premise. Any fractional-moment application must keep its
fixed parameters and stated unconditional range. No such calculation
is performed in this literature step.

Continue this ansatz if a proved leading asymptotic meets the exact
positive beta_* for one fixed lambda, or if a new quantitative bound
leaves a specific discriminating estimate accessible. A rigorous
incompatible coefficient/bound or failure of convergence rejects this
ansatz's equality, not conditional feasibility in general. If the
bounded moment/shell test yields only L418's existing O(log^2 H)
envelope, record that certificate's failure without inflating it to
an estimate of the actual F_lambda. Do not repeat the same envelope
test or reopen the blocked signed-clipping source search under a new
name. A changed observable or extra distributional hypothesis needs
separate REVIEW_REQUIRED coverage.

Even success would leave L418's separate audit, actual/global critical
realization, actual clipping, L413's complete regulator margin and
global mixed positivity unresolved. The source review establishes no
new capped estimate and changes neither PROOF.md nor the canonical DAG.
