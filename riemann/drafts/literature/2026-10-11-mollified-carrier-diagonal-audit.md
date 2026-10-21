# Proposed separate audit of the sharp mollified carrier reduction

TARGET: Critically audit L396's sharp mollified carrier diagonal, including ordinary-jet signs, weighted freezing, all rational collisions and both endpoint bounds.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bounded discovery and duplicate search in 2026-10-11-mollified-fixed-head-mean.md and ready reduction coverage in 2026-10-11-mollified-carrier-diagonal.md; inspected L396 and narrowly relevant L381/L390/L391/L395 passages, step 64 history, and the L390/L394 recorded stops.
SOURCE_EVIDENCE: Directly rechecked Bourgain arXiv:1408.5794v2 Theorem 5 (0.5), printed p. 2, https://arxiv.org/pdf/1408.5794v2#page=2; Bui–Hall arXiv:2304.05178v1 mollifier definition, Proposition 1 and Section 3 (6)–(8), printed pp. 6–8, https://arxiv.org/html/2304.05178v1#S3; reused audited L391 strip/Cauchy and L395 weighted-jet applications.
COMPARISON: The existing sources cover the two analytic inputs actually used by L396; its growing finite holomorphic weight, reflected ordinary-jet algebra, complete integer collisions and sharp connector budgets remain local critical-audit obligations. BCY Lemma 4.1 and its cross-mollifier theorem are unused.
GAP: Source coverage for the exact audit is ready; mathematical verification of L396 remains pending. The diagonal limit/sign, balanced term and complete signed coefficient remain outside scope.
REASON: Separate source comparison confirms that the completed reduction can be critically audited using unchanged ready coverage; approval to audit is not approval of its conclusion.

## Proposal at invocation start (coverage completed below)

Keep N fixed, Y=H^(1/100), P(u)=u^2 and ordinary derivatives through
order two. Essential local inputs are L381 Section 4, L390's reflected
identity and physical K, L391's connector estimate, and audited L395's
weighted derivative bounds. The next source comparison should reuse the
prior ready assessment and precise direct citations; this file introduces
no changed source theorem or fresh approval.

The concrete mathematical audit should check L396 (3)'s signs and exact
Omega' term, the actual growing-weight O(1/log H) freezing error,
holomorphy of the finite product extending |P_H|^2, the reflected Cauchy
disks, the global integer separation for every nonzero frequency, and
the finite condition mn b=rs a with every multiplicity retained. The
required normalized errors are o(1), specifically the displayed logarithmic
error and powers -1959/2000 and -3907/6000. Preserve any discovered failure
without inferring the actual carrier's value from an unsuccessful bound.

The main gap is still global actual-theta mixed positivity. A usable
carrier diagonal could support a later complete signed mean calculation;
no positive witness follows before its coefficient and the balanced term
are understood. Do not add RH, simplicity, disjointness, phase independence,
growing N or carrier negligibility. Total L367 margin, eventual discriminant
sign, actual common-zero upper bounds, low-index and above-forty signs,
and endpoint arithmetic margins remain unresolved. Full matching Mathlib
coverage is not checked. The proposal was REVIEW_REQUIRED at invocation start; the separate coverage approval below now authorizes its mathematical audit.

## Separate audit coverage approval — 2026-10-11, step 65

LITERATURE / REPRODUCTION / STALLED: this is a valid coverage/process
step using existing analytic inputs, with no new mathematical evidence.
LITERATURE_REASON: The supervisor required a separate comparison of the
new audit target; reuse ready discovery and check only its essential inputs.
SCOPE: Exactly TARGET above, fixed N, Y=H^(1/100), P(u)=u^2, ordinary orders at most two, all collisions and both sharp endpoints; no coefficient evaluation or growing N.

The inspected primary [Bui–Hall v1 Proposition 1 and (6)–(8)](https://arxiv.org/html/2304.05178v1#S3)
uses the usual finite Möbius mollifier with y=T^vartheta and fixed
polynomials. Its sharp normalized second moment permits vartheta<4/7
and P(0)=0; the mollifier definition also normalizes P(1)=1.
The choices vartheta=1/100 and P(u)=u^2 match L395. Independent
complex-shift operators with Q_1=Q_2=X^j, j=0,1,2, are the scalar
inputs to its audited weighted jet bounds. Section 3 supplies the Hardy
conversion and Schwarz error case. This theorem does not itself evaluate
the present same-height carrier; no new reproof is needed.

The inspected [Bourgain v2 Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2)
is unconditional and has critical-line exponent 13/84+epsilon.
It does not assert derivative or mollified connector bounds. L391's
already audited strip interpolation, functional-equation disk extension
and Cauchy argument are the relevant local applications. Reuse those
applications with conjugate height; do not import its fixed-twist
modified-Gonek theorem for growing support.

Read L396's complete proof to identify the actual source needs, without
performing its critical mathematical verification. BCY Lemma 4.1 is an
unused alternative, so its source proof and changed cross-mollifier
coefficient need no additional browsing. No unread lead is essential to
this audit. The completed step 62 search remains adequate under the
unchanged hypotheses; no novelty claim follows from it.

L390's four-critical-factor absolute-contour failure and L394's fixed
quadratic-weight negative-definite coefficient remain preserved. Neither
is a duplicate of this two-critical-factor short-mollifier audit, nor a
global contour ban. Step 64 expressly left L396 unreviewed; no duplicate
completed audit was found in the selected records.

Approve one separate RESEARCH / REPRODUCTION critical audit under
SPECIALIZE. Check (3)'s exact ordinary signs and Omega' term; real-edge
weighted freezing using L395; holomorphy of the finite weight; reflected
Cauchy disks at both endpoints; summed top-edge convergence and integer
frequency separation over unbounded m,n; and every mn b=rs a collision.
Require all normalized errors to be o(1), including the stated logarithmic
error and the two recorded negative powers. Continue toward later signed
means only if these checks pass. If a load-bearing identity, hypothesis
or endpoint bound fails, preserve the failure and park reliance on the
reduction until repaired; do not infer the carrier's value or sign.

No derivation, lemma or mathematical script was added. Matching Mathlib
coverage remains unchecked. Global mixed positivity and the independent
sign/count gaps listed above remain open. This approval establishes
coverage for the next audit, not its correctness or an RH consequence.
