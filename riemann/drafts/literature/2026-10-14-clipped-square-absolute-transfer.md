# Proposed scope: absolute clipped-square physical and response transfer

TARGET: Assess source coverage for transferring the negative-part-square discriminant statistic to its leading fixed-response-head model with uniform absolute dyadic error O((log H)^3+eta_N(log H)^4).
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 124 searched negative-part contraction, weighted square stability and zeta clipped moments; inspected Mathlib's primary contraction statement/proof and narrowly checked L390/L405/L406/L409, L407's head definitions and the step-99 stop. No matching completed clipped transfer was found in those records; no novelty inference is made.
SOURCE_EVIDENCE: Mathlib4 a63713524b66f0b5681eaa2bfa83e7218c5cdbe5, Topology/MetricSpace/Lipschitz.lean, LipschitzWith.max_const and lipschitzWith_max, statements and complete proofs; Bui–Hall 2304.05178v1 Theorem 3 and defining quartic asymptotic; audited L390 physical/tail estimates and L405 (2)–(7), with L406 (6)–(7) and L409 head definitions.
COMPARISON: Standard max contraction covers zero crossings without a small-value distribution premise; the inspected local pointwise errors and quartic envelope cover the intended powers. They do not state the exact combined clipped estimate, so a later family-specific product/head specialization is needed, not a new moment or contraction theorem.
GAP: Prove the exact combined absolute transfer with one constant and onset independent of N, retaining physical curvature and response derivatives. This source review does not establish the estimate or any clipped signed asymptotic.
REASON: Essential source coverage is now adequate for a bounded reproduction attempt using additional pointwise information; the step-99 signed-mean blocker and L410 scalar obstruction remain unchanged.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes from signed clipping to absolute stability; its essential contraction and uniform-envelope scope comparison was missing at startup.
SCOPE: Exact physical Delta/Bcal and L409 d_N/B0_N; ordinary jets through order two, all sufficiently large real H and every integer N>=1 with a common constant/onset; sharp dyadic absolute integral only. No signed clipping coefficient, phase symmetry, RH or growing-head twisted-moment theorem.
COVERED_TARGET: Prove the absolute clipped-square physical/head transfer with uniform dyadic error O((log H)^3+eta_N(log H)^4), using L390/L405/L406 and L409's fixed-head definitions.

The original continuation proposal followed step 123. The separate step-124
literature review below now supplies source coverage for the listed bounded
specialization. No mathematical attempt, new lemma or script was performed
in this review. The signed step-99 target remains parked.

## Precise proposed estimate and downstream use

Use L405's exact physical Delta and Bcal, L406's leading d and B0, and
L409's d_N,B0_N obtained by replacing Z=zeta(5/2+it) with its head n<=N.
Set u_-=max(-u,0), ell=log H and
eta_N=sum_(n>N) n^(-5/2), as in L390. The proposed estimate is

    H^(-1) integral_[H,2H]
      |Delta(t) (Bcal(t)_-)^2 - d_N(t) (B0_N(t)_-)^2| dt
        <= C [ell^3 + eta_N ell^4]

for every integer N>=1 and all sufficiently large real H, with C and
the onset independent of N. All ordinary jets, full physical response
derivatives and envelope curvature must remain included in the physical
error. The proposed comparison is absolute, so it must handle every
zero crossing without assuming a density bound for Bcal near zero.
No proof or assertion that this inequality holds is made here.

If covered and later proved, this would remove the physical-replacement
and response-tail obligations at the clipped quartic scale: H would tend
to infinity first at each fixed N, then N to infinity. The signed mean
of d_N (B0_N_-)^2 would still need a separate sign-sensitive mechanism.
It must not be treated as half the full square or evaluated by applying
a holomorphic contour shift to the nonholomorphic clipping function.
The point is to isolate that remaining arithmetic issue, not to reopen
the stopped five-scalar implication or claim a joint sign.

## Comparison and stopping test for the next review

Reuse the recorded L390/L405/L406 source inputs if their scope suffices;
check the standard real negative-part contraction and weighted product
stability hypotheses against the available sharp average U^2=O(ell^4).
Search the relevant local clipping/transfer records for an already proved
matching assertion. If a full match exists, import it rather than add a
duplicate lemma. If an additional unknown moment, sign distribution or
uniform-integrability premise is essential, record that gap instead of
silently assuming it. Approval requires precisely the uniform error above
or an explicitly revised threshold with a justified downstream use.

Essential inputs: L390, L405, L406 and L409's fixed-head definitions;
L410 is diagnostic contrast, not a proposed mathematical dependency.
Additional first-B moments and physical jet constraints were not copied
by its model. L394/L399/L400 and step-99 stops are preserved. Actual
clipped positivity, regulator choice, total L367 margin/remainder,
common-zero upper counts and global mixed positivity remain unresolved.
No RH, phase independence, asymptotic sign symmetry or growing-head
limit is permitted. Full matching Mathlib coverage remains not checked.

## Separate source comparison — 2026-10-14, step 124

This completes the saved source-review target only. The main gap,
intermediate threshold and downstream use are as stated above. The exact
transfer remains a future proof obligation; readiness is not verification.

### Primary contraction input

