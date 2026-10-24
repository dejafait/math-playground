# Section vanishing and the twisted Euler character — source approval

TARGET: Test whether L155's section vanishing and dual stability give a stronger split-count bound from L147's Euler character.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the five-query discovery and inspected theorem comparison in 2026-10-23-twisted-stable-summand-index-bound.md and the opposite-section assessments; scoped searches of the recent assessments/history and reads of L147/L153/L154/L155 and ATTEMPTS/087 identify no completed whole-Euler application of the independent L155 vanishing.
SOURCE_EVIDENCE: Reuse inspected Huybrechts, Lectures on K3 Surfaces, author draft, Chapter 1 (2.5)–(2.6)/Proposition 2.4 pp. 11–13, Chapter 9 (1.2)–(1.4) pp. 169–170, Section 3.1(iii)–(iv) pp. 175–176 and Theorem 4.9 p. 182; Perego (2021) Propositions 3.9–3.12 and 3.15 with proof pp. 36–38, as recorded in the ready assessments below. Fresh web reopening of the author PDF timed out; no fresh extraction is claimed or needed.
COMPARISON: General K3 RR, Serre duality, dual stability and equal-slope stable-Hom coverage already includes the proposed cohomology test on a locally free real-h-polystable bundle. L154 used these tools on numerical stable types without L155's independent whole-image section vanishing; the changed data-specific Euler application is not already a completed result.
GAP: In a separate research turn justify the passage from actual section vanishing through the stable decomposition to dual-section control, apply the whole Euler identity with its signed character, and compare the resulting necessary upper bound with 146; no bound or vanishing beyond L155 is derived in this source review.
REASON: Essential coverage matches this narrow specialization, so one REPRODUCTION proof attempt is ready without more browsing; no stable existence theorem, self-duality or new transform theorem is needed.
LITERATURE_REASON: The supplied REVIEW_REQUIRED gate concerns applying the newly audited independent section vanishing to the whole Euler character, outside the endpoint-only audit; this turn checks that scope while reusing adequate sources.
SCOPE: Same conditional equality F, original common g,h, preferred dual HE twist and actual locally free M as L147/L153/L155; only stable decomposition, section/dual-section control and whole-bundle Euler bookkeeping are approved, with all ranks, first classes, multiplicities and possibly empty Z retained.

## Gap, target and decision test

The main gap remains algebraic realization of arbitrary primitive rational
Hodge classes; neither this review nor the proposed necessary test closes it.
The intermediate target is a stronger upper restriction on the split set
of the same hypothetical equality kernel. Its plausible downstream use is
comparison with independent lower control, which is still absent.
Continue the test if the actual vanishing and covered decomposition give
a necessary upper bound strictly below 146. Otherwise preserve the compatible
range and park this particular cohomological test. No bound is calculated here.

## Primary coverage reused and applicability

The [stable-summand assessment](2026-10-23-twisted-stable-summand-index-bound.md)
records actual discovery queries and inspection of Daniel Huybrechts,
*Lectures on K3 Surfaces*, author-hosted prepublication draft,
[Chapter 9 (1.2)–(1.4), pp. 169–170](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=169).
These give the K3 Euler/Mukai formulas for arbitrary rank and determinant.
The [opposite-section audit assessment](2026-10-24-opposite-twisted-section-critical-audit.md)
records Chapter 1 (2.5)–(2.6)/Proposition 2.4, pp. 11–13 for RR and
Serre duality. The base here is a smooth projective K3 and M is locally
free, so coherent RR and Serre duality apply, with trivial canonical
bundle. L147's signed ordinary character and its absolute Euler check
are existing conditional local inputs, not fresh calculations of this turn.

Huybrechts, [Chapter 9 Section 3.1(iii)–(iv), pp. 175–176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
provides stable simplicity and dual stability for Kähler-class slope;
[Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
provides HE/polystable splitting. The inspected coverage explicitly uses
a real Kähler class. Audited L153 supplies its applicability to this
specific M at the original h, rather than a generic ample replacement.
Stable direct summands remain locally free and have slope zero; their
duals and the stable trivial line are within the covered Hom comparison.
The separate proof must explicitly handle the trivial isotypic part and
both directions of Hom before applying Serre duality. No equality
between M and its dual is needed or approved.

Reuse Arvid Perego, *Kobayashi–Hitchin corrispondence for twisted vector
bundles*, Complex Manifolds **8** (2021), 1–95,
[Propositions 3.9–3.12 and 3.15 with proof, pp. 36–38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36),
through the inspected proof records reused in the stable-summand and
opposite-section audit assessments. Ordinary bundles, trivial cocycle,
zero B-field and equal zero Einstein functions match the retained case.
These support the parallel-morphism/stable-Hom argument without a
rational-polarization assumption. Import these results by citation;
there is no reason to reprove them. A fresh attempt to reopen Huybrechts'
PDF returned a timeout; the recorded complete inspection makes that
nonessential access failure no source blocker.

## Duplicates, failures and boundary of approval

L154's canonical proof already uses section and dual-section tests for
individual nontrivial stable types. Its formal endpoint and
[ATTEMPTS/087](../../ATTEMPTS/087-twisted-stable-summand-endpoint.md)
retain sixteen trivial lines and did not have independent whole-image
cohomology. That stopped numerical filter is preserved. L155 adds
actual H^0(B,M)=0 by an opposite-image comparison, and its separate
audit checks that fact while explicitly declining the present whole-Euler
optimization. Thus the saved continuation uses an additional established
input rather than repeating the stopped single-image test.

The whole-base twisted odd-IT failure recorded in the opposite-section
assessment remains binding evidence: W must remain in derived degree two.
The proposed test is on the actual ordinary bundle M, not a declaration
that the full twisted pushforward is concentrated. Opposite-image
acyclicity must not be transferred to M. No claim that M is simple,
self-dual or acyclic is licensed. In particular, a necessary Euler sign
is not an existence or vanishing theorem for all its cohomology.

Continuation inputs are L071's conditional equality data, L147's actual
M and full signed character, audited L153's same-h polystability,
audited L155's section vanishing and L154's prior bound/comparison.
Retain identical marked factors/common g,h, locally free rank-two
Omega-polystable F, integral c_1=0 and ch_2=-14e_1-21e_2-tau_D,
k=(-4,-2,1,2), k^2=-14eta, k.h=0, integral eta=1, and finite possibly
empty Z. F, nonempty Z, independent lower control, reconstruction and
transport remain unproved. No cross-notebook input is used.

Full matching Mathlib coverage is not checked; unknown availability is
not evidence of absence. This is EXPLORATION / LITERATURE / REPRODUCTION:
a completed changed-scope source comparison, with no new mathematical
result or originality claim. No lemma, mathematical script, DAG edge or
argument overview is changed. The exact TARGET is ready for the next
research turn; further literature needs a new essential reason.
