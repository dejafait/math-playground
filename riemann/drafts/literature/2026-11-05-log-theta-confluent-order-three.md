# Logarithmic theta kernel: proposed finite confluent-minor review

TARGET: Assess known results and obstructions for the signed confluent order-three translation minor of H(v)=e^v K(e^v)/m_0, and specify one bounded actual-kernel test without assuming variation-diminishing sign transfer.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step610 completed bounded exact/log-dilation/PF3/confluent-minor searches and inspected the primary passages below; reused step502's direction assessment and local theta stops. No matching actual-H sign theorem was located; no originality inference.
SOURCE_EVIDENCE: Simon 1305.1173v1 Section3 equation(7)/finite-difference proof pp.6–7 and Section4 opening p.14; Nuttall author det3CAEXP_2.pdf Lemma2.1/full proof and Theorem2.2 p.4; Csordas 1309.0055v2 (4.2), Theorems4.1/4.2/4.5 pp.10–11; Michalowski 2602.20313v2 (2)–(5), Theorems1.1/1.2, Proposition2.2 pp.2–4 and complete Section5.1 pp.7–8. Primary links/read qualifications below.
COMPARISON: Smooth-kernel confluence supplies a necessary sign test. Inspected theta statements concern Phi(x+y), an even Phi translation kernel or Phi(sqrt(t)), not the proposed second-logarithmic H condition. Compact positive data do not give global TN3, lower oscillation or Xi signs.
GAP: Actual mixed-partial signs, justified derivative tails through order four and implementation normalization remain for research; global translation minors, signed integral interface and all-degree transfer remain independent gaps.
REASON: Source coverage now specifies one bounded actual-H test with a negative threshold and honest positive/inconclusive outcomes; this is preparation, not a sign result or mathematical advance.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target lacked primary confluence coverage and a precise test; step502 did not cover these hypotheses.
SCOPE: Completed source review only. The separate 2026-11-05-log-theta-confluent-compact-test.md scopes the proposed calculation, subject to separate supervisor approval; no derivative identity, H evaluation or sign-transfer theorem was derived here.

## Proposed purpose and boundaries

The main gap is actual-Xi all-degree mixed positivity. The intermediate
question is whether one finite confluent translation minor of the actual
logarithmic theta dilation kernel provides a usable theta-specific property
beyond positivity of an abstract moment measure. Such a property could
inform a later signed mechanism; it would leave the missing lower
oscillation, integral interface and all-degree transfer unresolved.
A counterexample could instead eliminate this specific finite-order
hypothesis. Neither result is asserted here.

Start from the narrow definitions of K and m_0 in L019/L021 and the
normalizations in L795, only as needed. Compare the exact relevant
source ranges and the stop
`ATTEMPTS/2026-11-05-theta-log-variation-automatic-sign-source-stop.md`.
The already checked upper-bound direction of variation diminution is not
a new completion mechanism. Reuse that comparison, rather than browsing
it again to renew a gate. The present question addresses one unverified
finite actual-kernel hypothesis, not the previously stopped automatic
transfer. The generic/admissible-kernel stop L738 is also a contrast,
not an actual-H sign premise. L820 and its two-unit-gap cap are a retained
comparison-model stop, not mathematical inputs to a theta minor.

Retrieve primary differential/confluent total-positivity hypotheses and
essential proof cases before proposing any specialization. Establish
exact sign conventions and distinguish a local necessary condition from
a sufficient global translation-kernel condition. Check existing finite
theta positivity results for the exact coordinate and kernel: ordinary
theta, logarithmic dilation, inverse-Xi densities and coefficient
sequences must not be conflated. Examine relevant recorded failures
before selecting any parameter domain or asymptotic mechanism.

Continue only if the review supplies adequate coverage and a precise,
nonduplicate, bounded test with a rigorously stated acceptance threshold.
If a known theorem covers the exact statement, import it. If the test
merely assumes target-equivalent positivity or repeats the stopped
upper-bound sign transfer, abandon this nomination and record why.
Do not infer originality from unsuccessful searches. Missing source
coverage blocks dependent mathematics, not the completed L820 audit.

A genuinely new central signed mechanism is not yet formulated. A later
proof_attempt/creative nomination requires a specific bounded test,
independent source readiness and an escalation explaining its relation
to mixed positivity. This pending source review is literature_comparison,
not such a creative attempt. No cross-notebook theorem is proposed.

## Completed source review — step610

Main gap: actual-Xi all-degree mixed positivity. The intermediate
target is only a finite necessary translation-minor condition for the
actual logarithmic scale law. It could exclude one theta-specific
hypothesis, or retain a compact local property for a later signed
mechanism; that mechanism remains missing. No mathematical calculation
or new identity was performed during this source review.

### Primary confluence coverage

