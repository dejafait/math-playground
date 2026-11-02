# Actual-Xi logarithmic-potential semiconcavity — completed source review

TARGET: Assess whether the actual theta heat family admits a local heat-time semiconcavity bound for spatial logarithmic potentials through a prospective real collision, with constants independent of the scalar regularization.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for semiconcavity, holomorphic logarithmic integrals, fiber-integral regularity and heat-zero potentials; queries and scoped duplication checks below. No applicable upper real-time estimate or independent theta condition was located; no novelty inference.
SOURCE_EVIDENCE: Yoshikawa, arXiv:math/0601426v1 (18 January 2006), Section 9, Theorem 9.1 and Lemmas 9.2–9.7 with proofs, https://arxiv.org/html/math/0601426v1 ; Polymath, arXiv:1904.12438v2, Proposition 3.1(ii) and proof, https://arxiv.org/html/1904.12438v2 . Reused Hall–Ho Proposition 4.1 and El Amrani–Jeddi's theorem/proof from the ready weak-potential assessment.
COMPARISON: Inspected logarithmic-integral regularity allows fractional-power singular terms and is stated for an additive parameter, not the nonadditive theta heat family or scalar-epsilon-uniform upper time curvature. Local heat-zero splitting covers all finite multiplicities but supplies no theta-specific sign. L616's finite cusp remains calibration only.
GAP: No independent actual-theta hypothesis implying the requested O(h^2) upper difference was found. Neither its truth for actual Xi nor its failure at an actual collision is established; locality, multiplicity and the uniform-epsilon interface remain mathematical obligations.
REASON: The stated continuation test did not identify a sufficient independent condition. Park this upper-bound proposal; nominate a separate conditional actual-family collision diagnostic using known local splitting, without assuming or proving collision exclusion.
LITERATURE_REASON: Essential missing coverage for an upper second-difference bound through zeros; the ready L616 audit assessment covers neither this bound nor actual-Xi specialization.
SCOPE: Completed literature-only comparison for the exact theta family of L058 on a compact positive-time interval and a fixed compact complex-spatial test. EXPLORE records the bounded search, not approval to attempt the parked upper bound. The distinct local diagnostic has a separate newly written assessment requiring next-turn approval.

## Exact proposed question, not a proved inequality

Use F(lambda,z)=Xi_lambda(z) from L058, with the exact K of L019
and the zero-time representation in L020. Fix a compact interval
I contained in (0,1/8), a bounded disk D about a real x_0, and a
nonnegative smooth phi compactly supported in D, equal to one near
x_0. For 0<epsilon<=1 define the proposed observable

    U_epsilon(lambda)=(1/4) integral_D
                          phi(z) log(|F(lambda,z)|^2+epsilon^2) dA.

The concrete desired source conclusion is a finite upper bound

    U_epsilon(lambda+h)+U_epsilon(lambda-h)-2U_epsilon(lambda)
        <= C h^2,

whenever the three times lie in I, uniform in epsilon. The constant
may depend on I, D, phi and independently bounded data of the actual
theta kernel. It must not use a positive lower bound for |F| on the
support, assumed zero simplicity, an assumed absence of collisions,
or an all-degree positivity criterion. This nomination does not assert
that the bound holds, is weaker than RH, or follows from smoothness of
the regularized integrand. In particular, merely computing L616's cusp
again is not the next target.

The main gap is all-degree mixed positivity for actual Xi. A bound of
this kind could potentially conflict with a collision cusp and thereby
address positive-time collision exclusion. The bridge for actual Xi,
including multiplicities greater than two and localization, must be
proved separately; the finite quartic audit does not supply it. C489a
is qualified downstream context only: its application/source audits,
infinite-zero and height-uniformity requirements are retained. No RH
conclusion or collision exclusion is imported from it here.

## Comparison obligations and discriminating test

Read primary hypotheses and relevant proof cases for parametric
logarithmic-potential regularity or semiconcavity before selecting a
mathematical target. Compare real-time upper bounds with complex-time
subharmonicity and with off-root identities; none can be substituted
for another without proof. Reuse the existing Hall–Ho and linear-current
coverage instead of reopening their unchanged statements.

Continue only if a source gives the bound with applicable hypotheses,
or identifies an exact independent theta condition and a bounded way
to test its implication. A later test must compare the symmetric
second difference with the O(h^2) threshold in one specified bounded
time/spatial neighborhood, with a constant uniform in epsilon; a
constant diverging as epsilon decreases fails the stated target.
Preserve L616 as the finite collision calibration. A theorem requiring
nonvanishing, simple real zeros, or positivity equivalent to the desired
conclusion does not pass. If no independent theta condition survives
the bounded source comparison, park this proposed bound and select a
materially different target; do not cycle through generic energy tests.

L487's bounded-comparison and the pair-energy, direct-spatial-barrier,
collective-landing and prior theta-curvature stops are contrasts, not
mathematical premises for the proposed bound. Preserve their evidence.
This nomination changes both the estimated quantity and the required
input; it does not reopen those stopped inferences under a new name.

Essential local material for the review is L058/L019/L020's actual
family, audited L616's regularization/trace distinction, and C489a's
qualified downstream statement. No cross-notebook input is proposed.
No justified creative invocation is ready until an independent theta
condition or source-supported test is identified. If one survives,
prepare a separate mathematical assessment and explain its central
obstruction and bounded test for creative routing. Full matching and
supporting Mathlib coverage for this new target are unchecked.

## Completed comparison — 1 November 2026

The preceding nomination preserves the question and its acceptance
test. This review does not derive a new inequality. The main gap is
actual-Xi all-degree positivity at unbounded heights. The intermediate
target was an epsilon-independent upper O(h^2) time difference through
a possible collision. Its hoped-for use was collision exclusion; that
use still needs an actual-family collision bridge and the qualifications
of C489a. The proposed upper bound has not passed its source test.

