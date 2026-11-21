# One-sided degree-average bound — completed source comparison, step236

TARGET: Assess whether every-epsilon one-sided upper bounds for A_n(X_n) suffice for the L966/L968 Li criterion via positive-coefficient singularity arguments, checking known results and the prior Pringsheim records.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step236 searched Li coefficients with Cesaro/Cesàro averages, partial sums, one-sided lower bounds and Pringsheim; read review233, review207 and relevant L976 statement/audit and L980-L982 interfaces. No inspected theorem states this exact moving-cutoff implication; no novelty inference.
SOURCE_EVIDENCE: Reopened Lagarias AIF57(2007) Thm2.4/(2.20)-(2.23), pp1702-1703 and full proof; Voros arXiv1403.4558v2 (31)-(32), p10 and Section3.4 radius statement, p12; Flajolet-Sedgewick Complex Asymptotics (8May2004), ThmIV.3(i)-(ii) and full proof, printed pp15-16/PDF23-24. Reuse review233's arithmetic-split/smooth-trend and Ross coverage and review207's local analytic tools.
COMPARISON: Lagarias covers individual ordinary Li coefficients, not averages. Pringsheim supplies the generic boundary theorem, while the actual partial-sum germ and one-sided correction need a bounded specialization. L976's different translated logarithm and radius obstruction do not transfer automatically. No inspected source pays the arithmetic average bound.
GAP: Sufficiency remains unproved locally. Establish the appropriate Li partial-sum germ, surviving interior singularities with multiplicities, positive-axis regularity and a correction analytic beyond a hypothetical radius; verify the needed L982 cutoff interface. Independent arithmetic payment remains separate.
REASON: Essential generic source coverage is ready for one standard specialization test, not a new estimate or creative mechanism. This literature turn does not derive the implication. A separate continuation assessment nominates the mathematical test for approval next turn.
LITERATURE_REASON: The one-sided hypothesis lies explicitly outside review234's scope; essential comparison with one-sided Li criteria and the recorded Pringsheim mechanism is missing.
SCOPE: Actual Lambda and the complete endpoints and compensator of L981/L982; n>=2, X_n=exp(10000*(n+1)^4), A_n(X)=(n-1)^(-1)*sum_(k=2)^n P_k(X). The proposed premise is A_n(X_n)<=C_epsilon*exp(epsilon*n) for every epsilon>0 and every n>=2, with finite nonnegative C_epsilon. No lower bound, RH or zero simplicity is assumed.

## Original step235 nomination, preserved

The pending-source language in this section is historical and is
superseded by the completed comparison below.

The main gap remains actual-Xi positivity and L966/L968 signed Li
forcing. A one-sided criterion could identify a different arithmetic
threshold worth pursuing, but an equivalent criterion alone is not
RH progress. This is a source-review nomination, not an approved
creative proof attempt or a claimed new criterion.

Check the exact primary one-sided Li statements, the relevant
Pringsheim hypotheses and essential proof cases, and the notebook's
prior positive-coefficient correction before any derivation. The
named local starting points are review233, the L982 step235 application,
and drafts/literature/2026-11-10-bn-envelope-singularity-compatibility-review-207.md;
read only the exact canonical results those records identify. Do not
treat a result for the other b_m observable as automatically applicable.
The current inverse uses a subtraction and is not itself a one-sided
estimate. No uniform limit exchange or arithmetic sign is available.

Continue only if coverage isolates a valid bounded specialization or
an independently testable inequality different from two-sided inverse
recovery. Import a matching known result rather than reprove it.
If this merely restates an unpaid equivalent criterion, record that
and seek an independently payable mechanism; do not schedule a chain
of equivalent formulations. No access blocker is currently known.
Full matching Mathlib coverage is unchecked. This nomination requires
a separate literature-only turn and supplies no mathematical input.

## Completed comparison — 10 November 2026, step236

The preceding nomination describes step235, not a current source
blocker. The source task is complete; the proposed mathematical
implication is unproved. Actual-Xi positivity and L966/L968 signed
forcing remain open. The intermediate target is exactly the SCOPE
premise. Its possible use is to identify a sufficient arithmetic
upper estimate; no such estimate is supplied here.

