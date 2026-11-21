# Actual-theta reciprocal Hankel contact test: completed source comparison

TARGET: Test whether the actual theta heat equation supplies c^T H_d'(lambda_*)c<=0 at each finite positive-parameter contact H_d(lambda_*)>=0, H_d(lambda_*)c=0, for H_d built from the logarithmic coefficients of Xi_lambda, without assuming higher-degree positivity.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact and stronger-result heat/Hankel/logarithmic-coefficient/Cole-Hopf/contact searches; read primary heat-zero and contour-Hankel cases and convex-invariance hypotheses below. Compared L057/L058, L843 and the ready signed-integral/coefficient-heat assessment. No inspected theorem signs this actual-theta finite contact; unsuccessful queries establish no novelty.
SOURCE_EVIDENCE: Polymath arXiv:1904.12438v2 Proposition3.1(i)-(ii), (28)-(33), full simple/repeated-zero proof; Rodgers-Tao arXiv:1801.05914v5 (1)-(4), Theorem1 and Theorem4.16; Tao 2017 polynomial-heat note (2)-(3), Exercise3; Deng-Yang-Lu arXiv:2608.11520v1 Proposition4.1/Theorem4.2 and proofs; Hamilton JDG24(1986) Lemma4.1/Theorems4.2-4.3 pp160-163, text of proofs; Horvath-Song-Terlaky arXiv:1607.01107v1 Theorem2.4. Reuse Shi source coverage from 2026-11-06-actual-xi-signed-integral-discovery.md.
COMPARISON: Known logarithmic heat transformations and zero dynamics provide differentiation tools, not this sign; real-zero energy arguments assume a real simple divisor. Contour-Hankel congruence moves coordinates of fixed zeros. L843 concerns factorial coefficient Toeplitz minors on one atomic law, not logarithmic reciprocal Hankel forms. Convex-invariance theorems require a defined vector field and a boundary condition on the whole state set; this proposed single-trajectory test supplies neither automatically.
GAP: The null-vector contraction for actual theta remains uncomputed and unsigned. Its dependence on coefficients outside H_d, any sufficient theta-specific estimate, contact existence/equality cases, initialization and degree-uniform continuation remain open. No all-degree positivity may be used to sign it.
REASON: Approve only one bounded attempt at the unchanged actual-theta contact question, after separate supervisor approval of this newly completed assessment. The discriminant is an exact flux expression with all uncontrolled terms retained and an independent theta sign input, or an explicit finding that this mechanism supplies none. No new identity or lemma is derived in this literature turn.
LITERATURE_REASON: Essential coverage for the startup REVIEW_REQUIRED target was missing: exact reciprocal-Hankel versus coefficient-Toeplitz overlap, repeated heat-zero cases, and the scope of semidefinite boundary reasoning. Ready coefficient-heat coverage was reused rather than re-audited.
SCOPE: The displayed actual theta family, Xi_lambda(0)>0, arbitrary fixed finite d, lambda_*>0 and real nonzero null vector c; one analytic contact-flux attempt using local logarithmic coefficients and actual theta information. No generic support/rank search, new zero-free bound, deformed zero-sum interchange, full invariant-cone theorem or all-degree sign import is approved.
COVERED_TARGET: Test whether the actual theta heat equation supplies c^T H_d'(lambda_*)c<=0 at each finite positive-parameter contact H_d(lambda_*)>=0, H_d(lambda_*)c=0, for H_d built from the logarithmic coefficients of Xi_lambda, without assuming higher-degree positivity.

## Completed review: 6 November 2026

The main gap is the actual-Xi all-degree mixed positivity in
L030-L032/C032a. The intermediate target is exactly the TARGET above.
A usable contact sign could be an input to decreasing-parameter
positivity continuation; it would still leave the continuation theorem,
initialization, equality cases and passage through all degrees open.
No such theorem or sign is established today.

### Primary inputs, hypotheses and comparison

