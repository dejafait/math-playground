# Native multiplicative reduction above 3 — proposed application review

TARGET: Test whether L048's unchanged curve satisfies IUT I Definition 3.1(b)'s multiplicative-reduction condition at every F-place above 3.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L045,L048,L049 conclusions/source sections, their reduction assessments, history/167 and ATTEMPTS/028 contain no completed all-place application. Targeted Galois-prime-transitivity, completion and stable-one-pointed-Weierstrass searches located Milne ANT, Kedlaya and Hassett; complete essential statements and the Galois proof case were inspected as recorded below.
SOURCE_EVIDENCE: Milne Algebraic Number Theory v3.08 (19 July 2020), Theorem 3.34 and its Galois proof pp.59–60, section 8 and Propositions 8.1–8.2 pp.135–136; Kedlaya Introduction: the Tate curve (fall 2004), Theorems 1–2 pp.3–4; Hassett Moduli spaces of weighted pointed stable curves, arXiv:math/0205009v1 (1 May 2002), section 2 pp.2–3, ordinary weight-one definition. Reuse the native May 2020 definition/conventions assessment with its reproduction qualification, and L048's inspected integral Tate series/reduction sources.
COMPARISON: Known results cover transitivity of places, their completion interpretation, split Tate reduction over finite p-adic fields and the definition of a stable one-pointed family. The remaining work is the explicit application to the fixed Q-defined curve and its pointed integral cubic at every F-place; no general new transport or reduction theorem is needed.
GAP: Approve exactly TARGET for a separate research application. Verify transport fixes E_0 and its origin, and check the projective cubic is a flat proper nodal family with smooth marking and relatively ample dualizing sheaf plus marking; do not use the regular I_n polygon as the stable pointed fiber. No sufficient native initial data or finite B>=A follows from this coverage.
REASON: SPECIALIZE the inspected known results and definitions; retain the unchanged arithmetic inputs. The pointed-model checks are the identified specialization difference, to be written next turn rather than derived in this literature-only step. No reproof of Tate uniformization, Galois transitivity or stable reduction is justified.
LITERATURE_REASON: The native all-F-place quantifier and pointed-curve object are changed hypotheses outside the existing single-completion Tate specialization; approve these specific applicability bridges while reusing ready torsion and reduction coverage.
SCOPE: Exactly TARGET for the same E_0,F,u,H,N,Omega and fixed M; no reselection, enlargement, new twist, K-core construction, actual input/action or numerical comparison.

The main gap is original finite B>=A. The intermediate target tests one
native prerequisite at all lifts of the moduli place 3. A pass would
remove L050's conditional exposition stop as an obstacle to this native
reduction test, while leaving the actual initial-data and comparison
bridges open. A failure must name an actual F-place and the fixed
X_F there; an additive Q_3-descent is insufficient.

Essential inputs: L045,L048,L049; L050 is contrast only. Retain
L044–L047,L042 through those inputs; E_F=E_0 over
F=Q(zeta_60,E_0[30]), X_F=E_F minus its origin, the unchanged
embedded H,N packet, M>=max(M_tors,31), v_3(3)=1 and
v_3(q_0)=30, without q_0=3^30. Do not assume a full selected
place set or all remaining Definition 3.1 hypotheses.

The completed review below supplies the previously missing coverage.
The mathematical specialization remains a separate research step.

Continuation test: approve the unchanged-curve application if coverage
controls every place above 3 and the exact native curve meaning. If
essential coverage is inaccessible, park the dependent bridge and choose
an independently testable target; do not repeat the broad-model twist
audit. Any research verdict must leave K-coricity, the covering/cusp
and selected-place data, actual inputs/actions, pilot, essentiality and
finite B>=A unresolved. Preserve ATTEMPTS/022,025,026,027,028.
Full matching Mathlib coverage remains unchecked.

## Completed coverage review — 2026-10-12

### Transport input and inspected proof case