### Primary contracts and applicability limits

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
AIF **57**(5) (2007), 1689-1740,
[Theorem2.4, pp1702-1703](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=15),
equates RH with every-epsilon exponential lower bounds for individual
ordinary coefficients, and with their absolute subexponential growth.
Its one-sided proof imports Bombieri-Lagarias; the remaining proof
uses a logarithmic-derivative germ and the functional equation.
Reuse L968's audited zeta normalization and L980's audited arithmetic
split and unconditional smooth trend, with review233's source scope.
An average is outside the individual-coefficient statement. The
coordinate-description typo recorded in review233 remains excluded;
no stopped Section6 estimate or alternating(4.13) is used. The original
Bombieri-Lagarias author PDF was located but its web text is corrupt;
no new original-proof import is made. The published theorem suffices
for the individual criterion.

André Voros, *Zeta functions over zeros of Zeta functions and an
exponential-asymptotic view of the Riemann Hypothesis*,
[arXiv1403.4558v2, 26July2014](https://arxiv.org/pdf/1403.4558v2#page=10),
(31)-(32), p10, fixes the ordinary normalization: the coefficient of
z^n in log Xi(1/(1-z)) is lambda_n/n. Section3.4, p12, states radius1
precisely under RH and a smaller radius otherwise. This Xi is a
normalized completed function of s, not real-height Xi(t). These are
inputs for a possible partial-sum singularity test, not an assertion
about the average's radius or a bound for the prime head. No saddle
expansion or simplicity assumption is imported.

P. Flajolet and R. Sedgewick, *Analytic Combinatorics — Complex
Asymptotics*, zeroth edition, 8May2004,
[TheoremIV.3, printed pp15-16/PDF23-24](https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23),
requires an analytic germ of finite positive Taylor radius R;
nonnegative Taylor coefficients force singularity at positive R.
Both proof cases were inspected: Cauchy's estimate excludes a larger
analytic disk; recentering left of R and rearranging nonnegative
terms excludes regularity at R. Signed coefficients do not suffice.
The theorem supplies neither a correction's signs nor its radius.
Import it without reproof. Reuse review207's inspected Taylor,
multiplicity and continuation tools in
[DLMF1.10(i)-(ii)](https://dlmf.nist.gov/1.10). The draft's later
heuristic singularity-composition rules are excluded.

### Local comparison and failure checks

L981 fixes full prime-power endpoints and the compensator starting
at1. L982 identifies the fixed-degree limit with S_f; its step235
application records error at most 2T/(n-1), T<=2exp(-630), between
the moving-cutoff average and the average of S_f. That application
is not separately audited: check its needed error in the proposed
test rather than treating it as audited by step231. Consecutive-mean
inversion contains subtraction; review233's Ross inverse does not
directly supply a one-sided implication.

The source-level difference is a cumulative ordinary-Li observable
instead of an individual coefficient. A test must identify its germ
by justified local power-series operations, retain degree1 and
constant terms, check whether mapped-zero singularities survive
averaging with arbitrary positive integer multiplicity, and match
the same germ along the positive real interval. Choose any
every-epsilon correction only after specifying the hypothetical
interior radius. These are obligations, not results of this turn.

Review207 led to L976. Its hypotheses, conclusion and independent
audit concern log xi(1/(2-w)), whose radius is below2 even under RH.
That radius conclusion does not automatically obstruct the different
germ based at s=1. Reuse its correction method, not its observable
or radius conclusion. The step235 automatic two-sided smoothing
stop and L983's separate lobe-sign stop remain preserved. No
cross-notebook input is used.

### Search record and decision

Queries included `Li coefficients Cesaro averages one sided lower
bound Riemann hypothesis Pringsheim`, `Li coefficients partial sums
nonnegative Riemann hypothesis criterion`, `"Li coefficients"
"partial sums" "criterion"`, and exact Cesaro/Cesàro and Pringsheim
combinations. Primary comparison used the sources above. Search
snippets and AI-written expositions are not mathematical inputs.
Xiao arXiv2006.13103 and the 2024 Ernvall-Hytönen–Odžak–Smajlović–Zubača
survey are unread leads, not matching theorem evidence. No novelty
or absence claim depends on them; generic primary contracts suffice
for this bounded specialization. No essential access blocker remains.

Continue only with the single sufficiency/singularity test nominated
in review236. Accept an implication only after its analytic and
cutoff obligations are proved; otherwise identify the failed
hypothesis. Success would still give a standard sufficient criterion,
with no arithmetic payment. Do not follow it with a chain of
equivalent criteria absent a materially different payable estimate.
The proposed conclusion is RH through the ordinary Li criterion;
it does not assert L966's separate all-index regularized Q_n signs.
No justified creative payment mechanism was found in this focused
review; this blocks creative routing, not research as a whole.

Outcome: EXPLORATION, source coverage and a bounded application
target; no new mathematical result. No lemma, mathematical script,
PROOF or DAG change. Full matching Mathlib coverage remains unknown.
