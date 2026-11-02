# General periodic clipping: completed differential-dual source review

TARGET: Assess a family-independent periodic clipping bound at 1/288 under L586's finite-cone covariance remainder, including total-derivative dual certificates.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-observable, periodic interpolation and auxiliary-function searches plus scoped local duplicate/failure checks found no inspected theorem deciding the unrestricted 1/288 problem; primary pointwise-dual statements and their boundary/weak-bound derivation were read. Queries and read/unread distinctions follow; no novelty inference is made.
SOURCE_EVIDENCE: Chernyavsky--Bramburger--Fantuzzi--Goluskin arXiv:2110.03079v1 Lemma 2.1 and (2.4)--(2.11), printed pp.8--10, and (3.4)--(3.10), pp.14--15; Fantuzzi arXiv:2201.00362v1 Lemma 5/(10), p.3; Tobasco--Goluskin--Doering arXiv:1705.07096v2 (1)--(8), pp.1--2, and compactness-dependent (15c) proof, p.5. L586/L588 supply the exact cone interface; L473 Section 4 supplies the finite-law comparison.
COMPARISON: Pointwise-dual methods cover sufficient total-derivative certificates, not feasibility or sharpness at 1/288. Sharp fixed-ODE compact-state duality does not apply here. L473's covariance-K finite law has clipped mean 1/144 but lacks stationary path realization by L580; whether quadratic differential storage distinguishes it must be tested before larger searches.
GAP: No universal clipping bound, feasible above-threshold periodic path, sharp duality or optimizer is established. The identified specialization is a bounded quadratic certificate/obstruction test retaining all six coordinates, the actual cone dual and both clipping branches; nonlinear storage, general periodic feasibility and Xi transfer remain outside this test.
REASON: Essential sources now support one restricted mathematical test. Import the sufficient-certificate method and test the local difference; do not reprove the general method, assume compactness or repeat an offset-family scan. No calculation, new derivation, lemma or mathematical-script edit was performed in this literature turn.
SCOPE: Original question: every real smooth P-periodic h, P>0, with K-C(h) in L586's actual C_I; no Fourier cutoff, zero-mode restriction, common period, probability normalization, fourth completion or Xi realization. Technique coverage is restricted to the proposed homogeneous quadratic storage/majorant test below.
LITERATURE_REASON: The saved REVIEW_REQUIRED nomination moves beyond L588's fixed family and needs essential unread differential-dual hypotheses; unchanged Fourier/cone, Laguerre and failure comparisons are reused.

## Exact question and relevance