Thomas Simon, *Total positivity of a Cauchy kernel*,
[arXiv:1305.1173v1, 6 May 2013](https://arxiv.org/pdf/1305.1173v1),
Section3, printed pp.6–7, defines the mixed derivative determinant
Delta_r=det[partial_x^(i-1) partial_y^(j-1) k(x,y)]. Equation(7)
identifies it with the ordered collocation determinant divided by
both positive Vandermonde products and multiplied by sf(r-1)^2.
The full argument uses repeated forward differences for a smooth real
function and row/column operations; its negative-limit case excludes
total nonnegativity. Although the displayed kernel is Cauchy's, the
finite-difference argument uses smoothness, not its rational formula.
Its applicability to T below must be justified in the research turn.
No new general theorem or reproof is proposed.

Section4 opening, p.14, invokes Karlin's strict ETP criterion
(Vol.I, Theorem2.2.6) requiring every smaller differential determinant
strictly positive throughout the rectangle. The monograph is unread
here; neither that sufficiency application nor the Cauchy-specific
parameter estimates are needed for the proposed necessary test.

Define the proposed observable, without evaluating or expanding it:

    T(x,y)=H(x-y),
    Q_3(v)=det[(partial_x^i partial_y^j T)(v,0)]_(i,j=0)^2 / H(v)^3.

Both collocation tuples increase. This mixed-partial convention fixes
the translation orientation; no unsigned derivative-Hankel determinant
is silently substituted. L019/L021 give H(v)>0 for finite real v.
Expansion into ordinary derivatives, cancellation of m_0 and the
derivative bounds through total order four remain research checks.

### Theta scope and known failures

John Nuttall, *Wronskians, Cumulants, and the Riemann Hypothesis*,
[16-page author copy](https://publish.uwo.ca/~jnuttall/det3CAEXP_2.pdf),
Lemma2.1/full short proof, printed p.4, assumes psi analytic near
(0,infinity), k(x,y)=psi(x+y), and epsilon_p w_p(t)>0 for every
t>=0 and p<=r, with epsilon_p=(-1)^(p(p-1)/2); it invokes Karlin's
differentiability/compound-kernel criterion. Theorem2.2 treats
Phi(x+y) as RR3: W1>0 and W2,W3<0. Its W2 proof uses an earlier
concavity inequality and Phi''(0)<0; W3 is deferred to Theorem3.5.
No new Section3 audit is claimed: step463's comparison is reused.
This is not a theorem for H(x-y), nor an invariance assertion under
an arbitrary nonlinear change of difference coordinate. L786's
coefficient theorem and L795's average concern different observables.

George Csordas,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
(4.2)/Theorem4.1, printed p.10, specify Phi's series, analyticity,
evenness, positivity, derivative tails and monotone decay. Theorems
4.2/4.5, p.11, concern square-root/original-coordinate log-concavity
and admissibility of associated kernels. Statements were inspected
for scope only; their cited concavity proofs were not newly inspected
or imported. They do not state the H minor inequality. This source's
Fourier transform named H is different from the proposed H here.

Wojciech Michalowski,
[arXiv:2602.20313v2, 20 July 2026](https://arxiv.org/pdf/2602.20313v2),
(2)–(5), Theorems1.1/1.2 and Proposition2.2 distinguish the even
de Bruijn–Newman kernel, a negative order-five Toeplitz witness and
smaller positive determinants at one configuration. These are not
global PF3/PF4 proofs or statements about e^v K(e^v). Complete
Section5.1 withdraws v1's derivative-based global threshold: required
derivative orders were not covered, an inserted flat tail bound was
false, and grid signs did not cover intervals. No certificate,
threshold or program from that source is adopted. Every derivative
used later needs its own justified tail bound; unresolved cells must
remain unresolved. This is source-failure coverage, not a new H result.

Reuse step502's ready review and automatic-sign stop unchanged.
L738 is a generic shape/sign countermodel, not an actual-H premise.
L820's comparison-model cap is retained and has no mathematical role
in this test. Narrow searches of the dated theta assessments/stops
located no duplicate actual-H confluent evaluation; no originality
is inferred.

### Bounded test, search record and decision

Propose only e^v in [1/4,2]. This is a chosen compact test domain,
not a source-given sufficient domain or a tail-reduction theorem.
Seek a rigorous negative point enclosure of Q_3, or a complete
nonnegative cover, stopping after 2048 terminal subintervals with all
unresolved cells retained. A negative point rejects the necessary TN3
hypothesis; a positive cover retains only this compact confluent
condition. Neither gives global minors, lower oscillation, L795's
unbounded-input interface or Xi signs. Exact supporting work and
acceptance thresholds are in the separate test assessment.

Queries included `total positivity smooth kernel confluent determinant
derivatives criterion extended total positivity Wronskian`,
`translation Hankel derivatives total positivity kernel`, `Riemann
theta logarithmic total positivity`, `theta logarithmic PF3`,
`theta H(v) total positivity`, `logarithmic theta kernel confluent`,
`e^v K(e^v) theta`, and `theta logarithmic dilation positivity`.
Primary passages above, not snippets, ground the comparison.

[rStation Paper95 v1](https://rstation.ai/problems/riemann_hypothesis/papers/95),
Section5 scope passage, identified Michalowski as a lead; no BPY or
reciprocity theorem was imported. The named even-kernel PF4 lead at
`https://kenan.works/posts/debruijn-newman-stops-at-four/` returned
HTTP502 and remains unread. It concerns a different kernel and is
not essential to this necessary local test. Karlin's unread global
sufficiency theorem is likewise unnecessary; no essential source
blocker is concealed by these scope exclusions.

Outcome EXPLORATION: source coverage and a precise test are prepared,
but no actual-H sign is proved. Mathematical exploration usage is
zero; no scheduler/counter reset is claimed. Confluence coverage now
exists, but an independent lower-sign bridge remains missing, so no
creative central mechanism is nominated. The next calculation is not
labeled creative. Full matching Mathlib coverage is unchecked. No
lemma, mathematical script, DAG or assembly argument was changed.
