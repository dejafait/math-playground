# Actual Jacobi orbit and collision factor — completed source screen

TARGET: Assess whether L608's actual Jacobi-orbit identities can control the nonvanishing analytic factor at a finite real heat double zero, beyond the recorded curvature and reciprocal-Stein conditions, and specify one independently testable collision criterion.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the three-candidate screen below: analytic factor bounds, spatial-orbit shape transfer, and pre-Schwarzian factor diagnostics. Reused the named theta/Stein/energy assessments; exact orbit/factor/collision queries and the new Stopple primary proof comparison found no applicable independent collision criterion. This is a bounded search result, not a theorem of nonexistence or novelty.
SOURCE_EVIDENCE: Reused L608's precise imports; checked Planat–Sole arXiv:2608.19160v1 Sections 5.1–5.2 (5.1)–(5.17), Lemma 5.1/Proposition 5.3 proofs, and Section 7; Romik arXiv:1807.06130v2 Section 6 (28), Theorem 11/proof, printed pp.14–15. Newly read Stopple arXiv:1508.05870v1 pp.1–6, simple-factor lemma (6)–(8), strong-pair definition (9), Theorem 1 and its complete proof. No source-manuscript audit or new theorem application.
COMPARISON: Orbit reconstruction is spatial, not a bound on a heat transform's preparation factor. L617 already retains that factor and proves its smooth potential contribution is O(h^2); no new cancellation of the collision cusp follows. Stopple's global comparison assumes RH and consecutive simple real zeros, uses their real-zero product and real-square positivity, and concerns a lower bound for the Newman constant. Its local simple-factor identities do not supply the missing collision-valid estimate.
GAP: No independently controlled actual-theta estimate links the orbit to exclusion of the hypothetical positive-time double zero. The smooth factor is not the uncontrolled cusp term; neither a sign transfer nor a collision criterion has been established. All-degree signs, tails, zero time and other source qualifications remain open.
REASON: All three candidates fail the stated nomination test. Park this particular orbit-to-local-factor proposal; EXPLORE records completed coverage only and approves no mathematical continuation on it. The newly inspected pre-Schwarzian proof rules out a specific tempting import, rather than establishing a new mathematical obstruction.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked essential actual-orbit-to-factor coverage; the changed target required checking exact factor hypotheses and the newly located pre-Schwarzian lead. Further browsing on this unchanged proposal is not nominated.
SCOPE: Literature-only comparison; no derivation, lemma/script edit, numerical sweep, zero-free claim or audit replay. No cross-notebook input. Matching and supporting Mathlib coverage are unchecked. The original nomination below is retained as historical scope.

## Completed screen — 1 November 2026

The main gap is actual-Xi all-degree mixed signs at unbounded heights.
The intermediate target was an independently sourced actual-kernel bound
on the nonvanishing preparation factor near a hypothetical finite real
double zero at positive heat time. Its proposed downstream use was to
control L617's collision defect. The acceptance test required independent
theta data, a sufficient collision-valid bound, and one bounded
discriminator. Exactly three candidate implications were compared.

### 1. Analytic control from the exact orbit

Read L608 completely and the relevant complete preparation/factor and
potential decomposition in L617, including its recorded conceptual audit.
Read L019/L058/L059 completely for normalization and local hypotheses.
In L617 the full factor E is already holomorphic and nowhere zero on a
fixed polydisk. Its logarithm and the complete harmonic cutoff trace
contribute a real-analytic function R(t), whose symmetric difference is
O(h^2). The positive |t| term is in the root-square contribution. These
are existing canonical conclusions, not a derivation in this turn.

Consequently another finite bound on derivatives of log E is not the
missing defect estimate in that argument. No assertion that E is
constant, globally bounded, or uniformly controlled over all collisions
is justified. This candidate supplies no independent exclusion criterion;
it is parked without computing another smooth residual.

### 2. Spatial shape or positivity carried through the transform