### Primary regularity result and relevant cases

Yoshikawa, *On the singularity of Quillen metrics*,
[arXiv:math/0601426v1](https://arxiv.org/html/math/0601426v1), Section 9:
Theorem 9.1 assumes a relatively compact domain Omega in C^n,
holomorphic G with critical locus contained in G^{-1}(0), and a smooth
compactly supported (n,n)-form chi. It places
integral log|G(z)-t|^2 chi(z) in the class B_0 defined there: smooth
terms plus finitely many |t|^{2r}(log|t|)^k times smooth coefficients,
with rational 0<r<=1 and 0<=k<=n. Inspected all relevant proofs:
resolution/localization in Lemma 9.2, the monomial reduction 9.3,
current calculation 9.4, rotational identity (9.9) in 9.5, radial
integration 9.6–9.7, and the final partition-of-unity argument.
The explicit monomial identity in 9.5 retains fractional powers;
there is no asserted upper real-direction Hessian bound or uniform
scalar-epsilon estimate. Barlet, Invent. Math. 68 (1982), Theorem 4bis,
is a cited proof input there, not an independently inspected source here.

This is a source-scope comparison, not an application of Theorem 9.1
to F(lambda,z). Its additive G(z)-t dependence does not match L058;
no parameter-dependent change of variables with controlled test and
regularization has been justified. Even its stated regularity class
is not the required semiconcavity conclusion. No compactification,
critical-value hypothesis or uniform constant for actual theta is
silently supplied. This source gives no independent theta condition.

Reused Hall–Ho's off-root identity and El Amrani–Jeddi's linear current
coverage in `2026-11-01-weak-log-potential-collision-balance.md` and
`2026-11-01-l616-collision-trace-audit.md`. The latter primary PDF's
theorem p. 2 and preparation/integrability passages pp. 4–5 were also
available during this review. Neither source states upper real-time
curvature; complex-current positivity is not such an estimate. No
general plurisubharmonic-to-semiconcavity implication is imported.

### Search and duplication checks

Queries included `"logarithmic potential" "semiconcavity" zeros
holomorphic parameter`, `"fiber integrals" "log" Barlet asymptotic
singularities`, `"de Bruijn Newman" "semiconcavity"`, `"logarithmic
integrals" "holomorphic" "parameter" regularity`, `"semiconcavity"
"holomorphic" zeros`, `"Riemann" "logarithmic potential" "heat"
curvature`, and `"Hermite" "heat equation" "logarithmic potential"
collision`. Unrelated forward-positive-heat, random-polynomial and
Riemann-surface leads were not used as matching theorems. Search
absence does not prove absence from the literature.

Read L058/L019/L020; L616's statement and its complete relevant
real-time/trace/cusp proof; C489a's qualified threshold application;
the earlier theta-collision three-family screen; the weak-event-atom
stop; and narrow curvature/potential source and working-record matches.
No duplicate actual-family, all-finite-multiplicity cusp theorem was
located in those records. L059/L060 already establish local splitting,
not a spatially integrated potential asymptotic. Their full proofs were
read for that distinction. No new audit of these results is claimed.
The bounded-energy, pair-energy and event-atom stops remain intact.

The Tokyo Yoshikawa PDF initially opened, but later page requests timed
out; the complete relevant Section 9 was then read in primary arXiv
HTML. The attempted shell download failed DNS. Demailly's detailed
book/notes remained inaccessible; they are nonessential unread leads,
not coverage. No repeated source-access loop is proposed.

### Route decision and separate continuation

No inspected source supplies the desired bound or an independently
stated theta condition implying it. Under the nomination's own test,
park that bound. This is an exploratory source outcome, not a proof
that the bound is false for the actual family and not a theorem about
RH. No new lemma, script, collision example, coefficient or limit is
derived. PROOF.md and DAG.md require no argument change.

A distinct, independently testable target is the *conditional local
collision diagnostic*: transfer the known finite-multiplicity splitting
to the unregularized spatial potential at a hypothetical actual-family
zero, and test for a strictly positive first-order symmetric difference.
This addresses an unresolved actual-family/multiplicity interface rather
than attempting another coercive upper estimate or recalculating L616's
quartic. Its use would be to determine what any proposed upper bound
would have to exclude. It would supply no independent collision exclusion.

Polymath's [Proposition 3.1(ii), equations (29)–(30) and proof](https://arxiv.org/html/1904.12438v2),
version 2, 4 August 2019, was inspected for this scope. At any repeated
H_t zero of finite order m>=2 it gives all m nearby zeros with Hermite
square-root leading locations and O(|t-t_0|) errors; the constants are
local. The proof uses Taylor rescaling, simple Hermite roots and Rouche
exhaustion, without assuming t>Lambda. It does not state a potential
asymptotic. L058/L059/L060 permit working in the notebook's own heat
normalization without reopening a global Hadamard product or importing
an unaudited global theorem. No new splitting theorem needs reproof.

The separate assessment is
`2026-11-01-actual-heat-multiple-zero-potential-diagnostic.md`.
It is newly written and must receive separate approval next turn.
Any later proof must control the nonvanishing local factor, the smooth
test away from the collision, symmetric cancellations and the order of
epsilon and time limits. Continue only with a rigorous positive
first-order lower threshold or a precise failure of that implication;
abandon if it merely repeats the quartic or assumes a theta sign.
This is standard specialization, not a justified creative mechanism:
the missing independent theta coercivity hypothesis still blocks that
nomination. Mathlib full matching/supporting coverage is unchecked.