[Milne, Algebraic Number Theory v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 3.34, printed pp.59–60, treats the integral closure of a
Dedekind domain in a finite separable extension. Its Galois proof
establishes transitivity on primes above a given prime, using the
Chinese remainder theorem and the norm to exclude separate orbits.
The complete Galois case was read, including the contradiction at its end.
Section 8, pp.135–136, identifies extensions of valuations with
completion factors; Propositions 8.1–8.2 assume finite separability.
These are applicable inputs because L045 records finite Galois F/Q.
The next application must transport both coefficients and origin:
E_0 is Q-defined. An arbitrary F-defined curve would require a separate
conjugacy argument. Completion transport is abstract over Q_3; it must
not be reported as equality of all embeddings inside Omega.

### Local and pointed-model coverage

[Kedlaya, Introduction: the Tate curve](https://kskedlaya.org/18.727/tate-curve.pdf),
fall 2004, Theorem 1 p.3 and Theorem 2 p.4, were inspected.
The local field must be a finite extension of Q_p. The former theorem
requires |q|<1 and supplies the Tate equation and full pointwise
uniformization; the latter assumes |j(E)|>1 and characterizes a
K-isomorphism to its unique Tate curve by split multiplicative reduction.
The cited proof reference is Silverman V.5.3. Reuse L048's approved
integral-series and split-node sources rather than rediscover them.
No field extension is needed to establish the already recorded
Q_3-isomorphism; subsequent base change is the research application.

[Hassett, Moduli spaces of weighted pointed stable curves](https://arxiv.org/pdf/math/0205009v1),
1 May 2002, section 2 pp.2–3, defines a family over a noetherian base
as flat proper with connected nodal geometric fibers of fixed arithmetic
genus and marked sections. Stability requires the markings to be smooth,
the weight collision condition, and relative ampleness of the dualizing
divisor plus weighted sections. All weights one recover ordinary pointed
stability. Theorem 2.1's proper moduli stack is also stated there, but
properness alone would allow a finite extension and is not the intended
argument over F_t. No use of its substantial proof is proposed.

The approved specialization must check these hypotheses on the
projectivized original integral cubic with its infinity section,
or on the cited integral Tate model, after the prescribed transport.
In particular it must establish geometric nodality/connectedness,
flatness, the smooth marked section, and relative ampleness in genus
one. An irreducible nodal cubic and an I_n regular polygon describe
different models; the latter's unmarked components are not automatically
stable. This is an explicit application of the weight-one definition,
not an assertion that elliptic semistability alone has already proved
the exact pointed-model predicate. The output needed is the stable
pointed compactification of X_F, with its multiplicative special fiber;
no total-space regularity or new covering/cusp data is required by this
specific test.

The native curve terminology is reused from the completed
`2026-10-12-native-selected-place-model-comparison.md`, including its
May 2020 reproduced-source qualification and the inspected SemiAnbd
section 0 convention. Attempts to reload SemiAnbd pp.9–10 this turn
returned metadata or text errors; no additional claim is based on those
responses. The earlier complete reading remains the coverage input.
Two guessed Brown lecture-note endpoints and an Edinburgh survey
endpoint failed; they are neither essential inputs nor inspected results.
Stacks' unpointed stable-curve page and moduli example index do not
supply the needed genus-one pointed criterion and are not substitutes.
The precise Hassett definition supplies that criterion directly.

Queries included `site.jmilne.org ANT Galois acts transitively primes
lying over completions`, `semistable elliptic curve stable one pointed
curve nodal Weierstrass model identity`, and `stable pointed three
Definition curves Hassett`. Search snippets were leads only. Neither
these searches nor this comparison establishes novelty.

### Scope, discriminating test and Mathlib

Coverage is ready for exactly TARGET with inputs L045,L048,L049 and
L050 as contrast only. The direct proof may need only L045,L048;
L049's everywhere semistability cannot replace the multiplicative test.
A successful application closes this single native reduction prerequisite
above 3, leaving all independent initial-data, K-core, selected-place,
covering/cusp, actual input/action, pilot and essentiality obligations,
and the original finite B>=A gap. A negative application must exhibit
failure for the fixed X_F at an actual F-completion. Failure of a
Q_3-descent does not meet that test.

No mathematical application, new lemma or script was performed here.
Full matching Mathlib coverage remains unchecked. The next turn should
use this saved SPECIALIZE assessment and classify the known-method
application as REPRODUCTION, with full model checks in a canonical lemma
if the attempt succeeds. No further literature turn is needed for these
unchanged hypotheses.