[Planat–Sole v1](https://arxiv.org/html/2608.19160v1#S5.SS1),
19 August 2026, defines the real-nome theta trajectory for x>0 and
L=log x. Lemma 5.1 imports theta logarithmic derivatives to prove U>0;
Proposition 5.3 gives the autonomous state, and (5.12) reconstructs the
spatial kernel. Section 7 states a double-Turan coefficient consequence.
These inspected statements contain no heat-time preparation-factor bound.
The short proofs and real-coordinate definitions were checked for scope;
the full curvature theorem, elliptic inequalities and certificates were
not audited. L608 retains its upstream import qualifications.

[Romik v2](https://arxiv.org/pdf/1807.06130v2), dated 17 October 2018,
Section 6 (28), printed p.14, records the ordinary-x Jacobi equation;
Theorem 11, p.15, uses a different centered variable and constant. Its
proof is a substitution into (28), with details left to the reader.
Neither passage asserts a Fourier heat-factor estimate. These are reused
structural inputs, not newly discovered results or an audit of Jacobi's
original theorem.

The exact full orbit is stronger data than the scalar conditions in the
retained comparisons. C055a's statement proves second-level shape for
its stated small-shift family despite nonreal Fourier zeros. L607's
statement and density/hazard setup give a monotone-Stein sextic law with
a negative first form. No claim that either comparison satisfies the
actual theta orbit is made. They prevent replacing the absent transfer
by those weaker scalar premises. The earlier theta-collision and
post-L607 screens are reused, not counted as fresh evidence.

### 3. Logarithmic derivatives of the external factor

New lead: Jeffrey Stopple, *Lehmer pairs revisited*,
[arXiv:1508.05870v1](https://arxiv.org/pdf/1508.05870v1), 24 August 2015,
printed pp.1–6. Read the simple-factor lemma (6)–(8), strong-pair
condition (9), Theorem 1 and its entire proof. The lemma is local at a
simple zero and does not need RH. The global theorem assumes RH and
consecutive simple positive zeros; its proof uses their real-zero product
and a real pre-Schwarzian square. The preceding cited Newman bound is
lower, not upper. The cited Csordas–Smith–Varga proof was not inspected.

This supplies no estimate uniform through a double collision and no
application to the deformed F. Importing the global real-zero premise
would assume the missing reality input; its conclusion also has the wrong
direction for excluding positive transition time. This newly checked
hypothesis mismatch parks candidate 3, without refuting other possible
factor methods. No theorem is imported or specialized here.

### Search, decision and continuation

Queries included `"Jacobi" "theta" "Weierstrass" "de Bruijn" collision`,
`"Riemann" "heat" "nonvanishing" "factor" double zero`,
`"Second-Level Concavity of the Riemann Xi Kernel"`,
`Stopple "Lehmer pairs" pre Schwarzian strong Lehmer arxiv`,
`"Jacobi" "theta" "heat" "collision" zeros factor`,
`"Riemann" "Weierstrass factor" "heat" zeros`,
`"theta" "Fourier" "analytic factor" "Newman"`,
`"Jacobi orbit" "collision"`, and
`"Riemann" "nonvanishing" "pre-Schwarzian"`.
Search hits were leads only; unrelated orbital-dynamics hits were ignored.
No global absence claim follows from these searches. Initial batched
output was truncated; the factor passage and the complete relevant
Stopple proof were subsequently inspected in bounded ranges. No claim
rests on an unread search snippet.

None passes the independent-data/bound/discriminator test. Park this
specified factor proposal. Reopening requires a concrete new
actual-kernel-to-collision implication, not regularity, another factor
normalization, assumed simplicity or all-degree signs. The uniform-energy,
Stein, curvature and source-access stops remain at their original scopes.
There is no RH candidate and no mathematical advance beyond checked
sources. No calculation allowance is spent or reset.

The separate nomination `2026-11-01-third-derivative-entry-source-scope.md`
changes to a finite signed exponential-sum estimator. Its purpose is
only a possible whole-interval input at one positive time. It reuses
C499d's negative evidence and the capped spatial-estimator stop, not
their rejected estimators. The d>=3 proof is an explicitly unread lead
in the prior entry assessment, so this continuation is REVIEW_REQUIRED;
no third-derivative calculation or approval occurs here. A creative
central-gap invocation remains blocked by missing independent transfer
data; a finite known-method source comparison is not labeled creative.

## Original nomination (historical; superseded by the completed screen)

Use the exact L019 kernel and L058 heat convention. Assume only for
the conditional test a real double zero at (lambda_*,x_*), lambda_*>0,
F_zz(lambda_*,x_*)!=0. L059 supplies its local splitting. In the
fixed preparation neighborhood of L617, keep the entire nonvanishing
analytic factor of the monic degree-two Weierstrass factorization.
No claim about its sign, its derivatives or a global zero product is
made here. The question is whether the actual orbit of L608 supplies
new control, not whether the heat PDE alone determines it.

Essential inputs for any later approved attempt: L019/L058/L059 and
the exact imports and normalization of L608. L487/L616/L617 are
preserved contrasts. Reuse `2026-10-30-theta-collision-inequality-discovery.md`,
`2026-11-01-post-l607-xi-specific-discovery.md` and the relevant recorded
Stein/curvature failures; compare their exact hypotheses before reopening
anything. Do not read sibling notebooks. No cross-notebook theorem is
nominated. Full matching/supporting Mathlib coverage is unchecked.

The main gap is actual-Xi all-degree signs and finite positive-time
collision exclusion. A useful intermediate input would constrain the
external analytic factor by actual theta data and give a specific
defect-control use. Initial signs, uniform tails, realization, source
audits and zero time remain independent gaps. A scalar sign without
that use is insufficient.

Continue only if one of at most three source-grounded implications
specifies (a) independent actual-kernel data, (b) a stated factor bound
or collision criterion with exact hypotheses, and (c) one bounded
discriminator capable of disproving the implication. Reject implications
using only conditions already met by recorded countermodels, or which
assume simplicity/all-degree signs. If no candidate passes, park this
specific orbit-to-factor proposal; do not calculate another smooth
residual or reopen the universal rescaled energy without materially new
input. Discovery is not an approved creative attempt. Any new mathematical
target requires its own coverage and the supervisor's separate approval.