The primary formal source is Mathlib4 at commit
`a63713524b66f0b5681eaa2bfa83e7218c5cdbe5`,
[Topology/MetricSpace/Lipschitz.lean](https://github.com/leanprover-community/mathlib4/blob/a63713524b66f0b5681eaa2bfa83e7218c5cdbe5/Mathlib/Topology/MetricSpace/Lipschitz.lean),
theorems `LipschitzWith.max_const` and `lipschitzWith_max`.
The former assumes a pseudo extended metric domain, a real-valued
K-Lipschitz map and a real constant a; taking max with a preserves K.
The complete inspected proof uses `LipschitzWith.max` with the constant
map. The latter controls max on real pairs, through the absolute max
difference inequality. Applying max-with-zero to real negation, an
isometry, is the precise negative-part specialization. It requires no
differentiability or exclusion of zero crossings. Import this input;
there is no reason to reprove contraction.

Squaring the negative part is not globally Lipschitz with a fixed
constant. The later proof must use the elementary difference-of-squares
identity together with size envelopes; treating its derivative as bounded
on the whole real line would be a mistake. Product subtraction and those
envelopes are the remaining family-specific work, not a cited full match.
No clipping differentiation or holomorphic extension is authorized.

### Existing analytic coverage and necessary specialization

Reuse the already assessed Bui–Hall input,
*On the derivatives of Hardy's function Z(t)*,
[2304.05178v1, Theorem 3 and its defining quartic asymptotic](https://arxiv.org/html/2304.05178v1).
The primary statement was checked again at the defining formula and
Theorem 3. It concerns four fixed nonnegative integer derivative orders,
with leading log exponent their sum plus four and an error one log lower.
The pure cases of orders zero, one and two are within this scope.
The conversion to the actual ordinary jets and sharp nonnegative
restriction is already justified in L390's proof and separate audit;
its prior source assessment is reused, not a new source proof.

The inspected canonical evidence is:

- L390, complete leading-jet replacement (4)–(5), full-tail paragraph
  and critical-audit paragraphs on norms/tails: physical error O(U/L),
  size O(U), fourth-jet envelope with dyadic mean U^2=O(ell^4), and
  head error O(eta_N U), uniformly in N. Complete response derivatives
  and the envelope-curvature correction are included before truncation.
- L405, (2)–(7) and its audit of physical replacement: exact Bcal,
  signed leading B0, error O(sqrt(U)/L), size O(sqrt(U)) and the same
  quartic envelope, all valid at vanishing jets.
- L406, definitions and (6)–(7): compatibility of the complete physical
  quantities and errors. Its separate power-three moment is unnecessary
  for this quartic absolute target.
- L409, hypotheses, and L407's fixed-head hypotheses: d_N and B0_N
  replace only the value Z by its head. B0 is a fixed real linear
  projection of that value, with coefficients in the critical jets.
  A head-uniform envelope must be verified using the absolute right-line
  series bound; no growing-head moment theorem or signed cubic tail
  estimate needs to be imported.

This comparison finds no essential missing higher moment, relative
error, sign-density assumption or uniform-integrability theorem. It
approves trying the product specialization at the original threshold,
not asserting its conclusion. The later proof must explicitly check
each product term, head-uniform constants and the common eventual onset.
Retain the H-first/N-second interpretation for any downstream mean.

### Discovery, duplicates and failures

Queries included `positive part function Lipschitz contraction negative
part inequality`, `negative part square stability inequality weighted
integral`, `zeta clipped moment Hardy discriminant`, and `negative part
discriminant zeta moment`. Bounded results did not supply an exact
actual-family theorem. Unrelated Sobolev/spectral stability hits were
not inspected or used. The Bauschke–Combettes author-hosted `livre1.pdf`
was only a 30-page introductory extract and did not expose the needed
numbered projection theorem. It is not an imported theorem citation.
Bauschke–Chen–Wang 1211.1639v1, Section 2's nonexpansive definition and
Lemma 2.1, were inspected but concern a different fixed-point question;
they are not load-bearing here. The precise Mathlib contraction source
supplies the required input without that unavailable book passage.

Narrow local checks covered L390/L405/L406/L409 and the relevant
full-square assessment, second-moment assessment, step-99 assessment,
draft/history and exact negative-part/head searches. No completed exact
combined transfer was found in those inspected records. L405's full-square
transfer is nearby but does not state clipping; do not add a duplicate
unclipped lemma. The step-99 failure is missing signed nonpolynomial
distribution coverage, whereas this target asks only absolute stability.
L410 still prevents the selected five scalar data from determining the
joint sign. Neither historical stop is reopened by this approval.

Full matching Mathlib theorem for the actual transfer: not checked.
Supporting max contraction: present at the precise commit above.
The source comparison establishes reusable coverage, not originality.

### Continuation and abandonment test

One later RESEARCH / REPRODUCTION attempt may address only the exact
COVERED_TARGET. Import contraction and the audited fourth-jet bound;
write the necessary physical/head specialization with full hypotheses
in one canonical result if it succeeds. Do not reprove the source inputs.
Continue only if the absolute product comparison reaches the stated
ell^3+eta_N ell^4 threshold with N-independent constant and onset,
including Bcal=0 and B0_N=0. Stop and document the precise failed term
if it needs a stronger moment, a relative sign margin, or N-dependent
onset. Any changed target requires REVIEW_REQUIRED coverage.

Essential inputs are L390/L405/L406 and L409's definitions. The clipped
signed mean, regulator choice, total L367 margin/remainder, actual common
zero upper counts and global mixed positivity remain unresolved. This
step writes no lemma or mathematical script and changes no argument in
PROOF.md or DAG.md. The new ready continuation remains subject to the
supervisor's separate next-turn approval before mathematical invocation.