Use L586's six ordinary lag-one jets J_h, covariance C(h), A(u),
I=[-1/2,1/2] and K=integral_I A(u)du. The original question is the
supremum of average_(0,P) (h h''-(h')^2)_+ over K-C(h) in C_I.
A bound strictly below 1/288 excludes every such single periodic bulk.
A rigorously feasible path at or above it distinguishes the general
class from L588; later L587 use also needs an interior remainder and
independent fourth/probability assembly. Neither answer transfers the
nonlinear observable to actual Xi.

The main gap is actual-Xi all-degree signs at unbounded heights. This
surrogate test is not a creative central-Xi mechanism: a controlled
nonlinear transfer input remains missing. Elapsed discovery intervals
do not themselves supply that input.

## Inspected primary coverage

A. Chernyavsky, J. J. Bramburger, G. Fantuzzi and D. Goluskin,
*Convex relaxations of integral variational problems: pointwise dual
relaxation and sum-of-squares optimization*,
[arXiv:2110.03079v1, 6 October 2021](https://arxiv.org/pdf/2110.03079v1).
Read the continuous-integrand/growth hypotheses, pp.6--7; Lemma 2.1
and complete boundary/weak-bound derivation (2.4)--(2.10), pp.8--9;
zero-boundary-integral case (2.11), p.10; polynomial/SOS restrictions
(3.4)--(3.10), pp.14--15. The domain is bounded Lipschitz, u is
W^(1,p), and admissible C1 fields have an integrable chain-rule
divergence. Feasible pointwise inequalities give one-sided integral
bounds; equality of primal/relaxed values is unnecessary. Also inspected
Theorem 3.1/Remark 3.2, p.18: convergence needs an Archimedean condition
implying compact pointwise feasible sets. That conclusion is not invoked.

G. Fantuzzi, *Verification of some functional inequalities via polynomial
optimization*, [arXiv:2201.00362v1, 2 January 2022](https://arxiv.org/pdf/2201.00362v1),
Sections 2--3.1, pp.2--3, especially Lemma 5/(10) and its divergence
justification. For W^(1,p) functions on a smooth bounded domain, the
C1 test field must have an integrable chain-rule derivative. Its total
divergence integrates to boundary flux. Polynomial objective results
elsewhere are not imported as a theorem about a clipped integrand.

I. Tobasco, D. Goluskin and C. R. Doering, *Optimal bounds and extremal
trajectories for time averages in dynamical systems*,
[arXiv:1705.07096v2](https://arxiv.org/pdf/1705.07096v2), (1)--(8),
pp.1--2; proof of (15a)--(15c), pp.4--5, especially Sion's step for
(23). The PDF has an arXiv v2 marker dated 1 June 2017 and a title-page
date of 21 September 2022. Hypotheses include a well-posed C1 autonomous
vector field, compact forward-invariant B, continuous observable and
C1 auxiliary functions. Compactness of probability measures on B is
used in the minimax proof. No such common vector field/B is supplied
for all paths here. Sharpness and attainment are therefore not imported.

## Applicability checks and unperformed specialization

A proposed later test uses the four states
(h(s),h'(s),h(s+1),h'(s+1)); their derivatives are already present in
J_h. This avoids a third-derivative premise. On each [0,P], these
smooth states are W^(1,2), with matching endpoints. A state-only
quadratic test has integrable quadratic derivative. The later proof
must check its endpoint flux under the imported divergence identity;
no random-law limit, expectation differentiation or uniform compact
box is required. Treat each period separately without rescaling lag one.

The clipped integrand is continuous with quadratic growth. The
variational source allows continuous integrands. For the proposed
finite algebraic certificate, require a common majorant for zero and
x_0 z_0-y_0^2; do not differentiate a positive part or replace it by
its unclipped average. These are search specifications, not a bound
proved here. The research turn must write their exact implication.

L588 Section 1 already establishes the necessary cone-dual inequality
for any nonnegative function in L586's actual entry space E. This is
the reusable interface for the covariance remainder. A proposed
multiplier H must be checked through f(u)=trace(H A(u)) on the full
closed I, respecting entry relations and off-diagonal conventions.
Ambient PSD remainder tests or sampled positivity do not certify this
condition. If needed, L588's audited exact Taylor-tail technique covers
these entry functions. No new coefficients or tail bounds are computed.

## Local duplicates and failures

Read L586 Sections 1--4, L588 Sections 1--3, and hypotheses/conclusions
of L576--L581; searched the scoped periodic/offset/wave/packet and
quartic-stationarity assessments/failures. L576/L577 stop independent
equal two/three-wave models. L578 assumes full spectral completion;
L579's finite-K packet stop already follows from its variance entry.
L588 stops a constant-offset cosine family. None supplies a general
periodic clipping bound.

L580/L581 rule out particular laws using quartic derivative identities,
not all periodic bulk. L473 Section 4 (11)--(13), read narrowly, already
provides a bounded finite vector B with E BB^T=K and E Q(B)=1/144.
These are existing results, not recalculated here. This makes it
necessary to test whether quadratic differential storage adds
constraints beyond K before a large certificate search. No implication
or obstruction is derived in this literature turn.

Reuse the inspected primary Laguerre comparison in
`2026-10-31-three-wave-stationary-bulk-review.md`: its real-zero/class
premise is absent here. Cone/cubature assessments concern linear
moments and do not decide clipping. L585/L587 remain possible later
assembly, retaining the non-effective carrier and L473's arithmetic
qualifications, not an actual-Xi transfer theorem.

## One bounded continuation, pending separate approval

The nominated target is:

    Test whether homogeneous quadratic periodic total-derivative certificates can bound L586's clipped mean below 1/288, using L473's finite law as an obstruction test.

Restrict V to a homogeneous quadratic polynomial in the four states
above and H to a real symmetric six-by-six matrix. For
v=(x_0,y_0,z_0,x_1,y_1,z_1), the proposed search conditions are

    v^T H v - D V(v) >= 0 for all v,
    v^T H v - D V(v) - (x_0 z_0-y_0^2) >= 0 for all v,
    trace(H A(u)) >= 0 for all u in I.

Here D V is the chain-rule expression using state derivative
(y_0,z_0,y_1,z_1). The proposed cost is trace(H K). These formulas
specify an unexecuted test; neither feasibility, optimality nor a new
certificate implication is asserted. First specialize the imported
sufficient-bound method and compare the exact quadratic relations
with L473's finite law. The standard spectral theorem for real
symmetric matrices covers quadratic nonnegativity/PSD conversion;
no reproof is needed.

A rigorously certified cost strictly below 1/288 would exclude this
single-periodic-bulk class. A rigorous obstruction to every certificate
in the quadratic class stops only that class. A finite-vector witness
is not a feasible periodic path. Solver failure or a crossing enclosure
is EXPLORATION. Do not increase degree or add a Fourier ansatz during
that attempt. Nonlinear storage and general periodic feasibility stay
open. New coverage is saved separately for supervisor approval before
research; this source turn does not invoke the test.

Essential input IDs: L473 Section 4, L586, L588. L580 is a failure
comparison. Fourth/probability completion and nonlinear Xi transfer
remain independent. No cross-notebook input. Full matching Mathlib
coverage is not checked; unknown coverage is not absence.

## Search evidence and unread leads

Queries included `Fantuzzi integral inequalities auxiliary functions
periodic functions polynomial differential inequalities sum of squares`;
`"h" "Laguerre" "positive part" periodic inequality`;
`"Tobasco" "Goluskin" "Doering" "auxiliary functions" 2018 bounds`;
`"Duality for variational problems" "Fantuzzi" 2019`;
`"Laguerre" "positive part" "inequality" periodic`;
`"periodic" "clipped" "covariance" derivative inequality`;
`"Laguerre inequality" "periodic" "positive part"`;
`"integral" "positive part" "ff" "derivative" periodic inequality`;
`"quadratic" "integral inequalities" "storage" periodic Fantuzzi`;
`"Laguerre" "inequality" "integral" "positive part"`;
`"f f" "f'" "positive part" "periodic" inequality`;
`"Gagliardo" "Nirenberg" "positive part" "second derivative" periodic`.

Hits mostly concerned unrelated clipping, ordinary norm inequalities
or particular PDEs. No exact matching theorem was inspected; that is
bounded discovery evidence, not a novelty/absence claim. Primary
statements and relevant boundary/weak-bound cases were retrieved before
larger source passages. No theorem from a search snippet or third-party
claimed RH page is used.

An attempted arXiv:1906.12136v3 URL returned 404; it was not read.
That optional sharp-duality lead is unnecessary for this sufficient
test and is not an essential blocker. Fantuzzi--Fuentes' *Global
Minimization of Polynomial Integral Functionals* was an abstract-only
lead and is not relied on. No further access retry is necessary.
