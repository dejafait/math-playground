# Proposed bounded exact-shift geometric test

TARGET: Test whether an even real quartic P with P(0)>0 and simple real roots outside [-40,40] can have P(a)=Re[P(a-2i)/(5/2+ia)]=0 at arbitrarily large a>40.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact/common-zero and shifted-xi search in 2026-10-07-actual-response-disjointness.md, supplemented by Hermite–Biehler real-rooted polynomial/shift/common-zero queries; no inspected theorem settles this pointwise quartic test.
SOURCE_EVIDENCE: Lagarias arXiv:math/0601653v2, Lemmas 2.1–2.2 pp. 4–7 and Theorem 2.1(1) with common-zero proof pp. 7–8, https://arxiv.org/pdf/math/0601653v2; precise hypotheses, complete relevant proof cases, source version and comparison are recorded in the parent assessment; local L018, L024 and L366 (1) inspected.
COMPARISON: The source compares complementary projections of the same shifted function; the proposed P and divided shifted real projection are different components. The strict modulus comparison does not by citation exclude their common zero, even when P has only simple real roots.
GAP: Decide the exact finite-degree pointwise inference with an unbounded prescribed height parameter; no example, universal exclusion or actual-family result has been proved.
REASON: Test the geometric mechanism suggested by the actual-disjointness review while retaining the exact shift and variable divisor, before attempting a product-based noncoincidence proof for actual xi.
SCOPE: Proposed comparison polynomials only, degree exactly four, even with real coefficients, P(0)>0 and all four roots real, simple and outside [-40,40]; arbitrarily large means a family with unbounded positive common-zero height, not infinitely many zeros of one polynomial. No D≤0, theta kernel, Euler product or Riemann–von Mangoldt count is required or asserted.

This is a newly written ready continuation proposal for separate supervisor
approval next turn. It records source scope and a proposed test only;
no mathematical construction has been performed in this literature turn.
The complete discovery/primary comparison is in
`drafts/literature/2026-10-07-actual-response-disjointness.md`.
No claim of originality follows from the bounded search. A later approved
research attempt may be classified REPRODUCTION or POTENTIALLY_NEW.

The main gap is global actual-theta mixed positivity and L367's total
signed margin. Actual eventual F_0/G disjointness is one additional
premise of L374, independent of D≤0 and signed arithmetic comparison.
The intermediate target here is a discriminating test of whether real
zero geometry and reflection alone support a pointwise exclusion.

The proposed model is explicitly defined by F_P(t)=2P(t) and
G_P(t)=−(t²+1/4)Re[P(t−2i)/(5/2+it)] for real t. These are target
definitions retaining the shift/divisor of L366, not identities asserted
for zeta or a newly derived lemma. If referring to a completion model,
define f_P(s)=P((s−1/2)/i) and justify its reflection/reality properties
in the later proof. Do not transfer P's real-rootedness to actual xi.

Essential context inputs are L018 (reflection and completion conventions),
L024 (paired product) and L366 (1) (actual response). They explain why
the model is tested; they are not mathematical premises proving a
polynomial example. L371/L373 preserve the arbitrary-pair common-zero
stops. This test differs by imposing the shift relationship; neither
historical example decides it. L368 and audited L374 provide downstream
motivation only. No cross-notebook theorem is proposed.

Continuation/abandonment test: give an exact parameterized quartic,
verify all four root locations, simplicity and P(0)>0, and check the
full divided projection at an unbounded set of parameter heights; or
prove exclusion for this precise quartic class. An example would stop
the pointwise geometry-only inference and require an actual arithmetic
input. Exclusion in degree four would justify considering a separately
reviewed larger-degree test, not an actual-family conclusion. Failure
to settle this bounded test is EXPLORATION or STALLED, not a theorem.

A finite polynomial obstruction cannot refute eventual disjointness
for each fixed polynomial: beyond its last zero the condition is vacuous.
The unbounded family would instead refute a universal pointwise claim
or an onset uniform over this geometric class. It supplies no actual
common zero, no discriminant sign and no RH counterexample. Full matching
Mathlib coverage is not checked; exact algebra needs no new scalar
theorem or reproof of Hermite–Biehler.