**Heat zeros, including multiplicities.** D. H. J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn-Newman constant*,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
Proposition 3.1(i)-(ii), equations (28)-(33): read the complete proof.
Its actual H_t, any real t_0, and enumeration paired by z_-k=-z_k
permit complex zeros. The simple-zero case uses implicit continuation,
the heat PDE, and a locally convergent paired Hadamard logarithmic
derivative. The repeated-zero case retains the Hermite rescaling,
O(|t-t_0|) displacement error and Rouche local zero count for every
finite multiplicity m>=2. Thus multiple zeros cannot be silently
handled by the simple-root ODE. Neither case is a finite-Hankel flux
inequality. This is scope comparison; no deformed reciprocal sum or
new growth estimate is imported. In particular, no source-to-notebook
time rescaling is needed for the approved local-coefficient calculation:
L058 supplies its own exact normalization.

Rodgers-Tao, *The de Bruijn-Newman constant is non-negative*,
[arXiv:1801.05914v5](https://arxiv.org/html/1801.05914),
3 July 2021, introduction (1)-(4), Theorem 1, Section 4/Theorem 4.16
and its cited proof: read those passages. The theorem is Lambda>=0,
not Lambda<=0. The displayed zero ODE is in Lambda<t<=0, inside the
assumed real-simple regime used in the contradiction argument; it is
not an unconditional estimate at arbitrary positive-parameter matrix
contacts. The subsequent formal energy discussion expressly warns
about divergent infinite sums and requires truncation. No energy sign
or untruncated identity is imported here. Its citation to
Csordas-Smith-Varga is a lead; that older PDF was inaccessible in this
turn, and is not counted as independently inspected. Polymath's
complete simple/repeated proof supplies the essential comparison.

**Logarithmic heat transform.** Tao, *Heat flow and zeroes of
polynomials*, [17 October 2017](https://terrytao.wordpress.com/2017/10/17/heat-flow-and-zeroes-of-polynomials/),
read through Exercise 3. Equation (2) uses forward heat, opposite to
L058's lambda direction. The simple-root discussion excludes repeated
roots; its quadratic example exhibits collision. Exercise 3 identifies
the logarithmic derivative/Stieltjes transform with a viscous Burgers
equation, pointing to the Cole-Hopf transformation. This is a known
tool, not the desired logarithmic-coefficient Hankel sign. The future
attempt must fix signs using L058 and retain the normalization at zero.
No coefficient evolution is derived or cited as already proved here.
The sign sought is the one in the unchanged TARGET for decreasing
lambda; forward preservation must not be substituted for it.

**Hankel evolution with a different parameter.** Deng-Yang-Lu,
*Contour Hankel dynamics and indicator fields for the Riemann
Xi-function*, [arXiv:2608.11520v1](https://arxiv.org/html/2608.11520),
12 August 2026, Proposition 4.1 and Theorem 4.2, (37)-(43), complete
proofs read. On crossing-free moving contours the enclosed zeros of
fixed Xi stay fixed; a C^1 center and positive C^1 radius give affine
coordinate motion and a finite congruence evolution. The theorem
preserves inertia between crossings when real symmetric. Its parameter
is not the theta heat time; its finite contour moments are not the
infinite reciprocal coefficients here. Applying its congruence law to
H_d(lambda) would require an additional result not in that theorem.
This exact scope mismatch rules out an automatic import, not the
proposed actual-theta test. The manuscript's introduction also states
its independent positivity requirement remains unresolved.

**Boundary conditions versus invariance.** Hamilton,
*Four-manifolds with positive curvature operator*, J. Differential
Geometry 24 (1986), 153-179,
[primary paper scan](https://scispace.com/pdf/four-manifolds-with-positive-curvature-operator-3nfj6l2gwc.pdf),
Lemma 4.1/Theorems 4.2-4.3, pp160-163. Read hypotheses and proof text:
the ODE requires a smooth field on an open state neighborhood and
tangency at every boundary point of a closed convex set. The proof
localizes with a cutoff, compares distance at nearest boundary points,
and uses a derivative bound near the set. The PDE statements additionally
use compact base, convex fibers and parallel-transport invariance.
OCR omits some displayed formulas; no formula from that scan is used
as a mathematical input. Publisher access was blocked and two page
image requests returned429; these do not block the comparison.

For an independently readable precise statement, Horvath-Song-Terlaky,
*Invariance Conditions for Nonlinear Dynamical Systems*,
[arXiv:1607.01107v1](https://arxiv.org/html/1607.01107),
5 July 2016, Theorem 2.4, (3), states Nagumo's criterion for a closed
convex set, continuous autonomous field and unique solutions from each
point in the set, with tangency at every boundary point. Its original
Nagumo reference is not independently read. Neither source turns a
non-strict contact test along one given analytic trajectory into a
preservation theorem without further hypotheses. No finite closed
evolution for H_d has yet been supplied. The future attempt must expose
rather than silently close that issue. No matrix maximum principle is
imported as an established step toward RH.

### Local duplicates and recorded failures

Read L024/L025/L030/L032/C032a completely: they establish the exact
zero-time normalization, algebraic-square form and all-degree
equivalence, with no sign import. L058 was read in full and already
provides joint analyticity, compact mixed-derivative domination and
strict positivity at zero. Its polynomial warning tests only the PDE
and local-zero inference, not the exact theta class. The contact
calculation can use these established local analytic facts without
reproving them or assuming a global logarithm.

Read L057 completely: any fixed finite set of its Hankel tests may
pass while the specified non-theta family has nonreal zeros. It gives
no uniform degree cutoff and does not settle actual-theta contact
flux. This remains a necessary qualification on downstream use, not
a reason to reject every intermediate finite-degree lemma.

Reuse `2026-11-06-actual-xi-signed-integral-discovery.md` and
`2026-11-06-three-atom-heat-minor-boundary-flux.md`: the primary Shi
Hexagon2610.00521v1 statements/proofs were already assessed there.
Their factorial-normalized coefficient evolution and alternating
row-derivative formula do not sign cofactors. This is reused coverage,
not a fresh source audit, and the Hexagon identifier is not an arXiv ID.
Read L843's hypotheses/conclusion and its recorded audited stop in
`ATTEMPTS/2026-11-06-three-atom-boundary-flux-no-boundary.md`:
on the fixed positive {0,1,4} law its coefficient Toeplitz determinant
is strictly positive, so the searched boundary does not exist. No
larger support/rank search or universal heat conclusion follows.
The proposed logarithmic reciprocal form is a different observable;
that distinction alone proves neither novelty nor feasibility.

L617's conditional cusp statement/source scope was read only for
contrast, not re-audited or used as an input. The November 1 collision
flux assessment separately parks a singular spatial-potential
compensator. No such potential, moving hole or singular-current
product is part of this local logarithmic-coefficient target.
L872/L873's spectral trace route stays parked; no trace repair,
cross-notebook theorem or sibling proof was used.

### Search record and bounded decision

Queries included `"de Bruijn Newman" "Hankel" moments heat`,
`"Hankel" "logarithmic" "Riemann" zeros heat equation`,
`Hankel moment matrix heat equation positivity boundary null vector
logarithmic derivative`, `"Hankel" "heat" "reciprocal"`,
`"Riemann" "Hankel" "heat" logarithmic coefficients`,
`"Hankel" "Cole-Hopf" zeros positivity`, and
`"Hankel" "logarithmic coefficients" "heat"`.
Stronger-result searches covered Rodgers-Tao zero dynamics and
Nagumo/semidefinite-cone and Hamilton null-eigenvector conditions.
Most Hankel/heat hits concerned Hankel transforms or unrelated source
reconstruction, and were not treated as theorem evidence. No exact
source match was found in the inspected results; no novelty is inferred.
No current zero-free region, reciprocal-series continuation or parked
arithmetic estimate is proposed, so the October baseline is not being
reopened.

Decision: EXPLORE only the unchanged TARGET after the separate approval
of this newly completed review. In one attempt, obtain the exact
null-vector contraction for a fixed but arbitrary d, keeping every
normalization and any coefficient outside H_d explicit, then seek a
sign from the actual theta representation under exactly the stated
finite contact premises. This is the bounded test, not a derived
identity or an assumed invariant hierarchy. The potentially creative
part is an independent actual-theta sign mechanism, not the known
logarithmic differentiation.

Continue only if the resulting expression has a rigorously justified
nonpositive sign from those premises and independently established
theta information, or identifies a specific new independently testable
theta estimate. End the attempt with an explicit obstruction if it
needs unproved higher-degree positivity, a real divisor, an unproved
tail estimate or a new generic model search. Retain incomplete
reasoning rather than broaden the target. Failure to obtain a sign is
not an actual-family counterexample. Even a favorable sign leaves
contact existence, non-strict equality/tangency, initialization,
continuation, unbounded-degree escape and endpoint positivity open.
Mathlib coverage of the full contact statement is not checked; no
absence claim or matching formal theorem is recorded.

## Proposed bounded question, not a derived identity

Use L058's exact theta family Xi_lambda with Xi_lambda(0)>0 and
partial_lambda Xi_lambda=-partial_z^2 Xi_lambda. Define the proposed
coefficient notation near z=0 by

    S_k(lambda) = -k [z^(2k)] log(Xi_lambda(z)/Xi_lambda(0)),
    H_d(lambda) = (S_(i+j+2)(lambda))_(0<=i,j<=d).

Here d is any fixed finite nonnegative integer, lambda_*>0, and
c is a fixed nonzero real vector of length d+1. The requested
inequality is a conditional boundary test, with positive
semidefiniteness only of this finite matrix at this parameter.
The sign sought is for decreasing lambda toward zero. Source review
must check that direction and what it can actually imply; no
first-contact theorem or preservation result is assumed.

At lambda=0, the intended interpretation is L024/L025/L030's
reciprocal-power form. The identification and any extension to
deformed zero sums must be justified, not inferred from the heat
PDE. Using local logarithmic coefficients is a proposed way to avoid
premature interchange of deformed infinite zero sums, not a claim
that all needed analytic or sign obligations have been met.

Essential continuation inputs are L018, L024, L025, L030-L032/C032a
and L058. L617 is an unaudited conditional warning, not a positivity
input. No cross-notebook result is proposed. The original actual
theta kernel and normalization must be retained: a generic
backward-heat positivity principle is already unsupported by L058's
explicit polynomial diagnostic. Compare
`drafts/literature/2026-11-06-three-atom-heat-minor-boundary-flux.md`
before treating this as distinct from the prior coefficient-minor
heat work; only its target/metadata surfaced in the nomination check.

## Original nomination requirements (historical; completed above)

Check exact known results, stronger statements and recorded failures
for reciprocal-power Hankel evolution, logarithmic heat/Riccati
identities and finite-dimensional semidefinite boundary tests.
Retrieve primary hypotheses and essential proof cases; do not derive
the new evolution or approve it by a fresh computation in that
literature-only turn. Unknown Mathlib coverage remains unknown.

A useful positive comparison would support one bounded calculation
of this null-vector flux using actual theta information. A known
counterexample, exact overlap or structural insufficiency should
change the target rather than launch a generic heat-positivity
reproof. A failed search alone does not establish novelty.

Even a favorable contact sign would leave initialization, non-strict
tangency/equality cases, degree-uniform continuation, possible escape
to unbounded degree, and the passage to all-degree positivity at
lambda=0 unresolved. These are not assumed in the proposed test.
The downstream purpose is directly L030-L032/C032a's sign gap,
rather than the period/graph bridge needed by the parked route.

This is a nomination for possible proof_attempt/creative only after
adequate coverage demonstrates a genuinely different actual-theta
mechanism. The critical claim would be the null-vector flux sign;
the bounded discriminant is its exact signed expression with all
uncontrolled terms exposed. It is not a creative invocation now:
the source gate and duplicate screen are essential and incomplete.
