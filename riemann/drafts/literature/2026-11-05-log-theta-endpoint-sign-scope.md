# Logarithmic theta endpoint signs — new source-review target

TARGET: Assess source coverage and recorded failures for determining the leading nonzero asymptotic sign of L821's normalized Q_3(v) as v tends to each real endpoint, with derivative-controlled actual-theta remainders.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step632 searched exact second-logarithmic/theta/confluent endpoint statements and stronger Wronskian results, checked step610/614 coverage and the named stops; no inspected theorem gives this exact Q_3 endpoint sign. Queries and inspected versus unread sources below; no novelty inference.
SOURCE_EVIDENCE: Csordas 1309.0055v2 (4.2), Theorem4.1(i)–(v), printed p10 and its proof attribution; DLMF20.2.3/20.2(ii), 20.7.32 and 2.1(ii); Nuttall det3CAEXP_2.pdf Theorem2.2/proof p4 as coordinate comparison; reusable Simon1305.1173v1 Section3(7) pp6–7. Complete local L016/L019/L021 and relevant L821 proof/audit read.
COMPARISON: Known theta analyticity, parity and qualitative differentiated decay support endpoint analysis, but do not supply the leading nonzero sign after the nonlinear Q_3 cancellations or relative differentiated errors. Nuttall's RR3 is in the original sum coordinate; L821's certified constants are compact only.
GAP: Specialize established theta series and L821 identities to each endpoint, retaining every derivative through order four and proving a final Q_3 error smaller than its first nonzero term; no coefficient, sign or endpoint theorem was derived in step632.
REASON: Essential source comparison now supports one bounded endpoint specialization, separately scoped for approval; full sign calculation remains research. Additional source retrieval is not needed for the specified local-series method.
LITERATURE_REASON: The invocation-start endpoint target was REVIEW_REQUIRED; compact confluence coverage did not cover either endpoint or differentiated asymptotic errors.
SCOPE: Completed literature-only review of the two endpoints of the existing Q_3; no mathematical calculation, new lemma, script, global TN3 inference, all-degree sign theorem or Xi transfer. The separate endpoint-test assessment nominates future mathematics and awaits separate approval.

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is whether L821's necessary translation-minor condition survives at both
ends of the actual logarithmic scale law. Its plausible downstream use is
to decide whether a global translation-kernel mechanism remains admissible;
even a positive answer would leave nonconfluent signs, lower oscillation,
the unbounded Laguerre integral interface and all-degree transfer open.

Use exactly H(v)=e^v K(e^v)/m_0 and L821's increasing-tuple convention,
Q_3=det[partial_x^i partial_y^j H(x-y)]_(i,j=0)^2/H(v)^3 at (v,0).
L821's already established logarithmic-derivative identity may be reused
after its complete relevant proof is read. The compact certificate is not
an endpoint estimate. No numerical evaluator or fitted moments are needed
unless a later, separately approved test explicitly justifies them.

First search the exact logarithmic-theta/translation-minor and endpoint
statements, including stronger known results. Reuse step610's coordinate
and confluence comparisons; read primary theorem hypotheses and essential
proof cases for any claimed asymptotic import. Inspect only necessary
L016/L019/L021 and L821 proof passages, with the step614 audited contract.
Check the named local stops before proposing a specialization. No
cross-notebook input is proposed; matching Mathlib coverage is unchecked.

The discriminating prospective test is the leading nonzero sign at each
endpoint with a remainder strictly dominated by its leading term, or an
exact identity if all candidate terms cancel. A rigorously negative
endpoint sign would exclude global TN3 for this translation kernel.
Positive leading signs would support only eventual positivity at the ends,
not global positivity or Xi signs. Uncontrolled differentiated remainders
or unresolved cancellation are inconclusive. The review should specify a
bounded calculation target or park the target if only the already stopped
upper-bound oscillation transfer is offered. No formulas, asymptotic
coefficients, signs or new mathematical claims are approved in step631.

