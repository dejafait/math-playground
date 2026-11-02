# Quartic stationarity identity: bounded-bulk nomination

TARGET: Assess whether the quartic stationarity identity can distinguish L473's explicit bounded bulk from a stationary C2 path law, checking integrability and prior holonomic coverage.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact-identity, stationary derivative-moment and occupation-measure searches; compared L473 Section 4, L472 Section 4, L424's source interface, the Gaussian trajectory stop and selected fourth-moment records. No inspected source already decides this exact finite bulk; no novelty claim follows.
SOURCE_EVIDENCE: Lasserre--Henrion--Prieur--Trelat, arXiv:math/0703377v1, Sections 2.1--2.3, (2.7),(2.10)--(2.12), printed pp. 3--5; Henrion--Korda--Kruzik--Rios-Zertuche, 2023-03-04 manuscript, Definitions 2.4/2.7, (6)--(8), pp. 3--4, and Lemma B.1 with complete proof, pp. 17--18. Reused the existing Bernard holonomic comparison; no realization theorem imported.
COMPARISON: The standard necessary occupation identity covers a polynomial state test with retained boundaries; the unperformed difference is its stationary expectation specialization and exact evaluation on L473's uncorrected bulk. L424 instead tests a different law with a Gaussian damping and moving normalization. Covariance matching and holonomic superposition do not supply the proposed path extension.
GAP: Prove the stationary specialization with the explicit finite-fourth-moment hypothesis package below, then evaluate only the uncorrected bulk. This review does not calculate its defect or establish any incompatibility; corrected laws, all fourth constraints and actual-Hardy transfer remain open.
REASON: Essential coverage is ready for one bounded REPRODUCTION attempt using a necessary path constraint, distinct from the stopped packet family. A citation alone does not evaluate this discrete law or justify the stochastic expectation step. Separate approval of this changed assessment precedes mathematics.
LITERATURE_REASON: The nominated target was REVIEW_REQUIRED for its exact polynomial test and stochastic integrability hypotheses, outside the earlier random-phase and Gaussian-damped trajectory assessments.
SCOPE: L473 Section 4 (11)--(13), with L472 Section 4's first marginal; real Borel random C2 paths whose law is invariant under all real translations and whose three jets have finite fourth moments at zero. No rare-component, covariance-corrected-law, actual-Hardy or Xi conclusion is covered.
COVERED_TARGET: Test L473's uncorrected bounded bulk against the quartic stationary-path identity, proving the finite-fourth-moment specialization and evaluating its exact defect.

