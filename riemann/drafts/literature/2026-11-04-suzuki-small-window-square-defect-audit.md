# Approved coverage: critical audit of the small-window square defect

TARGET: Critically audit L739's complete-kernel remainder and negative small-window square-defect witness, including the arithmetic cutoff, normalization, self-adjoint composition and existential onset.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior exact-target/composition searches and checked L739, the parameter-descent assessment, the square-order stop and step-267 history. Reopened the primary PDF at the specific imported statements and relevant proof cases; no new target or originality claim.
SOURCE_EVIDENCE: Independently reopened Suzuki arXiv:1907.07302v2 (6 March 2020), (1.1),(1.10), Theorem 1.2, (1.11),(1.13), Propositions 3.1–3.2 and relevant proof cases (3.8)–(3.10),(3.13), printed pp.1–3,5–7; read full L739 and the needed L018/L618 setup/support passages.
COMPARISON: These primary formulas supply all imported inputs for the existing fixed-parameter calculation. The audit must verify L739's uniform remainder and ordinary integral/Hilbert-space specialization; it must not reprove Suzuki's kernel construction or replay L618's large-parameter norm bound.
GAP: L739 has a full informal proof but no separate critical audit. Check every remainder order and coefficient, including the stronger Proposition 3.2 remainder despite the weaker printed proof display, and check that the witness concerns the actual compressed operator squares.
REASON: An independently checked negative witness decides whether the proposed sufficient square-order mechanism is available; a coefficient or support mistake could invalidate the stop. This is a bounded audit of a known-source specialization, not a new central-gap mechanism.
SCOPE: Only L739 at theta=2,4, t tending to zero from above, f_t=1_[-t,t]/sqrt(2t) in the original unweighted L2 space. No parameter/vector sweep, numerical onset, new order theorem, global contractivity implication, determinant equivalence or Xi sign claim.

The separate literature-only approval was completed in step 268.
SPECIALIZE coverage is ready for the exact TARGET above; this is not
a mathematical audit result. The prior calculation and its unaudited
status are preserved. No lemma or mathematical script was changed.
LITERATURE_REASON: The supervisor required separate approval of the newly nominated audit coverage; this step checks its essential source scope, not a fresh search for an unchanged target.

## Exact evidence to replay

The [primary source](https://arxiv.org/pdf/1907.07302v2) gives the
auxiliary asymptotic in Proposition 3.2 on printed p.6. Its Volterra
formula (3.8), near-zero bound from Proposition 3.1 on p.5, and
(3.9)–(3.10) support the stronger remainder used in the calculation;
the audit must inspect this use rather than substitute the weaker
additive O(x) display. Formula (3.13), p.7, retains both exponentials,
the factor 4 theta pi^theta and the removable Bessel quotient.
Equations (1.11),(1.13), p.3, give the arithmetic normalization and
causal sum. These are inspected theorem-level inputs, not unread leads.

Essential local inputs are L018 and L618. In L618 only its hypotheses
and compact-square support reduction are needed. Read L739 in full;
check its finite remainder constants, integration of the normalized
vector, cross term and remainder-square powers, coefficients
64 pi^4/5 and 1024 pi^8/81, and the positive existential onset.
Any correction must remain within these covered hypotheses; a new
mechanism or strengthened conclusion needs its own assessment.

Pass only if a fixed finite error constant bounds the defect by a
strictly negative quantity on an entire positive interval ending at
zero. Otherwise preserve the error and weaken or retract exactly the
unsupported part. Either result leaves actual-Xi mixed positivity,
all-window control and the bare contractivity implication unresolved.
Mathlib coverage is unknown; no availability claim is needed to audit
the informal proof. Recommended routing: proof_audit/routine_audit,
standard/high.

## Source-scope approval, step 268

Theorem 1.2 applies for theta>1; the auxiliary propositions assume
theta>0. Thus both cover the fixed parameters 2 and 4. The source
provides reality, continuity and causality without RH. Its arithmetic
formula includes n^(-1/2), while (3.13) retains both exponentials and
the Bessel quotient. The exact printed formulas agree with the
nomination's source descriptions.

Proposition 3.2 states the stronger O(x^theta) remainder. The proof's
weaker additive O(x) display must not be used alone at theta=4.
Proposition 3.1 explicitly supplies a near-zero bound; (3.8) and
(3.9) are available for the local verification already proposed in
L739. No strengthening is established by this approval.

The source does not certify L739's norm coefficients, error constants,
compressed self-adjoint composition or positive onset. Those remain
the next audit's obligations. Its pass/fail test and scope above are
unchanged. No full matching square-order theorem was located in the
reused assessment; this is not evidence of novelty. Mathlib coverage
remains unchecked.