Compared mechanisms: common-symbol lowering is obstructed by audited L825;
automatic Laguerre-adjoint closure lacks a paid forcing/boundary margin;
the selected endpoint test addresses the actual logarithmic kernel and
does not need either premise. This is preparation of a distinct analytic
test, not a creative proof attempt. A central creative route remains
blocked by the missing independent lower-oscillation/sign-transfer
mechanism; no route is relabelled creative to meet a scheduling target.

## Completed endpoint source comparison — step632

Outcome EXPLORATION. This review prepares a test; it establishes no
endpoint sign and no mathematical advance beyond the checked sources.
The preceding nomination records what was unreviewed in step631. The
following comparison replaces that source status, not its mathematical
qualifications. The calculation is specified separately in
`2026-11-05-log-theta-endpoint-sign-test.md` in this directory.

### Exact definitions and reusable evidence

Read L016/L019/L021 completely and L821's complete relevant proof,
including its independently audited differentiated tails. Use its
identities (1)–(5), including the increasing-tuple sign. Its constants
(6)–(7) are proved only on 1/4<=u<=2; they are not endpoint estimates.
Reusing a polynomial recurrence does not extend those numerical bounds.
No certificate needs replay in a source-review turn.

Step610's Simon confluence assessment remains adequate, unchanged.
Nuttall's original-coordinate RR3 and Csordas's ordinary-coordinate
concavity remain different assertions. Existing L047 was inspected as
a possible duplicate curvature input: it states a second-derivative
log-concavity bound, not this fourth-jet nonlinear endpoint observable.
It is not a premise of the proposed test; no audit of it was undertaken.

The common-symbol stop, automatic-adjoint stop and automatic
variation-sign stop were read. The first is a finite compatibility
failure; the latter two retain unpaid signed forcing or lower
oscillation/interface premises. Neither excludes an actual-H endpoint
calculation. Conversely endpoint positivity would pay none of them.
The prior full-first-summand review, step393, already compares retaining
the complete n=1 term. That method is known; applying it here is not a
new mechanism. Its smoothed original-coordinate determinant is not Q_3.

### Inspected primary statements and their limits

George Csordas, *Fourier Transforms of Positive Definite Kernels and
the Riemann xi-Function*,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
(4.2), Theorem4.1 and its complete proof-attribution paragraph, printed
p10: for the displayed actual Phi series, (i) positivity on t>=0,
(ii) analyticity in |Im z|<pi/8, (iii) evenness and vanishing odd
derivatives at zero, (iv) differentiated decay after multiplication
by exp((pi-epsilon)exp(4t)) for every epsilon>0, and (v) strict
decrease for t>0. The paragraph attributes (i)–(iv) to Polya and (v)
to Wintner/Spira; it does not reproduce their proofs. The source
coordinate relation K(u)=4Phi(u/2) is the already recorded step393
comparison and must be carried explicitly if any statement is used.
The source's Fourier transform named H is not this notebook's H.

These statements cover regularity, parity and qualitative derivative
decay. In particular (iv) does not state an error relative to the
full n=1 contribution, or the size of the error after Q_3 cancellation.
Neither monotonicity nor analyticity asserts nonvanishing of a
particular endpoint coefficient. No such implication is imported.