The following nomination is preserved as the pre-review record. The
completed comparison below supersedes its missing-source status; a
separate later approval is still required before mathematics.
The candidate constraint to locate and qualify is
E[F(0)^3 F''(0)+3F(0)^2 F'(0)^2]=0. It is not proved or applied
in this turn. A later mathematical test must not differentiate an
expectation using only an unexplained C2 sample-path assertion; check
local uniform domination or a suitable integrable weak formulation.
Distinguish a law of paths invariant under real translations from
finite sampling on a dyadic Hardy interval, where boundary terms can
remain. No claim about those boundary terms is made here.

Exact local input for a subsequent test is L473 Section 4 (11)--(13),
with the marginal referred to L472 Section 4. Review the latter only
as needed to establish that law; no arithmetic source extraction is
needed merely to test the uncorrected finite bulk. Reuse the existing
holonomic source comparison, including its distinction between closed
generalized measures and actual stationary C2 path laws. Check the
recorded Gaussian-jet trajectory diagnostic before declaring a new
separator. No cross-notebook input is proposed.

The main gap remains actual-Xi all-degree positivity at unbounded
height. Plausible downstream use is to identify a precise necessary
constraint on a derivative-preserving stationary replacement of the
finite moment counterlaw, rather than assume covariance matching
already supplies it. Even a failed stationary lift of this particular
bulk would not settle L473's full stationary moment-feasibility
question, actual-Hardy negative mass or RH.

Continuation test: approve a bounded later evaluation only after
locating an exact theorem or justified standard identity with its
integrability requirements and checking the local duplicates. If the
identity already decides this exact bulk in existing work, import that
decision and select another unresolved input; do not reproduce it as
new progress. If only a broader full-realization theorem is available
without the necessary hypotheses, do not invoke it. Failure to
distinguish the bulk should stop this single separator test; failure
of the bulk should identify the missing path constraint, not become
a generic stationary-process impossibility claim.

This is not labeled a creative central-gap mechanism: full-fourth
stationary realization, a derivative-preserving correction and
actual-Hardy/Xi transfer still lack a justified new construction.
Mathlib coverage of this exact application is not checked.

## Completed source review, 2026-10-31

### Inspected primary coverage

J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat,
*Nonlinear optimal control via occupation measures and LMI-relaxations*,
SIAM J. Control Optim. 47 (2008), 1643--1666,
[DOI](https://doi.org/10.1137/070685051),
[inspected arXiv PDF](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, printed pp. 3--5, (2.7),(2.10)--(2.12).
The PDF displays arXiv v1 dated 13 March 2007 and a footer date of
14 August 2016; it is not identified here with the previously inspected
January 2008 LAAS manuscript. Both LAAS URL cases failed in this turn;
the primary arXiv copy supplied the needed statement and derivation.

The setting has smooth dynamics, compact state/control sets, bounded
measurable controls and C1 tests. Equation (2.12) is the necessary
finite-interval transport identity including both terminal test values.
Read its trajectory/occupation definitions and derivation. No optimization,
no-gap or realization conclusion is used. This source supplies the
deterministic identity, not a theorem allowing unjustified differentiation
under an expectation.

D. Henrion, M. Korda, M. Kruzik and R. Rios-Zertuche,
*Occupation measure relaxations in variational problems: the role of
convexity*, [4 March 2023 primary manuscript](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
Definitions 2.4/2.7 and (6)--(8), printed pp. 3--4, and complete
Lemma B.1 proof, pp. 17--18, were inspected.
Definition 2.4 imposes finite p-moments of state and derivative and
boundary state, or compact support for p=infinity. Definition 2.7
requires nonlinear transport tests with state growth at most p and
state-gradient growth at most p-1. Lemma B.1 verifies integrability
using Holder in the finite-p case and continuity on compact support
in the bounded case. This gives integrability coverage for p=4,
not automatic stationarity, uniform integrability across heights or
realization from finitely many moments. Definition 2.7 is a necessary
constraint framework, not itself a path-existence theorem.

### Exact comparison and restricted later specialization

Reuse the inspected Bernard comparison in
`2026-10-31-stationary-hardy-path-feasibility.md`: generalized curves
and closed measures do not give a C2 path with its velocity equal to
the next prescribed jet. The unread Kurtz--Stockbridge lead is not
essential for this necessary test; no further access retry is needed.

The later attempt may take a Borel random element F of C2(R), with
the topology of local uniform convergence of derivatives through order
two, invariant in law under every real translation. Require
E(|F(0)|^4+|F'(0)|^4+|F''(0)|^4)<infinity. These are sufficient
working hypotheses, not a claim of minimality. Use the ordinary state
(F,F'), control F'', and the single polynomial test phi(x,y)=x^3 y.
There is no moving divisor or height limit in this model test.

The next proof must justify the source's compact-box use pathwise,
integrability of its boundary test and complete transport expression,
and Fubini using the finite fourth moments and translation-invariant
jet distributions. It must then justify equality of expected terminal
tests and constancy of the expected transport expression. This is the
specific unperformed specialization; do not simply write
E[d/dt]=d/dt E. If starting from finite-dimensional stationarity
instead of invariant path law, justify the induced stationarity of
derivative jets. No C3 assumption or derivative of F'' is intended.

The requested quartic identity is already stated in the nomination;
its proof and value on the law remain for the mathematical turn.
For a hypothetical extension of the bounded bulk, also verify that
the specified first marginal provides the required finite moments.
Use L473 (11)--(13) and L472 Section 4 exactly. A first-marginal
failure is enough to reject that bulk extension, but not enough to
reject the corrected total law. Its rare component retains fourth
moments and cannot be dropped from a quartic observable merely
because its probability is small.

### Duplicate checks, searches and stopping test

Read L424 through its exact source interface and transport identity,
and `ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`.
That law is L423, with a different bulk, Gaussian test, moving
normalization and unresolved exact height integral. This proposal
does not retry its failed numerical phase screen. L473 Section 7
explicitly leaves function-of-height realization unclaimed; neither
L472 nor L473 contains this stationary bulk evaluation.

A scoped literal-formula search in local lemmas, assessments, ATTEMPTS
and history found fourth-monomial tables and unrelated polynomial
expressions. Relevant ranges of L393/L400/L401/L405 and the one-height
fourth-moment assessment were checked: those record arithmetic moment
functionals, not a stationary extension decision for this twelve-state
marginal. This is a bounded duplicate check, not an originality claim.
L576--L579's already recorded wave/packet stops are contrasts only;
their parameter searches are not reopened.

Queries included `stationary differentiable process expectation derivative
zero integration by parts moments F cube second derivative`;
`stationary process E X differentiable integration by parts moments`;
`stationary third derivative fourth moment process identity`;
the Lasserre paper title and equation number; and Bernard closed-measure
terminology. Search snippets, informal stationarity tutorials and
unrelated stochastic-calculus hits were not imported. The primary
occupation sources, rather than a search failure, determine the scope.

Continue with one exact rational evaluation after the specialization is
proved. A rigorously nonzero defect rejects only this bulk as a
stationary C2 marginal. A zero defect or unavailable legitimate
hypotheses stops this single separator, without asserting realization
or generic impossibility. No larger separator search, corrected-law
calculation, endpoint estimate for Hardy sampling, or new mechanism
is approved by this assessment. The main all-degree Xi gap remains.
Mathlib coverage of the full stationary application is not checked.