The cited originating paper, Csordas–Norfolk–Varga, *The Riemann
Hypothesis and the Turan inequalities*, Trans.AMS296 (1986),521–541,
[author PDF](https://www.math.kent.edu/~varga/pub/paper_157.pdf), was
located but not read: web extraction returned zero readable lines,
screenshots supplied no inspectable image, and local retrieval failed
DNS resolution. No originating proof is claimed inspected. This is
not an essential blocker: the proposed quantitative test uses the
existing proved L016 series/modular identity and L821 recurrence,
not an uninspected bound or the Turan theorem. Csordas's numbered
synopsis is inspected source comparison, not a new audit of its citations.

NIST DLMF, online sections retrieved 2026-11-05 (release identifier
not inspected), [20.2.3 and 20.2(ii)](https://dlmf.nist.gov/20.2),
state the theta3 Fourier series and analyticity in tau for Im tau>0
(equivalently |q|<1 for the nome). The entire-in-z statement has
fixed tau and does not justify differentiation in this problem's
varying tau. [20.7.32](https://dlmf.nist.gov/20.7.E32), with
tau'=-1/tau and principal square roots, is the standard modular
identity already instantiated and proved by Poisson summation in
L016. No new modular theorem is needed. These statements give no
Q_3 sign. Exact substitutions, positivity of logarithm denominators
and differentiated Taylor errors remain research obligations.

[DLMF2.1(ii)](https://dlmf.nist.gov/2.1#ii) explicitly separates
integration from differentiation of asymptotic estimates. Its Ritt
example assumes analyticity and an O(z^nu) bound in a sector at
infinity, and concludes the derivative bound in a strictly interior
closed sector; it also treats little-o. Those sector hypotheses are
not established here and that theorem is not invoked. The proposed
test instead bounds each differentiated remainder directly from
the theta series, or from a justified local analytic Taylor series.
An undifferentiated asymptotic cannot simply be differentiated four
times. No new general differentiation theorem is proposed.

John Nuttall, *Wronskians, Cumulants, and the Riemann Hypothesis*,
[16-page author copy](https://publish.uwo.ca/~jnuttall/det3CAEXP_2.pdf),
Lemma2.1 and Theorem2.2/proof, printed p4, use psi(x+y), analytic
near the nonnegative real axis, and signed ordinary-derivative
Wronskians at t=x+y>=0. The proof treats W1, W2 and delegates W3
to Theorem3.5. Step610's fuller scope comparison is reused. No
Theorem3.5 re-audit or sufficiency import is made. Nonlinear change
to e^v K(e^v) is not a hypothesis in that theorem; its signs cannot
be transferred without a new argument. This is overlap comparison,
not a theorem import settling the endpoint target.

### Bounded search and disposition

Queries included `Riemann kernel total positivity theta logarithm`,
`theta kernel asymptotic derivatives`, `Hankel theta log-concavity
Riemann`, `logarithmic theta confluent`, `e^v K(e^v) theta
determinant`, `Riemann Phi kernel Wronskian asymptotic third
determinant Nuttall`, `logarithmic theta endpoint`, `theta Q_3
determinant`, `e^v theta total positivity`, `logarithmic theta
kernel derivative`, `Riemann logarithmic Wronskian asymptotic`,
`theta u d/du total positivity`, and the originating CNV title.
Exact searches gave no inspected matching endpoint theorem; broader
searches returned the different-coordinate works above. This does
not establish novelty or completeness of the literature.

Search leads to Nuttall's cumanal_a.pdf/det3n.pdf/RHsplit.pdf were
not newly read; their snippets are not evidence for an endpoint
theorem. The previously reviewed original-coordinate material is
reused at its recorded scope only. No new PF4/PF5 or automatic
sign-transfer source is relied on. Full matching Mathlib coverage
is unchecked; L016's supporting results are not this endpoint theorem.

Decision SPECIALIZE: import established regularity only where its
precise hypotheses are met, and perform only the missing quantitative
endpoint specialization. Direct error bounds are justified work
because the checked qualitative theorems lack the required relative
precision, not because their known regularity needs rediscovery.
The proposed order-eight origin calculation and exact full-n=1
large-u comparison are a single bounded test of one observable,
not a minor grid or degree sweep. Their scope and stop rule are in
the separate test assessment. No endpoint coefficient, asymptotic
formula, sign or cancellation has been calculated in this turn.

No independently specified central lower-oscillation/sign-transfer
mechanism became source-ready. That is the blocker to a creative
nomination; this ordinary endpoint specialization is not relabelled
creative. It may eliminate a necessary hypothesis, but positive
endpoints would not be progress to an RH proof without new inputs.
